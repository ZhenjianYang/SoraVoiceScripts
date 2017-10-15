from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5400   ._SN',
        MapName             = 'Other',
        Location            = 'C5400.x',
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
        'Joshua',                               # 9
        'Joshua',                               # 10
        'Joshua',                               # 11
        'Renne',                                # 12
        'Enhanced Jaeger',                      # 13
        'Enhanced Jaeger',                      # 14
        'Loewe',                                # 15
        'Don',                                  # 16
        'Kyle',                                 # 17
        'Sky Bandit Lonnie',                    # 18
        'Sky Bandit Aaron',                     # 19
        'Sky Bandit Lyall',                     # 20
        'Sky Bandit Ryan',                      # 21
        'Sky Bandit',                           # 22
        'Sky Bandit',                           # 23
        'ヴォーグル570（青）',                  # 24
        'ヴォーグル235（赤）',                  # 25
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
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT27/CH03001 ._CH',             # 01
        'ED6_DT26/CH20380 ._CH',             # 02
        'ED6_DT27/CH03005 ._CH',             # 03
        'ED6_DT26/CH20235 ._CH',             # 04
        'ED6_DT26/CH20376 ._CH',             # 05
        'ED6_DT27/CH03510 ._CH',             # 06
        'ED6_DT27/CH03000 ._CH',             # 07
        'ED6_DT27/CH04620 ._CH',             # 08
        'ED6_DT27/CH03003 ._CH',             # 09
        'ED6_DT07/CH02040 ._CH',             # 0A
        'ED6_DT27/CH04621 ._CH',             # 0B
        'ED6_DT27/CH04622 ._CH',             # 0C
        'ED6_DT27/CH04623 ._CH',             # 0D
        'ED6_DT26/CH20384 ._CH',             # 0E
        'ED6_DT27/CH04624 ._CH',             # 0F
        'ED6_DT26/CH20237 ._CH',             # 10
        'ED6_DT27/CH04001 ._CH',             # 11
        'ED6_DT26/CH20501 ._CH',             # 12
        'ED6_DT27/CH04002 ._CH',             # 13
        'ED6_DT26/CH20381 ._CH',             # 14
        'ED6_DT27/CH04000 ._CH',             # 15
        'ED6_DT07/CH00343 ._CH',             # 16
        'ED6_DT07/CH00341 ._CH',             # 17
        'ED6_DT07/CH00344 ._CH',             # 18
        'ED6_DT29/CH12570 ._CH',             # 19
        'ED6_DT29/CH12571 ._CH',             # 1A
        'ED6_DT29/CH12350 ._CH',             # 1B
        'ED6_DT29/CH12351 ._CH',             # 1C
        'ED6_DT07/CH02110 ._CH',             # 1D
        'ED6_DT07/CH02120 ._CH',             # 1E
        'ED6_DT07/CH01380 ._CH',             # 1F
        'ED6_DT26/CH20208 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT27/CH03001P._CP',             # 01
        'ED6_DT26/CH20380P._CP',             # 02
        'ED6_DT27/CH03005P._CP',             # 03
        'ED6_DT26/CH20235P._CP',             # 04
        'ED6_DT26/CH20376P._CP',             # 05
        'ED6_DT27/CH03510P._CP',             # 06
        'ED6_DT27/CH03000P._CP',             # 07
        'ED6_DT27/CH04620P._CP',             # 08
        'ED6_DT27/CH03003P._CP',             # 09
        'ED6_DT07/CH02040P._CP',             # 0A
        'ED6_DT27/CH04621P._CP',             # 0B
        'ED6_DT27/CH04622P._CP',             # 0C
        'ED6_DT27/CH04623P._CP',             # 0D
        'ED6_DT26/CH20384P._CP',             # 0E
        'ED6_DT27/CH04624P._CP',             # 0F
        'ED6_DT26/CH20237P._CP',             # 10
        'ED6_DT27/CH04001P._CP',             # 11
        'ED6_DT26/CH20501P._CP',             # 12
        'ED6_DT27/CH04002P._CP',             # 13
        'ED6_DT26/CH20381P._CP',             # 14
        'ED6_DT27/CH04000P._CP',             # 15
        'ED6_DT07/CH00343P._CP',             # 16
        'ED6_DT07/CH00341P._CP',             # 17
        'ED6_DT07/CH00344P._CP',             # 18
        'ED6_DT29/CH12570P._CP',             # 19
        'ED6_DT29/CH12571P._CP',             # 1A
        'ED6_DT29/CH12350P._CP',             # 1B
        'ED6_DT29/CH12351P._CP',             # 1C
        'ED6_DT07/CH02110P._CP',             # 1D
        'ED6_DT07/CH02120P._CP',             # 1E
        'ED6_DT07/CH01380P._CP',             # 1F
        'ED6_DT26/CH20208P._CP',             # 20
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
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
        Unknown3            = 32,
        ChipIndex           = 0x20,
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
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -134110,
        Z                   = 0,
        Y                   = 45880,
        Unknown_0C          = 0,
        Unknown_0E          = 25,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -135340,
        Z                   = 0,
        Y                   = -27900,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 2850,
        Y                   = 0,
        Z                   = 22850,
        Range               = 5160,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x6112,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = -52950,
        Y                   = 0,
        Z                   = -61000,
        Range               = -51020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF1730,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -42980,
        Y                   = -1000,
        Z                   = 75190,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 55,
    )

    DeclEvent(
        X                   = -36920,
        Y                   = -1000,
        Z                   = -67150,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 70070,
        Y                   = -1000,
        Z                   = -234030,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = -90500,
        Y                   = 0,
        Z                   = -343710,
        Range               = -85100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFAC61C,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = -131900,
        TriggerZ            = 0,
        TriggerY            = 10590,
        TriggerRange        = 1000,
        ActorX              = -131900,
        ActorZ              = 0,
        ActorY              = 11210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87000,
        TriggerZ            = 0,
        TriggerY            = -342900,
        TriggerRange        = 1000,
        ActorX              = -87000,
        ActorZ              = 1000,
        ActorY              = -343080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -127350,
        TriggerZ            = 0,
        TriggerY            = -58920,
        TriggerRange        = 1000,
        ActorX              = -126610,
        ActorZ              = 0,
        ActorY              = -58850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37010,
        TriggerZ            = 0,
        TriggerY            = -67050,
        TriggerRange        = 1000,
        ActorX              = -37010,
        ActorZ              = 1200,
        ActorY              = -67050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 43,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61080,
        TriggerZ            = 0,
        TriggerY            = -184550,
        TriggerRange        = 1000,
        ActorX              = 61080,
        ActorZ              = 1000,
        ActorY              = -184550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61000,
        TriggerZ            = 0,
        TriggerY            = -27060,
        TriggerRange        = 1000,
        ActorX              = 61000,
        ActorZ              = 1000,
        ActorY              = -27060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52900,
        TriggerZ            = 0,
        TriggerY            = -53160,
        TriggerRange        = 1000,
        ActorX              = 52880,
        ActorZ              = 1000,
        ActorY              = -52540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79360,
        TriggerZ            = 0,
        TriggerY            = -318070,
        TriggerRange        = 1000,
        ActorX              = -78700,
        ActorZ              = 0,
        ActorY              = -318100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -79400,
        TriggerZ            = 0,
        TriggerY            = -298090,
        TriggerRange        = 1000,
        ActorX              = -78740,
        ActorZ              = 0,
        ActorY              = -298130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37430,
        TriggerZ            = 0,
        TriggerY            = 73910,
        TriggerRange        = 1000,
        ActorX              = -37430,
        ActorZ              = 1000,
        ActorY              = 73910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 60,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38100,
        TriggerZ            = 0,
        TriggerY            = -71790,
        TriggerRange        = 1000,
        ActorX              = -38100,
        ActorZ              = 1000,
        ActorY              = -71790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83920,
        TriggerZ            = 0,
        TriggerY            = -346980,
        TriggerRange        = 1000,
        ActorX              = -83920,
        ActorZ              = 1000,
        ActorY              = -346980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 62,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_63A",          # 00, 0
        "Function_1_6E7",          # 01, 1
        "Function_2_9CA",          # 02, 2
        "Function_3_B47",          # 03, 3
        "Function_4_B4C",          # 04, 4
        "Function_5_C5A",          # 05, 5
        "Function_6_D29",          # 06, 6
        "Function_7_E7F",          # 07, 7
        "Function_8_FA0",          # 08, 8
        "Function_9_11B7",         # 09, 9
        "Function_10_1349",        # 0A, 10
        "Function_11_149B",        # 0B, 11
        "Function_12_1620",        # 0C, 12
        "Function_13_1730",        # 0D, 13
        "Function_14_2368",        # 0E, 14
        "Function_15_2BCB",        # 0F, 15
        "Function_16_2C82",        # 10, 16
        "Function_17_2D4B",        # 11, 17
        "Function_18_3106",        # 12, 18
        "Function_19_3230",        # 13, 19
        "Function_20_329D",        # 14, 20
        "Function_21_5E44",        # 15, 21
        "Function_22_5E59",        # 16, 22
        "Function_23_6596",        # 17, 23
        "Function_24_79B8",        # 18, 24
        "Function_25_7A30",        # 19, 25
        "Function_26_7B32",        # 1A, 26
        "Function_27_7BE9",        # 1B, 27
        "Function_28_7DE7",        # 1C, 28
        "Function_29_7E57",        # 1D, 29
        "Function_30_7EA9",        # 1E, 30
        "Function_31_7EFB",        # 1F, 31
        "Function_32_97B9",        # 20, 32
        "Function_33_97D5",        # 21, 33
        "Function_34_97F1",        # 22, 34
        "Function_35_980D",        # 23, 35
        "Function_36_9829",        # 24, 36
        "Function_37_98A3",        # 25, 37
        "Function_38_9D66",        # 26, 38
        "Function_39_A0B2",        # 27, 39
        "Function_40_A0E6",        # 28, 40
        "Function_41_A116",        # 29, 41
        "Function_42_A146",        # 2A, 42
        "Function_43_A15B",        # 2B, 43
        "Function_44_B2D7",        # 2C, 44
        "Function_45_B363",        # 2D, 45
        "Function_46_C20F",        # 2E, 46
        "Function_47_C290",        # 2F, 47
        "Function_48_C2D4",        # 30, 48
        "Function_49_C304",        # 31, 49
        "Function_50_C348",        # 32, 50
        "Function_51_C38C",        # 33, 51
        "Function_52_C3D0",        # 34, 52
        "Function_53_C400",        # 35, 53
        "Function_54_C430",        # 36, 54
        "Function_55_C44C",        # 37, 55
        "Function_56_C465",        # 38, 56
        "Function_57_C47E",        # 39, 57
        "Function_58_C497",        # 3A, 58
        "Function_59_C51D",        # 3B, 59
        "Function_60_C5AE",        # 3C, 60
        "Function_61_C5D4",        # 3D, 61
        "Function_62_C5FA",        # 3E, 62
    )


    def Function_0_63A(): pass

    label("Function_0_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_654")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_6E6")

    label("loc_654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_665")
    OP_A3(0x10F1)
    Event(0, 14)
    Jump("loc_6E6")

    label("loc_665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_67F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    Event(0, 20)
    Jump("loc_6E6")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_699")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    Event(0, 22)
    Jump("loc_6E6")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_6AA")
    OP_A3(0x10F4)
    Event(0, 17)
    Jump("loc_6E6")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_6C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 23)
    Jump("loc_6E6")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7F), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E6")
    Event(0, 38)

    label("loc_6E6")

    Return()

    # Function_0_63A end

    def Function_1_6E7(): pass

    label("Function_1_6E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_6F(0x25, 0)
    Jump("loc_71E")

    label("loc_717")

    OP_6F(0x25, 60)

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    OP_6F(0x26, 0)
    Jump("loc_737")

    label("loc_730")

    OP_6F(0x26, 60)

    label("loc_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")
    OP_6F(0x2B, 0)
    Jump("loc_750")

    label("loc_749")

    OP_6F(0x2B, 60)

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    OP_6F(0x2C, 0)
    Jump("loc_769")

    label("loc_762")

    OP_6F(0x2C, 60)

    label("loc_769")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783")
    OP_64(0x2, 0x1)
    OP_71(0x25, 0x0)
    OP_71(0x25, 0x4)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    OP_6F(0x2D, 0)
    Jump("loc_79C")

    label("loc_795")

    OP_6F(0x2D, 60)

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE")
    OP_6F(0x2E, 0)
    Jump("loc_7B5")

    label("loc_7AE")

    OP_6F(0x2E, 60)

    label("loc_7B5")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E1")
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x12F, 7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x12F, 0x1000)

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    SetChrPos(0xB, 70380, 0, -234050, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_72(0x1A, 0x10)

    label("loc_80F")

    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_823")
    OP_65(0x3, 0x1)
    OP_72(0x17, 0x10)

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_931")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_END)), "loc_85B")
    SetChrPos(0xF, -84180, 0, -335080, 270)
    SetChrPos(0x10, -84470, 0, -336340, 270)
    Jump("loc_87D")

    label("loc_85B")

    SetChrPos(0xF, -81860, 0, -334130, 180)
    SetChrPos(0x10, -81190, 0, -335370, 0)

    label("loc_87D")

    SetChrPos(0x11, -82890, 0, -331950, 45)
    SetChrPos(0x14, -81710, 0, -332430, 270)
    SetChrPos(0x15, -81980, 0, -331150, 180)
    SetChrPos(0x13, -81220, 0, -336530, 225)
    SetChrPos(0x12, -81780, 0, -338160, 0)
    SetChrPos(0x16, -82670, 0, -337380, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_65(0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_72(0x17, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_END)), "loc_951")
    OP_65(0x2, 0x1)
    OP_6F(0x25, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_951")
    OP_6F(0x25, 60)

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_969")
    OP_6F(0x3, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_END)), "loc_981")
    OP_6F(0x4, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_END)), "loc_999")
    OP_6F(0x5, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_END)), "loc_9B1")
    OP_6F(0x6, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_END)), "loc_9C9")
    OP_6F(0x7, 50)
    OP_71(0x23, 0x4)
    OP_72(0x24, 0x4)

    label("loc_9C9")

    Return()

    # Function_1_6E7 end

    def Function_2_9CA(): pass

    label("Function_2_9CA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EF")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B31")

    label("loc_9EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A08")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B31")

    label("loc_A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B31")

    label("loc_A21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B31")

    label("loc_A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A53")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B31")

    label("loc_A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B31")

    label("loc_A6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A85")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B31")

    label("loc_A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B31")

    label("loc_A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B31")

    label("loc_AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD0")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B31")

    label("loc_AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE9")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B31")

    label("loc_AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B31")

    label("loc_B02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B31")

    label("loc_B1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B31")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B46")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B31")

    label("loc_B46")

    Return()

    # Function_2_9CA end

    def Function_3_B47(): pass

    label("Function_3_B47")

    Call(0, 19)
    Return()

    # Function_3_B47 end

    def Function_4_B4C(): pass

    label("Function_4_B4C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_BB1")

    ChrTalk(    #0
        0xF,
        (
            "#490FYou found the card!\x02\x03",

            "#191FThat simplifies things!\x01",
            "Let's make good our escape.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_BB1")


    ChrTalk(    #1
        0xF,
        (
            "#197FThis place is too damn big, if you ask me.\x01",
            "I don't have a clue where the second floor\x01",
            "of the forecastle area would be.\x02\x03",

            "#199FRight, go on. But be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C56")

    TalkEnd(0xF)
    Return()

    # Function_4_B4C end

    def Function_5_C5A(): pass

    label("Function_5_C5A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #2
        0x10,
        (
            "#204FGood to see you made it back safe.\x02\x03",

            "#200FThere's no time. Let's get out of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D25")

    label("loc_CC2")


    ChrTalk(    #3
        0x10,
        (
            "#204FSome jaegers just came by here on patrol.\x02\x03",

            "#206FWatch out. Make sure they don't see you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D25")

    TalkEnd(0x10)
    Return()

    # Function_5_C5A end

    def Function_6_D29(): pass

    label("Function_6_D29")

    OP_EA(0x2, 0x53, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E01")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_D9A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\x87\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D30)
    Jump("loc_DFE")

    label("loc_D9A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\x87\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x87\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_DFE")

    Jump("loc_E71")

    label("loc_E01")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05The chest is empty. Please come back tomorrow\x01",
            "at 9 AM sharp for your free refill.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E71")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_D29 end

    def Function_7_E7F(): pass

    label("Function_7_E7F")

    OP_EA(0x2, 0x54, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F57")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_EF0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D31)
    Jump("loc_F54")

    label("loc_EF0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
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

    label("loc_F54")

    Jump("loc_F92")

    label("loc_F57")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05I dunno what you expected...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F92")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_E7F end

    def Function_8_FA0(): pass

    label("Function_8_FA0")

    OP_EA(0x2, 0x55, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1EF, 1)"), scpexpr(EXPR_END)), "loc_1011")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\xEF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3B)
    Jump("loc_1075")

    label("loc_1011")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\xEF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xEF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_1075")

    Jump("loc_1128")

    label("loc_1078")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05No matter where you go in this life, there's\x01",
            "always someone looking to take you for all you've\x01",
            "got. It happened to me, and it WILL happen to you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1128")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x44)"), scpexpr(EXPR_END)), "loc_1147")
    Jump("loc_11AE")

    label("loc_1147")


    AnonymousTalk(    #13
        (
            "\x07\x00Found a scrap of paper with a [ #495i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "\x07\x00Learned [ #495i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_11AE")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_FA0 end

    def Function_9_11B7(): pass

    label("Function_9_11B7")

    OP_EA(0x2, 0x56, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_1228")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3C)
    Jump("loc_128C")

    label("loc_1228")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
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

    label("loc_128C")

    Jump("loc_133B")

    label("loc_128F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05I know it's not much fun to open an empty chest,\x01",
            "but think about how much fun it was to open\x01",
            "when it still had something in it! Ah, memories.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_133B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_11B7 end

    def Function_10_1349(): pass

    label("Function_10_1349")

    OP_EA(0x2, 0x57, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1440")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x1E)
    OP_73(0x2D)
    OP_6F(0x2D, 30)
    AddSepith(0x0, 0x12C)
    AddSepith(0x1, 0x12C)
    AddSepith(0x2, 0x12C)
    AddSepith(0x3, 0x12C)
    AddSepith(0x4, 0x12C)
    AddSepith(0x5, 0x12C)
    AddSepith(0x6, 0x12C)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x300#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D4A)
    Jump("loc_1489")

    label("loc_1440")


    AnonymousTalk(    #19
        (
            "\x07\x05The chest is now filled with shame.\x01",
            "The shame of a double-dipper.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1489")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1349 end

    def Function_11_149B(): pass

    label("Function_11_149B")

    OP_EA(0x2, 0x58, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1573")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12A, 1)"), scpexpr(EXPR_END)), "loc_150C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "Found \x1F\x2A\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D4B)
    Jump("loc_1570")

    label("loc_150C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "Found \x1F\x2A\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2A\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_1570")

    Jump("loc_1612")

    label("loc_1573")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05You open the empty chest open again and again,\x01",
            "cackling manically to yourself. You KNOW it\x01",
            "contains some secret. It just has to!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1612")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_149B end

    def Function_12_1620(): pass

    label("Function_12_1620")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1639")
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_172F")

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_16A8")
    OP_64(0x4, 0x1)
    SetChrPos(0xC, 54170, 0, 12070, 270)
    SetChrPos(0xD, 60700, 0, 7800, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xC, 15)
    SetChrSubChip(0xD, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A2")
    OP_22(0x1C3, 0x0, 0x64)
    Jump("loc_16A5")

    label("loc_16A2")

    OP_23(0x1C3)

    label("loc_16A5")

    Jump("loc_172F")

    label("loc_16A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 3)), scpexpr(EXPR_END)), "loc_16BC")
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_172F")

    label("loc_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x391, 1)), scpexpr(EXPR_END)), "loc_16F4")
    OP_64(0x4, 0x1)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 270)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x48), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F(0x64, 0x0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_172F")

    label("loc_16F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_END)), "loc_1719")
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    Jump("loc_172F")

    label("loc_1719")

    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)

    label("loc_172F")

    Return()

    # Function_12_1620 end

    def Function_13_1730(): pass

    label("Function_13_1730")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_D6(0x1)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_31(0xFF, 0xFE, 0x0)
    SetChrPos(0x101, 78890, 0, 5300, 270)
    SetChrPos(0x8, 84600, 0, 5600, 270)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(79330, 0, 5940, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x101,
        "\x07\x00#1003F#6PThis is...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #24
        "\x07\x05#40W...Estelle...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5B)
    Sleep(500)

    def lambda_1852():
        OP_6D(82590, 0, 6280, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1852)

    def lambda_186A():
        OP_67(0, 6500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_186A)

    def lambda_1882():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1882)
    TurnDirection(0x101, 0x8, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #25
        0x101,
        "\x07\x00#1020F#1PJoshua!\x02",
    )

    CloseMessageWindow()

    def lambda_18BD():

        label("loc_18BD")

        OP_99(0x101, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_18BD")

    QueueWorkItem2(0x101, 1, lambda_18BD)
    Sleep(1500)
    SetChrChipByIndex(0x101, 1)

    def lambda_18DA():

        label("loc_18DA")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_18DA")

    QueueWorkItem2(0x101, 1, lambda_18DA)
    Sleep(1500)
    OP_62(0x101, 0x64, 1900, 0x28, 0x2B, 0xFA, 0x0)

    def lambda_1904():

        label("loc_1904")

        OP_99(0x101, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1904")

    QueueWorkItem2(0x101, 1, lambda_1904)
    Sleep(3000)

    ChrTalk(    #26
        0x101,
        "\x07\x00#1021F#1PWh-Why...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #27
        0x8,
        "\x07\x05#4P#40WIt's... It's okay. It's...enough.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    Sleep(500)
    OP_99(0x8, 0x0, 0x9, 0x5DC)
    OP_22(0x82, 0x0, 0x64)
    OP_99(0x8, 0xA, 0xB, 0x5DC)
    Sleep(500)
    OP_44(0x101, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        "\x07\x00#1020F#1PAaaah!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x8,
        "\x07\x05#4P#40WI was always...just a broken puppet...\x02",
    )

    CloseMessageWindow()

    def lambda_1A1F():
        OP_99(0x8, 0xC, 0x14, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A1F)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #30
        0x8,
        "\x07\x05#4P#40WI can never go back to being human...\x02",
    )

    CloseMessageWindow()

    def lambda_1A77():
        OP_6D(83130, 0, 6760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A77)
    OP_99(0x8, 0x15, 0x18, 0x5DC)

    def lambda_1A98():
        OP_99(0x8, 0x19, 0x25, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A98)
    OP_22(0xB1, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 20)
    SetChrSubChip(0x101, 32)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    SetChrPos(0x9, 82600, -800, 6180, 0)

    ChrTalk(    #31
        0x9,
        "\x07\x05#2P#40WSo...enough... Enough.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #32
        0x101,
        "\x07\x00#1020F#1PNo...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x8000)

    def lambda_1B35():
        OP_9E(0xFE, 0x14, 0x0, 0x9C4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B35)

    def lambda_1B4F():

        label("loc_1B4F")

        OP_99(0xFE, 0x20, 0x27, 0x5DC)
        OP_48()
        Jump("loc_1B4F")

    QueueWorkItem2(0x101, 2, lambda_1B4F)
    OP_8F(0x101, 0x13A2E, 0x0, 0x164E, 0x3E8, 0x0)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 32)
    Sleep(500)

    def lambda_1B84():
        OP_9E(0xFE, 0x14, 0x0, 0x9C4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B84)

    def lambda_1B9E():

        label("loc_1B9E")

        OP_99(0xFE, 0x20, 0x27, 0x5DC)
        OP_48()
        Jump("loc_1B9E")

    QueueWorkItem2(0x101, 2, lambda_1B9E)
    OP_8F(0x101, 0x14064, 0x0, 0x1842, 0x3E8, 0x0)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x0, 0x5, 0x5DC)
    Sleep(1500)
    Fade(500)

    def lambda_1BF0():
        OP_6B(2200, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BF0)
    SetChrSubChip(0x8, 38)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 82020, 0, 6210, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 21)
    Sleep(200)
    SetChrSubChip(0x101, 6)
    SetChrSubChip(0xA, 22)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    SetChrSubChip(0xA, 23)
    Sleep(1000)
    Sleep(500)
    SetChrPos(0x9, 81500, 0, 5500, 0)

    ChrTalk(    #33
        0x9,
        (
            "\x07\x05#2P#60WThank you...\x02\x03",

            "#80WGoodbye, Estelle...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrSubChip(0xA, 24)
    Sleep(1500)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #34
        0x101,
        "\x07\x00#1025F#6PNo... No!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 8)
    SetChrSubChip(0xA, 26)
    Sleep(100)
    SetChrSubChip(0x101, 10)
    SetChrSubChip(0xA, 27)
    Sleep(100)
    SetChrSubChip(0x101, 11)
    Sleep(1000)
    FadeToDark(2000, 0, -1)

    def lambda_1D03():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D03)

    ChrTalk(    #35 op#A op#5
        0x101,
        "\x07\x00#1014F#4S#30A#6PNOOOOOOOOOOOOOO!\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    Sleep(3500)
    OP_0D()
    OP_20(0x3E8)
    OP_21()
    ClearChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x8000)
    OP_44(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 60300, 500, 15000, 270)
    SetChrPos(0xB, 60720, 0, 13200, 0)
    ClearChrFlags(0xB, 0x80)
    OP_6D(60440, 0, 15530, 0)
    OP_67(0, 8510, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(32000, 0)
    OP_6E(288, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_1DF6():
        OP_99(0x101, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DF6)
    WaitChrThread(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 5)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        "#1020F#6PAh...!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0xB,
        (
            "\x07\x00#264F#2PWow, what a scream!\x02\x03",

            "Are you okay, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 7)
    Sleep(500)

    ChrTalk(    #38
        0x101,
        (
            "#1026F#6PRenne...\x02\x03",

            "#1025FOh, good... Just a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        "\x07\x00#260F#2PHeehee! Did you have a scaaary nightmare?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 4)
    Sleep(500)

    ChrTalk(    #40
        0x101,
        (
            "#1007FYeah, a total nightmare.\x02\x03",

            "Now that freaky doll is even showing up\x01",
            "in my dreams, I mean--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x23B, 0x0, 0x3C)

    def lambda_1F9A():
        OP_96(0xFE, 0xE9D4, 0x2BC, 0x3BD8, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F9A)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 180, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 3)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x800)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1020F#6PWAIT A SECOND!\x02\x03",

            "Renne, what are YOU doing here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "\x07\x00#261F#2PHeeheehee! I was wondering when\x01",
            "you were going to act all surprised.\x02\x03",

            "You're so laid back, Estelle! I love that\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1019F#6PYeah, well, forgive me for not being\x01",
            "on the ball right after waking up.\x02\x03",

            "#1004FAnyway, where...?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #44
        0xB,
        (
            "\x07\x00#263F#2PIt's not so odd for me to be here,\x01",
            "you know.\x02\x03",

            "#269FWe're actually at our brand new base.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #45
        0x101,
        "#1002F#6PNew base?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        "\x07\x00#1305F#2PMm-hmm. Look out the window.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1002F#6PUh, okay...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_2236():

        label("loc_2236")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2236")

    QueueWorkItem2(0xB, 2, lambda_2236)
    OP_8F(0x101, 0xE84E, 0x2BC, 0x3642, 0x5DC, 0x0)
    OP_96(0x101, 0xE93E, 0x0, 0x3516, 0xC8, 0xBB8)

    def lambda_2272():
        OP_6D(62950, 0, 12460, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2272)

    def lambda_228A():
        OP_67(0, 4220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_228A)

    def lambda_22A2():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A2)

    def lambda_22B2():
        OP_6C(57000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_22B2)

    def lambda_22C2():
        OP_6E(288, 3000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22C2)
    OP_8E(0x101, 0xE9FC, 0x0, 0x2D78, 0x7D0, 0x0)

    def lambda_22E6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_22E6)
    OP_8E(0x101, 0xF032, 0x0, 0x2C1A, 0x7D0, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #48
        0x101,
        "#6P#1020F#4SWHA?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1730 end

    def Function_14_2368(): pass

    label("Function_14_2368")

    EventBegin(0x0)
    SetChrPos(0x101, 61490, 0, 11290, 90)
    SetChrPos(0xB, 61300, 0, 12390, 90)
    ClearChrFlags(0xB, 0x80)
    OP_6D(62950, 0, 12460, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    OP_6D(63980, 0, 13140, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x101,
        "#1020F#5PAja, ba, ga, ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#263F#5PWelcome aboard the crimson ark,\x01",
            "the Glorious!\x02\x03",

            "This ship could beat up an entire army!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(400)

    ChrTalk(    #51
        0xB,
        "#1306F#5PDon't you think this is the best toy ever?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #52
        0x101,
        (
            "#1020F#2PY-You... You people...\x02\x03",

            "What are you planning on doing with\x01",
            "something like THIS?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    SetMessageWindowPos(320, 60, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #53
        "\x07\x05Ahhh, our guest has finally awoken.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 180, 600)
    Sleep(500)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    SetChrName("Man's Voice")

    AnonymousTalk(    #54
        (
            "\x07\x05Welcome aboard, Estelle. I trust your\x01",
            "nap was restful?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #55
        (
            "\x07\x05I'm sure you're quite out of sorts, being\x01",
            "brought aboard with no fanfare.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #56
        (
            "\x07\x05Fear not. We haven't brought you here to\x01",
            "cause you any harm. Far from it, in fact.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #57
        "\x07\x05You're free to relax here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #58
        0x101,
        "#1002F#5P...\x02",
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #59
        (
            "\x07\x05Why don't we take the chance to have\x01",
            "a nice chat?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #60
        (
            "\x07\x05About the society, about our goals,\x01",
            "and about our common friends.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #61
        "\x07\x05I think I can answer many of your questions.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #62
        0x101,
        (
            "#1022F#5P...Fine.\x02\x03",

            "Not like I have much of a choice.\x01",
            "Let's hear it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #63
        "\x07\x05Excellent! I'll be waiting.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Man's Voice")

    AnonymousTalk(    #64
        (
            "\x07\x05Renne, be a darling and show Estelle\x01",
            "the way up here, would you?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #65
        0xB,
        "#261F#5PSure, okay!\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x5A)
    Sleep(1000)
    OP_8C(0xB, 225, 400)

    def lambda_290F():
        OP_6D(61750, 0, 11850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_290F)
    OP_8E(0xB, 0xE8A8, 0x0, 0x2B34, 0x5DC, 0x0)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #66
        0xB,
        "#260F#5PCome on, Estelle! Let's go to the Sanctuary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1002F#4PSanctuary...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#263F#5PIt's a really pretty room on the top\x01",
            "deck of this ship.\x02\x03",

            "The professor's waiting for us there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1002F#4P...\x02\x03",

            "#1022FAll right. Show me the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        (
            "#1305F#5PAwww, you don't need to be so serious.\x02\x03",

            "I think you'll really like what we have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1015F#4PHuh? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#261F#5PYou'll just have to find out!\x02\x03",

            "#265FAnyway, follow me! C'mon, c'mon!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x2E, 0xFF, 0xFF)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x12F, 7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x12F, 0x1000)
    SetChrFlags(0xB, 0x80)
    OP_6D(59560, 0, 11060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 59560, 0, 11060, 270)
    SetChrPos(0x1, 59560, 0, 11060, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x1C1B)
    OP_3F(0x3FA, 1)
    OP_3F(0x3FB, 1)
    OP_3F(0x3FC, 1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_2368 end

    def Function_15_2BCB(): pass

    label("Function_15_2BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BD8")
    Return()

    label("loc_2BD8")

    EventBegin(0x1)
    TurnDirection(0x101, 0x12F, 400)

    NpcTalk(    #73
        0x101,
        "Renne",
        (
            "#263FOops, silly me. The Sanctuary isn't this way.\x02\x03",

            "#260FWe need to use the elevator on the opposite\x01",
            "side of the hallway.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_2BCB end

    def Function_16_2C82(): pass

    label("Function_16_2C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C8F")
    Return()

    label("loc_2C8F")

    EventBegin(0x1)
    TurnDirection(0x101, 0x12F, 400)

    NpcTalk(    #74
        0x101,
        "Renne",
        "#265FOops, silly me. The Sanctuary isn't this way.\x02",
    )

    CloseMessageWindow()
    OP_6D(-38720, 0, -65209, 2000)

    NpcTalk(    #75
        0x101,
        "Renne",
        "#2PC'mon, the elevator is just over there.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_69(0x101, 0x0)
    OP_0D()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_2C82 end

    def Function_17_2D4B(): pass

    label("Function_17_2D4B")

    EventBegin(0x0)
    SetChrPos(0x101, 73290, 0, -234130, 270)
    SetChrPos(0x12F, 74790, 0, -234130, 270)
    OP_6D(72090, 0, -232990, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1A, 0x10)
    OP_72(0x1A, 0x20)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0xF)
    OP_73(0x1A)

    def lambda_2DE1():
        OP_6D(67800, 0, -233840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DE1)

    def lambda_2DF9():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DF9)
    Sleep(100)

    def lambda_2E19():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_2E19)
    WaitChrThread(0x12F, 0x1)
    OP_6F(0x1A, 15)
    OP_70(0x1A, 0x0)
    TurnDirection(0x101, 0x12F, 400)
    Sleep(500)

    NpcTalk(    #76
        0x101,
        "Renne",
        (
            "#263F#5PAnd heeeere we are!\x01",
            "This is the Sanctuary.\x02\x03",

            "#260FThe professor should be just inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x12F,
        "Estelle",
        "#1015F#4PHey, Renne.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0x101,
        "Renne",
        "#260F#5PWhat is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #79
        0x12F,
        "Estelle",
        (
            "#1002F#4PWere you the one controlling that\x01",
            "Joshua puppet in the base?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x101,
        "Renne",
        (
            "#265F#5PUh huh, that's right!\x02\x03",

            "#261FThe professor asked me to! Neat, huh?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0x12F,
        "Estelle",
        (
            "#1007F#4P*sigh*\x02\x03",

            "#1003FSo you're a victim of the society, too...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x101,
        "Renne",
        "#264F#5PHuh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #83
        0x12F,
        "Estelle",
        (
            "#1007F#4PNever mind.\x02\x03",

            "#1006FWell, here I go.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x101,
        "Renne",
        "#261F#5PSee you later!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(67790, 0, -234130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    RemoveParty(0x2E, 0xFF)
    SetChrPos(0x101, 67790, 0, -234130, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0xB, 70380, 0, -234050, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_69(0x101, 0x0)
    OP_69(0x0, 0x0)
    OP_72(0x1A, 0x10)
    OP_A2(0x1C1C)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_2D4B end

    def Function_18_3106(): pass

    label("Function_18_3106")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 61000, 0, -185610, 0)
    OP_6D(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0xBB8)

    def lambda_3167():
        OP_6D(60980, 500, -184400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3167)

    def lambda_317F():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_317F)

    def lambda_3197():
        OP_6B(3120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3197)

    def lambda_31A7():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31A7)
    WaitChrThread(0x101, 0x0)
    OP_21()
    Sleep(300)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x10E)
    OP_22(0x132, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x79)
    OP_1F(0x46, 0x64)
    OP_73(0x2)

    def lambda_31E5():
        OP_8E(0xFE, 0xEDA8, 0x0, 0xFFFD3EEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31E5)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C5401   ._SN", 125, 0, 0)
    IdleLoop()
    OP_64(0x4, 0x1)
    OP_A2(0x1C89)
    Sleep(500)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_3106 end

    def Function_19_3230(): pass

    label("Function_19_3230")

    TalkBegin(0xB)

    ChrTalk(    #85
        0xB,
        (
            "#1306FJust go down this hallway and you'll\x01",
            "be in the Sanctuary.\x02\x03",

            "Go on, the professor's waiting!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_19_3230 end

    def Function_20_329D(): pass

    label("Function_20_329D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrPos(0xC, 6240, 0, 4990, 270)
    ClearChrFlags(0xC, 0x80)
    OP_6D(6850, 0, 5420, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x101, 55870, 200, 13910, 0)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 9)
    OP_6D(57200, 0, 14960, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #86
        0x101,
        (
            "#1003F#6P(If I join the society, I'll meet Joshua again.)\x02\x03",

            "(That's all but guaranteed.)\x02\x03",

            "#1016F(Besides, I don't have to join them for real,\x01",
            "right?)\x02\x03",

            "(I can just, like, pretend to join them and\x01",
            "learn more about how they operate.)\x02\x03",

            "#1025F(I'm not the best actress in the world, so it\x01",
            "might be hard, but it's better than just being\x01",
            "locked up...)\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)

    def lambda_34E0():
        OP_6D(58030, 0, 14730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34E0)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 56790, 0, 14000, 90)
    OP_0D()
    Sleep(1000)

    def lambda_3514():
        OP_6D(62030, 0, 11840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3514)
    OP_8E(0x101, 0xE272, 0x0, 0x2BD4, 0x7D0, 0x0)
    OP_8E(0x101, 0xF03C, 0x0, 0x2B34, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #87
        0x101,
        (
            "#1010F#6P(No... That's stupid.)\x02\x03",

            "#1002F(That isn't the way I do things.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, 50890, 0, 10990, 90)
    ClearChrFlags(0xE, 0x80)

    NpcTalk(    #88
        0xE,
        "Man's Voice",
        "#2PPardon me.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3617():
        OP_6D(59440, 0, 11670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3617)
    OP_22(0x6D, 0x0, 0x64)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x1)

    def lambda_3640():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3640)

    def lambda_3652():
        OP_8E(0xFE, 0xDDFE, 0x0, 0x2AE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3652)
    Sleep(500)

    def lambda_3672():
        OP_6D(60440, 0, 11670, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3672)
    Sleep(500)

    ChrTalk(    #89
        0x101,
        (
            "#1020FHuh?\x02\x03",

            "#1002FYou...!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xE, 0x1)

    ChrTalk(    #90
        0xE,
        (
            "#123F#5PHeh. No need to be so on guard.\x02\x03",

            "I have no intention of harming you--though if\x01",
            "you try something like that little stunt of yours\x01",
            "earlier, I may have no other choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1022FYeah, well, SOOORRY.\x02\x03",

            "#1019FWhat're you doing here, anyway?\x01",
            "Weren't you guys going out somewhere? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#124F#5PThe professor and the others are the ones\x01",
            "who will be advancing the plan.\x02\x03",

            "I'm staying behind and minding the\x01",
            "Glorious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1002FWhat is it you people are planning\x01",
            "on doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        (
            "#121F#5PIf you wish to find out, why not accept\x01",
            "the professor's invitation?\x02\x03",

            "You'll learn most of our plans if you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xE,
        (
            "#123F#5PHeh.\x02\x03",

            "It seems you have your answer,\x01",
            "but you're still hesitating, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1026FErm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "#124F#5PIf you want my advice, Estelle Bright?\x01",
            "You are not suited for the Society of\x01",
            "Ouroboros. At all.\x02\x03",

            "In both ability and personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1019FMan...\x02\x03",

            "Do you have to be so completely blunt\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xE,
        (
            "#121F#5PDon't misunderstand me. The potential\x01",
            "for the necessary skill is within you...\x01",
            "somewhere.\x02\x03",

            "But your personality...\x02\x03",

            "#124FYou have too little darkness within\x01",
            "you to be part of the Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1026F...'Darkness'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        (
            "#120F#5PAll those in service to the Grandmaster\x01",
            "bear some kind of darkness on their\x01",
            "shoulders.\x02\x03",

            "Myself, the professor, the other Enforcers...\x02\x03",

            "#124FJoshua, too, needless to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #103
        0x101,
        (
            "#1003F...\x02\x03",

            "#1010FHey...\x02\x03",

            "#1002FWhat's your relationship to Joshua,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xE,
        "#121F#5POur relationship...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1002FJoshua was weirdly focused on you.\x02\x03",

            "He seemed to know who you were\x01",
            "even though he didn't recognize you\x01",
            "with that mask on.\x02\x03",

            "And on top of that, it seemed like he\x01",
            "was desperate to find out who you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "#121F#5PThat doesn't surprise me.\x02\x03",

            "#124FThe professor sealed part of his memory\x01",
            "away.\x02\x03",

            "He was hypnotized in such a way that\x01",
            "the moment he left the society, he could\x01",
            "remember little about us.\x02\x03",

            "#120FEven if he remembered his actions as\x01",
            "part of the society, he could not remember\x01",
            "his confederates.\x02\x03",

            "That would have been the core of his dilemma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1020FThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        (
            "#124FThe memories of his childhood would\x01",
            "be the same.\x02\x03",

            "Even if he remembers Karin, he likely would\x01",
            "have only loosely remembered me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1003FI see... So that's why...\x02\x03",

            "#1015FWait. Karin? I've heard that name before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xE,
        "#121F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_3FC1():
        OP_6D(62560, 0, 12000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FC1)

    def lambda_3FD9():

        label("loc_3FD9")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_3FD9")

    QueueWorkItem2(0x101, 2, lambda_3FD9)
    OP_8F(0xE, 0xF078, 0x0, 0x2F1C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #111
        0xE,
        (
            "#129F#6PKarin Astray.\x02\x03",

            "A childhood friend of mine and Joshua's\x01",
            "older sister.\x02\x03",

            "She died ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1020F#3S#4PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xE,
        (
            "#122F#6PThat harmonica you have was originally\x01",
            "Karin's.\x02\x03",

            "Joshua held onto it as a memento...\x02\x03",

            "#125F...and then it was passed on to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1020F#4PJoshua had an older sister?!\x02\x03",

            "#1003F...\x02\x03",

            "Umm. How...?\x02\x03",

            "#1026FHow did Karin...um, pass away?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #115
        0xE,
        (
            "#123F#6PI hope you know what you're really asking.\x02\x03",

            "The answer to that question requires staring\x01",
            "into the abyss in which Joshua and the rest\x01",
            "of us reside...and it will stare back.\x02\x03",

            "Are you prepared for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1003F#4P...\x02\x03",

            "#1010FTell me.\x02\x03",

            "#1025FI don't know if I'm ready for what's\x01",
            "coming or whatever, but...\x02\x03",

            "I want to know what kind of path\x01",
            "Joshua has followed.\x02\x03",

            "If nothing else, I have to know that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xE,
        "#124F#6PAs you wish.\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_8C(0xE, 90, 300)
    WaitChrThread(0x101, 0x1)
    OP_21()
    Sleep(500)
    OP_1D(0x72)
    Sleep(500)

    def lambda_4367():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4367)
    Sleep(1000)

    ChrTalk(    #118
        0xE,
        (
            "#129F#6PIt was a little over ten years ago.\x02\x03",

            "Back when you could still find the village of\x01",
            "Hamel on maps of Erebonia and Liberl.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x10)
    OP_AD(0x240083, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetChrName("")

    AnonymousTalk(    #119
        (
            "\x07\x0CHamel was a tiny little place.\x02\x03",

            "There weren't many other young people, so the three of us\x01",
            "were always together.\x02\x03",

            "I dreamed of becoming a bracer, and I spent my free time\x01",
            "practicing my swordsmanship.\x02\x03",

            "Karin and Joshua would watch and encourage me. That was\x01",
            "how we wiled away the days.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240084, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #120
        (
            "\x07\x0COnce I was done with practice, we would turn our ears to\x01",
            "Karin's harmonica.\x02\x03",

            "Karin could play anything on that harmonica. Anything.\x01",
            "But my favorite was always the old Erebonian folk song,\x01",
            "'The Whereabouts of Light.'\x02\x03",

            "It seemed like that bliss would last forever...\x02\x03",

            "We believed that. We had no reason to doubt it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    Sleep(500)

    AnonymousTalk(    #121
        (
            "\x07\x0CThat day dawned and began just like any other.\x01",
            "And then they came.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240085, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #122
        (
            "\x07\x0CA band of invaders, garbed in black and armed with Liberlian\x01",
            "weaponry, came from nowhere.\x02\x03",

            "They encircled the village and slaughtered everyone in sight.\x02\x03",

            "None were spared. Not the old and infirm, not the young and\x01",
            "defenseless...not even infants.\x02\x03",

            "Those who were killed quickly in the opening moments were\x01",
            "the luckiest by far.\x02\x03",

            "And the women... Even in this telling, there are some things\x01",
            "I will not recount.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240086, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #123
        (
            "\x07\x0CWe fled desperately from that hell. We were lucky to be in a\x01",
            "position to escape when the attack began.\x02\x03",

            "We fled for the outskirts of the village; the screams of our\x01",
            "own families carried to our ears on the wind.\x02\x03",

            "Once we'd gotten to the outskirts, I told Karin and Joshua\x01",
            "I would act as bait to confuse any pursuers.\x02\x03",

            "I promised them I would catch up to them soon and sent them\x01",
            "ahead.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    Sleep(500)

    AnonymousTalk(    #124
        (
            "\x07\x0CBut the attackers... They had laid their plans well.\x02\x03",

            "They had people in position to deal with any who tried to flee.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x2F0, 0x264, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x2EF, 0x263, 0xFFFFFF, 0x0, "C_VIS112._CH")
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0xFF38, 0x0, 0x300, 0x200, 0x0, 0x0, 0x1FF, 0x1FF, 0xFFFFFF, 0x0, "C_VIS138._CH")
    OP_C5(0x2, 0x0, 0x0, 0x2C8, 0x264, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x2C7, 0x263, 0xFFFFFF, 0x1, "C_VIS139._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x0, 0x0, -100000, 0, 3000)
    Sleep(1000)
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x0, 100000, 0, 2000)
    Sleep(3000)
    FadeToDark(3000, 16777215, -1)
    OP_C6(0x1, 0x3, 16777215, 2000, 0)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_0D()
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    AnonymousTalk(    #125
        (
            "\x07\x0CWhen I'd finally caught up to them, the scene was strangely\x01",
            "quiet.\x02\x03",

            "A man, dead, shot through the throat...\x02\x03",

            "...Joshua with a gun in his hand, dumbstruck...\x02\x03",

            "...and Karin, holding Joshua with a horrific wound on her\x01",
            "back.\x02\x03",

            "She was...barely breathing at that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240088, 0x0, 0x0, 0x64)
    Sleep(3000)

    AnonymousTalk(    #126
        (
            "\x07\x0CEven now, the scene seems surreal to me. Karin was calm\x01",
            "and content.\x02\x03",

            "She entrusted her harmonica to Joshua, then asked that I take\x01",
            "care of him.\x02\x03",

            "And then...she died quietly, there in that clearing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C4(0x1, 0x10)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #127
        0x101,
        (
            "#1020F#4P...\x02\x03",

            "Wh... Why...on...?\x02\x03",

            "Why...did that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xE,
        (
            "#129F#6PThe Empire invaded Liberl almost immediately\x01",
            "afterwards.\x02\x03",

            "A defenseless little village, its inhabitants\x01",
            "slaughtered by men with Liberlian arms...\x02\x03",

            "It was almost too perfect an excuse to invade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1026F#4PIt...can't be.\x02\x03",

            "Liberlian troops...doing that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "#128F#6PWhen the local garrison found us, they were\x01",
            "adamant the invaders were Liberlian.\x02\x03",

            "#129FWhen the war ended a few months later with\x01",
            "the Empire's defeat, however, we were given\x01",
            "a different tale entirely.\x02\x03",

            "They told us instead that a band of jaeger\x01",
            "dropouts had turned to pure brigandry.\x02\x03",

            "And they told us to never speak to anyone else\x01",
            "of the attack.\x02\x03",

            "The Erebonian authorities announced that Hamel\x01",
            "had been destroyed in a landslide, and all roads\x01",
            "leading there were to be closed completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1020F#4PH-Hold on! What?!\x02\x03",

            "Why would they lie about that?\x01",
            "Neither explanation makes sense!\x02\x03",

            "That's almost...like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xE,
        (
            "#125F#6PHeh...\x02\x03",

            "#122FIndeed. Everything was a fabrication by the\x01",
            "war hawks in the Empire to justify the invasion\x01",
            "of Liberl.\x02\x03",

            "At the end of the war, the ruse was discovered,\x01",
            "and the Imperial government was thrown into a panic.\x02\x03",

            "They conceded to a comprehensive peace and\x01",
            "executed nearly everyone involved in the plot,\x01",
            "all to pretend that it never happened.\x02\x03",

            "#129FThat, Estelle Bright, is the tragedy of Hamel in\x01",
            "full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1020F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        (
            "#129F#6PThat was also when Joshua's heart was\x01",
            "broken entirely.\x02\x03",

            "He was now burdened with the torturous death\x01",
            "of his sister, his parents, and everyone he knew,\x01",
            "and even the shock of taking another man's life.\x02\x03",

            "How could that not shatter the soul of a\x01",
            "six-year-old child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1003F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "#128F#6PYou've likely heard the rest from Joshua.\x02\x03",

            "His spirit was so wholly broken that he lost\x01",
            "all will to do anything but play that harmonica.\x01",
            "He began to waste away.\x02\x03",

            "That was when the two of us were found\x01",
            "by Weissmann.\x02\x03",

            "To save Joshua's life, I'd entrusted him to\x01",
            "Weissmann's care and threw myself into\x01",
            "Ouroboros training.\x02\x03",

            "#129FAnd then, two years later...\x02\x03",

            "Joshua, 'repaired' as he was by Weissmann,\x01",
            "followed the same path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1027F#4P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 180, 400)
    Sleep(500)

    ChrTalk(    #138
        0xE,
        (
            "#123F#6PThis is darkness, Estelle Bright.\x02\x03",

            "Do you understand what sort of gulf\x01",
            "separates you and Joshua now?\x02\x03",

            "Do you understand what he stares into\x01",
            "every day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1003F#4P...\x02\x03",

            "#1010FI do, yeah.\x02\x03",

            "Now I think I really understand why\x01",
            "Joshua left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xE,
        "#126F#6PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1006F#4PHey, next time you see him, tell Weissmann\x01",
            "thanks, but no thanks.\x02\x03",

            "I'll never join Ouroboros.\x02\x03",

            "It's not because I like or dislike the society...\x02\x03",

            "But as long as I'm going to pull Joshua back\x01",
            "over that gulf you mentioned? Forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xE,
        "#120F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1015F#4PAlthough I do feel kinda bad about letting\x01",
            "Renne down after she went through all\x01",
            "this trouble to invite me...\x02\x03",

            "#1016FHey, you think she'll forgive me if I say I'm\x01",
            "sorry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xE,
        (
            "#124F#6PHeh... Hahaha.\x01",
            "You're one of a kind, Estelle Bright.\x02\x03",

            "#123FTo hear those horrors and thus lose\x01",
            "your hesitation?\x02\x03",

            "You truly are more than just the\x01",
            "daughter of the Divine Blade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1016F#4PUh, thanks for the compliment, I guess.\x02\x03",

            "#1006FAnd you say all that, but you care about\x01",
            "Joshua too, right? You guys were friends.\x02\x03",

            "Or maybe more like brothers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xE,
        "#121F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    Sleep(500)

    ChrTalk(    #147
        0xE,
        (
            "#125F#6PLet me be absolutely clear: that was\x01",
            "ten years ago.\x02\x03",

            "To me now, he is nothing more than\x01",
            "a rogue element to be eliminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1020F#4PWh--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "#128F#6PThe professor seems to enjoy letting\x01",
            "Joshua do as he pleases.\x02\x03",

            "I have a different plan in mind.\x02\x03",

            "#129FSooner or later, I will deal with Joshua\x01",
            "personally.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #150
        0x101,
        (
            "#1005F#4PWAIT A SECOND! What the hell is THIS?!\x02\x03",

            "Karin asked you to take care of him!\x01",
            "Doesn't that mean anything to you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "#129F#6PI have my own path I've chosen for myself.\x02\x03",

            "I've dedicated myself to my goal, and any\x01",
            "who stand in my way shall die by my blade.\x02\x03",

            "#128FNot even Karin's final request will stop me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1026F#4PHow can you...?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x15)
    Sleep(4000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)
    Sleep(1000)

    ChrTalk(    #153
        0x101,
        "#1020FAah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_329D end

    def Function_21_5E44(): pass

    label("Function_21_5E44")

    OP_22(0x133, 0x0, 0x2D)
    Sleep(4000)
    OP_22(0x133, 0x0, 0x2D)
    Sleep(4000)
    Return()

    # Function_21_5E44 end

    def Function_22_5E59(): pass

    label("Function_22_5E59")

    EventBegin(0x0)
    SetChrPos(0x101, 61500, 0, 11060, 90)
    SetChrPos(0xE, 61560, 0, 12060, 90)
    ClearChrFlags(0xE, 0x80)
    OP_6D(62560, 0, 12000, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #154
        0x101,
        "#1020F#6PThose're--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        (
            "#125F#6PThe professor and the others, yes.\x02\x03",

            "It looks like the third stage of the plan\x01",
            "is getting under way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #156
        0x101,
        "#1002F#4PThe third stage? What's...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #157
        0xE,
        (
            "#123F#6PHeh. That is not for you to know.\x02\x03",

            "#124FOnce we're finished, you'll be returned\x01",
            "to your father.\x02\x03",

            "Behave until then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)
    Sleep(500)

    def lambda_602D():
        OP_6D(60160, 0, 11740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_602D)

    def lambda_6045():
        OP_8F(0xFE, 0xDA52, 0x0, 0x2B16, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6045)
    Sleep(200)
    OP_8C(0x101, 270, 400)
    Sleep(1000)

    ChrTalk(    #158
        0x101,
        "#1005F#4PNOW JUST A--\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #159
        0xE,
        (
            "#122F#5PAs one final note, don't even think of\x01",
            "attempting to escape.\x02\x03",

            "#125FThe Glorious is eight thousand arge above\x01",
            "ground. You have nowhere to run.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6136():
        OP_6D(57590, 0, 11310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6136)
    OP_8E(0xE, 0xC6AC, 0x0, 0x2B16, 0x7D0, 0x0)

    def lambda_6162():
        OP_8E(0xFE, 0xC15C, 0x0, 0x2AC6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6162)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0x101, 0x1)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    OP_6D(62560, 0, 12000, 2000)
    Sleep(500)

    ChrTalk(    #160
        0x101,
        (
            "#1002F#6P...\x02\x03",

            "#1007F'Don't even think of attempting to escape,'\x01",
            "he says.\x02\x03",

            "As if he doesn't know that it's human\x01",
            "nature for me to want to do the EXACT\x01",
            "opposite.\x02\x03",

            "#1006FBesides, he's the only Enforcer on board.\x02\x03",

            "All right, why not? Let's do this.\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()

    def lambda_62B2():
        OP_6D(58740, 0, 11420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62B2)
    OP_8E(0x101, 0xD066, 0x0, 0x2A76, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(1000)
    OP_8C(0x101, 45, 400)
    OP_8E(0x101, 0xDF02, 0x0, 0x31F6, 0xBB8, 0x0)
    OP_8E(0x101, 0xDFF2, 0x0, 0x3778, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8E(0x101, 0xDF84, 0x0, 0x297C, 0xBB8, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    def lambda_639D():
        OP_6D(62560, 0, 12000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_639D)
    OP_8E(0x101, 0xF03C, 0x0, 0x2A9E, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_DC()

    ChrTalk(    #161
        0x101,
        (
            "#1002F#6P...\x02\x03",

            "Oooookay, the timing is gonna be\x01",
            "everything. If I can figure that out,\x01",
            "I'll be good.\x02\x03",

            "#1015FLet's see... I'll wait a couple hours until\x01",
            "they let their guard down, and then...\x02\x03",

            "#1006FRight! It's worth a shot!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)

    def lambda_64C8():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64C8)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 4)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #162
        0x101,
        (
            "#1007F#6PSo this was a memento of Karin, huh?\x02\x03",

            "#1027F#6PYou shouldn't throw away something\x01",
            "like this so easily, you idiot...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_22_5E59 end

    def Function_23_6596(): pass

    label("Function_23_6596")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0xD, 6240, 0, 4990, 270)
    SetChrPos(0xC, 4270, 0, 26120, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xD, 32)
    SetChrChipByIndex(0xC, 32)
    OP_6D(4660, 0, 23820, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(44000, 0)
    OP_6E(265, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x8, 0x10)
    OP_72(0x8, 0x20)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0x8, 0)
    OP_70(0x8, 0xF)
    OP_73(0x8)
    Sleep(1000)
    SetChrChipByIndex(0xC, 32)

    def lambda_664A():
        OP_8E(0xFE, 0xF78, 0x0, 0x1694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_664A)

    def lambda_6665():
        OP_6D(5620, 0, 5560, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6665)

    def lambda_667D():
        OP_6C(66000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_667D)
    Sleep(2000)
    OP_6F(0x8, 15)
    OP_70(0x8, 0x0)
    OP_71(0x8, 0x10)
    WaitChrThread(0x0, 0x1)
    SetChrChipByIndex(0xC, 32)
    SetChrSubChip(0xC, 0)
    Sleep(100)
    OP_8C(0xC, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    NpcTalk(    #163
        0xC,
        "Enhanced Jaeger",
        "#6PHey, time to change shifts.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #164
        0xC,
        "Enhanced Jaeger",
        "#6PHow's the girl acting?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #165
        0xD,
        "Enhanced Jaeger",
        "#7PHa! Quiet as a mouse.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #166
        0xD,
        "Enhanced Jaeger",
        (
            "#7PShe might be a bracer, but she's\x01",
            "still just a kid.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0xD,
        "Enhanced Jaeger",
        (
            "#7PProbably curled up in bed, scared\x01",
            "out of her mind.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #168
        0xC,
        "Enhanced Jaeger",
        (
            "#6PTch. Babysittin' while everyone else\x01",
            "is out sucks.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #169
        0xC,
        "Enhanced Jaeger",
        (
            "#6PThis is so boring. I wanted to get out\x01",
            "there into the action!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #170
        0xD,
        "Enhanced Jaeger",
        (
            "#7PQuit your whining. These're Leonhardt's\x01",
            "orders, and hell if I'm not gonna follow\x01",
            "HIS instructions to the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x3E8)
    OP_22(0xD6, 0x1, 0x46)
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(    #171
        0xD,
        "Enhanced Jaeger",
        "#7PEh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0xC,
        "Enhanced Jaeger",
        "#6PWhat was that sound?\x02",
    )

    CloseMessageWindow()

    def lambda_69A2():
        OP_6D(7090, 0, 5430, 1000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_69A2)
    OP_8C(0xD, 90, 400)
    Sleep(500)
    OP_22(0x72, 0x0, 0x64)
    Sleep(1500)

    NpcTalk(    #173
        0xD,
        "Enhanced Jaeger",
        "#6PHey! What're you doing?!\x02",
    )

    CloseMessageWindow()
    OP_23(0xD6)
    OP_22(0x134, 0x0, 0x64)
    Sleep(1000)
    OP_1F(0x64, 0x3E8)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #174
        0xC,
        "Enhanced Jaeger",
        "#6PYou don't think...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #175
        0xD,
        "Enhanced Jaeger",
        "#6PShe escaped?!\x02",
    )

    CloseMessageWindow()
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_72(0xA, 0x10)
    OP_72(0xA, 0x20)
    OP_22(0x6D, 0x0, 0x64)
    OP_6F(0xA, 0)
    OP_70(0xA, 0xF)
    OP_73(0xA)
    SetChrChipByIndex(0xD, 11)

    def lambda_6ACC():
        OP_8E(0xFE, 0x2134, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6ACC)
    Sleep(100)
    SetChrChipByIndex(0xC, 11)

    def lambda_6AF1():
        OP_8E(0xFE, 0x2134, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AF1)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    Fade(1000)
    OP_6D(52360, 0, 12450, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(56000, 0)
    OP_6E(281, 0)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_71(0xA, 0x10)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_22(0x1C3, 0x0, 0x64)
    OP_0D()

    def lambda_6B8E():
        OP_6D(58180, 0, 12600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B8E)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x1E)
    WaitChrThread(0xC, 0x1)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    NpcTalk(    #176
        0xC,
        "Enhanced Jaeger",
        "#6PDamn it...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #177
        0xD,
        "Enhanced Jaeger",
        (
            "#5PThat stupid girl! Does she not get where\x01",
            "she is?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #178
        0xD,
        "Enhanced Jaeger",
        "#5PIs she trying to kill herself or something?!\x02",
    )

    CloseMessageWindow()

    def lambda_6CAD():
        OP_6D(61920, 0, 11630, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CAD)
    SetChrChipByIndex(0xD, 11)

    def lambda_6CCA():
        OP_8E(0xFE, 0xF032, 0x0, 0x28F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6CCA)
    Sleep(300)
    SetChrChipByIndex(0xC, 11)

    def lambda_6CEF():
        OP_8E(0xFE, 0xEC4A, 0x0, 0x2CE2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6CEF)
    WaitChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 8)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 8)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    NpcTalk(    #179
        0xD,
        "Enhanced Jaeger",
        "#6P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #180
        0xD,
        "Enhanced Jaeger",
        (
            "#6PAww, Gehenna take me, right now.\x01",
            "She probably fell.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #181
        0xC,
        "Enhanced Jaeger",
        "#6PYou have got to be kidding me...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #182
        0xC,
        "Enhanced Jaeger",
        (
            "#6PWhat are we gonna tell Leonhardt\x01",
            "that'll let us keep our heads?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #183
        0xC,
        "Enhanced Jaeger",
        (
            "#6PThat damn brat... Nothing but a load\x01",
            "of trouble!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x3E8)
    OP_21()
    SetChrPos(0x101, 63690, 2000, 11810, 270)

    ChrTalk(    #184
        0x101,
        "#6PDamn brat, huh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x71)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 63500, 500, 11810, 270)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x1000)
    OP_99(0x101, 0x0, 0x2, 0x9C4)
    SetChrFlags(0x101, 0x800)

    def lambda_6F33():
        OP_99(0xFE, 0x3, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F33)
    OP_8F(0x101, 0xF1D6, 0xFFFFFF38, 0x2E22, 0x2EE0, 0x0)
    PlayEffect(0x1, 0x0, 0xC, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_43(0xC, 0x0, 0x0, 0x1C)

    NpcTalk(    #185 op#A op#5
        0xC,
        "Enhanced Jaeger",
        "#15A#5PGwah!\x05\x02",
    )


    def lambda_6FCB():
        OP_6D(59720, 0, 11940, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FCB)
    WaitChrThread(0x101, 0x2)

    def lambda_6FE8():

        label("loc_6FE8")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_6FE8")

    QueueWorkItem2(0x101, 3, lambda_6FE8)

    def lambda_6FF9():
        OP_96(0xFE, 0xEE02, 0x0, 0x2E7C, 0x9C4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FF9)
    Sleep(100)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    def lambda_7030():

        label("loc_7030")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_7030")

    QueueWorkItem2(0xD, 3, lambda_7030)

    def lambda_7041():
        OP_96(0xFE, 0xE7FE, 0x0, 0x1E96, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7041)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 14)

    def lambda_7073():
        OP_99(0xFE, 0x5, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7073)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x800)
    WaitChrThread(0xD, 0x2)
    Sleep(500)
    WaitChrThread(0xC, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_70AA():
        OP_6D(59670, 0, 10950, 1000)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_70AA)

    def lambda_70C2():
        OP_6E(298, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70C2)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    LoadEffect(0x2, "map\\\\mp003_00.eff")
    LoadEffect(0x3, "monster\\\\msc0310.eff")
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0xC, 0x1)
    OP_44(0x101, 0x3)

    NpcTalk(    #186
        0xD,
        "Enhanced Jaeger",
        "#4PYou!\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    TurnDirection(0x101, 0xD, 500)
    Sleep(500)

    ChrTalk(    #187
        0x101,
        "#1005F#6PNice try, old man!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xD, 0x0, 0x0, 0x18)
    OP_43(0xD, 0x1, 0x0, 0x19)

    def lambda_7192():
        OP_6D(58930, 0, 12880, 600)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7192)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_71B4():
        OP_96(0xFE, 0xE8A8, 0x1F4, 0x3B4C, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_71B4)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    def lambda_71E1():
        OP_6D(55620, 0, 9400, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_71E1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_71FE():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71FE)

    def lambda_720C():
        OP_96(0xFE, 0xDAF2, 0xC8, 0x36BA, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_720C)
    Sleep(50)
    OP_43(0xD, 0x0, 0x0, 0x1A)
    OP_43(0xD, 0x1, 0x0, 0x1B)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_7251():
        OP_8C(0xFE, 225, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7251)

    def lambda_725F():
        OP_96(0xFE, 0xD0CA, 0x0, 0x285A, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_725F)
    WaitChrThread(0x101, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0xD, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 17)

    def lambda_7295():
        OP_6D(59460, 0, 8740, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7295)
    OP_97(0x101, 0xD7DC, 0x24CC, 0xFFFE7960, 0x2EE0, 0x1)

    def lambda_72C2():
        OP_8C(0xFE, 90, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72C2)

    def lambda_72D0():
        OP_96(0xFE, 0xE1A0, 0x0, 0x1EA0, 0xC8, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72D0)
    Sleep(100)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_7302():
        OP_99(0x101, 0x1, 0xC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7302)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    Sleep(400)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0xD, 0, 700, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_736A():
        OP_6D(61000, 0, 8620, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_736A)

    def lambda_7382():
        OP_6B(2810, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7382)
    OP_44(0xD, 0x3)
    OP_8C(0xD, 270, 0)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x1000)

    def lambda_73B6():
        OP_8F(0xFE, 0xF03C, 0x5DC, 0x1F0E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_73B6)
    SetChrChipByIndex(0xD, 13)
    SetChrSubChip(0xD, 7)
    WaitChrThread(0xD, 0x1)
    OP_7C(0x64, 0x32, 0x1388, 0x3E8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    def lambda_73FF():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_73FF)
    Sleep(100)

    def lambda_741F():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_741F)
    Sleep(100)

    def lambda_743F():
        OP_8F(0xD, 0xF03C, 0x0, 0x1F0E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_743F)
    WaitChrThread(0xD, 0x1)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 15)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x0, 0x2, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #188
        0xD,
        "Enhanced Jaeger",
        "#5PGwah... *cough*\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    OP_8E(0x101, 0xE92A, 0x0, 0x1F67, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #189
        0x101,
        (
            "#1028F#6PHmph! Never underestimate a bracer!\x02\x03",

            "First of all, don't you think that was a\x01",
            "little rude? Calling a sweet maiden like\x01",
            "myself a 'damn brat.'\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #190
        0xD,
        "Enhanced Jaeger",
        "#5PI-It wasn't me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #191
        0xD,
        "Enhanced Jaeger",
        "#5PI didn't call you that, I swear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1004F#6POh, you didn't?\x02\x03",

            "#1006FWeeell, you didn't correct your buddy,\x01",
            "then. Either way, it's nap time for you.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 19)
    OP_0D()
    Sleep(300)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)

    def lambda_7689():
        OP_99(0x101, 0x0, 0xC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7689)
    Sleep(500)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0x32, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0xD, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_76E9():
        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_76E9)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)

    NpcTalk(    #193 op#5
        0xD,
        "Enhanced Jaeger",
        "#5PNnngh...\x05\x02",
    )

    Sleep(1500)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0xD, 60700, 0, 7800, 270)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 15)
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    Sleep(1500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #194
        0x101,
        "#1007F#6POkay...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #195
        0x101,
        (
            "#1006F#6PReinforcements are probably gonna get\x01",
            "here really quick, so I should book it.\x02\x03",

            "There's gotta be SOME way off this boat.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #196
        0x101,
        (
            "#1027F#6P(And I won't give up...)\x02\x03",

            "(Not until I see Joshua...\x01",
            "Not until I see that dummy again...)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #197
        0x101,
        (
            "#1005F#6P#3S(You won't stop for anything, Loewe?\x01",
            "Well, neither will I!)\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x1000)
    OP_6D(59690, 0, 8039, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x1C1D)
    OP_28(0x99, 0x4, 0x2)
    OP_28(0x99, 0x4, 0x8)
    OP_28(0x99, 0x1, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_23_6596 end

    def Function_24_79B8(): pass

    label("Function_24_79B8")

    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x1, 0x2)
    Return()

    # Function_24_79B8 end

    def Function_25_7A30(): pass

    label("Function_25_7A30")

    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60520, 0, 10840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60910, 0, 12450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 60540, 500, 14400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 61770, 800, 15340, 90, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_25_7A30 end

    def Function_26_7B32(): pass

    label("Function_26_7B32")

    Sleep(100)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x1, 0xD, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x1, 0x2)
    Return()

    # Function_26_7B32 end

    def Function_27_7BE9(): pass

    label("Function_27_7BE9")

    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 59540, 500, 15040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 57490, 1000, 16020, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 56080, 800, 15120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 55920, 200, 13920, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 53370, 0, 12980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 53800, 0, 10980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 52880, 0, 8770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 52810, 0, 8230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_27_7BE9 end

    def Function_28_7DE7(): pass

    label("Function_28_7DE7")

    SetChrChipByIndex(0xC, 13)
    SetChrSubChip(0xC, 0)

    def lambda_7DF7():
        OP_96(0xFE, 0xE010, 0x0, 0x2E40, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7DF7)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 11)
    OP_96(0xC, 0xD96C, 0x0, 0x2F30, 0x3E8, 0x1F40)
    OP_96(0xC, 0xD39A, 0x0, 0x2F26, 0x12C, 0x1770)
    Return()

    # Function_28_7DE7 end

    def Function_29_7E57(): pass

    label("Function_29_7E57")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 49790, 0, 10830, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7E7E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7E7E)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xD5E8, 0x0, 0x27BA, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_29_7E57 end

    def Function_30_7EA9(): pass

    label("Function_30_7EA9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 49790, 0, 10830, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7ED0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7ED0)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xD5E8, 0x0, 0x2E22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_30_7EA9 end

    def Function_31_7EFB(): pass

    label("Function_31_7EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F08")
    Return()

    label("loc_7F08")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F2D")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_7F2D")

    Fade(1000)
    OP_4A(0xF, 0)
    OP_4A(0x10, 0)
    OP_4A(0x11, 0)
    OP_4A(0x14, 0)
    OP_4A(0x15, 0)
    OP_4A(0x12, 0)
    OP_4A(0x13, 0)
    OP_4A(0x16, 0)
    SetChrPos(0x15, -81520, 0, -331440, 225)
    OP_6D(-87930, 0, -344320, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(57000, 0)
    OP_6E(343, 0)
    SetChrPos(0x10B, -88230, 0, -342500, 0)
    SetChrPos(0x102, -87830, 0, -343500, 0)
    SetChrPos(0x101, -89410, 0, -343500, 0)
    SetChrPos(0xF9, -88810, 0, -344500, 0)
    Sleep(500)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10B, 0x1, 0x0, 0x20)

    def lambda_8012():
        OP_6D(-82340, 0, -335690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8012)

    def lambda_802A():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_802A)

    def lambda_8042():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8042)

    def lambda_8052():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_8052)

    def lambda_8062():
        OP_6E(343, 2000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_8062)
    OP_43(0x101, 0x1, 0x0, 0x22)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x21)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    WaitChrThread(0x10B, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #198
        0x10B,
        "#415F#4S#5PGuys!\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_817D():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_817D)
    Sleep(50)

    def lambda_8190():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8190)
    Sleep(50)

    def lambda_81A3():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_81A3)
    Sleep(50)

    def lambda_81B6():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_81B6)
    Sleep(50)

    def lambda_81C9():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_81C9)
    Sleep(50)

    def lambda_81DC():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_81DC)
    Sleep(50)

    def lambda_81EF():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_81EF)
    Sleep(50)

    def lambda_8202():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8202)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #199
        0x10,
        "#201F#6PWhat in...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xF,
        "#192F#6PJosette! And...!\x02",
    )

    CloseMessageWindow()

    def lambda_824D():
        OP_67(0, 5660, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_824D)

    def lambda_8265():
        OP_6D(-84260, 0, -335810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8265)

    def lambda_827D():
        OP_8E(0xFE, 0xFFFEB60A, 0x0, 0xFFFADE2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_827D)
    Sleep(500)

    def lambda_829D():
        OP_8E(0xFE, 0xFFFEB790, 0x0, 0xFFFAE318, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_829D)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #201
        0x11,
        "#6PMiss Josette!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x12,
        "How did you get IN here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x10B,
        (
            "#415F#6POh, thank Aidios...\x01",
            "Thank Aidios, everyone's safe...\x02\x03",

            "Okay, just, just stay still! We're here\x01",
            "to rescue you! We'll get you out!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xF, 0x0)

    ChrTalk(    #204
        0x10,
        (
            "#203F#6PRESCUE us?\x02\x03",

            "#201FAstray, what in the hell is this?!\x02\x03",

            "And what are you even DOING here?!\x01",
            "How'd you get up to this city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#1042F#5PWell, briefly...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #206
        (
            "\x07\x05Joshua quickly explained what happened at the towers and\x01",
            "afterwards.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #207
        0xF,
        (
            "#490F#6PAh, I get it. You came here chasin'\x01",
            "the society again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x10,
        (
            "#204F#7POf all the... Hey, Josette?\x02\x03",

            "#206FYou realize we put ourselves on the\x01",
            "line so you could get away, right?\x02\x03",

            "So why are you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10B,
        (
            "#214F#6PAre you COMPLETELY dense?!\x02\x03",

            "Maybe I was 'safe,' but I was all alone!\x01",
            "I thought you all were...\x02\x03",

            "I THOUGHT it would've been better\x01",
            "if we all met Aidios together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x10,
        (
            "#201F#7PYeah, but what if I don't WANT my little\x01",
            "sister to meet the Goddess just yet?!\x02\x03",

            "Worry about yourself for ONCE\x01",
            "in your life, damn it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x10B,
        (
            "#216F#6PBut I AM worrying about myself!\x02\x03",

            "#215FWhy do you think you have nothing\x01",
            "to do with ME? What do you think\x01",
            "would happen to me if you...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8782")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_87C0")

    label("loc_8782")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A9")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_87C0")

    label("loc_87A9")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_87C0")

    Sleep(1000)

    ChrTalk(    #212
        0x101,
        (
            "#1016F#5P(Haha... Wow, I never realized\x01",
            "how close they are.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8848")

    ChrTalk(    #213
        0x107,
        "#067F#5P(Heehee. Yeah! I'm kinda jealous!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_8848")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8897")

    ChrTalk(    #214
        0x105,
        (
            "#1168F#5P(Haha. Makes you a little jealous,\x01",
            "doesn't it?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_8897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88EB")

    ChrTalk(    #215
        0x109,
        (
            "#1061F#5P(Heh, sort of a heartwarming\x01",
            "sibling fight, y'know?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_88EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8950")

    ChrTalk(    #216
        0x103,
        (
            "#027F#5P(Aww. They're the image of loving\x01",
            "siblings, locking horns constantly.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_8950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8993")

    ChrTalk(    #217
        0x104,
        "#031F#5P(Ahhh... It pulls the heartstrings.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_8993")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89C0")

    ChrTalk(    #218
        0x106,
        "#556F#5P(Heh... Yeah.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A0B")

    label("loc_89C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A0B")

    ChrTalk(    #219
        0x108,
        (
            "#071F#5P(Haha! They're so close,\x01",
            "despite the exterior.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0B")


    ChrTalk(    #220
        0xF,
        (
            "#192F#6PCome on, you two. This might be the single\x01",
            "worst place to have a fight right now.\x02\x03",

            "#199FStill acting like kids after\x01",
            "all this time, I swear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x10B,
        "#215F#6PDon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10,
        "#207F#7PBut--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xF,
        (
            "#198F#6PLook, Kyle, she's here and we can't change that.\x01",
            "Let's make the most of it and try to escape.\x02\x03",

            "#199FSo, lad, you have an idea on that front,\x01",
            "I hope.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B74():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B74)
    Sleep(50)

    def lambda_8B87():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_8B87)
    Sleep(500)

    ChrTalk(    #224
        0x102,
        (
            "#1035F#2PSort of...\x02\x03",

            "#1042FThe main issue is this energy barrier.\x01",
            "Its controls are, as near as I can tell,\x01",
            "completely locked.\x02\x03",

            "There's no way we'll have time to work\x01",
            "our way around the security program.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10,
        "#204F#6PI thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x10B,
        "#216F#6PBut, but...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#1015F#5PHmmm. Is there any way to force it?\x02\x03",

            "Like maybe use a bomb to blow off the\x01",
            "energy...border...thingies or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #228
        0x102,
        (
            "#1043F#2PNo, the barrier itself would be unaffected\x01",
            "by conventional explosives.\x02\x03",

            "And anything powerful enough to damage the\x01",
            "bulkhead would put the prisoners in danger.\x02\x03",

            "#1042FThe only option I can see at this point\x01",
            "is to find an up-to-date security card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1004F#5PA what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10B,
        (
            "#415F#6PWe can use that to get rid\x01",
            "of the barrier, right?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E86():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E86)
    Sleep(100)

    def lambda_8E99():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8E99)

    def lambda_8EA7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_8EA7)
    OP_6D(-84260, 0, -340520, 2000)

    ChrTalk(    #231
        0x102,
        (
            "#1040F#6PYes, it's a small card we put in the terminal\x01",
            "here. If we can find one, we should be able\x01",
            "to deactivate the barrier.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F49():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F49)
    Sleep(100)

    def lambda_8F5C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8F5C)
    OP_6D(-84260, 0, -335810, 1500)

    ChrTalk(    #232
        0x102,
        (
            "#1042F#2PThey've all but certainly changed the cards since\x01",
            "the last security breach, so the one I took\x01",
            "before is no good. We'll need a new one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x10B,
        "#212F#6POkay, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        "#1015F#5PAny idea where they'd keep these cards?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#1035F#2PSecond floor, in the forecastle.\x02\x03",

            "#1042FThe security dispensary is in the same\x01",
            "area where you were being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#1002F#5PI get it, the really high security block.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9151")

    ChrTalk(    #237
        0x107,
        "#062F#5PThat means we should hurry, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_9151")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_919F")

    ChrTalk(    #238
        0x105,
        (
            "#1162F#5PWe should move swiftly so we\x01",
            "are not detected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_919F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91F4")

    ChrTalk(    #239
        0x109,
        (
            "#1060F#5PWhat say we get a move on,\x01",
            "then, before they find us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_91F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9254")

    ChrTalk(    #240
        0x103,
        (
            "#027F#5PI think we should move quickly\x01",
            "before the hornets swarm us, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_9254")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_929F")

    ChrTalk(    #241
        0x104,
        (
            "#035F#5PWe should be swift, then.\x01",
            "Time is our enemy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_929F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92E4")

    ChrTalk(    #242
        0x106,
        "#051F#5PWe should get over there pronto, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_92E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9332")

    ChrTalk(    #243
        0x108,
        (
            "#070F#5PLet us make haste, then, before\x01",
            "we are discovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9332")


    def lambda_9338():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_9338)
    Sleep(50)

    def lambda_934B():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_934B)
    Sleep(50)

    def lambda_935E():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_935E)
    Sleep(50)

    def lambda_9371():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9371)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #244
        0x10B,
        (
            "#214F#6PKyle, Don, guys!\x02\x03",

            "We'll go find a card thing! Just hold on!\x02\x03",

            "We'll be right back once we get it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x10,
        (
            "#203F#7P*sigh* Fine. It's not like you'd listen\x01",
            "if I said no, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xF,
        (
            "#198F#6PLad...and the rest of you.\x02\x03",

            "#490FMake sure our little sister doesn't\x01",
            "fly too far off the handle, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        "#1040F#5PYou can count on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1006F#5PDon't worry, I've got a tight\x01",
            "grip on her leash.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)
    Sleep(300)

    ChrTalk(    #249
        0x10B,
        (
            "#210F#2POn my...? Pfft.\x02\x03",

            "Big words from someone who's waaaay\x01",
            "more reckless than I'll EVER be.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #250
        0x101,
        (
            "#1019F#5PI CAN tie an actual leash around you,\x01",
            "y'know.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(    #251
        0x102,
        (
            "#1052F#2PPlease, truce, remember?\x02\x03",

            "#1042FCome on, we need to return to the entrance.\x02\x03",

            "We'll need to use the elevator on the opposite\x01",
            "side to reach the second floor of the forecastle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)

    ChrTalk(    #252
        0x10B,
        "#212F#5PO-Okay!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #253
        0x101,
        "#1006F#5PCome on!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-87640, 0, -336030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87640, 0, -336030, 180)
    SetChrPos(0x1, -87640, 0, -336030, 180)
    SetChrPos(0x2, -87640, 0, -336030, 180)
    SetChrPos(0x3, -87640, 0, -336030, 180)
    SetChrPos(0xF, -84180, 0, -335080, 270)
    OP_8C(0xF, 270, 0)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    OP_4B(0x16, 255)
    OP_0D()
    OP_A2(0x2223)
    OP_28(0x9E, 0x1, 0x20)
    OP_28(0x9E, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_31_7EFB end

    def Function_32_97B9(): pass

    label("Function_32_97B9")

    OP_8E(0xFE, 0xFFFEB146, 0x0, 0xFFFADD14, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_32_97B9 end

    def Function_33_97D5(): pass

    label("Function_33_97D5")

    OP_8E(0xFE, 0xFFFEAFC0, 0x0, 0xFFFAD8AA, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_33_97D5 end

    def Function_34_97F1(): pass

    label("Function_34_97F1")

    OP_8E(0xFE, 0xFFFEACD2, 0x0, 0xFFFADDDC, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_34_97F1 end

    def Function_35_980D(): pass

    label("Function_35_980D")

    OP_8E(0xFE, 0xFFFEA926, 0x0, 0xFFFAD828, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_35_980D end

    def Function_36_9829(): pass

    label("Function_36_9829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_END)), "loc_9837")
    Call(0, 45)
    Jump("loc_989F")

    label("loc_9837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9851")
    Call(0, 45)
    Jump("loc_989F")

    label("loc_9851")


    AnonymousTalk(    #254
        (
            "\x07\x05The terminal is locked.\x01",
            "Seems like a security card is needed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_989F")

    TalkEnd(0xFF)
    Return()

    # Function_36_9829 end

    def Function_37_98A3(): pass

    label("Function_37_98A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D15")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98D0")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_98D0")

    Fade(1000)
    OP_6D(-127570, 0, -60040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -127670, 0, -58950, 90)
    SetChrPos(0x101, -126930, 0, -59970, 0)
    SetChrPos(0x10B, -128550, 0, -59930, 45)
    SetChrPos(0xF9, -127840, 0, -61020, 0)
    OP_0D()
    OP_6F(0x25, 0)
    OP_70(0x25, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x25)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #255
        "\x07\x00Received #1040i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x410, 1)
    OP_EA(0x2, 0xE, 0x2, 0x0)

    ChrTalk(    #256
        0x10B,
        "#213F#6PHey, that must be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#1004F#4PSo that's the security card you\x01",
            "were talking about? Huh, neat.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #258
        0x102,
        (
            "#1040F#6PYes, no doubt.\x02\x03",

            "If we insert this into the terminal next\x01",
            "to the cell, the computer will think we're\x01",
            "a guard and we can lower the barrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        "#1018F#4PAwesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10B,
        "#415F#6PThank you, Goddess! We can, we can...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B5D")

    ChrTalk(    #261
        0x107,
        "#067FHee, yeah! Let's hurry back to the cell!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BA2")

    ChrTalk(    #262
        0x105,
        "#1168FHaha, yes. Let's hurry back to the cell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BE7")

    ChrTalk(    #263
        0x109,
        (
            "#1061FWe can, indeeeed!\x01",
            "Let's get back to 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2E")

    ChrTalk(    #264
        0x103,
        (
            "#021FYes, we can.\x01",
            "Let's head back to the Capuas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C86")

    ChrTalk(    #265
        0x104,
        (
            "#031FHeh, we certainly can.\x01",
            "Let us return to our wayward bandits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CCF")

    ChrTalk(    #266
        0x106,
        "#051FAll right, then. Let's go free your brothers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D07")

    label("loc_9CCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D07")

    ChrTalk(    #267
        0x108,
        "#070FQuite! Let us free your family.\x02",
    )

    CloseMessageWindow()

    label("loc_9D07")

    OP_A2(0x2225)
    OP_28(0x9E, 0x1, 0x80)
    EventEnd(0x0)
    Jump("loc_9D65")

    label("loc_9D15")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #268
        "\x07\x05The more you stare, the emptier it seems.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_9D65")

    Return()

    # Function_37_98A3 end

    def Function_38_9D66(): pass

    label("Function_38_9D66")

    EventBegin(0x0)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D86")
    Call(0, 58)
    Call(0, 59)

    label("loc_9D86")

    OP_6D(-42070, 0, 75240, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -42880, 0, 76490, 180)
    SetChrPos(0x102, -42880, 0, 76490, 180)
    SetChrPos(0x10B, -42880, 0, 76490, 180)
    SetChrPos(0xF9, -42880, 0, 76490, 180)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x12, 0x10)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 0)
    OP_70(0x12, 0xF)
    OP_73(0x12)
    Sleep(300)

    def lambda_9E41():
        OP_6D(-42610, 0, 71440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E41)

    def lambda_9E59():
        OP_67(0, 6710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9E59)
    OP_43(0x101, 0x0, 0x0, 0x27)
    Sleep(700)
    OP_43(0x102, 0x0, 0x0, 0x28)
    Sleep(600)
    OP_43(0x10B, 0x0, 0x0, 0x29)
    Sleep(600)
    OP_43(0xF9, 0x0, 0x0, 0x2A)
    Sleep(1000)
    OP_71(0x12, 0x10)
    OP_6F(0x12, 15)
    OP_70(0x12, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF9, 0x0)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #269
        0x101,
        (
            "#1015F#2PThis is roughly the area where\x01",
            "they kept me locked up, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        (
            "#1035F#1PYes, this is the second floor of the forecastle.\x02\x03",

            "#1040FAmong other things, the jaeger barracks\x01",
            "and briefing rooms are in this section.\x02\x03",

            "A copy of the current security card should\x01",
            "be around here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #271
        0x10B,
        (
            "#212F#6PThen what are we waiting for?!\x01",
            "Let's look!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #272
        0x101,
        (
            "#1007F#2PYes, we know, calm down.\x02\x03",

            "#1006FProbably best to check each room,\x01",
            "one by one. C'mon!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22B2)
    EventEnd(0x0)
    Return()

    # Function_38_9D66 end

    def Function_39_A0B2(): pass

    label("Function_39_A0B2")

    OP_8E(0xFE, 0xFFFF575E, 0x0, 0x10F68, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_39_A0B2 end

    def Function_40_A0E6(): pass

    label("Function_40_A0E6")

    OP_8E(0xFE, 0xFFFF5740, 0x0, 0x11E22, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF53C6, 0x0, 0x1140E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_40_A0E6 end

    def Function_41_A116(): pass

    label("Function_41_A116")

    OP_8E(0xFE, 0xFFFF5740, 0x0, 0x11E22, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5C54, 0x0, 0x11512, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_41_A116 end

    def Function_42_A146(): pass

    label("Function_42_A146")

    OP_8E(0xFE, 0xFFFF5858, 0x0, 0x11904, 0x7D0, 0x0)
    Return()

    # Function_42_A146 end

    def Function_43_A15B(): pass

    label("Function_43_A15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B218")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A18C")
    Call(0, 58)
    Call(0, 59)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_A18C")

    Fade(1000)
    OP_6D(-37810, 0, -66450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -37980, 0, -67260, 90)
    SetChrPos(0x102, -38640, 0, -66330, 90)
    SetChrPos(0x10B, -39140, 0, -67430, 90)
    SetChrPos(0xF9, -39800, 0, -66450, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #273
        0x101,
        "#1004F#6PHey, this elevator...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#1042F#6PThis is the elevator used to access\x01",
            "the sanctuary and engine room.\x02\x03",

            "This one checks voice pattern. I think you\x01",
            "saw Renne do it, right? Only Enforcers and\x01",
            "above can use it.\x02\x03",

            "#1035FGiven that I'm currently AWOL from the\x01",
            "society, I'm afraid we can't make use of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #275
        0x101,
        "#1007F#4PRight...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x102, 400)
    Sleep(300)

    ChrTalk(    #276
        0x10B,
        "#213F#5PEr... What's a 'voice pattern'?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)
    Sleep(300)

    ChrTalk(    #277
        0x102,
        (
            "#1040F#6PNo two people have exactly the same voice.\x02\x03",

            "This machine can read a person's\x01",
            "voice and use it to identify them.\x02\x03",

            "That's how I understand it, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x10B,
        "#414F#5PI see... I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1016F#4PI feel like I get it and don't\x01",
            "get it at the same time...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A676")

    ChrTalk(    #280
        0x107,
        (
            "#561F#1PThat's such amazing technology...!\x02\x03",

            "#063F...Hey, Joshua?\x02\x03",

            "I've been curious about this for a long time.\x01",
            "Who makes the technology the society uses?\x01",
            "Like this ship, or the archaisms?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_A676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A82D")

    ChrTalk(    #282
        0x105,
        (
            "#1167F#1PSuch incredible technology.\x02\x03",

            "#1162FJoshua... I've been wondering for a while now.\x02\x03",

            "Where does the society get such\x01",
            "overwhelmingly advanced technology?\x01",
            "This ship, the archaisms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x102,
        (
            "#1035F#4PWhere indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_A82D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9E8")

    ChrTalk(    #284
        0x109,
        (
            "#1068F#1PAgain and again with the crazy freakin' tech...\x02\x03",

            "#1063F...Say, J?\x01",
            "Mind if I pry a bit?\x02\x03",

            "Where DO all these wonderful 'toys' come from?\x01",
            "Who makes stuff like this ship, or the archaisms?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_A9E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB5F")

    ChrTalk(    #286
        0x103,
        (
            "#025F#1PSuch incredible technology...\x02\x03",

            "#022F...Joshua, if I may?\x02\x03",

            "Where DOES the society get such technology?\x01",
            "Who creates it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_AB5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACFF")

    ChrTalk(    #288
        0x104,
        (
            "#035F#1PSuch astounding technology.\x02\x03",

            "#030FThough, if you would indulge my curiosity,\x01",
            "Joshua.\x02\x03",

            "How does the society possess this incredible\x01",
            "technology? Who created it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_ACFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEA7")

    ChrTalk(    #290
        0x106,
        (
            "#551F#1PSo many little friggin' tricks and traps...\x02\x03",

            "#555F...Say, Joshua.\x02\x03",

            "It's been buggin' me for a while.\x01",
            "Where the hell does Ouroboros GET\x01",
            "all this shit? Who designed it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B07B")

    label("loc_AEA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B07B")

    ChrTalk(    #292
        0x108,
        (
            "#074F#1POnce again, Ouroboros' technology is\x01",
            "impressive.\x02\x03",

            "#072FThough, Joshua. It has bothered me for\x01",
            "some time, so if I may ask...?\x02\x03",

            "What is the source of the society's seemingly\x01",
            "limitless technology? Who created it all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x102,
        (
            "#1035F#4PWho indeed.\x02\x03",

            "#1042FOne of the Anguis is a man called\x01",
            "Doctor Novartis.\x02\x03",

            "He leads the 'Thirteen Factories' of Ouroboros in\x01",
            "their development of radical orbal technology.\x01",
            "At least, that's what I was told, back when.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B07B")


    ChrTalk(    #294
        0x10B,
        "#212F#5PThe Thirteen Factories? Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1007F#4PNovartis... Never heard of him.\x02\x03",

            "#1019FIf he makes stuff like this, though, I can only\x01",
            "picture someone who's an even bigger mad\x01",
            "scientist than Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #296
        0x102,
        (
            "#1043F#6PLess 'mad'...and more completely\x01",
            "incomprehensible, from what I remember.\x02\x03",

            "#1035FOf course, to some extent, that's true\x01",
            "of all the Anguis. Including Weissmann.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2226)
    EventEnd(0x0)
    Jump("loc_B27B")

    label("loc_B218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B27B")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #297
        "\x07\x05The elevator doors are tightly closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_B27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D6")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #298
        "\x07\x05The elevator doors are tightly closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_B2D6")

    Return()

    # Function_43_A15B end

    def Function_44_B2D7(): pass

    label("Function_44_B2D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2E4")
    Return()

    label("loc_B2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B362")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x151E4), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x159B4), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x539E4), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x53FC0), scpexpr(EXPR_NEG), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B361")
    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(200)
    Call(0, 45)
    Jump("loc_B362")

    label("loc_B361")

    Return()

    label("loc_B362")

    Return()

    # Function_44_B2D7 end

    def Function_45_B363(): pass

    label("Function_45_B363")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37A")
    Call(0, 58)
    Call(0, 59)

    label("loc_B37A")

    Fade(1000)
    OP_6D(-86740, 0, -342830, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -88010, 0, -343970, 90)
    SetChrPos(0x102, -87600, 0, -343010, 90)
    SetChrPos(0x10B, -88360, 0, -342220, 90)
    SetChrPos(0xF9, -88850, 0, -343260, 90)
    OP_0D()
    Sleep(500)
    FadeToBright(0, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B480")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_71(0x23, 0x4)
    Sleep(100)
    OP_72(0x24, 0x4)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #299
        "\x07\x05--ID confirmed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_B480")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #300
        "\x07\x05Please select the barrier you wish to unlock.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #301
        "\x18\x07\x05Enter barrier # to release:\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[#1]\x01",      # 0
            "[#2]\x01",      # 1
            "[#3]\x01",      # 2
            "[#4]\x01",      # 3
            "[#5]\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_B584"),
        (2, "loc_B735"),
        (3, "loc_B8E6"),
        (4, "loc_BA97"),
        (0, "loc_BC48"),
        (SWITCH_DEFAULT, "loc_C20E"),
    )


    label("loc_B584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B667")
    OP_6D(-83240, 0, -320400, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x4)
    Sleep(500)
    OP_6F(0x4, 35)
    OP_70(0x4, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2228)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_B732")

    label("loc_B667")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #302
        "\x07\x05Lock on #2 removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_B732")

    Jump("loc_C20E")

    label("loc_B735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B818")
    OP_6D(-83240, 0, -309340, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x5)
    Sleep(500)
    OP_6F(0x5, 35)
    OP_70(0x5, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2229)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_B8E3")

    label("loc_B818")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #303
        "\x07\x05Lock on #3 removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_B8E3")

    Jump("loc_C20E")

    label("loc_B8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9C9")
    OP_6D(-83240, 0, -299470, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)
    OP_6F(0x6, 35)
    OP_70(0x6, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x222A)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_BA94")

    label("loc_B9C9")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #304
        "\x07\x05Lock on #4 removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_BA94")

    Jump("loc_C20E")

    label("loc_BA97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7A")
    OP_A2(0x222B)
    OP_6D(-83240, 0, -289000, 3000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x7)
    Sleep(500)
    OP_6F(0x7, 35)
    OP_70(0x7, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_BC45")

    label("loc_BB7A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #305
        "\x07\x05Lock on #5 removed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_6D(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -87600, 0, -342990, 90)
    SetChrPos(0x1, -87600, 0, -342990, 90)
    SetChrPos(0x2, -87600, 0, -342990, 90)
    SetChrPos(0x3, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x0)
    TalkEnd(0xFF)

    label("loc_BC45")

    Jump("loc_C20E")

    label("loc_BC48")

    SetMessageWindowPos(-1, -1, -1, -1)
    OP_6D(-81410, 0, -332940, 2000)
    OP_22(0xAA, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x23)
    OP_22(0xE1, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)
    OP_6F(0x3, 35)
    OP_70(0x3, 0x32)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x3)
    OP_4A(0xF, 0)

    def lambda_BCA7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BCA7)
    Sleep(20)
    OP_4A(0x10, 0)

    def lambda_BCBE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BCBE)
    Sleep(80)
    OP_4A(0x11, 0)

    def lambda_BCD5():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BCD5)
    Sleep(10)
    OP_4A(0x14, 0)

    def lambda_BCEC():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BCEC)
    Sleep(10)
    OP_4A(0x15, 0)

    def lambda_BD03():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BD03)
    Sleep(70)
    OP_4A(0x12, 0)

    def lambda_BD1A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BD1A)
    Sleep(20)
    OP_4A(0x13, 0)

    def lambda_BD31():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BD31)
    Sleep(15)
    OP_4A(0x16, 0)
    OP_8C(0x16, 270, 400)

    ChrTalk(    #306
        0x13,
        "#2PHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x14,
        "#6PWe're saaaaved!\x02",
    )

    CloseMessageWindow()

    def lambda_BD74():
        OP_6D(-86260, 0, -337310, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BD74)

    def lambda_BD8C():
        OP_67(0, 4660, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BD8C)

    def lambda_BDA4():
        OP_6B(3450, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_BDA4)

    def lambda_BDB4():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_BDB4)
    OP_43(0x10, 0x1, 0x0, 0x30)
    Sleep(500)
    OP_43(0xF, 0x1, 0x0, 0x2F)
    Sleep(600)
    OP_43(0x102, 0x2, 0x0, 0x2E)
    OP_43(0x16, 0x1, 0x0, 0x31)
    Sleep(700)
    OP_43(0x12, 0x1, 0x0, 0x32)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x33)
    OP_43(0x14, 0x1, 0x0, 0x34)
    Sleep(400)
    OP_43(0x11, 0x1, 0x0, 0x35)
    Sleep(600)
    OP_43(0x15, 0x1, 0x0, 0x36)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #308
        0x10B,
        "#415F#2PKyle, Don! We did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x10,
        "#200F#6PJosette...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xF,
        (
            "#490F#6PHeheh...\x02\x03",

            "I suppose we owe you, kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x102,
        (
            "#1040F#2PNo, Don. Consider us even,\x01",
            "if anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1006F#2PYeah, you guys saved our bacon.\x01",
            "We're just settling the balance!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAC, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF7C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BFBA")

    label("loc_BF7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFA3")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BFBA")

    label("loc_BFA3")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BFBA")

    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10B, 180, 400)

    ChrTalk(    #313
        0x101,
        "#1005FAw, crud!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        (
            "#1035F#2PLooks like we finally kicked the\x01",
            "hornet's nest too hard...\x02\x03",

            "#1042FEveryone, we're leaving. Now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x10B,
        "#210F#5PR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x10,
        "#201F#6PTime to work those legs!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 45, 400)
    OP_8C(0x14, 225, 400)

    ChrTalk(    #317
        0xF,
        "#196F#6PBoys, don't you dare fall behind!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(150, 80, -1, -1)
    SetChrName("Bandits")

    AnonymousTalk(    #318
        "\x07\x00#5SAye, aye, sir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5702   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_C20E")

    label("loc_C20E")

    Return()

    # Function_45_B363 end

    def Function_46_C20F(): pass

    label("Function_46_C20F")


    def lambda_C215():
        OP_8E(0xFE, 0xFFFEA926, 0x0, 0xFFFAD134, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_C215)
    Sleep(300)

    def lambda_C235():
        OP_8E(0xFE, 0xFFFEAAF2, 0x0, 0xFFFACBDA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C235)
    Sleep(300)

    def lambda_C255():
        OP_8E(0xFE, 0xFFFEA3FE, 0x0, 0xFFFAC8F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C255)
    Sleep(300)

    def lambda_C275():
        OP_8E(0xFE, 0xFFFEA80E, 0x0, 0xFFFAC63A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C275)
    WaitChrThread(0x10B, 0x1)
    Return()

    # Function_46_C20F end

    def Function_47_C290(): pass

    label("Function_47_C290")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEA6B0, 0x0, 0xFFFAD6DE, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_47_C290 end

    def Function_48_C2D4(): pass

    label("Function_48_C2D4")

    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEAC3C, 0x0, 0xFFFAD63E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_48_C2D4 end

    def Function_49_C304(): pass

    label("Function_49_C304")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEA548, 0x0, 0xFFFADC24, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_49_C304 end

    def Function_50_C348(): pass

    label("Function_50_C348")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEA7BE, 0x0, 0xFFFAE188, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_50_C348 end

    def Function_51_C38C(): pass

    label("Function_51_C38C")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB074, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEAA16, 0x0, 0xFFFADD5A, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_51_C38C end

    def Function_52_C3D0(): pass

    label("Function_52_C3D0")

    OP_8E(0xFE, 0xFFFEB89E, 0x0, 0xFFFADF62, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEAE1C, 0x0, 0xFFFADB7A, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_52_C3D0 end

    def Function_53_C400(): pass

    label("Function_53_C400")

    OP_8E(0xFE, 0xFFFEB916, 0x0, 0xFFFAE3D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFEB36C, 0x0, 0xFFFADE18, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_53_C400 end

    def Function_54_C430(): pass

    label("Function_54_C430")

    OP_8E(0xFE, 0xFFFEB682, 0x0, 0xFFFAE37C, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_54_C430 end

    def Function_55_C44C(): pass

    label("Function_55_C44C")

    OP_A3(0x1C81)
    OP_A2(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_55_C44C end

    def Function_56_C465(): pass

    label("Function_56_C465")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A2(0x1C83)
    OP_A3(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_56_C465 end

    def Function_57_C47E(): pass

    label("Function_57_C47E")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A2(0x1C84)
    OP_A3(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_57_C47E end

    def Function_58_C497(): pass

    label("Function_58_C497")

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
        (0, "loc_C510"),
        (1, "loc_C516"),
        (SWITCH_DEFAULT, "loc_C51C"),
    )


    label("loc_C510")

    OP_A2(0x1200)
    Jump("loc_C51C")

    label("loc_C516")

    OP_A2(0x1201)
    Jump("loc_C51C")

    label("loc_C51C")

    Return()

    # Function_58_C497 end

    def Function_59_C51D(): pass

    label("Function_59_C51D")

    FadeToDark(0, 0, -1)
    OP_6D(-107890, 0, -346700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
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

    # Function_59_C51D end

    def Function_60_C5AE(): pass

    label("Function_60_C5AE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24012F, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_60_C5AE end

    def Function_61_C5D4(): pass

    label("Function_61_C5D4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240130, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_61_C5D4 end

    def Function_62_C5FA(): pass

    label("Function_62_C5FA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240136, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_62_C5FA end

    SaveToFile()

Try(main)
