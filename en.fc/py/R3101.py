from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60020",
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
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Eastern Man',                          # 15
        'Zeiss',                                # 16
        'Elmo Village',                         # 17
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
        Unknown_3A              = 144,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT09/CH10060 ._CH',             # 01
        'ED6_DT09/CH10061 ._CH',             # 02
        'ED6_DT09/CH10063 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00102 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT07/CH00111 ._CH',             # 08
        'ED6_DT07/CH00112 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT09/CH10610 ._CH',             # 0B
        'ED6_DT09/CH10611 ._CH',             # 0C
        'ED6_DT09/CH10080 ._CH',             # 0D
        'ED6_DT09/CH10081 ._CH',             # 0E
        'ED6_DT09/CH10120 ._CH',             # 0F
        'ED6_DT09/CH10121 ._CH',             # 10
        'ED6_DT09/CH10140 ._CH',             # 11
        'ED6_DT09/CH10141 ._CH',             # 12
        'ED6_DT09/CH10620 ._CH',             # 13
        'ED6_DT09/CH10621 ._CH',             # 14
        'ED6_DT09/CH10600 ._CH',             # 15
        'ED6_DT09/CH10601 ._CH',             # 16
        'ED6_DT09/CH10400 ._CH',             # 17
        'ED6_DT09/CH10401 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT09/CH10060P._CP',             # 01
        'ED6_DT09/CH10061P._CP',             # 02
        'ED6_DT09/CH10063P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00102P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT07/CH00111P._CP',             # 08
        'ED6_DT07/CH00112P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT09/CH10610P._CP',             # 0B
        'ED6_DT09/CH10611P._CP',             # 0C
        'ED6_DT09/CH10080P._CP',             # 0D
        'ED6_DT09/CH10081P._CP',             # 0E
        'ED6_DT09/CH10120P._CP',             # 0F
        'ED6_DT09/CH10121P._CP',             # 10
        'ED6_DT09/CH10140P._CP',             # 11
        'ED6_DT09/CH10141P._CP',             # 12
        'ED6_DT09/CH10620P._CP',             # 13
        'ED6_DT09/CH10621P._CP',             # 14
        'ED6_DT09/CH10600P._CP',             # 15
        'ED6_DT09/CH10601P._CP',             # 16
        'ED6_DT09/CH10400P._CP',             # 17
        'ED6_DT09/CH10401P._CP',             # 18
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21960,
        Z                   = 0,
        Y                   = 68390,
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
        X                   = 68320,
        Z                   = 0,
        Y                   = -37930,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 31840,
        Z                   = -140,
        Y                   = -14910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21310,
        Z                   = 20,
        Y                   = 1100,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6650,
        Z                   = 10,
        Y                   = 6470,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7960,
        Z                   = -70,
        Y                   = 22900,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7300,
        Z                   = 80,
        Y                   = -13910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8220,
        Z                   = 70,
        Y                   = -25600,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18960,
        Z                   = 10,
        Y                   = -47120,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19200,
        Z                   = 50,
        Y                   = -40070,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2840,
        Z                   = 20,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23970,
        Z                   = -60,
        Y                   = -56200,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47630,
        Z                   = 40,
        Y                   = -38230,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41100,
        Z                   = 30,
        Y                   = -42080,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46340,
        Z                   = -10,
        Y                   = -47090,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39960,
        Z                   = -50,
        Y                   = -46350,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35370,
        Z                   = 60,
        Y                   = -38180,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39680,
        Z                   = -30,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31310,
        Z                   = -20,
        Y                   = -44150,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37830,
        Z                   = -40,
        Y                   = -49270,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20630,
        Z                   = -50,
        Y                   = -21460,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x213,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6340,
        Z                   = -20,
        Y                   = 12260,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9790,
        Z                   = 30,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7920,
        Z                   = -70,
        Y                   = -27310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22580,
        Z                   = 10,
        Y                   = 23060,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35830,
        Z                   = 30,
        Y                   = 26470,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31840,
        Z                   = -140,
        Y                   = -14910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21310,
        Z                   = 20,
        Y                   = 1100,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x351,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6650,
        Z                   = 10,
        Y                   = 6470,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7960,
        Z                   = -70,
        Y                   = 22900,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7300,
        Z                   = 80,
        Y                   = -13910,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8220,
        Z                   = 70,
        Y                   = -25600,
        Unknown_0C          = 180,
        Unknown_0E          = 21,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18960,
        Z                   = 10,
        Y                   = -47120,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19200,
        Z                   = 50,
        Y                   = -40070,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2840,
        Z                   = 20,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23970,
        Z                   = -60,
        Y                   = -56200,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -47630,
        Z                   = 40,
        Y                   = -38230,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41100,
        Z                   = 30,
        Y                   = -42080,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46340,
        Z                   = -10,
        Y                   = -47090,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39960,
        Z                   = -50,
        Y                   = -46350,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35370,
        Z                   = 60,
        Y                   = -38180,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39680,
        Z                   = -30,
        Y                   = -43880,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31310,
        Z                   = -20,
        Y                   = -44150,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37830,
        Z                   = -40,
        Y                   = -49270,
        Unknown_0C          = 180,
        Unknown_0E          = 17,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20630,
        Z                   = -50,
        Y                   = -21460,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x353,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6340,
        Z                   = -20,
        Y                   = 12260,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9790,
        Z                   = 30,
        Y                   = -7150,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7920,
        Z                   = -70,
        Y                   = -27310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22580,
        Z                   = 10,
        Y                   = 23060,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35830,
        Z                   = 30,
        Y                   = 26470,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -47070,
        Y                   = -2000,
        Z                   = 850,
        Range               = 5000,
        Unknown_10          = 0x3A98,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -26870,
        Y                   = -1000,
        Z                   = 40570,
        Range               = -17040,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x94DE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 36090,
        TriggerZ            = -130,
        TriggerY            = -4970,
        TriggerRange        = 1000,
        ActorX              = 36580,
        ActorZ              = 1370,
        ActorY              = -4390,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43660,
        TriggerZ            = -50,
        TriggerY            = -54700,
        TriggerRange        = 1000,
        ActorX              = -44130,
        ActorZ              = 1450,
        ActorY              = -55170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21630,
        TriggerZ            = -10,
        TriggerY            = 8540,
        TriggerRange        = 1000,
        ActorX              = -21750,
        ActorZ              = 1490,
        ActorY              = 7880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_89E",          # 00, 0
        "Function_1_8C1",          # 01, 1
        "Function_2_A3F",          # 02, 2
        "Function_3_A72",          # 03, 3
        "Function_4_C7F",          # 04, 4
        "Function_5_212F",         # 05, 5
        "Function_6_2CC1",         # 06, 6
        "Function_7_2E24",         # 07, 7
        "Function_8_2F5B",         # 08, 8
    )


    def Function_0_89E(): pass

    label("Function_0_89E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_8AA"),
        (SWITCH_DEFAULT, "loc_8C0"),
    )


    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BD")
    OP_A2(0x521)
    Event(0, 3)

    label("loc_8BD")

    Jump("loc_8C0")

    label("loc_8C0")

    Return()

    # Function_0_89E end

    def Function_1_8C1(): pass

    label("Function_1_8C1")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x3002E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    OP_B1("R3101_y")
    Jump("loc_8F4")

    label("loc_8EB")

    OP_B1("R3101_n")

    label("loc_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97B")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Jump("loc_9F3")

    label("loc_97B")

    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A05")
    OP_6F(0x0, 0)
    Jump("loc_A0C")

    label("loc_A05")

    OP_6F(0x0, 60)

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1E")
    OP_6F(0x2, 0)
    Jump("loc_A25")

    label("loc_A1E")

    OP_6F(0x2, 60)

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A37")
    OP_6F(0x1, 0)
    Jump("loc_A3E")

    label("loc_A37")

    OP_6F(0x1, 60)

    label("loc_A3E")

    Return()

    # Function_1_8C1 end

    def Function_2_A3F(): pass

    label("Function_2_A3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A71")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A6E")

    label("loc_A65")

    OP_99(0xFE, 0x0, 0x7, 0x578)

    label("loc_A6E")

    Jump("Function_2_A3F")

    label("loc_A71")

    Return()

    # Function_2_A3F end

    def Function_3_A72(): pass

    label("Function_3_A72")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(47020, 0, -37820, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 46440, 0, -37370, 135)
    SetChrPos(0x102, 47530, 0, -38220, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#002FNow, let's see...\x02\x03",

            "The plains road is so wide...\x01",
            "Where should we search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#015F#4PHmm... Supposedly, she said she was going\x01",
            "to take in the scenery...\x02\x03",

            "#012FSo it seems likely she's wandered away from\x01",
            "where the road's paved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#007FOh, man... Well, that's going\x01",
            "to be REALLY safe, isn't it?\x02\x03",

            "#002FBut hey, no biggie. Let's find\x01",
            "her and bring her back! Hopefully\x01",
            "with all pieces intact...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x40, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_3_A72 end

    def Function_4_C7F(): pass

    label("Function_4_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212E")
    OP_A2(0x522)
    OP_28(0x40, 0x1, 0x100)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -46310, 110, 840, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -47620, -30, -2150, 0)
    SetChrPos(0xA, -45450, -50, -2620, 0)
    SetChrPos(0xB, -44530, 40, -1070, 0)
    SetChrPos(0xC, -42950, 40, 330, 0)
    SetChrPos(0xD, -43940, 10, 2780, 0)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0xB, 0x8, 0)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0xD, 0x8, 0)
    TurnDirection(0x8, 0xB, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)

    NpcTalk(    #3
        0x8,
        "Girl's Voice",
        (
            "Aaahhhhh...! Nooo!\x01",
            "Someone help meeeee!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #4
        0x101,
        "#002FDid you hear that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#012FWhatever it was, it's not far.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #6
        0x8,
        "Girl's Voice",
        "Aidios! Daddy! Mommy!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x8,
        "Girl's Voice",
        "Niiiiaaalll! Help meeeee!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x101,
        (
            "#509FThat voice sounds suspiciously\x01",
            "familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#012FI think you're probably right...\x01",
            "but let's hurry!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(100)
    Fade(1000)
    OP_6D(-46630, 80, 1280, 0)
    OP_6C(0, 0)
    OP_B7(0xF, 0x1)
    AddParty(0xF, 0xFF)
    SetChrFlags(0x110, 0x8)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    OP_0D()
    OP_21()
    OP_1D(0x51)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)

    ChrTalk(    #10
        0xB,
        "Grrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#154F#3PC-C'mon, puppies...\x01",
            "Can't we talk about this?\x02\x03",

            "I don't think I'd taste\x01",
            "very good...\x02\x03",

            "I mean, I sleep at least twelve\x01",
            "hours a day, and I eat lots of\x01",
            "veggies, and my skin's all smooth!\x02\x03",

            "#153F...Uh. Wait, does being healthy\x01",
            "make me seem yummier?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)

    ChrTalk(    #12
        0xB,
        "Grrrrrrrr...!!\x02",
    )

    CloseMessageWindow()

    def lambda_108D():

        label("loc_108D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_108D")

    QueueWorkItem2(0x9, 2, lambda_108D)

    def lambda_109E():

        label("loc_109E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_109E")

    QueueWorkItem2(0xA, 1, lambda_109E)

    def lambda_10AF():

        label("loc_10AF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10AF")

    QueueWorkItem2(0xB, 1, lambda_10AF)

    def lambda_10C0():

        label("loc_10C0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10C0")

    QueueWorkItem2(0xC, 1, lambda_10C0)

    def lambda_10D1():

        label("loc_10D1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_10D1")

    QueueWorkItem2(0xD, 2, lambda_10D1)

    def lambda_10E2():
        OP_6D(-48670, -60, 3500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10E2)
    SetChrChipByIndex(0xB, 2)

    def lambda_10FF():
        OP_8E(0xFE, 0xFFFF4C82, 0x64, 0x1CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10FF)
    Sleep(300)
    SetChrChipByIndex(0x9, 2)

    def lambda_1124():
        OP_8F(0xFE, 0xFFFF3D82, 0x1E, 0x140, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1124)
    Sleep(100)
    SetChrChipByIndex(0xD, 2)

    def lambda_1149():
        OP_8F(0xFE, 0xFFFF4A70, 0xFFFFFFE2, 0x1072, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1149)
    Sleep(200)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_117B():
        OP_8F(0x8, 0xFFFF3F80, 0xFFFFFFBA, 0xD0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_117B)
    Sleep(500)
    SetChrChipByIndex(0xA, 2)

    def lambda_11A0():
        OP_8E(0xFE, 0xFFFF4458, 0x3C, 0x96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11A0)
    Sleep(300)
    SetChrChipByIndex(0xC, 2)

    def lambda_11C5():
        OP_8E(0xFE, 0xFFFF4D2C, 0x0, 0xA50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11C5)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 1)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 1)
    WaitChrThread(0xB, 0x2)
    SetChrChipByIndex(0xB, 1)
    WaitChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 1)
    WaitChrThread(0xC, 0x2)
    SetChrChipByIndex(0xC, 1)

    ChrTalk(    #13
        0x8,
        (
            "#152F#3PEeek! If I'd known this was coming,\x01",
            "I'd have made sure to get paid in\x01",
            "advance! And had a nice meal!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0xC, 1)
    SetChrPos(0x101, -44480, -70, -4400, 0)
    SetChrPos(0x102, -40040, 10, -840, 0)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    Sleep(100)

    def lambda_12D2():
        OP_6D(-47620, 30, 2760, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12D2)
    SetChrChipByIndex(0x101, 6)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_12F4():
        OP_99(0x101, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12F4)

    def lambda_1304():
        OP_8E(0xFE, 0xFFFF4CDC, 0x32, 0xFFFFFCCC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1304)

    def lambda_131F():
        OP_8E(0xFE, 0xFFFF4F16, 0x5A, 0x1AE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_131F)
    WaitChrThread(0x101, 0x1)

    def lambda_133F():

        label("loc_133F")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_133F")

    QueueWorkItem2(0x101, 2, lambda_133F)

    def lambda_1350():
        OP_96(0xFE, 0xFFFF45FC, 0xFFFFFFE2, 0xAC8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1350)
    Sleep(50)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    PlayEffect(0x8, 0xFF, 0xB, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_13C0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xFA0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13C0)
    Sleep(50)

    def lambda_13E3():

        label("loc_13E3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13E3")

    QueueWorkItem2(0xC, 2, lambda_13E3)

    def lambda_13F4():

        label("loc_13F4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_13F4")

    QueueWorkItem2(0xD, 2, lambda_13F4)

    def lambda_1405():
        OP_8F(0xFE, 0xFFFF5286, 0xA, 0xA82, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1405)

    def lambda_1420():
        OP_8F(0xFE, 0xFFFF4B9C, 0x0, 0x1554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1420)
    SetChrChipByIndex(0x102, 9)
    PlayEffect(0x12, 0xFF, 0x102, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_1475():
        OP_99(0x102, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1475)

    def lambda_1485():
        OP_96(0xFE, 0xFFFF4444, 0x32, 0x5A0, 0xBB8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1485)
    Sleep(350)
    OP_22(0x1F5, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xB, 0, 1000, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_14E2():
        OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14E2)
    OP_8F(0xB, 0xFFFF487C, 0x64, 0x352, 0x3A98, 0x0)

    def lambda_1508():

        label("loc_1508")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1508")

    QueueWorkItem2(0x102, 2, lambda_1508)

    def lambda_1519():

        label("loc_1519")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1519")

    QueueWorkItem2(0x9, 2, lambda_1519)

    def lambda_152A():

        label("loc_152A")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_152A")

    QueueWorkItem2(0xA, 2, lambda_152A)

    def lambda_153B():
        OP_8F(0xFE, 0xFFFF3BC0, 0x1E, 0xFFFFFDBC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_153B)

    def lambda_1556():
        OP_8F(0xFE, 0xFFFF4548, 0xFFFFFFEC, 0xFFFFFB78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1556)
    OP_95(0xB, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0xBB8)
    Sleep(2000)

    ChrTalk(    #14
        0x8,
        (
            "#153FHuh?\x01",
            "You two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#006FHeh...\x01",
            "Just as I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#010FNo need to worry, Dorothy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#155F...What were your names again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#007FUgh... Yeah, it's the same\x01",
            "old Dorothy, all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#018F...We're Joshua and Estelle,\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#151FHa ha...\x01",
            "I'm just teasing.\x02\x03",

            "Fancy meeting you two here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#509F(Aidios, give me the strength not\x01",
            "to leave her to the beasts...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#016FEstelle, on your guard!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_1749():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1749)
    SetChrChipByIndex(0xC, 2)

    def lambda_1764():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1764)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_1784():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1784)
    SetChrChipByIndex(0xD, 2)

    def lambda_179F():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_179F)
    Sleep(200)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Battle(0x3A5, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_17E1"),
        (SWITCH_DEFAULT, "loc_17E4"),
    )


    label("loc_17E1")

    OP_B4(0x0)
    Return()

    label("loc_17E4")

    EventBegin(0x0)
    OP_6D(-48280, -30, 2740, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x110, 0x8)
    SetChrPos(0x110, -51180, 0, 4520, 135)
    SetChrPos(0x101, -47620, -30, 2760, 90)
    SetChrPos(0x102, -48060, 50, 1440, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #23
        0x101,
        (
            "#006FWhew... I don't know how we\x01",
            "chased them off, but we did.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)
    SetChrChipByIndex(0x101, 65535)

    ChrTalk(    #24
        0x102,
        (
            "#012FDid they look familiar\x01",
            "to you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #25
        0x101,
        (
            "#002FYup. They're the monsters who \x01",
            "attacked the checkpoint on the\x01",
            "mountain pass.\x02\x03",

            "I wonder what they're doing\x01",
            "out here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x110,
        (
            "#151FOh, how lovely! You bracers\x01",
            "are very impressive!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19AD():

        label("loc_19AD")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_19AD")

    QueueWorkItem2(0x101, 1, lambda_19AD)

    def lambda_19BE():

        label("loc_19BE")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_19BE")

    QueueWorkItem2(0x102, 1, lambda_19BE)

    def lambda_19CF():
        OP_6B(2690, 2300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19CF)
    OP_8E(0x110, 0xFFFF4106, 0xFFFFFFE2, 0xA28, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #27
        0x110,
        (
            "#151FEstelle and Joshua...\x01",
            "It's been such a long time,\x01",
            "hasn't it?\x02\x03",

            "I never would've thought\x01",
            "I'd see you here.\x02\x03",

            "#155FDo you think...maybe...we were\x01",
            "destined to meet again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#007FFate is a fickle mistress,\x01",
            "all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010FSo, uh, Dorothy...\x02\x03",

            "...Are you staying at the inn\x01",
            "in Elmo, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x110,
        (
            "#153FWhy, yes...\x01",
            "HEEEEYYY, how did you know?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05Joshua and Estelle explained that the owner of Elmo's inn had requested\x01",
            "that they bring her back safely.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #32
        0x110,
        (
            "#151FOh, I see...\x01",
            "Well, isn't that just terrible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#007FUh-huh... As if you care about\x01",
            "anyone else's problems.\x02\x03",

            "#000FSo, what brings you out here?\x01",
            "A little cross-country hiking,\x01",
            "maybe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x110,
        (
            "#151FTsk, tsk, tsk... You mean you\x01",
            "don't even know THAT much?\x02\x03",

            "*chuckle* I see that you haven't\x01",
            "gotten any more insightful in our\x01",
            "time apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#009FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x110,
        (
            "#150FThe answer is actually that I'm looking\x01",
            "for a photograph that the newspaper\x01",
            "needs for a special edition.\x02\x03",

            "Oh, and by the way...Nial's the\x01",
            "one who assigned me this task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#010FI see...\x01",
            "So it's work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#007FOkay, but why would you be\x01",
            "looking for that HERE?\x02\x03",

            "Oh, forget it! This wears me\x01",
            "out faster than fighting any\x01",
            "monster ever did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x110,
        (
            "#154FAww, poor Estelle! Did you\x01",
            "get hurt in battle?\x02\x03",

            "Pain, pain, go away! Come again\x01",
            "some other day! ...Or not at all\x01",
            "would be better, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#005F#3SI'm not injured, I'm just\x01",
            "REALLY AGGRAVATED AT YOUR\x01",
            "UTTER OBLIVIOUSNESS!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#015F(Wow. It's rare for someone to\x01",
            "get under Estelle's skin this\x01",
            "badly...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#010FEstelle, why don't we head\x01",
            "back to Elmo?\x02\x03",

            "Maybe Tita's done fixing\x01",
            "the pump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#007FYes...\x01",
            "Let's go back...\x02\x03",

            "#509FAnd I think Dorothy will be\x01",
            "coming back with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x110,
        (
            "#154FHuh...? But I wanted to stay\x01",
            "and take more pictures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#001F#3SWe. Are. Going. Now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x110,
        "#152FScary...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    EventEnd(0x0)

    label("loc_212E")

    Return()

    # Function_4_C7F end

    def Function_5_212F(): pass

    label("Function_5_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2912")
    OP_A2(0x52A)
    EventBegin(0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -21840, 0, 52760, 180)

    NpcTalk(    #47
        0xE,
        "Man's Voice",
        "Ah, very good.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x110, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-22010, 0, 41300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -21580, 0, 38890, 0)
    SetChrPos(0x102, -22680, 0, 38930, 0)
    SetChrPos(0x107, -21390, 0, 37530, 0)
    SetChrPos(0x110, -22380, 0, 37650, 0)

    def lambda_224F():

        label("loc_224F")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_224F")

    QueueWorkItem2(0x101, 2, lambda_224F)

    def lambda_2260():

        label("loc_2260")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2260")

    QueueWorkItem2(0x102, 2, lambda_2260)

    def lambda_2271():

        label("loc_2271")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2271")

    QueueWorkItem2(0x107, 2, lambda_2271)

    def lambda_2282():

        label("loc_2282")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2282")

    QueueWorkItem2(0x110, 2, lambda_2282)
    OP_0D()
    OP_8E(0xE, 0xFFFFAA10, 0x0, 0xA528, 0xFA0, 0x0)

    ChrTalk(    #48
        0xE,
        (
            "#070FHello, ladies. I was just\x01",
            "wondering if I could ask--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x107,
        (
            "#064FWhoa...\x01",
            "He's huge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x110,
        "#153FIt's a b-b-b-bear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "#074F...Bear? Umm, okay.\x02\x03",

            "#070FYou don't need to worry about me.\x01",
            "All I want are some directions.\x02\x03",

            "You wouldn't happen to know\x01",
            "where Elmo's hot springs are,\x01",
            "would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#501FOh! Well, we just came\x01",
            "from there, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#010FIt's just down the road,\x01",
            "south from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "#071FAh, I see.\x01",
            "Thanks for the information.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #56
        0xE,
        (
            "#073FOh... You...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "#073FHmmm... Could it be?\x02\x03",

            "Is it possible...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#010FIs...what possible, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xE,
        (
            "#070FOh, sorry.\x01",
            "It's nothing important.\x02\x03",

            "Take care.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_254E():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_254E)

    def lambda_255E():
        OP_6D(-22090, 0, 38340, 2500)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_255E)

    def lambda_2576():
        OP_8E(0xFE, 0xFFFFB12C, 0x0, 0x9F9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2576)
    WaitChrThread(0xE, 0x1)
    OP_8E(0xE, 0xFFFFB12C, 0x0, 0x6590, 0xFA0, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x110, 0xFF)

    ChrTalk(    #61
        0x101,
        (
            "#505FUh, wow. Man of few words.\x02\x03",

            "#505FHis clothes looked Eastern, so\x01",
            "I figure he must be foreign.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2626():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2626)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #62
        0x102,
        (
            "#010FWell, Zeiss IS right on the border\x01",
            "with the Calvard Republic.\x02\x03",

            "He might've come from there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x110, 0, 600)
    OP_8C(0x107, 0, 600)

    ChrTalk(    #63
        0x107,
        (
            "#060FI bet you're right.\x02\x03",

            "Mrs. Mao told me about\x01",
            "people who live way off in\x01",
            "the east.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#501FOh, right... I think Kilika\x01",
            "is from the east, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x110,
        (
            "#151FAnd he was so HUGE.\x02\x03",

            "I was super-surprised!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        (
            "#067FHa ha... I guess he does\x01",
            "kinda look like a bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#006FBut he doesn't act like\x01",
            "any bear I've ever seen.\x02\x03",

            "He looks like he studies\x01",
            "martial arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x107,
        "#064FHow can you tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#502FWell, I'm a martial artist, too.\x02\x03",

            "He wasn't just big. He looked\x01",
            "like he'd trained his body like\x01",
            "crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#010FIndeed. And his legs were\x01",
            "like tree trunks.\x02\x03",

            "He might be a master, just\x01",
            "like Estelle's read about.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2CC0")

    label("loc_2912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CC0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B10")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2B")

    ChrTalk(    #71
        0x101,
        (
            "#002FAww, she's not here.\x02\x03",

            "I don't think she could\x01",
            "have gotten far, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #72
        0x102,
        (
            "#010FProbably not, if you think\x01",
            "about what Ed said.\x02\x03",

            "Let's search around in\x01",
            "the field some more.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #73
        0x101,
        "#002FYeah, let's check it out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B0D")

    label("loc_2A2B")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #74
        0x101,
        (
            "#002FHey, Joshua?\x02\x03",

            "You know, I don't think she\x01",
            "went that far, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #75
        0x102,
        (
            "#010FProbably not, if you think\x01",
            "about what Ed said.\x02\x03",

            "Let's search around in\x01",
            "the field some more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#002FYeah, let's check it out.\x02",
    )

    CloseMessageWindow()

    label("loc_2B0D")

    Jump("loc_2B8B")

    label("loc_2B10")


    def lambda_2B16():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B16)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #77
        0x102,
        (
            "#010FProbably not, if you think\x01",
            "about what Ed said.\x02\x03",

            "Let's search around in\x01",
            "the field some more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8B")

    Jump("loc_2CA5")

    label("loc_2B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #78
        0x102,
        (
            "#010FCome on, Estelle. We need\x01",
            "to hurry back to Elmo.\x02\x03",

            "Everyone at the inn is probably\x01",
            "worried about us by now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #79
        0x101,
        "#000FYeah, probably...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA5")

    label("loc_2C3C")


    ChrTalk(    #80
        0x102,
        (
            "#010FZeiss is this way...\x02\x03",

            "Everyone at the inn must be\x01",
            "worried about us. We should\x01",
            "go back to Elmo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA5")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2CC0")

    Return()

    # Function_5_212F end

    def Function_6_2CC1(): pass

    label("Function_6_2CC1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2D38")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59B)
    Jump("loc_2DB0")

    label("loc_2D38")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #82
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2DB0")

    Jump("loc_2E16")

    label("loc_2DB3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        (
            "\x07\x05It wouldn't be empty if you hadn't already looted it,\x01",
            "now would it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x8F)

    label("loc_2E16")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2CC1 end

    def Function_7_2E24(): pass

    label("Function_7_2E24")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F16")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_2E9B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59C)
    Jump("loc_2F13")

    label("loc_2E9B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #85
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2F13")

    Jump("loc_2F4D")

    label("loc_2F16")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #86
        "\x07\x05It's empty! Diabolical!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x90)

    label("loc_2F4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_2E24 end

    def Function_8_2F5B(): pass

    label("Function_8_2F5B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3059")
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -44130, 1500, -55170, 320)
    TurnDirection(0x11, 0x0, 0)

    def lambda_2FAA():
        OP_8F(0xFE, 0xFFFF539E, 0x3E8, 0xFFFF287E, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FAA)

    def lambda_2FC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2FC5)
    ClearChrFlags(0x11, 0x80)

    AnonymousTalk(    #87
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300E")
    Battle(0x356, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_301B")

    label("loc_300E")

    Battle(0x216, 0x0, 0x0, 0x0, 0xFF)

    label("loc_301B")

    SetChrFlags(0x11, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3034"),
        (2, "loc_3046"),
        (1, "loc_3056"),
        (SWITCH_DEFAULT, "loc_3059"),
    )


    label("loc_3034")

    OP_A2(0x59E)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_3059")

    label("loc_3046")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3056")

    OP_B4(0x0)
    Return()

    label("loc_3059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x26C, 1)"), scpexpr(EXPR_END)), "loc_30AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #88
        "\x07\x00Found \x07\x02Hit 3\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x59D)
    Jump("loc_3117")

    label("loc_30AB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #89
        (
            "\x07\x00Found \x07\x02Hit 3\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Hit 3\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3117")

    Jump("loc_3195")

    label("loc_311A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #90
        (
            "\x07\x05You must be awfully optimistic if you think\x01",
            "more treasure is going to appear in this chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x91)

    label("loc_3195")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2F5B end

    SaveToFile()

Try(main)
