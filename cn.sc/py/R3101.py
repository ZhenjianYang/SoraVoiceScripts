from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/R3101_1 ._SN',
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
        '吸血蚊',                               # 9
        '猿羊',                                 # 10
        '猿羊',                                 # 11
        '猿羊',                                 # 12
        '猿羊',                                 # 13
        '猿羊',                                 # 14
        '猿羊',                                 # 15
        '蔡斯方向',                             # 16
        '亚尔摩村方向',                         # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT29/CH12130 ._CH',             # 0E
        'ED6_DT29/CH12131 ._CH',             # 0F
        'ED6_DT09/CH11250 ._CH',             # 10
        'ED6_DT09/CH11251 ._CH',             # 11
        'ED6_DT27/CH04000 ._CH',             # 12
        'ED6_DT27/CH04001 ._CH',             # 13
        'ED6_DT27/CH04002 ._CH',             # 14
        'ED6_DT07/CH00160 ._CH',             # 15
        'ED6_DT07/CH00161 ._CH',             # 16
        'ED6_DT09/CH10144 ._CH',             # 17
        'ED6_DT09/CH11150 ._CH',             # 18
        'ED6_DT09/CH11151 ._CH',             # 19
        'ED6_DT09/CH11154 ._CH',             # 1A
        'ED6_DT29/CH12070 ._CH',             # 1B
        'ED6_DT29/CH12071 ._CH',             # 1C
        'ED6_DT29/CH12074 ._CH',             # 1D
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
        'ED6_DT29/CH12130P._CP',             # 0E
        'ED6_DT29/CH12131P._CP',             # 0F
        'ED6_DT09/CH11250P._CP',             # 10
        'ED6_DT09/CH11251P._CP',             # 11
        'ED6_DT27/CH04000P._CP',             # 12
        'ED6_DT27/CH04001P._CP',             # 13
        'ED6_DT27/CH04002P._CP',             # 14
        'ED6_DT07/CH00160P._CP',             # 15
        'ED6_DT07/CH00161P._CP',             # 16
        'ED6_DT09/CH10144P._CP',             # 17
        'ED6_DT09/CH11150P._CP',             # 18
        'ED6_DT09/CH11151P._CP',             # 19
        'ED6_DT09/CH11154P._CP',             # 1A
        'ED6_DT29/CH12070P._CP',             # 1B
        'ED6_DT29/CH12071P._CP',             # 1C
        'ED6_DT29/CH12074P._CP',             # 1D
    )

    DeclNpc(
        X                   = -53000,
        Z                   = -70,
        Y                   = -1910,
        Direction           = 94,
        Unknown2            = 14,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33300,
        Z                   = 0,
        Y                   = -32150,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34470,
        Z                   = 0,
        Y                   = -30990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33870,
        Z                   = 0,
        Y                   = -34110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35470,
        Z                   = 0,
        Y                   = -33030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33840,
        Z                   = 10,
        Y                   = -30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33840,
        Z                   = 10,
        Y                   = -30000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
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


    DeclMonster(
        X                   = 31840,
        Z                   = -140,
        Y                   = -14910,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21310,
        Z                   = 20,
        Y                   = 1100,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6650,
        Z                   = 10,
        Y                   = 6470,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
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
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7300,
        Z                   = 80,
        Y                   = -13910,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
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
        Unknown_0E          = 10,
        Unknown_10          = 65,
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
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19200,
        Z                   = 50,
        Y                   = -40070,
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
        X                   = -2840,
        Z                   = 20,
        Y                   = -43880,
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
        X                   = -23970,
        Z                   = -60,
        Y                   = -56200,
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
        X                   = -47630,
        Z                   = 40,
        Y                   = -38230,
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
        X                   = -41100,
        Z                   = 30,
        Y                   = -42080,
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
        X                   = -46340,
        Z                   = -10,
        Y                   = -47090,
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
        X                   = -39960,
        Z                   = -50,
        Y                   = -46350,
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
        X                   = -35370,
        Z                   = 60,
        Y                   = -38180,
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
        X                   = -39680,
        Z                   = -30,
        Y                   = -43880,
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
        X                   = -31310,
        Z                   = -20,
        Y                   = -44150,
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
        X                   = -37830,
        Z                   = -40,
        Y                   = -49270,
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
        X                   = -20630,
        Z                   = -50,
        Y                   = -21460,
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
        X                   = -6340,
        Z                   = -20,
        Y                   = 12260,
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
        X                   = -9790,
        Z                   = 30,
        Y                   = -7150,
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
        X                   = -7920,
        Z                   = -70,
        Y                   = -27310,
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
        X                   = -22580,
        Z                   = 10,
        Y                   = 23060,
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
        X                   = -35830,
        Z                   = 30,
        Y                   = 26470,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -53000,
        Y                   = -1000,
        Z                   = -1910,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
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
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43380,
        TriggerZ            = -30,
        TriggerY            = -54510,
        TriggerRange        = 1000,
        ActorX              = -43860,
        ActorZ              = -30,
        ActorY              = -54970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
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
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20640,
        TriggerZ            = -20,
        TriggerY            = -6840,
        TriggerRange        = 1000,
        ActorX              = 17090,
        ActorZ              = -600,
        ActorY              = -7230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_60A",          # 00, 0
        "Function_1_622",          # 01, 1
        "Function_2_773",          # 02, 2
        "Function_3_8F0",          # 03, 3
        "Function_4_AAB",          # 04, 4
        "Function_5_BC2",          # 05, 5
        "Function_6_CD9",          # 06, 6
        "Function_7_DF0",          # 07, 7
    )


    def Function_0_60A(): pass

    label("Function_0_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_621")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 1)

    label("loc_621")

    Return()

    # Function_0_60A end

    def Function_1_622(): pass

    label("Function_1_622")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x23002E)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69B")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_6EC")

    label("loc_69B")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_6EC")

    label("loc_6B0")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C5")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_6EC")

    label("loc_6C5")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_6EC")

    label("loc_6DA")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_6EC")

    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_715")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_727")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_739")
    OP_6F(0x0, 0)
    Jump("loc_740")

    label("loc_739")

    OP_6F(0x0, 60)

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_752")
    OP_6F(0x1, 0)
    Jump("loc_759")

    label("loc_752")

    OP_6F(0x1, 60)

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76B")
    OP_6F(0x2, 0)
    Jump("loc_772")

    label("loc_76B")

    OP_6F(0x2, 60)

    label("loc_772")

    Return()

    # Function_1_622 end

    def Function_2_773(): pass

    label("Function_2_773")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_798")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8DA")

    label("loc_798")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8DA")

    label("loc_7B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8DA")

    label("loc_7CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8DA")

    label("loc_7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8DA")

    label("loc_7FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_815")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8DA")

    label("loc_815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8DA")

    label("loc_82E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_847")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8DA")

    label("loc_847")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8DA")

    label("loc_860")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_879")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8DA")

    label("loc_879")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_892")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8DA")

    label("loc_892")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8DA")

    label("loc_8AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8DA")

    label("loc_8C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8DA")

    label("loc_8EF")

    Return()

    # Function_2_773 end

    def Function_3_8F0(): pass

    label("Function_3_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29F, 4)), scpexpr(EXPR_END)), "loc_8F8")
    Return()

    label("loc_8F8")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_9DD"),
        (SWITCH_DEFAULT, "loc_A00"),
    )


    label("loc_9DD")

    Fade(500)
    OP_89(0x0, -45180, -10, -2300, 270)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_A00")

    Battle(0xEE3, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -45180, -10, -2300, 270)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_A39"),
        (1, "loc_A3C"),
        (SWITCH_DEFAULT, "loc_A3F"),
    )


    label("loc_A39")

    EventEnd(0x0)
    Return()

    label("loc_A3C")

    OP_B4(0x0)
    Return()

    label("loc_A3F")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x14FC)
    OP_28(0xA7, 0x4, 0x10)
    OP_28(0xA7, 0x4, 0x2)
    OP_28(0xA7, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_8F0 end

    def Function_4_AAB(): pass

    label("Function_4_AAB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B83")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_B1A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1502)
    Jump("loc_B80")

    label("loc_B1A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_B80")

    Jump("loc_BB4")

    label("loc_B83")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BB4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_AAB end

    def Function_5_BC2(): pass

    label("Function_5_BC2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_C31")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1503)
    Jump("loc_C97")

    label("loc_C31")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_C97")

    Jump("loc_CCB")

    label("loc_C9A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CCB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BC2 end

    def Function_6_CD9(): pass

    label("Function_6_CD9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D8, 1)"), scpexpr(EXPR_END)), "loc_D48")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xD8\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1505)
    Jump("loc_DAE")

    label("loc_D48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xD8\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD8\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_DAE")

    Jump("loc_DE2")

    label("loc_DB1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DE2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CD9 end

    def Function_7_DF0(): pass

    label("Function_7_DF0")

    EventBegin(0x1)

    ChrTalk(    #11
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_E1C():
        OP_6D(17340, -20, -7640, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E1C)

    def lambda_E34():
        OP_6B(3250, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E34)

    def lambda_E44():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_E44)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECB")
    OP_C0(0xE, 0x23, 0x50BE, 0xFFFFFFEC, 0xFFFFE566, 0x10E, 0x4376, 0xFFFFFCE0, 0xFFFFE16A)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_EDA")

    label("loc_ECB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDA")
    EventEnd(0x1)

    label("loc_EDA")

    Return()

    # Function_7_DF0 end

    SaveToFile()

Try(main)
