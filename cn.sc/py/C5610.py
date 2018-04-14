from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '库拉茨',                               # 10
        '哨兵235',                              # 11
        '哨兵570',                              # 12
        '哨兵235',                              # 13
        '零部件',                               # 14
        '零部件',                               # 15
        '零部件',                               # 16
        '零部件',                               # 17
        '零部件',                               # 18
        '零部件',                               # 19
        '零部件',                               # 20
        '零部件',                               # 21
        '零部件',                               # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
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
        "Function_13_AEB",         # 0D, 13
        "Function_14_C02",         # 0E, 14
        "Function_15_D19",         # 0F, 15
        "Function_16_EE9",         # 10, 16
        "Function_17_1000",        # 11, 17
        "Function_18_1117",        # 12, 18
        "Function_19_1869",        # 13, 19
        "Function_20_1E69",        # 14, 20
        "Function_21_1EDB",        # 15, 21
        "Function_22_1F52",        # 16, 22
        "Function_23_1FC9",        # 17, 23
        "Function_24_2128",        # 18, 24
        "Function_25_21B8",        # 19, 25
        "Function_26_2254",        # 1A, 26
        "Function_27_22F0",        # 1B, 27
        "Function_28_238C",        # 1C, 28
        "Function_29_2428",        # 1D, 29
        "Function_30_2636",        # 1E, 30
        "Function_31_2D31",        # 1F, 31
        "Function_32_2D8F",        # 20, 32
        "Function_33_2DED",        # 21, 33
        "Function_34_39A4",        # 22, 34
        "Function_35_3B78",        # 23, 35
        "Function_36_3C02",        # 24, 36
        "Function_37_3C5F",        # 25, 37
        "Function_38_3CBA",        # 26, 38
        "Function_39_3CCD",        # 27, 39
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

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x0, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D00)
    Jump("loc_AD9")

    label("loc_ABF")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_AD9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_A46 end

    def Function_13_AEB(): pass

    label("Function_13_AEB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_B5A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x6C\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D02)
    Jump("loc_BC0")

    label("loc_B5A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\x6C\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x6C\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_BC0")

    Jump("loc_BF4")

    label("loc_BC3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BF4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_AEB end

    def Function_14_C02(): pass

    label("Function_14_C02")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x156, 1)"), scpexpr(EXPR_END)), "loc_C71")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x56\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D04)
    Jump("loc_CD7")

    label("loc_C71")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x56\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x56\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_CD7")

    Jump("loc_D0B")

    label("loc_CDA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D0B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_C02 end

    def Function_15_D19(): pass

    label("Function_15_D19")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF8")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D6B():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D6B)

    def lambda_D86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D86)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #8
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x423, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DD3"),
        (2, "loc_DE5"),
        (1, "loc_DF5"),
        (SWITCH_DEFAULT, "loc_DF8"),
    )


    label("loc_DD3")

    OP_A2(0x1D06)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_DF8")

    label("loc_DE5")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DF5")

    OP_B4(0x0)
    Return()

    label("loc_DF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xEB, 1)"), scpexpr(EXPR_END)), "loc_E47")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xEB\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D05)
    Jump("loc_EA9")

    label("loc_E47")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xEB\x00\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xEB\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_EA9")

    Jump("loc_EDB")

    label("loc_EAC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EDB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_D19 end

    def Function_16_EE9(): pass

    label("Function_16_EE9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_F58")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D07)
    Jump("loc_FBE")

    label("loc_F58")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_FBE")

    Jump("loc_FF2")

    label("loc_FC1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FF2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_EE9 end

    def Function_17_1000(): pass

    label("Function_17_1000")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29A, 1)"), scpexpr(EXPR_END)), "loc_106F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x9A\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D08)
    Jump("loc_10D5")

    label("loc_106F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\x9A\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x9A\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_10D5")

    Jump("loc_1109")

    label("loc_10D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1109")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1000 end

    def Function_18_1117(): pass

    label("Function_18_1117")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112E")
    Call(0, 35)
    Call(0, 36)

    label("loc_112E")

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

    def lambda_11C4():
        OP_6D(-64090, 20, 50870, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11C4)

    def lambda_11DC():
        OP_67(0, 5650, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11DC)

    def lambda_11F4():
        OP_6B(3060, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11F4)

    def lambda_1204():
        OP_6C(349000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1204)
    OP_6E(257, 6000)
    Sleep(500)

    ChrTalk(    #18
        0x101,
        "#1020F#6P这、这里是什么地方……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1279")

    ChrTalk(    #19
        0x107,
        (
            "#065F#6P像是某种\x01",
            "零部件的工厂……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_1279")


    ChrTalk(    #20
        0x109,
        (
            "#1064F#6P居然来到了这么\x01",
            "古怪的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12DF")

    ChrTalk(    #21
        0x106,
        (
            "#552F#6P哼……\x01",
            "似乎没有人的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_12DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1317")

    ChrTalk(    #22
        0x108,
        (
            "#072F#6P唔……\x01",
            "似乎没有人的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_1317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134F")

    ChrTalk(    #23
        0x103,
        (
            "#022F#6P唔……\x01",
            "似乎没有人的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_134F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1389")

    ChrTalk(    #24
        0x104,
        (
            "#032F#6P唔……\x01",
            "似乎没有人的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CC")

    label("loc_1389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(    #25
        0x105,
        (
            "#042F#6P………………………\x01",
            "似乎没有人的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CC")

    OP_22(0x12F, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1469")

    label("loc_142B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1452")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1469")

    label("loc_1452")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1469")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1490")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14CE")

    label("loc_1490")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B7")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14CE")

    label("loc_14B7")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14CE")

    Sleep(1000)

    def lambda_14D9():
        OP_6D(-58600, 20, 46370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14D9)

    def lambda_14F1():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14F1)

    def lambda_1501():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1501)
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

    def lambda_1561():
        OP_6D(-62310, 0, 49610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1561)

    def lambda_1579():
        OP_67(0, 5650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1579)

    def lambda_1591():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1591)

    def lambda_15A1():
        OP_6E(318, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_15A1)
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
        (2, "loc_1603"),
        (5, "loc_160B"),
        (3, "loc_1613"),
        (4, "loc_161B"),
        (6, "loc_1623"),
        (7, "loc_162B"),
        (SWITCH_DEFAULT, "loc_1633"),
    )


    label("loc_1603")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_1633")

    label("loc_160B")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_1633")

    label("loc_1613")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_1633")

    label("loc_161B")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_1633")

    label("loc_1623")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_1633")

    label("loc_162B")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_1633")

    label("loc_1633")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1659"),
        (5, "loc_1661"),
        (3, "loc_1669"),
        (4, "loc_1671"),
        (6, "loc_1679"),
        (7, "loc_1681"),
        (SWITCH_DEFAULT, "loc_1689"),
    )


    label("loc_1659")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_1689")

    label("loc_1661")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_1689")

    label("loc_1669")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_1689")

    label("loc_1671")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_1689")

    label("loc_1679")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_1689")

    label("loc_1681")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_1689")

    label("loc_1689")

    OP_0D()
    Sleep(200)

    ChrTalk(    #26
        0x101,
        "#1005F#5P这、这些是！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D9")

    ChrTalk(    #27
        0x106,
        "#054F#5P人形兵器吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_16D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(    #28
        0x103,
        "#024F#5P人形兵器！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_1704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1739")

    ChrTalk(    #29
        0x105,
        "#042F#5P难道是……人形兵器！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_1739")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(    #30
        0x104,
        "#030F#5P哦……人形兵器吗！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_176A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(    #31
        0x108,
        "#076F#5P人形兵器吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_1796")

    WaitChrThread(0x101, 0x0)

    def lambda_17A1():
        OP_6D(-63790, 20, 49470, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17A1)

    def lambda_17B9():
        OP_6B(1980, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17B9)
    SetChrChipByIndex(0xB, 1)

    def lambda_17CE():
        OP_8E(0xFE, 0xFFFF0B0A, 0x0, 0xC080, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_17CE)
    Sleep(50)
    SetChrChipByIndex(0xA, 7)

    def lambda_17F3():
        OP_8E(0xFE, 0xFFFF0D3A, 0x0, 0xC594, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_17F3)
    Sleep(50)
    SetChrChipByIndex(0xC, 7)

    def lambda_1818():
        OP_8E(0xFE, 0xFFFF0E7A, 0x14, 0xBA9A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1818)
    Sleep(300)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x2)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x422, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_185F"),
        (SWITCH_DEFAULT, "loc_1864"),
    )


    label("loc_185F")

    OP_B4(0x0)
    Jump("loc_1864")

    label("loc_1864")

    Call(0, 19)
    Return()

    # Function_18_1117 end

    def Function_19_1869(): pass

    label("Function_19_1869")

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
        (2, "loc_1918"),
        (5, "loc_1920"),
        (3, "loc_1928"),
        (4, "loc_1930"),
        (6, "loc_1938"),
        (7, "loc_1940"),
        (SWITCH_DEFAULT, "loc_1948"),
    )


    label("loc_1918")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_1948")

    label("loc_1920")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_1948")

    label("loc_1928")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_1948")

    label("loc_1930")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_1948")

    label("loc_1938")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_1948")

    label("loc_1940")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_1948")

    label("loc_1948")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_196E"),
        (5, "loc_1976"),
        (3, "loc_197E"),
        (4, "loc_1986"),
        (6, "loc_198E"),
        (7, "loc_1996"),
        (SWITCH_DEFAULT, "loc_199E"),
    )


    label("loc_196E")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_199E")

    label("loc_1976")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_199E")

    label("loc_197E")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_199E")

    label("loc_1986")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_199E")

    label("loc_198E")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_199E")

    label("loc_1996")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_199E")

    label("loc_199E")

    OP_6D(-61210, 0, 49410, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(305, 0)

    def lambda_19E1():
        OP_6B(2370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19E1)
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

    def lambda_1A29():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A29)
    Sleep(100)

    def lambda_1A3C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A3C)
    Sleep(100)
    OP_8C(0xF8, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AD0")

    ChrTalk(    #32
        0x101,
        (
            "#1007F#2P呼～吓我一跳。\x02\x03",

            "#1002F不过刚才的那些……\x01",
            "和废坑中出现的一模一样呢。\x02\x03",

            "果然是『结社』的\x01",
            "人形兵器吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1C")

    label("loc_1AD0")


    ChrTalk(    #33
        0x101,
        (
            "#1007F#2P呼～吓我一跳。\x02\x03",

            "#1002F不过这个……\x01",
            "就是『结社』的人形兵器吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1C")


    ChrTalk(    #34
        0x109,
        (
            "#1065F#6P啊啊……\x02\x03",

            "#1063F和亚宁堡那里出现的一模一样，\x01",
            "是用现代的导力技术制造的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFB")

    ChrTalk(    #35
        0x107,
        (
            "#062F#5P那、那么……\x02\x03",

            "这个区域，或许就是人形兵器的\x01",
            "零部件制造工厂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1002F#2P确实到处散乱着\x01",
            "一样的零件呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(    #37
        0x105,
        (
            "#049F#5P不过，真是不可思议……\x02\x03",

            "刚才引起那样的骚动，\x01",
            "却没有人过来看的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBC")

    label("loc_1C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB7")

    ChrTalk(    #38
        0x104,
        (
            "#034F#5P唔，真是奇怪。\x02\x03",

            "刚才引起那样的骚动，\x01",
            "却没有人过来看的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBC")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D0F")

    ChrTalk(    #39
        0x108,
        (
            "#572F#5P真是奇怪……\x02\x03",

            "刚才引起那样的骚动，\x01",
            "却没有人过来看的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBC")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6F")

    ChrTalk(    #40
        0x103,
        (
            "#522F#5P不过，真是奇怪啊……\x02\x03",

            "刚才引起那样的骚动，\x01",
            "却没有人过来看的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBC")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(    #41
        0x106,
        (
            "#552F#5P真是奇怪……\x02\x03",

            "引起那样的骚动\x01",
            "没有人聚集的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBC")


    ChrTalk(    #42
        0x101,
        (
            "#1026F#2P的确……\x02\x03",

            "#1003F……亚妮拉丝他们\x01",
            "真的是被抓来这里的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1065F#6P这些大概是\x01",
            "自动巡逻中的人形兵器吧。\x02\x03",

            "#1063F总之其它的区域\x01",
            "也一并调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C06)
    OP_28(0x98, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_19_1869 end

    def Function_20_1E69(): pass

    label("Function_20_1E69")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1E95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E95)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF204A, 0x0, 0xC968, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 6)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_20_1E69 end

    def Function_21_1EDB(): pass

    label("Function_21_1EDB")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1F0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F0C)
    SetChrChipByIndex(0xB, 1)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF1C8A, 0x0, 0xBF40, 0x1388, 0x0)
    SetChrChipByIndex(0xB, 0)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_21_1EDB end

    def Function_22_1F52(): pass

    label("Function_22_1F52")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -55980, 0, 42910, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1F83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F83)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xFE, 0xFFFF2554, 0x0, 0xB086, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF204A, 0x0, 0xB4A0, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 6)
    OP_8C(0xFE, 266, 400)
    Return()

    # Function_22_1F52 end

    def Function_23_1FC9(): pass

    label("Function_23_1FC9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【扳动拉杆】\x01",        # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2078")
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
    Jump("loc_207A")

    label("loc_2078")

    EventEnd(0x1)

    label("loc_207A")

    Jump("loc_2127")

    label("loc_207D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【扳动拉杆】\x01",        # 0
            "【什么也不做】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2125")
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
    Jump("loc_2127")

    label("loc_2125")

    EventEnd(0x1)

    label("loc_2127")

    Return()

    # Function_23_1FC9 end

    def Function_24_2128(): pass

    label("Function_24_2128")

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

    # Function_24_2128 end

    def Function_25_21B8(): pass

    label("Function_25_21B8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222C")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_64(0x8, 0x1)
    OP_10(0x1F, 0x1)
    OP_A2(0x1C10)
    Jump("loc_2250")

    label("loc_222C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2250")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2250")

    label("loc_2250")

    TalkEnd(0xFF)
    Return()

    # Function_25_21B8 end

    def Function_26_2254(): pass

    label("Function_26_2254")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C8")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0x17, 0x1E)
    OP_73(0x17)
    OP_64(0x9, 0x1)
    OP_10(0x20, 0x1)
    OP_A2(0x1C11)
    Jump("loc_22EC")

    label("loc_22C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22EC")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_22EC")

    label("loc_22EC")

    TalkEnd(0xFF)
    Return()

    # Function_26_2254 end

    def Function_27_22F0(): pass

    label("Function_27_22F0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2364")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_64(0xA, 0x1)
    OP_10(0x5, 0x1)
    OP_A2(0x1C12)
    Jump("loc_2388")

    label("loc_2364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2388")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2388")

    label("loc_2388")

    TalkEnd(0xFF)
    Return()

    # Function_27_22F0 end

    def Function_28_238C(): pass

    label("Function_28_238C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 29)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2400")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0xB, 0x1)
    OP_10(0x1D, 0x1)
    OP_A2(0x1CA0)
    Jump("loc_2424")

    label("loc_2400")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2424")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2424")

    label("loc_2424")

    TalkEnd(0xFF)
    Return()

    # Function_28_238C end

    def Function_29_2428(): pass

    label("Function_29_2428")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_2443")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_2454")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_2465")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2465")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2491"),
        (1, "loc_249E"),
        (3, "loc_24FA"),
        (7, "loc_257A"),
        (SWITCH_DEFAULT, "loc_261E"),
    )


    label("loc_2491")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261E")

    label("loc_249E")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【什么也不做】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24DD"),
        (1, "loc_24EA"),
        (SWITCH_DEFAULT, "loc_24F7"),
    )


    label("loc_24DD")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F7")

    label("loc_24EA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F7")

    label("loc_24F7")

    Jump("loc_261E")

    label("loc_24FA")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【什么也不做】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2550"),
        (1, "loc_255D"),
        (2, "loc_256A"),
        (SWITCH_DEFAULT, "loc_2577"),
    )


    label("loc_2550")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2577")

    label("loc_255D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2577")

    label("loc_256A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2577")

    label("loc_2577")

    Jump("loc_261E")

    label("loc_257A")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【使用蓝色密码卡】\x01",      # 2
            "【什么也不做】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25E7"),
        (1, "loc_25F4"),
        (2, "loc_2601"),
        (3, "loc_260E"),
        (SWITCH_DEFAULT, "loc_261B"),
    )


    label("loc_25E7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261B")

    label("loc_25F4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261B")

    label("loc_2601")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261B")

    label("loc_260E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_261B")

    label("loc_261B")

    Jump("loc_261E")

    label("loc_261E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_29_2428 end

    def Function_30_2636(): pass

    label("Function_30_2636")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264D")
    Call(0, 35)
    Call(0, 36)

    label("loc_264D")

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
        "#1004F#6P咦……！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2712():
        OP_6D(-77190, 20, 160620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2712)

    def lambda_272A():
        OP_67(0, 4880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_272A)

    def lambda_2742():
        OP_6B(2680, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2742)

    def lambda_2752():
        OP_6E(317, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2752)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #49
        0x101,
        "#1018F#5P库拉茨前辈！\x02",
    )

    CloseMessageWindow()

    def lambda_2782():
        OP_8E(0xFE, 0xFFFED77A, 0x14, 0x26AA2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2782)
    Sleep(100)

    def lambda_27A2():
        OP_8E(0xFE, 0xFFFED180, 0x14, 0x26B1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27A2)
    Sleep(130)

    def lambda_27C2():
        OP_8E(0xFE, 0xFFFED77A, 0x0, 0x26520, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_27C2)
    Sleep(110)

    def lambda_27E2():
        OP_8E(0xFE, 0xFFFED180, 0x0, 0x265A2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_27E2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #50
        0x9,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1025F#6P太好了，你没事啊！\x02\x03",

            "听克鲁茨前辈说明情况之后，\x01",
            "我们也过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        "#1063F#6P等等……他的表情很奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_28AD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28AD)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    Sleep(1000)

    ChrTalk(    #54
        0x9,
        "#827F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1020F#6P啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_2911():
        OP_6D(-77080, 20, 159880, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2911)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_293B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_293B)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_296D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_296D)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A9")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_29DD")

    label("loc_29A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CB")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_29DD")

    label("loc_29CB")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_29DD")


    def lambda_29E3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_29E3)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1F")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2A53")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A41")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2A53")

    label("loc_2A41")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_2A53")


    def lambda_2A59():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2A59)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A95")

    ChrTalk(    #56
        0x106,
        "#057F#6P……！\x02",
    )

    CloseMessageWindow()

    label("loc_2A95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ABB")

    ChrTalk(    #57
        0x107,
        "#065F#6P啊哇哇……\x02",
    )

    CloseMessageWindow()

    label("loc_2ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE3")

    ChrTalk(    #58
        0x103,
        "#523F#6P难不成……！\x02",
    )

    CloseMessageWindow()

    label("loc_2AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(    #59
        0x108,
        "#077F#6P……中计了吗！\x02",
    )

    CloseMessageWindow()

    label("loc_2B0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B35")

    ChrTalk(    #60
        0x105,
        "#043F#6P怎么会……！\x02",
    )

    CloseMessageWindow()

    label("loc_2B35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5D")

    ChrTalk(    #61
        0x104,
        "#032F#6P糟糕了……！\x02",
    )

    CloseMessageWindow()

    label("loc_2B5D")

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
        (2, "loc_2BCD"),
        (5, "loc_2BD5"),
        (3, "loc_2BDD"),
        (4, "loc_2BE5"),
        (6, "loc_2BED"),
        (7, "loc_2BF5"),
        (SWITCH_DEFAULT, "loc_2BFD"),
    )


    label("loc_2BCD")

    SetChrChipByIndex(0xF8, 15)
    Jump("loc_2BFD")

    label("loc_2BD5")

    SetChrChipByIndex(0xF8, 16)
    Jump("loc_2BFD")

    label("loc_2BDD")

    SetChrChipByIndex(0xF8, 17)
    Jump("loc_2BFD")

    label("loc_2BE5")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_2BFD")

    label("loc_2BED")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_2BFD")

    label("loc_2BF5")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_2BFD")

    label("loc_2BFD")

    Sleep(100)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_2C23"),
        (5, "loc_2C2B"),
        (3, "loc_2C33"),
        (4, "loc_2C3B"),
        (6, "loc_2C43"),
        (7, "loc_2C4B"),
        (SWITCH_DEFAULT, "loc_2C53"),
    )


    label("loc_2C23")

    SetChrChipByIndex(0xF9, 15)
    Jump("loc_2C53")

    label("loc_2C2B")

    SetChrChipByIndex(0xF9, 16)
    Jump("loc_2C53")

    label("loc_2C33")

    SetChrChipByIndex(0xF9, 17)
    Jump("loc_2C53")

    label("loc_2C3B")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_2C53")

    label("loc_2C43")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_2C53")

    label("loc_2C4B")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_2C53")

    label("loc_2C53")

    OP_0D()
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xC, 0x0)
    Sleep(1000)

    def lambda_2C69():
        OP_6D(-77520, 20, 158730, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C69)

    def lambda_2C81():
        OP_6B(2230, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C81)
    SetChrChipByIndex(0x9, 27)

    def lambda_2C96():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C96)
    Sleep(50)
    SetChrChipByIndex(0xA, 7)

    def lambda_2CBB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2CBB)
    Sleep(50)
    SetChrChipByIndex(0xC, 7)

    def lambda_2CE0():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2CE0)
    Sleep(300)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x41E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2D27"),
        (SWITCH_DEFAULT, "loc_2D2C"),
    )


    label("loc_2D27")

    OP_B4(0x0)
    Jump("loc_2D2C")

    label("loc_2D2C")

    Call(0, 33)
    Return()

    # Function_30_2636 end

    def Function_31_2D31(): pass

    label("Function_31_2D31")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -76000, 1200, 164220, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2D6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D6E)
    OP_8F(0xFE, 0xFFFED720, 0x0, 0x2817C, 0x7D0, 0x0)
    Return()

    # Function_31_2D31 end

    def Function_32_2D8F(): pass

    label("Function_32_2D8F")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78260, 1200, 164170, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2DCC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DCC)
    OP_8F(0xFE, 0xFFFECE4C, 0x0, 0x2814A, 0x7D0, 0x0)
    Return()

    # Function_32_2D8F end

    def Function_33_2DED(): pass

    label("Function_33_2DED")

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
            "#1007F#6P呼呼……\x02\x03",

            "#1015F实、实在是……\x01",
            "相当不好对付呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F83")

    ChrTalk(    #63
        0x106,
        (
            "#552F#6P哼……\x02\x03",

            "『渡鸦帮』的那些人还好说，\x01",
            "居然连游击士都能操纵……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_2F83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FCF")

    ChrTalk(    #64
        0x105,
        (
            "#049F#6P……和在灯塔被操纵的\x01",
            "『渡鸦帮』那些人一样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3013")

    ChrTalk(    #65
        0x103,
        (
            "#522F#6P伤脑筋了……\x01",
            "没想到连游击士也能操纵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_3013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3053")

    ChrTalk(    #66
        0x104,
        (
            "#034F#6P哎呀呀……\x01",
            "居然连游击士也能操纵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_3053")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308C")

    ChrTalk(    #67
        0x108,
        (
            "#074F#6P唔……\x01",
            "居然连游击士也能操纵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308C")


    ChrTalk(    #68
        0x109,
        "#1065F#6P接下来……\x02",
    )

    CloseMessageWindow()

    def lambda_30AB():
        OP_6D(-76780, 0, 163200, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30AB)
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
        "#826F#2P唔……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x9, 1)
    Sleep(1000)

    ChrTalk(    #70
        0x9,
        (
            "#825F#2P……抱歉……\x01",
            "好像给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()

    def lambda_3220():
        OP_8F(0xFE, 0xFFFED284, 0x14, 0x2774A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3220)

    ChrTalk(    #71
        0x101,
        "#1025F#6P库拉茨前辈……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3288")

    ChrTalk(    #72
        0x103,
        (
            "#020F#6P看来搞清楚\x01",
            "状况了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_3288")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32C0")

    ChrTalk(    #73
        0x106,
        (
            "#051F#6P哦，看来搞清楚\x01",
            "状况了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_32C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F4")

    ChrTalk(    #74
        0x108,
        (
            "#070F#6P看来搞清楚\x01",
            "状况了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_32F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_332C")

    ChrTalk(    #75
        0x104,
        (
            "#030F#6P呼，看来搞清楚\x01",
            "状况了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3361")

    label("loc_332C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3361")

    ChrTalk(    #76
        0x105,
        (
            "#542F#6P看来好像\x01",
            "搞清楚状况了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3361")


    ChrTalk(    #77
        0x9,
        (
            "#823F#2P嗯嗯，虽然想不起对方长相，\x01",
            "但确实被某人夺取了我的意识……\x02\x03",

            "#822F然后命令我在这里\x01",
            "击退新的侵入者……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1007F#6P是那个『教授』吧……\x02\x03",

            "#1002F你知道亚妮拉丝和\x01",
            "卡露娜她们在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#824F#2P不……我们是分别被抓来的。\x02\x03",

            "应该和我一样\x01",
            "被抓到某处去了……\x02\x03",

            "#826F呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x14, 0x0, 0x1F4, 0xBB8)
    SetChrSubChip(0x9, 0)
    Sleep(500)

    ChrTalk(    #80
        0x101,
        "#1020F#6P没、没事吗！？\x02",
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
            "#1025F#6P来，扶我的肩膀。\x02\x03",

            "悬崖下有条小船，\x01",
            "我带你到那里去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(200)

    ChrTalk(    #82
        0x9,
        (
            "#824F#5P不、不要紧……\x02\x03",

            "我知道这个建筑物的构造，\x01",
            "一个人也可以逃出去……\x02",
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
            "#825F#2P而且我也不想\x01",
            "再继续扯你们的后腿了……\x02\x03",

            "就算是请你们代替我吧，\x01",
            "卡露娜和亚妮拉丝就拜托了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1026F#6P库拉茨前辈……\x02\x03",

            "#1006F嗯……交给我们吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3667():

        label("loc_3667")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3667")

    QueueWorkItem2(0x101, 1, lambda_3667)

    def lambda_3678():

        label("loc_3678")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3678")

    QueueWorkItem2(0x109, 1, lambda_3678)

    def lambda_3689():

        label("loc_3689")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3689")

    QueueWorkItem2(0xF8, 1, lambda_3689)

    def lambda_369A():

        label("loc_369A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_369A")

    QueueWorkItem2(0xF9, 1, lambda_369A)

    def lambda_36AB():
        OP_6D(-76640, 50, 156810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36AB)
    OP_8E(0x9, 0xFFFEDC8E, 0x14, 0x27790, 0x7D0, 0x0)

    def lambda_36D7():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_36D7)
    OP_8E(0x9, 0xFFFEDD9C, 0x14, 0x269F8, 0x9C4, 0x0)

    def lambda_3705():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3705)
    OP_8E(0x9, 0xFFFED428, 0x0, 0x254FE, 0x7D0, 0x0)

    def lambda_3733():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3733)
    OP_8E(0x9, 0xFFFED400, 0x0, 0x24EA0, 0x9C4, 0x0)

    def lambda_3761():
        OP_8E(0xFE, 0xFFFED3F6, 0x0, 0x24C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3761)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_37A6():
        OP_6D(-76830, 0, 161490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37A6)
    OP_8C(0x101, 180, 400)
    OP_8C(0x109, 180, 400)
    OP_8C(0xF8, 180, 400)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(200)

    ChrTalk(    #85
        0x101,
        "#1015F#2P没、没问题吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)

    ChrTalk(    #86
        0x109,
        (
            "#1065F#5P现在只有相信那位老兄\x01",
            "继续前进了。\x02\x03",

            "#1060F还剩两个人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #87
        0x101,
        "#1002F#4P嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_386C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_386C)
    Sleep(50)

    def lambda_387F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_387F)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C2")

    ChrTalk(    #88
        0x106,
        (
            "#057F#6P哎……\x01",
            "看来动作要快了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_38C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F5")

    ChrTalk(    #89
        0x103,
        "#022F#6P看来动作要快了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_38F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_392B")

    ChrTalk(    #90
        0x104,
        (
            "#032F#6P唔……\x01",
            "看来动作要快了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_392B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3960")

    ChrTalk(    #91
        0x108,
        "#072F#6P看来要抓紧时间了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_3960")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3992")

    ChrTalk(    #92
        0x105,
        "#042F#6P看来要抓紧时间了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_3992")

    OP_A2(0x1C08)
    OP_28(0x98, 0x1, 0x8)
    OP_28(0x98, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_33_2DED end

    def Function_34_39A4(): pass

    label("Function_34_39A4")

    EventBegin(0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x1D, 0x0, 0x3)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #93
        (
            "\x07\x02#1S『人形兵器的种类』\x01",
            " \x01",
            "结社运用的人形兵器\x01",
            "是使徒直属研究机关『十三工房』\x01",
            "所开发的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_74(0x1D, 0x0, 0x2)
    SetMessageWindowPos(-1, -1, 24, 5)

    AnonymousTalk(    #94
        (
            "\x07\x02#1S此外，本设施中，\x01",
            "除了预警机『哨兵２』类型以外，\x01",
            "侦察机『目标探索者』，战斗机『亡命守护者』等\x01",
            "旧型号的人形兵器也是主要生产的对象，\x01",
            "但也有参考『守护者』开发新的型号……（※以下删除）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B59")
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #95
        "\x07\x00得到了\x1F\xFA\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FA, 1)
    Sleep(500)

    label("loc_3B59")

    OP_A2(0x1C09)
    OP_28(0x98, 0x1, 0x20)
    OP_74(0x1D, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x1)
    Return()

    # Function_34_39A4 end

    def Function_35_3B78(): pass

    label("Function_35_3B78")

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
        (0, "loc_3BF5"),
        (1, "loc_3BFB"),
        (SWITCH_DEFAULT, "loc_3C01"),
    )


    label("loc_3BF5")

    OP_A2(0x1200)
    Jump("loc_3C01")

    label("loc_3BFB")

    OP_A2(0x1201)
    Jump("loc_3C01")

    label("loc_3C01")

    Return()

    # Function_35_3B78 end

    def Function_36_3C02(): pass

    label("Function_36_3C02")

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

    # Function_36_3C02 end

    def Function_37_3C5F(): pass

    label("Function_37_3C5F")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #96
        "\x07\x05门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_37_3C5F end

    def Function_38_3CBA(): pass

    label("Function_38_3CBA")

    OP_A2(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_38_3CBA end

    def Function_39_3CCD(): pass

    label("Function_39_3CCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3EDC")

    label("loc_3D1E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #98
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC1")
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

    label("loc_3EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EDB")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3EDB")

    Return()

    label("loc_3EDC")

    Return()

    # Function_39_3CCD end

    SaveToFile()

Try(main)
