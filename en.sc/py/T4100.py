from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4100_1 ._SN',
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
        'Olivier',                              # 9
        'Renne',                                # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Soldier',                              # 30
        'Elnan',                                # 31
        'Vanguard',                             # 32
        'Vanguard',                             # 33
        'Pale Apache',                          # 34
        'Gaspard',                              # 35
        'Nonna',                                # 36
        'Dick',                                 # 37
        'Raleigh',                              # 38
        'Troy',                                 # 39
        'Berden',                               # 40
        'Latanya',                              # 41
        'Tran',                                 # 42
        'Royal Army Soldier',                   # 43
        'Royal Army Soldier',                   # 44
        'Tabasa',                               # 45
        'Sammy',                                # 46
        'Jane',                                 # 47
        'Deitus',                               # 48
        'Grancel - North Block',                # 49
        'Royal Avenue',                         # 50
        'Grancel - East Block',                 # 51
        'Grancel - West Block',                 # 52
        '',                                     # 53
        '',                                     # 54
        '',                                     # 55
        '',                                     # 56
        '',                                     # 57
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
        'ED6_DT07/CH00030 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT06/CH20043 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01160 ._CH',             # 05
        'ED6_DT07/CH01470 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01640 ._CH',             # 0B
        'ED6_DT27/CH04610 ._CH',             # 0C
        'ED6_DT27/CH04611 ._CH',             # 0D
        'ED6_DT27/CH04620 ._CH',             # 0E
        'ED6_DT27/CH04621 ._CH',             # 0F
        'ED6_DT29/CH12570 ._CH',             # 10
        'ED6_DT29/CH12571 ._CH',             # 11
        'ED6_DT29/CH12350 ._CH',             # 12
        'ED6_DT29/CH12351 ._CH',             # 13
        'ED6_DT29/CH12320 ._CH',             # 14
        'ED6_DT29/CH12321 ._CH',             # 15
        'ED6_DT07/CH01130 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
        'ED6_DT07/CH01150 ._CH',             # 18
        'ED6_DT07/CH01120 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH00030P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT06/CH20043P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01160P._CP',             # 05
        'ED6_DT07/CH01470P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01640P._CP',             # 0B
        'ED6_DT27/CH04610P._CP',             # 0C
        'ED6_DT27/CH04611P._CP',             # 0D
        'ED6_DT27/CH04620P._CP',             # 0E
        'ED6_DT27/CH04621P._CP',             # 0F
        'ED6_DT29/CH12570P._CP',             # 10
        'ED6_DT29/CH12571P._CP',             # 11
        'ED6_DT29/CH12350P._CP',             # 12
        'ED6_DT29/CH12351P._CP',             # 13
        'ED6_DT29/CH12320P._CP',             # 14
        'ED6_DT29/CH12321P._CP',             # 15
        'ED6_DT07/CH01130P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
        'ED6_DT07/CH01150P._CP',             # 18
        'ED6_DT07/CH01120P._CP',             # 19
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5720,
        Z                   = 0,
        Y                   = -36280,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -840,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 710,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -90,
        Z                   = 0,
        Y                   = -51500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -9390,
        Z                   = 250,
        Y                   = -6510,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8060,
        Z                   = 250,
        Y                   = 5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8060,
        Z                   = 250,
        Y                   = 4120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 5990,
        Z                   = 0,
        Y                   = -7440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
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
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
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
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
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
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
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


    DeclMonster(
        X                   = -430,
        Z                   = 0,
        Y                   = -39050,
        Unknown_0C          = 180,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x549,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17930,
        Z                   = 0,
        Y                   = -20130,
        Unknown_0C          = 180,
        Unknown_0E          = 20,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x54A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5660,
        Z                   = 0,
        Y                   = -1440,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x547,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21340,
        Z                   = 0,
        Y                   = -230,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x546,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13570,
        Z                   = 250,
        Y                   = -51100,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x548,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -5000,
        Y                   = -2000,
        Z                   = -65600,
        Range               = 5000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0344,
        Unknown_18          = 0x0,
        Unknown_1C          = 53,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 63,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 64,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 65,
    )


    DeclActor(
        TriggerX            = 9620,
        TriggerZ            = 500,
        TriggerY            = -25020,
        TriggerRange        = 800,
        ActorX              = 9620,
        ActorZ              = 1500,
        ActorY              = -25020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23690,
        TriggerZ            = 500,
        TriggerY            = -7620,
        TriggerRange        = 800,
        ActorX              = 23690,
        ActorZ              = 1500,
        ActorY              = -7620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16040,
        TriggerZ            = 500,
        TriggerY            = 6640,
        TriggerRange        = 800,
        ActorX              = 16040,
        ActorZ              = 1500,
        ActorY              = 6640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12480,
        TriggerZ            = 500,
        TriggerY            = -2460,
        TriggerRange        = 800,
        ActorX              = -12480,
        ActorZ              = 1500,
        ActorY              = -2460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10640,
        TriggerZ            = 500,
        TriggerY            = -11060,
        TriggerRange        = 800,
        ActorX              = -10640,
        ActorZ              = 1500,
        ActorY              = -11060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14870,
        TriggerZ            = 500,
        TriggerY            = -15350,
        TriggerRange        = 800,
        ActorX              = -14870,
        ActorZ              = 1500,
        ActorY              = -15350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10680,
        TriggerZ            = 500,
        TriggerY            = -29970,
        TriggerRange        = 800,
        ActorX              = -10680,
        ActorZ              = 1500,
        ActorY              = -29970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30,
        TriggerZ            = 300,
        TriggerY            = -43060,
        TriggerRange        = 800,
        ActorX              = -30,
        ActorZ              = 4300,
        ActorY              = -46060,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_986",          # 00, 0
        "Function_1_B2E",          # 01, 1
        "Function_2_CAF",          # 02, 2
        "Function_3_E2C",          # 03, 3
        "Function_4_E50",          # 04, 4
        "Function_5_EAD",          # 05, 5
        "Function_6_F3A",          # 06, 6
        "Function_7_FA9",          # 07, 7
        "Function_8_1018",         # 08, 8
        "Function_9_103C",         # 09, 9
        "Function_10_1778",        # 0A, 10
        "Function_11_1CF6",        # 0B, 11
        "Function_12_2529",        # 0C, 12
        "Function_13_28DE",        # 0D, 13
        "Function_14_2BD4",        # 0E, 14
        "Function_15_3934",        # 0F, 15
        "Function_16_412C",        # 10, 16
        "Function_17_46F7",        # 11, 17
        "Function_18_496C",        # 12, 18
        "Function_19_4C17",        # 13, 19
        "Function_20_4EBA",        # 14, 20
        "Function_21_5120",        # 15, 21
        "Function_22_53E2",        # 16, 22
        "Function_23_577C",        # 17, 23
        "Function_24_5C08",        # 18, 24
        "Function_25_5FBF",        # 19, 25
        "Function_26_6420",        # 1A, 26
        "Function_27_6452",        # 1B, 27
        "Function_28_6484",        # 1C, 28
        "Function_29_64B6",        # 1D, 29
        "Function_30_652B",        # 1E, 30
        "Function_31_6537",        # 1F, 31
        "Function_32_77F5",        # 20, 32
        "Function_33_781A",        # 21, 33
        "Function_34_785E",        # 22, 34
        "Function_35_78A2",        # 23, 35
        "Function_36_78D2",        # 24, 36
        "Function_37_7902",        # 25, 37
        "Function_38_7932",        # 26, 38
        "Function_39_7962",        # 27, 39
        "Function_40_7D4A",        # 28, 40
        "Function_41_7F8A",        # 29, 41
        "Function_42_84FA",        # 2A, 42
        "Function_43_8979",        # 2B, 43
        "Function_44_89A7",        # 2C, 44
        "Function_45_89D2",        # 2D, 45
        "Function_46_92C9",        # 2E, 46
        "Function_47_930B",        # 2F, 47
        "Function_48_96B9",        # 30, 48
        "Function_49_9A67",        # 31, 49
        "Function_50_9AFF",        # 32, 50
        "Function_51_9B80",        # 33, 51
        "Function_52_9BF9",        # 34, 52
        "Function_53_9C52",        # 35, 53
        "Function_54_A5F4",        # 36, 54
        "Function_55_A614",        # 37, 55
        "Function_56_A634",        # 38, 56
        "Function_57_A6BB",        # 39, 57
        "Function_58_A742",        # 3A, 58
        "Function_59_A762",        # 3B, 59
        "Function_60_A782",        # 3C, 60
        "Function_61_AD62",        # 3D, 61
        "Function_62_AD66",        # 3E, 62
        "Function_63_AD6A",        # 3F, 63
        "Function_64_AD6E",        # 40, 64
        "Function_65_AD72",        # 41, 65
    )


    def Function_0_986(): pass

    label("Function_0_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_9D0")
    Call(0, 40)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    Jump("loc_A5A")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9E4")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_9F8")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_A0C")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_A5A")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2E")
    Jump("loc_A5A")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A38")
    Jump("loc_A5A")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_A5A")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_A5A")
    SetChrPos(0x26, 16000, 250, 4030, 0)

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A81")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A9A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_A2(0x161A)
    Event(0, 24)
    Jump("loc_B2D")

    label("loc_A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_AB3")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_A2(0x162D)
    Event(0, 25)
    Jump("loc_B2D")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_AC9")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_B2D")

    label("loc_AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_AE8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_B2D")

    label("loc_AE8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_AF4"),
        (SWITCH_DEFAULT, "loc_B2D"),
    )


    label("loc_AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B15")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 42)
    Jump("loc_B2A")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2A")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_B2A")

    Jump("loc_B2D")

    label("loc_B2D")

    Return()

    # Function_0_986 end

    def Function_1_B2E(): pass

    label("Function_1_B2E")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_51(0x35, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_B1("t4100_y")
    Jump("loc_B74")

    label("loc_B6B")

    OP_B1("t4100_n")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_BC6")
    OP_72(0x0, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x10, 0x10)
    OP_1B(0x9, 0x0, 0x30)
    OP_1B(0xA, 0x0, 0x2F)
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 41)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_BE4")

    label("loc_BC6")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_B5(0x0)

    label("loc_BE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x54F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    OP_1B(0x9, 0x0, 0x3B)
    OP_1B(0xA, 0x0, 0x3A)
    OP_1B(0xB, 0x0, 0x37)
    OP_1B(0xC, 0x0, 0x38)
    OP_1B(0xD, 0x0, 0x37)
    OP_1B(0xE, 0x0, 0x39)
    Jump("loc_C53")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C53")
    OP_1B(0x9, 0x0, 0x3B)
    OP_1B(0xA, 0x0, 0x3A)
    OP_1B(0xB, 0x0, 0x37)
    OP_1B(0xC, 0x0, 0x38)
    OP_1B(0xD, 0x0, 0x37)
    OP_1B(0xE, 0x0, 0x39)
    Jump("loc_C53")

    label("loc_C53")

    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    OP_65(0x7, 0x1)

    label("loc_C77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C92")
    OP_82(0x84, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    Jump("loc_CAE")

    label("loc_C92")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4A70, 0x7D0, 0x3A98, 0x64, 0x0)

    label("loc_CAE")

    Return()

    # Function_1_B2E end

    def Function_2_CAF(): pass

    label("Function_2_CAF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E16")

    label("loc_CD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CED")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E16")

    label("loc_CED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D06")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E16")

    label("loc_D06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E16")

    label("loc_D1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D38")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E16")

    label("loc_D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D51")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E16")

    label("loc_D51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E16")

    label("loc_D6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D83")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E16")

    label("loc_D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E16")

    label("loc_D9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E16")

    label("loc_DB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E16")

    label("loc_DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E16")

    label("loc_DE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E00")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E16")

    label("loc_E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E2B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E16")

    label("loc_E2B")

    Return()

    # Function_2_CAF end

    def Function_3_E2C(): pass

    label("Function_3_E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4F")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_E2C")

    label("loc_E4F")

    Return()

    # Function_3_E2C end

    def Function_4_E50(): pass

    label("Function_4_E50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAC")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_E50")

    label("loc_EAC")

    Return()

    # Function_4_E50 end

    def Function_5_EAD(): pass

    label("Function_5_EAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F39")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_EAD")

    label("loc_F39")

    Return()

    # Function_5_EAD end

    def Function_6_F3A(): pass

    label("Function_6_F3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FA8")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_6_F3A")

    label("loc_FA8")

    Return()

    # Function_6_F3A end

    def Function_7_FA9(): pass

    label("Function_7_FA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1017")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_7_FA9")

    label("loc_1017")

    Return()

    # Function_7_FA9 end

    def Function_8_1018(): pass

    label("Function_8_1018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_103B")
    OP_8D(0xFE, -9540, -8220, -7490, -4270, 2000)
    Jump("Function_8_1018")

    label("loc_103B")

    Return()

    # Function_8_1018 end

    def Function_9_103C(): pass

    label("Function_9_103C")

    TalkBegin(0xFE)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1059")
    OP_A9(0xD6)
    TalkEnd(0xFE)
    Return()

    label("loc_1059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106A")
    TalkEnd(0xFE)
    Return()

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1074")
    Jump("loc_1774")

    label("loc_1074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1163")

    ChrTalk(    #0
        0xFE,
        (
            "I'm learning how to make popcorn over\x01",
            "an open flame like we used to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Haha. I'm usually pretty unlucky,\x01",
            "so I'm used to trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I'm sure things'll go back to normal someday,\x01",
            "so we just gotta get through the now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_1163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1248")

    ChrTalk(    #3
        0xFE,
        (
            "Yesterday, when I went to stock up,\x01",
            "I was able to buy popcorn ingredients\x01",
            "super cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Machines might be busted, but\x01",
            "the sit has got its upsides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'm glad I'm thinking positively like the\x01",
            "father said to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_1248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #6
        0xFE,
        "The popcorn machine broke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Er, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'm sure this is a message from the Goddess\x01",
            "telling me to not worry about selling and just\x01",
            "go stock up!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1343")

    label("loc_12FB")


    ChrTalk(    #9
        0xFE,
        (
            "Gotta think positive, gotta think positive...\x01",
            "*mutter* *mutter*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1343")

    Jump("loc_1774")

    label("loc_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1387")

    ChrTalk(    #10
        0xFE,
        (
            "Huh? That's odd...\x01",
            "The machines aren't working...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C2")

    ChrTalk(    #11
        0xFE,
        (
            "I went and talked to someone at the\x01",
            "church about my troubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Bishop Reval was kind enough\x01",
            "to hear me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "He said that even when bad things\x01",
            "happen, I should stay as positive as\x01",
            "I can in how I look at things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "All right, time to put that into\x01",
            "practice starting tomorrow!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1570")

    label("loc_14C2")


    ChrTalk(    #15
        0xFE,
        (
            "I went and talked to someone at the\x01",
            "church about my troubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "He said that even when bad things\x01",
            "happen, I should stay as positive as\x01",
            "I can in how I look at things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1570")

    Jump("loc_1774")

    label("loc_1573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1638")

    ChrTalk(    #17
        0xFE,
        (
            "*sigh* I forgot the money I set\x01",
            "aside for change at home today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "That caused a bit of trouble for my customers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Yeah, my life has been nothing but a\x01",
            "parade of misfortune.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_1638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_170F")

    ChrTalk(    #20
        0xFE,
        (
            "My life has been nothing but a\x01",
            "parade of misfortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "My stand broke during the Birthday Celebration,\x01",
            "my sales aren't going anywhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Maybe I should go get exorcised\x01",
            "at the Septian Church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1774")

    ChrTalk(    #23
        0xFE,
        "Hey, welcome to the capital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Why not have some popcorn while you're\x01",
            "taking a break?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1774")

    TalkEnd(0xFE)
    Return()

    # Function_9_103C end

    def Function_10_1778(): pass

    label("Function_10_1778")

    TalkBegin(0xFE)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1795")
    OP_A9(0xD5)
    TalkEnd(0xFE)
    Return()

    label("loc_1795")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A6")
    TalkEnd(0xFE)
    Return()

    label("loc_17A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_17B0")
    Jump("loc_1CF2")

    label("loc_17B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_187A")

    ChrTalk(    #25
        0xFE,
        (
            "Apparently, someone's moved into\x01",
            "the open house I was thinking of renting\x01",
            "in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Seems he's going to run a shop,\x01",
            "but that old guy is just plain suspicious\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_187A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_19C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1979")

    ChrTalk(    #27
        0xFE,
        (
            "There was an open house in the West Block,\x01",
            "but it seems someone's already snapped it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "It's a bit frustrating, but seems like\x01",
            "there was an incident there yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I'll just assume it wasn't meant to be\x01",
            "and give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_19C2")

    label("loc_1979")


    ChrTalk(    #30
        0xFE,
        (
            "Still, I wonder what kind of person's\x01",
            "renting out that empty house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C2")

    Jump("loc_1CF2")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1A21")

    ChrTalk(    #31
        0xFE,
        "What's wrong? Why are you looking around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Looking for someone, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1AB5")

    ChrTalk(    #33
        0xFE,
        (
            "There's a house that's been empty for\x01",
            "a while in the West Block...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I might be able to rent that with\x01",
            "the money I have saved up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B7B")

    ChrTalk(    #35
        0xFE,
        (
            "I've been working part time since before\x01",
            "the Birthday Celebration, so I have a fair\x01",
            "amount of money saved up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Maybe I should start seriously thinking\x01",
            "about living on my own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(    #37
        0xFE,
        "Welcome. How about a delicious crepe?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(    #38
        0xFE,
        "A Royal Army bigwig passed by a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "He was wearing a military uniform, but he\x01",
            "seemed like a very gentle person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "Just like a kindly dad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1CF2")

    ChrTalk(    #41
        0xFE,
        (
            "This is the center of Liberl,\x01",
            "the royal capital, Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We might've had a coup d'etat not too\x01",
            "long ago, but it's all back to normal now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF2")

    TalkEnd(0xFE)
    Return()

    # Function_10_1778 end

    def Function_11_1CF6(): pass

    label("Function_11_1CF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1D03")
    Jump("loc_2525")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D6F")

    ChrTalk(    #43
        0xFE,
        "...Talk about inconvenient...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "It's so dark at night that I can't even go\x01",
            "to the toilet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2525")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1DE3")

    ChrTalk(    #45
        0xFE,
        (
            "Yesterday, the Royal Guard fought some\x01",
            "giant tank at the harbor, apparently!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Pretty cool, huh?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2525")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E27")

    ChrTalk(    #47
        0xFE,
        "Huh... That bratty girl isn't here today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E74")

    label("loc_1E27")


    ChrTalk(    #48
        0xFE,
        "*siiigh* Isn't there anything fun to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Today is sooooo boring...\x02",
    )

    CloseMessageWindow()

    label("loc_1E74")

    Jump("loc_2525")

    label("loc_1E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_END)), "loc_1EE9")
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #50
        0xFE,
        "H-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12F,
        "#260FWho are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "W-We talked the other day, for cryin' out loud!\x02",
    )

    CloseMessageWindow()
    Jump("loc_215F")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E2")
    TurnDirection(0x24, 0x12F, 0)

    ChrTalk(    #53
        0xFE,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "H-Hey, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "You, in the white!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12F,
        "#264F...Do you mean me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Y-Yeah, you. Aren't you gonna come say hi?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12F,
        "#264FOh? Why do I have to say hello to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Everyone who comes to this town\x01",
            "has to come say hi to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12F,
        (
            "#267FHmm...\x02\x03",

            "#263FI don't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "Wh-What did you--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12F,
        (
            "#263FAfter all, my papa said a gentleman\x01",
            "always introduces himself first.\x02\x03",

            "#260FI don't want to be friends with someone\x01",
            "who doesn't practice common courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Gh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1650)
    Jump("loc_215F")

    label("loc_20E2")

    TurnDirection(0x12F, 0xFE, 0)

    ChrTalk(    #64
        0x12F,
        "#260F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #65
        0xFE,
        "Wh-What are you starin' at me for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Fine, I'll let you off for today.\x01",
            "You can go away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215F")

    Jump("loc_2525")

    label("loc_2162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D5")

    ChrTalk(    #67
        0xFE,
        "Ahh, I'm huuuuungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I better get home soon or Mom's gonna\x01",
            "smack me upside the head again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2525")

    label("loc_21D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_224E")

    ChrTalk(    #69
        0xFE,
        (
            "Is that 'non-aggresshon pakte' some\x01",
            "kinda medicine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "One way or another, it doesn't sound\x01",
            "very yummy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2525")

    label("loc_224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_24D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2455")
    TurnDirection(0x24, 0x12F, 0)

    ChrTalk(    #71
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "H-Hey, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "You, in the white!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x24, 400)

    ChrTalk(    #74
        0x12F,
        "#264F...Do you mean me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Y-Yeah, you. Aren't you gonna come say hi?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12F,
        "#264FOh? Why do I have to say hello to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Everyone who comes to this town\x01",
            "has to come say hi to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12F,
        (
            "#267FHmm...\x02\x03",

            "#263FI don't want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Wh-What did you--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12F,
        (
            "#263FAfter all, my papa said a gentleman\x01",
            "always introduces himself first.\x02\x03",

            "#260FI don't want to be friends with someone\x01",
            "who doesn't practice common courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Gh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164F)
    Jump("loc_24D2")

    label("loc_2455")

    TurnDirection(0x12F, 0x24, 400)

    ChrTalk(    #82
        0x12F,
        "#260F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x12F, 400)

    ChrTalk(    #83
        0xFE,
        "Wh-What are you starin' at me for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Fine, I'll let you off for today.\x01",
            "You can go away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D2")

    Jump("loc_2525")

    label("loc_24D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2525")

    ChrTalk(    #85
        0xFE,
        "...Troy's late. Again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "I wanna get out to the harbor and play!\x02",
    )

    CloseMessageWindow()

    label("loc_2525")

    TalkEnd(0xFE)
    Return()

    # Function_11_1CF6 end

    def Function_12_2529(): pass

    label("Function_12_2529")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2536")
    Jump("loc_28DA")

    label("loc_2536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(    #87
        0xFE,
        (
            "Dick's a scaredy cat who can't even\x01",
            "go to the toilet on his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "So, it's not really any different from normal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_262E")

    ChrTalk(    #89
        0xFE,
        (
            "I heard that a number of the Intelligence Division\x01",
            "people were captured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "This is huge deal...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_262E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_26A3")

    ChrTalk(    #91
        0xFE,
        "I like calm, quiet days like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "With days this pleasant,\x01",
            "I can spend my time deep\x01",
            "in thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_26A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_26F2")

    ChrTalk(    #93
        0xFE,
        (
            "The likelihood that Dick's heart rate\x01",
            "is increasing is...96.7%.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_26F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2722")

    ChrTalk(    #94
        0xFE,
        "Today is about up, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2755")

    ChrTalk(    #95
        0xFE,
        "I'm a little embarrassed, you guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28DA")

    label("loc_2755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2830")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279D")

    ChrTalk(    #96
        0xFE,
        (
            "Just as I thought, Troy was getting\x01",
            "sidetracked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_279D")


    ChrTalk(    #97
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "The likelihood that Dick's love at first sight\x01",
            "will end in a broken heart is...99.7%.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "...He's rather clumsy, emotionally.\x02",
    )

    CloseMessageWindow()

    label("loc_282D")

    Jump("loc_28DA")

    label("loc_2830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_28DA")

    ChrTalk(    #100
        0xFE,
        (
            "The likelihood Troy will be late\x01",
            "for our agreed time is...83%.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "He's always getting sidetracked by\x01",
            "something. Not like it's gonna be any\x01",
            "different today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DA")

    TalkEnd(0xFE)
    Return()

    # Function_12_2529 end

    def Function_13_28DE(): pass

    label("Function_13_28DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_28EB")
    Jump("loc_2BD0")

    label("loc_28EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2947")

    ChrTalk(    #102
        0xFE,
        (
            "The night is soooo dark that\x01",
            "you can see lots of stars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "It's so pretty!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_29D7")

    ChrTalk(    #104
        0xFE,
        (
            "Yesterday, I heard something really\x01",
            "loud over by the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "All the lights suddenly went out,\x01",
            "too. I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_29D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2A52")

    ChrTalk(    #106
        0xFE,
        "Ahhhhh, I wanna eat some ice cream...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Did you know? The ice cream in\x01",
            "the South Block is reeeally good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2AB7")

    ChrTalk(    #108
        0xFE,
        (
            "Dick's always trying to show off,\x01",
            "but he gets reeeally nervous when\x01",
            "girls are around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF3")

    ChrTalk(    #109
        0xFE,
        "I'm staaaaarving. I gotta get home soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2B33")

    ChrTalk(    #110
        0xFE,
        (
            "I'd rather it was something tasty,\x01",
            "not medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2B5D")

    ChrTalk(    #111
        0xFE,
        "Ahaha... Oops. Late again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2BD0")

    ChrTalk(    #112
        0xFE,
        "Mmmmm, it smells so gooood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Huh? I feel like I said I'd do something...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Hmm, what was it...?\x02",
    )

    CloseMessageWindow()

    label("loc_2BD0")

    TalkEnd(0xFE)
    Return()

    # Function_13_28DE end

    def Function_14_2BD4(): pass

    label("Function_14_2BD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2BE1")
    Jump("loc_3930")

    label("loc_2BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CB9")

    ChrTalk(    #115
        0xFE,
        (
            "Tom, the repair guy over at the factory,\x01",
            "is a real trustworthy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "If he says it's not a malfunction,\x01",
            "I believe him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Zacharias thinks they're trying to make him\x01",
            "buy new model units. Heh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3930")

    label("loc_2CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2DAC")

    ChrTalk(    #118
        0xFE,
        (
            "Is it true that Captain Amalthea, formerly of\x01",
            "the Intelligence Division, started an armed\x01",
            "uprising?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Apparently, the harbor's a helluva mess\x01",
            "thanks to their orbal tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "I hope it doesn't affect the non-aggression pact.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3930")

    label("loc_2DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F08")

    ChrTalk(    #121
        0xFE,
        (
            "Both Duke Dunan and Princess Klaudia\x01",
            "are candidates for the throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I wonder who Queen Alicia will choose\x01",
            "as her successor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Personally, I think Princess Klaudia'd be\x01",
            "good choice, though that's not based on\x01",
            "anything solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "To be honest, I actually don't know that\x01",
            "much about her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F02")

    ChrTalk(    #125
        0x105,
        "#042F...\x02",
    )

    CloseMessageWindow()

    label("loc_2F02")

    OP_A2(0x3)
    Jump("loc_2F78")

    label("loc_2F08")


    ChrTalk(    #126
        0xFE,
        (
            "I actually don't know that much about\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "I guess all I know is...that she's beautiful?\x02",
    )

    CloseMessageWindow()

    label("loc_2F78")

    Jump("loc_3930")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3074")

    ChrTalk(    #128
        0xFE,
        (
            "There's no shortage of citizens who'd\x01",
            "like to see Colonel Richard return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "That's just how charismatic he was,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Even I felt a little empty without him at\x01",
            "one point. He's just got a way about him,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3126")

    label("loc_3074")


    ChrTalk(    #131
        0xFE,
        (
            "There's no shortage of citizens who'd\x01",
            "like to see Colonel Richard return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Even I felt a little empty without him at\x01",
            "one point. He's just got a way about him,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3126")

    Jump("loc_3930")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3205")

    ChrTalk(    #133
        0xFE,
        (
            "There're always lights on at the\x01",
            "Liberl News in the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Those guys are at it day and night...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "It's such a familiar sight that the folks here\x01",
            "call the West Block the 'nightless city.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3930")

    label("loc_3205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_34C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3392")

    ChrTalk(    #136
        0xFE,
        (
            "If you're lost, you can just ask me.\x01",
            "I'm a born and bred Grancel boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "The Calvardian embassy's in the south end of\x01",
            "the East Block, and the Erebonian embassy's\x01",
            "straight north of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Grancel Castle is even farther north of\x01",
            "the North Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "The Liberl News is in the south part of the\x01",
            "West Block. The roads are pretty narrow,\x01",
            "so make sure you don't get lost.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_34BF")

    label("loc_3392")


    ChrTalk(    #140
        0xFE,
        (
            "The Calvardian embassy's in the south end of\x01",
            "the East Block, and the Erebonian embassy's\x01",
            "straight north of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Grancel Castle is even farther north of\x01",
            "the North Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "The Liberl News is in the south part of the\x01",
            "West Block. The roads are pretty narrow,\x01",
            "so make sure you don't get lost.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BF")

    Jump("loc_3930")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_366F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D1")

    ChrTalk(    #143
        0xFE,
        (
            "There's a pretty complex sewer system\x01",
            "here in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "A number of passages used for maintenance\x01",
            "are scattered about the city, so you can\x01",
            "probably go in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Rumor has it it's full of monsters, though,\x01",
            "so I can't say I recommend it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_366C")

    label("loc_35D1")


    ChrTalk(    #146
        0xFE,
        (
            "The sewers are full of monsters,\x01",
            "so you shouldn't go in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "The only people who go in are those crazy\x01",
            "bracer-types on extermination missions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366C")

    Jump("loc_3930")

    label("loc_366F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389F")

    ChrTalk(    #148
        0xFE,
        (
            "The South Block here has the Bracer Guild\x01",
            "and lots of shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "The North Block has the kingdom's\x01",
            "largest hotel, and further north of that\x01",
            "is Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "The West Block's known for the\x01",
            "Liberl News and the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "And the East Block's got embassies from\x01",
            "neighboring countries, the Grand Arena,\x01",
            "and a department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Right, right, I forgot an important point!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "On the other side of the West Block there's\x01",
            "a port and a warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "It was closed off during the coup d'etat.\x01",
            "No one could get in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3930")

    label("loc_389F")


    ChrTalk(    #155
        0xFE,
        (
            "On the other side of the West Block is\x01",
            "a port and a warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "It was closed off during the coup d'etat.\x01",
            "No one could get in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3930")

    TalkEnd(0xFE)
    Return()

    # Function_14_2BD4 end

    def Function_15_3934(): pass

    label("Function_15_3934")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_3941")
    Jump("loc_4128")

    label("loc_3941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_39CD")

    ChrTalk(    #157
        0xFE,
        (
            "Ahh, I never knew the sun could\x01",
            "be so bright and warm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Nights are so dark and cold.\x01",
            "It makes me all the more anxious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3AAD")

    ChrTalk(    #159
        0xFE,
        (
            "Apparently, Colonel Richard's second-in-\x01",
            "command started a second uprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "I had a feeling that sneaky woman\x01",
            "was planning something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I do sort of understand her dedication\x01",
            "to the colonel, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3B00")

    ChrTalk(    #162
        0xFE,
        "...A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I'm sorry, but I haven't seen her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_3B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3BC5")

    ChrTalk(    #164
        0xFE,
        "I saw Duke Dunan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I doubted my eyes when I saw him,\x01",
            "but there's no mistaking that hair style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "I'd heard he was under house arrest at\x01",
            "the villa, but I guess he came back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_3BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C7A")

    ChrTalk(    #167
        0xFE,
        (
            "I believe that Colonel Richard had some\x01",
            "reasons of his own for what he did, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I really have no intention of forgiving\x01",
            "Duke Dunan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "Don't you agree?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_3C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3D34")

    ChrTalk(    #170
        0xFE,
        (
            "You know the Imperial and the\x01",
            "Republican ambassadors...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I've seen the pair in public before,\x01",
            "but they both seem like they very much\x01",
            "have their own...idiosyncrasies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4128")

    label("loc_3D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3F")

    ChrTalk(    #172
        0xFE,
        (
            "Apparently, the Royal Army's guarding\x01",
            "the city since the signing ceremony for\x01",
            "the pact is close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "...I wonder what Colonel Richard's doing\x01",
            "nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I believe the colonel had some kind\x01",
            "of reasoning behind his coup d'etat,\x01",
            "even now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3ECF")

    label("loc_3E3F")


    ChrTalk(    #175
        0xFE,
        (
            "...I wonder what Colonel Richard's doing\x01",
            "nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I believe the colonel had some kind\x01",
            "of reasoning behind his coup d'etat,\x01",
            "even now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECF")

    Jump("loc_4128")

    label("loc_3ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405D")

    ChrTalk(    #177
        0xFE,
        (
            "If you want to go to the royal villa, it's\x01",
            "right out that gate there and south along\x01",
            "the Royal Avenue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "When you hit the fork in the road at\x01",
            "the guidepost, next head towards the\x01",
            "Gurune Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Then once you hit the next fork, head south\x01",
            "and you should reach the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "You shouldn't get lost as long as you make\x01",
            "sure to read the guideposts carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_4128")

    label("loc_405D")


    ChrTalk(    #181
        0xFE,
        (
            "If you want to go to the royal villa, it's\x01",
            "right out that gate there and south along\x01",
            "the Royal Avenue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "There are signposts along the way, so you\x01",
            "should be able to make it without getting lost.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4128")

    TalkEnd(0xFE)
    Return()

    # Function_15_3934 end

    def Function_16_412C(): pass

    label("Function_16_412C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4139")
    Jump("loc_46F3")

    label("loc_4139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4208")

    ChrTalk(    #183
        0xFE,
        (
            "All the younger people are pretty shocked,\x01",
            "it seems. Haha. Never been a day in their\x01",
            "lives when they didn't have orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Of course, the fisherman's group is\x01",
            "proving to be pretty tough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_4208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_42B4")

    ChrTalk(    #185
        0xFE,
        "Seems like Colonel Richard's caused an uprising.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "To cause trouble like that in the very lap of\x01",
            "the queen... They really were a crazy bunch\x01",
            "to the last.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_42B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4332")

    ChrTalk(    #187
        0xFE,
        (
            "Seems like the Ruan mayoral election\x01",
            "results are out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Maybe I'll pick up a copy of the Liberl\x01",
            "News later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_4332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_442D")

    ChrTalk(    #189
        0xFE,
        (
            "Anyone could whip up a\x01",
            "non-aggression pact, but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "I think the only one who could actually\x01",
            "make it happen is Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "The queen is the pride of Liberl. I'm very\x01",
            "glad that Richard, or whoever he is, has\x01",
            "been caught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_442D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44AA")

    ChrTalk(    #192
        0xFE,
        (
            "I never skip my early morning and\x01",
            "evening walks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Those daily walks are the\x01",
            "real secret to my health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_44AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4536")

    ChrTalk(    #194
        0xFE,
        (
            "When I heard that the queen was ill,\x01",
            "I thought I'd fall over where I was!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Does that Colonel Richard man\x01",
            "have any shame?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_4536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_462C")

    ChrTalk(    #196
        0xFE,
        (
            "I saw General Cassius in front of\x01",
            "the castle the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "He's younger than General Morgan,\x01",
            "but he's calm and has a certain gravity\x01",
            "to him, I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Still, why was the hero of the Hundred\x01",
            "Days War acting as a bracer?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F3")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_46F3")

    ChrTalk(    #199
        0xFE,
        (
            "Apparently, the pianist who was\x01",
            "frequenting that bar there until recently\x01",
            "played some amazing performances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "He was a strange one, but I think his\x01",
            "skills at least were the real deal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46F3")

    TalkEnd(0xFE)
    Return()

    # Function_16_412C end

    def Function_17_46F7(): pass

    label("Function_17_46F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4704")
    Jump("loc_4968")

    label("loc_4704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4781")

    ChrTalk(    #201
        0xFE,
        (
            "The capital's somehow managed\x01",
            "to regain its calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "This, too, is also thanks to the queen's\x01",
            "proclamation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4968")

    label("loc_4781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_47D2")

    ChrTalk(    #203
        0xFE,
        (
            "I didn't think Captain Amalthea would\x01",
            "be hiding in the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4968")

    label("loc_47D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_48A7")

    ChrTalk(    #204
        0xFE,
        (
            "There's a lot of people in the capital\x01",
            "who support Richard, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "However, his crime is too serious to\x01",
            "just overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "It's natural that military men who\x01",
            "violate military code are punished.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4968")

    label("loc_48A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_493F")

    ChrTalk(    #207
        0xFE,
        (
            "The day of the signing ceremony's\x01",
            "approaching, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "We'll be serving as security for the capital\x01",
            "under Colonel Cid's command.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4968")

    label("loc_493F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_494D")
    Jump("loc_4968")

    label("loc_494D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4957")
    Jump("loc_4968")

    label("loc_4957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4961")
    Jump("loc_4968")

    label("loc_4961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4968")

    label("loc_4968")

    TalkEnd(0xFE)
    Return()

    # Function_17_46F7 end

    def Function_18_496C(): pass

    label("Function_18_496C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4979")
    Jump("loc_4C13")

    label("loc_4979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_49B6")

    ChrTalk(    #209
        0xFE,
        "Even just waiting like this makes me nervous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C13")

    label("loc_49B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A88")

    ChrTalk(    #210
        0xFE,
        (
            "The Royal Army's investigated to\x01",
            "the extent of their ability, but that giant\x01",
            "construct hasn't been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "If something like that's turned up,\x01",
            "I wonder what'll happen to Liberl...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_4AE1")

    label("loc_4A88")


    ChrTalk(    #212
        0xFE,
        "No, the Royal Army has General Cassius...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "I'm sure he'll be able to handle it.\x02",
    )

    CloseMessageWindow()

    label("loc_4AE1")

    Jump("loc_4C13")

    label("loc_4AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4B4B")

    ChrTalk(    #214
        0xFE,
        "Nothing out of the ordinary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "I hope nothing happens before the\x01",
            "signing ceremony...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C13")

    label("loc_4B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_4BEA")

    ChrTalk(    #216
        0xFE,
        (
            "If you see anyone suspicious,\x01",
            "please report them immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "There might be people planning to interrupt\x01",
            "the signing ceremony, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C13")

    label("loc_4BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BF8")
    Jump("loc_4C13")

    label("loc_4BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4C02")
    Jump("loc_4C13")

    label("loc_4C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4C0C")
    Jump("loc_4C13")

    label("loc_4C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4C13")

    label("loc_4C13")

    TalkEnd(0xFE)
    Return()

    # Function_18_496C end

    def Function_19_4C17(): pass

    label("Function_19_4C17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4C24")
    Jump("loc_4EB6")

    label("loc_4C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C83")

    ChrTalk(    #218
        0xFE,
        "I wonder why the stove isn't working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "It's hard to cook without a stove...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4CE7")

    ChrTalk(    #220
        0xFE,
        (
            "I'm sure the Intelligence Division wanted to\x01",
            "cause trouble for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4D25")

    ChrTalk(    #221
        0xFE,
        (
            "The soldiers must be having a hard\x01",
            "time too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_4D60")

    ChrTalk(    #222
        0xFE,
        (
            "All right, time to give today\x01",
            "my very best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA6")

    ChrTalk(    #223
        0xFE,
        (
            "I need to get home and start preparing\x01",
            "for dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4E11")

    ChrTalk(    #224
        0xFE,
        (
            "*yaaaawn*\x01",
            "Maybe I'll go home and take a nap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "I wonder why eating makes me so sleepy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4E41")

    ChrTalk(    #226
        0xFE,
        "Mmmm, what lovely weather today!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4EB6")

    ChrTalk(    #227
        0xFE,
        "Hello. Lovely weather we're having.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "When the weather's this nice, you\x01",
            "can't help but feel nice too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB6")

    TalkEnd(0xFE)
    Return()

    # Function_19_4C17 end

    def Function_20_4EBA(): pass

    label("Function_20_4EBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4EC7")
    Jump("loc_511C")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4F44")

    ChrTalk(    #229
        0xFE,
        (
            "You can see the flying island\x01",
            "thingy from the harbor from what\x01",
            "I hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "What say we go see for ourselves?\x02",
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_4F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4F9D")

    ChrTalk(    #231
        0xFE,
        "Oh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "Yesterday, the Intelligence Division\x01",
            "appeared at the harbor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_4F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4FED")

    ChrTalk(    #233
        0xFE,
        (
            "They've finally picked someone\x01",
            "as the new mayor for Ruan, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_4FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_5052")

    ChrTalk(    #234
        0xFE,
        (
            "The weather's so nice today.\x01",
            "Maybe we should have a little\x01",
            "stroll at the royal villa?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_5052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_508B")

    ChrTalk(    #235
        0xFE,
        "Meat, or fish, that's the question...\x02",
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_508B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_50B9")

    ChrTalk(    #236
        0xFE,
        "What should we eat for dinner?\x02",
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_50B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_50E2")

    ChrTalk(    #237
        0xFE,
        "Where should we go today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_511C")

    label("loc_50E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_511C")

    ChrTalk(    #238
        0xFE,
        "Ooh, I'm so hungry I feel like I could die...\x02",
    )

    CloseMessageWindow()

    label("loc_511C")

    TalkEnd(0xFE)
    Return()

    # Function_20_4EBA end

    def Function_21_5120(): pass

    label("Function_21_5120")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_512D")
    Jump("loc_53DE")

    label("loc_512D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5168")

    ChrTalk(    #239
        0xFE,
        "Hmm... I just don't feel like it right now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_5168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_51F6")

    ChrTalk(    #240
        0xFE,
        (
            "Special Ops soldiers...? That means the\x01",
            "Intelligence Division's little kill squad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "Do you get it? They're the same thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_51F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5233")

    ChrTalk(    #242
        0xFE,
        "...He's always been a little on the odd side.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_5233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_5278")

    ChrTalk(    #243
        0xFE,
        (
            "...Didn't you know?\x01",
            "The villa's closed off right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_5278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52C8")

    ChrTalk(    #244
        0xFE,
        (
            "You really just spend half the\x01",
            "day worrying about food, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_52C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5329")

    ChrTalk(    #245
        0xFE,
        "You just ate, didn't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "I'm so full, I don't want to think about anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_5329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_5398")

    ChrTalk(    #247
        0xFE,
        "I don't really think we need to go anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "I'd like to relax and take it easy sometimes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53DE")

    label("loc_5398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_53DE")

    ChrTalk(    #249
        0xFE,
        (
            "Heehee. All right, let's have something to eat,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53DE")

    TalkEnd(0xFE)
    Return()

    # Function_21_5120 end

    def Function_22_53E2(): pass

    label("Function_22_53E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_53EF")
    Jump("loc_5778")

    label("loc_53EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_546E")

    ChrTalk(    #250
        0xFE,
        "Don't see any tourists around at all anymore...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "I mean, not much you can do about it,\x01",
            "but it's pretty sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_550D")

    ChrTalk(    #252
        0xFE,
        (
            "Last night, orbments in the West Block\x01",
            "became unusable for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Whatever. I'm sure if Tom's investigating,\x01",
            "we'll find the answer soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_550D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_556A")

    ChrTalk(    #254
        0xFE,
        (
            "I do think Zacharias over at the factory's\x01",
            "quite the businessman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "But...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_556A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_55F7")

    ChrTalk(    #256
        0xFE,
        (
            "There was a light on until late in the\x01",
            "factory's third floor last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "I'm sure Tom must've been up late fixing stuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_55F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5637")

    ChrTalk(    #258
        0xFE,
        (
            "Okay, time to head home before\x01",
            "the sun sets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_5637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_56CF")

    ChrTalk(    #259
        0xFE,
        (
            "Apparently, Tom at the factory had\x01",
            "a fight with the manager, Zacharias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "I'd heard they'd always kind of\x01",
            "gotten along poorly, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_56CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_5738")

    ChrTalk(    #261
        0xFE,
        "Tom over at the factory is really skilled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "I doubt there's anything he can't repair!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5778")

    label("loc_5738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5778")

    ChrTalk(    #263
        0xFE,
        (
            "The factory in this town has\x01",
            "a very nice repairman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5778")

    TalkEnd(0xFE)
    Return()

    # Function_22_53E2 end

    def Function_23_577C(): pass

    label("Function_23_577C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5797")
    Call(0, 49)
    Call(0, 50)
    AddParty(0x2E, 0xFF, 0xFF)

    label("loc_5797")

    SetChrPos(0x101, 1530, 0, -62500, 180)
    SetChrPos(0x12F, 150, 0, -63240, 90)
    SetChrPos(0xF7, 2900, 0, -63290, 270)
    SetChrPos(0xF8, 2150, 0, -64519, 0)
    SetChrPos(0xF9, 1100, 0, -64430, 0)
    OP_6D(1530, 0, -62500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(31000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#6POkay, let's get back to the guild.\x02\x03",

            "We need to talk to Elnan about Renne.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_593E")

    ChrTalk(    #265
        0x106,
        (
            "#552FThere's that, but our army contact should\x01",
            "be showing up soon.\x02\x03",

            "You didn't forget about that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1004F#6POh, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x106,
        "#053FFor cryin' out...\x02",
    )

    CloseMessageWindow()
    Jump("loc_59EA")

    label("loc_593E")


    ChrTalk(    #268
        0x103,
        (
            "#027FThat's very important, yes, but the\x01",
            "army should be sending their contact\x01",
            "soon.\x02\x03",

            "You didn't forget, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#1004F#6POh, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x103,
        "#025F*sigh* Estelle...\x02",
    )

    CloseMessageWindow()

    label("loc_59EA")


    ChrTalk(    #271
        0x12F,
        (
            "#264F#5PHuh? What's wrong?\x02\x03",

            "You said you're gonna show me to\x01",
            "this 'guild' place, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA1")

    ChrTalk(    #272
        0x104,
        (
            "#031FHeh, well, m'lady, please lend me\x01",
            "your hand.\x02\x03",

            "I, Olivier Lenheim, shall have the\x01",
            "honor of escorting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x12F,
        (
            "#263F#5PNo, thank you.\x02\x03",

            "I'd rather Miss Estelle to show me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x104,
        "#036FMy disappointments are ceaseless!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 231, 400)

    ChrTalk(    #275
        0x101,
        (
            "#1016F#6PHaha! Sorry, Olivier, no luck.\x02\x03",

            "#1006FC'mon, Renne. I'll show you the\x01",
            "Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BF0")

    label("loc_5BA1")

    OP_8C(0x101, 231, 400)

    ChrTalk(    #276
        0x101,
        (
            "#1006F#6POh, right!\x02\x03",

            "C'mon, Renne. I'll show you the\x01",
            "Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF0")


    ChrTalk(    #277
        0x12F,
        "#261F#5PYay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1619)
    EventEnd(0x0)
    Return()

    # Function_23_577C end

    def Function_24_5C08(): pass

    label("Function_24_5C08")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x2E, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x3, 0xF8, 0xFF)
    AddParty(0x7, 0xF9, 0xFF)
    SetChrPos(0x101, 5050, 0, -11050, 180)
    SetChrPos(0x108, 6200, 0, -12130, 270)
    SetChrPos(0x104, 4000, 0, -12230, 90)
    SetChrPos(0x105, 5130, 0, -13310, 360)
    OP_6D(5100, 0, -12050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #278
        0x101,
        (
            "#1011F#6PTime to get questioning, then.\x02\x03",

            "Where should we start?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x108,
        (
            "#070FDon't think it matters too much.\x02\x03",

            "If you want to go to the Calvardian embassy,\x01",
            "you've got a free pass with me around.\x02\x03",

            "I can introduce you to Elsa whenever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x104,
        (
            "#030F#6PI, of course, can get us into the\x01",
            "Erebonian embassy.\x02\x03",

            "They should be glad to escort us if\x01",
            "I introduce myself at the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x105,
        (
            "#040FAnd, of course, I rather doubt it'll be\x01",
            "very hard for me to get us into Grancel\x01",
            "Castle.\x02\x03",

            "It might be wise to simply go straight\x01",
            "there and speak with Grandmother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1006F#6PI kinda doubt the Liberl News will give\x01",
            "us any trouble either, so...\x02\x03",

            "Eh, let's just pick a direction and go!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8A, 0x4, 0x2)
    OP_28(0x8A, 0x4, 0x8)
    OP_28(0x8A, 0x1, 0x1)
    OP_28(0x8A, 0x1, 0x2)
    OP_28(0x8B, 0x4, 0x2)
    OP_28(0x8B, 0x4, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5F89")
    OP_28(0x8B, 0x1, 0x2)
    Jump("loc_5F96")

    label("loc_5F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5F96")
    OP_28(0x8B, 0x1, 0x1)

    label("loc_5F96")

    OP_28(0x8B, 0x1, 0x4)
    OP_28(0x8B, 0x1, 0x8)
    OP_28(0x8B, 0x1, 0x20)
    OP_28(0x8B, 0x1, 0x80)
    OP_28(0x8B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    Return()

    # Function_24_5C08 end

    def Function_25_5FBF(): pass

    label("Function_25_5FBF")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE6")
    Call(0, 49)
    Call(0, 51)

    label("loc_5FE6")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1B)
    Sleep(800)
    OP_43(0x107, 0x1, 0x0, 0x1C)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(2000)

    def lambda_608D():
        OP_6D(4550, 0, -13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_608D)
    OP_6C(32000, 3000)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #283
        0x101,
        (
            "#1011F#6PNow, then, where would I hide if\x01",
            "I was a silly little girl...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #284
        0x101,
        "#1006F#6PTita, any ideas?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x107,
        (
            "#561F#7PUmmm...\x02\x03",

            "#060FWe went by a lot of places in the\x01",
            "eastern block yesterday.\x02\x03",

            "Maybe she's at one of those places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        "#1004F#6PUh, which places?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x107,
        (
            "#560F#7PUm, let's see... First we looked around the\x01",
            "department store...\x02\x03",

            "Then we went to the History Museum...\x02\x03",

            "#061FAnd then we stopped by the ice cream\x01",
            "stand near the clock tower!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#1016F#6PWow, you two were busy...\x02\x03",

            "#1006FSounds like you had a lot of fun,\x01",
            "though, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x107,
        "#067F#7PHeehee...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_634E")

    ChrTalk(    #290
        0x108,
        (
            "#070FThat does give us a good list of\x01",
            "places to visit first, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_638B")

    label("loc_634E")


    ChrTalk(    #291
        0x105,
        (
            "#048FLet's begin by checking around\x01",
            "those places, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_63CA")

    ChrTalk(    #292
        0x106,
        "#051F#6PYeah, let's drag our little stray back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_63FD")

    label("loc_63CA")


    ChrTalk(    #293
        0x103,
        "#020F#6PYes, let's go fetch our stray kitten.\x02",
    )

    CloseMessageWindow()

    label("loc_63FD")

    OP_28(0x8C, 0x4, 0x2)
    OP_28(0x8C, 0x4, 0x8)
    OP_28(0x8C, 0x1, 0x1)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    OP_4B(0x2A, 255)
    OP_4B(0x2B, 255)
    Return()

    # Function_25_5FBF end

    def Function_26_6420(): pass

    label("Function_26_6420")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0xDDE, 0x0, 0xFFFFCD2E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_6420 end

    def Function_27_6452(): pass

    label("Function_27_6452")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x10F4, 0x0, 0xFFFFD0E4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_27_6452 end

    def Function_28_6484(): pass

    label("Function_28_6484")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x114E, 0x0, 0xFFFFC978, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_6484 end

    def Function_29_64B6(): pass

    label("Function_29_64B6")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)
    OP_8E(0xFE, 0x2418, 0x19A, 0xFFFFCD2E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x14A0, 0x0, 0xFFFFCD2E, 0x7D0, 0x0)
    Return()

    # Function_29_64B6 end

    def Function_30_652B(): pass

    label("Function_30_652B")

    EventBegin(0x0)
    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_652B end

    def Function_31_6537(): pass

    label("Function_31_6537")

    EventBegin(0x0)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2F, 0x80)
    OP_D2(0x260246, 0x26024B, 0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6598")
    Call(0, 49)
    Call(0, 51)
    FadeToBright(0, 0)

    label("loc_6598")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xF7, 4670, 0, -3450, 180)
    SetChrPos(0x8, 3420, 0, -3270, 180)
    SetChrPos(0xF9, 4650, 0, -1250, 180)
    SetChrPos(0x107, 3640, 0, -1760, 180)
    SetChrPos(0x101, 4890, 0, 8950, 180)
    SetChrPos(0x9, 3730, 0, 10070, 180)
    OP_6D(5110, 0, 330, 0)
    OP_67(0, 7760, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(45000, 0)
    OP_6E(320, 0)
    OP_43(0xF7, 0x1, 0x0, 0x21)
    OP_43(0x8, 0x1, 0x0, 0x22)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    OP_43(0x107, 0x1, 0x0, 0x24)
    OP_43(0x101, 0x1, 0x0, 0x25)
    OP_43(0x9, 0x1, 0x0, 0x26)

    def lambda_6675():
        OP_6D(8590, 250, -13060, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6675)
    FadeToBright(2000, 0)
    WaitChrThread(0xF7, 0x1)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x20)
    WaitChrThread(0x107, 0x1)
    Sleep(300)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)

    def lambda_6701():
        OP_8E(0xFE, 0x2544, 0x1F4, 0xFFFFCCCA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6701)

    def lambda_671C():
        OP_8E(0xFE, 0x1B4E, 0xFA, 0xFFFFCC98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_671C)
    WaitChrThread(0x9, 0x1)
    OP_71(0x1, 0x800)
    OP_8C(0x9, 90, 0)

    ChrTalk(    #294
        0x9,
        "#267F#1PHey, Estelle?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    OP_8E(0x101, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)

    ChrTalk(    #295
        0x101,
        (
            "#1006F#4PWhat's up?\x02\x03",

            "I'm not angry any more, don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x9,
        (
            "#261F#1PHeehee! No, that's not it.\x02\x03",

            "#265FBesides, you aren't scary even when\x01",
            "you ARE angry, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1019F#4PIf you WANT to see scary, little girl,\x01",
            "I can totally arrange it.\x02\x03",

            "#1015FBut, um, what's up, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x9,
        (
            "#267F#1PWell...\x02\x03",

            "While I was out, this boy gave me a letter.\x01",
            "To give to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1004F#4PA...letter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x9,
        "#267F#1PYeah. It was weird... Here, take it.\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_8F(0x9, 0x1F0E, 0xFA, 0xFFFFCCDE, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #301
        "\x07\x05Renne handed Estelle a letter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x9, 0x1B4E, 0xFA, 0xFFFFCC98, 0x7D0, 0x0)

    ChrTalk(    #302
        0x101,
        (
            "#1004F#4PHuh...?\x02\x03",

            "It IS addressed to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x9,
        "#260F#1PYeah! Like I said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1015F#4PWho's this from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x9,
        (
            "#263F#1PHeehee... I think the letter might tell you.\x01",
            "I, um, kinda peeked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        "#1011F#4POh, well, uh, let's see...\x02",
    )

    CloseMessageWindow()
    OP_D2(0x260246, 0x26024B, 0x16)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #307
        "\x07\x05Estelle opened the letter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetChrName("")
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #308
        (
            "\x07\x05My Dearest Estelle.\x02\x03",

            "I've thought this over, again and again, and now\x01",
            "I realize there's something I absolutely must\x01",
            "tell you.\x02\x03",

            "I know this is a lot to ask, but can\x01",
            "I meet you alone?\x02\x03",

            "I'll be waiting this evening at the Gurune Gate,\x01",
            "above the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    Sleep(500)

    ChrTalk(    #309
        0x101,
        "#1004F#4PWh-Wha...\x02",
    )

    CloseMessageWindow()
    OP_1D(0x5B)
    Sleep(500)

    ChrTalk(    #310
        0x9,
        (
            "#265F#1PHeehee. Is it from who I thought after all?\x02\x03",

            "As soon as I saw him, I remembered you\x01",
            "telling me that story and figured it was the\x01",
            "boy you were talking about. ♪\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #311
        0x101,
        (
            "#1020F#4PTh-Th-This...\x02\x03",

            "Renne, who gave this to you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x9,
        (
            "#260F#1PA really cute boy with black hair\x01",
            "and amber eyes.\x02\x03",

            "He asked me to give it to you when\x01",
            "I was at the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1025F#4POf course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x9,
        (
            "#261F#1PThat was the Joshua you talked about,\x01",
            "right, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        (
            "#1025F#4PI... Maybe...\x02\x03",

            "The writing looks like his, too...\x01",
            "s-so it's got to be him!\x02\x03",

            "#1015FEvening at the Gurune Gate,\x01",
            "above the Ahnenburg...\x02\x03",

            "#1020FEvening...\x01",
            "Aidios, that's practically now!\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    ClearChrFlags(0xF7, 0x80)

    def lambda_6F23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_6F23)

    def lambda_6F35():
        OP_8E(0xFE, 0x251C, 0x19A, 0xFFFFCD2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6F35)
    WaitChrThread(0xF7, 0x1)
    OP_72(0x1, 0x800)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_739A")

    ChrTalk(    #316
        0x106,
        (
            "#052FHey, Estelle, what the hell are you\x01",
            "still doing out here?\x02\x03",

            "Elnan's going to be running a briefing on\x01",
            "everything soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #317
        0x101,
        (
            "#1026F#6PAgate...\x02\x03",

            "What should I do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x106,
        (
            "#055FHuh?\x02\x03",

            "What happened? You look like you got\x01",
            "punched in the gut.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #319
        "\x07\x05Estelle wordlessly showed Agate the letter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #320
        0x106,
        (
            "#052F...\x02\x03",

            "#050FThis is from Joshua, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1026F#6PI think so...\x02\x03",

            "Renne said she got it from someone that\x01",
            "looks just like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x106,
        (
            "#053FHmmmmmm...\x02\x03",

            "#051FAll right. Get goin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x106,
        (
            "#051FIt's cool, just get goin' already.\x02\x03",

            "I'll cover for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#1025F#6PRight...\x02\x03",

            "#1001FAgate, thank you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 600)
    Sleep(300)

    ChrTalk(    #326
        0x101,
        (
            "#1018F#4PYou too, Renne. Thank you for telling me!\x01",
            "Goodbye!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x9,
        "#264F#1PYou're w--\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_7287():

        label("loc_7287")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_7287")

    QueueWorkItem2(0x9, 1, lambda_7287)

    def lambda_7298():
        OP_8E(0xFE, 0x2026, 0xFA, 0xFFFF8A62, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7298)
    Sleep(500)

    def lambda_72B8():
        OP_6D(8540, 250, -16640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72B8)
    OP_8E(0xF7, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)
    OP_8C(0xF7, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_6D(8189, 250, -12990, 2000)

    ChrTalk(    #328
        0x9,
        (
            "#268F#6PShe's gone already...\x02\x03",

            "#267FDoes she really want to meet\x01",
            "Joshua that badly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x106,
        (
            "#051F#6PDefinitely.\x02\x03",

            "Heh... Now what do I tell everyone else?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77D3")

    label("loc_739A")


    ChrTalk(    #330
        0x103,
        (
            "#020FEstelle, honey, what's wrong?\x02\x03",

            "Elnan's about to brief everyone on our\x01",
            "findings. Why are you out here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #331
        0x101,
        (
            "#1026F#6PSchera...\x02\x03",

            "What should I do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x103,
        (
            "#023FHm?\x02\x03",

            "#022F...Estelle, what's wrong?\x01",
            "Come now, tell me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #333
        "\x07\x05Estelle wordlessly showed Scherazard the letter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #334
        0x103,
        (
            "#022F...\x02\x03",

            "This is from Joshua, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1026F#6PI think so...\x02\x03",

            "Renne said she got it from someone that\x01",
            "looks just like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x103,
        (
            "#026FI see.\x02\x03",

            "#524FAll right, off you go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#1004F#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x103,
        (
            "#027FI'll come up with something to tell\x01",
            "the others.\x02\x03",

            "Or would you rather stay here and\x01",
            "mope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#1025F#6POh...\x02\x03",

            "#1001FSchera... Thank you! Thank you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 600)
    Sleep(300)

    ChrTalk(    #340
        0x101,
        (
            "#1018F#4PYou too, Renne.\x01",
            "Thank you for telling me! Goodbye!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x9,
        "#264F#1PYou're w--\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 600)

    def lambda_76B6():

        label("loc_76B6")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_76B6")

    QueueWorkItem2(0x9, 1, lambda_76B6)

    def lambda_76C7():
        OP_8E(0xFE, 0x2026, 0xFA, 0xFFFF8A62, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76C7)

    def lambda_76E2():
        OP_6D(8540, 250, -16640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_76E2)
    OP_8E(0xF7, 0x218E, 0xFA, 0xFFFFCCFC, 0x7D0, 0x0)
    OP_8C(0xF7, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_6D(8189, 250, -12990, 2000)

    ChrTalk(    #342
        0x9,
        (
            "#268F#6PShe's gone already...\x02\x03",

            "#267FDoes she really want to meet\x01",
            "Joshua that badly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x103,
        (
            "#524F#6PYes...she does.\x02\x03",

            "Joshua is the whole reason she's\x01",
            "traveling, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77D3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6537 end

    def Function_32_77F5(): pass

    label("Function_32_77F5")

    OP_8E(0xFE, 0x2CEC, 0x2EE, 0xFFFFCE1E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_77F5 end

    def Function_33_781A(): pass

    label("Function_33_781A")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1EBE, 0xFA, 0xFFFFCE82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x25C6, 0x1F4, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_33_781A end

    def Function_34_785E(): pass

    label("Function_34_785E")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1AB8, 0xFA, 0xFFFFCB12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x21CA, 0xFA, 0xFFFFCB26, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_34_785E end

    def Function_35_78A2(): pass

    label("Function_35_78A2")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1E5A, 0xFA, 0xFFFFCE14, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_35_78A2 end

    def Function_36_78D2(): pass

    label("Function_36_78D2")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1CDE, 0xFA, 0xFFFFC9AA, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_36_78D2 end

    def Function_37_7902(): pass

    label("Function_37_7902")

    OP_8E(0xFE, 0x12FC, 0x0, 0xFFFFDB2A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x161C, 0x0, 0xFFFFD044, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_37_7902 end

    def Function_38_7932(): pass

    label("Function_38_7932")

    OP_8E(0xFE, 0xDB6, 0x0, 0xFFFFD9D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x140A, 0x0, 0xFFFFCC48, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_38_7932 end

    def Function_39_7962(): pass

    label("Function_39_7962")

    EventBegin(0x0)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7985")
    Call(0, 49)

    label("loc_7985")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_6D(106730, -1920, 53920, 0)
    SetChrName("")

    AnonymousTalk(    #344
        (
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7A57")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_7A77")

    label("loc_7A57")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_7A77")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x1, 0x10)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1B)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x1C)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(2000)

    def lambda_7B38():
        OP_6D(4550, 0, -13010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B38)
    OP_6C(32000, 3000)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #345
        0x101,
        (
            "#1011F#6PAnd next up, Bose!\x02\x03",

            "If we're ready, shall we head to the port?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7C2F")

    ChrTalk(    #346
        0x106,
        (
            "#051F#6PWell, the Royal Army's on the bandit case\x01",
            "too, remember.\x02\x03",

            "For once we aren't feelin' the squeeze\x01",
            "to get somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CBE")

    label("loc_7C2F")


    ChrTalk(    #347
        0x103,
        (
            "#020F#6PThe Royal Army's also working on the\x01",
            "sky bandit case, remember.\x02\x03",

            "There's no pressing need for us to depart\x01",
            "immediately, for once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CBE")


    ChrTalk(    #348
        0x101,
        (
            "#1006F#6PThat's true.\x02\x03",

            "So let's take our time to finish up\x01",
            "stuff and then go.\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x1, 0x10)
    OP_A2(0x163D)
    OP_28(0x8E, 0x1, 0x10)
    OP_28(0x8E, 0x1, 0x20)
    OP_28(0x8E, 0x1, 0x40)
    OP_28(0x8E, 0x1, 0x80)
    OP_28(0x8E, 0x1, 0x100)
    EventEnd(0x0)
    OP_4B(0x28, 255)
    OP_4B(0x29, 255)
    OP_4B(0x2A, 255)
    OP_4B(0x2B, 255)
    Return()

    # Function_39_7962 end

    def Function_40_7D4A(): pass

    label("Function_40_7D4A")

    SetChrPos(0xA, 4360, 0, -46020, 45)
    SetChrPos(0xB, 8590, 250, 4630, 135)
    SetChrPos(0xC, -20020, 0, -18430, 45)
    SetChrPos(0xD, -1290, 0, -27300, 225)
    SetChrPos(0xE, -9520, 250, -34120, 135)
    SetChrPos(0xF, -5550, 0, 10730, 45)
    SetChrPos(0x10, -2220, 0, -52660, 135)
    SetChrPos(0x11, 8320, 0, -54670, 135)
    SetChrPos(0x12, -6330, 0, -43560, 45)
    SetChrPos(0x13, -4470, 0, -43980, 315)
    SetChrPos(0x14, 7400, 250, -24080, 135)
    SetChrPos(0x15, -7630, 250, -23890, 180)
    SetChrPos(0x16, 1760, 0, 3810, 180)
    SetChrPos(0x17, 80, 0, -5910, 315)
    SetChrPos(0x18, 10730, 0, -660, 270)
    SetChrPos(0x19, -10270, 250, -2340, 90)
    SetChrPos(0x1A, -12400, 0, -18460, 90)
    SetChrPos(0x1B, 7690, 0, -41750, 180)
    SetChrPos(0x1C, 3030, 0, -21550, 180)
    SetChrPos(0x1D, -3210, 0, -13780, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    Return()

    # Function_40_7D4A end

    def Function_41_7F8A(): pass

    label("Function_41_7F8A")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -40, 250, -19800, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 250, 4400, -9460, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -6990, 1800, -36580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -10790, 5400, -31940, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -12500, 5400, -3340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 12600, 4800, -33570, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 300, 3900, -2500, 0, 0, 0, 1500, 1800, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -740, 3210, -30070, 0, 0, 0, 1600, 1700, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 12400, 1900, -37980, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -15780, 7900, -15450, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 10800, 4800, 9940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 31290, 5000, -7600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6400, 1200, -55200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 12720, 4600, -33670, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 12400, 1700, -38000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -1000, 2700, -29750, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15780, 7600, -15200, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 1000, 2400, -2390, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 31290, 4500, -7600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 340, 4000, -9320, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -6720, 1500, -36580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -10840, 4800, -32049, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -12750, 5200, -3340, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 10800, 4700, 9940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_7F8A end

    def Function_42_84FA(): pass

    label("Function_42_84FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8524")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_8524")

    OP_D2(0x70371, 0x70376, 0x16)
    OP_D2(0x290144, 0x290148, 0x17)
    OP_D2(0x290144, 0x290148, 0x18)
    OP_D2(0x290144, 0x290148, 0x19)
    OP_D2(0x270110, 0x270120, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_8579"),
        (5, "loc_8586"),
        (6, "loc_8593"),
        (7, "loc_85A0"),
        (SWITCH_DEFAULT, "loc_85AD"),
    )


    label("loc_8579")

    OP_D2(0x701D0, 0x701DC, 0x1D)
    Jump("loc_85AD")

    label("loc_8586")

    OP_D2(0x70218, 0x70224, 0x1D)
    Jump("loc_85AD")

    label("loc_8593")

    OP_D2(0x70230, 0x7023C, 0x1D)
    Jump("loc_85AD")

    label("loc_85A0")

    OP_D2(0x70248, 0x70254, 0x1D)
    Jump("loc_85AD")

    label("loc_85AD")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_85C6"),
        (5, "loc_85D3"),
        (6, "loc_85E0"),
        (7, "loc_85ED"),
        (SWITCH_DEFAULT, "loc_85FA"),
    )


    label("loc_85C6")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    Jump("loc_85FA")

    label("loc_85D3")

    OP_D2(0x70218, 0x70224, 0x1E)
    Jump("loc_85FA")

    label("loc_85E0")

    OP_D2(0x70230, 0x7023C, 0x1E)
    Jump("loc_85FA")

    label("loc_85ED")

    OP_D2(0x70248, 0x70254, 0x1E)
    Jump("loc_85FA")

    label("loc_85FA")

    SetChrChipByIndex(0x1E, 22)
    SetChrPos(0x101, 630, 0, -62820, 0)
    SetChrPos(0x102, 1830, 0, -62880, 0)
    SetChrPos(0xF8, 270, 0, -64190, 0)
    SetChrPos(0xF9, 1700, 0, -64349, 0)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    OP_6D(780, 250, 3690, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(22000, 0)
    OP_6E(435, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    OP_DE("Grancel")
    FadeToBright(1000, 0)

    def lambda_86C6():
        OP_6D(1690, 0, -62710, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_86C6)

    def lambda_86DE():
        OP_67(0, 8670, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86DE)

    def lambda_86F6():
        OP_6B(1940, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86F6)

    def lambda_8706():
        OP_6C(33000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8706)
    OP_6E(389, 9000)

    ChrTalk(    #349
        0x101,
        "#1020F#6PNo...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8750")

    ChrTalk(    #350
        0x107,
        "#065F#2PWhy...?\x02",
    )

    CloseMessageWindow()

    label("loc_8750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8780")

    ChrTalk(    #351
        0x103,
        "#523F#2PSuch twisted evil...\x02",
    )

    CloseMessageWindow()

    label("loc_8780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87BE")

    ChrTalk(    #352
        0x108,
        "#077F#2PSuch indiscriminate destruction...\x02",
    )

    CloseMessageWindow()

    label("loc_87BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87E9")

    ChrTalk(    #353
        0x106,
        "#057F#2PThose bastards!\x02",
    )

    CloseMessageWindow()

    label("loc_87E9")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 28)

    ChrTalk(    #354
        0x102,
        "#1046F#4PHere they come!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrChipByIndex(0x1F, 20)
    SetChrChipByIndex(0x20, 20)
    SetChrPos(0x1F, -3390, 1000, -51000, 180)
    SetChrPos(0x20, 2660, 1000, -51000, 180)

    def lambda_8878():
        OP_6D(2080, 0, -60800, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8878)

    def lambda_8890():
        OP_67(0, 7000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8890)

    def lambda_88A8():
        OP_6B(1800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88A8)

    def lambda_88B8():
        OP_6E(389, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_88B8)
    SetChrChipByIndex(0x1F, 21)
    OP_43(0x1F, 0x3, 0x0, 0x2B)

    def lambda_88D4():
        OP_8F(0xFE, 0x0, 0x1F4, 0xFFFF13AC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_88D4)
    Sleep(200)
    SetChrChipByIndex(0x20, 21)

    def lambda_88F9():
        OP_8F(0xFE, 0xB0E, 0x1F4, 0xFFFF15A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_88F9)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 27)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 29)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 30)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x20, 0x1)
    OP_44(0x1F, 0x3)
    OP_23(0x13A)
    WaitChrThread(0x101, 0x0)
    OP_43(0x1F, 0x0, 0x0, 0x2C)
    Sleep(100)
    OP_43(0x20, 0x0, 0x0, 0x2C)
    WaitChrThread(0x1F, 0x0)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    Battle(0x54F, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 45)
    Return()

    # Function_42_84FA end

    def Function_43_8979(): pass

    label("Function_43_8979")

    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x13A, 0x0, 0x64)
    Return()

    # Function_43_8979 end

    def Function_44_89A7(): pass

    label("Function_44_89A7")

    SetChrChipByIndex(0xFE, 23)
    OP_99(0xFE, 0x0, 0x2, 0x5DC)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    OP_99(0xFE, 0x3, 0x4, 0x9C4)
    Return()

    # Function_44_89A7 end

    def Function_45_89D2(): pass

    label("Function_45_89D2")

    EventBegin(0x0)
    OP_D2(0x70371, 0x70376, 0x16)
    OP_D2(0x270110, 0x270120, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    OP_6D(30, 0, -56130, 0)
    OP_67(0, 7860, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(359000, 0)
    OP_6E(371, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, -490, 0, -62350, 0)
    SetChrPos(0x102, 790, 0, -62340, 0)
    SetChrPos(0xF8, -870, 0, -64030, 0)
    SetChrPos(0xF9, 1170, 0, -64250, 0)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)

    def lambda_8AD5():
        OP_6D(70, 0, -61320, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8AD5)

    def lambda_8AED():
        OP_6B(1990, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AED)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #355
        0x101,
        (
            "#1022F#6P*pant* What do...\x02\x03",

            "#1005FWhat're we even gonna do?!\x01",
            "The city...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1E, 4920, 0, -49670, 225)
    ClearChrFlags(0x1E, 0x80)

    NpcTalk(    #356
        0x1E,
        "Man's Voice",
        "#6PEveryone!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE6")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C24")

    label("loc_8BE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C0D")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C24")

    label("loc_8C0D")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8C24")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C50")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C8E")

    label("loc_8C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C77")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C8E")

    label("loc_8C77")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8C8E")

    Sleep(1000)

    def lambda_8C99():
        OP_6D(700, 0, -60230, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C99)

    def lambda_8CB1():
        OP_67(0, 5480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8CB1)

    def lambda_8CC9():
        OP_6B(2720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8CC9)

    def lambda_8CD9():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8CD9)

    def lambda_8CE9():
        OP_6E(289, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8CE9)

    def lambda_8CF9():
        OP_8E(0xFE, 0x76C, 0x0, 0xFFFF1776, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8CF9)

    def lambda_8D14():

        label("loc_8D14")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_8D14")

    QueueWorkItem2(0x101, 1, lambda_8D14)
    Sleep(50)

    def lambda_8D2A():

        label("loc_8D2A")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_8D2A")

    QueueWorkItem2(0x102, 1, lambda_8D2A)
    Sleep(50)

    def lambda_8D40():

        label("loc_8D40")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_8D40")

    QueueWorkItem2(0xF8, 1, lambda_8D40)
    Sleep(50)

    def lambda_8D56():

        label("loc_8D56")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_8D56")

    QueueWorkItem2(0xF9, 1, lambda_8D56)
    WaitChrThread(0x1E, 0x1)
    OP_8C(0x1E, 225, 400)
    OP_44(0x102, 0x1)
    OP_8C(0x102, 45, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #357
        0x101,
        "#1004F#5PElnan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x1E,
        (
            "#762F#4PYour timing is perfect!\x02\x03",

            "You're here about the business\x01",
            "the queen had with you, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        (
            "#1042F#5PThat WAS the idea.\x01",
            "What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x1E,
        (
            "#764F#4PThe army is in position along the eastern\x01",
            "and western blocks of the city as we speak.\x02\x03",

            "The fighting is terrible, but you\x01",
            "need to leave it to them.\x02\x03",

            "#762FYou must give chase to the Enforcers!\x01",
            "They are heading for the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1020F#5PBut...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F6D")

    ChrTalk(    #362
        0x103,
        (
            "#022FAre you sure the city\x01",
            "will be all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9003")

    label("loc_8F6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FB3")

    ChrTalk(    #363
        0x108,
        (
            "#072FAre you sure you don't need\x01",
            "our help here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9003")

    label("loc_8FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9003")

    ChrTalk(    #364
        0x106,
        (
            "#057FHang on! You want us to just\x01",
            "leave the city like this?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9003")


    ChrTalk(    #365
        0x1E,
        (
            "#762F#4PI've evacuated the people on\x01",
            "the street into the guildhouse.\x02\x03",

            "The army is evacuating the rest of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#1007F#5POkay...\x02\x03",

            "#1002FWe'll head to the castle, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x1E,
        (
            "#764F#4PThank you. Aidios guide you\x01",
            "and keep you safe.\x02\x03",

            "#760FBefore you go, take this.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x102, 0x3E8, 0xBB8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #368
        "\x07\x00Received #517i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x205, 4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8F(0x1E, 0x76C, 0x0, 0xFFFF1776, 0x7D0, 0x0)

    ChrTalk(    #369
        0x102,
        "#1040F#5PThank you, Elnan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x1E,
        "#762F#4PGood luck... I pray for your victory!\x02",
    )

    CloseMessageWindow()

    def lambda_91D7():

        label("loc_91D7")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_91D7")

    QueueWorkItem2(0x102, 1, lambda_91D7)
    OP_8C(0x1E, 0, 600)
    OP_8E(0x1E, 0x116C, 0x0, 0xFFFF37BA, 0x1388, 0x0)
    SetChrFlags(0x1E, 0x80)
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(1560, 0, -61910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1560, 0, -61910, 0)
    SetChrPos(0x1, 1560, 0, -61910, 0)
    SetChrPos(0x2, 1560, 0, -61910, 0)
    SetChrPos(0x3, 1560, 0, -61910, 0)
    OP_0D()
    OP_A2(0x203B)
    OP_28(0x9C, 0x1, 0x10)
    OP_28(0x9C, 0x1, 0x20)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_45_89D2 end

    def Function_46_92C9(): pass

    label("Function_46_92C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #371
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_92C9 end

    def Function_47_930B(): pass

    label("Function_47_930B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9314")
    Return()

    label("loc_9314")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9334")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_9334")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #372
        (
            "\x07\x05The sounds of gunfire and blades clashing\x01",
            "can be periodically heard from the eastern\x01",
            "city block.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942B")

    ChrTalk(    #373
        0x101,
        (
            "#1002F(Looks like the army and the\x01",
            "jaegers are fighting...)\x02\x03",

            "(We need to get to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_942B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94AC")

    ChrTalk(    #374
        0x102,
        (
            "#1042F(The army forces should be deployed over here...)\x02\x03",

            "(Let's leave this to them\x01",
            "and hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_94AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_952C")

    ChrTalk(    #375
        0x103,
        (
            "#022F(The army forces should be engaged\x01",
            "in combat over here...)\x02\x03",

            "(We should probably head to the castle...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_952C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95AD")

    ChrTalk(    #376
        0x107,
        (
            "#062F(Looks like the army soldiers are\x01",
            "fighting the society people...)\x02\x03",

            "(We need to hurry to the castle...!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_95AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9638")

    ChrTalk(    #377
        0x106,
        (
            "#057F(Seems like the army guys are havin'\x01",
            "it out with those damn jaegers...)\x02\x03",

            "(We should probably head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_9638")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9698")

    ChrTalk(    #378
        0x108,
        (
            "#072F(The army forces are deployed here...)\x02\x03",

            "(Then let's hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9698")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_930B end

    def Function_48_96B9(): pass

    label("Function_48_96B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96C2")
    Return()

    label("loc_96C2")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96E2")
    Call(0, 49)
    Call(0, 52)
    FadeToBright(0, 0)

    label("loc_96E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #379
        (
            "\x07\x05The sounds of gunfire and blades clashing\x01",
            "can be periodically heard from the wastern\x01",
            "city block.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D9")

    ChrTalk(    #380
        0x101,
        (
            "#1002F(Looks like the army and the\x01",
            "jaegers are fighting...)\x02\x03",

            "(We need to get to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A46")

    label("loc_97D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985A")

    ChrTalk(    #381
        0x102,
        (
            "#1042F(The army forces should be deployed over here...)\x02\x03",

            "(Let's leave this to them\x01",
            "and hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A46")

    label("loc_985A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98DA")

    ChrTalk(    #382
        0x103,
        (
            "#022F(The army forces should be engaged\x01",
            "in combat over here...)\x02\x03",

            "(We should probably head to the castle...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A46")

    label("loc_98DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_995B")

    ChrTalk(    #383
        0x107,
        (
            "#062F(Looks like the army soldiers are\x01",
            "fighting the society people...)\x02\x03",

            "(We need to hurry to the castle...!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A46")

    label("loc_995B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99E6")

    ChrTalk(    #384
        0x106,
        (
            "#057F(Seems like the army guys are havin'\x01",
            "it out with those damn jaegers...)\x02\x03",

            "(We should probably head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A46")

    label("loc_99E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A46")

    ChrTalk(    #385
        0x108,
        (
            "#072F(The army forces are deployed here...)\x02\x03",

            "(Then let's hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A46")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_48_96B9 end

    def Function_49_9A67(): pass

    label("Function_49_9A67")

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
        (0, "loc_9AE0"),
        (1, "loc_9AE6"),
        (SWITCH_DEFAULT, "loc_9AEC"),
    )


    label("loc_9AE0")

    OP_A2(0x1200)
    Jump("loc_9AEC")

    label("loc_9AE6")

    OP_A2(0x1201)
    Jump("loc_9AEC")

    label("loc_9AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9AFA")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_9AFE")

    label("loc_9AFA")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_9AFE")

    Return()

    # Function_49_9A67 end

    def Function_50_9AFF(): pass

    label("Function_50_9AFF")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9B42")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_9B60")

    label("loc_9B42")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_9B60")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_50_9AFF end

    def Function_51_9B80(): pass

    label("Function_51_9B80")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9BBF")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_9BD9")

    label("loc_9BBF")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_9BD9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_51_9B80 end

    def Function_52_9BF9(): pass

    label("Function_52_9BF9")

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

    # Function_52_9BF9 end

    def Function_53_9C52(): pass

    label("Function_53_9C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_9EF0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CBD")

    ChrTalk(    #386
        0x101,
        (
            "#1002F(We can't leave the capital right now...)\x02\x03",

            "(Let's hurry to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ECD")

    label("loc_9CBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D33")

    ChrTalk(    #387
        0x102,
        (
            "#1042F(We can't leave the capital right now...)\x02\x03",

            "(Let's hurry to the castle as soon as possible.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ECD")

    label("loc_9D33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D8F")

    ChrTalk(    #388
        0x103,
        (
            "#022F(We need every moment we can get...)\x02\x03",

            "(Let's hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ECD")

    label("loc_9D8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF4")

    ChrTalk(    #389
        0x107,
        (
            "#065F(This is the exit.)\x02\x03",

            "#062F(Right now we just need to get to the castle...!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ECD")

    label("loc_9DF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E66")

    ChrTalk(    #390
        0x106,
        (
            "#050F(This ain't the time to be hangin' around here...)\x02\x03",

            "(Gotta hurry and get to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ECD")

    label("loc_9E66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ECD")

    ChrTalk(    #391
        0x108,
        (
            "#072F(This isn't the moment to\x01",
            "waste time around here...)\x02\x03",

            "(Let's get to the castle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ECD")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_A5F3")

    label("loc_9EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F82")
    EventBegin(0x1)
    TurnDirection(0x101, 0x0, 400)

    ChrTalk(    #392
        0x101,
        (
            "#1006FRenne's somewhere in this city.\x02\x03",

            "If it's gonna come down to this,\x01",
            "we WILL find her!\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_A5F3")

    label("loc_9F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A280")
    EventBegin(0x1)
    TurnDirection(0x0, 0x1, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A014")

    ChrTalk(    #393
        0x101,
        (
            "#1006FNo way she'd have gone out of the\x01",
            "city on her own.\x02\x03",

            "First let's investigate around the East Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A262")

    label("loc_A014")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A08F")

    ChrTalk(    #394
        0x103,
        (
            "#020FIt's hard to believe she'd go out\x01",
            "of the city alone.\x02\x03",

            "For now, let's search around the East Block\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A262")

    label("loc_A08F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A114")

    ChrTalk(    #395
        0x107,
        (
            "#060FI think maybe Renne didn't leave the city.\x02\x03",

            "First let's look around the East\x01",
            "Block where we were yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A262")

    label("loc_A114")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A187")

    ChrTalk(    #396
        0x106,
        (
            "#050FI doubt she's gone outside the city.\x02\x03",

            "First, let's start searching around the\x01",
            "East Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A262")

    label("loc_A187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A206")

    ChrTalk(    #397
        0x108,
        (
            "#070FI really doubt she's left the bounds\x01",
            "of the city.\x02\x03",

            "Let's first start searching around\x01",
            "the East Block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A262")

    label("loc_A206")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A262")

    ChrTalk(    #398
        0x105,
        (
            "#040FI don't think she'd have left the city.\x02\x03",

            "Let's search the East Block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A262")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_A5F3")

    label("loc_A280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3F0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2DF")

    ChrTalk(    #399
        0x101,
        (
            "#1000FIt's already pretty late.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3D2")

    label("loc_A2DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A339")

    ChrTalk(    #400
        0x104,
        (
            "#030FIt's almost time for the sun to set.\x01",
            "Let us return to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3D2")

    label("loc_A339")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A389")

    ChrTalk(    #401
        0x108,
        (
            "#070FIt's already pretty late.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3D2")

    label("loc_A389")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D2")

    ChrTalk(    #402
        0x105,
        (
            "#040FIt's almost sunset.\x01",
            "We should return to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3D2")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_A5F3")

    label("loc_A3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5F3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A46B")

    ChrTalk(    #403
        0x101,
        (
            "#1000FWe don't have any business outside the city.\x02\x03",

            "Let's get to questioning right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5D8")

    label("loc_A46B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4E8")

    ChrTalk(    #404
        0x104,
        (
            "#030FWe still haven't finished investigating\x01",
            "the threat letters.\x02\x03",

            "Let us get to questioning immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5D8")

    label("loc_A4E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A567")

    ChrTalk(    #405
        0x108,
        (
            "#070FWe're not going to find the criminal\x01",
            "by leaving the area.\x02\x03",

            "Let's just get this questioning over with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5D8")

    label("loc_A567")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5D8")

    ChrTalk(    #406
        0x105,
        (
            "#040FWe still haven't finished investigating\x01",
            "the threat letters.\x02\x03",

            "Let us return to questioning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5D8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A5F3")

    Return()

    # Function_53_9C52 end

    def Function_54_A5F4(): pass

    label("Function_54_A5F4")

    Call(0, 60)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_A5F4 end

    def Function_55_A614(): pass

    label("Function_55_A614")

    Call(0, 60)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_A614 end

    def Function_56_A634(): pass

    label("Function_56_A634")

    Call(0, 60)
    OP_59()

    def lambda_A63F():
        OP_6D(-3370, 0, 9000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A63F)
    Fade(1000)
    SetChrPos(0x0, -3370, 0, 12430, 180)
    SetChrPos(0x1, -3370, 0, 12430, 180)
    SetChrPos(0x2, -3370, 0, 12430, 180)
    SetChrPos(0x3, -3370, 0, 12430, 180)
    SetChrPos(0x12F, -3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_A634 end

    def Function_57_A6BB(): pass

    label("Function_57_A6BB")

    Call(0, 60)
    OP_59()

    def lambda_A6C6():
        OP_6D(3370, 0, 9000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A6C6)
    Fade(1000)
    SetChrPos(0x0, 3370, 0, 12430, 180)
    SetChrPos(0x1, 3370, 0, 12430, 180)
    SetChrPos(0x2, 3370, 0, 12430, 180)
    SetChrPos(0x3, 3370, 0, 12430, 180)
    SetChrPos(0x12F, 3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_57_A6BB end

    def Function_58_A742(): pass

    label("Function_58_A742")

    Call(0, 60)
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_58_A742 end

    def Function_59_A762(): pass

    label("Function_59_A762")

    Call(0, 60)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_59_A762 end

    def Function_60_A782(): pass

    label("Function_60_A782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9FE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A811")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7B4")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_A7BB")

    label("loc_A7B4")

    TurnDirection(0x106, 0x0, 400)

    label("loc_A7BB")


    ChrTalk(    #407
        0x106,
        (
            "#050F...We gotta check what information we have.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A884")

    label("loc_A811")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A827")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_A82E")

    label("loc_A827")

    TurnDirection(0x103, 0x0, 400)

    label("loc_A82E")


    ChrTalk(    #408
        0x103,
        (
            "#020F...We need to check the info we have.\x01",
            "Let's return to the guild right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A884")

    Jump("loc_A9FB")

    label("loc_A887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A901")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8A4")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_A8AB")

    label("loc_A8A4")

    TurnDirection(0x106, 0x0, 400)

    label("loc_A8AB")


    ChrTalk(    #409
        0x106,
        (
            "#050F...We gotta check what information we have.\x01",
            "Let's get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A974")

    label("loc_A901")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A917")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_A91E")

    label("loc_A917")

    TurnDirection(0x103, 0x0, 400)

    label("loc_A91E")


    ChrTalk(    #410
        0x103,
        (
            "#020F...We need to check the info we have.\x01",
            "Let's return to the guild right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A974")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A7")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #411
        0x101,
        "#1000FYeah, absolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9D7")

    label("loc_A9A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9D7")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #412
        0x107,
        "#060FYes, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_A9D7")


    ChrTalk(    #413
        0x12F,
        "#268FAww, that's so boring.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A9FB")

    Jump("loc_AD61")

    label("loc_A9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD61")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA78")

    ChrTalk(    #414
        0x108,
        (
            "#070FIt's about time for the army lead to come.\x02\x03",

            "Let's hurry and get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD61")

    label("loc_AA78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AB03")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_AAA3")

    label("loc_AA9C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_AAA3")


    ChrTalk(    #415
        0x106,
        (
            "#050FIt's 'bout time for the army lead to come.\x02\x03",

            "Let's hurry and get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB7D")

    label("loc_AB03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB19")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_AB20")

    label("loc_AB19")

    TurnDirection(0x103, 0x0, 400)

    label("loc_AB20")


    ChrTalk(    #416
        0x103,
        (
            "#020FIt's about time for the army lead to come.\x02\x03",

            "Let's hurry and get back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB7D")

    Jump("loc_AD61")

    label("loc_AB80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AC04")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB9D")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_ABA4")

    label("loc_AB9D")

    TurnDirection(0x106, 0x0, 400)

    label("loc_ABA4")


    ChrTalk(    #417
        0x106,
        (
            "#050FIt's 'bout time for the army lead to come.\x02\x03",

            "Let's hurry and get back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC7E")

    label("loc_AC04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1A")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_AC21")

    label("loc_AC1A")

    TurnDirection(0x103, 0x0, 400)

    label("loc_AC21")


    ChrTalk(    #418
        0x103,
        (
            "#020FIt's about time for the army lead to come.\x02\x03",

            "Let's hurry and get back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACAA")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #419
        0x101,
        "#1011FOh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD35")

    label("loc_ACAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD3")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #420
        0x104,
        "#030FAh, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD35")

    label("loc_ACD3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD06")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #421
        0x105,
        "#040FYes, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD35")

    label("loc_AD06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD35")
    TurnDirection(0x0, 0xF7, 400)

    ChrTalk(    #422
        0x107,
        "#060FYes, that's true.\x02",
    )

    CloseMessageWindow()

    label("loc_AD35")


    ChrTalk(    #423
        0x12F,
        "#264FOh, we weren't going this way?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AD61")

    Return()

    # Function_60_A782 end

    def Function_61_AD62(): pass

    label("Function_61_AD62")

    SetPlaceName(0xB9)
    Return()

    # Function_61_AD62 end

    def Function_62_AD66(): pass

    label("Function_62_AD66")

    SetPlaceName(0xB0)
    Return()

    # Function_62_AD66 end

    def Function_63_AD6A(): pass

    label("Function_63_AD6A")

    SetPlaceName(0xB2)
    Return()

    # Function_63_AD6A end

    def Function_64_AD6E(): pass

    label("Function_64_AD6E")

    SetPlaceName(0xAE)
    Return()

    # Function_64_AD6E end

    def Function_65_AD72(): pass

    label("Function_65_AD72")

    SetPlaceName(0xB3)
    Return()

    # Function_65_AD72 end

    SaveToFile()

Try(main)
