from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Grant',                                # 9
        'Jaeger Grant',                         # 10
        'Jaeger Grant',                         # 11
        'Mirror Vogel',                         # 12
        'Mirror Vogel',                         # 13
        'Mirror Vogel',                         # 14
        'Parts',                                # 15
        'Parts',                                # 16
        'Parts',                                # 17
        'Parts',                                # 18
        'Parts',                                # 19
        'Parts',                                # 20
        'Parts',                                # 21
        'Parts',                                # 22
        'Parts',                                # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
        '',                                     # 33
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
        "Function_13_C27",         # 0D, 13
        "Function_14_D68",         # 0E, 14
        "Function_15_E9D",         # 0F, 15
        "Function_16_FE2",         # 10, 16
        "Function_17_1139",        # 11, 17
        "Function_18_1286",        # 12, 18
        "Function_19_13CF",        # 13, 19
        "Function_20_14D3",        # 14, 20
        "Function_21_2693",        # 15, 21
        "Function_22_2713",        # 16, 22
        "Function_23_2798",        # 17, 23
        "Function_24_281D",        # 18, 24
        "Function_25_2826",        # 19, 25
        "Function_26_3807",        # 1A, 26
        "Function_27_385C",        # 1B, 27
        "Function_28_38B6",        # 1C, 28
        "Function_29_3F05",        # 1D, 29
        "Function_30_3FC4",        # 1E, 30
        "Function_31_49B3",        # 1F, 31
        "Function_32_4C35",        # 20, 32
        "Function_33_4D8E",        # 21, 33
        "Function_34_4E1D",        # 22, 34
        "Function_35_4E84",        # 23, 35
        "Function_36_4F27",        # 24, 36
        "Function_37_4FCA",        # 25, 37
        "Function_38_506D",        # 26, 38
        "Function_39_5116",        # 27, 39
        "Function_40_530B",        # 28, 40
        "Function_41_5364",        # 29, 41
        "Function_42_558C",        # 2A, 42
        "Function_43_5642",        # 2B, 43
        "Function_44_56ED",        # 2C, 44
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x583, 1)"), scpexpr(EXPR_END)), "loc_B65")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x83\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB0)
    Jump("loc_BCD")

    label("loc_B65")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x83\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x83\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_BCD")

    Jump("loc_C19")

    label("loc_BD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05You take my stuff, I take your stuff!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8E, 0x0)

    label("loc_C19")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_AF7 end

    def Function_13_C27(): pass

    label("Function_13_C27")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D00")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DA, 1)"), scpexpr(EXPR_END)), "loc_C95")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xDA\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB1)
    Jump("loc_CFD")

    label("loc_C95")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xDA\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xDA\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_CFD")

    Jump("loc_D5A")

    label("loc_D00")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Tempting. But the chest is too heavy to take with you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8F, 0x0)

    label("loc_D5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_C27 end

    def Function_14_D68(): pass

    label("Function_14_D68")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E41")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DB, 1)"), scpexpr(EXPR_END)), "loc_DD6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xDB\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB2)
    Jump("loc_E3E")

    label("loc_DD6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xDB\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xDB\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_E3E")

    Jump("loc_E8F")

    label("loc_E41")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Be thankful this chest doesn't have teeth.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x90, 0x0)

    label("loc_E8F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_D68 end

    def Function_15_E9D(): pass

    label("Function_15_E9D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F76")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x52A, 1)"), scpexpr(EXPR_END)), "loc_F0B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x2A\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB3)
    Jump("loc_F73")

    label("loc_F0B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x2A\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x2A\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_F73")

    Jump("loc_FD4")

    label("loc_F76")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05It is said that ignorance is bliss. Tell me, is that true?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x91, 0x0)

    label("loc_FD4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_E9D end

    def Function_16_FE2(): pass

    label("Function_16_FE2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1B8, 1)"), scpexpr(EXPR_END)), "loc_1050")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\xB8\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB4)
    Jump("loc_10B8")

    label("loc_1050")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\xB8\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xB8\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_10B8")

    Jump("loc_112B")

    label("loc_10BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05When I said, 'Give me some space,' this wasn't exactly what I had in\x01",
            "mind...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x92, 0x0)

    label("loc_112B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_FE2 end

    def Function_17_1139(): pass

    label("Function_17_1139")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1212")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A8, 1)"), scpexpr(EXPR_END)), "loc_11A7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Found \x1F\xA8\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB5)
    Jump("loc_120F")

    label("loc_11A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05Found \x1F\xA8\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA8\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_120F")

    Jump("loc_1278")

    label("loc_1212")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05Merchant accidently dropped me here. Please don't leave me alone!!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x93, 0x0)

    label("loc_1278")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1139 end

    def Function_18_1286(): pass

    label("Function_18_1286")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x576, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x617, 1)"), scpexpr(EXPR_END)), "loc_12F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Found \x1F\x17\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB6)
    Jump("loc_135C")

    label("loc_12F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05Found \x1F\x17\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x17\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_135C")

    Jump("loc_13C1")

    label("loc_135F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05I rusted shut a long time ago! You must really be working out.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x94, 0x0)

    label("loc_13C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_18_1286 end

    def Function_19_13CF(): pass

    label("Function_19_13CF")

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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x1000\x01",
            "#57IWater Sepith x1000\x01",
            "#58IFire Sepith x1000\x01",
            "#59IWind Sepith x1000\x01",
            "#62ITime Sepith x1000\x01",
            "#60ISpace Sepith x1000\x01",
            "#61IMirage Sepith x1000.\x02",
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

    # Function_19_13CF end

    def Function_20_14D3(): pass

    label("Function_20_14D3")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155C")
    SetChrPos(0xEF, 64069, 0, 47900, 315)
    SetChrPos(0xF0, 65710, 0, 49570, 315)
    SetChrPos(0xF1, 65489, 0, 47710, 315)
    Jump("loc_15E1")

    label("loc_155C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A0")
    SetChrPos(0xF0, 64069, 0, 47900, 315)
    SetChrPos(0xEF, 65710, 0, 49570, 315)
    SetChrPos(0xF1, 65489, 0, 47710, 315)
    Jump("loc_15E1")

    label("loc_15A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E1")
    SetChrPos(0xF1, 64069, 0, 47900, 315)
    SetChrPos(0xEF, 65710, 0, 49570, 315)
    SetChrPos(0xF0, 65489, 0, 47710, 315)

    label("loc_15E1")

    OP_6D(53360, 3250, 60960, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(382, 0)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_162E():
        OP_6D(66130, 0, 49810, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_162E)

    def lambda_1646():
        OP_67(0, 6740, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1646)

    def lambda_165E():
        OP_6B(2350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_165E)

    def lambda_166E():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_166E)

    def lambda_167E():
        OP_6E(323, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_167E)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x10A,
        (
            "#1317F#11PThe archaism parts factory?\x02\x03",

            "But this was... Wait. Then...\x02",
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
        "#1063F#5PHere to greet us already, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10A,
        "#814F#11PWha...?\x02",
    )

    CloseMessageWindow()
    OP_1D(0x97)

    def lambda_1759():
        OP_6D(62270, 0, 49550, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1759)

    def lambda_1771():
        OP_67(0, 6260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1771)

    def lambda_1789():
        OP_6B(2500, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1789)

    def lambda_1799():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1799)

    def lambda_17A9():
        OP_6E(349, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_17A9)
    OP_43(0x13, 0x0, 0x0, 0x15)
    OP_43(0x14, 0x0, 0x0, 0x16)
    OP_43(0x15, 0x0, 0x0, 0x17)

    def lambda_17CE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17CE)
    Sleep(100)

    def lambda_17E1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_17E1)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    WaitChrThread(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1822")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1889")

    label("loc_1822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1889")

    label("loc_184A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1872")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1889")

    label("loc_1872")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1889")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_191D")

    label("loc_18B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_191D")

    label("loc_18DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1906")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_191D")

    label("loc_1906")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_191D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19B1")

    label("loc_194A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1972")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19B1")

    label("loc_1972")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19B1")

    label("loc_199A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19B1")

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
        "#812F#11PGah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1069F#5PTalking's gonna have to wait! Let's roll!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1A6D():
        OP_6D(62230, 0, 49370, 200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1A6D)

    def lambda_1A85():
        OP_67(0, 6470, -10000, 200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1A85)

    def lambda_1A9D():
        OP_6B(1970, 200)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1A9D)

    def lambda_1AAD():
        OP_6E(320, 200)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1AAD)
    SetChrChipByIndex(0x13, 1)
    SetChrChipByIndex(0x14, 1)
    SetChrChipByIndex(0x15, 1)

    def lambda_1ACC():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1ACC)

    def lambda_1AE7():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1AE7)

    def lambda_1B02():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1B02)

    def lambda_1B1D():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1B1D)

    def lambda_1B38():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1B38)

    def lambda_1B53():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1B53)

    def lambda_1B6E():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1B6E)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C61")
    SetChrPos(0xEF, 64069, 0, 47900, 270)
    SetChrPos(0xF0, 65710, 0, 49570, 270)
    SetChrPos(0xF1, 65489, 0, 47710, 270)
    Jump("loc_1CE6")

    label("loc_1C61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA5")
    SetChrPos(0xF0, 64069, 0, 47900, 270)
    SetChrPos(0xEF, 65710, 0, 49570, 270)
    SetChrPos(0xF1, 65489, 0, 47710, 270)
    Jump("loc_1CE6")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE6")
    SetChrPos(0xF1, 64069, 0, 47900, 270)
    SetChrPos(0xEF, 65710, 0, 49570, 270)
    SetChrPos(0xF0, 65489, 0, 47710, 270)

    label("loc_1CE6")

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

    def lambda_1D51():
        OP_6D(65970, 0, 49830, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D51)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        "#1841F#5PWhew... Those things sure weren't fun.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF5")

    ChrTalk(    #28
        0x107,
        "#065F#11PTh-They had a kind of reflective armor...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E40")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E40")

    ChrTalk(    #29
        0x10F,
        "#1443F#11PThey had reflective armor like the Merkabahs.\x02",
    )

    CloseMessageWindow()

    label("loc_1E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB5")

    ChrTalk(    #30
        0x102,
        (
            "#1503F#11PThey seemed to be a new model of Vogel,\x01",
            "but it's not a type I've ever seen before...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F01")

    label("loc_1EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F01")

    ChrTalk(    #31
        0x110,
        "#267F#11PThat's not a type of archaism I've seen before.\x02",
    )

    CloseMessageWindow()

    label("loc_1F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200C")

    ChrTalk(    #32
        0x10A,
        (
            "#1316F#11PPhew... Talk about a nasty surprise.\x02\x03",

            "#816FAt least it's now clear as day what's going\x01",
            "on here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F#11PYeah... The whole building's layout has been\x01",
            "flipped around.\x02\x03",

            "#1002FKind of like it was reflected in a mirror or\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2103")

    label("loc_200C")


    ChrTalk(    #34
        0x10A,
        (
            "#1316F#11PWhew... That was a nasty surprise.\x02\x03",

            "#816FAt least it's now clear as day what's going\x01",
            "on here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1065F#5PYeah... The whole building's layout has been\x01",
            "flipped around.\x02\x03",

            "#1063FKind of like it was reflected in a mirror or\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2103")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258E")

    ChrTalk(    #36
        0x110,
        (
            "#263F#11PYou silly thing. Did you really only just figure\x01",
            "that out?\x02\x03",

            "#1306FI realized the second we got a look at the\x01",
            "building from the outside.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(    #37
        0x101,
        (
            "#1019F#11PDid it not occur to you to share that information\x01",
            "with us, or do you just enjoy watching us stumble\x01",
            "around in the dark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x110,
        (
            "#261F#11PHeehee. Oh, I'm sure you know the answer to\x01",
            "that.\x02\x03",

            "#265FBesides, it's best if you try to work things out\x01",
            "before relying on me, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2577")

    label("loc_22D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C3")

    ChrTalk(    #39
        0x10F,
        (
            "#1446F#11PHonestly...\x02\x01",

            "#1801FCould you not have told us earlier, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x110,
        (
            "#261F#11PHeehee. But that would've spoiled the fun!\x02\x03",

            "#265FBesides, it's best if you try to work things out\x01",
            "before relying on me, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2577")

    label("loc_23C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2488")

    ChrTalk(    #41
        0x102,
        (
            "#1500F#11PI suppose it makes sense you'd be the first to\x01",
            "notice. You've always had a good memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x110,
        (
            "#261F#11PYuuup. Once I've seen something once,\x01",
            "I very rarely forget it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2577")

    label("loc_2488")


    ChrTalk(    #43
        0x109,
        (
            "#1068F#5P*sigh* Could you not have just told us?\x01",
            "It would've saved us a lot of trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x110,
        (
            "#261F#11PHeehee. But that would've spoiled the fun!\x02\x03",

            "#265FBesides, it's best if you try to work things out\x01",
            "before relying on me, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2577")


    ChrTalk(    #45
        0x10A,
        "#819F#11PAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_258E")

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
            "#1065F#5P...Well, whatever. It doesn't look like that's\x01",
            "the only trick this place has up its sleeve.\x02\x03",

            "#1063FLet's keep our eyes peeled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        "#812FRight!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B0D)
    OP_28(0x38, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_20_14D3 end

    def Function_21_2693(): pass

    label("Function_21_2693")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_26BA():

        label("loc_26BA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_26BA")

    QueueWorkItem2(0xFE, 3, lambda_26BA)

    def lambda_26CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26CD)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE1DC, 0x0, 0xC166, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_2693 end

    def Function_22_2713(): pass

    label("Function_22_2713")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_273F():

        label("loc_273F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_273F")

    QueueWorkItem2(0xFE, 3, lambda_273F)

    def lambda_2752():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2752)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xE43E, 0x0, 0xB914, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_22_2713 end

    def Function_23_2798(): pass

    label("Function_23_2798")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 55850, 0, 42510, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_27C4():

        label("loc_27C4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_27C4")

    QueueWorkItem2(0xFE, 3, lambda_27C4)

    def lambda_27D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27D7)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0xDAAC, 0x0, 0xB0E0, 0x1388, 0x0)
    OP_8E(0xFE, 0xDD36, 0x0, 0xBA90, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_23_2798 end

    def Function_24_281D(): pass

    label("Function_24_281D")

    Call(0, 25)
    Call(0, 28)
    Return()

    # Function_24_281D end

    def Function_25_2826(): pass

    label("Function_25_2826")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290B")
    SetChrPos(0xEF, 77650, 0, 154420, 0)
    SetChrPos(0xF0, 75720, 0, 152900, 0)
    SetChrPos(0xF1, 77790, 0, 152850, 0)
    Jump("loc_2990")

    label("loc_290B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294F")
    SetChrPos(0xF0, 77650, 0, 154420, 0)
    SetChrPos(0xEF, 75720, 0, 152900, 0)
    SetChrPos(0xF1, 77790, 0, 152850, 0)
    Jump("loc_2990")

    label("loc_294F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2990")
    SetChrPos(0xF1, 77650, 0, 154420, 0)
    SetChrPos(0xEF, 75720, 0, 152900, 0)
    SetChrPos(0xF0, 77790, 0, 152850, 0)

    label("loc_2990")

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
        "Young Man's Voice",
        (
            "#4PHaha... Hey, Anelace.\x02\x03",

            "Glad you made it. I'm guessing everything\x01",
            "being reversed made navigating this place\x01",
            "a pain, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB5")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B1C")

    label("loc_2AB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADD")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B1C")

    label("loc_2ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B05")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B1C")

    label("loc_2B05")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B1C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B49")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2BB0")

    label("loc_2B49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B71")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2BB0")

    label("loc_2B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B99")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2BB0")

    label("loc_2B99")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2BB0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDD")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C44")

    label("loc_2BDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C05")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C44")

    label("loc_2C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C44")

    label("loc_2C2D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C44")

    Sleep(1000)

    def lambda_2C4F():
        OP_6D(77590, 0, 165390, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C4F)

    def lambda_2C67():
        OP_67(0, 7120, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C67)

    def lambda_2C7F():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C7F)

    def lambda_2C8F():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C8F)

    def lambda_2C9F():
        OP_6E(242, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2C9F)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #49
        0x10A,
        "#1317F#1PGrant!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(77940, 0, 162080, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)

    def lambda_2D10():
        OP_8F(0xFE, 0x12980, 0x0, 0x26B1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D10)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D96")

    def lambda_2D3E():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2D3E)
    Sleep(100)

    def lambda_2D5E():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2D5E)
    Sleep(100)

    def lambda_2D7E():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2D7E)
    Jump("loc_2E6B")

    label("loc_2D96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E02")

    def lambda_2DAA():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2DAA)
    Sleep(100)

    def lambda_2DCA():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2DCA)
    Sleep(100)

    def lambda_2DEA():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2DEA)
    Jump("loc_2E6B")

    label("loc_2E02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6B")

    def lambda_2E16():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x26A48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2E16)
    Sleep(100)

    def lambda_2E36():
        OP_8F(0xFE, 0x1271E, 0x0, 0x263AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E36)
    Sleep(100)

    def lambda_2E56():
        OP_8F(0xFE, 0x12F5C, 0x0, 0x2646C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2E56)

    label("loc_2E6B")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #50
        0x10,
        (
            "#821F#5POh, if it isn't the priest who saved our bacon\x01",
            "last time we were here! Funny coincidence.\x02\x03",

            "I wasn't expecting to end up fighting you\x01",
            "here again... Especially not like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(    #51
        0x103,
        "#1522F#6PSo are you not real, either?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C1")

    label("loc_2F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB5")

    ChrTalk(    #52
        0x106,
        "#057F#6PSo are you not real, either?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C1")

    label("loc_2FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF0")

    ChrTalk(    #53
        0x108,
        "#072F#6PSo are you not real, either?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C1")

    label("loc_2FF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_302C")

    ChrTalk(    #54
        0x102,
        "#1502F#6PSo are you not real, either?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C1")

    label("loc_302C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3074")

    ChrTalk(    #55
        0x101,
        "#1015F#6PUmm... You're not the real Grant, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C1")

    label("loc_3074")


    ChrTalk(    #56
        0x109,
        (
            "#1063F#6PCorrect me if I'm wrong, but you're not\x01",
            "the real thing, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C1")


    ChrTalk(    #57
        0x10,
        "#820F#5PYeah... Still, I'm close enough.\x02",
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

    def lambda_3119():

        label("loc_3119")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3119")

    QueueWorkItem2(0x10, 3, lambda_3119)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_3168():
        OP_6D(77670, 0, 160700, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3168)

    def lambda_3180():
        OP_67(0, 6200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3180)

    def lambda_3198():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3198)

    def lambda_31A8():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_31A8)

    def lambda_31B8():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_31B8)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 71270, 0, 158340, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 82300, 0, 158360, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3268")

    def lambda_324A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_324A)
    Sleep(50)

    def lambda_325D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_325D)
    Jump("loc_32C9")

    label("loc_3268")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329A")

    def lambda_327C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_327C)
    Sleep(50)

    def lambda_328F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_328F)
    Jump("loc_32C9")

    label("loc_329A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C9")

    def lambda_32AE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_32AE)
    Sleep(50)

    def lambda_32C1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_32C1)

    label("loc_32C9")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 71270, -3000, 158340, 90)
    SetChrPos(0x12, 82300, -3000, 158360, 270)
    OP_22(0x85, 0x1, 0x64)

    def lambda_3300():

        label("loc_3300")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_3300")

    QueueWorkItem2(0x109, 3, lambda_3300)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_338E")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33F5")

    label("loc_338E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B6")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33F5")

    label("loc_33B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DE")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_33F5")

    label("loc_33DE")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_33F5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3422")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3489")

    label("loc_3422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3489")

    label("loc_344A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3472")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3489")

    label("loc_3472")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3489")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B6")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_351D")

    label("loc_34B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34DE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_351D")

    label("loc_34DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3506")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_351D")

    label("loc_3506")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_351D")

    Sleep(1000)

    ChrTalk(    #58
        0x109,
        "#1069F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CD")

    ChrTalk(    #59
        0x10A,
        "#1317F#6PW-Wait. This is just like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1005F#6P...just like when you were pretending to\x01",
            "be a jaeger during our training!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3643")

    label("loc_35CD")


    ChrTalk(    #61
        0x10A,
        (
            "#1317F#6PW-Wait. This is just like...\x02\x03",

            "...just like when you were pretending to\x01",
            "be a jaeger during our training!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3643")


    ChrTalk(    #62
        0x10,
        (
            "#823F#5PHeh. I wouldn't wanna try pulling the same trick\x01",
            "twice, but I can still have 'em back me up.\x02\x03",

            "#821FSo, come on! Show me what you got!\x02",
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

    def lambda_373B():
        OP_6D(77870, 0, 159490, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_373B)

    def lambda_3753():
        OP_67(0, 6520, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3753)

    def lambda_376B():
        OP_6B(2330, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_376B)

    def lambda_377B():
        OP_6E(275, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_377B)
    SetChrChipByIndex(0x10, 7)

    def lambda_3790():
        OP_8F(0xFE, 0x12C78, 0x0, 0x26E1C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3790)
    SetChrChipByIndex(0x11, 11)

    def lambda_37B0():
        OP_8F(0xFE, 0x1258E, 0x0, 0x268CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_37B0)
    SetChrChipByIndex(0x12, 11)

    def lambda_37D0():
        OP_8F(0xFE, 0x132CC, 0x0, 0x268CC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_37D0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A2, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_25_2826 end

    def Function_26_3807(): pass

    label("Function_26_3807")

    PlayEffect(0x1, 0x4, 0xFF, 71270, 0, 158340, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_26_3807 end

    def Function_27_385C(): pass

    label("Function_27_385C")

    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 82300, 0, 158360, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_27_385C end

    def Function_28_38B6(): pass

    label("Function_28_38B6")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D2")
    SetChrPos(0xEF, 77580, 0, 161540, 0)
    SetChrPos(0xF0, 75850, 0, 160090, 0)
    SetChrPos(0xF1, 77510, 0, 159980, 0)
    Jump("loc_3A57")

    label("loc_39D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A16")
    SetChrPos(0xF0, 77580, 0, 161540, 0)
    SetChrPos(0xEF, 75850, 0, 160090, 0)
    SetChrPos(0xF1, 77510, 0, 159980, 0)
    Jump("loc_3A57")

    label("loc_3A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A57")
    SetChrPos(0xF1, 77580, 0, 161540, 0)
    SetChrPos(0xEF, 75850, 0, 160090, 0)
    SetChrPos(0xF0, 77510, 0, 159980, 0)

    label("loc_3A57")

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
            "#824F#5PMaaan... I thought victory was as good as mine\x01",
            "when I had you surrounded, but I totally under-\x01",
            "estimated you guys.\x02\x03",

            "#825FHoly hell, though, Anelace. You've sure started\x01",
            "packing a real punch since we last fought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#819F#6PHeehee. Well, I've got you and the others to\x01",
            "thank for that.\x02\x03",

            "#813F...Do you really have to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#823F#5PLooks like it, I'm afraid.\x02\x03",

            "#825FI'll bet you don't need too many hints\x01",
            "on who you're gonna be fighting next.\x02\x03",

            "Don't go losing, okay? You beat me!\x01",
            "You've gotta beat the others, too.\x02",
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

    def lambda_3D37():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D37)
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
        "#1317F#6PHe's gone...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC0")

    ChrTalk(    #67
        0x103,
        "#1525F#6PWell, that wraps that up.\x02",
    )

    CloseMessageWindow()

    label("loc_3DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF8")

    ChrTalk(    #68
        0x101,
        "#1007F#6PWhew... That wasn't easy...\x02",
    )

    CloseMessageWindow()

    label("loc_3DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E35")

    ChrTalk(    #69
        0x106,
        "#551F#6PHe really didn't hold back on us.\x02",
    )

    CloseMessageWindow()

    label("loc_3E35")


    ChrTalk(    #70
        0x109,
        (
            "#1065F#6PWell, at least we managed to eke out a win.\x02\x03",

            "#1063FIt sounds like our next foe's gonna up the\x01",
            "ante, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 270, 400)
    Sleep(300)

    ChrTalk(    #71
        0x10A,
        "#815F#11PYeah...but we're gonna win next time, too!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B0E)
    OP_28(0x38, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_28_38B6 end

    def Function_29_3F05(): pass

    label("Function_29_3F05")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F26")
    Sleep(100)
    Jump("loc_3FA1")

    label("loc_3F26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F3B")
    Sleep(200)
    Jump("loc_3FA1")

    label("loc_3F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F50")
    Sleep(300)
    Jump("loc_3FA1")

    label("loc_3F50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F65")
    Sleep(400)
    Jump("loc_3FA1")

    label("loc_3F65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7A")
    Sleep(500)
    Jump("loc_3FA1")

    label("loc_3F7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8F")
    Sleep(600)
    Jump("loc_3FA1")

    label("loc_3F8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA1")
    Sleep(700)

    label("loc_3FA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FC3")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_3FA1")

    label("loc_3FC3")

    Return()

    # Function_29_3F05 end

    def Function_30_3FC4(): pass

    label("Function_30_3FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D3")
    EventBegin(0x0)
    Fade(500)
    OP_6D(77550, 0, 168460, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 76810, 0, 168160, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4065")
    SetChrPos(0xEF, 76470, 0, 166800, 0)
    SetChrPos(0xF0, 75500, 0, 165530, 0)
    SetChrPos(0xF1, 77140, 0, 165800, 0)
    Jump("loc_40EA")

    label("loc_4065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A9")
    SetChrPos(0xF0, 76470, 0, 166800, 0)
    SetChrPos(0xEF, 75500, 0, 165530, 0)
    SetChrPos(0xF1, 77140, 0, 165800, 0)
    Jump("loc_40EA")

    label("loc_40A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40EA")
    SetChrPos(0xF1, 76470, 0, 166800, 0)
    SetChrPos(0xEF, 75500, 0, 165530, 0)
    SetChrPos(0xF0, 77140, 0, 165800, 0)

    label("loc_40EA")

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
            "\x07\x02#1S#40WInvestigate one of the six gates that\x01",
            "manipulate the flow of the iron river,\x01",
            "then shall you obtain radiance.\x02",
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
        "\x07\x05Received \x1F\x2F\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x32F, 1)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4243")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42AA")

    label("loc_4243")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42AA")

    label("loc_426B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4293")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_42AA")

    label("loc_4293")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_42AA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_433E")

    label("loc_42D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42FF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_433E")

    label("loc_42FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4327")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_433E")

    label("loc_4327")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_433E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_43D2")

    label("loc_436B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4393")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_43D2")

    label("loc_4393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43BB")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_43D2")

    label("loc_43BB")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_43D2")

    Sleep(1000)

    ChrTalk(    #74
        0x10A,
        (
            "#1317F#6PWell, I get what we're meant to do with\x01",
            "the cardkey...\x02\x03",

            "...but what's up with that message?\x01",
            "It looked like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x109,
        (
            "#1840F#6PYeah. Even the computer's text has been\x01",
            "flipped.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4501")

    ChrTalk(    #76
        0x107,
        (
            "#065F#6PCompletely, too. It starts from the right\x01",
            "side of the screen instead of the left...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4543")

    ChrTalk(    #77
        0x10C,
        "#110F#6PHaha. Someone's certainly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4543")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4587")

    ChrTalk(    #78
        0x10D,
        "#277F#6PHmph. Someone's pointlessly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4587")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45C9")

    ChrTalk(    #79
        0x104,
        "#1541F#6PHeh. Someone's certainly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_45C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_460D")

    ChrTalk(    #80
        0x10E,
        "#179F#6PHmph. Someone's pointlessly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_460D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4652")

    ChrTalk(    #81
        0x10B,
        "#413F#6P*sigh* Someone's pointlessly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_469B")

    ChrTalk(    #82
        0x105,
        "#1165F#6PThis has been very thoroughly prepared...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_469B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(    #83
        0x10F,
        "#1806F#6PThat's very thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_46D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4716")

    ChrTalk(    #84
        0x103,
        "#1534F#6P*sigh* Someone's pointlessly thorough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4768")

    ChrTalk(    #85
        0x106,
        (
            "#555F#6PBah... Someone's sure wasted a lot of time on\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D2")

    ChrTalk(    #86
        0x108,
        (
            "#070F#6PHaha... I'm impressed at how thoroughly\x01",
            "they've done this, if nothing else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_47D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4824")

    ChrTalk(    #87
        0x102,
        "#1505F#6PThey've certainly put a lot of effort into this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4873")

    label("loc_4824")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4873")

    ChrTalk(    #88
        0x101,
        "#1007F#6PUgh. Someone's sure put a lot of effort into this.\x02",
    )

    CloseMessageWindow()

    label("loc_4873")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48B2")

    ChrTalk(    #89
        0x110,
        "#261F#6PHeehee. That's a nice little touch.\x02",
    )

    CloseMessageWindow()

    label("loc_48B2")

    OP_A2(0x2B0F)
    OP_28(0x38, 0x1, 0x20)
    OP_74(0x17, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_49B2")

    label("loc_48D3")

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
            "\x07\x02#1S#40WInvestigate one of the six gates that\x01",
            "manipulate the flow of the iron river,\x01",
            "then shall you obtain radiance.\x02",
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

    label("loc_49B2")

    Return()

    # Function_30_3FC4 end

    def Function_31_49B3(): pass

    label("Function_31_49B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A82")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5376)
    Sleep(500)
    Jump("loc_4A85")

    label("loc_4A82")

    TalkBegin(0xFF)

    label("loc_4A85")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #91
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C04")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B1D"),
        (1, "loc_4B98"),
        (2, "loc_4BC6"),
        (SWITCH_DEFAULT, "loc_4BF4"),
    )


    label("loc_4B1D")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_4C01")

    label("loc_4B98")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #92
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4C01")

    label("loc_4BC6")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_4C01")

    label("loc_4BF4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C01")

    label("loc_4C01")

    Jump("loc_4AC1")

    label("loc_4C04")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C31")
    OP_A2(0x2598)
    EventEnd(0x1)
    Jump("loc_4C34")

    label("loc_4C31")

    TalkEnd(0xFF)

    label("loc_4C34")

    Return()

    # Function_31_49B3 end

    def Function_32_4C35(): pass

    label("Function_32_4C35")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Operate Lever\x01",      # 0
            "Do Nothing\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE1")
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
    Jump("loc_4CE3")

    label("loc_4CE1")

    EventEnd(0x1)

    label("loc_4CE3")

    Jump("loc_4D8D")

    label("loc_4CE6")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Operate Lever\x01",      # 0
            "Do Nothing\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D8B")
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
    Jump("loc_4D8D")

    label("loc_4D8B")

    EventEnd(0x1)

    label("loc_4D8D")

    Return()

    # Function_32_4C35 end

    def Function_33_4D8E(): pass

    label("Function_33_4D8E")

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

    # Function_33_4D8E end

    def Function_34_4E1D(): pass

    label("Function_34_4E1D")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #94
        "\x07\x05The doors are sealed shut.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_4E1D end

    def Function_35_4E84(): pass

    label("Function_35_4E84")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EFF")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1E)
    OP_73(0x6)
    OP_64(0x3, 0x1)
    OP_10(0x1F, 0x1)
    OP_A2(0x2B59)
    Jump("loc_4F23")

    label("loc_4EFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F23")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_4F23")

    label("loc_4F23")

    TalkEnd(0xFF)
    Return()

    # Function_35_4E84 end

    def Function_36_4F27(): pass

    label("Function_36_4F27")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA2")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x1E)
    OP_73(0x11)
    OP_64(0x4, 0x1)
    OP_10(0x20, 0x1)
    OP_A2(0x2B5A)
    Jump("loc_4FC6")

    label("loc_4FA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FC6")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_4FC6")

    label("loc_4FC6")

    TalkEnd(0xFF)
    Return()

    # Function_36_4F27 end

    def Function_37_4FCA(): pass

    label("Function_37_4FCA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5045")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_64(0x5, 0x1)
    OP_10(0x5, 0x1)
    OP_A2(0x2B5B)
    Jump("loc_5069")

    label("loc_5045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5069")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_5069")

    label("loc_5069")

    TalkEnd(0xFF)
    Return()

    # Function_37_4FCA end

    def Function_38_506D(): pass

    label("Function_38_506D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #98
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50EE")
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
    Jump("loc_5112")

    label("loc_50EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5112")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_5112")

    label("loc_5112")

    TalkEnd(0xFF)
    Return()

    # Function_38_506D end

    def Function_39_5116(): pass

    label("Function_39_5116")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_END)), "loc_5131")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_END)), "loc_5142")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_END)), "loc_5153")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5153")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_517F"),
        (1, "loc_518C"),
        (3, "loc_51E1"),
        (7, "loc_5259"),
        (SWITCH_DEFAULT, "loc_52F3"),
    )


    label("loc_517F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52F3")

    label("loc_518C")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",      # 0
            "Do Nothing\x01",           # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_51C4"),
        (1, "loc_51D1"),
        (SWITCH_DEFAULT, "loc_51DE"),
    )


    label("loc_51C4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51DE")

    label("loc_51D1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51DE")

    label("loc_51DE")

    Jump("loc_52F3")

    label("loc_51E1")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",        # 0
            "Use Green Cardkey\x01",      # 1
            "Do Nothing\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_522F"),
        (1, "loc_523C"),
        (2, "loc_5249"),
        (SWITCH_DEFAULT, "loc_5256"),
    )


    label("loc_522F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5256")

    label("loc_523C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5256")

    label("loc_5249")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5256")

    label("loc_5256")

    Jump("loc_52F3")

    label("loc_5259")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",        # 0
            "Use Green Cardkey\x01",      # 1
            "Use Blue Cardkey\x01",       # 2
            "Do Nothing\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_52BC"),
        (1, "loc_52C9"),
        (2, "loc_52D6"),
        (3, "loc_52E3"),
        (SWITCH_DEFAULT, "loc_52F0"),
    )


    label("loc_52BC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52F0")

    label("loc_52C9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52F0")

    label("loc_52D6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52F0")

    label("loc_52E3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52F0")

    label("loc_52F0")

    Jump("loc_52F3")

    label("loc_52F3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_39_5116 end

    def Function_40_530B(): pass

    label("Function_40_530B")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_40_530B end

    def Function_41_5364(): pass

    label("Function_41_5364")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_543A")
    OP_28(0x14, 0x4, 0x2)
    OP_82(0x85, 0x2)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_543A")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_54C1")

    AnonymousTalk(    #100
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5557")

    label("loc_54C1")


    AnonymousTalk(    #101
        (
            "\x07\x05#40WThose who seek to enter this door\x01",
            "must first overcome a trial.\x01",
            "#500W \x01",
            "#40WShould this fail to deter you, open the door,\x01",
            "and step inside...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5557")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Call(0, 40)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5580")
    Call(0, 42)

    label("loc_5580")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_41_5364 end

    def Function_42_558C(): pass

    label("Function_42_558C")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x21)
    Sleep(500)

    def lambda_55F5():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_55F5)
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

    # Function_42_558C end

    def Function_43_5642(): pass

    label("Function_43_5642")

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

    # Function_43_5642 end

    def Function_44_56ED(): pass

    label("Function_44_56ED")

    OP_A2(0x2B64)
    OP_A3(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_44_56ED end

    SaveToFile()

Try(main)
