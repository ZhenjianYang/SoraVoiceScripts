from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Noel',                                 # 9
        'Becker',                               # 10
        'Palmer',                               # 11
        'Patrolman',                            # 12
        'Royal Army Soldier',                   # 13
        'Patrol Guard',                         # 14
        'Giselle',                              # 15
        'Duke Dunan',                           # 16
        'Kanone',                               # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Soldier',                              # 30
        'Soldier',                              # 31
        'Soldier',                              # 32
        'Soldier',                              # 33
        'Soldier',                              # 34
        'Soldier',                              # 35
        'Grancel - West Block',                 # 36
        'Grancel Castle',                       # 37
        'Grancel - East Block',                 # 38
        'Grancel - South Block',                # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
        '',                                     # 43
        '',                                     # 44
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT27/CH03120 ._CH',             # 02
        'ED6_DT07/CH01610 ._CH',             # 03
        'ED6_DT06/CH20043 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01290 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT27/CH04610 ._CH',             # 08
        'ED6_DT27/CH04611 ._CH',             # 09
        'ED6_DT27/CH04620 ._CH',             # 0A
        'ED6_DT27/CH04621 ._CH',             # 0B
        'ED6_DT29/CH12570 ._CH',             # 0C
        'ED6_DT29/CH12571 ._CH',             # 0D
        'ED6_DT29/CH12350 ._CH',             # 0E
        'ED6_DT29/CH12351 ._CH',             # 0F
        'ED6_DT29/CH12320 ._CH',             # 10
        'ED6_DT29/CH12321 ._CH',             # 11
        'ED6_DT07/CH01230 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT27/CH03120P._CP',             # 02
        'ED6_DT07/CH01610P._CP',             # 03
        'ED6_DT06/CH20043P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01290P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT27/CH04610P._CP',             # 08
        'ED6_DT27/CH04611P._CP',             # 09
        'ED6_DT27/CH04620P._CP',             # 0A
        'ED6_DT27/CH04621P._CP',             # 0B
        'ED6_DT29/CH12570P._CP',             # 0C
        'ED6_DT29/CH12571P._CP',             # 0D
        'ED6_DT29/CH12350P._CP',             # 0E
        'ED6_DT29/CH12351P._CP',             # 0F
        'ED6_DT29/CH12320P._CP',             # 10
        'ED6_DT29/CH12321P._CP',             # 11
        'ED6_DT07/CH01230P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2950,
        Z                   = 0,
        Y                   = 63820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -7440,
        Z                   = 0,
        Y                   = 49400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 7690,
        Z                   = 0,
        Y                   = 41560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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
        X                   = 170,
        Z                   = 0,
        Y                   = 39490,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x54A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16030,
        Z                   = 0,
        Y                   = 63610,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x548,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40070,
        Z                   = 0,
        Y                   = 49910,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x547,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14730,
        Z                   = 0,
        Y                   = 50220,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x549,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9080,
        Z                   = 250,
        Y                   = 58390,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x546,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = 19260,
        TriggerZ            = 750,
        TriggerY            = 44000,
        TriggerRange        = 800,
        ActorX              = 19260,
        ActorZ              = 1750,
        ActorY              = 44000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23040,
        TriggerZ            = 500,
        TriggerY            = 63200,
        TriggerRange        = 800,
        ActorX              = -23040,
        ActorZ              = 1500,
        ActorY              = 63200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22160,
        TriggerZ            = 500,
        TriggerY            = 29050,
        TriggerRange        = 800,
        ActorX              = -22160,
        ActorZ              = 1500,
        ActorY              = 29050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_63A",          # 00, 0
        "Function_1_6EB",          # 01, 1
        "Function_2_7AB",          # 02, 2
        "Function_3_7C1",          # 03, 3
        "Function_4_807",          # 04, 4
        "Function_5_A18",          # 05, 5
        "Function_6_A72",          # 06, 6
        "Function_7_B09",          # 07, 7
        "Function_8_C10",          # 08, 8
        "Function_9_C34",          # 09, 9
        "Function_10_12B9",        # 0A, 10
        "Function_11_16A7",        # 0B, 11
        "Function_12_1D45",        # 0C, 12
        "Function_13_1F28",        # 0D, 13
        "Function_14_20B3",        # 0E, 14
        "Function_15_2257",        # 0F, 15
        "Function_16_2733",        # 10, 16
        "Function_17_2778",        # 11, 17
        "Function_18_27FA",        # 12, 18
        "Function_19_2F3A",        # 13, 19
        "Function_20_33D6",        # 14, 20
        "Function_21_35AF",        # 15, 21
        "Function_22_35F1",        # 16, 22
        "Function_23_3988",        # 17, 23
        "Function_24_3D1F",        # 18, 24
        "Function_25_3DA5",        # 19, 25
        "Function_26_3DFE",        # 1A, 26
    )


    def Function_0_63A(): pass

    label("Function_0_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_645")
    Call(0, 20)

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_663")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_6C3")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_67C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_6C3")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_690")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6C3")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_6A4")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6C3")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    Jump("loc_6C3")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_6BC")
    Jump("loc_6C3")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_6C3")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6D9")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_6EA")

    label("loc_6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_6EA")

    Return()

    # Function_0_63A end

    def Function_1_6EB(): pass

    label("Function_1_6EB")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_712")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_732")
    OP_B1("t4103_y")
    Jump("loc_753")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74A")
    OP_B1("t4103_y")
    Jump("loc_753")

    label("loc_74A")

    OP_B1("t4103_n")

    label("loc_753")

    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_79C")
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x10)
    OP_1B(0x4, 0x0, 0x17)
    OP_1B(0x5, 0x0, 0x16)
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 19)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_7AA")

    label("loc_79C")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B5(0x0)

    label("loc_7AA")

    Return()

    # Function_1_6EB end

    def Function_2_7AB(): pass

    label("Function_2_7AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7AB")

    label("loc_7C0")

    Return()

    # Function_2_7AB end

    def Function_3_7C1(): pass

    label("Function_3_7C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_806")
    SetChrPos(0xFE, 31870, 0, 62980, 270)
    OP_8E(0xFE, 0xC6C, 0x0, 0xF604, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_3_7C1")

    label("loc_806")

    Return()

    # Function_3_7C1 end

    def Function_4_807(): pass

    label("Function_4_807")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A17")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xFD84, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_4_807")

    label("loc_A17")

    Return()

    # Function_4_807 end

    def Function_5_A18(): pass

    label("Function_5_A18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A71")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_5_A18")

    label("loc_A71")

    Return()

    # Function_5_A18 end

    def Function_6_A72(): pass

    label("Function_6_A72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B08")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_6_A72")

    label("loc_B08")

    Return()

    # Function_6_A72 end

    def Function_7_B09(): pass

    label("Function_7_B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0F")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_7_B09")

    label("loc_C0F")

    Return()

    # Function_7_B09 end

    def Function_8_C10(): pass

    label("Function_8_C10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C33")
    OP_8D(0xFE, 8130, 41700, 5710, 43100, 2000)
    Jump("Function_8_C10")

    label("loc_C33")

    Return()

    # Function_8_C10 end

    def Function_9_C34(): pass

    label("Function_9_C34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D12")

    ChrTalk(    #0
        0xFE,
        (
            "Everyone's acting like the queen can\x01",
            "just snap her fingers and make things\x01",
            "all better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "They still don't even know why orbal\x01",
            "energy's stopped, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "This sucks... I'm stressing out, big time...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(    #3
        0xFE,
        (
            "Did you hear about the West Block?\x01",
            "Crazy stuff, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Good thing that finished off the remnants\x01",
            "of the Intelligence Division. We should be\x01",
            "able to rest easy for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_EF0")

    ChrTalk(    #5
        0xFE,
        (
            "I've seen this couple with an adorable\x01",
            "little girl in a white dress around recently.\x01",
            "Tourists, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I've gotten so used to seeing the three of\x01",
            "them together that it threw me for a loop when\x01",
            "I saw their daughter walking alone today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "I hope everything's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6D")

    ChrTalk(    #8
        0xFE,
        "Oh, no, look at the time! \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I need to do some shopping for dinner\x01",
            "before the department store closes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_107E")

    ChrTalk(    #10
        0xFE,
        (
            "It feels like people from the Erebonia\x01",
            "and Calvard embassies have been in\x01",
            "and out of the castle a lot these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Maybe it's because of the signing ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "A non-aggression fact almost sounds\x01",
            "too good to real, but it is. It's actually\x01",
            "happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_107E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_12B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AB")

    ChrTalk(    #13
        0xFE,
        (
            "Have you heard? They've finally reopened\x01",
            "the castle to the public. It was closed during\x01",
            "the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I, of course, recommend a visit to the\x01",
            "garden terrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "The gentle winds off Valleria Lake and\x01",
            "the scent of the green garden are very\x01",
            "comforting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1003F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_12B5")

    label("loc_11AB")


    ChrTalk(    #17
        0xFE,
        (
            "They've finally reopened the castle to the public\x01",
            "after it was closed during the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I tell this to everyone, but the garden terrace in the\x01",
            "castle catches the breeze from Lake Valleria, and the\x01",
            "smell of the greenery there is just...so relaxing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B5")

    TalkEnd(0xFE)
    Return()

    # Function_9_C34 end

    def Function_10_12B9(): pass

    label("Function_10_12B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1349")

    ChrTalk(    #19
        0xFE,
        (
            "You can see that weird thing in\x01",
            "the sky pretty well from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I bet you could see it even better\x01",
            "from the castle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1482")

    ChrTalk(    #21
        0xFE,
        (
            "There's been talk of this enormous\x01",
            "orbal construct appearing around the\x01",
            "harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Everyone's saying it's one of Professor\x01",
            "Russell's crazy new weapons going on\x01",
            "a rampage. Think it could be true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "The rumors won't stop until there's\x01",
            "some official report. I wish they'd say\x01",
            "something, already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1523")

    ChrTalk(    #24
        0xFE,
        (
            "Oh, yeah, so I was talking to the\x01",
            "harbormaster recently, and the topic\x01",
            "of Ruan somehow came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "They've elected their new mayor,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1613")

    ChrTalk(    #26
        0xFE,
        (
            "That reminds me--Ruan's in the\x01",
            "middle of a mayoral election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Whoever succeeds Dalmore has\x01",
            "a hell of a lot of work in store for 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I wish 'em luck. Ruan needs a good\x01",
            "mayor after all the crap it's been through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1662")

    ChrTalk(    #29
        0xFE,
        "Busy, busy, busy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Okay, next delivery's to the East Block.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_1662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_16A3")

    ChrTalk(    #31
        0xFE,
        (
            "Move over, coming through!\x01",
            "I got deliveries to make!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A3")

    TalkEnd(0xFE)
    Return()

    # Function_10_12B9 end

    def Function_11_16A7(): pass

    label("Function_11_16A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1817")

    ChrTalk(    #32
        0xFE,
        (
            "I was given orders from Her Majesty\x01",
            "to go home by home and explain the\x01",
            "situation to each and every resident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Naturally, not a single one of them has\x01",
            "been thrilled to see me. I can understand\x01",
            "why, but it still stings a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "It's better to explain than to keep the\x01",
            "public wondering, though. Just about\x01",
            "anything right now could cause a panic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1952")

    ChrTalk(    #35
        0xFE,
        (
            "There's evidence that the Intelligence\x01",
            "Division was manipulating their budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I say 'manipulating,' but there's\x01",
            "enough to prove they made a number\x01",
            "of unauthorized expenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "One such expense includes that tank\x01",
            "that showed up around the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "That's another mystery solved, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1AB8")

    ChrTalk(    #39
        0xFE,
        (
            "Cassius returning to the army as a\x01",
            "general is a huge deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Not just strategically, but financially, too.\x01",
            "His orders are sound across the board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "He's a real man's man. Don't think we\x01",
            "would've stood a chance against the\x01",
            "Imperial Army if not for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Even just passing him by in the castle\x01",
            "makes me wanna stand straight and focus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0D")

    ChrTalk(    #43
        0xFE,
        (
            "It's about time I return to the castle\x01",
            "and report to Her Majesty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1C91")

    ChrTalk(    #44
        0xFE,
        (
            "There have been all sorts of rumors\x01",
            "flying around about the queen being ill,\x01",
            "but she's quite well, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "It's true that she's been running herself\x01",
            "ragged cleaning up after the coup d'etat and\x01",
            "preparing for the signing ceremony, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'll be right there to support her in any way\x01",
            "I can. Even the slightest delay in the signing\x01",
            "ceremony is unacceptable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D41")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D41")

    ChrTalk(    #47
        0xFE,
        (
            "I work at the castle, so the coup d'etat\x01",
            "was a big deal for me. I've been investigating\x01",
            "it since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "We're in the clear now, but the scars of\x01",
            "that case run deep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D41")

    TalkEnd(0xFE)
    Return()

    # Function_11_16A7 end

    def Function_12_1D45(): pass

    label("Function_12_1D45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D96")

    ChrTalk(    #49
        0xFE,
        (
            "To ensure the citizenry aren't worried,\x01",
            "I have to remain calm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F24")

    label("loc_1D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1EB1")

    ChrTalk(    #50
        0xFE,
        (
            "Captain Amalthea's an amazing woman\x01",
            "in more ways than one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I don't think anyone else would've\x01",
            "been able to carry out the same plans\x01",
            "so meticulously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "It just isn't the kind of thing your\x01",
            "average officer could pull off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "She'd make for a terrifying enemy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F24")

    label("loc_1EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1F24")

    ChrTalk(    #54
        0xFE,
        (
            "The signing will happen at the villa,\x01",
            "but we've been ordered to raise security\x01",
            "in the capital as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F24")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D45 end

    def Function_13_1F28(): pass

    label("Function_13_1F28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FA8")

    ChrTalk(    #55
        0xFE,
        (
            "A weapon in hand's all you need to\x01",
            "protect the citizenry, so I'm not too\x01",
            "worried about the orbment situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AF")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_206B")

    ChrTalk(    #56
        0xFE,
        (
            "Had that tank entered the city grounds,\x01",
            "the damage would've been far worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "One mistake could have set the entire\x01",
            "capital ablaze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Just the thought alone is horrifying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AF")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_20AF")

    ChrTalk(    #59
        0xFE,
        (
            "All clear here! I've found nothing out\x01",
            "of the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AF")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F28 end

    def Function_14_20B3(): pass

    label("Function_14_20B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20EA")

    ChrTalk(    #60
        0xFE,
        "Nice to meet you! My name's Giselle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2253")

    label("loc_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2115")

    ChrTalk(    #61
        0xFE,
        "That tank was horrifying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2253")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_217B")

    ChrTalk(    #62
        0xFE,
        "A girl in white? Is she lost or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Sorry, I haven't seen her around here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2253")

    label("loc_217B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D2")

    ChrTalk(    #64
        0xFE,
        (
            "Sorry, afraid I can't talk. I've got to\x01",
            "head back to my hotel room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2253")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2205")

    ChrTalk(    #65
        0xFE,
        "Maybe I should go visit the castle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2253")

    label("loc_2205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2253")

    ChrTalk(    #66
        0xFE,
        (
            "I've always wanted to stay in this hotel!\x01",
            "It's so nice, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2253")

    TalkEnd(0xFE)
    Return()

    # Function_14_20B3 end

    def Function_15_2257(): pass

    label("Function_15_2257")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_77(0xC8, 0xC8, 0xC8, 0x0, 0x0)
    OP_11(0x0, 0x0, 0x0, 0x9470, 0x1FBD0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -2650, 0, 50890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(-3300, 0, 71820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2540, 0, 73310, 180)
    SetChrPos(0xD, -2180, 0, 41910, 0)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x3, 0x0, 0x10)
    Sleep(600)
    FadeToBright(1000, 0)

    def lambda_237F():
        OP_6D(-2650, 0, 50890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_237F)
    OP_8E(0x101, 0xFFFFF5E2, 0x0, 0xC788, 0x1B58, 0x0)

    ChrTalk(    #67
        0x101,
        (
            "#584F#3P*huff*... *huff*...\x02\x03",

            "No...\x02\x03",

            "#588FJust... No way...\x02\x03",

            "Joshua wouldn't...\x01",
            "wouldn't run away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "#1PWhoa, you okay, miss? What're\x01",
            "you doing out without an umbrella?\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xD, 0x101, 0x7D0, 0xBB8, 0x0)

    ChrTalk(    #69
        0xD,
        (
            "You'll get soaked if you remain out in\x01",
            "this mess! You should head on home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#004F#3PHome...?\x02\x03",

            "Home...\x02\x03",

            "#586FYeah... Yeah, you're right.\x02\x03",

            "I should head home.\x01",
            "Joshua must've headed home.\x02\x03",

            "He...probably went right back home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#006F#3PThanks, Mr. Guard!\x02\x03",

            "I'll head home right away!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_259A():
        OP_6D(-1170, 0, 52220, 1000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_259A)

    def lambda_25B2():
        OP_67(0, 9500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_25B2)
    OP_8C(0x101, 45, 800)

    def lambda_25D1():
        OP_8E(0x101, 0x758, 0x0, 0xD548, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25D1)
    WaitChrThread(0x101, 0x1)

    def lambda_25F1():
        OP_8E(0x101, 0x938, 0x0, 0xEB3C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25F1)
    Sleep(1500)

    def lambda_2611():
        OP_6D(-2550, 0, 49300, 1500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2611)

    def lambda_2629():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2629)
    Sleep(1500)

    ChrTalk(    #73
        0xD,
        "What was THAT all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        "Swear I've seen her somewhere before...\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0xD,
        (
            "Wait, isn't that the girl who\x01",
            "helped stop the coup?!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_24(0x1C9, 0x5A)
    OP_0D()
    OP_AD(0x2400B6, 0x0, 0x0, 0x96)
    Sleep(1000)
    OP_56(0x2)
    OP_20(0xFA0)
    OP_43(0xD, 0x3, 0x0, 0x11)
    OP_AE(0xC8)
    OP_21()
    WaitChrThread(0xD, 0x3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/E0001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2257 end

    def Function_16_2733(): pass

    label("Function_16_2733")

    OP_22(0x1C9, 0x1, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Return()

    # Function_16_2733 end

    def Function_17_2778(): pass

    label("Function_17_2778")

    OP_24(0x1C9, 0x5F)
    Sleep(200)
    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C9, 0x55)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x4B)
    Sleep(200)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C9, 0x41)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x37)
    Sleep(200)
    OP_24(0x1C9, 0x32)
    Sleep(200)
    OP_24(0x1C9, 0x2D)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x23)
    Sleep(200)
    OP_24(0x1C9, 0x1E)
    Sleep(200)
    OP_23(0x1C9)
    Return()

    # Function_17_2778 end

    def Function_18_27FA(): pass

    label("Function_18_27FA")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0x8, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -40420, 0, 33150, 360)
    OP_6D(-40710, 0, 35630, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(262, 0)
    OP_69(0xF, 0x0)
    OP_C4(0x0, 0x40)
    OP_6A(0xF)
    FadeToBright(2000, 0)
    OP_8F(0xF, 0xFFFF62E4, 0x0, 0x83D6, 0x258, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF621C, 0x0, 0x86F6, 0x3E8, 0x0)
    Sleep(50)
    OP_8F(0xF, 0xFFFF6154, 0x0, 0x8B2E, 0x258, 0x0)
    Sleep(50)

    ChrTalk(    #76
        0xF,
        (
            "#480F*hic*...!\x02\x03",

            "Curse that Phillip and his inshessant scholding...\x02\x03",

            "Who dosh he think I am?!\x02\x03",

            "I'm... I'm Dunan von Aushlese!\x01",
            "I'm the rightful heeeir to thish country!\x01",
            "*HIC*!\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xF, 0xFFFF6280, 0x0, 0x8E62, 0x3E8, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF6348, 0x0, 0x920E, 0x258, 0x0)
    Sleep(50)

    ChrTalk(    #77
        0xF,
        (
            "#483FEuaughahgh... Think I drank t'much beer...\x02\x03",

            "That...'curry' shtuff was quite tashty, though...\x02\x03",

            "I shuppose lowering m'augusht shelf to th' level\x01",
            "of the peasantsh can be enjoyable shometimes...\x01",
            "*HIC*!\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xF, 0xFFFF63AC, 0x0, 0x9402, 0x3E8, 0x0)
    Sleep(100)
    OP_8F(0xF, 0xFFFF64CE, 0x0, 0x9786, 0x320, 0x0)
    Sleep(50)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)

    ChrTalk(    #78
        0xF,
        (
            "#480FPeasantsh... Thoshe brats...\x02\x03",

            "Klaudia...'n that bracer girl...\x02\x03",

            "Why... How could little girlsh like them...\x02\x03",

            "Why d'they confuse me sho...with their words!\x01",
            "And their...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -39770, 0, 46180, 180)

    NpcTalk(    #79
        0x10,
        "Woman's Voice",
        (
            "#2PYour suffering is great indeed,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_20(0x7D0)
    OP_6D(-39770, 0, 42350, 2000)

    ChrTalk(    #80
        0xF,
        (
            "#481F#4PWhrrr...?\x02\x03",

            "Yer Richard's...\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x51)
    Sleep(500)

    ChrTalk(    #81
        0x10,
        (
            "#1180F#5PCaptain Kanone Amalthea, Your Highness.\x02\x03",

            "It is good to see you well.\x02\x03",

            "#1183FThough...I suspect I may have\x01",
            "caught you at a bad time.\x02",
        )
    )

    CloseMessageWindow()
    OP_91(0xF, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    ChrTalk(    #82
        0xF,
        (
            "#484F#4PWhaddya want w'me...?\x02\x03",

            "You're a wanted woman, y'know...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D55():
        OP_6D(-39600, 0, 41260, 1200)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2D55)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -39000, 0, 33000, 0)
    SetChrPos(0x12, -40500, 0, 33000, 0)

    def lambda_2D99():
        OP_8E(0xFE, 0xFFFF67A8, 0x0, 0x8E94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D99)
    Sleep(50)

    def lambda_2DB9():
        OP_8E(0xFE, 0xFFFF61CC, 0x0, 0x8E94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DB9)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xF, 180, 600)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_91(0xF, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(    #83
        0xF,
        "#484F#6PUwaaaa!\x02",
    )

    CloseMessageWindow()

    def lambda_2E3C():
        OP_6D(-39600, 0, 38790, 2500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2E3C)

    def lambda_2E54():
        OP_92(0xFE, 0xF, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2E54)
    Sleep(2000)
    OP_8C(0xF, 360, 400)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x10, 0x2)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #84
        0x10,
        (
            "#1180FDon't be so tense, Your Highness.\x01",
            "You might get hurt.\x02\x03",

            "I simply...need your help, that's all.\x02\x03",

            "#1181FIf you would come with me...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_27FA end

    def Function_19_2F3A(): pass

    label("Function_19_2F3A")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 18680, 5000, 41990, 0, 0, 0, 1500, 1800, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -410, 3500, 33390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -16160, 4400, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -610, 3600, 25270, 0, 0, 0, 1300, 1500, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 10660, 5000, 27200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -21520, 5000, 26000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -22010, 5000, 62980, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 760, 4200, 58600, 0, 0, 0, 1500, 1700, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -46780, 3000, 52260, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -610, 3300, 25270, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -22010, 4800, 62980, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 760, 3800, 58600, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 10660, 4800, 27200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -21520, 4700, 26000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -46780, 2480, 52260, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 16740, 4200, 51970, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -410, 3400, 33390, 0, 0, 0, 1100, 1300, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -16160, 3900, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 18680, 4800, 41990, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_19_2F3A end

    def Function_20_33D6(): pass

    label("Function_20_33D6")

    SetChrPos(0x13, -37620, 0, 37330, 45)
    SetChrPos(0x14, -41800, 0, 37210, 135)
    SetChrPos(0x15, 9070, 0, 30110, 315)
    SetChrPos(0x16, 8300, 0, 66830, 225)
    SetChrPos(0x17, -6670, 0, 58620, 135)
    SetChrPos(0x18, -2340, 0, 34710, 180)
    SetChrPos(0x19, -9060, 250, 28940, 90)
    SetChrPos(0x1A, 13690, 250, 44060, 270)
    SetChrPos(0x1B, 4640, 0, 44330, 225)
    SetChrPos(0x1C, -11050, 0, 50470, 90)
    SetChrPos(0x1D, -30670, 0, 47940, 180)
    SetChrPos(0x1E, 8950, 250, 58550, 225)
    SetChrPos(0x1F, 3900, 0, 60990, 315)
    SetChrPos(0x20, -7260, 0, 48580, 270)
    SetChrPos(0x21, -6530, 250, 36470, 315)
    SetChrPos(0x22, 5150, 10, 30490, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    ClearChrFlags(0x1D, 0x1)
    ClearChrFlags(0x1E, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    ClearChrFlags(0x21, 0x1)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x22, 0x20)
    Return()

    # Function_20_33D6 end

    def Function_21_35AF(): pass

    label("Function_21_35AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_35AF end

    def Function_22_35F1(): pass

    label("Function_22_35F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FA")
    Return()

    label("loc_35FA")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_361A")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_361A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        (
            "\x07\x05The sounds of gunfire and blades clashing can be\x01",
            "periodically heard from the eastern city block.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3719")

    ChrTalk(    #87
        0x101,
        (
            "#1002F(Sounds like the army and the\x01",
            "jaegers are fighting.)\x02\x03",

            "(We need to get to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3967")

    label("loc_3719")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A0")

    ChrTalk(    #88
        0x102,
        (
            "#1042F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(Let's leave this to them and\x01",
            "hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3967")

    label("loc_37A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381B")

    ChrTalk(    #89
        0x103,
        (
            "#022F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We should probably head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3967")

    label("loc_381B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3884")

    ChrTalk(    #90
        0x107,
        (
            "#062F(Looks like the army's fighting over there.)\x02\x03",

            "(We need to hurry to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3967")

    label("loc_3884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F7")

    ChrTalk(    #91
        0x106,
        (
            "#057F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We need to head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3967")

    label("loc_38F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3967")

    ChrTalk(    #92
        0x108,
        (
            "#072F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We need to head to the castle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3967")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_35F1 end

    def Function_23_3988(): pass

    label("Function_23_3988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3991")
    Return()

    label("loc_3991")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39B1")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_39B1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #93
        (
            "\x07\x05The sounds of gunfire and swords clashing can be\x01",
            "periodically heard from the western city block.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB0")

    ChrTalk(    #94
        0x101,
        (
            "#1002F(Sounds like the army and the\x01",
            "jaegers are fighting.)\x02\x03",

            "(We need to get to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B37")

    ChrTalk(    #95
        0x102,
        (
            "#1042F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(Let's leave this to them and\x01",
            "hurry to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3B37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB2")

    ChrTalk(    #96
        0x103,
        (
            "#022F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We should probably head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1B")

    ChrTalk(    #97
        0x107,
        (
            "#062F(Looks like the army's fighting over there.)\x02\x03",

            "(We need to hurry to the castle!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3C1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8E")

    ChrTalk(    #98
        0x106,
        (
            "#057F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We need to head to the castle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3C8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CFE")

    ChrTalk(    #99
        0x108,
        (
            "#072F(The army forces have been deployed\x01",
            "over here already.)\x02\x03",

            "(We need to head to the castle.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFE")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_3988 end

    def Function_24_3D1F(): pass

    label("Function_24_3D1F")

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
        (0, "loc_3D98"),
        (1, "loc_3D9E"),
        (SWITCH_DEFAULT, "loc_3DA4"),
    )


    label("loc_3D98")

    OP_A2(0x1200)
    Jump("loc_3DA4")

    label("loc_3D9E")

    OP_A2(0x1201)
    Jump("loc_3DA4")

    label("loc_3DA4")

    Return()

    # Function_24_3D1F end

    def Function_25_3DA5(): pass

    label("Function_25_3DA5")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_25_3DA5 end

    def Function_26_3DFE(): pass

    label("Function_26_3DFE")

    SetPlaceName(0xB4)
    Return()

    # Function_26_3DFE end

    SaveToFile()

Try(main)
