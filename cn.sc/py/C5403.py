from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5403   ._SN',
        MapName             = 'Other',
        Location            = 'C5403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '',                                     # 9
        '基尔巴特',                             # 10
        '暴动钢臂（白）',                       # 11
        '暴动钢臂（白）',                       # 12
        '目标探索者',                           # 13
        '哨兵570（蓝）',                        # 14
        '哨兵235（红）',                        # 15
        '目标探索者',                           # 16
        '目标探索者',                           # 17
        '哨兵570（蓝）',                        # 18
        '哨兵235（红）',                        # 19
        '目标探索者',                           # 20
        '据点武装者',                           # 21
        '据点武装者',                           # 22
        '据点武装者',                           # 23
        '据点武装者',                           # 24
        '目标探索者',                           # 25
        '哨兵570（蓝）',                        # 26
        '哨兵235（红）',                        # 27
        '目标探索者',                           # 28
        '目标探索者',                           # 29
        '哨兵570（蓝）',                        # 30
        '哨兵235（红）',                        # 31
        '目标探索者',                           # 32
        '据点武装者',                           # 33
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12350 ._CH',             # 02
        'ED6_DT29/CH12351 ._CH',             # 03
        'ED6_DT26/CH20255 ._CH',             # 04
        'ED6_DT26/CH20255 ._CH',             # 05
        'ED6_DT29/CH12310 ._CH',             # 06
        'ED6_DT29/CH12310 ._CH',             # 07
        'ED6_DT29/CH12320 ._CH',             # 08
        'ED6_DT29/CH12321 ._CH',             # 09
        'ED6_DT27/CH03750 ._CH',             # 0A
        'ED6_DT29/CH12530 ._CH',             # 0B
        'ED6_DT29/CH12531 ._CH',             # 0C
        'ED6_DT26/CH20501 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT26/CH20255P._CP',             # 04
        'ED6_DT26/CH20255P._CP',             # 05
        'ED6_DT29/CH12310P._CP',             # 06
        'ED6_DT29/CH12310P._CP',             # 07
        'ED6_DT29/CH12320P._CP',             # 08
        'ED6_DT29/CH12321P._CP',             # 09
        'ED6_DT27/CH03750P._CP',             # 0A
        'ED6_DT29/CH12530P._CP',             # 0B
        'ED6_DT29/CH12531P._CP',             # 0C
        'ED6_DT26/CH20501P._CP',             # 0D
    )

    DeclNpc(
        X                   = 35060,
        Z                   = 2000,
        Y                   = -35010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 34000,
        Z                   = 1000,
        Y                   = -76880,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = -27100,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = 27210,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32040,
        Z                   = 1000,
        Y                   = 116120,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34140,
        Z                   = 1000,
        Y                   = 116640,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87240,
        Z                   = 0,
        Y                   = 27500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86970,
        Z                   = 0,
        Y                   = -24730,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33900,
        Z                   = 1000,
        Y                   = -75690,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -830,
        Z                   = 0,
        Y                   = -16890,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -940,
        Z                   = 0,
        Y                   = 8910,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -910,
        Z                   = 0,
        Y                   = -28570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34000,
        Z                   = 1000,
        Y                   = -76880,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = -27100,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = 27210,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32040,
        Z                   = 1000,
        Y                   = 116120,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34140,
        Z                   = 1000,
        Y                   = 116640,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87240,
        Z                   = 0,
        Y                   = 27500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86970,
        Z                   = 0,
        Y                   = -24730,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33900,
        Z                   = 1000,
        Y                   = -75690,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = -1000,
        Z                   = 82020,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -6200,
        Y                   = -1000,
        Z                   = -27740,
        Range               = 4700,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF978C,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -5910,
        Y                   = -1000,
        Z                   = 31010,
        Range               = 3950,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x695A,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -5690,
        Y                   = -1000,
        Z                   = -32460,
        Range               = 4110,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6E2E,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 80120,
        Y                   = -1000,
        Z                   = -36990,
        Range               = 84020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6000,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 80070,
        Y                   = -1000,
        Z                   = 8600,
        Range               = 83680,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x12AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = -127880,
        Y                   = -1000,
        Z                   = 10750,
        Range               = -124230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1AFE,
        Unknown_18          = 0x0,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = -88820,
        Y                   = -1000,
        Z                   = 10590,
        Range               = -84910,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1B6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )


    DeclActor(
        TriggerX            = -42690,
        TriggerZ            = 0,
        TriggerY            = -31970,
        TriggerRange        = 1000,
        ActorX              = -42030,
        ActorZ              = 0,
        ActorY              = -31970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35680,
        TriggerZ            = 0,
        TriggerY            = -35010,
        TriggerRange        = 1000,
        ActorX              = 35060,
        ActorZ              = 0,
        ActorY              = -35010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3580,
        TriggerZ            = 0,
        TriggerY            = 79630,
        TriggerRange        = 1000,
        ActorX              = 3580,
        ActorZ              = 1000,
        ActorY              = 79630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41170,
        TriggerZ            = 0,
        TriggerY            = 60740,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 60890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41200,
        TriggerZ            = 0,
        TriggerY            = 59640,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 59710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41220,
        TriggerZ            = 0,
        TriggerY            = 58190,
        TriggerRange        = 1000,
        ActorX              = 41930,
        ActorZ              = 1000,
        ActorY              = 58370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41190,
        TriggerZ            = 0,
        TriggerY            = 56900,
        TriggerRange        = 1000,
        ActorX              = 42060,
        ActorZ              = 1000,
        ActorY              = 57120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38140,
        TriggerZ            = 0,
        TriggerY            = 62850,
        TriggerRange        = 1000,
        ActorX              = 38130,
        ActorZ              = 1000,
        ActorY              = 63510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38390,
        TriggerZ            = 0,
        TriggerY            = 55260,
        TriggerRange        = 1000,
        ActorX              = 38380,
        ActorZ              = 1000,
        ActorY              = 54650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 15510,
        TriggerRange        = 1000,
        ActorX              = 42260,
        ActorZ              = 0,
        ActorY              = 15480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 12030,
        TriggerRange        = 1000,
        ActorX              = 42210,
        ActorZ              = 0,
        ActorY              = 11950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41590,
        TriggerZ            = 0,
        TriggerY            = 8540,
        TriggerRange        = 1000,
        ActorX              = 42300,
        ActorZ              = 0,
        ActorY              = 8510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43620,
        TriggerZ            = 0,
        TriggerY            = 17790,
        TriggerRange        = 1000,
        ActorX              = -43660,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39950,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -39990,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36240,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -36280,
        ActorZ              = 0,
        ActorY              = 18510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4960,
        TriggerZ            = 0,
        TriggerY            = 77000,
        TriggerRange        = 1000,
        ActorX              = 4960,
        ActorZ              = 1000,
        ActorY              = 77000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_726",          # 00, 0
        "Function_1_758",          # 01, 1
        "Function_2_B5E",          # 02, 2
        "Function_3_B74",          # 03, 3
        "Function_4_C8B",          # 04, 4
        "Function_5_E5B",          # 05, 5
        "Function_6_F72",          # 06, 6
        "Function_7_1089",         # 07, 7
        "Function_8_11A0",         # 08, 8
        "Function_9_12B7",         # 09, 9
        "Function_10_13CE",        # 0A, 10
        "Function_11_1521",        # 0B, 11
        "Function_12_1638",        # 0C, 12
        "Function_13_174F",        # 0D, 13
        "Function_14_1866",        # 0E, 14
        "Function_15_197D",        # 0F, 15
        "Function_16_1A94",        # 10, 16
        "Function_17_1BAB",        # 11, 17
        "Function_18_1BC4",        # 12, 18
        "Function_19_1BDA",        # 13, 19
        "Function_20_2CB5",        # 14, 20
        "Function_21_363A",        # 15, 21
        "Function_22_3650",        # 16, 22
        "Function_23_3666",        # 17, 23
        "Function_24_3684",        # 18, 24
        "Function_25_36B9",        # 19, 25
        "Function_26_36CE",        # 1A, 26
        "Function_27_3755",        # 1B, 27
        "Function_28_3965",        # 1C, 28
        "Function_29_3BB7",        # 1D, 29
        "Function_30_3BF8",        # 1E, 30
        "Function_31_3C39",        # 1F, 31
        "Function_32_3C7A",        # 20, 32
        "Function_33_3CBB",        # 21, 33
        "Function_34_3CFC",        # 22, 34
        "Function_35_3D3D",        # 23, 35
        "Function_36_3DCE",        # 24, 36
    )


    def Function_0_726(): pass

    label("Function_0_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_END)), "loc_757")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1950, 0, -22900, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 5)

    label("loc_757")

    Return()

    # Function_0_726 end

    def Function_1_758(): pass

    label("Function_1_758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_788")
    OP_6F(0x24, 0)
    Jump("loc_78F")

    label("loc_788")

    OP_6F(0x24, 60)

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A1")
    OP_6F(0x25, 0)
    Jump("loc_7A8")

    label("loc_7A1")

    OP_6F(0x25, 60)

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA")
    OP_6F(0x29, 0)
    Jump("loc_7C1")

    label("loc_7BA")

    OP_6F(0x29, 60)

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D3")
    OP_6F(0x2A, 0)
    Jump("loc_7DA")

    label("loc_7D3")

    OP_6F(0x2A, 60)

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC")
    OP_6F(0x2B, 0)
    Jump("loc_7F3")

    label("loc_7EC")

    OP_6F(0x2B, 60)

    label("loc_7F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_805")
    OP_6F(0x2C, 0)
    Jump("loc_80C")

    label("loc_805")

    OP_6F(0x2C, 60)

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81E")
    OP_6F(0x2D, 0)
    Jump("loc_825")

    label("loc_81E")

    OP_6F(0x2D, 60)

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_837")
    OP_6F(0x2E, 0)
    Jump("loc_83E")

    label("loc_837")

    OP_6F(0x2E, 60)

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_6F(0x2F, 0)
    Jump("loc_857")

    label("loc_850")

    OP_6F(0x2F, 60)

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_869")
    OP_6F(0x30, 0)
    Jump("loc_870")

    label("loc_869")

    OP_6F(0x30, 60)

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_882")
    OP_6F(0x31, 0)
    Jump("loc_889")

    label("loc_882")

    OP_6F(0x31, 60)

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89B")
    OP_6F(0x32, 0)
    Jump("loc_8A2")

    label("loc_89B")

    OP_6F(0x32, 60)

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4")
    OP_6F(0x33, 0)
    Jump("loc_8BB")

    label("loc_8B4")

    OP_6F(0x33, 60)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD")
    OP_6F(0x34, 0)
    Jump("loc_8D4")

    label("loc_8CD")

    OP_6F(0x34, 60)

    label("loc_8D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_929")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1200, 79630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_929")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AB")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    Jump("loc_9D8")

    label("loc_9AB")

    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)

    label("loc_9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6C")
    OP_72(0x17, 0x10)
    OP_6F(0x2, 100)
    OP_6F(0x4, 100)
    OP_6F(0x5, 100)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x17, 0x80)
    Jump("loc_A6C")

    label("loc_A6C")

    Call(0, 28)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x434), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D")
    OP_D2(0x2703A8, 0x2703B2, 0xE)
    OP_D2(0x2703AC, 0x2703B6, 0xF)
    OP_D2(0x2703AE, 0x2703B8, 0x10)
    OP_D2(0x26020B, 0x260210, 0x11)
    OP_D2(0x290216, 0x29021A, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270130, 0x270140, 0x14)
    OP_D2(0x702B4, 0x702BB, 0x15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_B02"),
        (3, "loc_B0F"),
        (4, "loc_B1C"),
        (5, "loc_B29"),
        (6, "loc_B36"),
        (7, "loc_B43"),
        (8, "loc_B50"),
        (SWITCH_DEFAULT, "loc_B5D"),
    )


    label("loc_B02")

    OP_D2(0x701D0, 0x701DC, 0x16)
    Jump("loc_B5D")

    label("loc_B0F")

    OP_D2(0x701E8, 0x701F4, 0x16)
    Jump("loc_B5D")

    label("loc_B1C")

    OP_D2(0x27036E, 0x27037B, 0x16)
    Jump("loc_B5D")

    label("loc_B29")

    OP_D2(0x70218, 0x70224, 0x16)
    Jump("loc_B5D")

    label("loc_B36")

    OP_D2(0x70230, 0x7023C, 0x16)
    Jump("loc_B5D")

    label("loc_B43")

    OP_D2(0x70248, 0x70254, 0x16)
    Jump("loc_B5D")

    label("loc_B50")

    OP_D2(0x270176, 0x270183, 0x16)
    Jump("loc_B5D")

    label("loc_B5D")

    Return()

    # Function_1_758 end

    def Function_2_B5E(): pass

    label("Function_2_B5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B73")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_B5E")

    label("loc_B73")

    Return()

    # Function_2_B5E end

    def Function_3_B74(): pass

    label("Function_3_B74")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x185, 1)"), scpexpr(EXPR_END)), "loc_BE3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x85\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D36)
    Jump("loc_C49")

    label("loc_BE3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x85\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x85\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_C49")

    Jump("loc_C7D")

    label("loc_C4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C7D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B74 end

    def Function_4_C8B(): pass

    label("Function_4_C8B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6A")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CDD():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CDD)

    def lambda_CF8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CF8)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #3
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x42C, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D45"),
        (2, "loc_D57"),
        (1, "loc_D67"),
        (SWITCH_DEFAULT, "loc_D6A"),
    )


    label("loc_D45")

    OP_A2(0x1D38)
    OP_6F(0x25, 60)
    Sleep(500)
    Jump("loc_D6A")

    label("loc_D57")

    OP_6F(0x25, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D67")

    OP_B4(0x0)
    Return()

    label("loc_D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19, 1)"), scpexpr(EXPR_END)), "loc_DB9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x19\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D37)
    Jump("loc_E1B")

    label("loc_DB9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x19\x00\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x19\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_E1B")

    Jump("loc_E4D")

    label("loc_E1E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C8B end

    def Function_5_E5B(): pass

    label("Function_5_E5B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F33")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_ECA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3D)
    Jump("loc_F30")

    label("loc_ECA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_F30")

    Jump("loc_F64")

    label("loc_F33")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F64")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E5B end

    def Function_6_F72(): pass

    label("Function_6_F72")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x166, 1)"), scpexpr(EXPR_END)), "loc_FE1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x66\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3E)
    Jump("loc_1047")

    label("loc_FE1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\x66\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x66\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_1047")

    Jump("loc_107B")

    label("loc_104A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_107B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F72 end

    def Function_7_1089(): pass

    label("Function_7_1089")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1161")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_10F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3F)
    Jump("loc_115E")

    label("loc_10F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_115E")

    Jump("loc_1192")

    label("loc_1161")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1192")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1089 end

    def Function_8_11A0(): pass

    label("Function_8_11A0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1278")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_120F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D40)
    Jump("loc_1275")

    label("loc_120F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_1275")

    Jump("loc_12A9")

    label("loc_1278")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12A9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_11A0 end

    def Function_9_12B7(): pass

    label("Function_9_12B7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1326")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D41)
    Jump("loc_138C")

    label("loc_1326")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2D, 60)
    OP_70(0x2D, 0x0)

    label("loc_138C")

    Jump("loc_13C0")

    label("loc_138F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_12B7 end

    def Function_10_13CE(): pass

    label("Function_10_13CE")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x1E)
    OP_73(0x2E)
    OP_6F(0x2E, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D42)
    Jump("loc_150F")

    label("loc_14F5")


    AnonymousTalk(    #23
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_150F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_13CE end

    def Function_11_1521(): pass

    label("Function_11_1521")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1590")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D43)
    Jump("loc_15F6")

    label("loc_1590")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_15F6")

    Jump("loc_162A")

    label("loc_15F9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_162A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1521 end

    def Function_12_1638(): pass

    label("Function_12_1638")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1710")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x30, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x170, 1)"), scpexpr(EXPR_END)), "loc_16A7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\x70\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D44)
    Jump("loc_170D")

    label("loc_16A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "宝箱里装有\x1F\x70\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x70\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x30, 60)
    OP_70(0x30, 0x0)

    label("loc_170D")

    Jump("loc_1741")

    label("loc_1710")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1741")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1638 end

    def Function_13_174F(): pass

    label("Function_13_174F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1827")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x31, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_17BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D46)
    Jump("loc_1824")

    label("loc_17BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x31, 60)
    OP_70(0x31, 0x0)

    label("loc_1824")

    Jump("loc_1858")

    label("loc_1827")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1858")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_174F end

    def Function_14_1866(): pass

    label("Function_14_1866")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x32, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_18D5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D47)
    Jump("loc_193B")

    label("loc_18D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x32, 60)
    OP_70(0x32, 0x0)

    label("loc_193B")

    Jump("loc_196F")

    label("loc_193E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_196F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1866 end

    def Function_15_197D(): pass

    label("Function_15_197D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A55")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x33, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_19EC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D48)
    Jump("loc_1A52")

    label("loc_19EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x33, 60)
    OP_70(0x33, 0x0)

    label("loc_1A52")

    Jump("loc_1A86")

    label("loc_1A55")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A86")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_197D end

    def Function_16_1A94(): pass

    label("Function_16_1A94")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_1B03")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D49)
    Jump("loc_1B69")

    label("loc_1B03")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x05\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_1B69")

    Jump("loc_1B9D")

    label("loc_1B6C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1B9D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1A94 end

    def Function_17_1BAB(): pass

    label("Function_17_1BAB")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A2(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_17_1BAB end

    def Function_18_1BC4(): pass

    label("Function_18_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BD1")
    Return()

    label("loc_1BD1")

    Call(0, 19)
    Call(0, 20)
    Return()

    # Function_18_1BC4 end

    def Function_19_1BDA(): pass

    label("Function_19_1BDA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BFF")
    Call(0, 26)
    Call(0, 35)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1BFF")

    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C97")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CD5")

    label("loc_1C97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CBE")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1CD5")

    label("loc_1CBE")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1CD5")

    Sleep(1000)

    def lambda_1CE0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CE0)
    Sleep(50)

    def lambda_1CF3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF3)
    Sleep(50)

    def lambda_1D06():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1D06)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    SetChrFlags(0x20, 0x80)
    Fade(500)
    OP_D2(0x2703A8, 0x2703B2, 0xE)
    OP_D2(0x2703AC, 0x2703B6, 0xF)
    OP_D2(0x2703AE, 0x2703B8, 0x10)
    OP_D2(0x26020B, 0x260210, 0x11)
    OP_D2(0x290216, 0x29021A, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270130, 0x270140, 0x14)
    OP_D2(0x702B4, 0x702BB, 0x15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1D99"),
        (3, "loc_1DA6"),
        (4, "loc_1DB3"),
        (5, "loc_1DC0"),
        (6, "loc_1DCD"),
        (7, "loc_1DDA"),
        (8, "loc_1DE7"),
        (SWITCH_DEFAULT, "loc_1DF4"),
    )


    label("loc_1D99")

    OP_D2(0x701D0, 0x701DC, 0x16)
    Jump("loc_1DF4")

    label("loc_1DA6")

    OP_D2(0x701E8, 0x701F4, 0x16)
    Jump("loc_1DF4")

    label("loc_1DB3")

    OP_D2(0x27036E, 0x27037B, 0x16)
    Jump("loc_1DF4")

    label("loc_1DC0")

    OP_D2(0x70218, 0x70224, 0x16)
    Jump("loc_1DF4")

    label("loc_1DCD")

    OP_D2(0x70230, 0x7023C, 0x16)
    Jump("loc_1DF4")

    label("loc_1DDA")

    OP_D2(0x70248, 0x70254, 0x16)
    Jump("loc_1DF4")

    label("loc_1DE7")

    OP_D2(0x270176, 0x270183, 0x16)
    Jump("loc_1DF4")

    label("loc_1DF4")

    OP_6D(150, 0, -28510, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    SetChrPos(0x101, -1540, 0, -27810, 180)
    SetChrPos(0x102, -120, 0, -27830, 180)
    SetChrPos(0x10B, -1860, 0, -29380, 180)
    SetChrPos(0xF9, -350, 0, -29430, 180)
    SetChrPos(0x9, -950, 0, -12970, 180)
    OP_0D()

    ChrTalk(    #42
        0x10B,
        "#216F#5P什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1020F#5P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x9,
        "青年的声音",
        (
            "#4P呼呼……\x01",
            "终于抓到你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA8")

    label("loc_1F6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F91")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FA8")

    label("loc_1F91")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FA8")

    Sleep(1000)

    def lambda_1FB3():
        OP_6D(-10, 0, -23700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB3)

    def lambda_1FCB():
        OP_67(0, 4680, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FCB)

    def lambda_1FE3():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FE3)

    def lambda_1FF3():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1FF3)

    def lambda_2003():
        OP_6E(357, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_2003)
    ClearChrFlags(0x9, 0x80)

    def lambda_2018():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xFFFFB3A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2018)

    def lambda_2033():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2033)
    Sleep(50)

    def lambda_2046():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2046)
    Sleep(80)

    def lambda_2059():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2059)
    Sleep(70)

    def lambda_206C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_206C)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x101,
        "#1005F#6P基、基尔巴特！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20DB")

    ChrTalk(    #46
        0x105,
        "#1164F#4P呀……前辈？\x02",
    )

    CloseMessageWindow()

    label("loc_20DB")


    ChrTalk(    #47
        0x102,
        "#1042F#2P……你在舰内啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#1226F#5P哎呀哎呀……\x01",
            "听说有人侵入舰艇，\x01",
            "我还在想是怎样的蠢货……\x02\x03",

            "#1221F果然是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10B,
        (
            "#213F#6P咦……\x02\x03",

            "……我说这家伙，\x01",
            "是你们认识的人吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233A")

    ChrTalk(    #50
        0x105,
        (
            "#1163F#2P嗯嗯……\x01",
            "是王立学院的前辈……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2280")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇做了王立学院解放任务（８章）】\x01",      # 0
            "【◇没做王立学院解放任务（８章）】\x01",      # 1
            "【◇什么也没有变更】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2274"),
        (1, "loc_227A"),
        (SWITCH_DEFAULT, "loc_2280"),
    )


    label("loc_2274")

    OP_A2(0x202F)
    Jump("loc_2280")

    label("loc_227A")

    OP_A3(0x202F)
    Jump("loc_2280")

    label("loc_2280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_22FB")

    ChrTalk(    #51
        0x101,
        (
            "#1007F#5P当他袭击学院的时候，\x01",
            "就已经失去前辈的资格啦。\x02\x03",

            "#1019F他是渎职市长的前党羽，\x01",
            "以前曾经被我们抓住……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2337")

    label("loc_22FB")


    ChrTalk(    #52
        0x101,
        (
            "#1019F#5P他是渎职市长的前党羽，\x01",
            "以前曾经被我们抓住……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    Jump("loc_238A")

    label("loc_233A")


    ChrTalk(    #53
        0x101,
        (
            "#1007F#5P嗯，算是吧。\x02\x03",

            "#1019F他是渎职市长的前党羽，\x01",
            "以前曾经被我们抓住……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238A")


    ChrTalk(    #54
        0x102,
        (
            "#1035F#5P后来在政变时趁乱逃走，\x01",
            "似乎已经投靠结社了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10B,
        (
            "#211F#6P啊哈哈，果然是这样。\x02\x03",

            "#210F是和我们一样\x01",
            "被关在雷斯顿要塞地下\x01",
            "的市长秘书对吧？\x02\x03",

            "不断哭喊着『我是无辜的！』，\x01",
            "所以我一直记得很清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #56
        0x9,
        "#1224F#5P什……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A4")

    ChrTalk(    #57
        0x105,
        "#1164F嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_24A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CB")

    ChrTalk(    #58
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_24CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(    #59
        0x104,
        (
            "#031F哈哈哈。\x01",
            "冲击性的事实曝光了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #60
        0x103,
        "#025F真丢脸……\x02",
    )

    CloseMessageWindow()

    label("loc_2526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254D")

    ChrTalk(    #61
        0x106,
        "#053F……太没用了。\x02",
    )

    CloseMessageWindow()

    label("loc_254D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A7")

    ChrTalk(    #62
        0x109,
        (
            "#1068F#2P我说小姑娘……\x02\x03",

            "#1066F这种时候\x01",
            "装作互不相识\x01",
            "是人之常情吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25FB")

    label("loc_25A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25FB")

    ChrTalk(    #63
        0x108,
        (
            "#075F#2P喂喂，小姑娘。\x02\x03",

            "#070F这种时候装作\x01",
            "互不相识是人之常情吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FB")


    ChrTalk(    #64
        0x101,
        (
            "#1025F#6P唔，嗯……\x02\x03",

            "#1016F算了，没必要\x01",
            "这么在意了吧？\x02\x03",

            "只有积累这样可耻的经验，\x01",
            "人才会不断成长……\x02\x03",

            "#1013F……不过看你现在这副狼狈样，\x01",
            "似乎完全都没有累积什么经验嘛……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x102,
        (
            "#1048F#2P……艾丝蒂尔。\x01",
            "你也太不给人家留面子了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(300)

    ChrTalk(    #66
        0x9,
        (
            "#1222F#5P你、你、你们，\x01",
            "到底要把我戏耍到何种地步……\x02\x03",

            "#1226F好吧……\x01",
            "我再也不会手下留情了……\x02\x03",

            "#1225F我新·基尔巴特的力量，\x01",
            "你们就好好见识一下吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 16)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -990, 800, 49890, 180)
    OP_43(0xA, 0x0, 0x0, 0x15)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)

    def lambda_2805():
        OP_69(0xA, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2805)

    def lambda_2813():
        OP_67(0, 2000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2813)

    def lambda_282B():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_282B)

    def lambda_283B():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_283B)

    def lambda_284B():
        OP_6E(380, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_284B)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x9, -10, 0, -19000, 180)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x101, -7820, 0, -30050, 0)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(900)
    OP_43(0x9, 0x3, 0x0, 0x18)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 12)

    def lambda_28B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_28B5)

    def lambda_28C7():
        OP_8F(0xFE, 0xFFFFF79A, 0x320, 0xFFFFFFE2, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_28C7)
    Sleep(1200)
    Fade(500)
    OP_69(0xA, 0x0)
    OP_6A(0xA)
    OP_67(0, 2500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(24000, 0)
    OP_6E(380, 0)

    def lambda_2922():
        OP_67(0, 3000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2922)

    def lambda_293A():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_293A)

    def lambda_294A():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_294A)
    WaitChrThread(0xA, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_6A(0xFF)
    OP_44(0x9, 0x3)
    OP_23(0x13F)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_297A():
        OP_96(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFD9A4, 0x1388, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_297A)
    Sleep(100)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2150, 800, -19000, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_29F7():
        OP_96(0xFE, 0xFFFFF79A, 0x320, 0xFFFFB5C8, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_29F7)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 11)
    OP_44(0xA, 0x0)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x1388, 0x1F4)
    Sleep(500)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_22(0x193, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #67
        0x101,
        "#1020F#1P！！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(400, 0, -22850, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(44000, 0)
    OP_6E(380, 0)
    SetChrPos(0x101, -1540, 0, -27810, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 20)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10B, 21)
    SetChrSubChip(0x10B, 0)
    SetChrChipByIndex(0xF9, 22)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #68
        0x10B,
        "#216F#6P什、什什什什！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1020F#6P机、机械装置的狮子！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#1042F#2P『十三工房』的新型吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#1221F#5P哈哈哈，这是狮子型人形兵器，\x01",
            "『暴动钢臂』！\x02\x03",

            "面对它惊人的性能，\x01",
            "你们就尽情地颤抖吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)
    Sleep(1200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2BEB():
        OP_6D(-210, 0, -25930, 700)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BEB)

    def lambda_2C03():
        OP_67(0, 6180, -10000, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C03)

    def lambda_2C1B():
        OP_6B(2020, 700)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C1B)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 12)
    OP_43(0xA, 0x0, 0x0, 0x15)
    OP_43(0xA, 0x3, 0x0, 0x19)
    OP_8F(0xA, 0xFFFFFC04, 0x320, 0xFFFFA79A, 0x2710, 0x0)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2C5C():
        OP_96(0xFE, 0xFFFFFCA4, 0x0, 0xFFFF92A0, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C5C)
    OP_44(0xA, 0x0)
    SetChrChipByIndex(0xA, 18)

    def lambda_2C83():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2C83)
    WaitChrThread(0x101, 0x1)
    OP_44(0xA, 0xFF)
    Battle(0x434, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2CAF"),
        (SWITCH_DEFAULT, "loc_2CB4"),
    )


    label("loc_2CAF")

    OP_B4(0x0)
    Jump("loc_2CB4")

    label("loc_2CB4")

    Return()

    # Function_19_1BDA end

    def Function_20_2CB5(): pass

    label("Function_20_2CB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_44(0xA, 0x1)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_6D(-480, 0, -22740, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2170, 0, -25140, 0)
    SetChrPos(0x102, -910, 0, -25200, 0)
    SetChrPos(0x10B, -2630, 0, -26440, 0)
    SetChrPos(0xF9, -1200, 0, -26530, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1620, 0, -22000, 180)
    SetChrChipByIndex(0x9, 15)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10B, 65535)
    SetChrChipByIndex(0xF9, 65535)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x9,
        (
            "#1224F#5P不、不可能……\x02\x03",

            "我居然……\x01",
            "我新·基尔巴特居然会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015F#6P那、那个～打扰一下？\x02\x03",

            "那东西…确实比以前的人形兵器\x01",
            "要强上许多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10B,
        (
            "#413F#6P不过，这并不代表\x01",
            "你本身变强了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#1224F#5P咦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(    #76
        0x105,
        (
            "#1165F确实啊，加个『新』字，\x01",
            "结果一点变化都没有……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F08")

    ChrTalk(    #77
        0x107,
        (
            "#067F确、确实，只是加个『新』字，\x01",
            "但一点进步都没有……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_2F08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(    #78
        0x109,
        (
            "#1068F确实啊，只是加个『新』字而已，\x01",
            "根本就没有一点进步嘛。\x02\x03",

            "#1060F这就是所谓的虚张声势吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_2F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FDE")

    ChrTalk(    #79
        0x103,
        (
            "#025F确实，加个『新』字，\x01",
            "结果一点进步都没有。\x02\x03",

            "#524F男人的虚荣心真是可悲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_2FDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3035")

    ChrTalk(    #80
        0x104,
        (
            "#035F呼，这么没用还敢加个『新』字。\x02\x03",

            "#037F这就是所谓的虚荣心吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_3035")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308A")

    ChrTalk(    #81
        0x106,
        (
            "#551F切……\x01",
            "什么『新』。\x02\x03",

            "#555F是男人就靠\x01",
            "自己的双手来战斗吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F5")

    label("loc_308A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F5")

    ChrTalk(    #82
        0x108,
        (
            "#074F唔，确实，虽然加了个『新』字，\x01",
            "但一点长进都没有啊。\x02\x03",

            "#070F这就是年轻人的虚荣心吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F5")


    ChrTalk(    #83
        0x9,
        "#1228F#5P……（语塞）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0x9, -1950, 0, -22900, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #84
        0x101,
        "#1004F#6P啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10B,
        "#213F#6P咦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3192")

    ChrTalk(    #86
        0x105,
        "#1164F嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_3192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B8")

    ChrTalk(    #87
        0x107,
        "#065F啊哇哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_31B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DD")

    ChrTalk(    #88
        0x109,
        "#1064F哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_31DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31FF")

    ChrTalk(    #89
        0x103,
        "#023F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_31FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3223")

    ChrTalk(    #90
        0x104,
        "#033F哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_3223")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3245")

    ChrTalk(    #91
        0x106,
        "#052F喔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3264")

    label("loc_3245")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3264")

    ChrTalk(    #92
        0x108,
        "#073F喂……\x02",
    )

    CloseMessageWindow()

    label("loc_3264")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CB")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_32FF")

    label("loc_32CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32ED")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_32FF")

    label("loc_32ED")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_32FF")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x10B)
    OP_63(0xF9)
    Sleep(500)

    def lambda_331B():
        OP_6D(-1450, 0, -25300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_331B)

    def lambda_3333():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3333)
    Sleep(50)

    def lambda_3346():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3346)
    Sleep(50)

    def lambda_3359():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_3359)
    Sleep(50)

    def lambda_336C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_336C)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #93
        0x101,
        (
            "#1016F#5P好，好～了。\x01",
            "赶快返回牢房吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33E0")

    ChrTalk(    #94
        0x105,
        "#1165F是、是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_33E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3406")

    ChrTalk(    #95
        0x107,
        "#067F是，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_3406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3431")

    ChrTalk(    #96
        0x109,
        "#1066F啊哈哈，是呀～\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_3431")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3459")

    ChrTalk(    #97
        0x103,
        "#021F是，是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_3459")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347F")

    ChrTalk(    #98
        0x104,
        "#031F呼，赞成。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_347F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A5")

    ChrTalk(    #99
        0x106,
        "#551F……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C8")

    label("loc_34A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C8")

    ChrTalk(    #100
        0x108,
        "#070F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_34C8")


    ChrTalk(    #101
        0x10B,
        (
            "#211F#6P嗯嗯。\x01",
            "得赶快去救大哥他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        "#1052F#5P（真是个可怜的家伙呢……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1410, 0, -25050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1410, 0, -25050, 0)
    SetChrPos(0x1, -1410, 0, -25050, 0)
    SetChrPos(0x2, -1410, 0, -25050, 0)
    SetChrPos(0x3, -1410, 0, -25050, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_71(0x17, 0x10)
    OP_6F(0x2, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_BE(0x2, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_BE(0x4, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_BE(0x5, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_A2(0x2227)
    EventEnd(0x0)
    Return()

    # Function_20_2CB5 end

    def Function_21_363A(): pass

    label("Function_21_363A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_364F")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_21_363A")

    label("loc_364F")

    Return()

    # Function_21_363A end

    def Function_22_3650(): pass

    label("Function_22_3650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3665")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_22_3650")

    label("loc_3665")

    Return()

    # Function_22_3650 end

    def Function_23_3666(): pass

    label("Function_23_3666")

    SetChrChipByIndex(0xFE, 18)
    OP_22(0x195, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_23_3666 end

    def Function_24_3684(): pass

    label("Function_24_3684")

    OP_22(0x13F, 0x0, 0x46)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(400)

    label("loc_36A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36B8")
    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    Jump("loc_36A2")

    label("loc_36B8")

    Return()

    # Function_24_3684 end

    def Function_25_36B9(): pass

    label("Function_25_36B9")

    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    Return()

    # Function_25_36B9 end

    def Function_26_36CE(): pass

    label("Function_26_36CE")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3748"),
        (1, "loc_374E"),
        (SWITCH_DEFAULT, "loc_3754"),
    )


    label("loc_3748")

    OP_A2(0x1200)
    Jump("loc_3754")

    label("loc_374E")

    OP_A2(0x1201)
    Jump("loc_3754")

    label("loc_3754")

    Return()

    # Function_26_36CE end

    def Function_27_3755(): pass

    label("Function_27_3755")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #103
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3964")

    label("loc_37A6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #104
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3949")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1000, 79630, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_70(0x28, 0x32)
    OP_73(0x28)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 3580, 1000, 79630, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1000, 79630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3949")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3963")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3963")

    Return()

    label("loc_3964")

    Return()

    # Function_27_3755 end

    def Function_28_3965(): pass

    label("Function_28_3965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3A96")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)
    OP_71(0x5, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A95")
    OP_72(0x17, 0x10)
    OP_6F(0x2, 100)
    OP_6F(0x4, 100)
    OP_6F(0x5, 100)
    OP_72(0x2, 0x2)
    OP_72(0x4, 0x2)
    OP_72(0x5, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x17, 0x80)

    label("loc_3A95")

    Return()

    label("loc_3A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 4)), scpexpr(EXPR_END)), "loc_3AC6")
    OP_6F(0x0, 100)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5310, -1000, 30410, 3470, 2000, 27560)

    label("loc_3AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 5)), scpexpr(EXPR_END)), "loc_3AF6")
    OP_6F(0x1, 100)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5210, -1000, -36500, 3470, 2000, -33500)

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 6)), scpexpr(EXPR_END)), "loc_3B26")
    OP_6F(0x2, 100)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)

    label("loc_3B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 7)), scpexpr(EXPR_END)), "loc_3B56")
    OP_6F(0x3, 100)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, 80690, -1000, 8260, 83470, 2000, 5400)

    label("loc_3B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 0)), scpexpr(EXPR_END)), "loc_3B86")
    OP_6F(0x4, 100)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)

    label("loc_3B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 1)), scpexpr(EXPR_END)), "loc_3BB6")
    OP_6F(0x5, 100)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)

    label("loc_3BB6")

    Return()

    # Function_28_3965 end

    def Function_29_3BB7(): pass

    label("Function_29_3BB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3BC4")
    Return()

    label("loc_3BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 4)), scpexpr(EXPR_END)), "loc_3BCC")
    Return()

    label("loc_3BCC")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x0)
    OP_A2(0x1C94)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_29_3BB7 end

    def Function_30_3BF8(): pass

    label("Function_30_3BF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C05")
    Return()

    label("loc_3C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 5)), scpexpr(EXPR_END)), "loc_3C0D")
    Return()

    label("loc_3C0D")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x1C95)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_30_3BF8 end

    def Function_31_3C39(): pass

    label("Function_31_3C39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C46")
    Return()

    label("loc_3C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 6)), scpexpr(EXPR_END)), "loc_3C4E")
    Return()

    label("loc_3C4E")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x1C96)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_31_3C39 end

    def Function_32_3C7A(): pass

    label("Function_32_3C7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C87")
    Return()

    label("loc_3C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 7)), scpexpr(EXPR_END)), "loc_3C8F")
    Return()

    label("loc_3C8F")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x1C97)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_32_3C7A end

    def Function_33_3CBB(): pass

    label("Function_33_3CBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3CC8")
    Return()

    label("loc_3CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 0)), scpexpr(EXPR_END)), "loc_3CD0")
    Return()

    label("loc_3CD0")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x1C98)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_33_3CBB end

    def Function_34_3CFC(): pass

    label("Function_34_3CFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3D09")
    Return()

    label("loc_3D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 1)), scpexpr(EXPR_END)), "loc_3D11")
    Return()

    label("loc_3D11")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x1C99)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_34_3CFC end

    def Function_35_3D3D(): pass

    label("Function_35_3D3D")

    FadeToDark(0, 0, -1)
    OP_6D(-27650, 0, -3680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_35_3D3D end

    def Function_36_3DCE(): pass

    label("Function_36_3DCE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240131, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_36_3DCE end

    SaveToFile()

Try(main)
