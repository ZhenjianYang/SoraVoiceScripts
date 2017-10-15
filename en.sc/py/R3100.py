from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        'Royal Army Officer',                   # 9
        'Soldier',                              # 10
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
        'Vanguard',                             # 25
        'Vanguard',                             # 26
        'Vanguard',                             # 27
        'Vanguard',                             # 28
        'Vanguard',                             # 29
        'Vanguard',                             # 30
        'Target',                               # 31
        'Target',                               # 32
        'Target',                               # 33
        'Target',                               # 34
        'Target',                               # 35
        'Target',                               # 36
        'Zeiss',                                # 37
        'Elmo Village',                         # 38
        'Wolf Fort',                            # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
        '',                                     # 43
        '',                                     # 44
        '',                                     # 45
        '',                                     # 46
        '',                                     # 47
        '',                                     # 48
        '',                                     # 49
        '',                                     # 50
        '',                                     # 51
        '',                                     # 52
        '',                                     # 53
        '',                                     # 54
        '',                                     # 55
        '',                                     # 56
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
        'ED6_DT09/CH10610 ._CH',             # 00
        'ED6_DT09/CH10611 ._CH',             # 01
        'ED6_DT09/CH10080 ._CH',             # 02
        'ED6_DT09/CH10081 ._CH',             # 03
        'ED6_DT09/CH10120 ._CH',             # 04
        'ED6_DT09/CH10121 ._CH',             # 05
        'ED6_DT09/CH10140 ._CH',             # 06
        'ED6_DT09/CH10141 ._CH',             # 07
        'ED6_DT09/CH10620 ._CH',             # 08
        'ED6_DT09/CH10621 ._CH',             # 09
        'ED6_DT09/CH10600 ._CH',             # 0A
        'ED6_DT09/CH10601 ._CH',             # 0B
        'ED6_DT09/CH10400 ._CH',             # 0C
        'ED6_DT09/CH10401 ._CH',             # 0D
        'ED6_DT09/CH11210 ._CH',             # 0E
        'ED6_DT09/CH11211 ._CH',             # 0F
        'ED6_DT09/CH11250 ._CH',             # 10
        'ED6_DT09/CH11251 ._CH',             # 11
        'ED6_DT07/CH00330 ._CH',             # 12
        'ED6_DT07/CH01300 ._CH',             # 13
        'ED6_DT29/CH12320 ._CH',             # 14
        'ED6_DT07/CH00336 ._CH',             # 15
        'ED6_DT07/CH00320 ._CH',             # 16
        'ED6_DT07/CH00321 ._CH',             # 17
        'ED6_DT29/CH12321 ._CH',             # 18
        'ED6_DT29/CH12323 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT09/CH10610P._CP',             # 00
        'ED6_DT09/CH10611P._CP',             # 01
        'ED6_DT09/CH10080P._CP',             # 02
        'ED6_DT09/CH10081P._CP',             # 03
        'ED6_DT09/CH10120P._CP',             # 04
        'ED6_DT09/CH10121P._CP',             # 05
        'ED6_DT09/CH10140P._CP',             # 06
        'ED6_DT09/CH10141P._CP',             # 07
        'ED6_DT09/CH10620P._CP',             # 08
        'ED6_DT09/CH10621P._CP',             # 09
        'ED6_DT09/CH10600P._CP',             # 0A
        'ED6_DT09/CH10601P._CP',             # 0B
        'ED6_DT09/CH10400P._CP',             # 0C
        'ED6_DT09/CH10401P._CP',             # 0D
        'ED6_DT09/CH11210P._CP',             # 0E
        'ED6_DT09/CH11211P._CP',             # 0F
        'ED6_DT09/CH11250P._CP',             # 10
        'ED6_DT09/CH11251P._CP',             # 11
        'ED6_DT07/CH00330P._CP',             # 12
        'ED6_DT07/CH01300P._CP',             # 13
        'ED6_DT29/CH12320P._CP',             # 14
        'ED6_DT07/CH00336P._CP',             # 15
        'ED6_DT07/CH00320P._CP',             # 16
        'ED6_DT07/CH00321P._CP',             # 17
        'ED6_DT29/CH12321P._CP',             # 18
        'ED6_DT29/CH12323P._CP',             # 19
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        X                   = -26180,
        Z                   = 0,
        Y                   = 75950,
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
        X                   = -27440,
        Z                   = 0,
        Y                   = -76050,
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
        X                   = 57120,
        Z                   = 20,
        Y                   = -11610,
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
        X                   = -31930,
        Z                   = -10,
        Y                   = 25570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17900,
        Z                   = -100,
        Y                   = 29570,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17830,
        Z                   = -50,
        Y                   = 10270,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33160,
        Z                   = 80,
        Y                   = 9720,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33640,
        Z                   = -20,
        Y                   = -11610,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34150,
        Z                   = 10,
        Y                   = -34210,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17610,
        Z                   = 60,
        Y                   = -32390,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13750,
        Z                   = 20,
        Y                   = 4540,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28640,
        Z                   = -50,
        Y                   = -14990,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39490,
        Z                   = -40,
        Y                   = 9070,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28310,
        Z                   = 0,
        Y                   = 15860,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19410,
        Z                   = -90,
        Y                   = 27970,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20370,
        Z                   = 10,
        Y                   = 8119,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21540,
        Z                   = 50,
        Y                   = 3820,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43300,
        Z                   = 80,
        Y                   = -22610,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25500,
        Z                   = 20,
        Y                   = 17440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7640,
        Z                   = 0,
        Y                   = 5540,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -31610,
        TriggerZ            = 0,
        TriggerY            = 41470,
        TriggerRange        = 1500,
        ActorX              = -31610,
        ActorZ              = 1500,
        ActorY              = 41470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15330,
        TriggerZ            = 0,
        TriggerY            = -13840,
        TriggerRange        = 1500,
        ActorX              = -15330,
        ActorZ              = 1350,
        ActorY              = -13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12250,
        TriggerZ            = 0,
        TriggerY            = -9350,
        TriggerRange        = 1500,
        ActorX              = -12250,
        ActorZ              = 1400,
        ActorY              = -9350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3410,
        TriggerZ            = -20,
        TriggerY            = -11850,
        TriggerRange        = 1000,
        ActorX              = 3410,
        ActorZ              = 1480,
        ActorY              = -12510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -29130,
        TriggerZ            = 90,
        TriggerY            = -8189,
        TriggerRange        = 1000,
        ActorX              = -28780,
        ActorZ              = 1590,
        ActorY              = -8610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_7EA",          # 00, 0
        "Function_1_809",          # 01, 1
        "Function_2_923",          # 02, 2
        "Function_3_A69",          # 03, 3
        "Function_4_BA8",          # 04, 4
        "Function_5_1547",         # 05, 5
        "Function_6_1695",         # 06, 6
        "Function_7_17B7",         # 07, 7
        "Function_8_18D9",         # 08, 8
        "Function_9_19FB",         # 09, 9
        "Function_10_1B1D",        # 0A, 10
        "Function_11_1C3F",        # 0B, 11
        "Function_12_1D61",        # 0C, 12
        "Function_13_1DE1",        # 0D, 13
        "Function_14_1E61",        # 0E, 14
        "Function_15_1EE1",        # 0F, 15
        "Function_16_2AA5",        # 10, 16
        "Function_17_2AD3",        # 11, 17
        "Function_18_2B01",        # 12, 18
        "Function_19_2B2F",        # 13, 19
        "Function_20_2B5D",        # 14, 20
        "Function_21_2BDE",        # 15, 21
        "Function_22_2C30",        # 16, 22
    )


    def Function_0_7EA(): pass

    label("Function_0_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_808")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_808")

    Return()

    # Function_0_7EA end

    def Function_1_809(): pass

    label("Function_1_809")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x23002D)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_836")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)

    label("loc_836")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_894")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_8E5")

    label("loc_894")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_8E5")

    label("loc_8A9")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_8E5")

    label("loc_8BE")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_8E5")

    label("loc_8D3")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_8E5")

    OP_51(0x31, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_902")
    OP_6F(0x0, 0)
    Jump("loc_909")

    label("loc_902")

    OP_6F(0x0, 60)

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91B")
    OP_6F(0x1, 0)
    Jump("loc_922")

    label("loc_91B")

    OP_6F(0x1, 60)

    label("loc_922")

    Return()

    # Function_1_809 end

    def Function_2_923(): pass

    label("Function_2_923")

    OP_EA(0x2, 0xEA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x250, 1)"), scpexpr(EXPR_END)), "loc_994")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x50\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1500)
    Jump("loc_9F8")

    label("loc_994")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x50\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x50\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_9F8")

    Jump("loc_A5B")

    label("loc_9FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The chest is full of hopes,\x01",
            "but you can't seem to take them away.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A5B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_923 end

    def Function_3_A69(): pass

    label("Function_3_A69")

    OP_EA(0x2, 0xEB, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B41")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D4, 1)"), scpexpr(EXPR_END)), "loc_ADA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xD4\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1501)
    Jump("loc_B3E")

    label("loc_ADA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xD4\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD4\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_B3E")

    Jump("loc_B9A")

    label("loc_B41")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05The only thing worse than people\x01",
            "like you? Chests like me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B9A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_A69 end

    def Function_4_BA8(): pass

    label("Function_4_BA8")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    SetChrPos(0x8, -29200, -70, 33610, 180)
    SetChrPos(0x9, -24560, 0, 32650, 180)
    SetChrPos(0xA, -23210, -40, 32509, 180)
    SetChrPos(0xB, -23790, 0, 34420, 180)
    SetChrPos(0xC, -30940, 10, 33050, 180)
    SetChrPos(0xD, -30670, 70, 34610, 180)
    SetChrPos(0xE, -32119, -10, 34350, 180)
    SetChrPos(0xF, -21940, -20, 29970, 180)
    SetChrPos(0x10, -20480, -20, 29690, 180)
    SetChrPos(0x11, -21000, -10, 30930, 180)
    SetChrPos(0x12, -37550, -70, 30440, 180)
    SetChrPos(0x13, -38850, -170, 32369, 180)
    SetChrPos(0x14, -37340, -100, 32500, 180)
    SetChrPos(0x15, -27000, 400, 33740, 180)
    SetChrPos(0x16, -34420, 400, 31580, 180)
    SetChrPos(0x17, -22100, 400, 26090, 180)
    SetChrPos(0x18, -28080, 0, -50520, 0)
    SetChrPos(0x19, -24880, 0, -51600, 0)
    SetChrPos(0x1A, -28240, 10, -55120, 0)
    SetChrPos(0x1B, -25980, 0, -55110, 0)
    SetChrPos(0x1C, -26210, 0, -58780, 0)
    SetChrPos(0x1D, -25980, 0, -62040, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    SetChrFlags(0x1A, 0x800)
    SetChrFlags(0x1B, 0x800)
    SetChrFlags(0x1C, 0x800)
    SetChrFlags(0x1D, 0x800)
    LoadEffect(0x0, "battle\\\\btgun60.eff")
    LoadEffect(0x1, "map\\\\mp019_00.eff")
    LoadEffect(0x2, "Scraft\\\\sc008_04.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    LoadEffect(0x4, "Scraft\\\\sc003_12.eff")
    OP_C8(0x200, 0x46, "C_PLAC19._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_43(0x8, 0x3, 0x0, 0x5)
    Sleep(2000)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        "#7PHere they come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "#7PHOWITZERS! Load and aim!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    PlayEffect(0x2, 0x0, 0xFF, -26480, 1250, 30810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x1, 0xFF, -33230, 1250, 28840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x2, 0xFF, -21710, 1250, 23210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(-25880, 0, -49340, 0)
    OP_67(0, 4130, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(146000, 0)
    OP_6E(290, 0)
    SetChrChipByIndex(0x18, 24)
    SetChrChipByIndex(0x19, 24)
    SetChrChipByIndex(0x1A, 24)
    SetChrChipByIndex(0x1B, 24)
    SetChrChipByIndex(0x1C, 24)
    SetChrChipByIndex(0x1D, 24)

    def lambda_102F():
        OP_6D(-26900, 0, -47350, 3500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_102F)

    def lambda_1047():
        OP_67(0, 5390, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1047)

    def lambda_105F():
        OP_6B(3280, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_105F)

    def lambda_106F():
        OP_6C(123000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_106F)

    def lambda_107F():
        OP_6E(340, 3500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_107F)

    def lambda_108F():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_108F)

    def lambda_10AA():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10AA)

    def lambda_10C5():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10C5)

    def lambda_10E0():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_10E0)

    def lambda_10FB():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_10FB)

    def lambda_1116():
        OP_90(0xFE, 0x3E8, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1116)
    Sleep(4000)
    Fade(500)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    OP_0D()

    ChrTalk(    #8
        0x8,
        "#7P#3SFIRE!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(100)
    OP_43(0x101, 0x2, 0x0, 0xD)
    Sleep(100)
    OP_43(0x101, 0x3, 0x0, 0xE)
    Sleep(3000)
    OP_43(0x102, 0x1, 0x0, 0xF)
    Fade(500)
    OP_6D(-25630, 0, -32509, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(156000, 0)
    OP_6E(329, 0)
    SetChrPos(0x1E, -25500, 0, -26000, 0)
    SetChrPos(0x1F, -29500, 0, -26000, 0)
    SetChrPos(0x20, -22000, 0, -31000, 0)
    SetChrPos(0x21, -34000, 0, -31000, 0)
    SetChrPos(0x22, -20000, 0, -37000, 0)
    SetChrPos(0x23, -36000, 0, -37000, 0)
    SetChrPos(0x18, -29080, 0, -36000, 0)
    SetChrPos(0x19, -25780, 0, -37590, 0)
    SetChrPos(0x1A, -27930, 0, -41140, 0)
    SetChrPos(0x1B, -24760, 0, -42840, 0)
    SetChrPos(0x1C, -27700, 0, -45820, 0)
    SetChrPos(0x1D, -24460, 0, -47690, 0)
    OP_43(0x18, 0x1, 0x0, 0x6)
    OP_43(0x19, 0x1, 0x0, 0x7)
    OP_43(0x1A, 0x1, 0x0, 0x8)
    OP_43(0x1B, 0x1, 0x0, 0x9)
    OP_43(0x1C, 0x1, 0x0, 0xA)
    OP_43(0x1D, 0x1, 0x0, 0xB)

    def lambda_12FE():
        OP_6D(-25630, 0, -32509, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12FE)

    def lambda_1316():
        OP_67(0, 4600, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1316)

    def lambda_132E():
        OP_6B(4000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_132E)

    def lambda_133E():
        OP_6C(168000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_133E)

    def lambda_134E():
        OP_6E(347, 7000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_134E)
    Sleep(9000)
    Fade(500)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    OP_0D()
    OP_A2(0x0)

    ChrTalk(    #9
        0x8,
        "#7PCease fire!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 21)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x8, 1)
    Sleep(200)
    OP_0D()

    ChrTalk(    #10
        0x8,
        (
            "#7PAll squads, FORWARD! Do not let a\x01",
            "single one of these things into the city!\x01",
            "FOR THE QUEEN! FOR LIBERL!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #11
        "\x07\x00#5SFOR LIBERL!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x9, 0x1, 0x0, 0x10)
    Sleep(10)
    OP_43(0xC, 0x1, 0x0, 0x11)
    Sleep(10)
    OP_43(0xF, 0x1, 0x0, 0x12)
    Sleep(10)
    OP_43(0x12, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x10)
    Sleep(10)
    OP_43(0xD, 0x1, 0x0, 0x11)
    Sleep(10)
    OP_43(0x10, 0x1, 0x0, 0x12)
    Sleep(10)
    OP_43(0x13, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x10)
    Sleep(10)
    OP_43(0xE, 0x1, 0x0, 0x11)
    Sleep(10)
    OP_43(0x11, 0x1, 0x0, 0x12)
    Sleep(10)
    OP_43(0x14, 0x1, 0x0, 0x13)
    Sleep(1000)
    OP_A2(0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_BA8 end

    def Function_5_1547(): pass

    label("Function_5_1547")

    Sleep(150)
    OP_22(0x13A, 0x0, 0x1E)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x23)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x28)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x2D)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x32)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x37)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x3C)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x41)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x46)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x4B)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)

    label("loc_1600")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1613")
    Jump("loc_1628")

    label("loc_1613")

    OP_22(0x13A, 0x0, 0x50)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    Jump("loc_1600")

    label("loc_1628")

    OP_22(0x13A, 0x0, 0x46)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x3C)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x32)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x28)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x1E)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    OP_22(0x13A, 0x0, 0x14)
    Sleep(200)
    OP_23(0x13A)
    Sleep(180)
    Return()

    # Function_5_1547 end

    def Function_6_1695(): pass

    label("Function_6_1695")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x5DC, 0x0, 0x1D4C, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFA0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_6_1695 end

    def Function_7_17B7(): pass

    label("Function_7_17B7")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x5DC, 0x0, 0x1770, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFA0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_7_17B7 end

    def Function_8_18D9(): pass

    label("Function_8_18D9")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0x1B58, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFA0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_8_18D9 end

    def Function_9_19FB(): pass

    label("Function_9_19FB")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0x1388, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0xFA0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_9_19FB end

    def Function_10_1B1D(): pass

    label("Function_10_1B1D")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_10_1B1D end

    def Function_11_1C3F(): pass

    label("Function_11_1C3F")

    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0xBB8, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_90(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_11_1C3F end

    def Function_12_1D61(): pass

    label("Function_12_1D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE0")
    PlayEffect(0x0, 0xFF, 0xFF, -26480, 1250, 30810, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFF, -26480, 1000, 30810, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("Function_12_1D61")

    label("loc_1DE0")

    Return()

    # Function_12_1D61 end

    def Function_13_1DE1(): pass

    label("Function_13_1DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E60")
    PlayEffect(0x0, 0xFF, 0xFF, -33230, 1250, 28840, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFF, -33230, 1000, 28840, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("Function_13_1DE1")

    label("loc_1E60")

    Return()

    # Function_13_1DE1 end

    def Function_14_1E61(): pass

    label("Function_14_1E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE0")
    PlayEffect(0x0, 0xFF, 0xFF, -21710, 1250, 23210, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFF, -21710, 1000, 23210, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("Function_14_1E61")

    label("loc_1EE0")

    Return()

    # Function_14_1E61 end

    def Function_15_1EE1(): pass

    label("Function_15_1EE1")

    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1C, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1E, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x18, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1D, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1E, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x22, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1B, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x21, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x1E, 0, 0, 0, 0)
    Return()

    # Function_15_1EE1 end

    def Function_16_2AA5(): pass

    label("Function_16_2AA5")

    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0xFFFF9B88, 0x0, 0x64A0, 0x1770, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
    Return()

    # Function_16_2AA5 end

    def Function_17_2AD3(): pass

    label("Function_17_2AD3")

    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0xFFFF9552, 0xA, 0x643C, 0x1770, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
    Return()

    # Function_17_2AD3 end

    def Function_18_2B01(): pass

    label("Function_18_2B01")

    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0xFFFFA22C, 0xFFFFFFEC, 0x709E, 0x1770, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
    Return()

    # Function_18_2B01 end

    def Function_19_2B2F(): pass

    label("Function_19_2B2F")

    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0xFFFF8D5A, 0xFFFFFFCE, 0x4B82, 0x1770, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1770, 0x0)
    Return()

    # Function_19_2B2F end

    def Function_20_2B5D(): pass

    label("Function_20_2B5D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x05North: City of Zeiss\x01",
            "South: Elmo Village - 165 selge     Wolf Fort - 280 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_2B5D end

    def Function_21_2BDE(): pass

    label("Function_21_2BDE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05South: Elmo Village - 130 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_2BDE end

    def Function_22_2C30(): pass

    label("Function_22_2C30")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05North: City of Zeiss\x01",
            "East: Wolf Fort - 245 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_2C30 end

    SaveToFile()

Try(main)
