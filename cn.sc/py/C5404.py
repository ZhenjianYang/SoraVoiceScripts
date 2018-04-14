from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5404   ._SN',
        MapName             = 'Other',
        Location            = 'C5404.x',
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
        '亡命守护者',                           # 10
        '目标探索者',                           # 11
        '目标探索者',                           # 12
        '哨兵570（蓝）',                        # 13
        '目标探索者',                           # 14
        '目标探索者',                           # 15
        '哨兵235（红）',                        # 16
        '亡命守护者',                           # 17
        '据点武装者',                           # 18
        '据点武装者',                           # 19
        '据点武装者',                           # 20
        '亡命守护者',                           # 21
        '目标探索者',                           # 22
        '目标探索者',                           # 23
        '哨兵570（蓝）',                        # 24
        '目标探索者',                           # 25
        '目标探索者',                           # 26
        '哨兵235（红）',                        # 27
        '亡命守护者',                           # 28
        '据点武装者',                           # 29
        '据点武装者',                           # 30
        '据点武装者',                           # 31
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
        'ED6_DT29/CH12580 ._CH',             # 04
        'ED6_DT29/CH12581 ._CH',             # 05
        'ED6_DT29/CH12310 ._CH',             # 06
        'ED6_DT29/CH12310 ._CH',             # 07
        'ED6_DT29/CH12320 ._CH',             # 08
        'ED6_DT29/CH12321 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT29/CH12580P._CP',             # 04
        'ED6_DT29/CH12581P._CP',             # 05
        'ED6_DT29/CH12310P._CP',             # 06
        'ED6_DT29/CH12310P._CP',             # 07
        'ED6_DT29/CH12320P._CP',             # 08
        'ED6_DT29/CH12321P._CP',             # 09
    )

    DeclNpc(
        X                   = 73000,
        Z                   = 2000,
        Y                   = -98360,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -1000,
        Z                   = 0,
        Y                   = 78200,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x425,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13970,
        Z                   = 0,
        Y                   = 79920,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12740,
        Z                   = 0,
        Y                   = 79820,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69850,
        Z                   = 1000,
        Y                   = 58110,
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
        X                   = 40980,
        Z                   = 0,
        Y                   = 3640,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 124900,
        Z                   = 0,
        Y                   = -50190,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -62040,
        Z                   = 1000,
        Y                   = -113250,
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
        X                   = -1140,
        Z                   = 0,
        Y                   = -75510,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x425,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -980,
        Z                   = 0,
        Y                   = -7880,
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
        X                   = -1440,
        Z                   = 0,
        Y                   = -31230,
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
        X                   = -900,
        Z                   = 0,
        Y                   = -49020,
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
        X                   = -1000,
        Z                   = 0,
        Y                   = 78200,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13970,
        Z                   = 0,
        Y                   = 79920,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12740,
        Z                   = 0,
        Y                   = 79820,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69850,
        Z                   = 1000,
        Y                   = 58110,
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
        X                   = 40980,
        Z                   = 0,
        Y                   = 3640,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 124900,
        Z                   = 0,
        Y                   = -50190,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -62040,
        Z                   = 1000,
        Y                   = -113250,
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
        X                   = -1140,
        Z                   = 0,
        Y                   = -75510,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -770,
        Z                   = 0,
        Y                   = -80,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4030,
        Z                   = 0,
        Y                   = -25880,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -640,
        Z                   = 0,
        Y                   = -43460,
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
        X                   = -1030,
        Y                   = -1000,
        Z                   = 133840,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -119660,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -28000,
        Y                   = -3000,
        Z                   = 76300,
        Range               = -26800,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x14758,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = -6500,
        Y                   = 0,
        Z                   = -2500,
        Range               = 5500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9C4,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = -6500,
        Y                   = 0,
        Z                   = -60500,
        Range               = 5500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF2734,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 38000,
        Y                   = 0,
        Z                   = -6000,
        Range               = 45000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFFA24,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 131500,
        Y                   = 0,
        Z                   = -192000,
        Range               = 136500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFD3140,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )


    DeclActor(
        TriggerX            = 75730,
        TriggerZ            = 0,
        TriggerY            = -20940,
        TriggerRange        = 1000,
        ActorX              = 75070,
        ActorZ              = 0,
        ActorY              = -20990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1000,
        TriggerZ            = 0,
        TriggerY            = 134330,
        TriggerRange        = 1000,
        ActorX              = -1000,
        ActorZ              = 1000,
        ActorY              = 134330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 67030,
        TriggerZ            = 0,
        TriggerY            = -90240,
        TriggerRange        = 1000,
        ActorX              = 66960,
        ActorZ              = 0,
        ActorY              = -89540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69990,
        TriggerZ            = 0,
        TriggerY            = -90250,
        TriggerRange        = 1000,
        ActorX              = 70020,
        ActorZ              = 0,
        ActorY              = -89630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73000,
        TriggerZ            = 0,
        TriggerY            = -90250,
        TriggerRange        = 1000,
        ActorX              = 72970,
        ActorZ              = 0,
        ActorY              = -89680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72970,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 73000,
        ActorZ              = 0,
        ActorY              = -98360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69940,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 69980,
        ActorZ              = 0,
        ActorY              = -98310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66990,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 67020,
        ActorZ              = 0,
        ActorY              = -98360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68510,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 68480,
        ActorZ              = 0,
        ActorY              = -131590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72000,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 71970,
        ActorZ              = 0,
        ActorY              = -131630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75450,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 75410,
        ActorZ              = 0,
        ActorY              = -131590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75480,
        TriggerZ            = 0,
        TriggerY            = -139800,
        TriggerRange        = 1000,
        ActorX              = 75510,
        ActorZ              = 0,
        ActorY              = -140420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72040,
        TriggerZ            = 0,
        TriggerY            = -139790,
        TriggerRange        = 1000,
        ActorX              = 71980,
        ActorZ              = 0,
        ActorY              = -140460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68470,
        TriggerZ            = 0,
        TriggerY            = -139800,
        TriggerRange        = 1000,
        ActorX              = 68510,
        ActorZ              = 0,
        ActorY              = -140460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5910,
        TriggerZ            = 0,
        TriggerY            = 88840,
        TriggerRange        = 1000,
        ActorX              = 5910,
        ActorZ              = 1000,
        ActorY              = 88840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14960,
        TriggerZ            = 0,
        TriggerY            = -120950,
        TriggerRange        = 1000,
        ActorX              = 14960,
        ActorZ              = 1000,
        ActorY              = -120950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6A2",          # 00, 0
        "Function_1_6B3",          # 01, 1
        "Function_2_91F",          # 02, 2
        "Function_3_935",          # 03, 3
        "Function_4_A88",          # 04, 4
        "Function_5_B9F",          # 05, 5
        "Function_6_CB6",          # 06, 6
        "Function_7_DCD",          # 07, 7
        "Function_8_F9D",          # 08, 8
        "Function_9_10B4",         # 09, 9
        "Function_10_11CB",        # 0A, 10
        "Function_11_12E2",        # 0B, 11
        "Function_12_13F9",        # 0C, 12
        "Function_13_1510",        # 0D, 13
        "Function_14_1627",        # 0E, 14
        "Function_15_177A",        # 0F, 15
        "Function_16_1891",        # 10, 16
        "Function_17_18AA",        # 11, 17
        "Function_18_18C3",        # 12, 18
        "Function_19_231D",        # 13, 19
        "Function_20_2365",        # 14, 20
        "Function_21_23AD",        # 15, 21
        "Function_22_23F5",        # 16, 22
        "Function_23_243D",        # 17, 23
        "Function_24_2769",        # 18, 24
        "Function_25_2B7C",        # 19, 25
        "Function_26_2C5E",        # 1A, 26
        "Function_27_2C9F",        # 1B, 27
        "Function_28_2CE0",        # 1C, 28
        "Function_29_2D21",        # 1D, 29
        "Function_30_2D62",        # 1E, 30
        "Function_31_2DE9",        # 1F, 31
        "Function_32_2E7A",        # 20, 32
        "Function_33_2EA0",        # 21, 33
    )


    def Function_0_6A2(): pass

    label("Function_0_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6B2")
    OP_A3(0x10F0)
    OP_B5(0x0)
    Event(0, 18)

    label("loc_6B2")

    Return()

    # Function_0_6A2 end

    def Function_1_6B3(): pass

    label("Function_1_6B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D1")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E3")
    OP_6F(0x0, 0)
    Jump("loc_6EA")

    label("loc_6E3")

    OP_6F(0x0, 60)

    label("loc_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FC")
    OP_6F(0x21, 0)
    Jump("loc_703")

    label("loc_6FC")

    OP_6F(0x21, 60)

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_715")
    OP_6F(0x22, 0)
    Jump("loc_71C")

    label("loc_715")

    OP_6F(0x22, 60)

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72E")
    OP_6F(0x23, 0)
    Jump("loc_735")

    label("loc_72E")

    OP_6F(0x23, 60)

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747")
    OP_6F(0x24, 0)
    Jump("loc_74E")

    label("loc_747")

    OP_6F(0x24, 60)

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_760")
    OP_6F(0x25, 0)
    Jump("loc_767")

    label("loc_760")

    OP_6F(0x25, 60)

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_779")
    OP_6F(0x26, 0)
    Jump("loc_780")

    label("loc_779")

    OP_6F(0x26, 60)

    label("loc_780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_792")
    OP_6F(0x27, 0)
    Jump("loc_799")

    label("loc_792")

    OP_6F(0x27, 60)

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AB")
    OP_6F(0x28, 0)
    Jump("loc_7B2")

    label("loc_7AB")

    OP_6F(0x28, 60)

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C4")
    OP_6F(0x29, 0)
    Jump("loc_7CB")

    label("loc_7C4")

    OP_6F(0x29, 60)

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DD")
    OP_6F(0x2A, 0)
    Jump("loc_7E4")

    label("loc_7DD")

    OP_6F(0x2A, 60)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6")
    OP_6F(0x2B, 0)
    Jump("loc_7FD")

    label("loc_7F6")

    OP_6F(0x2B, 60)

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80F")
    OP_6F(0x2C, 0)
    Jump("loc_816")

    label("loc_80F")

    OP_6F(0x2C, 60)

    label("loc_816")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CA")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_901")

    label("loc_8CA")

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

    label("loc_901")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91A")
    OP_72(0x7, 0x10)
    OP_65(0x1, 0x1)

    label("loc_91A")

    Call(0, 25)
    Return()

    # Function_1_6B3 end

    def Function_2_91F(): pass

    label("Function_2_91F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_934")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_91F")

    label("loc_934")

    Return()

    # Function_2_91F end

    def Function_3_935(): pass

    label("Function_3_935")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
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
    OP_A2(0x1D39)
    Jump("loc_A76")

    label("loc_A5C")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A76")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_935 end

    def Function_4_A88(): pass

    label("Function_4_A88")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B60")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_AF7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2330)
    Jump("loc_B5D")

    label("loc_AF7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_B5D")

    Jump("loc_B91")

    label("loc_B60")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A88 end

    def Function_5_B9F(): pass

    label("Function_5_B9F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C77")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x22, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6B, 1)"), scpexpr(EXPR_END)), "loc_C0E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x6B\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2331)
    Jump("loc_C74")

    label("loc_C0E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x6B\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x6B\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x22, 60)
    OP_70(0x22, 0x0)

    label("loc_C74")

    Jump("loc_CA8")

    label("loc_C77")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CA8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B9F end

    def Function_6_CB6(): pass

    label("Function_6_CB6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x23, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_D25")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2333)
    Jump("loc_D8B")

    label("loc_D25")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x23, 60)
    OP_70(0x23, 0x0)

    label("loc_D8B")

    Jump("loc_DBF")

    label("loc_D8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DBF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CB6 end

    def Function_7_DCD(): pass

    label("Function_7_DCD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F60")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAC")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_E1F():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E1F)

    def lambda_E3A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E3A)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #11
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x432, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E87"),
        (2, "loc_E99"),
        (1, "loc_EA9"),
        (SWITCH_DEFAULT, "loc_EAC"),
    )


    label("loc_E87")

    OP_A2(0x2335)
    OP_6F(0x24, 60)
    Sleep(500)
    Jump("loc_EAC")

    label("loc_E99")

    OP_6F(0x24, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_EA9")

    OP_B4(0x0)
    Return()

    label("loc_EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x139, 1)"), scpexpr(EXPR_END)), "loc_EFB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x39\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2334)
    Jump("loc_F5D")

    label("loc_EFB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x39\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x39\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_F5D")

    Jump("loc_F8F")

    label("loc_F60")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F8F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_DCD end

    def Function_8_F9D(): pass

    label("Function_8_F9D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_100C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2336)
    Jump("loc_1072")

    label("loc_100C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_1072")

    Jump("loc_10A6")

    label("loc_1075")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_F9D end

    def Function_9_10B4(): pass

    label("Function_9_10B4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_1123")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2337)
    Jump("loc_1189")

    label("loc_1123")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_1189")

    Jump("loc_11BD")

    label("loc_118C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11BD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_10B4 end

    def Function_10_11CB(): pass

    label("Function_10_11CB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_123A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2338)
    Jump("loc_12A0")

    label("loc_123A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF5\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_12A0")

    Jump("loc_12D4")

    label("loc_12A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_11CB end

    def Function_11_12E2(): pass

    label("Function_11_12E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_1351")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2339)
    Jump("loc_13B7")

    label("loc_1351")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_13B7")

    Jump("loc_13EB")

    label("loc_13BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_12E2 end

    def Function_12_13F9(): pass

    label("Function_12_13F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x88, 1)"), scpexpr(EXPR_END)), "loc_1468")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\x88\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233A)
    Jump("loc_14CE")

    label("loc_1468")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "宝箱里装有\x1F\x88\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x88\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_14CE")

    Jump("loc_1502")

    label("loc_14D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1502")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_13F9 end

    def Function_13_1510(): pass

    label("Function_13_1510")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_157F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233C)
    Jump("loc_15E5")

    label("loc_157F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_15E5")

    Jump("loc_1619")

    label("loc_15E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1619")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1510 end

    def Function_14_1627(): pass

    label("Function_14_1627")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x1E)
    OP_73(0x2B)
    OP_6F(0x2B, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
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
    OP_A2(0x233D)
    Jump("loc_1768")

    label("loc_174E")


    AnonymousTalk(    #34
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1768")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1627 end

    def Function_15_177A(): pass

    label("Function_15_177A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1852")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_17E9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233E)
    Jump("loc_184F")

    label("loc_17E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_184F")

    Jump("loc_1883")

    label("loc_1852")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1883")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_177A end

    def Function_16_1891(): pass

    label("Function_16_1891")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A2(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_16_1891 end

    def Function_17_18AA(): pass

    label("Function_17_18AA")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A2(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_17_18AA end

    def Function_18_18C3(): pass

    label("Function_18_18C3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18DA")
    Call(0, 30)
    Call(0, 31)

    label("loc_18DA")

    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_193B"),
        (3, "loc_1952"),
        (4, "loc_1969"),
        (5, "loc_1980"),
        (6, "loc_1997"),
        (7, "loc_19AE"),
        (8, "loc_19C5"),
        (SWITCH_DEFAULT, "loc_19DC"),
    )


    label("loc_193B")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_19DC")

    label("loc_1952")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_19DC")

    label("loc_1969")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_19DC")

    label("loc_1980")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_19DC")

    label("loc_1997")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_19DC")

    label("loc_19AE")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_19DC")

    label("loc_19C5")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_19DC")

    label("loc_19DC")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0x10B, 14)
    SetChrChipByIndex(0xF9, 16)
    OP_6D(-25490, 100, 79270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(-20610, 0, 81250, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)
    FadeToBright(1000, 0)

    def lambda_1A97():
        OP_6D(-4780, 0, 80680, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A97)

    def lambda_1AAF():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AAF)

    def lambda_1AC7():
        OP_6B(2830, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AC7)

    def lambda_1AD7():
        OP_6C(56000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1AD7)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Sleep(100)
    OP_43(0x101, 0x1, 0x0, 0x13)
    Sleep(300)
    OP_43(0x10B, 0x1, 0x0, 0x15)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x16)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10B, 0x1)
    WaitChrThread(0xF9, 0x1)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10B, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0x10B,
        "#216F#6P这、这就是『古罗力亚斯』的内部……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(    #39
        0x107,
        (
            "#065F好、好厉害……！\x01",
            "竟然如此宽阔……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE9")

    ChrTalk(    #40
        0x105,
        (
            "#1163F……完全不像是在\x01",
            "飞船里的宽度啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C27")

    ChrTalk(    #41
        0x109,
        (
            "#1068F啊～完全不像是在\x01",
            "飞船里的宽度呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1C27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C72")

    ChrTalk(    #42
        0x103,
        (
            "#022F原来如此，和外观一样，\x01",
            "里面也是很夸张的宽度啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD3")

    ChrTalk(    #43
        0x104,
        (
            "#033F这……\x01",
            "这就是宽阔的舰内啊。\x02\x03",

            "#031F感觉都快可以开\x01",
            "我的演奏会了不是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D12")

    ChrTalk(    #44
        0x106,
        (
            "#555F咦……完全不像是在\x01",
            "飞船里的宽度啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4A")

    label("loc_1D12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4A")

    ChrTalk(    #45
        0x108,
        (
            "#072F嗯……\x01",
            "很合乎飞船外观的宽度嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4A")

    Sleep(100)
    Fade(500)
    OP_6D(-10600, 0, 80800, 0)
    OP_67(0, 6980, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_8C(0x101, 225, 400)
    Sleep(500)

    ChrTalk(    #46
        0x101,
        (
            "#1007F#5P呼～\x01",
            "宽阔得简直令人头晕呢。\x02\x03",

            "#1002F而且结社的人形兵器\x01",
            "又放得到处都是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10B,
        (
            "#215F#6P…………………………………\x02\x03",

            "#212F你们曾经从这艘舰艇\x01",
            "逃出过吧？\x02\x03",

            "大哥他们所在的地方有线索吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E63():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E63)
    Sleep(50)

    def lambda_1E76():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E76)
    Sleep(50)

    def lambda_1E89():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1E89)
    Sleep(500)

    ChrTalk(    #48
        0x101,
        (
            "#1004F#5P啊，嗯……这个啊。\x02\x03",

            "#1015F说不定在一开始\x01",
            "关我的客舱附近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1035F#2P不……\x01",
            "因为那里怎么说都是客房。\x02\x03",

            "#1042F多半是被关在\x01",
            "监禁用的牢房里。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1F71():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F71)
    Sleep(50)

    def lambda_1F84():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1F84)
    Sleep(50)

    def lambda_1F97():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1F97)
    WaitChrThread(0x10B, 0x1)

    ChrTalk(    #50
        0x10B,
        "#216F#6P监、监禁用的牢房里～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1002F#5P还、还有这种房间啊。\x02\x03",

            "之前逃脱的时候，\x01",
            "印象中倒是没看过……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    Sleep(300)

    ChrTalk(    #52
        0x102,
        (
            "#1035F#4P那个时候，防止脱逃用的\x01",
            "电磁栅栏都是展开着的，\x01",
            "所以能前往的地方很有限。\x02\x03",

            "#1042F但是现在电磁栅栏\x01",
            "似乎都没有展开……\x02\x03",

            "说不定这正是帮助\x01",
            "多伦先生他们的好机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10B,
        (
            "#212F#6P那、那么……\x01",
            "那个牢房在哪里！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20FC():

        label("loc_20FC")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_20FC")

    QueueWorkItem2(0x101, 2, lambda_20FC)

    def lambda_210D():

        label("loc_210D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_210D")

    QueueWorkItem2(0x10B, 2, lambda_210D)

    def lambda_211E():

        label("loc_211E")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_211E")

    QueueWorkItem2(0xF9, 2, lambda_211E)
    OP_8C(0x102, 90, 400)
    Sleep(300)

    def lambda_213B():
        OP_6D(-3990, 0, 77560, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_213B)
    OP_8E(0x102, 0xFFFFEE30, 0x0, 0x12D54, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x102, 180, 400)
    OP_6D(-1740, 0, 73860, 1500)

    ChrTalk(    #54
        0x102,
        (
            "#1042F#5P……这前面的通道\x01",
            "有接连到下层的小楼梯。\x02\x03",

            "从那里下去应该就是牢房了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-9270, 0, 80720, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    OP_8C(0x102, 270, 400)
    OP_44(0x101, 0x2)
    OP_44(0x10B, 0x2)
    OP_44(0xF9, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1006F#6P向下通往牢房的小楼梯啊……\x01",
            "好～先试着调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-10420, 0, 79270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -10420, 0, 79270, 90)
    SetChrPos(0x1, -10420, 0, 79270, 90)
    SetChrPos(0x2, -10420, 0, 79270, 90)
    SetChrPos(0x3, -10420, 0, 79270, 90)
    OP_69(0x0, 0x0)
    OP_A2(0x2222)
    OP_28(0x9E, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_18_18C3 end

    def Function_19_231D(): pass

    label("Function_19_231D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 80800, 90)

    def lambda_2344():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2344)
    OP_8E(0xFE, 0xFFFFD698, 0x0, 0x13BA0, 0x1770, 0x0)
    Return()

    # Function_19_231D end

    def Function_20_2365(): pass

    label("Function_20_2365")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 79270, 90)

    def lambda_238C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_238C)
    OP_8E(0xFE, 0xFFFFD620, 0x0, 0x134FC, 0x1770, 0x0)
    Return()

    # Function_20_2365 end

    def Function_21_23AD(): pass

    label("Function_21_23AD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 81200, 90)

    def lambda_23D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23D4)
    OP_8E(0xFE, 0xFFFFD06C, 0x0, 0x13BBE, 0x1770, 0x0)
    Return()

    # Function_21_23AD end

    def Function_22_23F5(): pass

    label("Function_22_23F5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 79180, 90)

    def lambda_241C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_241C)
    OP_8E(0xFE, 0xFFFFCEFA, 0x0, 0x134B6, 0x1770, 0x0)
    Return()

    # Function_22_23F5 end

    def Function_23_243D(): pass

    label("Function_23_243D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_246D"),
        (1, "loc_24B7"),
        (10, "loc_2503"),
        (6, "loc_2550"),
        (4, "loc_2599"),
        (8, "loc_25E5"),
        (2, "loc_2633"),
        (3, "loc_267C"),
        (5, "loc_26CB"),
        (7, "loc_2716"),
        (SWITCH_DEFAULT, "loc_2765"),
    )


    label("loc_246D")


    ChrTalk(    #56
        0x101,
        (
            "#1002F（监禁用的牢房\x01",
            "  是在通道的反方向吧……）\x02\x03",

            "（得先去那边。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_24B7")


    ChrTalk(    #57
        0x102,
        (
            "#1042F（监禁用的牢房\x01",
            "  是在通道的反方向……）\x02\x03",

            "（这边待会儿再来。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2503")


    ChrTalk(    #58
        0x10B,
        (
            "#212F（……监禁用的牢房\x01",
            "  是在通道的反方向吧。）\x02\x03",

            "（得先去那边……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2550")


    ChrTalk(    #59
        0x107,
        (
            "#062F（嗯，记得牢房\x01",
            "  是在通道的反方向吧……）\x02\x03",

            "（得先去那边。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2599")


    ChrTalk(    #60
        0x105,
        (
            "#1162F（监禁用的牢房\x01",
            "  应该是在通道的反方向……）\x02\x03",

            "（得先去那边。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_25E5")


    ChrTalk(    #61
        0x109,
        (
            "#1063F（监禁用的牢房\x01",
            "  是在通道的反方向吧……）\x02\x03",

            "（这边待会儿再来。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2633")


    ChrTalk(    #62
        0x103,
        (
            "#022F（监禁用的牢房\x01",
            "  是在通道的反方向吧……）\x02\x03",

            "（先去那边吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_267C")


    ChrTalk(    #63
        0x104,
        (
            "#030F（唔，监禁用的牢房\x01",
            "  好像是在通道的反方向……）\x02\x03",

            "（先去那边吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_26CB")


    ChrTalk(    #64
        0x106,
        (
            "#050F（监禁用的牢房\x01",
            "  好像是在通道的反方向……）\x02\x03",

            "（得先去那边。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2716")


    ChrTalk(    #65
        0x108,
        (
            "#072F（监禁用的牢房\x01",
            "  好像是在通道的反方向。）\x02\x03",

            "（这边待会儿再来吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2765")

    label("loc_2765")

    TalkEnd(0xFF)
    Return()

    # Function_23_243D end

    def Function_24_2769(): pass

    label("Function_24_2769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27D2")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2B7B")

    label("loc_27D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7B")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2810"),
        (1, "loc_285C"),
        (10, "loc_28B8"),
        (6, "loc_28FB"),
        (4, "loc_2957"),
        (8, "loc_29B2"),
        (2, "loc_2A0A"),
        (3, "loc_2A51"),
        (5, "loc_2AB6"),
        (7, "loc_2B06"),
        (SWITCH_DEFAULT, "loc_2B60"),
    )


    label("loc_2810")


    ChrTalk(    #67
        0x101,
        (
            "#1002F（还没救出\x01",
            "  乔丝特的哥哥们……）\x02\x03",

            "（逃出的事待会儿再说吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_285C")


    ChrTalk(    #68
        0x102,
        (
            "#1043F（在救出吉尔先生他们之前\x01",
            "  还是不要随便逃出比较好……）\x02\x03",

            "（回到舰内搜索吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_28B8")


    ChrTalk(    #69
        0x10B,
        (
            "#215F（不行……\x01",
            "  还不能逃出去。）\x02\x03",

            "（必须救出大哥们……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_28FB")


    ChrTalk(    #70
        0x107,
        (
            "#062F（还不能从『古罗力亚斯』\x01",
            "  里面出去吧……）\x02\x03",

            "（必须尽快救出\x01",
            "  空贼那些人……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2957")


    ChrTalk(    #71
        0x105,
        (
            "#1163F（还不能从『古罗力亚斯』\x01",
            "  里面出去……）\x02\x03",

            "  必须救出\x01",
            "  乔丝特的哥哥们……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_29B2")


    ChrTalk(    #72
        0x109,
        (
            "#1063F（哦，逃出的事待会儿再说。）\x02\x03",

            "（不管怎样得先救出\x01",
            "  空贼的小哥们才行……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2A0A")


    ChrTalk(    #73
        0x103,
        (
            "#022F（还没救出\x01",
            "  空贼的成员……）\x02\x03",

            "（逃出的事待会儿再说吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2A51")


    ChrTalk(    #74
        0x104,
        (
            "#033F（哎呀……\x01",
            "  现在逃跑可太不华丽。）\x02\x03",

            "#035F（必须大胆且华丽地救出\x01",
            "  诸位空贼之后再说。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2AB6")


    ChrTalk(    #75
        0x106,
        (
            "#052F（哦，不行不行……）\x02\x03",

            "#053F（要开溜也得等\x01",
            "  救出了空贼之后再说。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2B06")


    ChrTalk(    #76
        0x108,
        (
            "#074F（在救出空贼们之前\x01",
            "  还是不要随便逃出比较好……）\x02\x03",

            "#072F（回到舰内搜索吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B60")

    label("loc_2B60")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2B7B")

    Return()

    # Function_24_2769 end

    def Function_25_2B7C(): pass

    label("Function_25_2B7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B89")
    Return()

    label("loc_2B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 1)), scpexpr(EXPR_END)), "loc_2BBE")
    OP_6F(0x1, 100)
    OP_72(0x1, 0x2)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -1500, 3600, 2000, 1500)

    label("loc_2BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 2)), scpexpr(EXPR_END)), "loc_2BF3")
    OP_6F(0x2, 100)
    OP_72(0x2, 0x2)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -59500, 3600, 2000, -56500)

    label("loc_2BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 3)), scpexpr(EXPR_END)), "loc_2C28")
    OP_6F(0x3, 100)
    OP_72(0x3, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 38000, -1000, -5300, 45000, 2000, -2500)

    label("loc_2C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 4)), scpexpr(EXPR_END)), "loc_2C5D")
    OP_6F(0x4, 100)
    OP_72(0x4, 0x2)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, 132500, -1000, -191000, 135500, 2000, -185000)

    label("loc_2C5D")

    Return()

    # Function_25_2B7C end

    def Function_26_2C5E(): pass

    label("Function_26_2C5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C6B")
    Return()

    label("loc_2C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 1)), scpexpr(EXPR_END)), "loc_2C73")
    Return()

    label("loc_2C73")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x1CA1)
    Call(0, 25)
    EventEnd(0x3)
    Return()

    # Function_26_2C5E end

    def Function_27_2C9F(): pass

    label("Function_27_2C9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CAC")
    Return()

    label("loc_2CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 2)), scpexpr(EXPR_END)), "loc_2CB4")
    Return()

    label("loc_2CB4")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x1CA2)
    Call(0, 25)
    EventEnd(0x3)
    Return()

    # Function_27_2C9F end

    def Function_28_2CE0(): pass

    label("Function_28_2CE0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CED")
    Return()

    label("loc_2CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 3)), scpexpr(EXPR_END)), "loc_2CF5")
    Return()

    label("loc_2CF5")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x1CA3)
    Call(0, 25)
    EventEnd(0x3)
    Return()

    # Function_28_2CE0 end

    def Function_29_2D21(): pass

    label("Function_29_2D21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D2E")
    Return()

    label("loc_2D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 4)), scpexpr(EXPR_END)), "loc_2D36")
    Return()

    label("loc_2D36")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x1CA4)
    Call(0, 25)
    EventEnd(0x3)
    Return()

    # Function_29_2D21 end

    def Function_30_2D62(): pass

    label("Function_30_2D62")

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
        (0, "loc_2DDC"),
        (1, "loc_2DE2"),
        (SWITCH_DEFAULT, "loc_2DE8"),
    )


    label("loc_2DDC")

    OP_A2(0x1200)
    Jump("loc_2DE8")

    label("loc_2DE2")

    OP_A2(0x1201)
    Jump("loc_2DE8")

    label("loc_2DE8")

    Return()

    # Function_30_2D62 end

    def Function_31_2DE9(): pass

    label("Function_31_2DE9")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
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

    # Function_31_2DE9 end

    def Function_32_2E7A(): pass

    label("Function_32_2E7A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240133, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_32_2E7A end

    def Function_33_2EA0(): pass

    label("Function_33_2EA0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240134, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_33_2EA0 end

    SaveToFile()

Try(main)
