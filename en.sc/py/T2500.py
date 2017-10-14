from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2500   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2500.x',
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
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Sieg',                                 # 11
        'Mickey',                               # 12
        'Felicity',                             # 13
        'Reina',                                # 14
        'Kaden',                                # 15
        'Purity',                               # 16
        'Mr. Effort',                           # 17
        'Janitor Parkes',                       # 18
        'Olivier',                              # 19
        "Bleublanc's Ghost",                    # 20
        'Enhanced Jaeger',                      # 21
        'Enhanced Jaeger',                      # 22
        'Enhanced Jaeger',                      # 23
        'Enhanced Jaeger',                      # 24
        'Steel Cougar',                         # 25
        'Steel Cougar',                         # 26
        'Vogel 235',                            # 27
        'Vogel 235',                            # 28
        'Royal Army Soldier',                   # 29
        'Royal Army Soldier',                   # 30
        'Carna',                                # 31
        'Grant',                                # 32
        'Rhody',                                # 33
        'Patrick',                              # 34
        'Academy - Back Road',                  # 35
        'Vista Forest Road',                    # 36
        '',                                     # 37
        '',                                     # 38
        '',                                     # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
        '',                                     # 43
        '',                                     # 44
        '',                                     # 45
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
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT26/CH20238 ._CH',             # 03
        'ED6_DT07/CH02323 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH01090 ._CH',             # 06
        'ED6_DT07/CH01370 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01093 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT06/CH20045 ._CH',             # 0C
        'ED6_DT26/CH20270 ._CH',             # 0D
        'ED6_DT26/CH20422 ._CH',             # 0E
        'ED6_DT26/CH20424 ._CH',             # 0F
        'ED6_DT29/CH12320 ._CH',             # 10
        'ED6_DT29/CH12321 ._CH',             # 11
        'ED6_DT07/CH01640 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01260 ._CH',             # 14
        'ED6_DT26/CH20423 ._CH',             # 15
        'ED6_DT07/CH01360 ._CH',             # 16
        'ED6_DT29/CH12330 ._CH',             # 17
        'ED6_DT29/CH12331 ._CH',             # 18
        'ED6_DT29/CH12350 ._CH',             # 19
        'ED6_DT29/CH12351 ._CH',             # 1A
        'ED6_DT29/CH12570 ._CH',             # 1B
        'ED6_DT29/CH12571 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT26/CH20238P._CP',             # 03
        'ED6_DT07/CH02323P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH01090P._CP',             # 06
        'ED6_DT07/CH01370P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01093P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT06/CH20045P._CP',             # 0C
        'ED6_DT26/CH20270P._CP',             # 0D
        'ED6_DT26/CH20422P._CP',             # 0E
        'ED6_DT26/CH20424P._CP',             # 0F
        'ED6_DT29/CH12320P._CP',             # 10
        'ED6_DT29/CH12321P._CP',             # 11
        'ED6_DT07/CH01640P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01260P._CP',             # 14
        'ED6_DT26/CH20423P._CP',             # 15
        'ED6_DT07/CH01360P._CP',             # 16
        'ED6_DT29/CH12330P._CP',             # 17
        'ED6_DT29/CH12331P._CP',             # 18
        'ED6_DT29/CH12350P._CP',             # 19
        'ED6_DT29/CH12351P._CP',             # 1A
        'ED6_DT29/CH12570P._CP',             # 1B
        'ED6_DT29/CH12571P._CP',             # 1C
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58530,
        Z                   = 0,
        Y                   = 49540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 32450,
        Z                   = 0,
        Y                   = 63980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 32530,
        Z                   = 0,
        Y                   = 66280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 29910,
        Z                   = -2000,
        Y                   = 47650,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 35640,
        Z                   = 0,
        Y                   = 77750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 60000,
        Z                   = 0,
        Y                   = 50000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 39000,
        Z                   = -2000,
        Y                   = 46000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 38010,
        Z                   = 0,
        Y                   = 21120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 0,
        Y                   = 47520,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 0,
        Y                   = 44370,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29380,
        Z                   = -2000,
        Y                   = 35460,
        Direction           = 318,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = -2000,
        Y                   = 58930,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
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
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
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
        X                   = 52160,
        Z                   = 0,
        Y                   = 12900,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31950,
        Z                   = 0,
        Y                   = 19680,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15470,
        Z                   = 0,
        Y                   = 14340,
        Unknown_0C          = 180,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21240,
        Z                   = 0,
        Y                   = 45950,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15510,
        Z                   = 0,
        Y                   = 81080,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34060,
        Z                   = -2000,
        Y                   = 46430,
        Unknown_0C          = 180,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33470,
        Z                   = 0,
        Y                   = 66230,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 62710,
        Z                   = 0,
        Y                   = 50010,
        Unknown_0C          = 180,
        Unknown_0E          = 23,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63430,
        Z                   = 0,
        Y                   = 79810,
        Unknown_0C          = 180,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 12290,
        Y                   = -1000,
        Z                   = 47300,
        Range               = 14900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xAE38,
        Unknown_18          = 0x0,
        Unknown_1C          = 85,
    )

    DeclEvent(
        X                   = 12600,
        Y                   = -2000,
        Z                   = 44600,
        Range               = 14000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xB98C,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 13400,
        Y                   = -1000,
        Z                   = 24000,
        Range               = 18060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x625C,
        Unknown_18          = 0x0,
        Unknown_1C          = 50,
    )

    DeclEvent(
        X                   = 26000,
        Y                   = -1000,
        Z                   = 11270,
        Range               = 26800,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x36F6,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 47400,
        Y                   = -1000,
        Z                   = 11070,
        Range               = 49000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x3A48,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = 52060,
        Y                   = -1000,
        Z                   = 26000,
        Range               = 54200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7918,
        Unknown_18          = 0x0,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = 52060,
        Y                   = -1000,
        Z                   = 61000,
        Range               = 54200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x101D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 43200,
        Y                   = -1000,
        Z                   = 82000,
        Range               = 41450,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x136F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 27430,
        Y                   = -1000,
        Z                   = 82000,
        Range               = 26100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x13880,
        Unknown_18          = 0x0,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 13400,
        Y                   = -1000,
        Z                   = 68000,
        Range               = 18060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x10E3C,
        Unknown_18          = 0x0,
        Unknown_1C          = 75,
    )

    DeclEvent(
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 88,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 88,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 89,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 90,
    )


    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 0,
        TriggerY            = 45900,
        TriggerRange        = 700,
        ActorX              = 13480,
        ActorZ              = 1500,
        ActorY              = 46000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66600,
        TriggerZ            = 0,
        TriggerY            = 27910,
        TriggerRange        = 700,
        ActorX              = 66600,
        ActorZ              = 1500,
        ActorY              = 27910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17020,
        TriggerZ            = 0,
        TriggerY            = 22130,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 22000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16940,
        TriggerZ            = 0,
        TriggerY            = 16040,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 16000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57010,
        TriggerZ            = 0,
        TriggerY            = 14090,
        TriggerRange        = 700,
        ActorX              = 56980,
        ActorZ              = 1500,
        ActorY              = 14000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 53,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57730,
        TriggerZ            = 0,
        TriggerY            = 36050,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 36000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 57,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = 0,
        TriggerY            = 39920,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 40110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 59,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59010,
        TriggerZ            = 0,
        TriggerY            = 45880,
        TriggerRange        = 700,
        ActorX              = 59000,
        ActorZ              = 1500,
        ActorY              = 46040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57910,
        TriggerZ            = 0,
        TriggerY            = 51930,
        TriggerRange        = 700,
        ActorX              = 58000,
        ActorZ              = 1500,
        ActorY              = 51970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 63,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 49150,
        TriggerZ            = 0,
        TriggerY            = 79920,
        TriggerRange        = 700,
        ActorX              = 48980,
        ActorZ              = 1500,
        ActorY              = 79890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17000,
        TriggerZ            = 0,
        TriggerY            = 77050,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 76930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 71,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16960,
        TriggerZ            = 0,
        TriggerY            = 71100,
        TriggerRange        = 700,
        ActorX              = 17000,
        ActorZ              = 1500,
        ActorY              = 71000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_A1E",          # 00, 0
        "Function_1_E8F",          # 01, 1
        "Function_2_112A",         # 02, 2
        "Function_3_1140",         # 03, 3
        "Function_4_1377",         # 04, 4
        "Function_5_13D4",         # 05, 5
        "Function_6_16DE",         # 06, 6
        "Function_7_1702",         # 07, 7
        "Function_8_1726",         # 08, 8
        "Function_9_174A",         # 09, 9
        "Function_10_1858",        # 0A, 10
        "Function_11_1E32",        # 0B, 11
        "Function_12_2070",        # 0C, 12
        "Function_13_233B",        # 0D, 13
        "Function_14_27A1",        # 0E, 14
        "Function_15_2A7E",        # 0F, 15
        "Function_16_3456",        # 10, 16
        "Function_17_3712",        # 11, 17
        "Function_18_3ECA",        # 12, 18
        "Function_19_3FF8",        # 13, 19
        "Function_20_403A",        # 14, 20
        "Function_21_410B",        # 15, 21
        "Function_22_423B",        # 16, 22
        "Function_23_543C",        # 17, 23
        "Function_24_54B7",        # 18, 24
        "Function_25_575E",        # 19, 25
        "Function_26_5921",        # 1A, 26
        "Function_27_5AEA",        # 1B, 27
        "Function_28_5CB0",        # 1C, 28
        "Function_29_5E7C",        # 1D, 29
        "Function_30_603F",        # 1E, 30
        "Function_31_6202",        # 1F, 31
        "Function_32_645D",        # 20, 32
        "Function_33_6473",        # 21, 33
        "Function_34_65BD",        # 22, 34
        "Function_35_664B",        # 23, 35
        "Function_36_66E3",        # 24, 36
        "Function_37_6776",        # 25, 37
        "Function_38_680E",        # 26, 38
        "Function_39_6943",        # 27, 39
        "Function_40_6A84",        # 28, 40
        "Function_41_6BA2",        # 29, 41
        "Function_42_6CD9",        # 2A, 42
        "Function_43_71D9",        # 2B, 43
        "Function_44_721D",        # 2C, 44
        "Function_45_7261",        # 2D, 45
        "Function_46_7358",        # 2E, 46
        "Function_47_7543",        # 2F, 47
        "Function_48_75BD",        # 30, 48
        "Function_49_77AE",        # 31, 49
        "Function_50_78F8",        # 32, 50
        "Function_51_7A1A",        # 33, 51
        "Function_52_7DD4",        # 34, 52
        "Function_53_804E",        # 35, 53
        "Function_54_823F",        # 36, 54
        "Function_55_836C",        # 37, 55
        "Function_56_854C",        # 38, 56
        "Function_57_872C",        # 39, 57
        "Function_58_87EF",        # 3A, 58
        "Function_59_88F2",        # 3B, 59
        "Function_60_8A53",        # 3C, 60
        "Function_61_8B2C",        # 3D, 61
        "Function_62_8D1D",        # 3E, 62
        "Function_63_8E22",        # 3F, 63
        "Function_64_8F22",        # 40, 64
        "Function_65_9083",        # 41, 65
        "Function_66_92BA",        # 42, 66
        "Function_67_9320",        # 43, 67
        "Function_68_9511",        # 44, 68
        "Function_69_95FB",        # 45, 69
        "Function_70_987C",        # 46, 70
        "Function_71_9AFD",        # 47, 71
        "Function_72_9CEE",        # 48, 72
        "Function_73_9DC9",        # 49, 73
        "Function_74_9FBA",        # 4A, 74
        "Function_75_A0AA",        # 4B, 75
        "Function_76_A1CC",        # 4C, 76
        "Function_77_A403",        # 4D, 77
        "Function_78_AAD3",        # 4E, 78
        "Function_79_ACB0",        # 4F, 79
        "Function_80_AD05",        # 50, 80
        "Function_81_ADAC",        # 51, 81
        "Function_82_B530",        # 52, 82
        "Function_83_C6B0",        # 53, 83
        "Function_84_C748",        # 54, 84
        "Function_85_C7A1",        # 55, 85
        "Function_86_CA9D",        # 56, 86
        "Function_87_CAA1",        # 57, 87
        "Function_88_CAA5",        # 58, 88
        "Function_89_CAA9",        # 59, 89
        "Function_90_CAAD",        # 5A, 90
    )


    def Function_0_A1E(): pass

    label("Function_0_A1E")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A3D")
    OP_B5(0x0)

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_AB9")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x10, 45800, 0, 46000, 0)
    OP_43(0x10, 0x0, 0x0, 0x4)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0xC, 36500, 0, 70920, 225)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x6, 0x2)
    SetChrPos(0xD, 35500, 0, 69860, 45)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x6, 0x2)
    OP_B5(0x0)
    Jump("loc_BC4")

    label("loc_AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_AD7")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_BC4")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AF7")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_B5(0x0)
    Jump("loc_BC4")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B37")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x11, 46910, 0, 52960, 180)
    SetChrPos(0x10, 22070, 0, 28390, 0)
    Jump("loc_BC4")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_B97")
    SetChrPos(0x10, 20410, 0, 28400, 53)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 40830, -2000, 42670, 270)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_44(0xF, 0xFF)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 9)
    SetChrPos(0xF, 33280, 200, 79020, 180)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_BC4")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_BB0")
    SoundLoad(190)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Jump("loc_BC4")

    label("loc_BB0")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_END)), "loc_CD7")
    OP_A3(0x10FE)
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_BEF")
    OP_A3(0x10F0)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 42)
    Jump("loc_CD4")

    label("loc_BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C0B")
    OP_A3(0x10F1)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 45)
    Jump("loc_CD4")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_C1C")
    OP_A3(0x10F2)
    Event(0, 47)
    Jump("loc_CD4")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_C2D")
    OP_A3(0x10F3)
    Event(0, 49)
    Jump("loc_CD4")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_C3E")
    OP_A3(0x10F4)
    Event(0, 54)
    Jump("loc_CD4")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_C4F")
    OP_A3(0x10F5)
    Event(0, 58)
    Jump("loc_CD4")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_C60")
    OP_A3(0x10F6)
    Event(0, 60)
    Jump("loc_CD4")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_C71")
    OP_A3(0x10F7)
    Event(0, 62)
    Jump("loc_CD4")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_C82")
    OP_A3(0x10F8)
    Event(0, 64)
    Jump("loc_CD4")

    label("loc_C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_C93")
    OP_A3(0x10F9)
    Event(0, 65)
    Jump("loc_CD4")

    label("loc_C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_CA4")
    OP_A3(0x10FA)
    Event(0, 66)
    Jump("loc_CD4")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_CB5")
    OP_A3(0x10FB)
    Event(0, 68)
    Jump("loc_CD4")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_CC6")
    OP_A3(0x10FC)
    Event(0, 72)
    Jump("loc_CD4")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_CD4")
    OP_A3(0x10FD)
    Event(0, 74)

    label("loc_CD4")

    Jump("loc_E8E")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_CF6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_E8E")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_D15")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)
    Jump("loc_E8E")

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_D2B")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 77)
    Jump("loc_E8E")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_D4A")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 78)
    Jump("loc_E8E")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_D62")
    OP_A3(0x10F4)
    OP_B5(0x0)
    SetMapFlags(0x10000000)
    Event(0, 82)
    Jump("loc_E8E")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC3")
    SetMapFlags(0x10000000)
    Event(0, 81)
    Jump("loc_E8E")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8E")
    OP_44(0x10, 0xFF)
    SetChrPos(0x10, 20410, 0, 28400, 53)
    OP_43(0x10, 0x0, 0x6, 0x2)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 40830, -2000, 42670, 270)
    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_44(0xF, 0xFF)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 9)
    SetChrPos(0xF, 33280, 200, 79020, 180)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_A2(0x1221)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_E64"),
        (103, "loc_E6B"),
        (104, "loc_E72"),
        (105, "loc_E79"),
        (106, "loc_E80"),
        (107, "loc_E87"),
        (SWITCH_DEFAULT, "loc_E8E"),
    )


    label("loc_E64")

    Event(0, 25)
    Jump("loc_E8E")

    label("loc_E6B")

    Event(0, 26)
    Jump("loc_E8E")

    label("loc_E72")

    Event(0, 27)
    Jump("loc_E8E")

    label("loc_E79")

    Event(0, 29)
    Jump("loc_E8E")

    label("loc_E80")

    Event(0, 28)
    Jump("loc_E8E")

    label("loc_E87")

    Event(0, 30)
    Jump("loc_E8E")

    label("loc_E8E")

    Return()

    # Function_0_A1E end

    def Function_1_E8F(): pass

    label("Function_1_E8F")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB9")
    OP_B1("t2500_y")
    Jump("loc_EC2")

    label("loc_EB9")

    OP_B1("t2500_n")

    label("loc_EC2")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F22")
    OP_B5(0x0)
    OP_6F(0x21, 60)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)
    Jump("loc_1002")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_F71")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_6F(0x21, 60)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5E")
    OP_6F(0x22, 0)
    OP_72(0x22, 0x10)
    Jump("loc_F6E")

    label("loc_F5E")

    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)

    label("loc_F6E")

    Jump("loc_1002")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_FF2")
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")
    OP_6F(0x22, 0)
    OP_72(0x22, 0x10)
    Jump("loc_FBF")

    label("loc_FAF")

    OP_6F(0x22, 60)
    OP_72(0x22, 0x10)
    OP_64(0x1, 0x1)

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEF")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)

    label("loc_FEF")

    Jump("loc_1002")

    label("loc_FF2")

    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_64(0x0, 0x1)

    label("loc_1002")

    Jump("loc_1053")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_101F")
    OP_64(0x0, 0x1)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 60)
    Jump("loc_1037")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_102D")
    OP_64(0x0, 0x1)
    Jump("loc_1037")

    label("loc_102D")

    OP_72(0x21, 0x10)
    OP_72(0x2D, 0x4)

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 3)), scpexpr(EXPR_END)), "loc_104C")
    OP_64(0x1, 0x1)
    OP_6F(0x22, 60)
    Jump("loc_1053")

    label("loc_104C")

    OP_6F(0x22, 0)

    label("loc_1053")

    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    OP_51(0x25, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_E8F end

    def Function_2_112A(): pass

    label("Function_2_112A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_113F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_112A")

    label("loc_113F")

    Return()

    # Function_2_112A end

    def Function_3_1140(): pass

    label("Function_3_1140")

    OP_8E(0xFE, 0xEA60, 0x0, 0xED80, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE484, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0xF618, 0x1388, 0x0)

    label("loc_11A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1376")
    OP_8E(0xFE, 0xBB80, 0x0, 0xF618, 0x1388, 0x0)
    OP_8E(0xFE, 0xB98C, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xB798, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xB5A4, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xB3B0, 0x0, 0xED80, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xB3B0, 0x0, 0x7918, 0x1388, 0x0)
    OP_8E(0xFE, 0xB5A4, 0x0, 0x75F8, 0x1388, 0x0)
    OP_8E(0xFE, 0xB798, 0x0, 0x72D8, 0x1388, 0x0)
    OP_8E(0xFE, 0xB98C, 0x0, 0x7148, 0x1388, 0x0)
    OP_8E(0xFE, 0xBB80, 0x0, 0x7080, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0x7080, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xE484, 0x0, 0x7148, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x72D8, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0x75F8, 0x1388, 0x0)
    OP_8E(0xFE, 0xEA60, 0x0, 0x7918, 0x1388, 0x0)
    OP_8E(0xFE, 0xEA60, 0x0, 0xED80, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xE86C, 0x0, 0xF0A0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0xF3C0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE484, 0x0, 0xF550, 0x1388, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0xF618, 0x1388, 0x0)
    Jump("loc_11A4")

    label("loc_1376")

    Return()

    # Function_3_1140 end

    def Function_4_1377(): pass

    label("Function_4_1377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D3")
    OP_8E(0xFE, 0xB3B0, 0x0, 0xF9CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x567C, 0x0, 0xF9CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x567C, 0x0, 0x6D2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB3B0, 0x0, 0x6D2E, 0x7D0, 0x0)
    Jump("Function_4_1377")

    label("loc_13D3")

    Return()

    # Function_4_1377 end

    def Function_5_13D4(): pass

    label("Function_5_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1401")

    label("loc_13DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13FE")
    OP_8D(0xFE, 48790, 55520, 45390, 51020, 1000)
    Jump("loc_13DB")

    label("loc_13FE")

    Jump("loc_16DD")

    label("loc_1401")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16DD")
    Sleep(1500)
    OP_8B(0xFE, 0x9858, 0xDAC0, 0x190)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xDAC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xDAC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9470, 0xFFFFF830, 0xDEA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88B8, 0xFFFFF830, 0xDEA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0xFFFFF830, 0xE290, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0xF618, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80E8, 0x0, 0xFA00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5DC0, 0x0, 0xFA00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0xF618, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0xB3B0, 0x7D0, 0x0)
    OP_8B(0xFE, 0x4B64, 0xB3B0, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7080, 0xA3AC, 0x190)
    Sleep(200)
    OP_8B(0xFE, 0x7080, 0xC3B4, 0x190)
    Sleep(1500)
    OP_8B(0xFE, 0x71AC, 0xB3B0, 0x190)
    OP_8E(0xFE, 0x6D60, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7148, 0xFFFFF830, 0xAFC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7148, 0xFFFFF830, 0x8CA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7530, 0xFFFFF830, 0x88B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80E8, 0xFFFFF830, 0x88B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0xFFFFF830, 0x84D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8B(0xFE, 0x8CA0, 0x7148, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7D00, 0x7148, 0x190)
    Sleep(800)
    OP_8B(0xFE, 0x9470, 0x61A8, 0x190)
    Sleep(1000)
    OP_8E(0xFE, 0x9470, 0x0, 0x61A8, 0x7D0, 0x0)
    Sleep(500)
    OP_8B(0xFE, 0x884A, 0x5096, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0xA028, 0x55F0, 0x190)
    Sleep(1000)
    OP_8B(0xFE, 0xA028, 0x6D60, 0x190)
    OP_8E(0xFE, 0xA028, 0x0, 0x6D60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xABE0, 0x0, 0x6D60, 0x7D0, 0x0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8E(0xFE, 0xAFC8, 0x0, 0xB3B0, 0x7D0, 0x0)
    OP_8B(0xFE, 0x4B64, 0xB3B0, 0x190)
    Sleep(500)
    OP_8B(0xFE, 0x7080, 0xA3AC, 0x190)
    Sleep(200)
    OP_8B(0xFE, 0x7080, 0xC3B4, 0x190)
    Sleep(1500)
    OP_8B(0xFE, 0x71AC, 0xB3B0, 0x190)
    OP_8E(0xFE, 0x9858, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
    Jump("loc_1401")

    label("loc_16DD")

    Return()

    # Function_5_13D4 end

    def Function_6_16DE(): pass

    label("Function_6_16DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1701")
    OP_8D(0xFE, 27793, 65500, 35900, 62530, 2000)
    Jump("Function_6_16DE")

    label("loc_1701")

    Return()

    # Function_6_16DE end

    def Function_7_1702(): pass

    label("Function_7_1702")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1725")
    OP_8D(0xFE, 34220, 72290, 36840, 78320, 2000)
    Jump("Function_7_1702")

    label("loc_1725")

    Return()

    # Function_7_1702 end

    def Function_8_1726(): pass

    label("Function_8_1726")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1749")
    OP_8D(0xFE, 27610, 33720, 30640, 36510, 2000)
    Jump("Function_8_1726")

    label("loc_1749")

    Return()

    # Function_8_1726 end

    def Function_9_174A(): pass

    label("Function_9_174A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_17E7")

    ChrTalk(    #0
        0xFE,
        "Ahhh, the school festival was so fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Well, guess I'll fill that hole in my life\x01",
            "with club activities until the next festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_17E7")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        "Ahhh, the school festival was so fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I wonder when our next chance to\x01",
            "party like that will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1854")

    TalkEnd(0xFE)
    Return()

    # Function_9_174A end

    def Function_10_1858(): pass

    label("Function_10_1858")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 2)), scpexpr(EXPR_END)), "loc_1947")

    ChrTalk(    #4
        0xFE,
        (
            "#035FHeh, the girls' dorm of the renowned\x01",
            "royal academy...\x02\x03",

            "I am sure tremendously sweet \x01",
            "buds are flowering within.\x02\x03",

            "#035FHaha... HeheHaha...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #5
        0x101,
        "#1019F(...I am SO not letting him in there.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E2E")

    label("loc_1947")

    OP_22(0xBE, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x4, 0x578)
    OP_99(0xFE, 0x4, 0x0, 0x1F4)
    Sleep(1000)
    OP_A2(0x1262)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DA")

    ChrTalk(    #6
        0xFE,
        "#035FAh, why, if it isn't Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1018FHow's it going, Olivier?\x01",
            "Turn anything up?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Jump("loc_1A2F")

    label("loc_19DA")


    ChrTalk(    #8
        0xFE,
        "#035FHeh, why, Princess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        "#040FHello, Olivier. How's the questioning going?\x02",
    )

    CloseMessageWindow()

    label("loc_1A2F")


    ChrTalk(    #10
        0xFE,
        (
            "#035FHaha, marvelous! Or so I imagine.\x01",
            "I left that business to Dorothy.\x02\x03",

            "More importantly, I heard tell of a dorm\x01",
            "for the female students.\x02\x03",

            "I am urgently searching for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        "#044FFor the girls' dorm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1004FWhy the heck are you searching for that?\x02\x03",

            "#1015FWell, I think I can kiiinda guess, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #13
        0xFE,
        (
            "#031FHeh, that should be obvious.\x02\x03",

            "To safeguard the place where these maidens\x01",
            "lay themselves to sleep, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F*sigh* I knew it was gonna go there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#045FHow, um, expected of you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "#035FIt would, after all, be far too late once\x01",
            "the foul hands of evil disturbed their peace\x01",
            "and put them in danger, you see...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0xFE,
        (
            "#031FOh, yes. Incidentally, Estelle...\x02\x03",

            "I believe you have spent some time\x01",
            "at this academy before.\x02\x03",

            "Perhaps you could guide me to the dorm?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #18
        0x101,
        (
            "#1016FAh...ha...\x02\x03",

            "#1016FI'm, ah, a little busy right now, so...\x01",
            "another time!\x02\x03",

            "#1019F(I know whose 'foul hands of evil' I'M\x01",
            "going to safeguard the girls' dorm from.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1858 end

    def Function_11_1E32(): pass

    label("Function_11_1E32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(    #19
        0xFE,
        "Really, there's all sorts who attend this school.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5B")

    label("loc_1E7D")

    OP_A2(0x6)

    ChrTalk(    #20
        0xFE,
        (
            "When I was making my rounds through\x01",
            "the schoolhouse yesterday, I found a male\x01",
            "student hiding in a classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "He just popped outta nowhere like a damned ghost.\x01",
            "I was so surprised I thought I'd die right there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5B")

    Jump("loc_206C")

    label("loc_1F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1FDE")

    ChrTalk(    #22
        0xFE,
        "Phew! Everything on campus checks out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Now, then, just need to have a look-see\x01",
            "at all the clubs' equipment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206C")

    label("loc_1FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_206C")

    ChrTalk(    #24
        0xFE,
        "The clubs are starting up again tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'm doin' my rounds on the school grounds,\x01",
            "making sure everything's in good shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E32 end

    def Function_12_2070(): pass

    label("Function_12_2070")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_216B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210B")

    ChrTalk(    #26
        0xFE,
        "Oh, bracers. Really, great work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I'm busy for my part getting\x01",
            "ready to start classes again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2168")

    label("loc_210B")


    ChrTalk(    #29
        0xFE,
        (
            "I'm busy for my part getting ready\x01",
            "to start classes again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_2168")

    Jump("loc_2337")

    label("loc_216B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_21CD")

    ChrTalk(    #31
        0xFE,
        "All right, clubs start again today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Guess it's time to reforge some slackers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_21E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_21DE")
    Jump("loc_21E1")

    label("loc_21DE")

    OP_A2(0x5)

    label("loc_21E1")

    Jump("loc_2337")

    label("loc_21E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_2278")

    ChrTalk(    #33
        0xFE,
        "Phew! Day's finally over, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Guess I'd better make an early night of\x01",
            "it so that I'm ready tomorrow when clubs\x01",
            "start up again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_2278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_2337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_22A2")

    ChrTalk(    #35
        0xFE,
        "One two, one two...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_22A2")

    OP_A2(0x5)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #36
        0xFE,
        (
            "Clubs start up again tomorrow\x01",
            "after a long hiatus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I'm getting in some running today while\x01",
            "I can to get myself back in the groove.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    TalkEnd(0xFE)
    Return()

    # Function_12_2070 end

    def Function_13_233B(): pass

    label("Function_13_233B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_248A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23D9")

    ChrTalk(    #38
        0xFE,
        (
            "There was someone suspicious hiding\x01",
            "out in the old schoolhouse, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "How exciting!\x01",
            "It's like something straight out of a novel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2487")

    label("loc_23D9")

    OP_A2(0x4)

    ChrTalk(    #40
        0xFE,
        "I just heard a juicy rumor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "There was someone suspicious hiding\x01",
            "out in the old schoolhouse, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "How exciting!\x01",
            "It's like something straight out of a novel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2487")

    Jump("loc_279D")

    label("loc_248A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_25FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2527")

    ChrTalk(    #43
        0xFE,
        (
            "I'm thinking of trying my hand at writing\x01",
            "a full-length novel over vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I think I'll make a school like ours\x01",
            "as the setting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FC")

    label("loc_2527")

    OP_A2(0x4)

    ChrTalk(    #45
        0xFE,
        (
            "I'm thinking of trying my hand at writing\x01",
            "a full-length novel over vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "What do you think of the school?\x01",
            "It's pretty ideal for a novel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I'm thinking of making the school\x01",
            "the setting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FC")

    Jump("loc_279D")

    label("loc_25FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_279D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(    #48
        0xFE,
        (
            "It needs to be charming and yet...\x01",
            "mysterious. A mysterious phenomenon\x01",
            "assaulting the academy... Yes... Yes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I might be able to use it\x01",
            "in the novel I'm planning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279D")

    label("loc_26BC")

    OP_A2(0x4)

    ChrTalk(    #50
        0xFE,
        "Strange events during the exams...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "No, nothing in particular happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "But, how interesting. Mysterious phenomena\x01",
            "assaulting the academy... Oh, my.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I might be able to use it\x01",
            "in the novel I'm planning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279D")

    TalkEnd(0xFE)
    Return()

    # Function_13_233B end

    def Function_14_27A1(): pass

    label("Function_14_27A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_27F8")

    ChrTalk(    #54
        0xFE,
        (
            "The Art Club's scheduled to do\x01",
            "some sketching together today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286A")

    label("loc_27F8")

    OP_A2(0x3)

    ChrTalk(    #55
        0xFE,
        (
            "The Art Club's scheduled to do\x01",
            "some sketching together today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "...But no one's here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Am I early?\x02",
    )

    CloseMessageWindow()

    label("loc_286A")

    Jump("loc_2A7A")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_29AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28F6")

    ChrTalk(    #58
        0xFE,
        "It's been a while since I've faced a canvas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I feel like I could paint or draw\x01",
            "something really lovely today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29AC")

    label("loc_28F6")

    OP_A2(0x3)

    ChrTalk(    #60
        0xFE,
        "Hmmhmmhmmmmm... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "The Art Club's searching for a motif\x01",
            "in preparation for a production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Oh, the schoolhouse bathed in the glow\x01",
            "of the sunset might be a good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AC")

    Jump("loc_2A7A")

    label("loc_29AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_2A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A05")

    ChrTalk(    #63
        0xFE,
        "I don't think there was anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "Try asking someone else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A7A")

    label("loc_2A05")

    OP_A2(0x3)

    ChrTalk(    #65
        0xFE,
        "Strange events during the exam period...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "No, I don't really know of anything.\x01",
            "Try asking someone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7A")

    TalkEnd(0xFE)
    Return()

    # Function_14_27A1 end

    def Function_15_2A7E(): pass

    label("Function_15_2A7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_31EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9A")
    Call(0, 17)
    OP_A2(0x20C5)
    Jump("loc_31E8")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D7")

    ChrTalk(    #67
        0xFE,
        (
            "Milady needs to be possessed of\x01",
            "a broader view...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Those born into noble families are\x01",
            "fated to bear the weight of their name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1015F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #70
        0xFE,
        "Oh, is there something you require?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1008FY-Yeah, so, I'm just asking for\x01",
            "work-related reasons, but...\x02\x03",

            "#1015F(Umm, so...how did the arranged wedding\x01",
            "meeting go in the end?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #72
        0x102,
        (
            "#1048F(Wait just a sec... What part\x01",
            "of this is work-related, exactly?)\x02\x03",

            "(You just want to know.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #73
        0x101,
        (
            "#1009F(H-Hey, what's the problem? It's a\x01",
            "LITTLE related to work. Sort of.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "(Well, I don't really mind...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "(It was a great success, of course.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(400)

    ChrTalk(    #76
        0x101,
        (
            "#1004F(Whaaaat?! It succeeded?!)\x02\x03",

            "#1013F(So, that means... Felicity, she's...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "(These things have an order to them,\x01",
            "so it did not jump immediately to an\x01",
            "engagement.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "(Ultimately, it simply means both of\x01",
            "them find the other acceptable.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F(I-I see...)\x02\x03",

            "#1007F(Phew! This might be someone else's\x01",
            "situation, but I kinda freaked out there\x01",
            "for a sec.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F76")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #80
        0x103,
        (
            "#027F(Hmm? And why are you all flustered\x01",
            "about this, Estelle?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #81
        0x101,
        (
            "#1013F(Ah, n-no real reason... It's just, she's\x01",
            "the same age as me, so... y'know.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3032")

    label("loc_2F76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3032")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #82
        0x106,
        "#055F(The heck? Why are YOU all bothered by it?)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1013F(Ah, n-no real reason... It's just, she's\x01",
            "the same age as me, so... y'know.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3032")


    ChrTalk(    #84
        0xFE,
        (
            "(For now, we will have them deepen\x01",
            "their connection through writing\x01",
            "letters and such.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "(So, their engagement will still\x01",
            "be some time in the future.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20C6)
    Jump("loc_315E")

    label("loc_30D7")


    ChrTalk(    #86
        0xFE,
        (
            "Milady needs to be possessed of\x01",
            "a broader view...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Those born into noble families are\x01",
            "fated to bear the weight of their name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315E")

    Jump("loc_31E8")

    label("loc_3161")


    ChrTalk(    #88
        0xFE,
        (
            "Milady needs to be possessed of\x01",
            "a broader view...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Those born into noble families are\x01",
            "fated to bear the weight of their name.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E8")

    Jump("loc_3452")

    label("loc_31EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32D2")

    ChrTalk(    #90
        0xFE,
        (
            "(The other part of this engagement meeting\x01",
            "will be a youth of Imperial nobility...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "(Apparently he is interested in the young lady\x01",
            "after hearing that she is a progressive woman\x01",
            "of many talents residing abroad.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3452")

    label("loc_32D2")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        (
            "(Felicity believes I've obtained permission\x01",
            "from her home, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "(Actually, this trip back was always\x01",
            "intended to be a journey to Bose.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "(There's a restaurant there, as well as\x01",
            "airships to and from the Empire, so...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "(It truly is perfect as a site for an arranged\x01",
            "wedding meeting with a member of the\x01",
            "Imperial nobility.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #96
        0xFE,
        "(...Do keep this a secret.)\x02",
    )

    CloseMessageWindow()

    label("loc_3452")

    TalkEnd(0xFE)
    Return()

    # Function_15_2A7E end

    def Function_16_3456(): pass

    label("Function_16_3456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3472")
    Call(0, 17)
    OP_A2(0x20C5)
    Jump("loc_3585")

    label("loc_3472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3503")

    ChrTalk(    #97
        0xFE,
        "A-Anyway... You really saved me today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "It seems the kingdom is in danger,\x01",
            "but we're dedicated to protecting\x01",
            "our school life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3585")

    label("loc_3503")


    ChrTalk(    #99
        0xC,
        (
            "There's not a person who would be\x01",
            "happy to have their life controlled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "I can't think of things as clearly\x01",
            "as Reina can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3585")

    Jump("loc_370E")

    label("loc_3588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35FC")

    ChrTalk(    #101
        0xFE,
        (
            "I'll be able to stay in Bose for a\x01",
            "little while before heading home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "Reina has some good parts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_370E")

    label("loc_35FC")

    OP_A2(0x1)

    ChrTalk(    #103
        0xFE,
        "Phew... Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'll be able to stay in Bose for a\x01",
            "little while before heading home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "It won't be long, but I should have enough\x01",
            "time to enjoy the sights of the city a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "This is thanks to Reina negotiating\x01",
            "with my family back in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370E")

    TalkEnd(0xFE)
    Return()

    # Function_16_3456 end

    def Function_17_3712(): pass

    label("Function_17_3712")

    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xC, 0x101, 0)
    Sleep(400)

    ChrTalk(    #107
        0xC,
        "Estelle and Joshua...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #108
        0xD,
        "Everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        "You have my sincerest gratitude for saving milady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xD,
        (
            "As a representative of the household,\x01",
            "allow me to offer you our heartfelt\x01",
            "thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1017FNo, we don't need thanks, really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#1040FYes, we were just fulfilling our duties.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #113
        0xC,
        "Well! Bracers are always so humble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        "Still, I'm quite indebted to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "Thanks to you solving this case the gap\x01",
            "between us has been filled in, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C16")

    ChrTalk(    #116
        0x101,
        (
            "#1004FAh... So, then, that means...\x02\x03",

            "You two've made up?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #117
        0xC,
        "Yes, for now, at least.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #118
        0xD,
        "It seems she at least understands my position.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        "However...I do not believe she is satisfied.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(    #120
        0xC,
        "Oh, but of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "How could I possibly be satisfied having people\x01",
            "arranging my wedding without any input from me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)

    ChrTalk(    #122
        0xD,
        (
            "As I said, please stop focusing on such\x01",
            "small details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xD,
        (
            "Felicity, you need to possess a broader\x01",
            "view of things...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0xC,
        (
            "Th-This is my future, you know!\x01",
            "What about that is small?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1016FN-Now, now... Calm down, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1052F(Can you really call this 'making up'?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1015F(Hmm, it's hard to say.)\x02\x03",

            "#1016F(Well, I guess it's true they've\x01",
            "returned to how they usually are.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EBB")

    label("loc_3C16")

    TurnDirection(0xD, 0xC, 400)

    ChrTalk(    #128
        0xD,
        (
            "Well, certainly it seems she at\x01",
            "least understands my position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "However, milady must learn an attitude\x01",
            "that is unfazed by the little details.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)

    ChrTalk(    #130
        0xC,
        "My, but of course I would be fazed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "There's not a person who would be\x01",
            "happy to have their life controlled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xD,
        (
            "I am saying that thinking about it in such\x01",
            "a manner is small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xD,
        "*sigh* Oh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xD,
        (
            "It seems milady's qualities are ultimately\x01",
            "lesser than I'd thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0xC,
        "Wh-What did you say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#1052F(Seems like they've started fighting...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1016F(Aaand things are back to normal.)\x02\x03",

            "(They're always like this, so it might\x01",
            "be proof of how well they get along.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBB")

    OP_A2(0x1)
    OP_A2(0x2)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    Return()

    # Function_17_3712 end

    def Function_18_3ECA(): pass

    label("Function_18_3ECA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F4F")

    ChrTalk(    #138
        0xFE,
        (
            "I wonder what that white shadow\x01",
            "ended up being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Well, it's probably just one of\x01",
            "that suspicious guy's tricks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF4")

    label("loc_3F4F")

    OP_A2(0x0)

    ChrTalk(    #140
        0xFE,
        "Hey, I heard the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Apparently there was some suspicious\x01",
            "guy hiding in the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "I wonder if that white shadow I saw\x01",
            "was his doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF4")

    TalkEnd(0xFE)
    Return()

    # Function_18_3ECA end

    def Function_19_3FF8(): pass

    label("Function_19_3FF8")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "Good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "You can leave further guarding to me!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3FF8 end

    def Function_20_403A(): pass

    label("Function_20_403A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AD")

    ChrTalk(    #145
        0xFE,
        "Sorry we're so late in getting here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "With our airships unusable, deployment\x01",
            "takes time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_4107")

    label("loc_40AD")


    ChrTalk(    #147
        0xFE,
        (
            "We're very sorry we were so late in arriving.\x01",
            "We'll handle the guard work from here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4107")

    TalkEnd(0xFE)
    Return()

    # Function_20_403A end

    def Function_21_410B(): pass

    label("Function_21_410B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E8")

    ChrTalk(    #148
        0xFE,
        (
            "It only just occurred to me now that\x01",
            "all the craziness is over, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Those maniacs were using orbal guns,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "How could they use guns with orbments\x01",
            "not working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "It's a mystery...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4237")

    label("loc_41E8")


    ChrTalk(    #152
        0xFE,
        (
            "How could they use guns with orbments\x01",
            "not working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "It's a mystery...\x02",
    )

    CloseMessageWindow()

    label("loc_4237")

    TalkEnd(0xFE)
    Return()

    # Function_21_410B end

    def Function_22_423B(): pass

    label("Function_22_423B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4248")
    Return()

    label("loc_4248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4259")
    Call(0, 83)

    label("loc_4259")

    EventBegin(0x0)
    OP_71(0x2, 0x10)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x3C)
    Sleep(1000)
    Fade(1000)
    OP_C4(0x0, 0x2)
    OP_7E(0x44C, 0x7D0, 0x64, 0xA, 0x1)
    AddParty(0x4, 0xF9, 0xFF)
    OP_31(0x4, 0x0, 0x26)
    OP_31(0x4, 0xFE, 0x0)
    OP_41(0x4, 0x7F, 0xFF)
    OP_41(0x4, 0xFF, 0xFF)
    OP_41(0x4, 0x120, 0xFF)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x2D4, 0x1)
    OP_41(0x4, 0x25B, 0x2)
    OP_35(0x4, 0x0)
    OP_35(0x4, 0x8C)
    OP_BB(0x4, 0x6, 0xFA)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x105, 0x8)
    SetChrPos(0x101, 22270, 0, 46760, 91)
    SetChrPos(0xF7, 21650, 0, 45420, 84)
    SetChrPos(0x104, 20500, 0, 47120, 85)
    SetChrPos(0x127, 20100, 0, 46000, 85)
    SetChrPos(0x105, 22100, 0, 59170, 195)
    SetChrPos(0x8, 20980, 0, 58890, 171)
    SetChrPos(0x9, 22410, 0, 58760, 179)
    OP_6D(61060, 0, 55000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(6110, 0)
    OP_6C(75000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x3E8)
    OP_DE("Jenis Royal Academy")

    def lambda_43CA():
        OP_6D(21160, 0, 46450, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_43CA)

    def lambda_43E2():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_43E2)
    Sleep(2000)
    StopSound(0x9470, 0x14C08, 0x1F40)

    def lambda_4404():
        OP_6B(3000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4404)

    def lambda_4414():
        OP_67(0, 8350, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4414)
    Sleep(8000)

    ChrTalk(    #154
        0x104,
        (
            "#033FAhh! So this is the royal academy.\x02\x03",

            "#035FFull of budding flowers trembling with\x01",
            "potential, dewed with the passionate\x01",
            "moisture of sweat and youthful tears...\x02\x03",

            "Ah... A lovely place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x127,
        (
            "#151FOh, wow, I see like ten pictures\x01",
            "I wanna take already!\x02\x03",

            "I'm gonna go through sooooo\x01",
            "much fiiiilm...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_45DF")

    ChrTalk(    #156
        0x106,
        (
            "#551F#6PUh, just a reminder, we're here\x01",
            "to investigate the ghost mess.\x02\x03",

            "#552FKeep your heads in the game,\x01",
            "thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4667")

    label("loc_45DF")


    ChrTalk(    #157
        0x103,
        (
            "#025F#6P*sigh* You've completely forgotten\x01",
            "why we're here, haven't you?\x02\x03",

            "#020FRemember--we're here to investigate\x01",
            "the ghost issue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4667")


    ChrTalk(    #158
        0x101,
        (
            "#1025F#6PThis kinda makes me all nostalgic,\x01",
            "though...\x02\x03",

            "I mean, we were only here a week,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_476E")

    ChrTalk(    #159
        0x106,
        (
            "#051F#6PHey, that just goes to show how\x01",
            "important the time you spent with\x01",
            "your friends was.\x02\x03",

            "You did somethin' for the academy\x01",
            "play, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_480A")

    label("loc_476E")


    ChrTalk(    #160
        0x103,
        (
            "#027F#6PThat just means you\x01",
            "cherish the time you spent with\x01",
            "your friends.\x02\x03",

            "I believe you acted together in a play\x01",
            "during their school festival, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_480A")


    ChrTalk(    #161
        0x127,
        (
            "#151FOoooh, I heard about that from Nial!\x02\x03",

            "Estelle was a knight, and Joshua\x01",
            "was a princess, right?\x02\x03",

            "#154FOooh, I wish I coulda gotten\x01",
            "some pictures...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x104,
        (
            "#036FWait... What...? Is this true?!\x02\x03",

            "#034FAh, what a tragedy! That I should miss\x01",
            "Joshua at his most graceful and alluring!\x02\x03",

            "We simply must find him and have\x01",
            "him wear such splendor again!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(    #163
        0x101,
        (
            "#1007F#4PAnd all of my memories are ruined forever.\x02\x03",

            "#1015FChanging gears, though... Matron Theresa said\x01",
            "the test period would be over soon.\x02\x03",

            "I wonder if we're here a little early,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x127, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4ADE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ADE)

    def lambda_4AEC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4AEC)

    def lambda_4AFA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4AFA)

    def lambda_4B08():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_4B08)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #164
        0x101,
        "#1004F#6P*gasp*! Sieg!\x02",
    )

    CloseMessageWindow()
    OP_6D(27230, 0, 48860, 1500)

    def lambda_4B48():
        OP_6D(21160, 0, 46450, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4B48)
    OP_22(0x8C, 0x0, 0x64)
    SetChrPos(0xA, 36940, 6000, 46020, 90)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x1, 0x0, 0x2)
    OP_8E(0xA, 0x55F0, 0x7D0, 0xBCAC, 0x1770, 0x0)
    OP_22(0x197, 0x0, 0x64)
    OP_44(0xA, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFA81C0, 0x1770, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFE2B40, 0x1388, 0x1)
    OP_97(0xA, 0x56FE, 0xB6A8, 0xFFFF15A0, 0xBB8, 0x1)
    OP_8C(0x101, 135, 0)
    OP_43(0xA, 0x1, 0x0, 0x2)

    def lambda_4BEC():
        OP_8C(0xA, 90, 100)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4BEC)
    OP_8F(0xA, 0x5708, 0x2BC, 0xB43C, 0x7D0, 0x0)
    Fade(500)
    OP_44(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 3)
    OP_0D()
    OP_8C(0xF7, 0, 400)
    SetChrSubChip(0x101, 5)
    OP_8C(0x104, 135, 400)

    ChrTalk(    #165
        0xA,
        "#311F#6PScreee! Screee, screee! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1016F#4PHaha! I have NO idea what you're saying,\x01",
            "but you're welcoming me, right?\x02\x03",

            "#1006FHow have you been, Sieg?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        "#311F#6PScreee! ㈱\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #168
        0x105,
        "Girl's Voice",
        "#6PEstelle...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 3)
    SetChrFlags(0x101, 0x20)
    TurnDirection(0x101, 0x105, 400)

    def lambda_4D4D():
        TurnDirection(0xF7, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4D4D)

    def lambda_4D5B():
        TurnDirection(0x104, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D5B)

    def lambda_4D69():
        TurnDirection(0x127, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_4D69)
    ClearChrFlags(0x101, 0x20)

    ChrTalk(    #169
        0x101,
        "#1025F#6POh...!\x02",
    )

    CloseMessageWindow()

    def lambda_4D91():
        OP_6D(21750, 0, 50070, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4D91)

    def lambda_4DA9():
        OP_67(0, 9280, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4DA9)

    def lambda_4DC1():
        OP_6C(328000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4DC1)

    def lambda_4DD1():
        OP_6B(2840, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_4DD1)
    Fade(250)
    SetChrPos(0xA, 22710, 0, 46900, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_4E0B():
        OP_8F(0xA, 0x6342, 0xD48, 0xC968, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4E0B)
    OP_43(0xA, 0x1, 0x0, 0x2)

    def lambda_4E2D():
        OP_8E(0xFE, 0x5852, 0x0, 0xCC4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E2D)
    Sleep(1000)

    def lambda_4E4D():
        OP_8E(0xFE, 0x54B0, 0x0, 0xCFC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E4D)
    Sleep(300)

    def lambda_4E6D():
        OP_8E(0xFE, 0x591A, 0x0, 0xD17E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E6D)
    WaitChrThread(0xA, 0x0)
    OP_8C(0xA, 270, 180)
    OP_8C(0xA, 180, 180)
    Sleep(250)
    OP_44(0xA, 0x1)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x1, 0x2)
    WaitChrThread(0x1, 0x3)
    Sleep(500)

    ChrTalk(    #170
        0x101,
        (
            "#1025F#5PKloe...\x02\x03",

            "#1016FHaha... Been a while, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#542FIt...has.\x02\x03",

            "Umm... I...\x02\x03",

            "#049F...\x01",
            "...\x01",
            "I...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F38():

        label("loc_4F38")

        TurnDirection(0xF7, 0x105, 0)
        OP_48()
        Jump("loc_4F38")

    QueueWorkItem2(0xF7, 2, lambda_4F38)

    def lambda_4F49():

        label("loc_4F49")

        TurnDirection(0x104, 0x105, 0)
        OP_48()
        Jump("loc_4F49")

    QueueWorkItem2(0x104, 2, lambda_4F49)

    def lambda_4F5A():

        label("loc_4F5A")

        TurnDirection(0x127, 0x105, 0)
        OP_48()
        Jump("loc_4F5A")

    QueueWorkItem2(0x127, 2, lambda_4F5A)

    def lambda_4F6B():
        OP_8E(0x105, 0x55F0, 0x0, 0xB810, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F6B)
    Sleep(300)
    Fade(500)
    OP_6D(22200, 0, 48130, 0)
    OP_67(0, 9280, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)

    def lambda_4FCD():
        OP_6D(22270, 0, 46760, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4FCD)

    def lambda_4FE5():
        OP_67(0, 9280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4FE5)

    def lambda_4FFD():
        OP_8E(0xFE, 0x53A2, 0x0, 0xBEE6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FFD)
    Sleep(300)

    def lambda_501D():
        OP_8E(0xFE, 0x5802, 0x0, 0xC01C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_501D)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x105, 0x80)
    OP_99(0x101, 0x0, 0x3, 0x7D0)
    OP_44(0xF7, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x127, 0x2)

    def lambda_5066():

        label("loc_5066")

        TurnDirection(0xF7, 0x101, 0)
        OP_48()
        Jump("loc_5066")

    QueueWorkItem2(0xF7, 2, lambda_5066)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x101,
        "#1025FWhoa! What's wrong, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x105,
        (
            "#049F#4PI'm sorry... I'm so, so sorry...\x02\x03",

            "You've suffered so much and I...\x01",
            "I can't do anything...\x02\x03",

            "I can't do anything to help my friends...\x01",
            "I'm such a wretch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1025FHey, hey... Don't say that.\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x6, 0x5DC)
    Sleep(500)

    ChrTalk(    #175
        0x101,
        (
            "#1012FI'm glad you care so much.\x02\x03",

            "I'm sure Joshua would feel\x01",
            "the same way.\x02\x03",

            "#1017FI'm...just happy to see you\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        (
            "#047F#4PI... Me too...\x02\x03",

            "#048FThank Aidios we were able to meet again...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #177
        0x8,
        (
            "#649F#4PGood griiiiieeef, you two are dramatic\x01",
            "even OFF the stage!\x02\x03",

            "#648FHey, Estelle! Think we saw each other\x01",
            "last at the birthday celebrations, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1017FHi, Jill! Yeah, that's about right.\x02\x03",

            "And Hans, too! Hello!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#730F#2PHi, Estelle, everyone.\x02\x03",

            "I'd love to chat, but I think we need\x01",
            "to put that aside for a minute.\x02\x03",

            "You guys are here on bracer business,\x01",
            "right? The dean wants to see you.\x01",
            "We'll show you the way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2510   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_22_423B end

    def Function_23_543C(): pass

    label("Function_23_543C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #180
        (
            "\x07\x05Due to exams, entry to academy grounds is restricted.\x01",
            "-Jenis Royal Academy\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_543C end

    def Function_24_54B7(): pass

    label("Function_24_54B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54DA")
    Call(0, 80)
    Jump("loc_5704")

    label("loc_54DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5655")
    OP_A2(0x2017)
    EventBegin(0x0)
    Fade(500)
    OP_6D(65860, 0, 27990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(122000, 0)
    OP_6E(262, 0)
    OP_6D(65860, 0, 27990, 0)
    SetChrPos(0x102, 65860, 0, 27990, 90)
    SetChrSubChip(0x102, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #181
        "\x07\x05The back gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #182
        0x102,
        (
            "#1043F(Beyond here is the old schoolhouse...)\x02\x03",

            "#1040F(Mmm, just in case...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #183
        "\x07\x05Joshua pulled out his tools and inserted them into the lock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x50)
    Sleep(1000)
    Call(0, 76)
    EventEnd(0x0)
    Jump("loc_5704")

    label("loc_5655")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #184
        "\x07\x05The back gate is unlocked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #185
        0x102,
        (
            "#1035F(I don't need to go past here right now.)\x02\x03",

            "#1042F(I should return to investigating school grounds.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5704")

    TalkEnd(0xFF)
    Jump("loc_575D")

    label("loc_570A")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #186
        "\x07\x05The back gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_575D")

    Return()

    # Function_24_54B7 end

    def Function_25_575E(): pass

    label("Function_25_575E")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 22990, 250, 66860, 176)
    SetChrPos(0x105, 22040, 250, 66860, 175)
    OP_6D(22280, 480, 67450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #187
        0x101,
        "#1004FHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #188
        0x105,
        (
            "#542FI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #189
        0x101,
        (
            "#1006FYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_25_575E end

    def Function_26_5921(): pass

    label("Function_26_5921")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 40810, 250, 73170, 271)
    SetChrPos(0x105, 40760, 250, 74250, 287)
    OP_6D(41600, 460, 73930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x101,
        "#1004F#2PHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #191
        0x105,
        (
            "#542FI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #192
        0x101,
        (
            "#1006F#2PYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_26_5921 end

    def Function_27_5AEA(): pass

    label("Function_27_5AEA")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 52040, 0, 65500, 258)
    SetChrPos(0x105, 52280, 0, 64660, 252)
    OP_6D(52780, 0, 65680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        "#1004FHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #194
        0x105,
        (
            "#542F#4PI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #195
        0x101,
        (
            "#1006FYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_27_5AEA end

    def Function_28_5CB0(): pass

    label("Function_28_5CB0")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 51910, 0, 61530, 268)
    SetChrPos(0x105, 52160, 0, 62400, 253)
    OP_6D(52910, 0, 61210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x101,
        "#1004F#2PHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #197
        0x105,
        (
            "#542F#1PI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #198
        0x101,
        (
            "#1006F#2PYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_28_5CB0 end

    def Function_29_5E7C(): pass

    label("Function_29_5E7C")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 46730, 0, 45410, 277)
    SetChrPos(0x105, 47060, 0, 46350, 262)
    OP_6D(47100, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x101,
        "#1004FHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #200
        0x105,
        (
            "#542FI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1006FYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_29_5E7C end

    def Function_30_603F(): pass

    label("Function_30_603F")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrPos(0x101, 51870, 0, 30080, 275)
    SetChrPos(0x105, 52310, 0, 29300, 257)
    OP_6D(52390, 0, 30630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #202
        0x101,
        "#1004FHoly crap, it's late already.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #203
        0x105,
        (
            "#542FI think we've gotten just about everything\x01",
            "we can from the students. Shall we head\x01",
            "back to the Student Council room?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #204
        0x101,
        (
            "#1006FYeah, let's.\x02\x03",

            "With any luck, we can put together\x01",
            "what we've heard with everyone else\x01",
            "and figure out what's up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1221)
    OP_28(0x83, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_30_603F end

    def Function_31_6202(): pass

    label("Function_31_6202")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    OP_DB()
    OP_6D(72780, 0, 23250, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(40000, 0)
    OP_6E(439, 0)
    SetChrFlags(0x13, 0x20)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x1)
    SetChrPos(0x13, 71000, 7000, 17030, 180)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x13, 0)

    def lambda_6277():

        label("loc_6277")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6277")

    QueueWorkItem2(0x13, 1, lambda_6277)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    OP_A0(0x13, 0xB4, 0xB4, 0xB4, 0x0)
    FadeToBright(2000, 0)

    def lambda_62A8():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_62A8)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFA81C0, 0xBB8, 0x1)
    OP_97(0x13, 0x10D88, 0x4286, 0xFFFEA070, 0x7D0, 0x1)
    Sleep(300)
    OP_8C(0x13, 90, 1000)
    OP_8C(0x13, 360, 1000)
    OP_8C(0x13, 270, 1000)
    Sleep(300)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)

    def lambda_631E():
        OP_6D(71780, 0, 23250, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_631E)

    def lambda_6336():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6336)

    def lambda_6346():
        OP_96(0x13, 0x101C6, 0x1388, 0x4286, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6346)
    WaitChrThread(0x13, 0x2)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x0, 0x1)
    Sleep(500)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 21)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    SetChrSubChip(0x13, 8)
    Sleep(100)
    SetChrSubChip(0x13, 16)
    Sleep(100)
    SetChrSubChip(0x13, 24)
    Sleep(100)
    SetChrSubChip(0x13, 32)
    Sleep(100)
    SetChrSubChip(0x13, 40)
    Sleep(100)
    SetChrSubChip(0x13, 48)
    Sleep(100)
    SetChrSubChip(0x13, 56)
    Sleep(100)
    SetChrSubChip(0x13, 64)
    Sleep(100)
    SetChrSubChip(0x13, 72)
    Sleep(1000)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x2)
    OP_8C(0x13, 90, 600)

    def lambda_640D():
        OP_6D(74780, 0, 23250, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_640D)

    def lambda_6425():
        OP_8E(0xFE, 0x124F8, 0x1B58, 0x4F4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6425)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6202 end

    def Function_32_645D(): pass

    label("Function_32_645D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6472")
    OP_99(0xFE, 0x0, 0x7, 0x1F4)
    Jump("Function_32_645D")

    label("loc_6472")

    Return()

    # Function_32_645D end

    def Function_33_6473(): pass

    label("Function_33_6473")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x16, 0x1, 0x0, 0x24)
    OP_43(0x17, 0x1, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    OP_6D(45900, 0, 46020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_6564():
        OP_6D(15710, 0, 46020, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6564)

    def lambda_657C():
        OP_6C(90000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_657C)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_6473 end

    def Function_34_65BD(): pass

    label("Function_34_65BD")

    SetChrPos(0xFE, 46550, 0, 54620, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_65D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_664A")
    OP_8C(0xFE, 315, 400)
    Sleep(600)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB34C, 0x0, 0xC026, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB5D6, 0x0, 0xD55C, 0x7D0, 0x0)
    Jump("loc_65D3")

    label("loc_664A")

    Return()

    # Function_34_65BD end

    def Function_35_664B(): pass

    label("Function_35_664B")

    SetChrPos(0xFE, 45710, 0, 44810, 45)
    ClearChrFlags(0xFE, 0x80)
    Sleep(200)

    label("loc_6666")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66E2")
    Sleep(600)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB608, 0x0, 0x7C2E, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(600)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB28E, 0x0, 0xAF0A, 0x7D0, 0x0)
    Jump("loc_6666")

    label("loc_66E2")

    Return()

    # Function_35_664B end

    def Function_36_66E3(): pass

    label("Function_36_66E3")

    SetChrPos(0xFE, 21070, 0, 38420, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_66F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6775")
    OP_8E(0xFE, 0x524E, 0x0, 0xD28C, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x524E, 0x0, 0x9614, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Jump("loc_66F9")

    label("loc_6775")

    Return()

    # Function_36_66E3 end

    def Function_37_6776(): pass

    label("Function_37_6776")

    SetChrPos(0xFE, 22990, 0, 54810, 180)
    ClearChrFlags(0xFE, 0x80)
    Sleep(200)

    label("loc_6791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_680D")
    OP_8E(0xFE, 0x59CE, 0x0, 0x9EE8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Sleep(600)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x59CE, 0x0, 0xD61A, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Jump("loc_6791")

    label("loc_680D")

    Return()

    # Function_37_6776 end

    def Function_38_680E(): pass

    label("Function_38_680E")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    Sleep(200)
    SetChrPos(0xFE, 31840, -1650, 57320, 0)
    ClearChrFlags(0xFE, 0x80)

    label("loc_6830")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6942")
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x75BC, 0xFFFFF894, 0xDE80, 0x9C4, 0x0)
    SetChrPos(0xFE, 30140, -1650, 56960, 270)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x7602, 0xFFFFF894, 0xC5DA, 0x9C4, 0x0)
    SetChrPos(0xFE, 30210, -1550, 50650, 180)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 225, 400)
    Sleep(800)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x80FC, 0xFFFFF894, 0xBE14, 0x9C4, 0x0)
    SetChrPos(0xFE, 33020, -1700, 48660, 135)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x7C60, 0xFFFFF894, 0xDFE8, 0x9C4, 0x0)
    SetChrPos(0xFE, 31840, -1650, 57320, 0)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(800)
    OP_8C(0xFE, 315, 400)
    Jump("loc_6830")

    label("loc_6942")

    Return()

    # Function_38_680E end

    def Function_39_6943(): pass

    label("Function_39_6943")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 33990, -1650, 34800, 135)
    ClearChrFlags(0xFE, 0x80)

    label("loc_6960")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A83")
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x78D2, 0xFFFFF894, 0x8746, 0x9C4, 0x0)
    SetChrPos(0xFE, 30930, -1650, 34630, 270)
    SetChrChipByIndex(0xFE, 23)
    Sleep(800)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x747C, 0xFFFFF894, 0xABD6, 0x9C4, 0x0)
    SetChrPos(0xFE, 29820, -1650, 43990, 0)
    SetChrChipByIndex(0xFE, 23)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x8552, 0xFFFFF894, 0xA83E, 0x9C4, 0x0)
    SetChrPos(0xFE, 34130, -1650, 43070, 90)
    SetChrChipByIndex(0xFE, 23)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x84C6, 0xFFFFF894, 0x87F0, 0x9C4, 0x0)
    SetChrPos(0xFE, 33990, -1650, 34800, 180)
    SetChrChipByIndex(0xFE, 23)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(800)
    OP_8C(0xFE, 135, 400)
    Jump("loc_6960")

    label("loc_6A83")

    Return()

    # Function_39_6943 end

    def Function_40_6A84(): pass

    label("Function_40_6A84")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 40320, -2000, 48550, 90)
    ClearChrFlags(0xFE, 0x80)
    Sleep(800)

    label("loc_6AA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BA1")
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x933A, 0xFFFFF830, 0xB860, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9038, 0xFFFFF830, 0xCEC2, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 45, 400)
    Sleep(800)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8C78, 0xFFFFF830, 0xDC50, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9A42, 0xFFFFF830, 0xD250, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9D80, 0xFFFFF830, 0xBDA6, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    Jump("loc_6AA6")

    label("loc_6BA1")

    Return()

    # Function_40_6A84 end

    def Function_41_6BA2(): pass

    label("Function_41_6BA2")

    OP_43(0xFE, 0x0, 0x0, 0x2)
    SetChrPos(0xFE, 36800, -2000, 41930, 315)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)

    label("loc_6BCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CD8")
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9B3C, 0xFFFFF830, 0xA78A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8E(0xFE, 0x99A2, 0xFFFFF830, 0x8E3A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    OP_8C(0xFE, 270, 400)
    Sleep(800)
    OP_8C(0xFE, 215, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8CA0, 0xFFFFF830, 0x875A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 90, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x9560, 0xFFFFF830, 0x85B6, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(800)
    OP_8C(0xFE, 180, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0x8FC0, 0xFFFFF830, 0xA3CA, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 25)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    Jump("loc_6BCE")

    label("loc_6CD8")

    Return()

    # Function_41_6BA2 end

    def Function_42_6CD9(): pass

    label("Function_42_6CD9")

    EventBegin(0x0)
    OP_6D(15700, 0, 45080, 0)
    OP_67(0, 11040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(132000, 0)
    OP_6E(446, 0)
    SetChrPos(0x102, 10480, 0, 580, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x26000D, 0x260012, 0x1F)
    SetChrChipByIndex(0x14, 31)
    SetChrChipByIndex(0x15, 31)
    SetChrChipByIndex(0x16, 31)
    SetChrChipByIndex(0x17, 31)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x16, 0x1, 0x0, 0x24)
    OP_43(0x17, 0x1, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x3E8)
    OP_DE("Jenis Royal Academy")
    FadeToBright(1000, 0)

    def lambda_6DF9():
        OP_6D(13720, 0, 10560, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DF9)

    def lambda_6E11():
        OP_67(0, 10100, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E11)

    def lambda_6E29():
        OP_6C(143000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6E29)

    def lambda_6E39():
        OP_6E(296, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6E39)

    def lambda_6E49():
        OP_6B(2570, 6000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6E49)
    Sleep(4500)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_8F(0x102, 0x2FF8, 0x0, 0x22A6, 0x1770, 0x0)
    OP_8C(0x102, 45, 400)
    SetChrChipByIndex(0x102, 30)
    SetChrSubChip(0x102, 1)
    WaitChrThread(0x102, 0x1)

    def lambda_6EB0():
        OP_6D(15230, 0, 13640, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EB0)

    def lambda_6EC8():
        OP_6C(179000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6EC8)
    SetChrSubChip(0x102, 1)
    Sleep(300)
    SetChrSubChip(0x102, 0)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0x102, 0x4)
    OP_7D(0x0, 0x102, 0x28, 0x1F4)
    OP_96(0x102, 0x35DE, 0xD48, 0x2C56, 0x1194, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0x102, 0x3C32, 0x0, 0x3610, 0x5DC, 0x1770)
    SetChrSubChip(0x102, 1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #205
        0x102,
        "#1035F...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_6F80():
        OP_6D(16090, 0, 24680, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F80)
    OP_8E(0x102, 0x3F48, 0x0, 0x5FC8, 0xBB8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    OP_8C(0x102, 45, 0)
    OP_0D()
    Sleep(1000)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    OP_43(0x14, 0x1, 0x0, 0x2B)
    OP_43(0x15, 0x1, 0x0, 0x2C)

    def lambda_6FE5():
        OP_6D(21840, 0, 27280, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6FE5)

    def lambda_6FFD():
        OP_6B(2910, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FFD)

    def lambda_700D():
        OP_6C(153000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_700D)
    OP_6E(301, 4000)
    Sleep(3000)
    Fade(500)
    OP_6D(16090, 0, 24680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(166000, 0)
    OP_6E(288, 0)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(    #206
        0x102,
        (
            "#1043F(I should use the buildings for cover,\x01",
            "and stay behind them to avoid being seen.)\x02\x03",

            "#1042F(I need to find where they're keeping\x01",
            "the hostages and try to get some kind\x01",
            "of headcount of the enemy...)\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    OP_8C(0x102, 180, 0)
    OP_0D()

    def lambda_7165():
        OP_6D(16500, 0, 21880, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7165)

    def lambda_717D():
        OP_6C(151000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_717D)
    OP_8E(0x102, 0x4060, 0x0, 0x5546, 0x7D0, 0x0)
    OP_8C(0x102, 90, 400)
    WaitChrThread(0x102, 0x1)

    def lambda_71AD():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71AD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_6CD9 end

    def Function_43_71D9(): pass

    label("Function_43_71D9")

    SetChrPos(0xFE, 20980, 0, 38990, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x51F4, 0x0, 0x6E00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81F6, 0x0, 0x6E00, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_71D9 end

    def Function_44_721D(): pass

    label("Function_44_721D")

    SetChrPos(0xFE, 30910, 0, 29060, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x59EC, 0x0, 0x7184, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59EC, 0x0, 0x9F56, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_44_721D end

    def Function_45_7261(): pass

    label("Function_45_7261")

    EventBegin(0x0)
    OP_6D(16500, 0, 21880, 0)
    OP_6C(151000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(288, 0)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #207
        0x102,
        (
            "#1035F(Two enemy soldiers in the boys' dorm...)\x02\x03",

            "#1040F(I need to check every building like this.)\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_45_7261 end

    def Function_46_7358(): pass

    label("Function_46_7358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_7495")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_73DF"),
        (1, "loc_7483"),
        (SWITCH_DEFAULT, "loc_7492"),
    )


    label("loc_73DF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7424")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_744F")

    label("loc_7424")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_744F")


    def lambda_7455():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7455)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_7492")

    label("loc_7483")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_7492")

    label("loc_7492")

    Jump("loc_753F")

    label("loc_7495")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74DA")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_750E")

    label("loc_74DA")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 21830, 90)
    OP_6D(16480, 0, 21830, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_750E")


    def lambda_7514():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7514)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_753F")

    TalkEnd(0xFF)
    Return()

    # Function_46_7358 end

    def Function_47_7543(): pass

    label("Function_47_7543")

    EventBegin(0x0)
    OP_6D(16480, 0, 21830, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_758D")
    OP_6C(150000, 0)
    Jump("loc_7596")

    label("loc_758D")

    OP_6C(30000, 0)

    label("loc_7596")

    SetChrPos(0x102, 16480, 0, 21830, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_7543 end

    def Function_48_75BD(): pass

    label("Function_48_75BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_END)), "loc_7700")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7644"),
        (1, "loc_76EE"),
        (SWITCH_DEFAULT, "loc_76FD"),
    )


    label("loc_7644")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7689")
    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_76BD")

    label("loc_7689")

    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_76BD")


    def lambda_76C3():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76C3)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2512   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_76EE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_76FD")

    label("loc_76FD")

    Jump("loc_77AA")

    label("loc_7700")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7745")
    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_7779")

    label("loc_7745")

    Fade(500)
    SetChrPos(0x102, 16490, 0, 16250, 90)
    OP_6D(16490, 0, 16250, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_7779")


    def lambda_777F():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_777F)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2512   ._SN", 107, 0, 0)
    IdleLoop()

    label("loc_77AA")

    TalkEnd(0xFF)
    Return()

    # Function_48_75BD end

    def Function_49_77AE(): pass

    label("Function_49_77AE")

    EventBegin(0x0)
    OP_6D(16490, 0, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77F8")
    OP_6C(150000, 0)
    Jump("loc_7801")

    label("loc_77F8")

    OP_6C(30000, 0)

    label("loc_7801")

    SetChrPos(0x102, 16490, 0, 16250, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78EC")
    Sleep(500)

    ChrTalk(    #208
        0x102,
        (
            "#1043F(Two male students and an injured faculty\x01",
            "member... Looks like he was shot.)\x02\x03",

            "#1040F(His injury doesn't seem\x01",
            "life-threatening, though.)\x02\x03",

            "(Thank Aidios for little mercies, I guess.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2014)

    label("loc_78EC")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_49_77AE end

    def Function_50_78F8(): pass

    label("Function_50_78F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7905")
    Return()

    label("loc_7905")

    EventBegin(0x1)
    Fade(500)
    OP_6D(16410, 0, 23210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_8E(0x102, 0x4056, 0x0, 0x604A, 0x7D0, 0x0)
    OP_8C(0x102, 45, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #209
        0x102,
        (
            "#1042F(There's someone patrolling in\x01",
            "the front. I should go behind.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(15550, 0, 23560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 15550, 0, 23560, 180)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_50_78F8 end

    def Function_51_7A1A(): pass

    label("Function_51_7A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A27")
    Return()

    label("loc_7A27")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B5A")

    def lambda_7A37():
        OP_6D(35520, 0, 12770, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A37)

    def lambda_7A4F():
        OP_6B(2910, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A4F)

    def lambda_7A5F():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7A5F)
    OP_6E(310, 3000)
    Sleep(1000)
    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 26720, 0, 12520, 45)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    OP_0D()
    Sleep(250)

    ChrTalk(    #210
        0x102,
        "#1042F(...No choice. I'll have to dash across.)\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x102, 90, 400)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(250)
    Jump("loc_7BE1")

    label("loc_7B5A")

    Fade(500)
    OP_6D(26720, 0, 12520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(237000, 0)
    OP_6E(502, 0)
    SetChrPos(0x102, 26720, 0, 12520, 90)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(250)

    label("loc_7BE1")

    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x99, 0x0, 0x64)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 31)
    SetChrSubChip(0x102, 0)

    def lambda_7C27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C27)

    def lambda_7C39():
        OP_8E(0xFE, 0xCE5E, 0x0, 0x3282, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C39)

    def lambda_7C54():
        OP_99(0xFE, 0x3, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7C54)

    def lambda_7C64():
        OP_6C(225000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_7C64)

    def lambda_7C74():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7C74)
    OP_6D(34000, 0, 12820, 300)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x3)
    SetChrFlags(0x102, 0x80)
    Fade(500)
    OP_6D(50030, 0, 12990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 49830, 4000, 12930, 90)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_7D36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7D36)
    SetChrFlags(0x102, 0x4)

    def lambda_7D4D():
        OP_8F(0xFE, 0xC36E, 0x0, 0x32BE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D4D)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    OP_D3(0x1D)
    OP_A2(0x2015)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_51_7A1A end

    def Function_52_7DD4(): pass

    label("Function_52_7DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DE1")
    Return()

    label("loc_7DE1")

    EventBegin(0x0)
    Fade(500)
    OP_6D(48840, 0, 12980, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(135000, 0)
    OP_6E(502, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrPos(0x102, 48840, 0, 12980, 270)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x99, 0x0, 0x64)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 31)

    def lambda_7EB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7EB9)

    def lambda_7ECB():
        OP_8E(0xFE, 0x619E, 0x0, 0x30E8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7ECB)

    def lambda_7EE6():
        OP_6C(150000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_7EE6)

    def lambda_7EF6():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7EF6)
    OP_6D(41000, 0, 12960, 300)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x3)
    SetChrFlags(0x102, 0x80)
    Fade(500)
    OP_6D(24400, 0, 12550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 24400, 4000, 12550, 270)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_7FB3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7FB3)
    SetChrFlags(0x102, 0x4)

    def lambda_7FCA():
        OP_8F(0xFE, 0x5F50, 0x0, 0x3106, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FCA)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    WaitChrThread(0x102, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_52_7DD4 end

    def Function_53_804E(): pass

    label("Function_53_804E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_END)), "loc_8191")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_80D5"),
        (1, "loc_817F"),
        (SWITCH_DEFAULT, "loc_818E"),
    )


    label("loc_80D5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811A")
    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_814E")

    label("loc_811A")

    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_814E")


    def lambda_8154():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8154)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_817F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_818E")

    label("loc_818E")

    Jump("loc_823B")

    label("loc_8191")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81D6")
    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(285000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_820A")

    label("loc_81D6")

    Fade(500)
    SetChrPos(0x102, 56980, 0, 13500, 0)
    OP_6D(56980, 0, 13500, 0)
    OP_6C(75000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_820A")


    def lambda_8210():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8210)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_823B")

    TalkEnd(0xFF)
    Return()

    # Function_53_804E end

    def Function_54_823F(): pass

    label("Function_54_823F")

    EventBegin(0x0)
    OP_6D(56980, 0, 13500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8289")
    OP_6C(285000, 0)
    Jump("loc_8292")

    label("loc_8289")

    OP_6C(75000, 0)

    label("loc_8292")

    SetChrPos(0x102, 56980, 0, 13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8360")
    Sleep(500)

    ChrTalk(    #211
        0x102,
        (
            "#1043F(Four soldiers...)\x02\x03",

            "(Looks like they're being kept in reserve\x01",
            "in case something happens.)\x02\x03",

            "#1042F(They may be keeping the hostages\x01",
            "on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2016)

    label("loc_8360")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_54_823F end

    def Function_55_836C(): pass

    label("Function_55_836C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8379")
    Return()

    label("loc_8379")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x18, 38350, 350, 27790, 315)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_6C(270000, 0)
    OP_8C(0x102, 270, 0)
    OP_69(0x102, 0x0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_83E1():
        OP_6D(36580, 0, 27680, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83E1)

    def lambda_83F9():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_83F9)

    def lambda_8411():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8411)

    def lambda_8421():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8421)

    def lambda_8431():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_8431)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6F36), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8474")
    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x7ADA, 0x1388, 0x0)
    Jump("loc_849C")

    label("loc_8474")

    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x6392, 0x1388, 0x0)

    label("loc_849C")

    OP_8C(0x102, 90, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_69(0x102, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x18, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #212
        0x102,
        (
            "#1042F(There's someone patrolling in\x01",
            "the front. I should go behind.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_55_836C end

    def Function_56_854C(): pass

    label("Function_56_854C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8559")
    Return()

    label("loc_8559")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x18, 36310, 350, 64080, 225)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 23)
    SetChrSubChip(0x18, 0)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_6C(270000, 0)
    OP_8C(0x102, 270, 0)
    OP_69(0x102, 0x0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_85C1():
        OP_6D(34720, 0, 63840, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_85C1)

    def lambda_85D9():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85D9)

    def lambda_85F1():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_85F1)

    def lambda_8601():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8601)

    def lambda_8611():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_8611)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF816), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8654")
    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0x1040A, 0x1388, 0x0)
    Jump("loc_867C")

    label("loc_8654")

    OP_90(0x102, 0x258, 0x0, 0x0, 0x1388, 0x0)
    OP_8E(0x102, 0xD67E, 0x0, 0xEC22, 0x1388, 0x0)

    label("loc_867C")

    OP_8C(0x102, 90, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_69(0x102, 0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x18, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x102,
        (
            "#1042F(There's someone patrolling in\x01",
            "the front. I should go behind.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_56_854C end

    def Function_57_872C(): pass

    label("Function_57_872C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87A4")
    EventBegin(0x0)
    OP_A2(0x2018)
    OP_28(0xC0, 0x1, 0x2)
    Fade(500)
    SetChrPos(0x102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_8776():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8776)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2510   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_87EE")

    label("loc_87A4")


    ChrTalk(    #214
        0x102,
        (
            "#1043F(They're still talking.)\x02\x03",

            "#1042F(I should check elsewhere.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_87EE")

    Return()

    # Function_57_872C end

    def Function_58_87EF(): pass

    label("Function_58_87EF")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 36000, 270)
    OP_6D(58500, 0, 36000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #215
        0x102,
        (
            "#1035F(So he's the one behind all this...)\x02\x03",

            "#1043F(It makes sense, in hindsight.\x01",
            "He's an alumnus of the school and\x01",
            "is familiar with the layout...)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_58_87EF end

    def Function_59_88F2(): pass

    label("Function_59_88F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_END)), "loc_89ED")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8979"),
        (1, "loc_89DB"),
        (SWITCH_DEFAULT, "loc_89EA"),
    )


    label("loc_8979")

    Fade(500)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_89B0():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89B0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2510   ._SN", 113, 0, 0)
    IdleLoop()

    label("loc_89DB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_89EA")

    label("loc_89EA")

    Jump("loc_8A4F")

    label("loc_89ED")

    Fade(500)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_6C(285000, 0)
    OP_0D()

    def lambda_8A24():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A24)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2510   ._SN", 113, 0, 0)
    IdleLoop()

    label("loc_8A4F")

    TalkEnd(0xFF)
    Return()

    # Function_59_88F2 end

    def Function_60_8A53(): pass

    label("Function_60_8A53")

    EventBegin(0x0)
    SetChrPos(0x102, 58510, 0, 40110, 270)
    OP_6D(58510, 0, 40110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(285000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B20")
    Sleep(500)

    ChrTalk(    #216
        0x102,
        (
            "#1043F(I don't see any of the teachers...)\x02\x03",

            "#1035F(They're most likely being held elsewhere.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2019)

    label("loc_8B20")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_60_8A53 end

    def Function_61_8B2C(): pass

    label("Function_61_8B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_END)), "loc_8C6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8BB3"),
        (1, "loc_8C5D"),
        (SWITCH_DEFAULT, "loc_8C6C"),
    )


    label("loc_8BB3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF8")
    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_8C2C")

    label("loc_8BF8")

    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_8C2C")


    def lambda_8C32():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C32)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_8C5D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_8C6C")

    label("loc_8C6C")

    Jump("loc_8D19")

    label("loc_8C6F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CB4")
    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(315000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_8CE8")

    label("loc_8CB4")

    Fade(500)
    SetChrPos(0x102, 59500, 0, 46040, 270)
    OP_6D(59500, 0, 46040, 0)
    OP_6C(225000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_8CE8")


    def lambda_8CEE():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CEE)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_8D19")

    TalkEnd(0xFF)
    Return()

    # Function_61_8B2C end

    def Function_62_8D1D(): pass

    label("Function_62_8D1D")

    EventBegin(0x0)
    OP_6D(59500, 0, 46040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D67")
    OP_6C(315000, 0)
    Jump("loc_8D70")

    label("loc_8D67")

    OP_6C(225000, 0)

    label("loc_8D70")

    SetChrPos(0x102, 59500, 0, 46040, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E16")
    Sleep(500)

    ChrTalk(    #217
        0x102,
        (
            "#1042F(There's a sharp angle, so I can't tell,\x01",
            "but I hear someone in the hallway...)\x02\x03",

            "(Most likely a guard on watch.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201A)

    label("loc_8E16")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_62_8D1D end

    def Function_63_8E22(): pass

    label("Function_63_8E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EAC")
    EventBegin(0x0)
    OP_A2(0x201B)
    Fade(500)
    OP_6D(58500, 0, 51970, 0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6C(225000, 0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x102,
        "#1044F(Ah!)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_8F21")

    label("loc_8EAC")


    ChrTalk(    #219
        0x102,
        (
            "#1043F(I shouldn't spend too much time\x01",
            "talking or the guard might notice.)\x02\x03",

            "#1042F(Time to check elsewhere.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_8F21")

    Return()

    # Function_63_8E22 end

    def Function_64_8F22(): pass

    label("Function_64_8F22")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(    #220
        0x102,
        (
            "#1040F#6P(Quiet, Hans.)\x02\x03",

            "(Don't be too loud or the\x01",
            "guard will notice.)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(352, 0, -1, -1)
    SetChrName("Hans")

    AnonymousTalk(    #221
        (
            "\x07\x00#732F(R-R-Right...)\x02\x03",

            "#734F(But, c'mon...)\x02\x03",

            "(How am I not supposed to lose it when\x01",
            "you come out of the blue like that?)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #222
        0x102,
        "#1054F#6P(Haha, sorry.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_64_8F22 end

    def Function_65_9083(): pass

    label("Function_65_9083")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetMessageWindowPos(360, 50, -1, -1)
    SetChrName("Hans")

    AnonymousTalk(    #223
        "\x07\x00#734F(I knew you were gonna shout...)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 0, -1, -1)
    SetChrName("Jill")

    AnonymousTalk(    #224
        (
            "#645F(Excuse me for being thrilled!)\x02\x03",

            "#644F(Joshua, you impossible dummy!\x01",
            "What the heck are YOU doing here?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #225
        0x102,
        (
            "#1040F#6P(It's good to see you, Jill.)\x02\x03",

            "#1035F(I don't have much time, so\x01",
            "let me explain very quickly...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #226
        (
            "\x07\x05Joshua explained how the group found out about the takeover\x01",
            "from Mickey and what they were going to do about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_65_9083 end

    def Function_66_92BA(): pass

    label("Function_66_92BA")

    EventBegin(0x0)
    SetChrPos(0x102, 58500, 0, 51970, 270)
    OP_6D(58500, 0, 51970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_66_92BA end

    def Function_67_9320(): pass

    label("Function_67_9320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_END)), "loc_9463")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_93A7"),
        (1, "loc_9451"),
        (SWITCH_DEFAULT, "loc_9460"),
    )


    label("loc_93A7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_93EC")
    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_9420")

    label("loc_93EC")

    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_9420")


    def lambda_9426():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9426)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_9451")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9460")

    label("loc_9460")

    Jump("loc_950D")

    label("loc_9463")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_94A8")
    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(105000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_94DC")

    label("loc_94A8")

    Fade(500)
    SetChrPos(0x102, 48830, 0, 80500, 180)
    OP_6D(48830, 0, 80500, 0)
    OP_6C(255000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_94DC")


    def lambda_94E2():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94E2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_950D")

    TalkEnd(0xFF)
    Return()

    # Function_67_9320 end

    def Function_68_9511(): pass

    label("Function_68_9511")

    EventBegin(0x0)
    OP_6D(48830, 0, 80500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_955B")
    OP_6C(105000, 0)
    Jump("loc_9564")

    label("loc_955B")

    OP_6C(255000, 0)

    label("loc_9564")

    SetChrPos(0x102, 48830, 0, 80500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95EF")
    Sleep(500)

    ChrTalk(    #227
        0x102,
        (
            "#1040F(I don't hear anyone in the waiting room...)\x02\x03",

            "(I think it's safe to say it's empty.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201C)

    label("loc_95EF")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_68_9511 end

    def Function_69_95FB(): pass

    label("Function_69_95FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9608")
    Return()

    label("loc_9608")

    EventBegin(0x0)
    Fade(500)
    OP_6D(43190, 0, 81780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(45000, 0)
    OP_6E(499, 0)
    SetChrPos(0x102, 43040, 0, 81120, 270)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x99, 0x0, 0x64)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 31)
    SetChrSubChip(0x102, 0)

    def lambda_96D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96D7)

    def lambda_96E9():
        OP_8E(0xFE, 0x6450, 0x0, 0x13C40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96E9)

    def lambda_9704():
        OP_99(0xFE, 0x3, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9704)

    def lambda_9714():
        OP_6C(30000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_9714)

    def lambda_9724():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9724)
    OP_6D(36000, 0, 81030, 300)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x3)
    SetChrFlags(0x102, 0x80)
    Fade(500)
    OP_6D(25160, 0, 80940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 25160, 4000, 80940, 270)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_97E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97E1)
    SetChrFlags(0x102, 0x4)

    def lambda_97F8():
        OP_8F(0xFE, 0x6248, 0x0, 0x13C2C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97F8)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x102, 0x2)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_69_95FB end

    def Function_70_987C(): pass

    label("Function_70_987C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9889")
    Return()

    label("loc_9889")

    EventBegin(0x0)
    Fade(500)
    OP_6D(26220, 0, 80980, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(1620, 0)
    OP_6C(312000, 0)
    OP_6E(499, 0)
    SetChrPos(0x102, 26220, 0, 80980, 90)
    OP_D2(0x270019, 0x27001D, 0x1D)
    OP_D2(0x2600FC, 0x260101, 0x1E)
    OP_D2(0x270011, 0x270015, 0x1F)
    OP_0D()
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    Fade(250)
    SetChrChipByIndex(0x102, 29)
    SetChrSubChip(0x102, 0)
    OP_0D()
    Sleep(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x99, 0x0, 0x64)
    OP_7D(0x0, 0x102, 0x78, 0xFA0)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 31)
    SetChrSubChip(0x102, 0)

    def lambda_9958():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9958)

    def lambda_996A():
        OP_8E(0xFE, 0xA83E, 0x0, 0x13C4A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_996A)

    def lambda_9985():
        OP_99(0xFE, 0x3, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9985)

    def lambda_9995():
        OP_6C(330000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_9995)

    def lambda_99A5():
        OP_67(0, 6300, -10000, 300)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_99A5)
    OP_6D(34000, 0, 80920, 300)
    WaitChrThread(0x102, 0x2)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x3)
    SetChrFlags(0x102, 0x80)
    Fade(500)
    OP_6D(44120, 0, 80990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_7D(0x0, 0x102, 0x28, 0x3E8)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x1000)
    SetChrPos(0x102, 44120, 4000, 80990, 90)
    SetChrChipByIndex(0x102, 30)
    SetChrFlags(0x102, 0x20)
    SetChrSubChip(0x102, 1)

    def lambda_9A62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A62)
    SetChrFlags(0x102, 0x4)

    def lambda_9A79():
        OP_8F(0xFE, 0xAC58, 0x0, 0x13C5E, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A79)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x0, 0xFF, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x102, 0x2)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    Sleep(500)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x1000)
    OP_D3(0x1D)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_70_987C end

    def Function_71_9AFD(): pass

    label("Function_71_9AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_END)), "loc_9C40")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B84"),
        (1, "loc_9C2E"),
        (SWITCH_DEFAULT, "loc_9C3D"),
    )


    label("loc_9B84")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BC9")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_9BFD")

    label("loc_9BC9")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_9BFD")


    def lambda_9C03():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C03)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2512   ._SN", 116, 0, 0)
    IdleLoop()

    label("loc_9C2E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9C3D")

    label("loc_9C3D")

    Jump("loc_9CEA")

    label("loc_9C40")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C85")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_9CB9")

    label("loc_9C85")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 76930, 90)
    OP_6D(16480, 0, 76930, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_9CB9")


    def lambda_9CBF():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9CBF)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2512   ._SN", 116, 0, 0)
    IdleLoop()

    label("loc_9CEA")

    TalkEnd(0xFF)
    Return()

    # Function_71_9AFD end

    def Function_72_9CEE(): pass

    label("Function_72_9CEE")

    EventBegin(0x0)
    OP_6D(16480, 0, 76930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D38")
    OP_6C(150000, 0)
    Jump("loc_9D41")

    label("loc_9D38")

    OP_6C(30000, 0)

    label("loc_9D41")

    SetChrPos(0x102, 16480, 0, 76930, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DBD")
    Sleep(500)

    ChrTalk(    #228
        0x102,
        (
            "#1043F(Three girls...)\x02\x03",

            "#1042F(The others must be in the\x01",
            "main schoolhouse.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201D)

    label("loc_9DBD")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_72_9CEE end

    def Function_73_9DC9(): pass

    label("Function_73_9DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_END)), "loc_9F0C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_57(0xC8, 0x14, 0xC, "#5CLook inside again?")
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "[Yes]")
    OP_CC(0x1, 0x0, "[No]")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_DA()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E50"),
        (1, "loc_9EFA"),
        (SWITCH_DEFAULT, "loc_9F09"),
    )


    label("loc_9E50")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E95")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_9EC9")

    label("loc_9E95")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_9EC9")


    def lambda_9ECF():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ECF)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2512   ._SN", 109, 0, 0)
    IdleLoop()

    label("loc_9EFA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9F09")

    label("loc_9F09")

    Jump("loc_9FB6")

    label("loc_9F0C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F51")
    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(150000, 0)
    OP_A3(0x2030)
    OP_0D()
    Jump("loc_9F85")

    label("loc_9F51")

    Fade(500)
    SetChrPos(0x102, 16480, 0, 71110, 90)
    OP_6D(16480, 0, 71110, 0)
    OP_6C(30000, 0)
    OP_A2(0x2030)
    OP_0D()

    label("loc_9F85")


    def lambda_9F8B():
        OP_6E(241, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F8B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2512   ._SN", 109, 0, 0)
    IdleLoop()

    label("loc_9FB6")

    TalkEnd(0xFF)
    Return()

    # Function_73_9DC9 end

    def Function_74_9FBA(): pass

    label("Function_74_9FBA")

    EventBegin(0x0)
    OP_6D(16480, 0, 71110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A004")
    OP_6C(150000, 0)
    Jump("loc_A00D")

    label("loc_A004")

    OP_6C(30000, 0)

    label("loc_A00D")

    SetChrPos(0x102, 16480, 0, 71110, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09E")
    Sleep(500)

    ChrTalk(    #229
        0x102,
        (
            "#1042F(Two enemy soldiers on watch...)\x02\x03",

            "#1035F(I don't hear anything from\x01",
            "the other club rooms.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x201E)

    label("loc_A09E")

    Call(0, 76)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_74_9FBA end

    def Function_75_A0AA(): pass

    label("Function_75_A0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0B7")
    Return()

    label("loc_A0B7")

    EventBegin(0x1)
    Fade(500)
    OP_6D(16260, 0, 70080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8E(0x102, 0x406A, 0x0, 0x10B6C, 0x7D0, 0x0)
    OP_8C(0x102, 135, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #230
        0x102,
        (
            "#1042F(There's someone patrolling in\x01",
            "the front. I should go behind.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(15560, 0, 69700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 15560, 0, 69700, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_75_A0AA end

    def Function_76_A1CC(): pass

    label("Function_76_A1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E3")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as checked all buildings, and unlocked back gate\x01",                        # 0
            "Set as have not checked all buildings, and have not unlocked back gate\x01",      # 1
            "No change\x01",                                                                   # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A2A1"),
        (1, "loc_A2C2"),
        (SWITCH_DEFAULT, "loc_A2E3"),
    )


    label("loc_A2A1")

    OP_A2(0x2017)
    OP_A2(0x2014)
    OP_A2(0x2016)
    OP_A2(0x2018)
    OP_A2(0x2019)
    OP_A2(0x201A)
    OP_A2(0x201B)
    OP_A2(0x201C)
    OP_A2(0x201D)
    OP_A2(0x201E)
    Jump("loc_A2E3")

    label("loc_A2C2")

    OP_A3(0x2017)
    OP_A3(0x2014)
    OP_A3(0x2016)
    OP_A3(0x2018)
    OP_A3(0x2019)
    OP_A3(0x201A)
    OP_A3(0x201B)
    OP_A3(0x201C)
    OP_A3(0x201D)
    OP_A3(0x201E)
    Jump("loc_A2E3")

    label("loc_A2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A402")
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #231
        0x102,
        (
            "#1035F(All right, I've scouted the entire campus.)\x02\x03",

            "#1042F(With so few men, I could probably...)\x02\x03",

            "(...)\x02\x03",

            "#1043F(No... It's still not time for that.)\x02\x03",

            "(I should get back to the others.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_A402")

    Return()

    # Function_76_A1CC end

    def Function_77_A403(): pass

    label("Function_77_A403")

    EventBegin(0x0)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    SetChrPos(0x16, 21540, 0, 46950, 180)
    SetChrPos(0x17, 21540, 0, 45600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_6D(53310, 0, 46050, 0)
    OP_67(0, 8390, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(90000, 0)
    OP_6E(375, 0)

    def lambda_A4FD():
        OP_6D(23270, 0, 46150, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A4FD)

    def lambda_A515():
        OP_67(0, 7570, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A515)

    def lambda_A52D():
        OP_6B(3220, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_A52D)

    def lambda_A53D():
        OP_6E(345, 6000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A53D)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    Fade(1000)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #232
        0x16,
        (
            "#6PThe hell is Gilbert thinking, anyway?\x02\x03",

            "All we get from taking over a place like\x01",
            "this is freaking out a bunch'a rich kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x17,
        (
            "#2PYeah, if we really wanted to stir up some\x01",
            "chaos, we'd attack one of the little rat\x01",
            "holes these hicks call villages.\x02\x03",

            "It's like you said, though, man.\x01",
            "The brats here are LOADED.\x02\x03",

            "Rumor even has it that a member of the\x01",
            "Liberlian royal family attends this joint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x16,
        "#6PWhat, like that Klaudia chick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x17,
        (
            "#2PHaha, nah, no way.\x01",
            "She's, like, in the palace or some shit.\x02\x03",

            "Whoever it is, though, the Phantom\x01",
            "Thief's friggin' OBSESSED with the\x01",
            "chick who goes to this joint.\x02\x03",

            "That's Gilbert's game plan--find out\x01",
            "who it is, and deliver her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x16,
        (
            "#6PI get it... Yeah, we could score some major\x01",
            "points with an Enforcer if we do that.\x02\x03",

            "But man, that just makes things even worse.\x01",
            "If the chick is that important, the bracers\x01",
            "and army are gonna come right at us.\x02\x03",

            "We better be ready for some\x01",
            "major shit to go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x17,
        (
            "#2PPssh, don't worry.\x01",
            "We JUST hit this place, it'll take\x01",
            "'em a while to figure it out.\x02\x03",

            "Besides, their orbal-based guns ain't\x01",
            "gonna work, unlike ours, remember?\x02\x03",

            "Gonna be like a shootin' range\x01",
            "if they take us on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x16,
        "#6PHeh, yeah, good point.\x02",
    )

    CloseMessageWindow()
    OP_22(0x235, 0x0, 0x3C)
    Sleep(600)
    OP_22(0x235, 0x0, 0x46)
    OP_20(0x7D0)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    OP_22(0x235, 0x0, 0x50)
    Sleep(400)

    def lambda_AAA0():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AAA0)
    Sleep(50)

    def lambda_AAB3():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_AAB3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/R2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_77_A403 end

    def Function_78_AAD3(): pass

    label("Function_78_AAD3")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x26000D, 0x260012, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrChipByIndex(0x14, 32)
    SetChrChipByIndex(0x15, 32)
    SetChrChipByIndex(0x16, 32)
    SetChrChipByIndex(0x17, 32)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x23)
    OP_43(0x18, 0x1, 0x0, 0x26)
    OP_43(0x19, 0x1, 0x0, 0x27)
    OP_43(0x1A, 0x1, 0x0, 0x28)
    OP_43(0x1B, 0x1, 0x0, 0x29)
    SetChrPos(0x16, 21540, 0, 46950, 270)
    SetChrPos(0x17, 21540, 0, 45600, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_6F(0x21, 0)
    OP_72(0x21, 0x10)
    OP_6D(22660, 0, 46750, 0)
    OP_67(0, 7180, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    OP_43(0x16, 0x2, 0x0, 0x4F)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #239
        0x16,
        (
            "#5PSHIT! POWDER GUNS?!\x01",
            "The hell they'd get that junk from?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x17,
        (
            "#2PThey'll bury us in bullets at this rate...\x01",
            "Go get the friggin' reserve guys!\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_78_AAD3 end

    def Function_79_ACB0(): pass

    label("Function_79_ACB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD04")
    OP_22(0x235, 0x0, 0x50)
    Sleep(1500)
    OP_23(0x235)
    Sleep(500)
    OP_22(0x235, 0x0, 0x50)
    Sleep(1900)
    OP_23(0x235)
    Sleep(700)
    OP_22(0x235, 0x0, 0x50)
    Sleep(1700)
    OP_23(0x235)
    Sleep(600)
    OP_22(0x235, 0x0, 0x50)
    Sleep(2000)
    OP_23(0x235)
    Sleep(800)
    Jump("Function_79_ACB0")

    label("loc_AD04")

    Return()

    # Function_79_ACB0 end

    def Function_80_AD05(): pass

    label("Function_80_AD05")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 67000, 0, 28000, 270)
    SetChrPos(0x102, 69060, 0, 28020, 270)
    SetChrPos(0x10A, 68950, 0, 27000, 315)
    SetChrPos(0x10E, 68850, 0, 29110, 225)
    OP_6D(65590, 0, 28000, 0)
    OP_67(0, 7570, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_70(0x22, 0x3C)
    OP_73(0x22)
    Sleep(1000)
    OP_A2(0x2020)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_80_AD05 end

    def Function_81_ADAC(): pass

    label("Function_81_ADAC")

    EventBegin(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_ADD6"),
        (102, "loc_AE94"),
        (103, "loc_AF52"),
        (105, "loc_B010"),
        (106, "loc_B0CE"),
        (107, "loc_B18C"),
        (108, "loc_B24A"),
        (109, "loc_B308"),
        (SWITCH_DEFAULT, "loc_B3C6"),
    )


    label("loc_ADD6")

    OP_6D(21430, 250, 67190, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 35940, -2000, 50640, 0)
    SetChrPos(0x101, 21590, 250, 66630, 180)
    SetChrPos(0x102, 22830, 250, 66650, 180)
    SetChrPos(0x10A, 21570, 500, 67710, 180)
    SetChrPos(0x10E, 22630, 500, 67660, 180)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #241
        0x14,
        "Girl's Voice",
        "#2PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_AE94")

    OP_6D(22360, 250, 25500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(144000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 40130, 250, 27260, 0)
    SetChrPos(0x101, 22590, 250, 26500, 0)
    SetChrPos(0x102, 21540, 250, 26340, 0)
    SetChrPos(0x10A, 22540, 500, 25460, 0)
    SetChrPos(0x10E, 21540, 500, 25390, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #242
        0x14,
        "Girl's Voice",
        "#4PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_AF52")

    OP_6D(41330, 440, 73990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 48840, 0, 54680, 0)
    SetChrPos(0x101, 40760, 250, 73540, 270)
    SetChrPos(0x102, 40820, 250, 74500, 270)
    SetChrPos(0x10A, 41510, 500, 73600, 270)
    SetChrPos(0x10E, 41580, 500, 74500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #243
        0x14,
        "Girl's Voice",
        "#3PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B010")

    OP_6D(49030, 0, 45120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 47790, 250, 46520, 270)
    SetChrPos(0x102, 47710, 250, 45530, 270)
    SetChrPos(0x10A, 48800, 500, 46520, 270)
    SetChrPos(0x10E, 48670, 500, 45520, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #244
        0x14,
        "Girl's Voice",
        "#3PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B0CE")

    OP_6D(52890, 0, 62050, 0)
    OP_67(0, 8870, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(99000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51310, 0, 62270, 315)
    SetChrPos(0x102, 52320, 0, 62850, 315)
    SetChrPos(0x10A, 52190, 0, 61540, 315)
    SetChrPos(0x10E, 53310, 0, 61990, 315)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #245
        0x14,
        "Girl's Voice",
        "#3PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B18C")

    OP_6D(52540, 0, 29710, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(86000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51230, 0, 29590, 225)
    SetChrPos(0x102, 52250, 0, 29160, 225)
    SetChrPos(0x10A, 51900, 0, 30380, 225)
    SetChrPos(0x10E, 52990, 0, 29970, 225)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #246
        0x14,
        "Girl's Voice",
        "#3PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B24A")

    OP_6D(47860, 0, 19530, 0)
    OP_67(0, 9580, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 46810, 250, 19550, 270)
    SetChrPos(0x102, 46800, 250, 18440, 270)
    SetChrPos(0x10A, 47820, 500, 19500, 270)
    SetChrPos(0x10E, 47810, 500, 18470, 270)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #247
        0x14,
        "Girl's Voice",
        "#6PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B308")

    OP_6D(52820, 0, 26990, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(105000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 65770, 0, 27850, 0)
    SetChrPos(0x101, 51270, 0, 27310, 315)
    SetChrPos(0x102, 52020, 0, 27920, 315)
    SetChrPos(0x10A, 52120, 0, 26600, 315)
    SetChrPos(0x10E, 53070, 0, 27160, 315)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #248
        0x14,
        "Girl's Voice",
        "#4PNOOOOOOOO!\x02",
    )

    Jump("loc_B3C6")

    label("loc_B3C6")

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_B43D():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B43D)
    Sleep(50)

    def lambda_B450():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B450)
    Sleep(50)

    def lambda_B463():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B463)
    Sleep(50)

    def lambda_B476():
        TurnDirection(0xFE, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_B476)
    Sleep(500)

    ChrTalk(    #249
        0x101,
        "#1020FThat voice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        "#1042FIt's that way--behind the academy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x10E,
        (
            "#842FThere is one person left on\x01",
            "the list. It must be her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x10A,
        "#815FLet's hurry!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x202E)
    OP_28(0xC0, 0x1, 0x4000)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_81_ADAC end

    def Function_82_B530(): pass

    label("Function_82_B530")

    EventBegin(0x0)
    OP_20(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5A9")
    Call(0, 83)
    Call(0, 84)
    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B568")
    OP_A2(0x2031)

    label("loc_B568")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B578")
    OP_A2(0x2032)

    label("loc_B578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B588")
    OP_A2(0x2033)

    label("loc_B588")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B598")
    OP_A2(0x2034)

    label("loc_B598")

    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    AddParty(0x9, 0xF8, 0xFF)
    AddParty(0xD, 0xF9, 0xFF)

    label("loc_B5A9")

    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    OP_D2(0x260049, 0x26004E, 0x1D)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x101, 3)
    SetChrPos(0x101, 20370, 0, 45200, 270)
    SetChrPos(0x102, 20600, 0, 46260, 270)
    SetChrPos(0x107, 21330, 0, 45740, 270)
    SetChrPos(0x103, 21830, 0, 46650, 270)
    SetChrPos(0x106, 21700, 0, 44370, 270)
    SetChrPos(0x108, 22800, 0, 45100, 270)
    SetChrPos(0x10A, 18520, 0, 45400, 90)
    SetChrPos(0x1F, 17170, 0, 46730, 90)
    SetChrPos(0x1E, 17290, 0, 45450, 90)
    SetChrPos(0x10E, 18420, 0, 46630, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(12000, 0, 46000, 0)
    OP_67(0, 7050, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(90000, 0)
    OP_6E(469, 0)
    OP_1D(0xE)

    def lambda_B6D0():
        OP_6D(21530, 0, 46000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B6D0)

    def lambda_B6E8():
        OP_67(0, 8310, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6E8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(18910, 0, 46630, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(315000, 0)
    OP_6E(397, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #253
        0x101,
        (
            "#2P#1012FKurt, Anelace, everyone.\x02\x03",

            "#1006FThank you so much for helping\x01",
            "us out here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x10A,
        "#811F#3PAww, c'mon! Don't be so stuffy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x10E,
        (
            "#841F#6PIndeed. It was part of the duty\x01",
            "we share as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x1E,
        (
            "#835F#3PAs far as I'm concerned,\x01",
            "we were just paying you back\x01",
            "for the save in that lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x1F,
        (
            "#821F#3PIf anything comes up, we'll\x01",
            "be glad to help again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x103,
        "#021FWe'll be counting on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x102,
        (
            "#1040FWhere were you planning\x01",
            "on going after this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10E,
        (
            "#840F#6PWe're heading to Bose through\x01",
            "the Krone Pass.\x02\x03",

            "We intend to patrol the pass to\x01",
            "help ensure something like this\x01",
            "doesn't happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x108,
        "#070FA good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x107,
        "#560F#2PUm... Please be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x1F,
        "#825F#3PHaha! You too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x1E,
        (
            "#831F#3PAs long as this mess keeps up,\x01",
            "all we can do is pound the ground\x01",
            "and try to keep people safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x106,
        "#051F#2PDarn straight.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #266
        0x10A,
        "#814F#3PYeah... Hey, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#2P#1011FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x10A,
        (
            "#816F#3PI kinda noticed something when\x01",
            "we were fighting together...\x02\x03",

            "The way you used to hesitate when\x01",
            "you attacked? It's, like, totally gone.\x01",
            "You're SO more at ease now!\x02\x03",

            "#811FI know that's sorta out of the blue,\x01",
            "but it kinda blew me away how\x01",
            "much better you've gotten!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#2P#1016FAh, h-hey. C'mon, knock off the flattery.\x02\x03",

            "#1008FBesides, it's not like you aren't\x01",
            "loads better too, Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x10A,
        (
            "#1314F#3PWell, yeah, I've been up to\x01",
            "my ears in fights lately.\x02\x03",

            "#817FI don't just mean that, though.\x01",
            "It's like...you've gotten stronger\x01",
            "somewhere deep inside.\x02\x03",

            "I gotta think it's because you found\x01",
            "that path you were looking for in\x01",
            "your journey to find Joshua.\x02\x03",

            "#816FYou've really become strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#2P#1017FAnelace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x10A,
        (
            "#819F#3PHeehee, just means I better step\x01",
            "up my game as your rival, huh?\x02\x03",

            "#1310FIf we get the chance, let's fight\x01",
            "together again, okay?\x02\x03",

            "#811FNext time, it'll be my turn\x01",
            "to surprise YOU!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#2P#1018FHaha... Yeah! Bring it on!\x02",
    )

    CloseMessageWindow()
    OP_B7(0x9)
    OP_B7(0xD)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF94")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #274
        (
            "\x07\x05Following that, Agate and Tita returned to the\x01",
            "Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #275
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #276
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_C434")

    label("loc_BF94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C088")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #277
        (
            "\x07\x05Following that, Scherazard and Agate returned to\x01",
            "the Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #278
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #279
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_C434")

    label("loc_C088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C175")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #280
        (
            "\x07\x05Following that, Agate and Zin returned to the\x01",
            "Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #281
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #282
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_C434")

    label("loc_C175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C268")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #283
        (
            "\x07\x05Following that, Scherazard and Tita returned to\x01",
            "the Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #284
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #285
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_C434")

    label("loc_C268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C354")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #286
        (
            "\x07\x05Following that, Tita and Zin returned to the\x01",
            "Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #287
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #288
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_C434")

    label("loc_C354")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #289
        (
            "\x07\x05After that, Scherazard and Zin returned to\x01",
            "the Ruan guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #290
        "\x07\x05Sieg, who'd come from Grancel, flew back to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #291
        (
            "\x07\x05Estelle's group said their farewells to everyone\x01",
            "at the academy and departed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_C434")

    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #292
        "#0CQuest #2C[The Occupation of Jenis] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0xC0, 0x4, 0x10)
    OP_28(0xC0, 0x1, 0x8000)
    OP_28(0xC1, 0x3, 0x2)
    OP_28(0xC1, 0x3, 0x8)
    OP_28(0xC3, 0x4, 0x2)
    OP_28(0xC3, 0x4, 0x8)
    OP_28(0xC3, 0x4, 0x10)
    OP_28(0xC3, 0x1, 0x100)
    OP_28(0xC3, 0x1, 0x200)
    OP_28(0xC3, 0x1, 0x400)
    OP_28(0xC3, 0x1, 0x800)
    OP_28(0xC3, 0x1, 0x1000)
    OP_28(0xC3, 0x1, 0x2000)
    OP_28(0xC3, 0x1, 0x4000)
    OP_28(0xC3, 0x1, 0x8000)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C508")
    AddParty(0x5, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C532")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52E")
    AddParty(0x2, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C532")

    label("loc_C52E")

    AddParty(0x2, 0xF9, 0xFF)

    label("loc_C532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C55C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C558")
    AddParty(0x6, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C55C")

    label("loc_C558")

    AddParty(0x6, 0xF9, 0xFF)

    label("loc_C55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C586")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C582")
    AddParty(0x7, 0xF8, 0xFF)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C586")

    label("loc_C582")

    AddParty(0x7, 0xF9, 0xFF)

    label("loc_C586")

    OP_6D(21410, 0, 45890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 21410, 0, 45890, 270)
    SetChrPos(0x1, 21410, 0, 45890, 270)
    SetChrPos(0x2, 21410, 0, 45890, 270)
    SetChrPos(0x3, 21410, 0, 45890, 270)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_A2(0x202F)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 45800, 0, 46000, 0)
    OP_43(0x10, 0x0, 0x0, 0x4)
    SetChrPos(0xC, 36500, 0, 70920, 225)
    OP_43(0xC, 0x0, 0x6, 0x2)
    SetChrPos(0xD, 35500, 0, 69860, 45)
    OP_43(0xD, 0x0, 0x6, 0x2)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(100)
    OP_1D(0x1A)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_82_B530 end

    def Function_83_C6B0(): pass

    label("Function_83_C6B0")

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
        (0, "loc_C729"),
        (1, "loc_C72F"),
        (SWITCH_DEFAULT, "loc_C735"),
    )


    label("loc_C729")

    OP_A2(0x1200)
    Jump("loc_C735")

    label("loc_C72F")

    OP_A2(0x1201)
    Jump("loc_C735")

    label("loc_C735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C743")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_C747")

    label("loc_C743")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_C747")

    Return()

    # Function_83_C6B0 end

    def Function_84_C748(): pass

    label("Function_84_C748")

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

    # Function_84_C748 end

    def Function_85_C7A1(): pass

    label("Function_85_C7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C990")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C826")

    ChrTalk(    #293
        0x101,
        (
            "#1002F(Now's our chance while the enemy is\x01",
            "being drawn out. We need to free the\x01",
            "hostages quickly.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96D")

    label("loc_C826")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C892")

    ChrTalk(    #294
        0x102,
        (
            "#1042F(Right now the enemy is focused outside.\x01",
            "We need to hurry and free the hostages.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96D")

    label("loc_C892")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8FB")

    ChrTalk(    #295
        0x10A,
        (
            "#816F(It seems like they've taken the bait.\x01",
            "We need to hurry and free the hostages.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96D")

    label("loc_C8FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96D")

    ChrTalk(    #296
        0x10E,
        (
            "#842F(Now's our chance while the enemy is otherwise\x01",
            "occupied. Hurry, let's rescue the hostages.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C96D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_CA9C")

    label("loc_C990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA0B")
    EventBegin(0x1)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #297
        0x105,
        (
            "#040FIt's almost sunset. Let's return\x01",
            "to the Student Council room.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_CA9C")

    label("loc_CA0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA9C")
    EventBegin(0x1)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #298
        0x105,
        (
            "#040FThe students should be in the dorms or\x01",
            "classrooms. Let's ask around inside the\x01",
            "school.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_CA9C")

    Return()

    # Function_85_C7A1 end

    def Function_86_CA9D(): pass

    label("Function_86_CA9D")

    SetPlaceName(0x5F)
    Return()

    # Function_86_CA9D end

    def Function_87_CAA1(): pass

    label("Function_87_CAA1")

    SetPlaceName(0x5C)
    Return()

    # Function_87_CAA1 end

    def Function_88_CAA5(): pass

    label("Function_88_CAA5")

    SetPlaceName(0x5D)
    Return()

    # Function_88_CAA5 end

    def Function_89_CAA9(): pass

    label("Function_89_CAA9")

    SetPlaceName(0x6C)
    Return()

    # Function_89_CAA9 end

    def Function_90_CAAD(): pass

    label("Function_90_CAAD")

    SetPlaceName(0x6D)
    Return()

    # Function_90_CAAD end

    SaveToFile()

Try(main)
