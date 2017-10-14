from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'ヴァンガード',                         # 10
        'ポートシーカー',                       # 11
        'ポートシーカー',                       # 12
        'ヴォーグル570（青）',                  # 13
        'ポートシーカー',                       # 14
        'ポートシーカー',                       # 15
        'ヴォーグル235（赤）',                  # 16
        'ヴァンガード',                         # 17
        'レオールガンイージ',                   # 18
        'レオールガンイージ',                   # 19
        'レオールガンイージ',                   # 20
        'ヴァンガード',                         # 21
        'ポートシーカー',                       # 22
        'ポートシーカー',                       # 23
        'ヴォーグル570（青）',                  # 24
        'ポートシーカー',                       # 25
        'ポートシーカー',                       # 26
        'ヴォーグル235（赤）',                  # 27
        'ヴァンガード',                         # 28
        'レオールガンイージ',                   # 29
        'レオールガンイージ',                   # 30
        'レオールガンイージ',                   # 31
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
        "Function_4_A64",          # 04, 4
        "Function_5_BA8",          # 05, 5
        "Function_6_CC6",          # 06, 6
        "Function_7_E0D",          # 07, 7
        "Function_8_FF2",          # 08, 8
        "Function_9_1146",         # 09, 9
        "Function_10_1274",        # 0A, 10
        "Function_11_13C9",        # 0B, 11
        "Function_12_14FC",        # 0C, 12
        "Function_13_162A",        # 0D, 13
        "Function_14_17A1",        # 0E, 14
        "Function_15_1901",        # 0F, 15
        "Function_16_1A95",        # 10, 16
        "Function_17_1AAE",        # 11, 17
        "Function_18_1AC7",        # 12, 18
        "Function_19_268C",        # 13, 19
        "Function_20_26D4",        # 14, 20
        "Function_21_271C",        # 15, 21
        "Function_22_2764",        # 16, 22
        "Function_23_27AC",        # 17, 23
        "Function_24_2BE5",        # 18, 24
        "Function_25_3067",        # 19, 25
        "Function_26_3149",        # 1A, 26
        "Function_27_318A",        # 1B, 27
        "Function_28_31CB",        # 1C, 28
        "Function_29_320C",        # 1D, 29
        "Function_30_324D",        # 1E, 30
        "Function_31_32D3",        # 1F, 31
        "Function_32_3364",        # 20, 32
        "Function_33_338A",        # 21, 33
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

    OP_EA(0x2, 0x71, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2C")
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
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D39)
    Jump("loc_A52")

    label("loc_A2C")


    AnonymousTalk(    #1
        "\x07\x05...Say, haven't we met before?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A52")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_935 end

    def Function_4_A64(): pass

    label("Function_4_A64")

    OP_EA(0x2, 0x72, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_AD5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2330)
    Jump("loc_B39")

    label("loc_AD5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_B39")

    Jump("loc_B9A")

    label("loc_B3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05You've already looted this chest right down to\x01",
            "the bare bottom.\x07\x00\x02",
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

    # Function_4_A64 end

    def Function_5_BA8(): pass

    label("Function_5_BA8")

    OP_EA(0x2, 0x73, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C80")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x22, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6B, 1)"), scpexpr(EXPR_END)), "loc_C19")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\x6B\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2331)
    Jump("loc_C7D")

    label("loc_C19")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\x6B\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6B\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x22, 60)
    OP_70(0x22, 0x0)

    label("loc_C7D")

    Jump("loc_CB8")

    label("loc_C80")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Not exactly shy, are you?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CB8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BA8 end

    def Function_6_CC6(): pass

    label("Function_6_CC6")

    OP_EA(0x2, 0x74, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x23, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_D37")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2333)
    Jump("loc_D9B")

    label("loc_D37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x23, 60)
    OP_70(0x23, 0x0)

    label("loc_D9B")

    Jump("loc_DFF")

    label("loc_D9E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Let's form a pact. Infinite treasure in exchange...\x01",
            "for your LIFE.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DFF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CC6 end

    def Function_7_E0D(): pass

    label("Function_7_E0D")

    OP_EA(0x2, 0x75, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_E64():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E64)

    def lambda_E7F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E7F)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #11
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x432, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_ED2"),
        (2, "loc_EE4"),
        (1, "loc_EF4"),
        (SWITCH_DEFAULT, "loc_EF7"),
    )


    label("loc_ED2")

    OP_A2(0x2335)
    OP_6F(0x24, 60)
    Sleep(500)
    Jump("loc_EF7")

    label("loc_EE4")

    OP_6F(0x24, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_EF4")

    OP_B4(0x0)
    Return()

    label("loc_EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x139, 1)"), scpexpr(EXPR_END)), "loc_F43")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "Found \x1F\x39\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2334)
    Jump("loc_FA5")

    label("loc_F43")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        (
            "Found \x1F\x39\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x39\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_FA5")

    Jump("loc_FE4")

    label("loc_FA8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #14
        "\x07\x05You found a fine layer of dust!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FE4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_E0D end

    def Function_8_FF2(): pass

    label("Function_8_FF2")

    OP_EA(0x2, 0x76, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1063")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2336)
    Jump("loc_10C7")

    label("loc_1063")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_10C7")

    Jump("loc_1138")

    label("loc_10CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05For every extra item you take from a treasure\x01",
            "chest, a creepy sheep is sheared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1138")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_FF2 end

    def Function_9_1146(): pass

    label("Function_9_1146")

    OP_EA(0x2, 0x77, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x466, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_11B7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2337)
    Jump("loc_121B")

    label("loc_11B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_121B")

    Jump("loc_1266")

    label("loc_121E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Everything that mattered in here is gone.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1266")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1146 end

    def Function_10_1274(): pass

    label("Function_10_1274")

    OP_EA(0x2, 0x78, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_12E5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2338)
    Jump("loc_1349")

    label("loc_12E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_1349")

    Jump("loc_13BB")

    label("loc_134C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05You begin to suspect that this treasure chest is\x01",
            "a portal to the Meat Dimension.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13BB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1274 end

    def Function_11_13C9(): pass

    label("Function_11_13C9")

    OP_EA(0x2, 0x7A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_143A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2339)
    Jump("loc_149E")

    label("loc_143A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_149E")

    Jump("loc_14EE")

    label("loc_14A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Orbmints: Keeping your breath fresher, longer.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_13C9 end

    def Function_12_14FC(): pass

    label("Function_12_14FC")

    OP_EA(0x2, 0x7B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x88, 1)"), scpexpr(EXPR_END)), "loc_156D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "Found \x1F\x88\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233A)
    Jump("loc_15D1")

    label("loc_156D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "Found \x1F\x88\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x88\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_15D1")

    Jump("loc_161C")

    label("loc_15D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Was returning here another...BRIGHT IDEA?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_161C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_14FC end

    def Function_13_162A(): pass

    label("Function_13_162A")

    OP_EA(0x2, 0x7C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_169B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233C)
    Jump("loc_16FF")

    label("loc_169B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_16FF")

    Jump("loc_1793")

    label("loc_1702")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05You flip open the lid, knowing full well you won't\x01",
            "find anything. You're still somehow disappointed\x01",
            "by the result.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1793")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_162A end

    def Function_14_17A1(): pass

    label("Function_14_17A1")

    OP_EA(0x2, 0x7D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")
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
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x233D)
    Jump("loc_18EF")

    label("loc_1898")


    AnonymousTalk(    #34
        (
            "\x07\x05Returning to a chest you just looted is\x01",
            "kinda like dumpster diving, you know...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_18EF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_17A1 end

    def Function_15_1901(): pass

    label("Function_15_1901")

    OP_EA(0x2, 0x7E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x467, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_1972")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x233E)
    Jump("loc_19D6")

    label("loc_1972")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_19D6")

    Jump("loc_1A87")

    label("loc_19D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x07\x05YOU might look at this chest and think its empty,\x01",
            "but that's just negative thinking. Others see this\x01",
            "baby and marvel at the amazing air inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A87")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1901 end

    def Function_16_1A95(): pass

    label("Function_16_1A95")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A2(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_16_1A95 end

    def Function_17_1AAE(): pass

    label("Function_17_1AAE")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A2(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_17_1AAE end

    def Function_18_1AC7(): pass

    label("Function_18_1AC7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADE")
    Call(0, 30)
    Call(0, 31)

    label("loc_1ADE")

    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    OP_D2(0x702B4, 0x702BB, 0xE)
    OP_D2(0x702B5, 0x702BC, 0xF)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1B3F"),
        (3, "loc_1B56"),
        (4, "loc_1B6D"),
        (5, "loc_1B84"),
        (6, "loc_1B9B"),
        (7, "loc_1BB2"),
        (8, "loc_1BC9"),
        (SWITCH_DEFAULT, "loc_1BE0"),
    )


    label("loc_1B3F")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_1BE0")

    label("loc_1B56")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_1BE0")

    label("loc_1B6D")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_1BE0")

    label("loc_1B84")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_1BE0")

    label("loc_1B9B")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_1BE0")

    label("loc_1BB2")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_1BE0")

    label("loc_1BC9")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_1BE0")

    label("loc_1BE0")

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

    def lambda_1C9B():
        OP_6D(-4780, 0, 80680, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C9B)

    def lambda_1CB3():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CB3)

    def lambda_1CCB():
        OP_6B(2830, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CCB)

    def lambda_1CDB():
        OP_6C(56000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1CDB)
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
        "#216F#5PThis is the interior of the Glorious?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA3")

    ChrTalk(    #39
        0x107,
        "#065FWaaaah! It's so huge!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF9")

    ChrTalk(    #40
        0x105,
        (
            "#1163FIt's massive... It's hard to believe\x01",
            "we're inside a ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E50")

    ChrTalk(    #41
        0x109,
        (
            "#1068FHoly Testaments. Feels like we're\x01",
            "outdoors, not in a ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(    #42
        0x103,
        (
            "#022FAs spacious inside as it is\x01",
            "large outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1E96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(    #43
        0x104,
        (
            "#033FSuch a spacious vessel!\x02\x03",

            "#031FThe acoustics would be sufficient\x01",
            "for a concert, even.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1F06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F5E")

    ChrTalk(    #44
        0x106,
        (
            "#555FFriggin'... What does a ship need\x01",
            "an interior like this for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB1")

    label("loc_1F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB1")

    ChrTalk(    #45
        0x108,
        (
            "#072FHmm. Such space inside...\x01",
            "It's like we're outside, really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB1")

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
            "#1007F#6PIt really is kind of stupidly huge, isn't it?\x02\x03",

            "#1002FAnd Ouroboros probably has combat\x01",
            "archaisms all over the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10B,
        (
            "#215F#6P...\x02\x03",

            "#212FYou guys escaped from this ship\x01",
            "before, right?\x02\x03",

            "Any idea where Kyle and Don might be?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20FB():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20FB)
    Sleep(50)

    def lambda_210E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_210E)
    Sleep(50)

    def lambda_2121():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2121)
    Sleep(500)

    ChrTalk(    #48
        0x101,
        (
            "#1004F#7PActually, maybe!\x02\x03",

            "#1015FThere is that room I was kept locked up in.\x01",
            "Sort of a weird prison, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1035F#2PThat's because it was technically\x01",
            "a guest room.\x02\x03",

            "#1042FI'd bet the Capuas are being kept\x01",
            "in the brig.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2252():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2252)
    Sleep(50)

    def lambda_2265():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2265)
    Sleep(50)

    def lambda_2278():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2278)
    WaitChrThread(0x10B, 0x1)

    ChrTalk(    #50
        0x10B,
        "#216F#6PThe BRIG?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1002F#6PSo they do have an actual prison.\x02\x03",

            "I don't remember seeing it when\x01",
            "we escaped before.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    Sleep(300)

    ChrTalk(    #52
        0x102,
        (
            "#1035F#4PThey had the electromagnetic barriers raised to\x01",
            "try and stop our escape, remember? It prevented\x01",
            "us from going everywhere on the ship.\x02\x03",

            "#1042FThe barriers aren't up at the moment.\x02\x03",

            "This is probably the best chance we\x01",
            "have at saving the Capuas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10B,
        "#212F#6PSo do you know where the cells are?\x02",
    )

    CloseMessageWindow()

    def lambda_2445():

        label("loc_2445")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2445")

    QueueWorkItem2(0x101, 2, lambda_2445)

    def lambda_2456():

        label("loc_2456")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2456")

    QueueWorkItem2(0x10B, 2, lambda_2456)

    def lambda_2467():

        label("loc_2467")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2467")

    QueueWorkItem2(0xF9, 2, lambda_2467)
    OP_8C(0x102, 90, 400)
    Sleep(300)

    def lambda_2484():
        OP_6D(-3990, 0, 77560, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2484)
    OP_8E(0x102, 0xFFFFEE30, 0x0, 0x12D54, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x102, 180, 400)
    OP_6D(-1740, 0, 73860, 1500)

    ChrTalk(    #54
        0x102,
        (
            "#1042F#6PAs I remember, there's a small staircase\x01",
            "to the lower decks down this passage.\x02\x03",

            "The brig should be down there.\x02",
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
            "#1006F#6PStaircase to the brig...\x01",
            "Let's check it out.\x02",
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

    # Function_18_1AC7 end

    def Function_19_268C(): pass

    label("Function_19_268C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 80800, 90)

    def lambda_26B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26B3)
    OP_8E(0xFE, 0xFFFFD698, 0x0, 0x13BA0, 0x1770, 0x0)
    Return()

    # Function_19_268C end

    def Function_20_26D4(): pass

    label("Function_20_26D4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 79270, 90)

    def lambda_26FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26FB)
    OP_8E(0xFE, 0xFFFFD620, 0x0, 0x134FC, 0x1770, 0x0)
    Return()

    # Function_20_26D4 end

    def Function_21_271C(): pass

    label("Function_21_271C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 81200, 90)

    def lambda_2743():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2743)
    OP_8E(0xFE, 0xFFFFD06C, 0x0, 0x13BBE, 0x1770, 0x0)
    Return()

    # Function_21_271C end

    def Function_22_2764(): pass

    label("Function_22_2764")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -32830, -200, 79180, 90)

    def lambda_278B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_278B)
    OP_8E(0xFE, 0xFFFFCEFA, 0x0, 0x134B6, 0x1770, 0x0)
    Return()

    # Function_22_2764 end

    def Function_23_27AC(): pass

    label("Function_23_27AC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_27DC"),
        (1, "loc_283F"),
        (10, "loc_289C"),
        (6, "loc_28FF"),
        (4, "loc_2963"),
        (8, "loc_29D5"),
        (2, "loc_2A3F"),
        (3, "loc_2AA9"),
        (5, "loc_2B25"),
        (7, "loc_2B84"),
        (SWITCH_DEFAULT, "loc_2BE1"),
    )


    label("loc_27DC")


    ChrTalk(    #56
        0x101,
        (
            "#1002F(The brig should be on the\x01",
            "other side of the passage...)\x02\x03",

            "(Let's check there first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_283F")


    ChrTalk(    #57
        0x102,
        (
            "#1042F(The brig is on the other side\x01",
            "of the passage.)\x02\x03",

            "(Let's leave this for later.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_289C")


    ChrTalk(    #58
        0x10B,
        (
            "#212F(I think the brig is on the other\x01",
            "side of the passage.)\x02\x03",

            "(We need to go there first!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_28FF")


    ChrTalk(    #59
        0x107,
        (
            "#062F(Umm, isn't the ship jail on the\x01",
            "other side of this passage?)\x02\x03",

            "(Let's go there first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2963")


    ChrTalk(    #60
        0x105,
        (
            "#1162F(I believe the brig is on the\x01",
            "other side of this passage.)\x02\x03",

            "(That should be our first destination.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_29D5")


    ChrTalk(    #61
        0x109,
        (
            "#1063F(Hey. The cells are on the other\x01",
            "side of the passage.)\x02\x03",

            "(Let's leave this for later, okay?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2A3F")


    ChrTalk(    #62
        0x103,
        (
            "#022F(The detention area is on the\x01",
            "other side of this passage.)\x02\x03",

            "(That should be our first stop.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2AA9")


    ChrTalk(    #63
        0x104,
        (
            "#030F(Ah, remember, the cells are on\x01",
            "the other side of the passage.)\x02\x03",

            "(That is where the next act\x01",
            "is set to occur.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2B25")


    ChrTalk(    #64
        0x106,
        (
            "#050F(The brig's on the other side\x01",
            "of the passage.)\x02\x03",

            "(That's where we gotta go first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2B84")


    ChrTalk(    #65
        0x108,
        (
            "#072F(The brig is on the other side\x01",
            "of this passage.)\x02\x03",

            "(We should head there first.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2BE1")

    TalkEnd(0xFF)
    Return()

    # Function_23_27AC end

    def Function_24_2BE5(): pass

    label("Function_24_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C57")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05The gate is shut tight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3066")

    label("loc_2C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3066")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2C95"),
        (1, "loc_2CDD"),
        (10, "loc_2D54"),
        (6, "loc_2DA2"),
        (4, "loc_2DF5"),
        (8, "loc_2E47"),
        (2, "loc_2E9E"),
        (3, "loc_2EE8"),
        (5, "loc_2F6F"),
        (7, "loc_2FCD"),
        (SWITCH_DEFAULT, "loc_304B"),
    )


    label("loc_2C95")


    ChrTalk(    #67
        0x101,
        (
            "#1002F(We haven't finished here yet.)\x02\x03",

            "(Escape can come later.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2CDD")


    ChrTalk(    #68
        0x102,
        (
            "#1043F(We shouldn't try escaping until we've\x01",
            "saved the Capuas.)\x02\x03",

            "(We should continue to investigate\x01",
            "the ship.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2D54")


    ChrTalk(    #69
        0x10B,
        (
            "#215F(No, we can't leave yet.)\x02\x03",

            "(I've still gotta save Kyle and Don!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2DA2")


    ChrTalk(    #70
        0x107,
        (
            "#062F(We can't leave the Glorious yet...)\x02\x03",

            "(We've gotta save the bandits!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2DF5")


    ChrTalk(    #71
        0x105,
        (
            "#1163F(We can't leave the Glorious yet.)\x02\x03",

            "(We need to rescue the Capuas.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2E47")


    ChrTalk(    #72
        0x109,
        (
            "#1063F(Hang on, escape comes later.)\x02\x03",

            "(We gotta save those bandit guys first!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2E9E")


    ChrTalk(    #73
        0x103,
        (
            "#022F(We still need to save the bandits.)\x02\x03",

            "(We can escape later.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2EE8")


    ChrTalk(    #74
        0x104,
        (
            "#033F(Ah, wait. Our time on this\x01",
            "stage is not yet done!)\x02\x03",

            "#035F(We must boldly sally forth and\x01",
            "rescue those bandit gentlemen!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2F6F")


    ChrTalk(    #75
        0x106,
        (
            "#052F(Wait a minute...)\x02\x03",

            "#053F(We gotta save those bandits\x01",
            "before we ditch the ship.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_2FCD")


    ChrTalk(    #76
        0x108,
        (
            "#074F(We should not attempt escape\x01",
            "until we've saved the bandits.)\x02\x03",

            "#072F(Let's continue our search\x01",
            "aboard the ship.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304B")

    label("loc_304B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3066")

    Return()

    # Function_24_2BE5 end

    def Function_25_3067(): pass

    label("Function_25_3067")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3074")
    Return()

    label("loc_3074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 1)), scpexpr(EXPR_END)), "loc_30A9")
    OP_6F(0x1, 100)
    OP_72(0x1, 0x2)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -1500, 3600, 2000, 1500)

    label("loc_30A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 2)), scpexpr(EXPR_END)), "loc_30DE")
    OP_6F(0x2, 100)
    OP_72(0x2, 0x2)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5600, -1000, -59500, 3600, 2000, -56500)

    label("loc_30DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 3)), scpexpr(EXPR_END)), "loc_3113")
    OP_6F(0x3, 100)
    OP_72(0x3, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 38000, -1000, -5300, 45000, 2000, -2500)

    label("loc_3113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 4)), scpexpr(EXPR_END)), "loc_3148")
    OP_6F(0x4, 100)
    OP_72(0x4, 0x2)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, 132500, -1000, -191000, 135500, 2000, -185000)

    label("loc_3148")

    Return()

    # Function_25_3067 end

    def Function_26_3149(): pass

    label("Function_26_3149")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3156")
    Return()

    label("loc_3156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 1)), scpexpr(EXPR_END)), "loc_315E")
    Return()

    label("loc_315E")

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

    # Function_26_3149 end

    def Function_27_318A(): pass

    label("Function_27_318A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3197")
    Return()

    label("loc_3197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 2)), scpexpr(EXPR_END)), "loc_319F")
    Return()

    label("loc_319F")

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

    # Function_27_318A end

    def Function_28_31CB(): pass

    label("Function_28_31CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31D8")
    Return()

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 3)), scpexpr(EXPR_END)), "loc_31E0")
    Return()

    label("loc_31E0")

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

    # Function_28_31CB end

    def Function_29_320C(): pass

    label("Function_29_320C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3219")
    Return()

    label("loc_3219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 4)), scpexpr(EXPR_END)), "loc_3221")
    Return()

    label("loc_3221")

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

    # Function_29_320C end

    def Function_30_324D(): pass

    label("Function_30_324D")

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
        (0, "loc_32C6"),
        (1, "loc_32CC"),
        (SWITCH_DEFAULT, "loc_32D2"),
    )


    label("loc_32C6")

    OP_A2(0x1200)
    Jump("loc_32D2")

    label("loc_32CC")

    OP_A2(0x1201)
    Jump("loc_32D2")

    label("loc_32D2")

    Return()

    # Function_30_324D end

    def Function_31_32D3(): pass

    label("Function_31_32D3")

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

    # Function_31_32D3 end

    def Function_32_3364(): pass

    label("Function_32_3364")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240133, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_32_3364 end

    def Function_33_338A(): pass

    label("Function_33_338A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240134, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_33_338A end

    SaveToFile()

Try(main)
