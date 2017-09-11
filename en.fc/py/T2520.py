from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2520   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2520.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60075",
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
        'Dean Collins',                         # 9
        'Polly',                                # 10
        'Matron Theresa',                       # 11
        'Daniel',                               # 12
        'Mary',                                 # 13
        'Clem',                                 # 14
        'Sieg',                                 # 15
        'Fauna',                                # 16
        'Mr. Ratio',                            # 17
        'Ms. Wiola',                            # 18
        'Ms. Millia',                           # 19
        'Mr. Effort',                           # 20
        'Rhody',                                # 21
        'Kaden',                                # 22
        'Alice',                                # 23
        'Taylor',                               # 24
        'Purity',                               # 25
        'Logic',                                # 26
        'Argyle',                               # 27
        'Roy',                                  # 28
        'Monika',                               # 29
        'Thelma',                               # 30
        'Richelle',                             # 31
        'Patrick',                              # 32
        'Gerome',                               # 33
        'Nikita',                               # 34
        'Felicity',                             # 35
        'Reina',                                # 36
        'Mayor Maybelle',                       # 37
        'Duke Dunan',                           # 38
        'Butler Phillip',                       # 39
        'Nial',                                 # 40
        'Carna',                                # 41
        'Professor Alba',                       # 42
        'Ciel',                                 # 43
        'Eletta',                               # 44
        'Eva',                                  # 45
        'Seagaro',                              # 46
        'Edel',                                 # 47
        'Portos',                               # 48
        'Noria',                                # 49
        'Liz',                                  # 50
        'Antonio',                              # 51
        'Lila',                                 # 52
        'Mayor Dalmore',                        # 53
        'Visitor',                              # 54
        'Visitor',                              # 55
        'Visitor',                              # 56
        'Visitor',                              # 57
        'Visitor',                              # 58
        'Visitor',                              # 59
        'Visitor',                              # 60
        'Visitor',                              # 61
        'Visitor',                              # 62
        'CH22000',                              # 63
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02320 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01430 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH02600 ._CH',             # 0B
        'ED6_DT07/CH01360 ._CH',             # 0C
        'ED6_DT07/CH01580 ._CH',             # 0D
        'ED6_DT07/CH01590 ._CH',             # 0E
        'ED6_DT07/CH01370 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
        'ED6_DT07/CH01080 ._CH',             # 11
        'ED6_DT07/CH01360 ._CH',             # 12
        'ED6_DT07/CH01590 ._CH',             # 13
        'ED6_DT07/CH02360 ._CH',             # 14
        'ED6_DT07/CH02140 ._CH',             # 15
        'ED6_DT07/CH02470 ._CH',             # 16
        'ED6_DT07/CH02060 ._CH',             # 17
        'ED6_DT07/CH01240 ._CH',             # 18
        'ED6_DT07/CH02050 ._CH',             # 19
        'ED6_DT07/CH01540 ._CH',             # 1A
        'ED6_DT07/CH01170 ._CH',             # 1B
        'ED6_DT07/CH01210 ._CH',             # 1C
        'ED6_DT07/CH01040 ._CH',             # 1D
        'ED6_DT07/CH01130 ._CH',             # 1E
        'ED6_DT07/CH01680 ._CH',             # 1F
        'ED6_DT07/CH01030 ._CH',             # 20
        'ED6_DT07/CH02410 ._CH',             # 21
        'ED6_DT07/CH02370 ._CH',             # 22
        'ED6_DT07/CH02500 ._CH',             # 23
        'ED6_DT06/CH20021 ._CH',             # 24
        'ED6_DT07/CH01200 ._CH',             # 25
        'ED6_DT07/CH02480 ._CH',             # 26
        'ED6_DT07/CH01120 ._CH',             # 27
        'ED6_DT07/CH01030 ._CH',             # 28
        'ED6_DT07/CH01130 ._CH',             # 29
        'ED6_DT07/CH01140 ._CH',             # 2A
        'ED6_DT07/CH01100 ._CH',             # 2B
        'ED6_DT07/CH01180 ._CH',             # 2C
        'ED6_DT07/CH01470 ._CH',             # 2D
        'ED6_DT07/CH01770 ._CH',             # 2E
        'ED6_DT07/CH01780 ._CH',             # 2F
        'ED6_DT07/CH02363 ._CH',             # 30
        'ED6_DT07/CH01373 ._CH',             # 31
        'ED6_DT07/CH01213 ._CH',             # 32
        'ED6_DT07/CH01593 ._CH',             # 33
        'ED6_DT07/CH01043 ._CH',             # 34
        'ED6_DT07/CH01033 ._CH',             # 35
        'ED6_DT07/CH01363 ._CH',             # 36
        'ED6_DT07/CH01690 ._CH',             # 37
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02320P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01430P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH02600P._CP',             # 0B
        'ED6_DT07/CH01360P._CP',             # 0C
        'ED6_DT07/CH01580P._CP',             # 0D
        'ED6_DT07/CH01590P._CP',             # 0E
        'ED6_DT07/CH01370P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
        'ED6_DT07/CH01080P._CP',             # 11
        'ED6_DT07/CH01360P._CP',             # 12
        'ED6_DT07/CH01590P._CP',             # 13
        'ED6_DT07/CH02360P._CP',             # 14
        'ED6_DT07/CH02140P._CP',             # 15
        'ED6_DT07/CH02470P._CP',             # 16
        'ED6_DT07/CH02060P._CP',             # 17
        'ED6_DT07/CH01240P._CP',             # 18
        'ED6_DT07/CH02050P._CP',             # 19
        'ED6_DT07/CH01540P._CP',             # 1A
        'ED6_DT07/CH01170P._CP',             # 1B
        'ED6_DT07/CH01210P._CP',             # 1C
        'ED6_DT07/CH01040P._CP',             # 1D
        'ED6_DT07/CH01210P._CP',             # 1E
        'ED6_DT07/CH01680P._CP',             # 1F
        'ED6_DT07/CH01030P._CP',             # 20
        'ED6_DT07/CH02410P._CP',             # 21
        'ED6_DT07/CH02370P._CP',             # 22
        'ED6_DT07/CH02500P._CP',             # 23
        'ED6_DT06/CH20021P._CP',             # 24
        'ED6_DT07/CH01200P._CP',             # 25
        'ED6_DT07/CH02480P._CP',             # 26
        'ED6_DT07/CH01120P._CP',             # 27
        'ED6_DT07/CH01030P._CP',             # 28
        'ED6_DT07/CH01130P._CP',             # 29
        'ED6_DT07/CH01140P._CP',             # 2A
        'ED6_DT07/CH01100P._CP',             # 2B
        'ED6_DT07/CH01180P._CP',             # 2C
        'ED6_DT07/CH01470P._CP',             # 2D
        'ED6_DT07/CH01770P._CP',             # 2E
        'ED6_DT07/CH01780P._CP',             # 2F
        'ED6_DT07/CH02363P._CP',             # 30
        'ED6_DT07/CH01373P._CP',             # 31
        'ED6_DT07/CH01213P._CP',             # 32
        'ED6_DT07/CH01593P._CP',             # 33
        'ED6_DT07/CH01043P._CP',             # 34
        'ED6_DT07/CH01033P._CP',             # 35
        'ED6_DT07/CH01363P._CP',             # 36
        'ED6_DT07/CH01690P._CP',             # 37
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 0,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
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
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
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
        X                   = 41400,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 89260,
        Z                   = 0,
        Y                   = 1520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -2900,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 0,
        Y                   = 35500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 28800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -6000,
        Z                   = 0,
        Y                   = 700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 82700,
        Z                   = 0,
        Y                   = 33000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 90900,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 92300,
        Z                   = 0,
        Y                   = 33400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 85900,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 83500,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -3900,
        Z                   = 0,
        Y                   = 34700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 0,
        Y                   = 34100,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 43480,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 2700,
        Z                   = 0,
        Y                   = 32500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 89800,
        Z                   = 0,
        Y                   = 29200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 88400,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = -6100,
        Z                   = 0,
        Y                   = 34900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 3060,
        Z                   = 0,
        Y                   = 30300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 30900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 32600,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 300,
        Z                   = 0,
        Y                   = 29800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 3090,
        Z                   = 0,
        Y                   = 32340,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = -5900,
        Z                   = 0,
        Y                   = -300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 41520,
        Z                   = 0,
        Y                   = 1170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 30590,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 38380,
        Z                   = 0,
        Y                   = 1600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 26440,
        Z                   = 0,
        Y                   = -160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 39730,
        Z                   = 0,
        Y                   = 31370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 28810,
        Z                   = 0,
        Y                   = 31500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 45020,
        Z                   = 0,
        Y                   = 30260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 57380,
        Z                   = 0,
        Y                   = 30950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = 43840,
        Z                   = 0,
        Y                   = 35940,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 24710,
        Z                   = 0,
        Y                   = 29820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835044,
        ChipIndex           = 0x24,
        NpcIndex            = 0x166,
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
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 76,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 77,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 78,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 79,
    )


    DeclActor(
        TriggerX            = 41160,
        TriggerZ            = 0,
        TriggerY            = 6230,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 48200,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 48200,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 62,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31580,
        TriggerZ            = 0,
        TriggerY            = 1450,
        TriggerRange        = 800,
        ActorX              = 31580,
        ActorZ              = 1000,
        ActorY              = 1450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 63,
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
        TalkFunctionIndex   = 64,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57380,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 57380,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 65,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31630,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 31630,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 66,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3420,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 3420,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3570,
        TriggerZ            = 0,
        TriggerY            = 34450,
        TriggerRange        = 800,
        ActorX              = 3570,
        ActorZ              = 1200,
        ActorY              = 34450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 68,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 790,
        TriggerZ            = 0,
        TriggerY            = 35530,
        TriggerRange        = 800,
        ActorX              = 790,
        ActorZ              = 1200,
        ActorY              = 35530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 69,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5010,
        TriggerZ            = 0,
        TriggerY            = 29180,
        TriggerRange        = 800,
        ActorX              = -5010,
        ActorZ              = 1200,
        ActorY              = 29180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 70,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1970,
        TriggerZ            = 0,
        TriggerY            = 30780,
        TriggerRange        = 800,
        ActorX              = -1970,
        ActorZ              = 1200,
        ActorY              = 30780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 71,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93560,
        TriggerZ            = 0,
        TriggerY            = 33350,
        TriggerRange        = 800,
        ActorX              = 93560,
        ActorZ              = 1000,
        ActorY              = 33350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 72,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87220,
        TriggerZ            = 0,
        TriggerY            = 34060,
        TriggerRange        = 800,
        ActorX              = 87220,
        ActorZ              = 1000,
        ActorY              = 34060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85030,
        TriggerZ            = 0,
        TriggerY            = 33920,
        TriggerRange        = 800,
        ActorX              = 85030,
        ActorZ              = 1000,
        ActorY              = 33920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 74,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_C06",          # 00, 0
        "Function_1_1308",         # 01, 1
        "Function_2_1340",         # 02, 2
        "Function_3_14EE",         # 03, 3
        "Function_4_153B",         # 04, 4
        "Function_5_1640",         # 05, 5
        "Function_6_1664",         # 06, 6
        "Function_7_1688",         # 07, 7
        "Function_8_16AC",         # 08, 8
        "Function_9_16D0",         # 09, 9
        "Function_10_1EE2",        # 0A, 10
        "Function_11_1EE7",        # 0B, 11
        "Function_12_289D",        # 0C, 12
        "Function_13_2BF5",        # 0D, 13
        "Function_14_2FB4",        # 0E, 14
        "Function_15_350C",        # 0F, 15
        "Function_16_393E",        # 10, 16
        "Function_17_3B3B",        # 11, 17
        "Function_18_3B40",        # 12, 18
        "Function_19_3FB6",        # 13, 19
        "Function_20_426E",        # 14, 20
        "Function_21_4504",        # 15, 21
        "Function_22_4597",        # 16, 22
        "Function_23_4E87",        # 17, 23
        "Function_24_4ECB",        # 18, 24
        "Function_25_52DC",        # 19, 25
        "Function_26_53D7",        # 1A, 26
        "Function_27_5548",        # 1B, 27
        "Function_28_55AB",        # 1C, 28
        "Function_29_55FA",        # 1D, 29
        "Function_30_574F",        # 1E, 30
        "Function_31_5914",        # 1F, 31
        "Function_32_5A0A",        # 20, 32
        "Function_33_5A91",        # 21, 33
        "Function_34_5EF7",        # 22, 34
        "Function_35_62D3",        # 23, 35
        "Function_36_63EB",        # 24, 36
        "Function_37_656F",        # 25, 37
        "Function_38_689B",        # 26, 38
        "Function_39_68DB",        # 27, 39
        "Function_40_6A81",        # 28, 40
        "Function_41_6AD4",        # 29, 41
        "Function_42_6C5C",        # 2A, 42
        "Function_43_6CBD",        # 2B, 43
        "Function_44_6CE2",        # 2C, 44
        "Function_45_6D16",        # 2D, 45
        "Function_46_6D8D",        # 2E, 46
        "Function_47_6E4E",        # 2F, 47
        "Function_48_6F53",        # 30, 48
        "Function_49_70F6",        # 31, 49
        "Function_50_7563",        # 32, 50
        "Function_51_766E",        # 33, 51
        "Function_52_7736",        # 34, 52
        "Function_53_7851",        # 35, 53
        "Function_54_7901",        # 36, 54
        "Function_55_798C",        # 37, 55
        "Function_56_7A38",        # 38, 56
        "Function_57_7AEC",        # 39, 57
        "Function_58_7B89",        # 3A, 58
        "Function_59_7C2F",        # 3B, 59
        "Function_60_8006",        # 3C, 60
        "Function_61_8FE2",        # 3D, 61
        "Function_62_904A",        # 3E, 62
        "Function_63_90C1",        # 3F, 63
        "Function_64_9127",        # 40, 64
        "Function_65_918A",        # 41, 65
        "Function_66_91FA",        # 42, 66
        "Function_67_9265",        # 43, 67
        "Function_68_92B9",        # 44, 68
        "Function_69_9319",        # 45, 69
        "Function_70_939B",        # 46, 70
        "Function_71_93F2",        # 47, 71
        "Function_72_9451",        # 48, 72
        "Function_73_94E9",        # 49, 73
        "Function_74_957A",        # 4A, 74
        "Function_75_ABD9",        # 4B, 75
        "Function_76_ABDD",        # 4C, 76
        "Function_77_ABE1",        # 4D, 77
        "Function_78_ABE5",        # 4E, 78
        "Function_79_ABE9",        # 4F, 79
    )


    def Function_0_C06(): pass

    label("Function_0_C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C14")
    OP_A3(0x3FA)
    Event(0, 59)

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_C7B")
    SetChrPos(0x10, 5320, 250, 2110, 270)
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x14, 400, 0, 0, 90)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x19, -2900, 0, 30000, 90)
    Jump("loc_12BA")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_CBC")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1D, 0x80)
    Jump("loc_12BA")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_F31")
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 42090, 0, 3930, 45)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 42970, 0, 2640, 0)
    SetChrPos(0x17, -1590, 0, 34700, 0)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 51)
    SetChrPos(0x1E, -6000, 100, 700, 90)
    OP_44(0x1E, 0xFF)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x10)
    ClearChrFlags(0x32, 0x80)
    SetChrChipByIndex(0x32, 52)
    SetChrPos(0x32, -5960, 0, 3010, 90)
    OP_44(0x32, 0xFF)
    SetChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x10)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, -4000, 0, 4100, 270)
    SetChrChipByIndex(0x31, 53)
    OP_44(0x31, 0xFF)
    SetChrFlags(0x31, 0x4)
    SetChrFlags(0x31, 0x10)
    SetChrPos(0x14, -70, 0, 3050, 270)
    SetChrChipByIndex(0x14, 54)
    OP_44(0x14, 0xFF)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 89110, 0, 29220, 90)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 89160, 0, 34290, 0)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 85890, 0, 32890, 315)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 90550, 0, 29250, 270)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x2A, 0x80)
    SetChrPos(0x2A, 31660, 0, 100, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 32619, 0, 320, 270)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jump("loc_12BA")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1143")
    SetChrPos(0x11, -6910, 0, 33220, 90)
    SetChrPos(0x12, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42940, 0, 1070, 270)
    SetChrFlags(0x8, 0x10)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x10, 2790, 0, 5460, 225)
    SetChrPos(0x15, 4500, 250, 2970, 270)
    SetChrPos(0x16, -990, 0, -1260, 0)
    SetChrChipByIndex(0x16, 47)
    OP_43(0x16, 0x0, 0x0, 0x3)
    SetChrPos(0x18, -4990, 0, 5010, 180)
    SetChrChipByIndex(0x18, 46)
    OP_43(0x18, 0x0, 0x0, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x24, 48)
    SetChrPos(0x24, -4019, 100, 3080, 270)
    OP_44(0x24, 0xFF)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, -5040, 100, 2050, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrChipByIndex(0x2C, 50)
    SetChrPos(0x2C, -130, 0, 4000, 270)
    OP_44(0x2C, 0xFF)
    SetChrFlags(0x2C, 0x4)
    SetChrFlags(0x2C, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -1960, 0, -300, 90)
    SetChrChipByIndex(0x1C, 49)
    OP_44(0x1C, 0xFF)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x19, 1300, 0, 28510, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x10)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_END)), "loc_1140")
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    SetChrPos(0x29, -1680, 0, 34680, 0)
    ClearChrFlags(0x29, 0x80)

    label("loc_1140")

    Jump("loc_12BA")

    label("loc_1143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1199")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x15, -5200, 0, 2050, 0)
    SetChrPos(0x16, 4500, 250, 4019, 270)
    SetChrPos(0x19, 790, 0, 34680, 0)
    Jump("loc_12BA")

    label("loc_1199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_11C8")
    SetChrPos(0x11, 5300, 250, 32080, 267)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_12BA")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_11FF")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_123B")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_123B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_127C")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_12BA")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_12BA")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D4")
    OP_A2(0x443)

    label("loc_12D4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_12E0"),
        (SWITCH_DEFAULT, "loc_12F6"),
    )


    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F3")
    OP_A2(0x432)
    Event(0, 60)

    label("loc_12F3")

    Jump("loc_12F6")

    label("loc_12F6")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_C06 end

    def Function_1_1308(): pass

    label("Function_1_1308")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_131B")
    OP_65(0x1, 0x1)

    label("loc_131B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_132F")
    OP_64(0x1, 0x1)
    SetChrFlags(0x3E, 0x80)

    label("loc_132F")

    OP_75(0x6, 0x0, 0x0)
    OP_74(0x6, 0x0, 0x0)
    Return()

    # Function_1_1308 end

    def Function_2_1340(): pass

    label("Function_2_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_1371")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_135F")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1371")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1371")
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1371")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1396")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_14D8")

    label("loc_1396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AF")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_14D8")

    label("loc_13AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_14D8")

    label("loc_13C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_13E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FA")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_14D8")

    label("loc_13FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1413")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_14D8")

    label("loc_1413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142C")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_14D8")

    label("loc_142C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1445")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_14D8")

    label("loc_1445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145E")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_14D8")

    label("loc_145E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1477")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_14D8")

    label("loc_1477")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_14D8")

    label("loc_1490")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A9")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_14D8")

    label("loc_14A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C2")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_14D8")

    label("loc_14C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D8")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_14D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14ED")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_14D8")

    label("loc_14ED")

    Return()

    # Function_2_1340 end

    def Function_3_14EE(): pass

    label("Function_3_14EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_153A")
    OP_8E(0xFE, 0xFFFFEC5A, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFFC22, 0x0, 0xFFFFFB14, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_3_14EE")

    label("loc_153A")

    Return()

    # Function_3_14EE end

    def Function_4_153B(): pass

    label("Function_4_153B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9EC, 0x0, 0xB86, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x7C6, 0x0, 0xC12, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0xD98, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D2, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0x1356, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFEC82, 0x0, 0x1392, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(3000)
    Jump("Function_4_153B")

    label("loc_163F")

    Return()

    # Function_4_153B end

    def Function_5_1640(): pass

    label("Function_5_1640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1663")
    OP_8D(0xFE, 24420, 1500, 29350, -1300, 1500)
    Jump("Function_5_1640")

    label("loc_1663")

    Return()

    # Function_5_1640 end

    def Function_6_1664(): pass

    label("Function_6_1664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1687")
    OP_8D(0xFE, 38740, 33660, 43330, 28250, 1500)
    Jump("Function_6_1664")

    label("loc_1687")

    Return()

    # Function_6_1664 end

    def Function_7_1688(): pass

    label("Function_7_1688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16AB")
    OP_8D(0xFE, 42670, 31640, 49420, 28690, 2000)
    Jump("Function_7_1688")

    label("loc_16AB")

    Return()

    # Function_7_1688 end

    def Function_8_16AC(): pass

    label("Function_8_16AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16CF")
    OP_8D(0xFE, 23100, 31490, 27030, 28520, 3000)
    Jump("Function_8_16AC")

    label("loc_16CF")

    Return()

    # Function_8_16AC end

    def Function_9_16D0(): pass

    label("Function_9_16D0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1848")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AF")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "#780FAh, hello there.\x02\x03",

            "First of all, I'd like to say how\x01",
            "relieved I am that the criminals\x01",
            "have been caught.\x02\x03",

            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1845")

    label("loc_17AF")


    ChrTalk(    #1
        0xFE,
        (
            "#780FThank goodness that the\x01",
            "attackers have been arrested.\x02\x03",

            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1845")

    Jump("loc_1EDE")

    label("loc_1848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_195E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "#780FAh, you're here.\x02\x03",

            "I heard about Matron Theresa\x01",
            "and the children.\x02\x03",

            "They certainly didn't deserve this.\x02\x03",

            "What words are there to describe\x01",
            "such a thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_195B")

    label("loc_18FD")


    ChrTalk(    #3
        0xFE,
        (
            "#780FI heard about Matron Theresa\x01",
            "and her children.\x02\x03",

            "They certainly didn't deserve this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195B")

    Jump("loc_1EDE")

    label("loc_195E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A64")
    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",

            "The play was magnificent. Joshua's\x01",
            "portrayal of Princess Cecilia was\x01",
            "particularly memorable.\x02\x03",

            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF7")

    label("loc_1A64")


    ChrTalk(    #5
        0xFE,
        (
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",

            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF7")

    Jump("loc_1EDE")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1C14")
    ClearChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAF")
    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "#780FAh, hello there. Everything's been\x01",
            "quite a big success.\x02\x03",

            "I'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C11")

    label("loc_1BAF")


    ChrTalk(    #7
        0xFE,
        (
            "#780FI'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C11")

    Jump("loc_1EDE")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1DE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2A")
    OP_A2(0x457)
    OP_4A(0x34, 255)

    ChrTalk(    #8
        0x8,
        (
            "#781FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",

            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x34,
        (
            "#661FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",

            "I expect that today will be\x01",
            "quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x34, 255)
    Jump("loc_1DE1")

    label("loc_1D2A")


    ChrTalk(    #10
        0x8,
        (
            "#781FI'd like to get your input on some\x01",
            "of the school's affairs, if you have\x01",
            "the time.\x02\x03",

            "Though we may be chartered by\x01",
            "the monarchy, it's still important\x01",
            "to hear the local views.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE1")

    Jump("loc_1EDE")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1EDE")

    ChrTalk(    #11
        0xFE,
        (
            "#780FDon't worry, I'll make sure you have a place\x01",
            "to stay. And I'm greatly looking forward to\x01",
            "your...erm...'transformation'...\x02\x03",

            "There's also a cafeteria on campus, which\x01",
            "you may use at your leisure. Just relax,\x01",
            "and work hard on the play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDE")

    TalkEnd(0x8)
    Return()

    # Function_9_16D0 end

    def Function_10_1EE2(): pass

    label("Function_10_1EE2")

    Call(0, 11)
    Return()

    # Function_10_1EE2 end

    def Function_11_1EE7(): pass

    label("Function_11_1EE7")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6B")
    OP_A2(0x2)

    ChrTalk(    #12
        0xF,
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xF,
        (
            "Classes just ended, so the students\x01",
            "should be milling about any moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8A")

    label("loc_1F6B")


    ChrTalk(    #14
        0xF,
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    label("loc_1F8A")

    Jump("loc_2899")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(    #15
        0xF,
        (
            "Ha ha...the festival was a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "I always worry that the people\x01",
            "with children will lose track of\x01",
            "them in the crowd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(    #17
        0xF,
        (
            "Success! This is possibly our\x01",
            "best turnout yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "Though I do always worry that the people\x01",
            "with children will lose track of them in\x01",
            "the crowd. But so far...no fatalities!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E4")
    OP_A2(0x2)

    ChrTalk(    #19
        0xF,
        (
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "The play's scheduled to be held\x01",
            "in the auditorium this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        (
            "The Student Council has set up the\x01",
            "cafeteria as the rest area, so please,\x01",
            "feel free to relax there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2270")

    label("loc_21E4")


    ChrTalk(    #22
        0xF,
        (
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "The play's scheduled to be held\x01",
            "in the auditorium this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2270")

    Jump("loc_2899")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230F")
    OP_A2(0x2)

    ChrTalk(    #24
        0xF,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xF,
        (
            "It looks like we'll have more\x01",
            "attendees tomorrow than\x01",
            "ever before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234E")

    label("loc_230F")


    ChrTalk(    #26
        0xF,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234E")

    Jump("loc_2899")

    label("loc_2351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_244E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240B")
    OP_A2(0x2)

    ChrTalk(    #27
        0xF,
        (
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        "It's almost festival time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        (
            "I hope all of the students are\x01",
            "trying their hardest for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_240B")


    ChrTalk(    #30
        0xF,
        (
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244B")

    Jump("loc_2899")

    label("loc_244E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255C")
    OP_A2(0x2)

    ChrTalk(    #31
        0xF,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#040FPardon me, Fauna...I just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        "Ha ha, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xF,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xF,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        (
            "#040FOh, all right. I'll go and see\x01",
            "him now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C5")

    label("loc_255C")


    ChrTalk(    #37
        0xF,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    label("loc_25C5")

    Jump("loc_2899")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_26C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A0")
    OP_A2(0x2)

    ChrTalk(    #39
        0xF,
        (
            "Hello, Kloe. Are you already done\x01",
            "with your off-campus errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#040FOh, not yet...\x02\x03",

            "I'm sorry, but I still have some\x01",
            "errands left to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "That's fine. Just take care\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_26A0")


    ChrTalk(    #42
        0xF,
        "Take care of yourself, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_26C2")

    Jump("loc_2899")

    label("loc_26C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2744")

    ChrTalk(    #43
        0xF,
        "Oh, did you want a guided tour?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "I'm terribly sorry, but I can't\x01",
            "show you around while class\x01",
            "is in session.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2848")
    OP_A2(0x2)

    ChrTalk(    #45
        0xF,
        (
            "Oh, hello, Kloe. Are you back\x01",
            "to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        (
            "#040FNo...I'm just showing some folks\x01",
            "around on the way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "I see...well, since this is your\x01",
            "vacation, make sure you let\x01",
            "your hair down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        "#040FI will...thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_2848")


    ChrTalk(    #49
        0xF,
        (
            "Since this is your vacation,\x01",
            "make sure you let your hair\x01",
            "down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2899")

    TalkEnd(0xF)
    Return()

    # Function_11_1EE7 end

    def Function_12_289D(): pass

    label("Function_12_289D")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_28EE")

    ChrTalk(    #50
        0xFE,
        (
            "Class may be over, but I still\x01",
            "get questions from my students.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_28EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2963")

    ChrTalk(    #51
        0xFE,
        (
            "Hmm...my class has done a\x01",
            "fine job on the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "They really put a lot of work\x01",
            "into this set.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_2963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_29D9")

    ChrTalk(    #53
        0xFE,
        (
            "The lead roles will be played\x01",
            "by students, will they not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Everyone's even more active\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_29D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB0")
    OP_A2(0x3)

    ChrTalk(    #55
        0xFE,
        (
            "You kids came from Rolent,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I'm actually from there, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Speaking of which, my parents will\x01",
            "be visiting to attend the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "It's good that they were invited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B3F")

    label("loc_2AB0")


    ChrTalk(    #59
        0xFE,
        (
            "Ah, yes...I had a chance to\x01",
            "watch the rehearsals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I'm quite looking forward to\x01",
            "the performance. The, uh,\x01",
            "princess is something else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3F")

    Jump("loc_2BF1")

    label("loc_2B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2BF1")

    ChrTalk(    #61
        0xFE,
        (
            "With the festival coming up, the\x01",
            "kids practically vibrate in their\x01",
            "seats when class is almost out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Ha ha...but I suppose there's\x01",
            "nothing to be done about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF1")

    TalkEnd(0x10)
    Return()

    # Function_12_289D end

    def Function_13_2BF5(): pass

    label("Function_13_2BF5")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C58")
    OP_A2(0x4)

    ChrTalk(    #63
        0xFE,
        "Let's see...this problem here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "How do you do it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_2C8A")

    label("loc_2C58")


    ChrTalk(    #66
        0xFE,
        (
            "Wow, the students here are\x01",
            "really dedicated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8A")

    Jump("loc_2FB0")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(    #67
        0xFE,
        (
            "Ahh, I'm so bored...I wonder how\x01",
            "much longer it will be until the\x01",
            "play starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Good thing you two seem like\x01",
            "the really reliable sort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB0")

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDC")
    OP_A2(0x4)

    ChrTalk(    #69
        0xFE,
        "Hmm...my class is fairly low-key...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "To be honest, I think the research\x01",
            "periodical is pretty plain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "But it's okay. I'm just glad we\x01",
            "have readers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0B")

    label("loc_2DDC")


    ChrTalk(    #72
        0xFE,
        "I don't want to lose to Millia's class...\x02",
    )

    CloseMessageWindow()

    label("loc_2E0B")

    Jump("loc_2FB0")

    label("loc_2E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F68")
    OP_A2(0x4)

    ChrTalk(    #73
        0xFE,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#040FHello, Ms. Wiola.\x02\x03",

            "I'm sorry I missed your class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Ha ha...you don't need to worry\x01",
            "about that, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "You did have important business\x01",
            "to attend to, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "If you stop by the faculty lounge later,\x01",
            "I can give you a printout of the\x01",
            "work you missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#040FYes, ma'am. I will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB0")

    label("loc_2F68")


    ChrTalk(    #79
        0xFE,
        (
            "Now, then...I suppose I should get\x01",
            "started on grading these tests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB0")

    TalkEnd(0x11)
    Return()

    # Function_13_2BF5 end

    def Function_14_2FB4(): pass

    label("Function_14_2FB4")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(    #80
        0xFE,
        (
            "I've been put in charge of writing\x01",
            "up the entrance examinations\x01",
            "for this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "I look forward to the challenge.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3508")

    label("loc_3049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_31B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3138")
    OP_A2(0x5)

    ChrTalk(    #83
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "The students in that class are\x01",
            "impressive...though the same\x01",
            "can't be said for the teacher.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B2")

    label("loc_3138")


    ChrTalk(    #86
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B2")

    Jump("loc_3508")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3214")

    ChrTalk(    #88
        0xFE,
        (
            "Have you seen the size\x01",
            "of the crowd?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "I wonder if they're all on vacation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3508")

    label("loc_3214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_331C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C9")
    OP_A2(0x5)

    ChrTalk(    #90
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I'll do my best to keep my criticisms\x01",
            "to myself...as valid as they may be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3319")

    label("loc_32C9")


    ChrTalk(    #92
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3319")

    Jump("loc_3508")

    label("loc_331C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343E")
    OP_A2(0x5)

    ChrTalk(    #93
        0xFE,
        (
            "Everyone tends to slack off in\x01",
            "the lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I suppose all the instruction in\x01",
            "the world can't change that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3508")

    label("loc_343E")


    ChrTalk(    #96
        0xFE,
        (
            "Everyone tends to slack off in the\x01",
            "lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3508")

    TalkEnd(0x12)
    Return()

    # Function_14_2FB4 end

    def Function_15_350C(): pass

    label("Function_15_350C")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_358D")

    ChrTalk(    #98
        0xFE,
        "I should make my rounds, soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The students are generally\x01",
            "well-behaved enough to not\x01",
            "require me to hover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393A")

    label("loc_358D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_36FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3634")

    ChrTalk(    #100
        0xFE,
        (
            "Ah, thanks for everything you\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I don't really have anything\x01",
            "I need to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'm just staying here,\x01",
            "in case I'm needed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3634")


    ChrTalk(    #103
        0xFE,
        (
            "I heard some students talking\x01",
            "yesterday about having seen\x01",
            "monsters in the old building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'll be making sure everything is\x01",
            "locked up tight before my rounds,\x01",
            "just to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F7")

    Jump("loc_393A")

    label("loc_36FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_389D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F2")
    OP_A2(0x6)

    ChrTalk(    #105
        0xFE,
        (
            "There are three major courses\x01",
            "offered at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389A")

    label("loc_37F2")


    ChrTalk(    #108
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389A")

    Jump("loc_393A")

    label("loc_389D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_393A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3910")
    OP_A2(0x6)

    ChrTalk(    #110
        0xFE,
        "Hey, aren't you students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Class is in session. You'll need\x01",
            "a pass to go off-campus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393A")

    label("loc_3910")


    ChrTalk(    #112
        0xFE,
        "You'll need a pass to go off-campus.\x02",
    )

    CloseMessageWindow()

    label("loc_393A")

    TalkEnd(0x13)
    Return()

    # Function_15_350C end

    def Function_16_393E(): pass

    label("Function_16_393E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C3")
    OP_A2(0x7)

    ChrTalk(    #113
        0xFE,
        (
            "Ahhh...finally, classes are done\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FD")

    label("loc_39C3")


    ChrTalk(    #115
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FD")

    Jump("loc_3B37")

    label("loc_3A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB4")
    OP_A2(0x7)

    ChrTalk(    #116
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "Yep, I'm feeling good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B37")

    label("loc_3AB4")


    ChrTalk(    #119
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B37")

    TalkEnd(0x14)
    Return()

    # Function_16_393E end

    def Function_17_3B3B(): pass

    label("Function_17_3B3B")

    Call(0, 18)
    Return()

    # Function_17_3B3B end

    def Function_18_3B40(): pass

    label("Function_18_3B40")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3B4D")
    Jump("loc_3BC5")

    label("loc_3B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3BC5")
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

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB1")
    OP_0D()
    OP_A9(0x31)
    OP_56(0x0)
    TalkEnd(0x15)
    Return()

    label("loc_3BB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC2")
    TalkEnd(0x15)
    Return()

    label("loc_3BC2")

    Jump("loc_3BC5")

    label("loc_3BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3C25")

    ChrTalk(    #121
        0x15,
        "Okay, time for the club activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x15,
        "I've GOT to finish this painting today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3CBB")

    ChrTalk(    #123
        0x15,
        (
            "Since I'm working on the coffee house,\x01",
            "I've got to push myself! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x15,
        "This is pretty tough...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D00")
    OP_A2(0x8)

    ChrTalk(    #125
        0x15,
        (
            "Is the guest at that table\x01",
            "a real maid...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D64")

    label("loc_3D00")


    ChrTalk(    #126
        0x15,
        (
            "Ugh...staying up all night has left\x01",
            "me completely drained. Or is that\x01",
            "the caffeine withdrawal?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D64")

    Jump("loc_3FB2")

    label("loc_3D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_3E57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFE")
    OP_A2(0x8)

    ChrTalk(    #127
        0x15,
        (
            "Whoa! What the hell?!\x01",
            "This is a cappuccino...\x01",
            "I ordered an espresso! Nooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x15,
        (
            "I'll never finish up in time\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E54")

    label("loc_3DFE")


    ChrTalk(    #129
        0x15,
        "Hmm...maybe if I work all night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x15,
        (
            "Ahhh...that should give me\x01",
            "plenty of time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E54")

    Jump("loc_3FB2")

    label("loc_3E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7B")
    OP_A2(0x8)

    ChrTalk(    #131
        0x15,
        (
            "Hmmhmmhmmmmm... ♪\x01",
            "They've got an awful lot of coffee... ♪\x01",
            "An awful lot of coffee... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x15,
        (
            "I'm making outfits to wear at\x01",
            "the food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x15,
        (
            "I've got to really throw myself\x01",
            "into this! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x15,
        "I love making stuff like this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3F7B")


    ChrTalk(    #135
        0x15,
        (
            "I've got to make decorations for\x01",
            "the room, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB2")

    TalkEnd(0x15)
    Return()

    # Function_18_3B40 end

    def Function_19_3FB6(): pass

    label("Function_19_3FB6")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(    #136
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I'd be glad to show you to\x01",
            "your seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426A")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4056")

    ChrTalk(    #138
        0xFE,
        "Hee hee...isn't this a cute outfit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Kaden's been making a lot of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_426A")

    label("loc_4056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4130")

    ChrTalk(    #140
        0xFE,
        (
            "He thought we had more time than we actually\x01",
            "do. Thankfully, with enough coffee in him, we\x01",
            "can still make the deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "So worry not, we'll be ready!\x01",
            "I want this to be the cutest\x01",
            "little place ever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426A")

    label("loc_4130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_426A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F4")
    OP_A2(0x9)

    ChrTalk(    #142
        0xFE,
        (
            "Kaden's really good with his hands,\x01",
            "and if you give him a little coffee,\x01",
            "then he can do just about anything! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Maybe I can get him to make\x01",
            "some stuffed dolls next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426A")

    label("loc_41F4")


    ChrTalk(    #144
        0xFE,
        (
            "Despite the fact that he's appearing\x01",
            "in the play, he still managed to find\x01",
            "the time to make maid outfits for us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426A")

    TalkEnd(0x16)
    Return()

    # Function_19_3FB6 end

    def Function_20_426E(): pass

    label("Function_20_426E")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_43A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4353")
    OP_A2(0xA)

    ChrTalk(    #145
        0xFE,
        (
            "I didn't really understand the\x01",
            "lesson in my last class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Umm...I thought maybe I should\x01",
            "ask some questions, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the faculty lounge once class is over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A2")

    label("loc_4353")


    ChrTalk(    #148
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the faculty lounge once class is over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A2")

    Jump("loc_4500")

    label("loc_43A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449F")
    OP_A2(0xA)

    ChrTalk(    #149
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "My class is doing either a tea house or a\x01",
            "haunted house. Not sure which, though,\x01",
            "frankly I think there's cross-over potential.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4500")

    label("loc_449F")


    ChrTalk(    #152
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    label("loc_4500")

    TalkEnd(0x17)
    Return()

    # Function_20_426E end

    def Function_21_4504(): pass

    label("Function_21_4504")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_4538")

    ChrTalk(    #154
        0xFE,
        "Welcome to the Fontana Tea House.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4593")

    label("loc_4538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4593")

    ChrTalk(    #155
        0xFE,
        (
            "I'm kind of embarrassed to be\x01",
            "dressed like this, but it is for\x01",
            "the festival...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4593")

    TalkEnd(0x18)
    Return()

    # Function_21_4504 end

    def Function_22_4597(): pass

    label("Function_22_4597")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_45D3")

    ChrTalk(    #156
        0xFE,
        (
            "Hmm...today's lesson was\x01",
            "very worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E83")

    label("loc_45D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_478E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B1")
    OP_A2(0xC)

    ChrTalk(    #157
        0xFE,
        "Man, being a senior is rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I understand the need to enjoy oneself,\x01",
            "but at the end of the day, I still need to\x01",
            "hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "Getting good grades is paramount.\x02",
    )

    CloseMessageWindow()
    Jump("loc_478B")

    label("loc_46B1")


    ChrTalk(    #160
        0xFE,
        (
            "There are a great many alumni\x01",
            "coming, as well as the general\x01",
            "audience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I understand the need to engage in outside\x01",
            "activities, but at the end of the day, I still\x01",
            "need to hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478B")

    Jump("loc_4E83")

    label("loc_478E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4BBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_4929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F5")
    OP_A2(0xC)

    ChrTalk(    #162
        0xFE,
        (
            "My social studies class has been using various\x01",
            "economic indicators to predict future trends\x01",
            "and we'll be displaying the results here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "We also have a collection of materials\x01",
            "summarising the history and development of this\x01",
            "region in a simple, easy to read format.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_48F5")


    ChrTalk(    #165
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4926")

    Jump("loc_4BB9")

    label("loc_4929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A97")
    OP_A2(0xC)

    ChrTalk(    #166
        0xFE,
        (
            "My social studies class will be\x01",
            "researching various economic\x01",
            "indicators to predict future trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "Reviewing the history and growth\x01",
            "of Ruan should provide useful\x01",
            "data for this project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "If any details are missing, you just\x01",
            "have to go with what makes the most\x01",
            "sense from the data available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB9")

    label("loc_4A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_4B88")

    ChrTalk(    #170
        0xFE,
        (
            "It may push me past deadline, but I'd\x01",
            "love to get my hands on a copy of 'Ruan\x01",
            "Economics.' Very useful data in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "If you should happen to see any\x01",
            "of the volumes, would you please\x01",
            "return them to the reference room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BB9")

    label("loc_4B88")


    ChrTalk(    #172
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB9")

    Jump("loc_4E83")

    label("loc_4BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8A")
    OP_A2(0xC)

    ChrTalk(    #173
        0xFE,
        (
            "I need more research materials\x01",
            "to better substantiate my findings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "I don't think there's enough time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "I suppose I'll just have to do the\x01",
            "best I can with what I have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD4")

    label("loc_4C8A")


    ChrTalk(    #176
        0xFE,
        (
            "I need more research materials\x01",
            "to better substantiate my findings...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD4")

    Jump("loc_4E83")

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E61")
    OP_A2(0xC)

    ChrTalk(    #177
        0xFE,
        (
            "Hello, Kloe.\x01",
            "So, you've come back to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "The preparations for the class\x01",
            "program appear to be coming\x01",
            "along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "How fares the play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "I'm told the casting has not yet\x01",
            "been finalized, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#040FHa ha. That was done some\x01",
            "time ago, Logic.\x02\x03",

            "It's going to be great.\x01",
            "I hope you'll enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Ah, yes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "Then I wish you the best of luck.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E83")

    label("loc_4E61")


    ChrTalk(    #184
        0xFE,
        "I wish you the best of luck.\x02",
    )

    CloseMessageWindow()

    label("loc_4E83")

    TalkEnd(0x19)
    Return()

    # Function_22_4597 end

    def Function_23_4E87(): pass

    label("Function_23_4E87")

    TalkBegin(0x1A)

    ChrTalk(    #185
        0xFE,
        "No haunted houses this year?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "Too cliched, I guess.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_23_4E87 end

    def Function_24_4ECB(): pass

    label("Function_24_4ECB")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_4F78")

    ChrTalk(    #187
        0xFE,
        (
            "Rumor has it the queen's birthday\x01",
            "celebration is going to feature the\x01",
            "biggest competition yet this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I'd love for my Fencing Club\x01",
            "to participate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D8")

    label("loc_4F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_50AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5030")
    OP_A2(0xE)

    ChrTalk(    #189
        0xFE,
        (
            "I'm too busy with classes to do\x01",
            "much with the club, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "We've been switching off who's\x01",
            "supervising the club shop, so \x01",
            "I was thinking of checking in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AB")

    label("loc_5030")


    ChrTalk(    #191
        0xFE,
        (
            "In my case, there's a lot of\x01",
            "people to watch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "But the more enthusiastic ones\x01",
            "have some pretty sharp questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AB")

    Jump("loc_52D8")

    label("loc_50AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_51D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5163")
    OP_A2(0xE)

    ChrTalk(    #193
        0xFE,
        (
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "It's eaten up most of my time, actually.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51D5")

    label("loc_5163")


    ChrTalk(    #196
        0xFE,
        (
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D5")

    Jump("loc_52D8")

    label("loc_51D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_52D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526C")
    OP_A2(0xE)

    ChrTalk(    #198
        0xFE,
        "Oh, hi, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D8")

    label("loc_526C")


    ChrTalk(    #201
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D8")

    TalkEnd(0x1B)
    Return()

    # Function_24_4ECB end

    def Function_25_52DC(): pass

    label("Function_25_52DC")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5350")
    OP_A2(0xF)

    ChrTalk(    #203
        0xFE,
        (
            "I'll be manning the club's food\x01",
            "stand all afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "So, I need to have fun while I can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53D3")

    label("loc_5350")


    ChrTalk(    #205
        0xFE,
        (
            "Rhody's in the same club, and he\x01",
            "runs the stand in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I think I'll get an idea of how\x01",
            "annoying it can be soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D3")

    TalkEnd(0x1C)
    Return()

    # Function_25_52DC end

    def Function_26_53D7(): pass

    label("Function_26_53D7")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5440")

    ChrTalk(    #207
        0xFE,
        (
            "Ms. Wiola has been yawning\x01",
            "non-stop for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "And the pretty lady came, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F1")
    OP_A2(0x10)

    ChrTalk(    #209
        0xFE,
        (
            "Ha ha...today, we're on standby.\x01",
            "We're like...the information desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "We can explain the social studies\x01",
            "periodical in plainer terms if anyone\x01",
            "asks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_54F1")


    ChrTalk(    #211
        0xFE,
        (
            "We can explain the social studies\x01",
            "periodical in plainer terms if anyone\x01",
            "asks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5544")

    TalkEnd(0x1D)
    Return()

    # Function_26_53D7 end

    def Function_27_5548(): pass

    label("Function_27_5548")

    TalkBegin(0x1E)

    ChrTalk(    #212
        0xFE,
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "I'm tending the store in the morning,\x01",
            "so I can have fun in the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1E)
    Return()

    # Function_27_5548 end

    def Function_28_55AB(): pass

    label("Function_28_55AB")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_55F6")

    ChrTalk(    #214
        0xFE,
        "Ha ha...I know all about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "Gerome did a bang-up job.\x02",
    )

    CloseMessageWindow()

    label("loc_55F6")

    TalkEnd(0x1F)
    Return()

    # Function_28_55AB end

    def Function_29_55FA(): pass

    label("Function_29_55FA")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_56D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5696")
    OP_A2(0x13)

    ChrTalk(    #216
        0xFE,
        (
            "Huh...I'm having more fun than\x01",
            "I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "I had no idea how I'd get it all\x01",
            "done when we came up with the\x01",
            "plans for it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_5696")


    ChrTalk(    #218
        0xFE,
        "*yaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Ugh...so sleepy...\x01",
            "My kingdom for a nap!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D4")

    Jump("loc_574B")

    label("loc_56D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_574B")

    ChrTalk(    #220
        0xFE,
        (
            "Err...wh-what are my mom and kid\x01",
            "sister doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "I told them not to come...\x01",
            "I said I'd be busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574B")

    TalkEnd(0x20)
    Return()

    # Function_29_55FA end

    def Function_30_574F(): pass

    label("Function_30_574F")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_57AD")

    ChrTalk(    #222
        0xFE,
        (
            "S-Sis? Shouldn't you be...working?!\x01",
            "Is the shop gonna be okay without\x01",
            "you?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5910")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A1")
    OP_A2(0x14)

    ChrTalk(    #223
        0xFE,
        (
            "In the end, we weren't able to finish\x01",
            "setting up the displays yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Somehow, though, it was all done\x01",
            "when we came back in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "We were still in the middle of\x01",
            "working when it was time to\x01",
            "go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5910")

    label("loc_58A1")


    ChrTalk(    #226
        0xFE,
        (
            "We still weren't done when it was\x01",
            "time to go home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "We asked around, but no one\x01",
            "knew who'd done it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5910")

    TalkEnd(0x21)
    Return()

    # Function_30_574F end

    def Function_31_5914(): pass

    label("Function_31_5914")

    TalkBegin(0x22)

    ChrTalk(    #228
        0xFE,
        (
            "Reina and I don't share any classes\x01",
            "or clubs, but we still room together\x01",
            "at the dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "Phew...at this rate, it's going\x01",
            "to be difficult to breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I guess I should take advantage\x01",
            "of the freedom to enjoy it while\x01",
            "I still can.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_31_5914 end

    def Function_32_5A0A(): pass

    label("Function_32_5A0A")

    TalkBegin(0x23)

    ChrTalk(    #231
        0xFE,
        "Okay, general viewing is over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I think I'll go see Felicity in the\x01",
            "shop and torture her...uh, I mean\x01",
            "encourage her.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x23)
    Return()

    # Function_32_5A0A end

    def Function_33_5A91(): pass

    label("Function_33_5A91")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_5B03")

    ChrTalk(    #233
        0xFE,
        (
            "#610FHa ha...this is rather fun.\x02\x03",

            "The play is this afternoon, right?\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF3")

    label("loc_5B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_5EF3")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B2C")
    SetChrSubChip(0xFE, 2)
    Jump("loc_5B5D")

    label("loc_5B2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B42")
    SetChrSubChip(0xFE, 1)
    Jump("loc_5B5D")

    label("loc_5B42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B58")
    SetChrSubChip(0xFE, 0)
    Jump("loc_5B5D")

    label("loc_5B58")

    SetChrSubChip(0xFE, 2)

    label("loc_5B5D")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E63")
    OP_A2(0x453)

    ChrTalk(    #234
        0x101,
        "#004FMayor Maybelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "#613FOh! Well, if it isn't Estelle\x01",
            "and Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#004FWhat are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "#611FHa ha...to tell you the truth,\x01",
            "I actually graduated from here.\x02\x03",

            "I always make a point of going\x01",
            "to the campus festival each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#000FOh, okay. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "#610FBut enough about me. How\x01",
            "have you two been doing?\x02\x03",

            "Are you here on guild business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#001FHeh heh...well, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #241
        "\x07\x05Estelle told Mayor Maybelle what had been going on.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #242
        0xFE,
        (
            "#613FOh, so you're helping out\x01",
            "with the play?\x02\x03",

            "#611FI've always found them to be\x01",
            "slightly tiresome.\x02\x03",

            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#017F(Ugh...I'd really rather not have\x01",
            "anyone I KNOW in the audience\x01",
            "for this...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEE")

    label("loc_5E63")


    ChrTalk(    #244
        0xFE,
        (
            "#610FI've always found plays to be\x01",
            "slightly tiresome.\x02\x03",

            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EEE")

    SetChrSubChip(0xFE, 0)

    label("loc_5EF3")

    TalkEnd(0x24)
    Return()

    # Function_33_5A91 end

    def Function_34_5EF7(): pass

    label("Function_34_5EF7")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_607E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FEF")
    OP_A2(0x18)

    ChrTalk(    #245
        0xFE,
        (
            "#220FWell, well...so the play starts\x01",
            "this afternoon.\x02\x03",

            "I can't imagine it will come\x01",
            "anywhere near to the splendor\x01",
            "of Grancel's theater...\x02\x03",

            "But this is official business,\x01",
            "after all. I suppose I will go\x01",
            "see it. If I must.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_607B")

    label("loc_5FEF")


    ChrTalk(    #246
        0xFE,
        (
            "#220FWell, well...so the play starts\x01",
            "this afternoon.\x02\x03",

            "But this is official business,\x01",
            "after all. I suppose I will go\x01",
            "see it. If I must.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607B")

    Jump("loc_62CF")

    label("loc_607E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_62CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F1")
    OP_A2(0x454)

    ChrTalk(    #247
        0xFE,
        (
            "#220FSo this is the campus which is\x01",
            "funded through the royal coffers.\x02\x03",

            "As the queen's nephew, I ought\x01",
            "to give it a thorough inspection.\x02\x03",

            "#221FHa ha ha...I'm sure that the students\x01",
            "will consider it a great honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#509F(Was the old fart even invited?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x102,
        (
            "#010F(I imagine he was. NOT inviting\x01",
            "him would have just been asking\x01",
            "for trouble...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62CF")

    label("loc_61F1")


    ChrTalk(    #250
        0x25,
        (
            "#220FSo THIS is the campus which is funded through the\x01",
            "royal coffers. Hmm...I find it somewhat lacking.\x01",
            "They haven't even a single gilded bird feeder.\x02\x03",

            "As the queen's nephew, I ought\x01",
            "to give it a thorough inspection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62CF")

    TalkEnd(0x25)
    Return()

    # Function_34_5EF7 end

    def Function_35_62D3(): pass

    label("Function_35_62D3")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_635A")

    ChrTalk(    #251
        0xFE,
        (
            "#720FThe Jenis Royal Academy... It's\x01",
            "as magnificent as I'd expected.\x02\x03",

            "The campus festival is quite\x01",
            "the event, I see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E7")

    label("loc_635A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_63E7")
    OP_62(0x26, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #252
        0xFE,
        (
            "#722FY-Your Grace, I hate to say\x01",
            "this once more...\x02\x03",

            "But please consider your words\x01",
            "when among the public.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E7")

    TalkEnd(0x26)
    Return()

    # Function_35_62D3 end

    def Function_36_63EB(): pass

    label("Function_36_63EB")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D0")
    OP_A2(0x1A)

    ChrTalk(    #253
        0xFE,
        (
            "#140FAhh, okay. The play starts\x01",
            "this afternoon.\x02\x03",

            "#142FAnd it's based on the old classic,\x01",
            "'Madrigal of the White Magnolia,'\x01",
            "huh?\x02\x03",

            "Sad to say, I'm not so sure that\x01",
            "a bunch of students can pull\x01",
            "that one off...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656B")

    label("loc_64D0")


    ChrTalk(    #254
        0xFE,
        (
            "#142FSo, the show's going to be\x01",
            "'Madrigal of the White Magnolia,'\x01",
            "huh?\x02\x03",

            "Sad to say, I'm not so sure that\x01",
            "a bunch of students can pull\x01",
            "that one off...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_656B")

    TalkEnd(0x27)
    Return()

    # Function_36_63EB end

    def Function_37_656F(): pass

    label("Function_37_656F")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6838")
    OP_A2(0x456)

    ChrTalk(    #255
        0x101,
        "#000FHey, Carna.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x102,
        "#010FGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "#830FHi, guys. Jean told me what's\x01",
            "been going on.\x02\x03",

            "So, you're just helping out wherever\x01",
            "you're needed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        "#000FHeh heh...more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x102,
        (
            "#010FAre you working as security,\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "#830FBasically.\x02\x03",

            "The alumni here tend to be Liberlian\x01",
            "celebrities from all walks of life.\x02\x03",

            "Every year, they're all invited back.\x02\x03",

            "Thus, the need for heightened\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_END)), "loc_677C")

    ChrTalk(    #261
        0x102,
        (
            "#010FSpeaking of which, Mayor Maybelle\x01",
            "told us she graduated from here,\x01",
            "also.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67CD")

    label("loc_677C")


    ChrTalk(    #262
        0x101,
        (
            "#000FWow...I wonder who else went here.\x01",
            "The who's who of Liberl, I guess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CD")


    ChrTalk(    #263
        0xFE,
        (
            "#830FWell, just leave security up to\x01",
            "me and you two can focus on\x01",
            "helping out with the festival.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x456)
    Jump("loc_6897")

    label("loc_6838")


    ChrTalk(    #264
        0xFE,
        (
            "#830FJust leave security up to me\x01",
            "and you two can focus on\x01",
            "helping out with the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6897")

    TalkEnd(0x28)
    Return()

    # Function_37_656F end

    def Function_38_689B(): pass

    label("Function_38_689B")

    TalkBegin(0x29)

    ChrTalk(    #265
        0xFE,
        (
            "#130FWell, now...\x02\x03",

            "I see that you're studying hard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x29)
    Return()

    # Function_38_689B end

    def Function_39_68DB(): pass

    label("Function_39_68DB")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6918")

    ChrTalk(    #266
        0xFE,
        (
            "Let's see...maybe I should just\x01",
            "rest here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A7D")

    label("loc_6918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69ED")
    OP_A2(0x1C)

    ChrTalk(    #267
        0xFE,
        (
            "I took a day off of work to see\x01",
            "how my son has matured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "Eletta seems to be quite pleased,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "I need to be a better mother from\x01",
            "here on out. Gotta turn the doting\x01",
            "up to 9!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A7D")

    label("loc_69ED")


    ChrTalk(    #270
        0xFE,
        (
            "I took a day off of work to see\x01",
            "how my son has matured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "I need to be a better mother from\x01",
            "here on out. Gotta turn the doting\x01",
            "up to 9!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A7D")

    TalkEnd(0x2A)
    Return()

    # Function_39_68DB end

    def Function_40_6A81(): pass

    label("Function_40_6A81")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6AA8")

    ChrTalk(    #272
        0xFE,
        "I want some juice...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AD0")

    label("loc_6AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6AD0")

    ChrTalk(    #273
        0xFE,
        "Hey! I wanna plaaaaayyy...!\x02",
    )

    CloseMessageWindow()

    label("loc_6AD0")

    TalkEnd(0x2B)
    Return()

    # Function_40_6A81 end

    def Function_41_6AD4(): pass

    label("Function_41_6AD4")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6B95")

    ChrTalk(    #274
        0xFE,
        (
            "Hah... Found her! Thought she\x01",
            "could get away from her big\x01",
            "sis, did she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "She seems pretty close to that Gerome\x01",
            "fellow, I've noticed. I wonder if there's\x01",
            "anything there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C58")

    label("loc_6B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6C58")

    ChrTalk(    #276
        0xFE,
        (
            "Heh... Under normal circumstances,\x01",
            "I'd never be able to get in here.\x01",
            "It's exciting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Now, where is my little sister's\x01",
            "classroom...? Got to fulfill my\x01",
            "obligations as her guardian.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C58")

    TalkEnd(0x2C)
    Return()

    # Function_41_6AD4 end

    def Function_42_6C5C(): pass

    label("Function_42_6C5C")

    TalkBegin(0x2D)

    ChrTalk(    #278
        0xFE,
        (
            "Hmm...okay, the economic\x01",
            "development after the Hundred\x01",
            "Days War hinged upon these...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2D)
    Return()

    # Function_42_6C5C end

    def Function_43_6CBD(): pass

    label("Function_43_6CBD")

    TalkBegin(0x2E)

    ChrTalk(    #279
        0xFE,
        "*sigh* I need a break...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x2E)
    Return()

    # Function_43_6CBD end

    def Function_44_6CE2(): pass

    label("Function_44_6CE2")

    TalkBegin(0x2F)

    ChrTalk(    #280
        0xFE,
        "Ugh...I hate these writing assignments.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x2F)
    Return()

    # Function_44_6CE2 end

    def Function_45_6D16(): pass

    label("Function_45_6D16")

    TalkBegin(0x30)

    ChrTalk(    #281
        0xFE,
        "Schoolwork is all well and good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "But I'd like for my kid to be more\x01",
            "thoughtful, first and foremost.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x30)
    Return()

    # Function_45_6D16 end

    def Function_46_6D8D(): pass

    label("Function_46_6D8D")

    TalkBegin(0x32)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6E0F")

    ChrTalk(    #283
        0xFE,
        (
            "My mom's really eager for me\x01",
            "to get in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "So I've got to really bust my butt\x01",
            "to pass the entrance exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E4A")

    label("loc_6E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6E4A")

    ChrTalk(    #285
        0xFE,
        (
            "I wonder what typical classes\x01",
            "here are like...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E4A")

    TalkEnd(0x32)
    Return()

    # Function_46_6D8D end

    def Function_47_6E4E(): pass

    label("Function_47_6E4E")

    TalkBegin(0x31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_6EBB")

    ChrTalk(    #286
        0xFE,
        "*sigh* The festival is just PERFECT.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "Now I want my son to enroll\x01",
            "here more than ever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F4F")

    label("loc_6EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_6F4F")

    ChrTalk(    #288
        0xFE,
        (
            "I came here with my son to check\x01",
            "out the royal academy campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "We've got to get him focused on\x01",
            "passing next year's entrance\x01",
            "exams!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4F")

    TalkEnd(0x31)
    Return()

    # Function_47_6E4E end

    def Function_48_6F53(): pass

    label("Function_48_6F53")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_70F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_706C")
    OP_A2(0x457)
    OP_4A(0x8, 255)

    ChrTalk(    #290
        0x8,
        (
            "#781FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",

            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x34,
        (
            "#661FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",

            "I expect that today will be\x01",
            "quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x34, 0x10)
    OP_4B(0x8, 255)
    Jump("loc_70F2")

    label("loc_706C")


    ChrTalk(    #292
        0x34,
        (
            "#661FAh, so you kids are here, too.\x02\x03",

            "I come to the campus festival\x01",
            "every year at the invitation of\x01",
            "the dean and Student Council.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70F2")

    TalkEnd(0x34)
    Return()

    # Function_48_6F53 end

    def Function_49_70F6(): pass

    label("Function_49_70F6")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7161")

    ChrTalk(    #293
        0xFE,
        (
            "#620FI saw Joshua running off earlier.\x01",
            "He looked quite serious.\x02\x03",

            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_755F")

    label("loc_7161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_755F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751B")
    OP_A2(0x453)

    ChrTalk(    #294
        0x101,
        "#004FAh, Lila?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#621FIt's good to see you both again.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x10)
    TurnDirection(0x24, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71D5")
    SetChrSubChip(0x24, 2)
    Jump("loc_7206")

    label("loc_71D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71EB")
    SetChrSubChip(0x24, 1)
    Jump("loc_7206")

    label("loc_71EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x24, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7201")
    SetChrSubChip(0x24, 0)
    Jump("loc_7206")

    label("loc_7201")

    SetChrSubChip(0x24, 2)

    label("loc_7206")

    OP_8C(0x24, 270, 0)
    SetChrFlags(0x24, 0x10)

    ChrTalk(    #296
        0x24,
        "#613FOh! Well, if it isn't Estelle and Joshua!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x24, 0)
    TurnDirection(0x102, 0x24, 0)
    TurnDirection(0x105, 0x24, 0)

    ChrTalk(    #297
        0x101,
        (
            "#004FMayor Maybelle, too?!\x02\x03",

            "What are you two doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x24,
        (
            "#611FHa ha...to tell you the truth,\x01",
            "I actually graduated from here.\x02\x03",

            "I always make a point of going\x01",
            "to the campus festival each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#000FOh, okay. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x24,
        (
            "#610FBut enough about me. How\x01",
            "have you two been doing?\x02\x03",

            "Are you here on guild business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#001FHeh heh...well, actually...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #302
        "\x07\x05Estelle told Mayor Maybelle what had been going on.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #303
        0x24,
        (
            "#613FOh, so you're helping out\x01",
            "with the play?\x02\x03",

            "#611FI've always found them to be\x01",
            "slightly tiresome.\x02\x03",

            "Ha ha...but if you're going to be\x01",
            "on stage, I certainly don't want\x01",
            "to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x102,
        (
            "#017F(Ugh...I'd really rather not have\x01",
            "anyone I KNOW in the audience\x01",
            "for this...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0)
    Jump("loc_755F")

    label("loc_751B")


    ChrTalk(    #305
        0xFE,
        (
            "#621FLong time no see, you two.\x01",
            "You look as energetic as ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_755F")

    TalkEnd(0x33)
    Return()

    # Function_49_70F6 end

    def Function_50_7563(): pass

    label("Function_50_7563")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_75DC")

    ChrTalk(    #306
        0xFE,
        (
            "Time was, all of the students'\x01",
            "displays were research papers\x01",
            "of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "Times change, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_766A")

    label("loc_75DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_766A")

    ChrTalk(    #308
        0xFE,
        (
            "When we were students, \x01",
            "this building wasn't even\x01",
            "around yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "The building to the north used\x01",
            "to be the main school building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766A")

    TalkEnd(0x35)
    Return()

    # Function_50_7563 end

    def Function_51_766E(): pass

    label("Function_51_766E")

    TalkBegin(0x36)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_76E4")

    ChrTalk(    #310
        0xFE,
        (
            "The highest final exam grade\x01",
            "was from...one Kloe Rinz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "Wow, she and Jill must be\x01",
            "really smart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7732")

    label("loc_76E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7732")

    ChrTalk(    #312
        0xFE,
        (
            "Sunday School is nice and all, but\x01",
            "this? This is REAL learning...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7732")

    TalkEnd(0x36)
    Return()

    # Function_51_766E end

    def Function_52_7736(): pass

    label("Function_52_7736")

    TalkBegin(0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_77E2")

    ChrTalk(    #313
        0xFE,
        (
            "They must have something\x01",
            "interesting up their sleeves\x01",
            "for this afternoon's play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "I asked my daughter about it,\x01",
            "but she wouldn't tell me any\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_784D")

    label("loc_77E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_784D")

    ChrTalk(    #315
        0xFE,
        "So, this is the academy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "My daughter attends here, but\x01",
            "this is my first time on campus.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_784D")

    TalkEnd(0x37)
    Return()

    # Function_52_7736 end

    def Function_53_7851(): pass

    label("Function_53_7851")

    TalkBegin(0x38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_78AF")

    ChrTalk(    #317
        0xFE,
        (
            "All this walking has tired me\x01",
            "out. Maybe I should rest in\x01",
            "the coffee house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_78AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_78FD")

    ChrTalk(    #318
        0xFE,
        (
            "The natural science and\x01",
            "social studies classes\x01",
            "are up here. Neat!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78FD")

    TalkEnd(0x38)
    Return()

    # Function_53_7851 end

    def Function_54_7901(): pass

    label("Function_54_7901")

    TalkBegin(0x39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_795B")

    ChrTalk(    #319
        0xFE,
        (
            "All the displays were fun.\x01",
            "The children seem to be\x01",
            "having a great time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7988")

    label("loc_795B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7988")

    ChrTalk(    #320
        0xFE,
        "I'm not sure where to go next...\x02",
    )

    CloseMessageWindow()

    label("loc_7988")

    TalkEnd(0x39)
    Return()

    # Function_54_7901 end

    def Function_55_798C(): pass

    label("Function_55_798C")

    TalkBegin(0x3A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_79FD")

    ChrTalk(    #321
        0xFE,
        "There are displays everywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "You can see that the students\x01",
            "put a lot of work into them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A34")

    label("loc_79FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7A34")

    ChrTalk(    #323
        0xFE,
        (
            "I wasn't expecting so many\x01",
            "buildings here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A34")

    TalkEnd(0x3A)
    Return()

    # Function_55_798C end

    def Function_56_7A38(): pass

    label("Function_56_7A38")

    TalkBegin(0x3B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7AA1")

    ChrTalk(    #324
        0xFE,
        "I'm really amazed at this class...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "These students have really\x01",
            "accomplished a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE8")

    label("loc_7AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7AE8")

    ChrTalk(    #326
        0xFE,
        (
            "Well, well...this is the natural\x01",
            "sciences exhibition, eh? \x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE8")

    TalkEnd(0x3B)
    Return()

    # Function_56_7A38 end

    def Function_57_7AEC(): pass

    label("Function_57_7AEC")

    TalkBegin(0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7B40")

    ChrTalk(    #327
        0xFE,
        (
            "I think the exhibitions will be\x01",
            "shut down soon. I'd better hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B85")

    label("loc_7B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7B85")

    ChrTalk(    #328
        0xFE,
        (
            "Is it just me, or are there more\x01",
            "people here than usual?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B85")

    TalkEnd(0x3C)
    Return()

    # Function_57_7AEC end

    def Function_58_7B89(): pass

    label("Function_58_7B89")

    TalkBegin(0x3D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_7BE5")

    ChrTalk(    #329
        0xFE,
        (
            "I'm going to see the play\x01",
            "this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "I hope it'll start soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C2B")

    label("loc_7BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7C2B")

    ChrTalk(    #331
        0xFE,
        (
            "You attend classes here? Do\x01",
            "you ever get to have any fun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C2B")

    TalkEnd(0x3D)
    Return()

    # Function_58_7B89 end

    def Function_59_7C2F(): pass

    label("Function_59_7C2F")

    EventBegin(0x0)
    OP_6D(-5190, 0, 34000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x31, 3150, 0, 31480, 90)
    SetChrPos(0x19, -5600, 0, 29020, 90)
    SetChrPos(0x25, 88600, 0, 34670, 0)
    SetChrPos(0x26, 89570, 0, 34410, 270)
    ClearChrFlags(0x29, 0x80)
    OP_4A(0x29, 255)
    SetChrPos(0x101, 2630, 0, 29470, 0)
    SetChrPos(0x102, 2510, 0, 28440, 0)
    SetChrPos(0x105, 1400, 0, 28920, 0)
    SetChrPos(0x29, 1690, 0, 30250, 0)
    FadeToBright(2000, 0)
    OP_6D(2050, 0, 29480, 4000)

    ChrTalk(    #332
        0x29,
        (
            "#132FWell, well...you've certainly pulled out all\x01",
            "the stops, haven't you?\x02\x03",

            "So many areas of interest, from history to\x01",
            "economics...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 180, 400)

    ChrTalk(    #333
        0x29,
        (
            "#130FThank you so much. This looks like smashing\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x105,
        (
            "#048FIt was my pleasure to help, sir.\x02\x03",

            "Social studies is my major, so I hope you enjoy\x01",
            "looking around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#506FI've never been any good at this whole\x01",
            "academics thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x102,
        (
            "#017F*sigh* One of these days, you're really going to\x01",
            "have to get over that.\x02\x03",

            "#010FBeing a bracer requires knowledge in many\x01",
            "different areas of study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#509F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x29,
        (
            "#130FHa ha. Well, I'm itching to start looking\x01",
            "around, so if you'll excuse me.\x02\x03",

            "Thank you again for showing me the way here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x29, 315, 400)

    def lambda_7FCF():
        OP_6D(1000, 0, 31440, 2000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7FCF)
    OP_8E(0x29, 0xFFFFF970, 0x0, 0x8778, 0x7D0, 0x0)
    OP_8C(0x29, 0, 400)
    OP_4B(0x29, 255)
    OP_A2(0x45A)
    EventEnd(0x0)
    Return()

    # Function_59_7C2F end

    def Function_60_8006(): pass

    label("Function_60_8006")

    EventBegin(0x0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    SetChrPos(0x9, 41350, -250, -3330, 0)
    SetChrPos(0xA, 40790, -250, -4570, 0)
    SetChrPos(0xB, 39420, 0, -2040, 0)
    SetChrPos(0xC, 41420, -250, -2220, 0)
    SetChrPos(0xD, 40840, 0, -1870, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 46630, 2000, 7580, 180)
    SetChrPos(0x102, 46550, 2000, 8570, 180)
    SetChrPos(0x105, 45690, 2000, 8960, 180)
    OP_0D()

    ChrTalk(    #339
        0xD,
        "#1PMiss Kloe!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8144():
        OP_6D(44200, 0, 1160, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8144)
    WaitChrThread(0x101, 0x1)

    def lambda_8161():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8161)

    def lambda_817C():
        OP_8E(0xFE, 0xA7C6, 0x0, 0x5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_817C)
    Sleep(200)

    def lambda_819C():
        OP_8E(0xFE, 0xABC2, 0x0, 0xFFFFFD6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_819C)

    def lambda_81B7():
        OP_8E(0xFE, 0xA4CE, 0x0, 0x10E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_81B7)
    Sleep(200)

    def lambda_81D7():
        OP_8E(0xFE, 0xA848, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_81D7)
    Sleep(100)

    def lambda_81F7():
        OP_8E(0xFE, 0xB798, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81F7)
    Sleep(500)

    def lambda_8217():
        OP_8E(0xFE, 0xB27A, 0x0, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8217)
    WaitChrThread(0x101, 0x1)

    def lambda_8237():
        OP_8E(0xFE, 0xA870, 0x0, 0x618, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8237)
    WaitChrThread(0x102, 0x1)

    def lambda_8257():
        OP_8E(0xFE, 0xAF28, 0x0, 0x1A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8257)
    WaitChrThread(0x105, 0x1)

    def lambda_8277():
        OP_8E(0xFE, 0xAD02, 0x0, 0x55A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8277)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 225, 400)

    ChrTalk(    #340
        0x105,
        "#041FOh... You're all here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#001F#3PHeya, kiddos! Glad you could\x01",
            "make it! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#019F#4PAre you having fun?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x9,
        "Yeah! It's awesome! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xB,
        "I ate so much candy I puked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xC,
        (
            "I told you not to be such\x01",
            "a pig...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x105,
        (
            "#048FHa ha... Is Matron Theresa\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #347
        0xD,
        (
            "#770FYep, she's talkin' to those\x01",
            "people over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #348
        0xD,
        "#771FHere she is!\x02",
    )

    CloseMessageWindow()

    def lambda_8431():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8431)

    def lambda_843F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_843F)

    def lambda_844D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_844D)

    def lambda_845B():

        label("loc_845B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_845B")

    QueueWorkItem2(0x101, 2, lambda_845B)

    def lambda_846C():

        label("loc_846C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_846C")

    QueueWorkItem2(0x102, 2, lambda_846C)

    def lambda_847D():

        label("loc_847D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_847D")

    QueueWorkItem2(0x105, 2, lambda_847D)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xA410, 0x0, 0xFFFFFBB4, 0x7D0, 0x0)
    TurnDirection(0xA, 0x105, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(    #349
        0xA,
        "#750FGood afternoon, all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        "#004F#3PMatron Theresa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x105,
        "#048FGood afternoon, Matron.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        (
            "#751FThank you very much for\x01",
            "inviting us here today.\x02\x03",

            "The children and I have\x01",
            "enjoyed it greatly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(    #353
        0xD,
        (
            "#770FHey, Miss Kloe?\x02\x03",

            "When's your play thingy\x01",
            "supposed to start?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85CE():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_85CE)

    def lambda_85DC():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_85DC)

    def lambda_85EA():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_85EA)
    TurnDirection(0xC, 0x105, 400)

    ChrTalk(    #354
        0xC,
        (
            "We've all been looking forward\x01",
            "to it. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x105,
        (
            "#040FI see... Well, you'll have to\x01",
            "wait just a little bit longer.\x02\x03",

            "#041FDid you know that both Estelle and Joshua are\x01",
            "going to be in the play with me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #356
        0xB,
        "Really? That's gonna be so cool!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #357
        0x9,
        (
            "What part are you going to be playing, Mister\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x102,
        "#018F#4PUmm... Well, how to put this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        (
            "#001F#3PHa ha ha! You'll just have to wait and see,\x01",
            "won't you? ㈱\x02\x03",

            "#000FOh, by the way...are you guys\x01",
            "still staying in Manoria?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xA,
        (
            "#750FYes, through the continued good will\x01",
            "of the innkeepers.\x02\x03",

            "#757FThat said, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#501F#3P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x102,
        (
            "#015F#4P...\x02\x03",

            "#010FHey, guys. Do you want to see\x01",
            "the costumes that'll be used\x01",
            "in the play?\x02\x03",

            "There are pretty dresses and\x01",
            "suits of armor...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88E8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_88E8)

    def lambda_88F6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88F6)

    def lambda_8904():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8904)

    def lambda_8912():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8912)
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #363
        0xC,
        "Pretty dresses?!\x02",
    )

    CloseMessageWindow()

    def lambda_893D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_893D)
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #364
        0xD,
        "#774F#1PSuits of armor?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x102,
        (
            "#019FHa ha... I guess I have your\x01",
            "attention.\x02\x03",

            "I'll give you an exclusive\x01",
            "sneak peek at them, before\x01",
            "the play even starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xB,
        "Yaaaaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x9,
        "I wanna go, too!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #368
        0x102,
        (
            "#010F(I'll be backstage. Come\x01",
            "when you're ready.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A52():

        label("loc_8A52")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A52")

    QueueWorkItem2(0x105, 1, lambda_8A52)

    def lambda_8A63():

        label("loc_8A63")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A63")

    QueueWorkItem2(0x101, 1, lambda_8A63)

    def lambda_8A74():

        label("loc_8A74")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A74")

    QueueWorkItem2(0xA, 1, lambda_8A74)

    def lambda_8A85():

        label("loc_8A85")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A85")

    QueueWorkItem2(0xD, 1, lambda_8A85)

    def lambda_8A96():

        label("loc_8A96")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8A96")

    QueueWorkItem2(0xC, 1, lambda_8A96)

    def lambda_8AA7():

        label("loc_8AA7")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8AA7")

    QueueWorkItem2(0x9, 1, lambda_8AA7)

    def lambda_8AB8():

        label("loc_8AB8")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_8AB8")

    QueueWorkItem2(0xB, 1, lambda_8AB8)
    SetChrFlags(0x102, 0x4)
    OP_8C(0x102, 180, 400)
    OP_8E(0x102, 0xB004, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
    OP_8E(0x102, 0xA8B6, 0x0, 0xFFFFF902, 0x7D0, 0x0)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #369
        0x102,
        "#010FOkay. Now follow me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)
    OP_8E(0x102, 0xA438, 0xFFFFFF06, 0xFFFFF5EC, 0x7D0, 0x0)
    ClearChrFlags(0x102, 0x4)

    def lambda_8B43():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B43)

    def lambda_8B5E():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8B5E)
    Sleep(700)

    def lambda_8B7E():
        OP_8E(0xFE, 0xA622, 0xFFFFFF06, 0xFFFFF6FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B7E)
    WaitChrThread(0x102, 0x1)
    SetChrFlags(0x102, 0x80)

    def lambda_8BA3():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8BA3)

    def lambda_8BBE():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8BBE)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)

    def lambda_8BE3():
        OP_8E(0xFE, 0xA136, 0x0, 0xFFFFFCCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8BE3)
    WaitChrThread(0xB, 0x1)

    def lambda_8C03():
        OP_8E(0xFE, 0xA438, 0xFFFFFF06, 0xFFFFEC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8C03)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xA, 0xFF)

    def lambda_8C4D():
        OP_6D(42780, 0, 270, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8C4D)

    def lambda_8C65():
        OP_8E(0xFE, 0xA8FC, 0x0, 0xFFFFFFBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C65)
    Sleep(400)

    def lambda_8C85():
        OP_8E(0xFE, 0xA474, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C85)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xA, 400)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #370
        0xA,
        (
            "#750F#5P*chuckle* Joshua is such a\x01",
            "thoughtful boy.\x02\x03",

            "#757FI didn't want to speak of this\x01",
            "in front of the children.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D28():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8D28)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #371
        0x101,
        "#002F#3PYou mean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #372
        0xA,
        (
            "#754FYes. I've chosen to accept the\x01",
            "mayor's offer.\x02\x03",

            "We will impose upon the\x01",
            "Manorians no longer.\x02\x03",

            "#750FI will tell the children today,\x01",
            "after the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x105,
        (
            "#049F#4PI... I see...\x02\x03",

            "That's sad...but I suppose\x01",
            "you have no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xA,
        (
            "#751F*chuckle* Please, don't look\x01",
            "at me so...\x02\x03",

            "Grancel is easily reachable\x01",
            "by airship.\x02\x03",

            "#750FMoreover, I can look for work\x01",
            "while I am there.\x02\x03",

            "If I save enough mira, I'll be\x01",
            "able to rebuild the orphanage,\x01",
            "some day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x101,
        "#003F#3PMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x105,
        "#049F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xA,
        (
            "#751FNow, then... Let us find the\x01",
            "children, shall we?\x02\x03",

            "I would imagine that they're a\x01",
            "bit much for Joshua to handle\x01",
            "on his own.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2523   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_60_8006 end

    def Function_61_8FE2(): pass

    label("Function_61_8FE2")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x3E, 0x80)
    OP_64(0x1, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #378
        "\x07\x00Found \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33E, 1)
    OP_28(0x27, 0x1, 0x80)
    TalkEnd(0xFF)
    Return()

    # Function_61_8FE2 end

    def Function_62_904A(): pass

    label("Function_62_904A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #379
        (
            "\x07\x05Ahead: Dean's Room, Faculty Lounge\x01\x01",
            "* Academy personnel ONLY, please\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_62_904A end

    def Function_63_90C1(): pass

    label("Function_63_90C1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #380
        (
            "\x07\x05Humanities Refreshment Booth\x01",
            "     Fontana Tea House\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_63_90C1 end

    def Function_64_9127(): pass

    label("Function_64_9127")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #381
        (
            "\x07\x05KEEP OUR HALLWAYS QUIET\x01\x01",
            "      --Student Council\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_64_9127 end

    def Function_65_918A(): pass

    label("Function_65_918A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #382
        (
            "\x07\x05Natural Sciences Demonstration\x01",
            "'Quartz Circuits & Orbal Arts'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_65_918A end

    def Function_66_91FA(): pass

    label("Function_66_91FA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #383
        (
            "\x07\x05Social Studies Demonstration\x01",
            "'Ruanian History & Economy'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_66_91FA end

    def Function_67_9265(): pass

    label("Function_67_9265")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #384
        "\x07\x05Welcome to the Fontana Tea House!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_67_9265 end

    def Function_68_92B9(): pass

    label("Function_68_92B9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #385
        (
            "\x07\x05It summarizes the trends in\x01",
            "orbal arts usage.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_68_92B9 end

    def Function_69_9319(): pass

    label("Function_69_9319")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #386
        (
            "\x07\x05It has a graph, depicting changes in the\x01",
            "tourist industry's annual growth rate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_69_9319 end

    def Function_70_939B(): pass

    label("Function_70_939B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #387
        "\x07\x05It lists the most important exports.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_70_939B end

    def Function_71_93F2(): pass

    label("Function_71_93F2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #388
        (
            "\x07\x05It concerns population growth and\x01",
            "migration.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_71_93F2 end

    def Function_72_9451(): pass

    label("Function_72_9451")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #389
        (
            "\x07\x05              Orbal Functional Unit Memory\x01\x01",
            "* Displayed items are on loan from the\x01",
            "Zeiss central lab.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_72_9451 end

    def Function_73_94E9(): pass

    label("Function_73_94E9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #390
        (
            "\x07\x05               Orbal Compatibility Tester\x01\x01",
            "* Now working! No more electric shocks! We promise!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_73_94E9 end

    def Function_74_957A(): pass

    label("Function_74_957A")

    EventBegin(0x0)
    Fade(1000)

    def lambda_9587():
        OP_6D(84960, 1650, 32920, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_9587)

    def lambda_959F():
        OP_67(0, 1300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_959F)

    def lambda_95B7():
        OP_6B(1400, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_95B7)

    def lambda_95C7():
        OP_6C(0, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_95C7)

    def lambda_95D7():
        OP_6E(262, 1000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_95D7)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_95FF")
    Jump("loc_964C")

    label("loc_95FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_9609")
    Jump("loc_964C")

    label("loc_9609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_9631")
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x2C, 0x80)
    Jump("loc_964C")

    label("loc_9631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_964C")
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)

    label("loc_964C")

    Sleep(1000)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Fade(500)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #391
        (
            "\x07\x02Orbal Compatibility Tester\x01",
            "Version:1.0014.4082\x01",
            "(C) 1202 Jenis Royal Academy\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    SetChrName("Tester")

    AnonymousTalk(    #392
        "\x07\x05Begin test?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB46")
    SetMessageWindowPos(72, 290, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_974B"),
        (1, "loc_974E"),
        (SWITCH_DEFAULT, "loc_975B"),
    )


    label("loc_974B")

    Jump("loc_9768")

    label("loc_974E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96F7")

    label("loc_975B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96F7")

    label("loc_9768")


    AnonymousTalk(    #393
        "\x07\x05Whose profile will you input?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        5,
        0,
        (
            "[Estelle]\x01",         # 0
            "[Joshua]\x01",          # 1
            "[Scherazard]\x01",      # 2
            "[Olivier]\x01",         # 3
            "[Kloe]\x01",            # 4
            "[Nial]\x01",            # 5
            "[Dorothy]\x01",         # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_9811"),
        (1, "loc_9858"),
        (2, "loc_989F"),
        (3, "loc_98EA"),
        (4, "loc_9931"),
        (5, "loc_9975"),
        (6, "loc_99B9"),
        (SWITCH_DEFAULT, "loc_99FF"),
    )


    label("loc_9811")


    AnonymousTalk(    #394
        (
            "\x07\x05[Estelle Bright] \x01",
            "Born 8-7-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_9858")


    AnonymousTalk(    #395
        (
            "\x07\x05[Joshua Bright]\x01",
            "Born 12-20-1185, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_989F")


    AnonymousTalk(    #396
        (
            "\x07\x05[Scherazard Harvey] \x01",
            "Born 5-14-1179, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_98EA")


    AnonymousTalk(    #397
        (
            "\x07\x05[Olivier Lenheim]\x01",
            "Born 4-1-1177, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_9931")


    AnonymousTalk(    #398
        (
            "\x07\x05[Kloe Rinz] \x01",
            "Born 10-11-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_9975")


    AnonymousTalk(    #399
        (
            "\x07\x05[Nial Burns]\x01",
            "Born 11-25-1172, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_99B9")


    AnonymousTalk(    #400
        (
            "\x07\x05[Dorothy Hyatt]\x01",
            "Born 1-22-1182, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_99FF")


    AnonymousTalk(    #401
        "\x07\x05Please input next profile.\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        426,
        5,
        0,
        (
            "[Estelle]\x01",         # 0
            "[Joshua]\x01",          # 1
            "[Scherazard]\x01",      # 2
            "[Olivier]\x01",         # 3
            "[Kloe]\x01",            # 4
            "[Nial]\x01",            # 5
            "[Dorothy]\x01",         # 6
        )
    )

    MenuEnd(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_9AA5"),
        (1, "loc_9AEC"),
        (2, "loc_9B33"),
        (3, "loc_9B7E"),
        (4, "loc_9BC5"),
        (5, "loc_9C09"),
        (6, "loc_9C4D"),
        (SWITCH_DEFAULT, "loc_9C93"),
    )


    label("loc_9AA5")


    AnonymousTalk(    #402
        (
            "\x07\x05[Estelle Bright] \x01",
            "Born 8-7-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9AEC")


    AnonymousTalk(    #403
        (
            "\x07\x05[Joshua Bright]\x01",
            "Born 12-20-1185, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9B33")


    AnonymousTalk(    #404
        (
            "\x07\x05[Scherazard Harvey] \x01",
            "Born 5-14-1179, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9B7E")


    AnonymousTalk(    #405
        (
            "\x07\x05[Olivier Lenheim]\x01",
            "Born 4-1-1177, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9BC5")


    AnonymousTalk(    #406
        (
            "\x07\x05[Kloe Rinz] \x01",
            "Born 10-11-1186, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9C09")


    AnonymousTalk(    #407
        (
            "\x07\x05[Nial Burns]\x01",
            "Born 11-25-1172, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9C4D")


    AnonymousTalk(    #408
        (
            "\x07\x05[Dorothy Hyatt]\x01",
            "Born 1-22-1182, Septian Calendar...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9C93")

    label("loc_9C93")

    SetChrName("Tester")

    AnonymousTalk(    #409
        "\x07\x05Beginning analysis.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x27, 0x0, 0x64)
    OP_75(0x6, 0x0, 0x0)
    Sleep(50)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(60)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(70)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(80)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(90)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(100)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(110)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(120)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(130)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(140)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(150)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(160)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(170)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(180)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(190)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(200)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(210)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(220)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(230)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(240)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(260)
    SetChrName("Tester")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (4, "loc_9F2B"),
        (40, "loc_9F2B"),
        (12, "loc_9F2B"),
        (21, "loc_9F2B"),
        (24, "loc_9F2B"),
        (42, "loc_9F2B"),
        (36, "loc_9F2B"),
        (63, "loc_9F2B"),
        (5, "loc_A0E3"),
        (50, "loc_A0E3"),
        (14, "loc_A0E3"),
        (41, "loc_A0E3"),
        (26, "loc_A0E3"),
        (62, "loc_A0E3"),
        (2, "loc_A2A0"),
        (20, "loc_A2A0"),
        (6, "loc_A2A0"),
        (60, "loc_A2A0"),
        (15, "loc_A2A0"),
        (51, "loc_A2A0"),
        (1, "loc_A496"),
        (10, "loc_A496"),
        (13, "loc_A496"),
        (31, "loc_A496"),
        (25, "loc_A496"),
        (52, "loc_A496"),
        (46, "loc_A496"),
        (64, "loc_A496"),
        (16, "loc_A653"),
        (61, "loc_A653"),
        (23, "loc_A653"),
        (32, "loc_A653"),
        (34, "loc_A653"),
        (43, "loc_A653"),
        (56, "loc_A653"),
        (65, "loc_A653"),
        (3, "loc_A82E"),
        (30, "loc_A82E"),
        (35, "loc_A82E"),
        (53, "loc_A82E"),
        (45, "loc_A82E"),
        (54, "loc_A82E"),
        (0, "loc_A9E2"),
        (11, "loc_A9E2"),
        (22, "loc_A9E2"),
        (33, "loc_A9E2"),
        (44, "loc_A9E2"),
        (55, "loc_A9E2"),
        (66, "loc_A9E2"),
        (SWITCH_DEFAULT, "loc_AB0B"),
    )


    label("loc_9F2B")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(1000)

    AnonymousTalk(    #410
        (
            "\x07\x05Today will be an especially active day\x01",
            "for both individuals.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #411
        (
            "\x07\x05Your actions will cause your life\x01",
            "to be firmly enmeshed in another's. \x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #412
        (
            "\x07\x05Because of lively conversation, when the two of you\x01",
            "can be alone, the fire in your hearts may be kindled.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #413
        "\x07\x05Before you can be overwhelmed, take action.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #414
        (
            "\x07\x05Your common goals and interests will carry your\x01",
            "relationship further than it has ever been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A0E3")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(1000)

    AnonymousTalk(    #415
        (
            "\x07\x05These two are greatly attuned to one another, and their\x01",
            "time spent together today should be very enjoyable.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #416
        (
            "\x07\x05They should be able to overcome any obstacle together,\x01",
            "regardless of the circumstances or consequences.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #417
        (
            "\x07\x05Their shared awareness will enable them to overcome\x01",
            "unknown foes, and their bond will grow ever stronger.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #418
        (
            "\x07\x05These two have strong ties of love\x01",
            "and comradeship to each other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A2A0")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x5)
    Sleep(1000)

    AnonymousTalk(    #419
        (
            "\x07\x05Today is a day for them to look to the\x01",
            "future with open and optimistic eyes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #420
        (
            "\x07\x05Today, in spite of their differences, they should\x01",
            "be able to pass the time together quietly without\x01",
            "argument or serious bodily injury.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #421
        (
            "\x07\x05Normally, these two would feel compelled\x01",
            "to push their opinions onto each other...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #422
        "\x07\x05But today feels like a day of peace and tranquility.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #423
        (
            "\x07\x05There is a real chance to move on from the\x01",
            "usual conversation, and speak of new things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A496")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x2)
    Sleep(1000)

    AnonymousTalk(    #424
        "\x07\x05These are two very active individuals.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #425
        (
            "\x07\x05Today is the ideal day to take on\x01",
            "new challenges or foes together.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #426
        (
            "\x07\x05All it will take is for each to suppress the\x01",
            "impulse to force an opinion onto the other.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #427
        (
            "\x07\x05If these two learn to respect each other's point of view,\x01",
            "they will both grow more mature from the experience.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #428
        (
            "\x07\x05Most importantly, they must each learn\x01",
            "to consider the other's feelings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A653")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x7)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x4)
    Sleep(1000)

    AnonymousTalk(    #429
        (
            "\x07\x05Though these two are in each other's company today, there\x01",
            "seems to be a distinct awkwardness between them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #430
        (
            "\x07\x05A secret will be revealed, and if one lies, it\x01",
            "will sow the seeds of distrust in the other.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #431
        (
            "\x07\x05If they cannot find their common ground,\x01",
            "conversation between them will do no good.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #432
        (
            "\x07\x05Today is the day, either for compromise\x01",
            "or for giving up altogether.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #433
        "\x07\x05Only time and distance will likely heal the damage done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A82E")

    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x6)
    Sleep(250)
    OP_22(0x27, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x3)
    Sleep(1000)

    AnonymousTalk(    #434
        (
            "\x07\x05These two are in grave need of expressing their feelings\x01",
            "to one another, or they risk a serious argument.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #435
        (
            "\x07\x05A prolonged argument will lead to a\x01",
            "painful and reluctant separation.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #436
        (
            "\x07\x05Today is a day that is, perhaps, better spent among\x01",
            "a crowd than in each other's exclusive company.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #437
        (
            "\x07\x05Regardless of what is said, it must be heard with an\x01",
            "open mind, no matter how unwelcome it may be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0B")

    label("loc_A9E2")

    OP_74(0x6, 0x0, 0x0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xF7, 0x0, 0x64)
    OP_20(0x0)
    FadeToDark(500, 0, -1)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_56(0x0)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #438
        "\x07\x024 Error(s)...  0 Warning(s)...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #439
        (
            "\x07\x02Orbal Compatibility Tester\x01",
            "Version:1.0014.4082\x01",
            "(C) 1202 Jenis Royal Academy\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W........#20WOK!\x01",
            "#200W　#20W\x01",
            "restart\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_1E()
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x6, 0x0, 0x1)
    OP_0D()
    Jump("loc_AB0B")

    label("loc_AB0B")

    SetMessageWindowPos(72, 290, 56, 3)
    OP_5F(0x1)
    OP_5F(0x0)
    OP_74(0x6, 0x0, 0x1)
    SetChrName("Tester")

    AnonymousTalk(    #440
        "\x07\x05Continue analysis?\x02",
    )

    CloseMessageWindow()
    Jump("loc_96F7")

    label("loc_AB46")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(1000)
    OP_74(0x6, 0x0, 0x0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_AB89")
    Jump("loc_ABD6")

    label("loc_AB89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AB93")
    Jump("loc_ABD6")

    label("loc_AB93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_ABBB")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x2C, 0x80)
    Jump("loc_ABD6")

    label("loc_ABBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_ABD6")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)

    label("loc_ABD6")

    EventEnd(0x1)
    Return()

    # Function_74_957A end

    def Function_75_ABD9(): pass

    label("Function_75_ABD9")

    SetPlaceName(0x6F)
    Return()

    # Function_75_ABD9 end

    def Function_76_ABDD(): pass

    label("Function_76_ABDD")

    SetPlaceName(0x5E)
    Return()

    # Function_76_ABDD end

    def Function_77_ABE1(): pass

    label("Function_77_ABE1")

    SetPlaceName(0x6E)
    Return()

    # Function_77_ABE1 end

    def Function_78_ABE5(): pass

    label("Function_78_ABE5")

    SetPlaceName(0x74)
    Return()

    # Function_78_ABE5 end

    def Function_79_ABE9(): pass

    label("Function_79_ABE9")

    SetPlaceName(0x73)
    Return()

    # Function_79_ABE9 end

    SaveToFile()

Try(main)
