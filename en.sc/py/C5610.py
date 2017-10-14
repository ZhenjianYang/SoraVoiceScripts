from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5610   ._SN',
        MapName             = 'Other',
        Location            = 'C5610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        'Grant',                                # 10
        'Vogel 235',                            # 11
        'Vogel 570',                            # 12
        'Vogel 235',                            # 13
        '部品',                                 # 14
        '部品',                                 # 15
        '部品',                                 # 16
        '部品',                                 # 17
        '部品',                                 # 18
        '部品',                                 # 19
        '部品',                                 # 20
        '部品',                                 # 21
        '部品',                                 # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
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
        'ED6_DT29/CH12320 ._CH',             # 02
        'ED6_DT29/CH12321 ._CH',             # 03
        'ED6_DT29/CH12330 ._CH',             # 04
        'ED6_DT29/CH12331 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
        'ED6_DT07/CH01260 ._CH',             # 0A
        'ED6_DT07/CH00390 ._CH',             # 0B
        'ED6_DT26/CH20404 ._CH',             # 0C
        'ED6_DT26/CH20409 ._CH',             # 0D
        'ED6_DT27/CH04000 ._CH',             # 0E
        'ED6_DT07/CH00120 ._CH',             # 0F
        'ED6_DT07/CH00150 ._CH',             # 10
        'ED6_DT07/CH00130 ._CH',             # 11
        'ED6_DT07/CH00140 ._CH',             # 12
        'ED6_DT07/CH00160 ._CH',             # 13
        'ED6_DT07/CH00170 ._CH',             # 14
        'ED6_DT27/CH04080 ._CH',             # 15
        'ED6_DT29/CH12574 ._CH',             # 16
        'ED6_DT27/CH03084 ._CH',             # 17
        'ED6_DT27/CH03005 ._CH',             # 18
        'ED6_DT29/CH12354 ._CH',             # 19
        'ED6_DT26/CH20373 ._CH',             # 1A
        'ED6_DT07/CH00391 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12320P._CP',             # 02
        'ED6_DT29/CH12321P._CP',             # 03
        'ED6_DT29/CH12330P._CP',             # 04
        'ED6_DT29/CH12331P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
        'ED6_DT07/CH01260P._CP',             # 0A
        'ED6_DT07/CH00390P._CP',             # 0B
        'ED6_DT26/CH20404P._CP',             # 0C
        'ED6_DT26/CH20409P._CP',             # 0D
        'ED6_DT27/CH04000P._CP',             # 0E
        'ED6_DT07/CH00120P._CP',             # 0F
        'ED6_DT07/CH00150P._CP',             # 10
        'ED6_DT07/CH00130P._CP',             # 11
        'ED6_DT07/CH00140P._CP',             # 12
        'ED6_DT07/CH00160P._CP',             # 13
        'ED6_DT07/CH00170P._CP',             # 14
        'ED6_DT27/CH04080P._CP',             # 15
        'ED6_DT29/CH12574P._CP',             # 16
        'ED6_DT27/CH03084P._CP',             # 17
        'ED6_DT27/CH03005P._CP',             # 18
        'ED6_DT29/CH12354P._CP',             # 19
        'ED6_DT26/CH20373P._CP',             # 1A
        'ED6_DT07/CH00391P._CP',             # 1B
    )

    DeclNpc(
        X                   = 80960,
        Z                   = 1500,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x6,
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
        Unknown3            = 2,
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
        Unknown3            = 2,
        ChipIndex           = 0x6,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 131085,
        ChipIndex           = 0xD,
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
        Unknown3            = 65549,
        ChipIndex           = 0xD,
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
        Unknown3            = 196621,
        ChipIndex           = 0xD,
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
        Unknown3            = 65549,
        ChipIndex           = 0xD,
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
        Unknown3            = 131085,
        ChipIndex           = 0xD,
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
        Unknown3            = 196621,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 65549,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -158630,
        Z                   = 0,
        Y                   = -17300,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 86870,
        Z                   = 0,
        Y                   = -9080,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 88230,
        Z                   = 0,
        Y                   = 105630,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 88000,
        Z                   = 0,
        Y                   = 95860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37720,
        Z                   = 0,
        Y                   = 125100,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10490,
        Z                   = 0,
        Y                   = 109180,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 23010,
        Y                   = -1000,
        Z                   = 131280,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 38,
    )


    DeclActor(
        TriggerX            = -107320,
        TriggerZ            = 0,
        TriggerY            = 67990,
        TriggerRange        = 1000,
        ActorX              = -107980,
        ActorZ              = 0,
        ActorY              = 67990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4290,
        TriggerZ            = 0,
        TriggerY            = 32990,
        TriggerRange        = 1000,
        ActorX              = -5000,
        ActorZ              = 0,
        ActorY              = 32990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -152290,
        TriggerZ            = 0,
        TriggerY            = -16970,
        TriggerRange        = 1000,
        ActorX              = -153000,
        ActorZ              = 0,
        ActorY              = -17010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 80300,
        TriggerZ            = 0,
        TriggerY            = -9000,
        TriggerRange        = 1000,
        ActorX              = 80960,
        ActorZ              = 0,
        ActorY              = -9000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70290,
        TriggerZ            = 0,
        TriggerY            = 44530,
        TriggerRange        = 1000,
        ActorX              = 70950,
        ActorZ              = 0,
        ActorY              = 44530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 82290,
        TriggerZ            = 0,
        TriggerY            = 101030,
        TriggerRange        = 1000,
        ActorX              = 82990,
        ActorZ              = 0,
        ActorY              = 101030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12880,
        TriggerZ            = 0,
        TriggerY            = -18740,
        TriggerRange        = 800,
        ActorX              = -12880,
        ActorZ              = 1000,
        ActorY              = -18740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76940,
        TriggerZ            = 0,
        TriggerY            = 169050,
        TriggerRange        = 800,
        ActorX              = -76940,
        ActorZ              = 1000,
        ActorY              = 169050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28830,
        TriggerZ            = 0,
        TriggerY            = 25920,
        TriggerRange        = 800,
        ActorX              = 28830,
        ActorZ              = 1200,
        ActorY              = 25920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24650,
        TriggerZ            = 0,
        TriggerY            = 131700,
        TriggerRange        = 800,
        ActorX              = 24650,
        ActorZ              = 1200,
        ActorY              = 131700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28770,
        TriggerZ            = 0,
        TriggerY            = 11950,
        TriggerRange        = 800,
        ActorX              = 28770,
        ActorZ              = 1200,
        ActorY              = 11950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -66710,
        TriggerZ            = 0,
        TriggerY            = 67500,
        TriggerRange        = 800,
        ActorX              = -66710,
        ActorZ              = 1200,
        ActorY              = 67500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9010,
        TriggerZ            = 0,
        TriggerY            = 138700,
        TriggerRange        = 1200,
        ActorX              = -9010,
        ActorZ              = 1000,
        ActorY              = 138700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5E6",          # 00, 0
        "Function_1_63D",          # 01, 1
        "Function_2_7EC",          # 02, 2
        "Function_3_802",          # 03, 3
        "Function_4_83E",          # 04, 4
        "Function_5_87F",          # 05, 5
        "Function_6_8C0",          # 06, 6
        "Function_7_901",          # 07, 7
        "Function_8_942",          # 08, 8
        "Function_9_983",          # 09, 9
        "Function_10_9C4",         # 0A, 10
        "Function_11_A05",         # 0B, 11
        "Function_12_A46",         # 0C, 12
        "Function_13_B39",         # 0D, 13
        "Function_14_C99",         # 0E, 14
        "Function_15_DF3",         # 0F, 15
        "Function_16_102F",        # 10, 16
        "Function_17_119E",        # 11, 17
        "Function_18_12FE",        # 12, 18
        "Function_19_1A9E",        # 13, 19
        "Function_20_22E2",        # 14, 20
        "Function_21_2354",        # 15, 21
        "Function_22_23CB",        # 16, 22
        "Function_23_2442",        # 17, 23
        "Function_24_2593",        # 18, 24
        "Function_25_2623",        # 19, 25
        "Function_26_26C6",        # 1A, 26
        "Function_27_2769",        # 1B, 27
        "Function_28_280C",        # 1C, 28
        "Function_29_28AF",        # 1D, 29
        "Function_30_2AB3",        # 1E, 30
        "Function_31_3186",        # 1F, 31
        "Function_32_31E4",        # 20, 32
        "Function_33_3242",        # 21, 33
        "Function_34_3FB4",        # 22, 34
        "Function_35_4275",        # 23, 35
        "Function_36_42FE",        # 24, 36
        "Function_37_435B",        # 25, 37
        "Function_38_43C1",        # 26, 38
        "Function_39_43D4",        # 27, 39
    )


    def Function_0_5E6(): pass

    label("Function_0_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_5F7")
    OP_A3(0x10F0)
    Event(0, 24)
    Jump("loc_63C")

    label("loc_5F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60F")
    Event(0, 18)

    label("loc_60F")

    Jump("loc_63C")

    label("loc_612")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A")
    Event(0, 30)

    label("loc_62A")

    Jump("loc_63C")

    label("loc_62D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63C")
    OP_A2(0x1C1A)

    label("loc_63C")

    Return()

    # Function_0_5E6 end

    def Function_1_63D(): pass

    label("Function_1_63D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (128, "loc_651"),
        (129, "loc_651"),
        (135, "loc_651"),
        (SWITCH_DEFAULT, "loc_659"),
    )


    label("loc_651")

    OP_22(0xA0, 0x1, 0x64)
    Jump("loc_65F")

    label("loc_659")

    OP_23(0xA0)
    Jump("loc_65F")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671")
    OP_6F(0x0, 0)
    Jump("loc_678")

    label("loc_671")

    OP_6F(0x0, 60)

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")
    OP_6F(0x1, 0)
    Jump("loc_691")

    label("loc_68A")

    OP_6F(0x1, 60)

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A3")
    OP_6F(0x2, 0)
    Jump("loc_6AA")

    label("loc_6A3")

    OP_6F(0x2, 60)

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BC")
    OP_6F(0x3, 0)
    Jump("loc_6C3")

    label("loc_6BC")

    OP_6F(0x3, 60)

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5")
    OP_6F(0x4, 0)
    Jump("loc_6DC")

    label("loc_6D5")

    OP_6F(0x4, 60)

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE")
    OP_6F(0x5, 0)
    Jump("loc_6F5")

    label("loc_6EE")

    OP_6F(0x5, 60)

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 7)), scpexpr(EXPR_END)), "loc_709")
    OP_10(0x0, 0x1)
    OP_6F(0x1E, 60)
    Jump("loc_715")

    label("loc_709")

    OP_1B(0x0, 0x0, 0x25)
    OP_6F(0x1E, 1)

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 0)), scpexpr(EXPR_END)), "loc_72B")
    OP_64(0x8, 0x1)
    OP_71(0xC, 0x10)
    OP_10(0x1F, 0x1)
    Jump("loc_733")

    label("loc_72B")

    OP_10(0x1F, 0x0)
    OP_72(0xC, 0x10)

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 1)), scpexpr(EXPR_END)), "loc_749")
    OP_64(0x9, 0x1)
    OP_71(0x17, 0x10)
    OP_10(0x20, 0x1)
    Jump("loc_751")

    label("loc_749")

    OP_10(0x20, 0x0)
    OP_72(0x17, 0x10)

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x382, 2)), scpexpr(EXPR_END)), "loc_767")
    OP_64(0xA, 0x1)
    OP_71(0xB, 0x10)
    OP_10(0x5, 0x1)
    Jump("loc_76F")

    label("loc_767")

    OP_10(0x5, 0x0)
    OP_72(0xB, 0x10)

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 0)), scpexpr(EXPR_END)), "loc_785")
    OP_64(0xB, 0x1)
    OP_71(0x13, 0x10)
    OP_10(0x1D, 0x1)
    Jump("loc_78D")

    label("loc_785")

    OP_10(0x1D, 0x0)
    OP_72(0x13, 0x10)

    label("loc_78D")

    OP_74(0x1D, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EB")
    LoadEffect(0x1, "map\\\\mp027_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, -9010, 1000, 138700, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_7EB")

    Return()

    # Function_1_63D end

    def Function_2_7EC(): pass

    label("Function_2_7EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_801")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7EC")

    label("loc_801")

    Return()

    # Function_2_7EC end

    def Function_3_802(): pass

    label("Function_3_802")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_83D")
    SetChrPos(0xFE, -62120, 1500, 73320, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF0D58, 0x5DC, 0xD994, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("Function_3_802")

    label("loc_83D")

    Return()

    # Function_3_802 end

    def Function_4_83E(): pass

    label("Function_4_83E")

    Sleep(2000)

    label("loc_843")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87E")
    SetChrPos(0xFE, -62120, 1500, 73320, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF0D58, 0x5DC, 0xD994, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_843")

    label("loc_87E")

    Return()

    # Function_4_83E end

    def Function_5_87F(): pass

    label("Function_5_87F")

    Sleep(3800)

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BF")
    SetChrPos(0xFE, -62120, 1500, 73320, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF0D58, 0x5DC, 0xD994, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_884")

    label("loc_8BF")

    Return()

    # Function_5_87F end

    def Function_6_8C0(): pass

    label("Function_6_8C0")

    Sleep(2000)

    label("loc_8C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_900")
    SetChrPos(0xFE, -56020, 1500, 73390, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF252C, 0x5DC, 0xD9C6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_8C5")

    label("loc_900")

    Return()

    # Function_6_8C0 end

    def Function_7_901(): pass

    label("Function_7_901")

    Sleep(4000)

    label("loc_906")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941")
    SetChrPos(0xFE, -56020, 1200, 73390, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF252C, 0x5DC, 0xD9C6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_906")

    label("loc_941")

    Return()

    # Function_7_901 end

    def Function_8_942(): pass

    label("Function_8_942")

    Sleep(5800)

    label("loc_947")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_982")
    SetChrPos(0xFE, -56020, 1200, 73390, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF252C, 0x5DC, 0xD9C6, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_947")

    label("loc_982")

    Return()

    # Function_8_942 end

    def Function_9_983(): pass

    label("Function_9_983")

    Sleep(1000)

    label("loc_988")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C3")
    SetChrPos(0xFE, -49970, 1500, 72960, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF3CCE, 0x5DC, 0xD9BC, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_988")

    label("loc_9C3")

    Return()

    # Function_9_983 end

    def Function_10_9C4(): pass

    label("Function_10_9C4")

    Sleep(3000)

    label("loc_9C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A04")
    SetChrPos(0xFE, -49970, 1500, 72960, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF3CCE, 0x5DC, 0xD9BC, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_9C9")

    label("loc_A04")

    Return()

    # Function_10_9C4 end

    def Function_11_A05(): pass

    label("Function_11_A05")

    Sleep(4800)

    label("loc_A0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A45")
    SetChrPos(0xFE, -49970, 1500, 72960, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFF3CCE, 0x5DC, 0xD9BC, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_A0A")

    label("loc_A45")

    Return()

    # Function_11_A05 end

    def Function_12_A46(): pass

    label("Function_12_A46")

    OP_EA(0x2, 0x9F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x0, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "Found #2C#56IEarth Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D00)
    Jump("loc_B27")

    label("loc_AC1")


    AnonymousTalk(    #1
        (
            "\x07\x05Now that all my contents are gone I feel so lost.\x01",
            "What's my purpose? Why am I here? Who am I?!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B27")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_A46 end

    def Function_13_B39(): pass

    label("Function_13_B39")

    OP_EA(0x2, 0xA0, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C11")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_BAA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\x6C\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D02)
    Jump("loc_C0E")

    label("loc_BAA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\x6C\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6C\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_C0E")

    Jump("loc_C8B")

    label("loc_C11")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05There's nothing in the chest. You briefly\x01",
            "wonder if you could use it as a makeshift\x01",
            "boat...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_B39 end

    def Function_14_C99(): pass

    label("Function_14_C99")

    OP_EA(0x2, 0xA1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x156, 1)"), scpexpr(EXPR_END)), "loc_D0A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\x56\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D04)
    Jump("loc_D6E")

    label("loc_D0A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\x56\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x56\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_D6E")

    Jump("loc_DE5")

    label("loc_D71")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05In the dust, you can faintly make out the imprint\x01",
            "of whatever was in here previously.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DE5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_C99 end

    def Function_15_DF3(): pass

    label("Function_15_DF3")

    OP_EA(0x2, 0x7, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDD")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_E4A():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E4A)

    def lambda_E65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E65)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #8
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x423, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_EB8"),
        (2, "loc_ECA"),
        (1, "loc_EDA"),
        (SWITCH_DEFAULT, "loc_EDD"),
    )


    label("loc_EB8")

    OP_A2(0x1D06)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_EDD")

    label("loc_ECA")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_EDA")

    OP_B4(0x0)
    Return()

    label("loc_EDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xEB, 1)"), scpexpr(EXPR_END)), "loc_F29")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        "Found \x1F\xEB\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D05)
    Jump("loc_F8B")

    label("loc_F29")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        (
            "Found \x1F\xEB\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xEB\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_F8B")

    Jump("loc_1021")

    label("loc_F8E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        (
            "\x07\x05Did you hear about the girl who paid for\x01",
            "everything with black sepith crystals? She said it\x01",
            "was only costing her time!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1021")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_DF3 end

    def Function_16_102F(): pass

    label("Function_16_102F")

    OP_EA(0x2, 0xA2, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1107")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_10A0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D07)
    Jump("loc_1104")

    label("loc_10A0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1104")

    Jump("loc_1190")

    label("loc_1107")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This chest's proud possessions have already\x01",
            "passed to some wandering adventurer's\x01",
            "satchel. Probably yours.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1190")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_102F end

    def Function_17_119E(): pass

    label("Function_17_119E")

    OP_EA(0x2, 0xA3, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1276")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29A, 1)"), scpexpr(EXPR_END)), "loc_120F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\x9A\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D08)
    Jump("loc_1273")

    label("loc_120F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\x9A\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x9A\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1273")

    Jump("loc_12F0")

    label("loc_1276")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05The chest's empty, but if you keep opening and\x01",
            "closing the lid, it looks like it's talking!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_12F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_119E end

    def Function_18_12FE(): pass

    label("Function_18_12FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131F")
    Call(0, 35)
    Call(0, 36)

    label("loc_131F")

    SetChrPos(0x101, -63620, 20, 50130, 45)
    SetChrPos(0x109, -63800, 20, 48690, 45)
    SetChrPos(0xF8, -64780, 20, 50340, 45)
    SetChrPos(0xF9, -65010, 0, 48600, 45)
    OP_6D(-52780, 0, 64129, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(290000, 0)
    OP_6E(341, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_13B5():
        OP_6D(-64090, 20, 50870, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13B5)

    def lambda_13CD():
        OP_67(0, 5650, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CD)

    def lambda_13E5():
        OP_6B(3060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13E5)

    def lambda_13F5():
        OP_6C(349000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13F5)
    OP_6E(257, 6000)
    Sleep(500)

    ChrTalk(    #18
        0x101,
        "#1020F#6PWhat in the world...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1476")

    ChrTalk(    #19
        0x107,
        "#065FThis looks like a factory of some sort...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14AA")

    label("loc_1476")


    ChrTalk(    #20
        0x109,
        "#1064F#1POkay, I expected a lot, but not this.\x02",
    )

    CloseMessageWindow()

    label("loc_14AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E5")

    ChrTalk(    #21
        0x106,
        "#552FHuh... Don't see anyone around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_14E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1525")

    ChrTalk(    #22
        0x108,
        "#072F#6PHmm... I don't see anyone around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_1525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1578")

    ChrTalk(    #23
        0x103,
        (
            "#022FThat's strange... There doesn't seem\x01",
            "to be anyone here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_1578")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B3")

    ChrTalk(    #24
        0x104,
        "#032FHmmm... No one is present. Odd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F5")

    label("loc_15B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F5")

    ChrTalk(    #25
        0x105,
        "#042FThere...don't seem to be any people here.\x02",
    )

    CloseMessageWindow()

    label("loc_15F5")

    OP_22(0x12F, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1654")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1692")

    label("loc_1654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1692")

    label("loc_167B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F7")

    label("loc_16B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16F7")

    label("loc_16E0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16F7")

    Sleep(1000)

    def lambda_1702():
        OP_6D(-58600, 20, 46370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1702)

    def lambda_171A():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_171A)

    def lambda_172A():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_172A)
    OP_8C(0x101, 90, 400)
    OP_8C(0x109, 90, 400)
    OP_8C(0xF8, 90, 400)
    OP_8C(0xF9, 90, 400)
    WaitChrThread(0x101, 0x0)
    OP_43(0xA, 0x1, 0x0, 0x14)
    OP_43(0xB, 0x1, 0x0, 0x15)
    OP_43(0xC, 0x1, 0x0, 0x16)
    OP_43(0xA, 0x3, 0x0, 0x2)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2)
    Sleep(1000)

    def lambda_178A():
        OP_6D(-62310, 0, 49610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_178A)

    def lambda_17A2():
        OP_67(0, 5650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A2)

    def lambda_17BA():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17BA)

    def lambda_17CA():
        OP_6E(318, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17CA)
    WaitChrThread(0x101, 0x3)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 14)
    Sleep(100)
    SetChrChipByIndex(0x109, 21)
    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_182C"),
        (5, "loc_1834"),
        (3, "loc_183C"),
        (4, "loc_1844"),
        (6, "loc_184C"),
        (7, "loc_1854"),
        (SWITCH_DEFAULT, "loc_185C"),
    )


    label("loc_182C")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_185C")

    label("loc_1834")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_185C")

    label("loc_183C")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_185C")

    label("loc_1844")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_185C")

    label("loc_184C")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_185C")

    label("loc_1854")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_185C")

    label("loc_185C")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1882"),
        (5, "loc_188A"),
        (3, "loc_1892"),
        (4, "loc_189A"),
        (6, "loc_18A2"),
        (7, "loc_18AA"),
        (SWITCH_DEFAULT, "loc_18B2"),
    )


    label("loc_1882")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_18B2")

    label("loc_188A")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_18B2")

    label("loc_1892")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_18B2")

    label("loc_189A")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_18B2")

    label("loc_18A2")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_18B2")

    label("loc_18AA")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_18B2")

    label("loc_18B2")

    OP_0D()
    Sleep(200)

    ChrTalk(    #26
        0x101,
        "#1005F#6PNo way!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F8")

    ChrTalk(    #27
        0x106,
        "#054F#6PArchaisms?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19CB")

    label("loc_18F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(    #28
        0x103,
        "#024F#6PArchaisms?! Here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19CB")

    label("loc_1929")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1961")

    ChrTalk(    #29
        0x105,
        "#042F#6PIt can't be...archaisms?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19CB")

    label("loc_1961")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199D")

    ChrTalk(    #30
        0x104,
        "#030F#6POh? Archaisms... Interesting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19CB")

    label("loc_199D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19CB")

    ChrTalk(    #31
        0x108,
        "#076F#6PArchaisms! How...?\x02",
    )

    CloseMessageWindow()

    label("loc_19CB")

    WaitChrThread(0x101, 0x0)

    def lambda_19D6():
        OP_6D(-63790, 20, 49470, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19D6)

    def lambda_19EE():
        OP_6B(1980, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19EE)
    SetChrChipByIndex(0xB, 1)

    def lambda_1A03():
        OP_8E(0xFE, 0xFFFF0B0A, 0x0, 0xC080, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1A03)
    Sleep(50)
    SetChrChipByIndex(0xA, 7)

    def lambda_1A28():
        OP_8E(0xFE, 0xFFFF0D3A, 0x0, 0xC594, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1A28)
    Sleep(50)
    SetChrChipByIndex(0xC, 7)

    def lambda_1A4D():
        OP_8E(0xFE, 0xFFFF0E7A, 0x14, 0xBA9A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1A4D)
    Sleep(300)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x2)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x422, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1A94"),
        (SWITCH_DEFAULT, "loc_1A99"),
    )


    label("loc_1A94")

    OP_B4(0x0)
    Jump("loc_1A99")

    label("loc_1A99")

    Call(0, 19)
    Return()

    # Function_18_12FE end

    def Function_19_1A9E(): pass

    label("Function_19_1A9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0xA, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x2)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -60280, 20, 49830, 90)
    SetChrPos(0x109, -60280, 20, 48430, 90)
    SetChrPos(0xF8, -61780, 0, 49890, 90)
    SetChrPos(0xF9, -61660, 0, 48470, 90)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x109, 21)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1B4D"),
        (5, "loc_1B55"),
        (3, "loc_1B5D"),
        (4, "loc_1B65"),
        (6, "loc_1B6D"),
        (7, "loc_1B75"),
        (SWITCH_DEFAULT, "loc_1B7D"),
    )


    label("loc_1B4D")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_1B7D")

    label("loc_1B55")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_1B7D")

    label("loc_1B5D")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_1B7D")

    label("loc_1B65")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_1B7D")

    label("loc_1B6D")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_1B7D")

    label("loc_1B75")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_1B7D")

    label("loc_1B7D")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1BA3"),
        (5, "loc_1BAB"),
        (3, "loc_1BB3"),
        (4, "loc_1BBB"),
        (6, "loc_1BC3"),
        (7, "loc_1BCB"),
        (SWITCH_DEFAULT, "loc_1BD3"),
    )


    label("loc_1BA3")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1BD3")

    label("loc_1BAB")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_1BD3")

    label("loc_1BB3")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1BD3")

    label("loc_1BBB")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_1BD3")

    label("loc_1BC3")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_1BD3")

    label("loc_1BCB")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_1BD3")

    label("loc_1BD3")

    OP_6D(-61210, 0, 49410, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(305, 0)

    def lambda_1C16():
        OP_6B(2370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C16)
    FadeToBright(2000, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x109, 65535)
    Sleep(100)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x101, 0x2)

    def lambda_1C5E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C5E)
    Sleep(100)

    def lambda_1C71():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C71)
    Sleep(100)
    OP_8C(0xF8, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D4F")

    ChrTalk(    #32
        0x101,
        (
            "#1007F#4PPhew! I think we're still alive.\x01",
            "Mostly.\x02\x03",

            "#1002FBut these things... They're the same\x01",
            "as the ones that showed up in the mine!\x02\x03",

            "So they really are society-controlled\x01",
            "archaisms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC2")

    label("loc_1D4F")


    ChrTalk(    #33
        0x101,
        (
            "#1007F#4PPhew! I think we're still alive.\x01",
            "Mostly.\x02\x03",

            "#1002FBut were those...were those the society's\x01",
            "archaisms?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC2")


    ChrTalk(    #34
        0x109,
        (
            "#1065F#6PYeah...\x02\x03",

            "#1063F'Cept they ain't 'archaic.'\x01",
            "They're like the ones that assaulted us on\x01",
            "the Ahnenburg. They were made recently.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F01")

    ChrTalk(    #35
        0x107,
        (
            "#062F#6PIn that case...\x02\x03",

            "This area might be a factory of\x01",
            "some sort for orbal weapon parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1002F#4PGood point. A lot of the same parts\x01",
            "are rolling along.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F76")

    ChrTalk(    #37
        0x105,
        (
            "#049F#6PBut it's strange...\x02\x03",

            "Despite all the noise we made,\x01",
            "I don't see or hear anyone coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_1F76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #38
        0x104,
        (
            "#034F#6PThere is something else curious, I fear.\x02\x03",

            "We made a scene to raise Gehenna,\x01",
            "yet this place remains as silent as a tomb.\x01",
            "No one is coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2095")

    ChrTalk(    #39
        0x108,
        (
            "#572F#6PIt is strange, though...\x02\x03",

            "Despite all the noise we made,\x01",
            "no one has come to investigate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2095")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2140")

    ChrTalk(    #40
        0x103,
        (
            "#522F#6PAnd something else strange is going on...\x02\x03",

            "We made quite a bit of noise, and I'm sure most\x01",
            "of the building heard it, but...no one is coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2140")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D6")

    ChrTalk(    #41
        0x106,
        (
            "#552F#6PSomethin' funny's going on...\x02\x03",

            "Half the damn building shoulda heard that\x01",
            "racket, and yet, there still ain't anyone\x01",
            "coming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D6")


    ChrTalk(    #42
        0x101,
        (
            "#1026F#4PYeah, you're right...\x02\x03",

            "#1003FYou'd think that Anelace or even one of\x01",
            "the Enforcers would come to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1065F#6PThose things were probably on some\x01",
            "kinda automated patrol.\x02\x03",

            "#1063FLooks like we really do need to check\x01",
            "every corner.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C06)
    OP_28(0x98, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_19_1A9E end

    def Function_20_22E2(): pass

    label("Function_20_22E2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_230E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_230E)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF204A, 0x0, 0xC968, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 6)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_20_22E2 end

    def Function_21_2354(): pass

    label("Function_21_2354")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2385():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2385)
    SetChrChipByIndex(0xB, 1)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF1C8A, 0x0, 0xBF40, 0x1388, 0x0)
    SetChrChipByIndex(0xB, 0)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_21_2354 end

    def Function_22_23CB(): pass

    label("Function_22_23CB")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_23FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23FC)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF204A, 0x0, 0xB4A0, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 6)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_22_23CB end

    def Function_23_2442(): pass

    label("Function_23_2442")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Move Lever]\x01",      # 0
            "[Don't]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EA")
    Sleep(200)
    OP_B0(0x1E, 0x3C)
    OP_6F(0x1E, 1)
    OP_70(0x1E, 0x3C)
    OP_22(0x64, 0x0, 0x64)
    OP_73(0x1E)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1C07)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_24EC")

    label("loc_24EA")

    EventEnd(0x1)

    label("loc_24EC")

    Jump("loc_2592")

    label("loc_24EF")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Move Lever]\x01",      # 0
            "[Don't]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2590")
    Sleep(200)
    OP_B0(0x1E, 0x3C)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x1)
    OP_73(0x1E)
    OP_22(0x64, 0x0, 0x64)
    OP_73(0x1E)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x1C07)
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2592")

    label("loc_2590")

    EventEnd(0x1)

    label("loc_2592")

    Return()

    # Function_23_2442 end

    def Function_24_2593(): pass

    label("Function_24_2593")

    EventBegin(0x0)
    SetChrPos(0x0, -12060, 0, -18650, 271)
    SetChrPos(0x1, -12060, 0, -18650, 271)
    SetChrPos(0x2, -12060, 0, -18650, 271)
    SetChrPos(0x3, -12060, 0, -18650, 271)
    OP_6D(-12060, 0, -18650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_24_2593 end

    def Function_25_2623(): pass

    label("Function_25_2623")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269E")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_64(0x8, 0x1)
    OP_10(0x1F, 0x1)
    OP_A2(0x1C10)
    Jump("loc_26C2")

    label("loc_269E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26C2")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_26C2")

    label("loc_26C2")

    TalkEnd(0xFF)
    Return()

    # Function_25_2623 end

    def Function_26_26C6(): pass

    label("Function_26_26C6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2741")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0x17, 0x1E)
    OP_73(0x17)
    OP_64(0x9, 0x1)
    OP_10(0x20, 0x1)
    OP_A2(0x1C11)
    Jump("loc_2765")

    label("loc_2741")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2765")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2765")

    label("loc_2765")

    TalkEnd(0xFF)
    Return()

    # Function_26_26C6 end

    def Function_27_2769(): pass

    label("Function_27_2769")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E4")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_64(0xA, 0x1)
    OP_10(0x5, 0x1)
    OP_A2(0x1C12)
    Jump("loc_2808")

    label("loc_27E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2808")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2808")

    label("loc_2808")

    TalkEnd(0xFF)
    Return()

    # Function_27_2769 end

    def Function_28_280C(): pass

    label("Function_28_280C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2887")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0xB, 0x1)
    OP_10(0x1D, 0x1)
    OP_A2(0x1CA0)
    Jump("loc_28AB")

    label("loc_2887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28AB")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_28AB")

    label("loc_28AB")

    TalkEnd(0xFF)
    Return()

    # Function_28_280C end

    def Function_29_28AF(): pass

    label("Function_29_28AF")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_28CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_28CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_28DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_28EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_28EC")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2918"),
        (1, "loc_2925"),
        (3, "loc_297D"),
        (7, "loc_29FA"),
        (SWITCH_DEFAULT, "loc_2A9B"),
    )


    label("loc_2918")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A9B")

    label("loc_2925")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",      # 0
            "[Don't Use]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2960"),
        (1, "loc_296D"),
        (SWITCH_DEFAULT, "loc_297A"),
    )


    label("loc_2960")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_297A")

    label("loc_296D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_297A")

    label("loc_297A")

    Jump("loc_2A9B")

    label("loc_297D")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Don't Use]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29D0"),
        (1, "loc_29DD"),
        (2, "loc_29EA"),
        (SWITCH_DEFAULT, "loc_29F7"),
    )


    label("loc_29D0")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F7")

    label("loc_29DD")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F7")

    label("loc_29EA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F7")

    label("loc_29F7")

    Jump("loc_2A9B")

    label("loc_29FA")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Use Blue Cardkey]\x01",       # 2
            "[Don't Use]\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A64"),
        (1, "loc_2A71"),
        (2, "loc_2A7E"),
        (3, "loc_2A8B"),
        (SWITCH_DEFAULT, "loc_2A98"),
    )


    label("loc_2A64")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A98")

    label("loc_2A71")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A98")

    label("loc_2A7E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A98")

    label("loc_2A8B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A98")

    label("loc_2A98")

    Jump("loc_2A9B")

    label("loc_2A9B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_29_28AF end

    def Function_30_2AB3(): pass

    label("Function_30_2AB3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ACA")
    Call(0, 35)
    Call(0, 36)

    label("loc_2ACA")

    SetChrPos(0x9, -76750, 0, 162560, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, -76130, 20, 154070, 0)
    SetChrPos(0x109, -77410, 0, 153960, 0)
    SetChrPos(0xF8, -76130, 0, 152870, 0)
    SetChrPos(0xF9, -77410, 0, 152790, 0)
    OP_6D(-77510, 0, 153430, 0)
    OP_67(0, 8189, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(315000, 0)
    OP_6E(271, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #48
        0x101,
        "#1004F#6PWhat the...?!\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2B92():
        OP_6D(-77190, 20, 160620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B92)

    def lambda_2BAA():
        OP_67(0, 4880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BAA)

    def lambda_2BC2():
        OP_6B(2680, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BC2)

    def lambda_2BD2():
        OP_6E(317, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2BD2)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #49
        0x101,
        "#1018F#5PGrant!\x02",
    )

    CloseMessageWindow()

    def lambda_2BFC():
        OP_8E(0xFE, 0xFFFED77A, 0x14, 0x26AA2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BFC)
    Sleep(100)

    def lambda_2C1C():
        OP_8E(0xFE, 0xFFFED180, 0x14, 0x26B1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C1C)
    Sleep(130)

    def lambda_2C3C():
        OP_8E(0xFE, 0xFFFED77A, 0x0, 0x26520, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2C3C)
    Sleep(110)

    def lambda_2C5C():
        OP_8E(0xFE, 0xFFFED180, 0x0, 0x265A2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2C5C)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #50
        0x9,
        "#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1025F#5PThank Aidios, you're safe!\x02\x03",

            "Kurt told us what happened and\x01",
            "we came as soon as we--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        "#1063F#6PHold on... Something's up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1004F#5PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_2D25():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D25)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    Sleep(1000)

    ChrTalk(    #54
        0x9,
        "#827F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1020F#5PAh!\x02",
    )

    CloseMessageWindow()

    def lambda_2D6F():
        OP_6D(-77080, 20, 159880, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D6F)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2D99():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D99)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2DCB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DCB)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E07")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2E3B")

    label("loc_2E07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E29")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2E3B")

    label("loc_2E29")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_2E3B")


    def lambda_2E41():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2E41)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7D")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2EB1")

    label("loc_2E7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E9F")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2EB1")

    label("loc_2E9F")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_2EB1")


    def lambda_2EB7():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2EB7)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF5")

    ChrTalk(    #56
        0x106,
        "#057F#5PDamn it!\x02",
    )

    CloseMessageWindow()

    label("loc_2EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F18")

    ChrTalk(    #57
        0x107,
        "#065F#5PWaaaah!\x02",
    )

    CloseMessageWindow()

    label("loc_2F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(    #58
        0x103,
        "#523F#5PBlast it!\x02",
    )

    CloseMessageWindow()

    label("loc_2F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F69")

    ChrTalk(    #59
        0x108,
        "#077F#5PHe's been taken!\x02",
    )

    CloseMessageWindow()

    label("loc_2F69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8C")

    ChrTalk(    #60
        0x105,
        "#043F#5POh, no!\x02",
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB2")

    ChrTalk(    #61
        0x104,
        "#032F#5PTo battle!\x02",
    )

    CloseMessageWindow()

    label("loc_2FB2")

    Sleep(200)
    OP_43(0xA, 0x0, 0x0, 0x1F)
    Sleep(200)
    OP_43(0xC, 0x0, 0x0, 0x20)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 14)
    Sleep(100)
    SetChrChipByIndex(0x109, 21)
    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_3022"),
        (5, "loc_302A"),
        (3, "loc_3032"),
        (4, "loc_303A"),
        (6, "loc_3042"),
        (7, "loc_304A"),
        (SWITCH_DEFAULT, "loc_3052"),
    )


    label("loc_3022")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_3052")

    label("loc_302A")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_3052")

    label("loc_3032")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_3052")

    label("loc_303A")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_3052")

    label("loc_3042")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_3052")

    label("loc_304A")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_3052")

    label("loc_3052")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3078"),
        (5, "loc_3080"),
        (3, "loc_3088"),
        (4, "loc_3090"),
        (6, "loc_3098"),
        (7, "loc_30A0"),
        (SWITCH_DEFAULT, "loc_30A8"),
    )


    label("loc_3078")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_30A8")

    label("loc_3080")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_30A8")

    label("loc_3088")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_30A8")

    label("loc_3090")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_30A8")

    label("loc_3098")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_30A8")

    label("loc_30A0")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_30A8")

    label("loc_30A8")

    OP_0D()
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xC, 0x0)
    Sleep(1000)

    def lambda_30BE():
        OP_6D(-77520, 20, 158730, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30BE)

    def lambda_30D6():
        OP_6B(2230, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30D6)
    SetChrChipByIndex(0x9, 27)

    def lambda_30EB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_30EB)
    Sleep(50)
    SetChrChipByIndex(0xA, 7)

    def lambda_3110():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3110)
    Sleep(50)
    SetChrChipByIndex(0xC, 7)

    def lambda_3135():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_3135)
    Sleep(300)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x41E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_317C"),
        (SWITCH_DEFAULT, "loc_3181"),
    )


    label("loc_317C")

    OP_B4(0x0)
    Jump("loc_3181")

    label("loc_3181")

    Call(0, 33)
    Return()

    # Function_30_2AB3 end

    def Function_31_3186(): pass

    label("Function_31_3186")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -76000, 1200, 164220, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_31C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31C3)
    OP_8F(0xFE, 0xFFFED720, 0x0, 0x2817C, 0x7D0, 0x0)
    Return()

    # Function_31_3186 end

    def Function_32_31E4(): pass

    label("Function_32_31E4")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78260, 1200, 164170, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_3221():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3221)
    OP_8F(0xFE, 0xFFFECE4C, 0x0, 0x2814A, 0x7D0, 0x0)
    Return()

    # Function_32_31E4 end

    def Function_33_3242(): pass

    label("Function_33_3242")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    OP_44(0xC, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    SetChrPos(0x9, -76700, 20, 163790, 180)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -76090, 20, 161510, 0)
    SetChrPos(0x109, -77180, 20, 161610, 0)
    SetChrPos(0xF8, -75650, 20, 160360, 0)
    SetChrPos(0xF9, -77190, 20, 160470, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_6D(-76900, 20, 162590, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(315000, 0)
    OP_6E(298, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #62
        0x101,
        (
            "#1007F#6PHoooh...\x02\x03",

            "#1015FHow the heck does he manage...\x01",
            "swings like that?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F6")

    ChrTalk(    #63
        0x106,
        (
            "#552FSonuva...\x02\x03",

            "The Ravens are one thing,\x01",
            "but controlling a bracer like this...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354A")

    label("loc_33F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(    #64
        0x105,
        (
            "#049FHe's just like the Ravens who were\x01",
            "controlled at the lighthouse...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354A")

    label("loc_3454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B3")

    ChrTalk(    #65
        0x103,
        (
            "#522FThis is bad... I didn't think they'd be\x01",
            "able to do this to bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354A")

    label("loc_34B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_350A")

    ChrTalk(    #66
        0x104,
        (
            "#034FMy goodness... Even bracers are not\x01",
            "immune to such control.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_354A")

    label("loc_350A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_354A")

    ChrTalk(    #67
        0x108,
        "#074FHm... Even bracers can be controlled...\x02",
    )

    CloseMessageWindow()

    label("loc_354A")


    ChrTalk(    #68
        0x109,
        "#1065F#6PNow, then...\x02",
    )

    CloseMessageWindow()

    def lambda_356B():
        OP_6D(-76780, 0, 163200, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_356B)
    OP_8E(0x109, 0xFFFED360, 0x14, 0x27B28, 0x5DC, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(500)
    SetChrChipByIndex(0x109, 26)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(1000)
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0x109, 300, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    LoadEffect(0x0, "scraft\\\\sc001_05.eff")
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_9E(0x9, 0x14, 0x0, 0x1F4, 0xBB8)
    Sleep(1000)

    ChrTalk(    #69
        0x9,
        "#826F#4PGh...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x9, 1)
    Sleep(1000)

    ChrTalk(    #70
        0x9,
        "#825F#4P...Sorry. Guess I got in the way, huh?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_36E4():
        OP_8F(0xFE, 0xFFFED284, 0x14, 0x2774A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36E4)

    ChrTalk(    #71
        0x101,
        "#1025F#6PGrant! You're okay!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3767")

    ChrTalk(    #72
        0x103,
        (
            "#020FI'm guessing you understand what\x01",
            "happened, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3884")

    label("loc_3767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37AD")

    ChrTalk(    #73
        0x106,
        (
            "#051FHeh, got a handle on what\x01",
            "happened, Grant?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3884")

    label("loc_37AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F6")

    ChrTalk(    #74
        0x108,
        (
            "#070FLooks like you have a grasp\x01",
            "on what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3884")

    label("loc_37F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383F")

    ChrTalk(    #75
        0x104,
        (
            "#030FYou realize what happened, then,\x01",
            "my good man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3884")

    label("loc_383F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3884")

    ChrTalk(    #76
        0x105,
        (
            "#542FYou remember what happened,\x01",
            "then, Mr. Grant?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3884")


    ChrTalk(    #77
        0x9,
        (
            "#823F#4PYeah... Can't remember the face, but\x01",
            "someone...hijacked my mind or something.\x02\x03",

            "#822FI was ordered to stop any other\x01",
            "intruders coming through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1007F#6PIt must be that professor guy...\x02\x03",

            "#1002FGrant, where are Carna and Anelace?\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#824F#4PI don't... We got separated, and\x01",
            "they caught us each alone.\x02\x03",

            "They're probably chained up in\x01",
            "their own minds somewhere in\x01",
            "here like I was...\x02\x03",

            "#826FAgh...!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x14, 0x0, 0x1F4, 0xBB8)
    SetChrSubChip(0x9, 0)
    Sleep(500)

    ChrTalk(    #80
        0x101,
        "#1020F#6PGrant!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFED6EE, 0x14, 0x27C5E, 0x7D0, 0x0)
    Fade(250)
    OP_8C(0x101, 315, 400)
    SetChrChipByIndex(0x101, 24)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #81
        0x101,
        (
            "#1025F#6PHere, give me your shoulder.\x02\x03",

            "We've got a boat on the beach,\x01",
            "we'll take you there.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(200)

    ChrTalk(    #82
        0x9,
        (
            "#824F#4PNah, I'm okay.\x02\x03",

            "I know the layout of the building,\x01",
            "so I can get out on my own...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 10)
    OP_0D()
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 0, 400)
    OP_8F(0x101, 0xFFFED6C6, 0x14, 0x276E6, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #83
        0x9,
        (
            "#825F#4PI won't drag you guys down any further...\x02\x03",

            "Just...please, find Carna and Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1026F#6PGrant...\x02\x03",

            "#1006FYeah... Leave it to us!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C3D():

        label("loc_3C3D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3C3D")

    QueueWorkItem2(0x101, 1, lambda_3C3D)

    def lambda_3C4E():

        label("loc_3C4E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3C4E")

    QueueWorkItem2(0x109, 1, lambda_3C4E)

    def lambda_3C5F():

        label("loc_3C5F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3C5F")

    QueueWorkItem2(0xF8, 1, lambda_3C5F)

    def lambda_3C70():

        label("loc_3C70")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3C70")

    QueueWorkItem2(0xF9, 1, lambda_3C70)

    def lambda_3C81():
        OP_6D(-76640, 50, 156810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C81)
    OP_8E(0x9, 0xFFFEDC8E, 0x14, 0x27790, 0x7D0, 0x0)

    def lambda_3CAD():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CAD)
    OP_8E(0x9, 0xFFFEDD9C, 0x14, 0x269F8, 0x9C4, 0x0)

    def lambda_3CDB():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CDB)
    OP_8E(0x9, 0xFFFED428, 0x0, 0x254FE, 0x7D0, 0x0)

    def lambda_3D09():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D09)
    OP_8E(0x9, 0xFFFED400, 0x0, 0x24EA0, 0x9C4, 0x0)

    def lambda_3D37():
        OP_8E(0xFE, 0xFFFED3F6, 0x0, 0x24C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D37)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_3D7C():
        OP_6D(-76830, 0, 161490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D7C)
    OP_8C(0x101, 180, 400)
    OP_8C(0x109, 180, 400)
    OP_8C(0xF8, 180, 400)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(200)

    ChrTalk(    #85
        0x101,
        "#1015F#4PIs he really gonna be okay...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)

    ChrTalk(    #86
        0x109,
        (
            "#1065F#6PFor now we just need to\x01",
            "trust him and keep movin'.\x02\x03",

            "#1060FThere's two more, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #87
        0x101,
        "#1002F#4PYeah...\x02",
    )

    CloseMessageWindow()

    def lambda_3E6C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3E6C)
    Sleep(50)

    def lambda_3E7F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3E7F)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(    #88
        0x106,
        (
            "#057F#6PWe'll need to get movin', then.\x01",
            "C'mon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FA2")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F03")

    ChrTalk(    #89
        0x103,
        "#022F#6PLet us hurry, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FA2")

    label("loc_3F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F3E")

    ChrTalk(    #90
        0x104,
        "#032F#6PHm. Let us make haste, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FA2")

    label("loc_3F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F76")

    ChrTalk(    #91
        0x108,
        "#072F#6PLet's move quickly, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FA2")

    label("loc_3F76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA2")

    ChrTalk(    #92
        0x105,
        "#042F#6PWe should hurry!\x02",
    )

    CloseMessageWindow()

    label("loc_3FA2")

    OP_A2(0x1C08)
    OP_28(0x98, 0x1, 0x8)
    OP_28(0x98, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_33_3242 end

    def Function_34_3FB4(): pass

    label("Function_34_3FB4")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x1D, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #93
        (
            "\x07\x02#1S[Archaism Classification] The orbal droid weapons\x01",
            "utilized by the society are modeled after the ancient\x01",
            "archaism weapons and developed by the research\x01",
            "organization the 'Thirteen Factories,' under the direct\x01",
            "command of an Anguis.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x1D, 0x0, 0x2)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #94
        (
            "\x07\x02#1SFurthermore, these facilities produce primarily standardized\x01",
            "humanoid units, such as both types of patrol units, the\x01",
            "'Vogel,' the scout unit 'Port Seeker,' as well as the combat\x01",
            "unit 'Vanguard,' but development based on the Guardian for\x01",
            "new... (※FOLLOWING TEXT REDACTED)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4256")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #95
        "\x07\x00Received #1018i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FA, 1)
    Sleep(500)

    label("loc_4256")

    OP_A2(0x1C09)
    OP_28(0x98, 0x1, 0x20)
    OP_74(0x1D, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_34_3FB4 end

    def Function_35_4275(): pass

    label("Function_35_4275")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_42F1"),
        (1, "loc_42F7"),
        (SWITCH_DEFAULT, "loc_42FD"),
    )


    label("loc_42F1")

    OP_A2(0x1200)
    Jump("loc_42FD")

    label("loc_42F7")

    OP_A2(0x1201)
    Jump("loc_42FD")

    label("loc_42FD")

    Return()

    # Function_35_4275 end

    def Function_36_42FE(): pass

    label("Function_36_42FE")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_36_42FE end

    def Function_37_435B(): pass

    label("Function_37_435B")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05The gate is locked tight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_37_435B end

    def Function_38_43C1(): pass

    label("Function_38_43C1")

    OP_A2(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_38_43C1 end

    def Function_39_43D4(): pass

    label("Function_39_43D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_45F5")

    label("loc_443A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #98
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45DA")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x1, 0x2)
    PlayEffect(0x1, 0x1, 0xFF, -9010, 1000, 138700, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1F, 0)
    OP_70(0x1F, 0x32)
    OP_73(0x1F)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x1, 0x2)
    LoadEffect(0x2, "map\\\\mp027_01.eff")
    PlayEffect(0x2, 0x2, 0xFF, -9010, 1000, 138700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x2, 0x2)
    PlayEffect(0x1, 0x1, 0xFF, -9010, 1000, 138700, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1F, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_45DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45F4")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_45F4")

    Return()

    label("loc_45F5")

    Return()

    # Function_39_43D4 end

    SaveToFile()

Try(main)
