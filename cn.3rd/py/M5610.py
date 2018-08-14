from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5610   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '库拉茨',                               # 9
        '猎兵库拉茨',                           # 10
        '猎兵库拉茨',                           # 11
        '镜子哨兵',                             # 12
        '镜子哨兵',                             # 13
        '镜子哨兵',                             # 14
        '零部件',                               # 15
        '零部件',                               # 16
        '零部件',                               # 17
        '零部件',                               # 18
        '零部件',                               # 19
        '零部件',                               # 20
        '零部件',                               # 21
        '零部件',                               # 22
        '零部件',                               # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14950 ._CH',             # 00
        'ED6_DT29/CH14951 ._CH',             # 01
        'ED6_DT29/CH14960 ._CH',             # 02
        'ED6_DT29/CH14961 ._CH',             # 03
        'ED6_DT26/CH20409 ._CH',             # 04
        'ED6_DT07/CH01260 ._CH',             # 05
        'ED6_DT07/CH00390 ._CH',             # 06
        'ED6_DT07/CH00391 ._CH',             # 07
        'ED6_DT07/CH00394 ._CH',             # 08
        'ED6_DT07/CH00395 ._CH',             # 09
        'ED6_DT27/CH04820 ._CH',             # 0A
        'ED6_DT27/CH04821 ._CH',             # 0B
        'ED6_DT29/CH15160 ._CH',             # 0C
        'ED6_DT29/CH15161 ._CH',             # 0D
        'ED6_DT29/CH15170 ._CH',             # 0E
        'ED6_DT29/CH15171 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT29/CH14950P._CP',             # 00
        'ED6_DT29/CH14951P._CP',             # 01
        'ED6_DT29/CH14960P._CP',             # 02
        'ED6_DT29/CH14961P._CP',             # 03
        'ED6_DT26/CH20409P._CP',             # 04
        'ED6_DT07/CH01260P._CP',             # 05
        'ED6_DT07/CH00390P._CP',             # 06
        'ED6_DT07/CH00391P._CP',             # 07
        'ED6_DT07/CH00394P._CP',             # 08
        'ED6_DT07/CH00395P._CP',             # 09
        'ED6_DT27/CH04820P._CP',             # 0A
        'ED6_DT27/CH04821P._CP',             # 0B
        'ED6_DT29/CH15160P._CP',             # 0C
        'ED6_DT29/CH15161P._CP',             # 0D
        'ED6_DT29/CH15170P._CP',             # 0E
        'ED6_DT29/CH15171P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131076,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65540,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196612,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65540,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131076,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196612,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
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
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65540,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 158730,
        Z                   = 0,
        Y                   = -17340,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x280,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -37030,
        Z                   = 0,
        Y                   = 127000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -85140,
        Z                   = 0,
        Y                   = 97350,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x282,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86310,
        Z                   = 0,
        Y                   = -8950,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x283,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 150910,
        Z                   = 0,
        Y                   = -12950,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 148650,
        Z                   = 0,
        Y                   = -22930,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 7750,
        Z                   = 0,
        Y                   = -12840,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 930,
        Z                   = 0,
        Y                   = 32900,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -69050,
        Z                   = 0,
        Y                   = 44350,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -82990,
        Z                   = 0,
        Y                   = 107060,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -22970,
        Y                   = 0,
        Z                   = 133110,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 44,
    )


    DeclActor(
        TriggerX            = 8890,
        TriggerZ            = 0,
        TriggerY            = 137900,
        TriggerRange        = 1000,
        ActorX              = 8890,
        ActorZ              = 2000,
        ActorY              = 137900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77020,
        TriggerZ            = 0,
        TriggerY            = 169070,
        TriggerRange        = 800,
        ActorX              = 77020,
        ActorZ              = 1000,
        ActorY              = 169070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12640,
        TriggerZ            = 0,
        TriggerY            = -18920,
        TriggerRange        = 800,
        ActorX              = 12640,
        ActorZ              = 1600,
        ActorY              = -18920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28670,
        TriggerZ            = 0,
        TriggerY            = 26010,
        TriggerRange        = 800,
        ActorX              = -28670,
        ActorZ              = 1200,
        ActorY              = 26010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24680,
        TriggerZ            = 0,
        TriggerY            = 131780,
        TriggerRange        = 800,
        ActorX              = -24680,
        ActorZ              = 1200,
        ActorY              = 131780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28680,
        TriggerZ            = 0,
        TriggerY            = 12030,
        TriggerRange        = 800,
        ActorX              = -28680,
        ActorZ              = 1200,
        ActorY              = 12030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66700,
        TriggerZ            = 0,
        TriggerY            = 67540,
        TriggerRange        = 800,
        ActorX              = 66700,
        ActorZ              = 1200,
        ActorY              = 67540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46870,
        TriggerZ            = 0,
        TriggerY            = 70120,
        TriggerRange        = 1000,
        ActorX              = 46870,
        ActorZ              = 1000,
        ActorY              = 70120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91320,
        TriggerZ            = 0,
        TriggerY            = 101670,
        TriggerRange        = 1000,
        ActorX              = -91320,
        ActorZ              = 1000,
        ActorY              = 101670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 153000,
        TriggerZ            = 0,
        TriggerY            = -16980,
        TriggerRange        = 1000,
        ActorX              = 153000,
        ActorZ              = 1000,
        ActorY              = -16980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -89500,
        TriggerZ            = 0,
        TriggerY            = -9000,
        TriggerRange        = 1000,
        ActorX              = -89500,
        ActorZ              = 1000,
        ActorY              = -9000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -89500,
        TriggerZ            = 0,
        TriggerY            = -7500,
        TriggerRange        = 1000,
        ActorX              = -89500,
        ActorZ              = 1000,
        ActorY              = -7500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -89500,
        TriggerZ            = 0,
        TriggerY            = -10500,
        TriggerRange        = 1000,
        ActorX              = -89500,
        ActorZ              = 1000,
        ActorY              = -10500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3020,
        TriggerZ            = 0,
        TriggerY            = 33100,
        TriggerRange        = 1000,
        ActorX              = 3020,
        ActorZ              = 1000,
        ActorY              = 33100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 107130,
        TriggerZ            = 0,
        TriggerY            = 67950,
        TriggerRange        = 1000,
        ActorX              = 108000,
        ActorZ              = 3000,
        ActorY              = 68070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59980,
        TriggerZ            = 0,
        TriggerY            = 68370,
        TriggerRange        = 100,
        ActorX              = 60730,
        ActorZ              = 1000,
        ActorY              = 68490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_682",          # 00, 0
        "Function_1_6DA",          # 01, 1
        "Function_2_89D",          # 02, 2
        "Function_3_8B3",          # 03, 3
        "Function_4_8EF",          # 04, 4
        "Function_5_930",          # 05, 5
        "Function_6_971",          # 06, 6
        "Function_7_9B2",          # 07, 7
        "Function_8_9F3",          # 08, 8
        "Function_9_A34",          # 09, 9
        "Function_10_A75",         # 0A, 10
        "Function_11_AB6",         # 0B, 11
        "Function_12_AF7",         # 0C, 12
        "Function_13_C1D",         # 0D, 13
        "Function_14_D43",         # 0E, 14
        "Function_15_E69",         # 0F, 15
        "Function_16_F8F",         # 10, 16
        "Function_17_10B5",        # 11, 17
        "Function_18_11DB",        # 12, 18
        "Function_19_1301",        # 13, 19
        "Function_20_1425",        # 14, 20
        "Function_21_23F1",        # 15, 21
        "Function_22_2471",        # 16, 22
        "Function_23_24F6",        # 17, 23
        "Function_24_257B",        # 18, 24
        "Function_25_2584",        # 19, 25
        "Function_26_3447",        # 1A, 26
        "Function_27_349C",        # 1B, 27
        "Function_28_34F6",        # 1C, 28
        "Function_29_3A70",        # 1D, 29
        "Function_30_3B2F",        # 1E, 30
        "Function_31_4401",        # 1F, 31
        "Function_32_4699",        # 20, 32
        "Function_33_47F8",        # 21, 33
        "Function_34_4887",        # 22, 34
        "Function_35_48E4",        # 23, 35
        "Function_36_4982",        # 24, 36
        "Function_37_4A20",        # 25, 37
        "Function_38_4ABE",        # 26, 38
        "Function_39_4B62",        # 27, 39
        "Function_40_4D7C",        # 28, 40
        "Function_41_4DF0",        # 29, 41
        "Function_42_4FEB",        # 2A, 42
        "Function_43_50A1",        # 2B, 43
        "Function_44_514C",        # 2C, 44
    )


    def Function_0_682(): pass

    label("Function_0_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_698")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_6A6")

    label("loc_698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6A6")
    OP_A3(0x2504)
    Event(0, 33)

    label("loc_6A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE")
    Event(0, 20)

    label("loc_6BE")

    Jump("loc_6D9")

    label("loc_6C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D9")
    Event(0, 24)

    label("loc_6D9")

    Return()

    # Function_0_682 end

    def Function_1_6DA(): pass

    label("Function_1_6DA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (128, "loc_6EE"),
        (129, "loc_6EE"),
        (135, "loc_6EE"),
        (SWITCH_DEFAULT, "loc_6F6"),
    )


    label("loc_6EE")

    OP_22(0xA0, 0x1, 0x64)
    Jump("loc_6FC")

    label("loc_6F6")

    OP_23(0xA0)
    Jump("loc_6FC")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 0)), scpexpr(EXPR_END)), "loc_710")
    OP_10(0x0, 0x1)
    OP_6F(0x18, 60)
    Jump("loc_71C")

    label("loc_710")

    OP_1B(0x0, 0x0, 0x22)
    OP_6F(0x18, 1)

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_72D")

    OP_82(0x84, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_740")
    OP_82(0x85, 0x0)
    Jump("loc_743")

    label("loc_740")

    OP_82(0x86, 0x0)

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 4)), scpexpr(EXPR_END)), "loc_74E")
    OP_64(0xF, 0x1)

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 1)), scpexpr(EXPR_END)), "loc_765")
    OP_64(0x3, 0x1)
    OP_71(0x1006, 0x0)
    ExitThread()
    OP_10(0x1F, 0x1)
    Jump("loc_76E")

    label("loc_765")

    OP_10(0x1F, 0x0)
    OP_72(0x1006, 0x0)
    ExitThread()

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 2)), scpexpr(EXPR_END)), "loc_785")
    OP_64(0x4, 0x1)
    OP_71(0x1011, 0x0)
    ExitThread()
    OP_10(0x20, 0x1)
    Jump("loc_78E")

    label("loc_785")

    OP_10(0x20, 0x0)
    OP_72(0x1011, 0x0)
    ExitThread()

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 3)), scpexpr(EXPR_END)), "loc_7A5")
    OP_64(0x5, 0x1)
    OP_71(0x1005, 0x0)
    ExitThread()
    OP_10(0x5, 0x1)
    Jump("loc_7AE")

    label("loc_7A5")

    OP_10(0x5, 0x0)
    OP_72(0x1005, 0x0)
    ExitThread()

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 3)), scpexpr(EXPR_END)), "loc_7C5")
    OP_64(0x6, 0x1)
    OP_71(0x100D, 0x0)
    ExitThread()
    OP_10(0x1D, 0x1)
    Jump("loc_7CE")

    label("loc_7C5")

    OP_10(0x1D, 0x0)
    OP_72(0x100D, 0x0)
    ExitThread()

    label("loc_7CE")

    OP_74(0x17, 0x0, 0x0)
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF")
    OP_6F(0x1A, 0)
    Jump("loc_806")

    label("loc_7FF")

    OP_6F(0x1A, 60)

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818")
    OP_6F(0x1B, 0)
    Jump("loc_81F")

    label("loc_818")

    OP_6F(0x1B, 60)

    label("loc_81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_831")
    OP_6F(0x1C, 0)
    Jump("loc_838")

    label("loc_831")

    OP_6F(0x1C, 60)

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84A")
    OP_6F(0x1D, 0)
    Jump("loc_851")

    label("loc_84A")

    OP_6F(0x1D, 60)

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")
    OP_6F(0x1E, 0)
    Jump("loc_86A")

    label("loc_863")

    OP_6F(0x1E, 60)

    label("loc_86A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")
    OP_6F(0x1F, 0)
    Jump("loc_883")

    label("loc_87C")

    OP_6F(0x1F, 60)

    label("loc_883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_895")
    OP_6F(0x20, 0)
    Jump("loc_89C")

    label("loc_895")

    OP_6F(0x20, 60)

    label("loc_89C")

    Return()

    # Function_1_6DA end

    def Function_2_89D(): pass

    label("Function_2_89D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_89D")

    label("loc_8B2")

    Return()

    # Function_2_89D end

    def Function_3_8B3(): pass

    label("Function_3_8B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EE")
    SetChrPos(0xFE, 50060, 1500, 73170, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xC350, 0x5DC, 0xDCBE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("Function_3_8B3")

    label("loc_8EE")

    Return()

    # Function_3_8B3 end

    def Function_4_8EF(): pass

    label("Function_4_8EF")

    Sleep(2000)

    label("loc_8F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92F")
    SetChrPos(0xFE, 50060, 1500, 73170, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xC350, 0x5DC, 0xDCBE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_8F4")

    label("loc_92F")

    Return()

    # Function_4_8EF end

    def Function_5_930(): pass

    label("Function_5_930")

    Sleep(3800)

    label("loc_935")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_970")
    SetChrPos(0xFE, 50060, 1500, 73170, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xC350, 0x5DC, 0xDCBE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_935")

    label("loc_970")

    Return()

    # Function_5_930 end

    def Function_6_971(): pass

    label("Function_6_971")

    Sleep(2000)

    label("loc_976")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B1")
    SetChrPos(0xFE, 55960, 1500, 73110, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xDB24, 0x5DC, 0xDA66, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_976")

    label("loc_9B1")

    Return()

    # Function_6_971 end

    def Function_7_9B2(): pass

    label("Function_7_9B2")

    Sleep(4000)

    label("loc_9B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F2")
    SetChrPos(0xFE, 55960, 1500, 73110, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xDB24, 0x5DC, 0xDA66, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_9B7")

    label("loc_9F2")

    Return()

    # Function_7_9B2 end

    def Function_8_9F3(): pass

    label("Function_8_9F3")

    Sleep(5800)

    label("loc_9F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0xFE, 55960, 1500, 73110, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xDB24, 0x5DC, 0xDA66, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_9F8")

    label("loc_A33")

    Return()

    # Function_8_9F3 end

    def Function_9_A34(): pass

    label("Function_9_A34")

    Sleep(1000)

    label("loc_A39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A74")
    SetChrPos(0xFE, 62020, 1500, 72930, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xF294, 0x5DC, 0xDD4A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_A39")

    label("loc_A74")

    Return()

    # Function_9_A34 end

    def Function_10_A75(): pass

    label("Function_10_A75")

    Sleep(3000)

    label("loc_A7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB5")
    SetChrPos(0xFE, 62020, 1500, 72930, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xF294, 0x5DC, 0xDD4A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_A7A")

    label("loc_AB5")

    Return()

    # Function_10_A75 end

    def Function_11_AB6(): pass

    label("Function_11_AB6")

    Sleep(4800)

    label("loc_ABB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF6")
    SetChrPos(0xFE, 62020, 1500, 72930, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xF294, 0x5DC, 0xDD4A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_ABB")

    label("loc_AF6")

    Return()

    # Function_11_AB6 end

    def Function_12_AF7(): pass

    label("Function_12_AF7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x583, 1)"), scpexpr(EXPR_END)), "loc_B6B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x83\x05\x07\x00。\x02",
    )

    Jump("loc_B50")

    label("loc_B50")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB0)
    Jump("loc_BD9")

    label("loc_B6B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x83\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x83\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_BBA")

    label("loc_BBA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_BD9")

    Jump("loc_C0F")

    label("loc_BDC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C0F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_AF7 end

    def Function_13_C1D(): pass

    label("Function_13_C1D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D02")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DA, 1)"), scpexpr(EXPR_END)), "loc_C91")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xDA\x02\x07\x00。\x02",
    )

    Jump("loc_C76")

    label("loc_C76")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB1)
    Jump("loc_CFF")

    label("loc_C91")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xDA\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDA\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_CE0")

    label("loc_CE0")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_CFF")

    Jump("loc_D35")

    label("loc_D02")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D35")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_C1D end

    def Function_14_D43(): pass

    label("Function_14_D43")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E28")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DB, 1)"), scpexpr(EXPR_END)), "loc_DB7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xDB\x02\x07\x00。\x02",
    )

    Jump("loc_D9C")

    label("loc_D9C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB2)
    Jump("loc_E25")

    label("loc_DB7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xDB\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDB\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_E06")

    label("loc_E06")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_E25")

    Jump("loc_E5B")

    label("loc_E28")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E5B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_D43 end

    def Function_15_E69(): pass

    label("Function_15_E69")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x52A, 1)"), scpexpr(EXPR_END)), "loc_EDD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x2A\x05\x07\x00。\x02",
    )

    Jump("loc_EC2")

    label("loc_EC2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB3)
    Jump("loc_F4B")

    label("loc_EDD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x2A\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x2A\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_F2C")

    label("loc_F2C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_F4B")

    Jump("loc_F81")

    label("loc_F4E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F81")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_E69 end

    def Function_16_F8F(): pass

    label("Function_16_F8F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1074")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B8, 1)"), scpexpr(EXPR_END)), "loc_1003")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xB8\x01\x07\x00。\x02",
    )

    Jump("loc_FE8")

    label("loc_FE8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB4)
    Jump("loc_1071")

    label("loc_1003")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xB8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xB8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1052")

    label("loc_1052")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_1071")

    Jump("loc_10A7")

    label("loc_1074")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_F8F end

    def Function_17_10B5(): pass

    label("Function_17_10B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A8, 1)"), scpexpr(EXPR_END)), "loc_1129")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xA8\x01\x07\x00。\x02",
    )

    Jump("loc_110E")

    label("loc_110E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB5)
    Jump("loc_1197")

    label("loc_1129")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xA8\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA8\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1178")

    label("loc_1178")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_1197")

    Jump("loc_11CD")

    label("loc_119A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_10B5 end

    def Function_18_11DB(): pass

    label("Function_18_11DB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x617, 1)"), scpexpr(EXPR_END)), "loc_124F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\x17\x06\x07\x00。\x02",
    )

    Jump("loc_1234")

    label("loc_1234")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB6)
    Jump("loc_12BD")

    label("loc_124F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\x17\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x17\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_129E")

    label("loc_129E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_12BD")

    Jump("loc_12F3")

    label("loc_12C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12F3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_11DB end

    def Function_19_1301(): pass

    label("Function_19_1301")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    AddSepith(0x0, 0x3E8)
    AddSepith(0x1, 0x3E8)
    AddSepith(0x2, 0x3E8)
    AddSepith(0x3, 0x3E8)
    AddSepith(0x4, 0x3E8)
    AddSepith(0x5, 0x3E8)
    AddSepith(0x6, 0x3E8)

    AnonymousTalk(    #21
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１０００\x01",
            "\x07\x02#57I水之耀晶片×１０００\x01",
            "\x07\x02#58I火之耀晶片×１０００\x01",
            "\x07\x02#59I风之耀晶片×１０００\x01",
            "\x07\x02#62I时之耀晶片×１０００\x01",
            "\x07\x02#60I空之耀晶片×１０００\x01",
            "\x07\x02#61I幻之耀晶片×１０００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2B3C)
    OP_64(0xF, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_19_1301 end

    def Function_20_1425(): pass

    label("Function_20_1425")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x50, 0x2)
    OP_E0(238, 0x51, 0x3)
    OP_E0(239, 0x52, 0x2)
    OP_E0(239, 0x53, 0x3)
    OP_E0(240, 0x54, 0x2)
    OP_E0(240, 0x55, 0x3)
    OP_E0(241, 0x56, 0x2)
    OP_E0(241, 0x57, 0x3)
    SetChrPos(0x109, 64099, 0, 49420, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    SetChrPos(0xEF, 64069, 0, 47900, 315)
    SetChrPos(0xF0, 65710, 0, 49570, 315)
    SetChrPos(0xF1, 65489, 0, 47710, 315)
    Jump("loc_1533")

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F2")
    SetChrPos(0xF0, 64069, 0, 47900, 315)
    SetChrPos(0xEF, 65710, 0, 49570, 315)
    SetChrPos(0xF1, 65489, 0, 47710, 315)
    Jump("loc_1533")

    label("loc_14F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")
    SetChrPos(0xF1, 64069, 0, 47900, 315)
    SetChrPos(0xEF, 65710, 0, 49570, 315)
    SetChrPos(0xF0, 65489, 0, 47710, 315)

    label("loc_1533")

    OP_6D(53360, 3250, 60960, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(382, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1580():
        OP_6D(66130, 0, 49810, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1580)

    def lambda_1598():
        OP_67(0, 6740, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1598)

    def lambda_15B0():
        OP_6B(2350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15B0)

    def lambda_15C0():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15C0)

    def lambda_15D0():
        OP_6E(323, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_15D0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x10A,
        (
            "#1317F#11P人形兵器的零件工场……\x02\x03",

            "不过，这果然是……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x12F, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #23
        0x109,
        (
            "#1063F#5P……和那时候一样，\x01",
            "很快就有人来迎接了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10A,
        "#814F#11P咦……\x02",
    )

    CloseMessageWindow()
    OP_1D(0x97)

    def lambda_16C1():
        OP_6D(62270, 0, 49550, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16C1)

    def lambda_16D9():
        OP_67(0, 6260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16D9)

    def lambda_16F1():
        OP_6B(2500, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16F1)

    def lambda_1701():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1701)

    def lambda_1711():
        OP_6E(349, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_1711)
    OP_43(0x13, 0x0, 0x0, 0x15)
    OP_43(0x14, 0x0, 0x0, 0x16)
    OP_43(0x15, 0x0, 0x0, 0x17)

    def lambda_1736():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1736)
    Sleep(100)

    def lambda_1749():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1749)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178A")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17F1")

    label("loc_178A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B2")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17F1")

    label("loc_17B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DA")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17F1")

    label("loc_17DA")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17F1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181E")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1885")

    label("loc_181E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1846")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1885")

    label("loc_1846")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1885")

    label("loc_186E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1885")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B2")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1919")

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1919")

    label("loc_18DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1902")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1919")

    label("loc_1902")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1919")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 16)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 18)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 20)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 22)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #25
        0x10A,
        "#812F#11P唔……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1069F#5P稍后再说……！\x01",
            "先解决掉这些吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_19DB():
        OP_6D(62230, 0, 49370, 200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_19DB)

    def lambda_19F3():
        OP_67(0, 6470, -10000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_19F3)

    def lambda_1A0B():
        OP_6B(1970, 200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1A0B)

    def lambda_1A1B():
        OP_6E(320, 200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1A1B)
    SetChrChipByIndex(0x13, 1)
    SetChrChipByIndex(0x14, 1)
    SetChrChipByIndex(0x15, 1)

    def lambda_1A3A():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1A3A)

    def lambda_1A55():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1A55)

    def lambda_1A70():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1A70)

    def lambda_1A8B():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1A8B)

    def lambda_1AA6():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1AA6)

    def lambda_1AC1():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1AC1)

    def lambda_1ADC():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1ADC)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A1, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x50, 0x2)
    OP_E0(238, 0x51, 0x3)
    OP_E0(239, 0x52, 0x2)
    OP_E0(239, 0x53, 0x3)
    OP_E0(240, 0x54, 0x2)
    OP_E0(240, 0x55, 0x3)
    OP_E0(241, 0x56, 0x2)
    OP_E0(241, 0x57, 0x3)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 64099, 0, 49420, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCF")
    SetChrPos(0xEF, 64069, 0, 47900, 270)
    SetChrPos(0xF0, 65710, 0, 49570, 270)
    SetChrPos(0xF1, 65489, 0, 47710, 270)
    Jump("loc_1C54")

    label("loc_1BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C13")
    SetChrPos(0xF0, 64069, 0, 47900, 270)
    SetChrPos(0xEF, 65710, 0, 49570, 270)
    SetChrPos(0xF1, 65489, 0, 47710, 270)
    Jump("loc_1C54")

    label("loc_1C13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C54")
    SetChrPos(0xF1, 64069, 0, 47900, 270)
    SetChrPos(0xEF, 65710, 0, 49570, 270)
    SetChrPos(0xF0, 65489, 0, 47710, 270)

    label("loc_1C54")

    SetChrChipByIndex(0xEE, 16)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 18)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 20)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 22)
    SetChrSubChip(0xF1, 0)
    OP_6D(61290, 0, 49600, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)

    def lambda_1CBF():
        OP_6D(65970, 0, 49830, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CBF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        (
            "#1841F#5P『结社』的小型人形兵器……\x01",
            "是相当强的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D76")

    ChrTalk(    #28
        0x107,
        (
            "#065F#11P刚、刚才那个……\x01",
            "好像是镜面装甲的一种。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCB")

    label("loc_1D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCB")

    ChrTalk(    #29
        0x10F,
        (
            "#1443F#11P那是……\x01",
            "好像是和『梅尔卡瓦』一样的\x01",
            "镜面装甲吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(    #30
        0x102,
        (
            "#1503F#11P新型的哨兵……\x01",
            "这型号似乎没见过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1E14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E51")

    ChrTalk(    #31
        0x110,
        (
            "#267F#11P嗯……\x01",
            "是没见过的型号呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F34")

    ChrTalk(    #32
        0x10A,
        (
            "#1316F#11P呼……吓了一大跳。\x02\x03",

            "#816F不过，暂且不谈刚才的人形兵器，\x01",
            "这样一来的话就搞清楚了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F#11P嗯……\x01",
            "看来建筑的结构\x01",
            "好像左右反转了。\x02\x03",

            "#1002F正像是映在镜子里一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2009")

    label("loc_1F34")


    ChrTalk(    #34
        0x10A,
        (
            "#1316F#11P呼……吓了一大跳。\x02\x03",

            "#816F不过，暂且不谈刚才的人形兵器，\x01",
            "这样一来的话就搞清楚了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1065F#5P啊啊……\x01",
            "看来建筑的结构\x01",
            "好像左右反转了啊。\x02\x03",

            "#1063F正像是映在镜子里一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2304")

    ChrTalk(    #36
        0x110,
        (
            "#263F#11P嘻嘻，大家好迟钝哦。\x02\x03",

            "#1306F玲从看第一眼的时候\x01",
            "就已经知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")

    ChrTalk(    #37
        0x101,
        (
            "#1019F#11P你、你啊……\x01",
            "既然发现了就早说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x110,
        (
            "#261F#11P哎呀，艾丝蒂尔真是的。\x02\x03",

            "#265F马上就说出答案来\x01",
            "多无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_210F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(    #39
        0x10F,
        (
            "#1446F#11P……真是的。\x02\x01",

            "#1801F既然发现了\x01",
            "不是应该早点说出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x110,
        (
            "#261F#11P哎呀，大姐姐真是的。\x02\x03",

            "#265F马上就说出答案来\x01",
            "多无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_21C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225E")

    ChrTalk(    #41
        0x102,
        (
            "#1500F#11P原来如此……\x01",
            "以你的记忆力来说是理所当然的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x110,
        (
            "#261F#11P嗯嗯，玲只要看过东西一次\x01",
            "就绝不会轻易忘记的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_225E")


    ChrTalk(    #43
        0x109,
        (
            "#1068F#5P你啊……\x01",
            "既然发现了就早说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x110,
        (
            "#261F#11P哎呀，大哥哥真是的。\x02\x03",

            "#265F马上就说出答案来\x01",
            "多无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E4")


    ChrTalk(    #45
        0x10A,
        "#819F#11P啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_2304")

    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x109,
        (
            "#1065F#5P……唉，无论如何，\x01",
            "除此以外似乎还有很多机关啊。\x02\x03",

            "#1063F小心谨慎地开始探索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        "#812F好！\x02",
    )

    Jump("loc_23DF")

    label("loc_23DF")

    CloseMessageWindow()
    OP_A2(0x2B0D)
    OP_28(0x38, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_20_1425 end

    def Function_21_23F1(): pass

    label("Function_21_23F1")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2418():

        label("loc_2418")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2418")

    QueueWorkItem2(0xFE, 3, lambda_2418)

    def lambda_242B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_242B)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE1DC, 0x0, 0xC166, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_23F1 end

    def Function_22_2471(): pass

    label("Function_22_2471")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_249D():

        label("loc_249D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_249D")

    QueueWorkItem2(0xFE, 3, lambda_249D)

    def lambda_24B0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24B0)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE43E, 0x0, 0xB914, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_2471 end

    def Function_23_24F6(): pass

    label("Function_23_24F6")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2522():

        label("loc_2522")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2522")

    QueueWorkItem2(0xFE, 3, lambda_2522)

    def lambda_2535():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2535)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xDD36, 0x0, 0xBA90, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_23_24F6 end

    def Function_24_257B(): pass

    label("Function_24_257B")

    Call(0, 25)
    Call(0, 28)
    Return()

    # Function_24_257B end

    def Function_25_2584(): pass

    label("Function_25_2584")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x50, 0x2)
    OP_E0(238, 0x51, 0x3)
    OP_E0(239, 0x52, 0x2)
    OP_E0(239, 0x53, 0x3)
    OP_E0(240, 0x54, 0x2)
    OP_E0(240, 0x55, 0x3)
    OP_E0(241, 0x56, 0x2)
    OP_E0(241, 0x57, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 76870, 0, 164890, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 76060, 0, 154530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2669")
    SetChrPos(0xEF, 77650, 0, 154420, 0)
    SetChrPos(0xF0, 75720, 0, 152900, 0)
    SetChrPos(0xF1, 77790, 0, 152850, 0)
    Jump("loc_26EE")

    label("loc_2669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AD")
    SetChrPos(0xF0, 77650, 0, 154420, 0)
    SetChrPos(0xEF, 75720, 0, 152900, 0)
    SetChrPos(0xF1, 77790, 0, 152850, 0)
    Jump("loc_26EE")

    label("loc_26AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26EE")
    SetChrPos(0xF1, 77650, 0, 154420, 0)
    SetChrPos(0xEF, 75720, 0, 152900, 0)
    SetChrPos(0xF0, 77790, 0, 152850, 0)

    label("loc_26EE")

    OP_6D(77580, 0, 154540, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(45000, 0)
    OP_6E(252, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #48
        0x10,
        "青年的声音",
        (
            "#4P哈哈……\x02\x03",

            "结构反过来之后\x01",
            "果然让你们有点迷惑吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CF")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_27CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_27F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_281F")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2836")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2863")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_2863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_288B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_28B3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28CA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_295E")

    label("loc_28F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_295E")

    label("loc_291F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2947")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_295E")

    label("loc_2947")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_295E")

    Sleep(1000)

    def lambda_2969():
        OP_6D(77590, 0, 165390, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2969)

    def lambda_2981():
        OP_67(0, 7120, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2981)

    def lambda_2999():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2999)

    def lambda_29A9():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_29A9)

    def lambda_29B9():
        OP_6E(242, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_29B9)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #49
        0x10A,
        "#1317F#1P库拉茨前辈……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(77940, 0, 162080, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)

    def lambda_2A3B():
        OP_8F(0xFE, 0x12980, 0x0, 0x26B1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A3B)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC1")

    def lambda_2A69():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2A69)
    Sleep(100)

    def lambda_2A89():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2A89)
    Sleep(100)

    def lambda_2AA9():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2AA9)
    Jump("loc_2B96")

    label("loc_2AC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2D")

    def lambda_2AD5():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2AD5)
    Sleep(100)

    def lambda_2AF5():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2AF5)
    Sleep(100)

    def lambda_2B15():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2B15)
    Jump("loc_2B96")

    label("loc_2B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B96")

    def lambda_2B41():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2B41)
    Sleep(100)

    def lambda_2B61():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2B61)
    Sleep(100)

    def lambda_2B81():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2B81)

    label("loc_2B96")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #50
        0x10,
        (
            "#821F#5P哦……\x01",
            "那时的神父也在一起啊。\x02\x03",

            "没想到会在这种状况下\x01",
            "和你们交手。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C49")

    ChrTalk(    #51
        0x103,
        (
            "#1522F#6P果然，\x01",
            "你也不是本人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2C49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C86")

    ChrTalk(    #52
        0x106,
        (
            "#057F#6P果然，\x01",
            "你也不是本人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CC3")

    ChrTalk(    #53
        0x108,
        (
            "#072F#6P果然，\x01",
            "你也不是本人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D07")

    ChrTalk(    #54
        0x102,
        (
            "#1502F#6P果然库拉茨前辈\x01",
            "也不是本人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2D07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D52")

    ChrTalk(    #55
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "果然库拉茨前辈\x01",
            "也不是本人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7F")

    label("loc_2D52")


    ChrTalk(    #56
        0x109,
        (
            "#1063F#6P果然，\x01",
            "你也不是本人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")


    ChrTalk(    #57
        0x10,
        (
            "#820F#5P嗯……\x01",
            "不过，也差不多啦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 9)

    def lambda_2DD7():

        label("loc_2DD7")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2DD7")

    QueueWorkItem2(0x10, 3, lambda_2DD7)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_2E26():
        OP_6D(77670, 0, 160700, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2E26)

    def lambda_2E3E():
        OP_67(0, 6200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2E3E)

    def lambda_2E56():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2E56)

    def lambda_2E66():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E66)

    def lambda_2E76():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2E76)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 71270, 0, 158340, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 82300, 0, 158360, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F26")

    def lambda_2F08():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2F08)
    Sleep(50)

    def lambda_2F1B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2F1B)
    Jump("loc_2F87")

    label("loc_2F26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F58")

    def lambda_2F3A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2F3A)
    Sleep(50)

    def lambda_2F4D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_2F4D)
    Jump("loc_2F87")

    label("loc_2F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F87")

    def lambda_2F6C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2F6C)
    Sleep(50)

    def lambda_2F7F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_2F7F)

    label("loc_2F87")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 71270, -3000, 158340, 90)
    SetChrPos(0x12, 82300, -3000, 158360, 270)
    OP_22(0x85, 0x1, 0x64)

    def lambda_2FBE():

        label("loc_2FBE")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2FBE")

    QueueWorkItem2(0x109, 3, lambda_2FBE)
    OP_43(0x11, 0x0, 0x0, 0x1A)
    OP_43(0x12, 0x0, 0x0, 0x1B)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_44(0x109, 0x3)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0xEE, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_30B3")

    label("loc_304C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3074")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_30B3")

    label("loc_3074")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_30B3")

    label("loc_309C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_30B3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3147")

    label("loc_30E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3108")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3147")

    label("loc_3108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3130")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3147")

    label("loc_3130")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3147")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3174")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31DB")

    label("loc_3174")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31DB")

    label("loc_319C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_31DB")

    label("loc_31C4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_31DB")

    Sleep(1000)

    ChrTalk(    #58
        0x109,
        "#1069F#6P什……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326C")

    ChrTalk(    #59
        0x10A,
        "#1317F#6P难、难不成……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1005F#6P是库拉茨前辈\x01",
            "变装过的假猎兵！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B8")

    label("loc_326C")


    ChrTalk(    #61
        0x10A,
        (
            "#1317F#6P难、难不成……\x02\x03",

            "是库拉茨前辈\x01",
            "变装过的假猎兵！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B8")


    ChrTalk(    #62
        0x10,
        (
            "#823F#5P嘿嘿，\x01",
            "要是和之前一样就太过平淡无奇了。\x02\x03",

            "#821F让我好好开心一下吧！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 16)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 18)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 20)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 22)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_337B():
        OP_6D(77870, 0, 159490, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_337B)

    def lambda_3393():
        OP_67(0, 6520, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3393)

    def lambda_33AB():
        OP_6B(2330, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_33AB)

    def lambda_33BB():
        OP_6E(275, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_33BB)
    SetChrChipByIndex(0x10, 7)

    def lambda_33D0():
        OP_8F(0xFE, 0x12C78, 0x0, 0x26E1C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_33D0)
    SetChrChipByIndex(0x11, 11)

    def lambda_33F0():
        OP_8F(0xFE, 0x1258E, 0x0, 0x268CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_33F0)
    SetChrChipByIndex(0x12, 11)

    def lambda_3410():
        OP_8F(0xFE, 0x132CC, 0x0, 0x268CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3410)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A2, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_25_2584 end

    def Function_26_3447(): pass

    label("Function_26_3447")

    PlayEffect(0x1, 0x4, 0xFF, 71270, 0, 158340, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_26_3447 end

    def Function_27_349C(): pass

    label("Function_27_349C")

    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 82300, 0, 158360, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_349C end

    def Function_28_34F6(): pass

    label("Function_28_34F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 76870, 0, 164890, 180)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0x1D)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 100, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, 76220, 0, 161830, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3612")
    SetChrPos(0xEF, 77580, 0, 161540, 0)
    SetChrPos(0xF0, 75850, 0, 160090, 0)
    SetChrPos(0xF1, 77510, 0, 159980, 0)
    Jump("loc_3697")

    label("loc_3612")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3656")
    SetChrPos(0xF0, 77580, 0, 161540, 0)
    SetChrPos(0xEF, 75850, 0, 160090, 0)
    SetChrPos(0xF1, 77510, 0, 159980, 0)
    Jump("loc_3697")

    label("loc_3656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3697")
    SetChrPos(0xF1, 77580, 0, 161540, 0)
    SetChrPos(0xEF, 75850, 0, 160090, 0)
    SetChrPos(0xF0, 77510, 0, 159980, 0)

    label("loc_3697")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(77790, 0, 163580, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(2510, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #63
        0x10,
        (
            "#824F#5P唔，\x01",
            "包围你们的时候我还以为赢定了……\x02\x03",

            "#825F不过亚妮拉丝，\x01",
            "你本事进步了不少啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#819F#6P嘿嘿，\x01",
            "平时就一直受前辈们指导嘛。\x02\x03",

            "#813F嗯……\x01",
            "你要走了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#823F#5P啊，看来是的。\x02\x03",

            "#825F在上面等待的家伙……\x01",
            "嗯，你们应该可以想像得到吧。\x02\x03",

            "既然已经赢了我，\x01",
            "可别那么容易就输了哦？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 0, -500, 0, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_38BA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_38BA)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    OP_6D(78070, 0, 162360, 1500)
    Sleep(300)

    ChrTalk(    #66
        0x10A,
        "#1317F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393E")

    ChrTalk(    #67
        0x103,
        "#1525F#6P哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_393E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3975")

    ChrTalk(    #68
        0x101,
        (
            "#1007F#6P唉……\x01",
            "真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3975")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B9")

    ChrTalk(    #69
        0x106,
        (
            "#551F#6P那个家伙……\x01",
            "完全没有手下留情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B9")


    ChrTalk(    #70
        0x109,
        (
            "#1065F#6P嗯，\x01",
            "虽然辛苦不过总算撑过来了。\x02\x03",

            "#1063F不过看起来……\x01",
            "下一个对手也很厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 270, 400)
    Sleep(300)

    ChrTalk(    #71
        0x10A,
        (
            "#815F#11P嗯嗯……\x01",
            "拿出斗志往上冲吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0E)
    OP_28(0x38, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_28_34F6 end

    def Function_29_3A70(): pass

    label("Function_29_3A70")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A91")
    Sleep(100)
    Jump("loc_3B0C")

    label("loc_3A91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA6")
    Sleep(200)
    Jump("loc_3B0C")

    label("loc_3AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABB")
    Sleep(300)
    Jump("loc_3B0C")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD0")
    Sleep(400)
    Jump("loc_3B0C")

    label("loc_3AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE5")
    Sleep(500)
    Jump("loc_3B0C")

    label("loc_3AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AFA")
    Sleep(600)
    Jump("loc_3B0C")

    label("loc_3AFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0C")
    Sleep(700)

    label("loc_3B0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B2E")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_3B0C")

    label("loc_3B2E")

    Return()

    # Function_29_3A70 end

    def Function_30_3B2F(): pass

    label("Function_30_3B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4344")
    EventBegin(0x0)
    Fade(500)
    OP_6D(77550, 0, 168460, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 76810, 0, 168160, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD0")
    SetChrPos(0xEF, 76470, 0, 166800, 0)
    SetChrPos(0xF0, 75500, 0, 165530, 0)
    SetChrPos(0xF1, 77140, 0, 165800, 0)
    Jump("loc_3C55")

    label("loc_3BD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C14")
    SetChrPos(0xF0, 76470, 0, 166800, 0)
    SetChrPos(0xEF, 75500, 0, 165530, 0)
    SetChrPos(0xF1, 77140, 0, 165800, 0)
    Jump("loc_3C55")

    label("loc_3C14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C55")
    SetChrPos(0xF1, 76470, 0, 166800, 0)
    SetChrPos(0xEF, 75500, 0, 165530, 0)
    SetChrPos(0xF0, 77140, 0, 165800, 0)

    label("loc_3C55")

    OP_0D()
    Sleep(300)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x17, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        (
            "\x07\x02#1S#40W铁之川奔腾流逝。\x01",
            "调查操纵此奔流的\x01",
            "六道水门之一吧。\x01",
            "如此汝即可获得光辉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x07\x00得到了\x1F\x2F\x03\x07\x00。\x02",
    )

    Jump("loc_3D2B")

    label("loc_3D2B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32F, 1)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8E")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF5")

    label("loc_3D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB6")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF5")

    label("loc_3DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DDE")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3DF5")

    label("loc_3DDE")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3DF5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E22")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E89")

    label("loc_3E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E89")

    label("loc_3E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E72")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E89")

    label("loc_3E72")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E89")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB6")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F1D")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EDE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F1D")

    label("loc_3EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F06")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F1D")

    label("loc_3F06")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3F1D")

    Sleep(1000)

    ChrTalk(    #74
        0x10A,
        (
            "#1317F#6P虽然卡片钥匙\x01",
            "已经到手了……\x02\x03",

            "不过刚才的文字，难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        (
            "#1840F#6P啊啊，\x01",
            "似乎是终端的信息反转过来显示的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(    #76
        0x107,
        (
            "#065F#6P而、而且连文字的流向\x01",
            "也反过来了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_403A")

    ChrTalk(    #77
        0x10C,
        (
            "#110F#6P呵呵……\x01",
            "做得真是细致啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_403A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4075")

    ChrTalk(    #78
        0x10D,
        (
            "#277F#6P哼……\x01",
            "无聊的执着啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_4075")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B3")

    ChrTalk(    #79
        0x104,
        (
            "#1541F#6P呵……\x01",
            "做得真是细致呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_40B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40F6")

    ChrTalk(    #80
        0x10E,
        (
            "#179F#6P哎呀哎呀……\x01",
            "做得真是细致啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_40F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4135")

    ChrTalk(    #81
        0x10B,
        (
            "#413F#6P唉……\x01",
            "真是细致得无聊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_4135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_416A")

    ChrTalk(    #82
        0x105,
        "#1165F#6P相当执着呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_416A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A3")

    ChrTalk(    #83
        0x10F,
        "#1806F#6P……做得真细致呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_41A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E3")

    ChrTalk(    #84
        0x103,
        (
            "#1534F#6P唉……\x01",
            "真是细致得无聊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_41E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4226")

    ChrTalk(    #85
        0x106,
        (
            "#555F#6P真是的……\x01",
            "莫名奇妙地执着啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_4226")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4267")

    ChrTalk(    #86
        0x108,
        (
            "#070F#6P哈哈……\x01",
            "莫名奇妙地执着啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_4267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_429E")

    ChrTalk(    #87
        0x102,
        "#1505F#6P做得真细致呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_42DF")

    label("loc_429E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DF")

    ChrTalk(    #88
        0x101,
        (
            "#1007F#6P真是的……\x01",
            "真是细致得无聊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4323")

    ChrTalk(    #89
        0x110,
        (
            "#261F#6P嘻嘻，\x01",
            "玲倒是不讨厌这种孩子气呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4323")

    OP_A2(0x2B0F)
    OP_28(0x38, 0x1, 0x20)
    OP_74(0x17, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_4400")

    label("loc_4344")

    TalkBegin(0xFF)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x17, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #90
        (
            "\x07\x02#1S#40W铁之川奔腾流逝。\x01",
            "调查操纵此奔流的\x01",
            "六道水门之一吧。\x01",
            "如此汝即可获得光辉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    FadeToBright(300, 0)
    OP_74(0x17, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    TalkEnd(0xFF)

    label("loc_4400")

    Return()

    # Function_30_3B2F end

    def Function_31_4401(): pass

    label("Function_31_4401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D0")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5376)
    Sleep(500)
    Jump("loc_44D3")

    label("loc_44D0")

    TalkBegin(0xFF)

    label("loc_44D3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_44FD")

    label("loc_44FD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4668")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_4562")

    label("loc_4562")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_457F"),
        (1, "loc_45FA"),
        (2, "loc_4629"),
        (SWITCH_DEFAULT, "loc_4658"),
    )


    label("loc_457F")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4665")

    label("loc_45FA")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4626")

    label("loc_4626")

    Jump("loc_4665")

    label("loc_4629")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_4655")

    label("loc_4655")

    Jump("loc_4665")

    label("loc_4658")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4665")

    label("loc_4665")

    Jump("loc_4510")

    label("loc_4668")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4695")
    OP_A2(0x2598)
    EventEnd(0x1)
    Jump("loc_4698")

    label("loc_4695")

    TalkEnd(0xFF)

    label("loc_4698")

    Return()

    # Function_31_4401 end

    def Function_32_4699(): pass

    label("Function_32_4699")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【搬动拉杆】\x01",        # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4748")
    Sleep(200)
    OP_B0(0x18, 0x3C)
    OP_6F(0x4, 1)
    OP_70(0x18, 0x3C)
    OP_22(0x64, 0x0, 0x64)
    OP_73(0x18)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2B58)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_474A")

    label("loc_4748")

    EventEnd(0x1)

    label("loc_474A")

    Jump("loc_47F7")

    label("loc_474D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【搬动拉杆】\x01",        # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F5")
    Sleep(200)
    OP_B0(0x18, 0x3C)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x1)
    OP_73(0x18)
    OP_22(0x64, 0x0, 0x64)
    OP_73(0x18)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x2B58)
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_47F7")

    label("loc_47F5")

    EventEnd(0x1)

    label("loc_47F7")

    Return()

    # Function_32_4699 end

    def Function_33_47F8(): pass

    label("Function_33_47F8")

    EventBegin(0x0)
    SetChrPos(0x0, 11920, 0, -18990, 90)
    SetChrPos(0x1, 11920, 0, -18990, 90)
    SetChrPos(0x2, 11920, 0, -18990, 90)
    SetChrPos(0x3, 11920, 0, -18990, 90)
    OP_6D(11920, 0, -18990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_33_47F8 end

    def Function_34_4887(): pass

    label("Function_34_4887")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #94
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_4887 end

    def Function_35_48E4(): pass

    label("Function_35_48E4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495A")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_64(0x3, 0x1)
    OP_10(0x1F, 0x1)
    OP_A2(0x2B59)
    Jump("loc_497E")

    label("loc_495A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_497E")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_497E")

    label("loc_497E")

    TalkEnd(0xFF)
    Return()

    # Function_35_48E4 end

    def Function_36_4982(): pass

    label("Function_36_4982")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F8")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x1E)
    OP_73(0x11)
    OP_64(0x4, 0x1)
    OP_10(0x20, 0x1)
    OP_A2(0x2B5A)
    Jump("loc_4A1C")

    label("loc_49F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A1C")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_4A1C")

    label("loc_4A1C")

    TalkEnd(0xFF)
    Return()

    # Function_36_4982 end

    def Function_37_4A20(): pass

    label("Function_37_4A20")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A96")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_64(0x5, 0x1)
    OP_10(0x5, 0x1)
    OP_A2(0x2B5B)
    Jump("loc_4ABA")

    label("loc_4A96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ABA")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_4ABA")

    label("loc_4ABA")

    TalkEnd(0xFF)
    Return()

    # Function_37_4A20 end

    def Function_38_4ABE(): pass

    label("Function_38_4ABE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #98
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3A")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_71(0x20D, 0x0)
    ExitThread()
    OP_64(0x6, 0x1)
    OP_10(0x1D, 0x1)
    OP_A2(0x2B63)
    Jump("loc_4B5E")

    label("loc_4B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B5E")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_4B5E")

    label("loc_4B5E")

    TalkEnd(0xFF)
    Return()

    # Function_38_4ABE end

    def Function_39_4B62(): pass

    label("Function_39_4B62")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_END)), "loc_4B7D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_END)), "loc_4B8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_END)), "loc_4B9F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4B9F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4BCB"),
        (1, "loc_4BD8"),
        (3, "loc_4C36"),
        (7, "loc_4CBA"),
        (SWITCH_DEFAULT, "loc_4D64"),
    )


    label("loc_4BCB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D64")

    label("loc_4BD8")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【什么也不做】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C19"),
        (1, "loc_4C26"),
        (SWITCH_DEFAULT, "loc_4C33"),
    )


    label("loc_4C19")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C33")

    label("loc_4C26")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C33")

    label("loc_4C33")

    Jump("loc_4D64")

    label("loc_4C36")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【什么也不做】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C90"),
        (1, "loc_4C9D"),
        (2, "loc_4CAA"),
        (SWITCH_DEFAULT, "loc_4CB7"),
    )


    label("loc_4C90")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB7")

    label("loc_4C9D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB7")

    label("loc_4CAA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB7")

    label("loc_4CB7")

    Jump("loc_4D64")

    label("loc_4CBA")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【使用蓝色卡片钥匙】\x01",      # 2
            "【什么也不做】\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D2D"),
        (1, "loc_4D3A"),
        (2, "loc_4D47"),
        (3, "loc_4D54"),
        (SWITCH_DEFAULT, "loc_4D61"),
    )


    label("loc_4D2D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D61")

    label("loc_4D3A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D61")

    label("loc_4D47")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D61")

    label("loc_4D54")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D61")

    label("loc_4D61")

    Jump("loc_4D64")

    label("loc_4D64")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_39_4B62 end

    def Function_40_4D7C(): pass

    label("Function_40_4D7C")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_4DD9")

    label("loc_4DD9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_40_4D7C end

    def Function_41_4DF0(): pass

    label("Function_41_4DF0")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 105530, 0, 68810, 90)
    SetChrPos(0x1, 105550, 0, 66900, 90)
    SetChrPos(0x2, 103720, 0, 68840, 90)
    SetChrPos(0x3, 103430, 0, 66730, 90)
    OP_6D(106590, 0, 67810, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC6")
    OP_28(0x14, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4EC6")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4F3D")

    AnonymousTalk(    #100
        (
            "\x07\x05#40W     道路既已打开……\x01",
            "#500W\x01",
            "#40W　   穿越此『门』吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB6")

    label("loc_4F3D")


    AnonymousTalk(    #101
        (
            "\x07\x05#40W   欲通过此『门』之人……\x01",
            "　   前方有试炼降临。\x01",
            "#500W\x01",
            "#40W　 　 若汝有此觉悟，\x01",
            "     便可穿越此『门』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB6")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 40)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FDF")
    Call(0, 42)

    label("loc_4FDF")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_41_4DF0 end

    def Function_42_4FEB(): pass

    label("Function_42_4FEB")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x21)
    Sleep(500)

    def lambda_5054():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5054)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x1F, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_4FEB end

    def Function_43_50A1(): pass

    label("Function_43_50A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 105530, 0, 68810, 90)
    SetChrPos(0x1, 105550, 0, 66900, 90)
    SetChrPos(0x2, 103720, 0, 68840, 90)
    SetChrPos(0x3, 103430, 0, 66730, 90)
    OP_6D(106590, 0, 67810, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3740, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_43_50A1 end

    def Function_44_514C(): pass

    label("Function_44_514C")

    OP_A2(0x2B64)
    OP_A3(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_44_514C end

    SaveToFile()

Try(main)
