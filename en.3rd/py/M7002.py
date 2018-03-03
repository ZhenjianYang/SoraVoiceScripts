from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7002   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT26/CH20622 ._CH',             # 00
        'ED6_DT29/CH14400 ._CH',             # 01
        'ED6_DT29/CH14401 ._CH',             # 02
        'ED6_DT29/CH14410 ._CH',             # 03
        'ED6_DT29/CH14411 ._CH',             # 04
        'ED6_DT29/CH14420 ._CH',             # 05
        'ED6_DT29/CH14421 ._CH',             # 06
        'ED6_DT29/CH14010 ._CH',             # 07
        'ED6_DT29/CH14011 ._CH',             # 08
        'ED6_DT29/CH14020 ._CH',             # 09
        'ED6_DT27/CH03581 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT26/CH20622P._CP',             # 00
        'ED6_DT29/CH14400P._CP',             # 01
        'ED6_DT29/CH14401P._CP',             # 02
        'ED6_DT29/CH14410P._CP',             # 03
        'ED6_DT29/CH14411P._CP',             # 04
        'ED6_DT29/CH14420P._CP',             # 05
        'ED6_DT29/CH14421P._CP',             # 06
        'ED6_DT29/CH14010P._CP',             # 07
        'ED6_DT29/CH14011P._CP',             # 08
        'ED6_DT29/CH14020P._CP',             # 09
        'ED6_DT27/CH03581P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 14180,
        Z                   = 6000,
        Y                   = 5970,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6010,
        Z                   = 6000,
        Y                   = -2040,
        Unknown_0C          = 90,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22030,
        Z                   = 6000,
        Y                   = -1980,
        Unknown_0C          = 270,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13970,
        Z                   = -2000,
        Y                   = -52280,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -53060,
        Z                   = -12500,
        Y                   = -49050,
        Unknown_0C          = 90,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -44960,
        Z                   = -12500,
        Y                   = -40990,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36980,
        Z                   = -12500,
        Y                   = -48990,
        Unknown_0C          = 270,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -45080,
        Z                   = -12500,
        Y                   = -57110,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32560,
        Z                   = -34000,
        Y                   = 45090,
        Unknown_0C          = 0,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23970,
        Z                   = -24000,
        Y                   = 20,
        Unknown_0C          = 0,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 9480,
        Y                   = -7000,
        Z                   = -77980,
        Range               = 18460,
        Unknown_10          = 0xFFFFF448,
        Unknown_14          = 0xFFFEDA72,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 13910,
        TriggerZ            = -6000,
        TriggerY            = -87950,
        TriggerRange        = 1000,
        ActorX              = 13910,
        ActorZ              = -4000,
        ActorY              = -87950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14110,
        TriggerZ            = -21000,
        TriggerY            = -23080,
        TriggerRange        = 1000,
        ActorX              = -14400,
        ActorZ              = -21000,
        ActorY              = -25630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14400,
        TriggerZ            = -21500,
        TriggerY            = -25630,
        TriggerRange        = 1000,
        ActorX              = -14260,
        ActorZ              = -20000,
        ActorY              = -23090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34180,
        TriggerZ            = -42000,
        TriggerY            = 10490,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = -39000,
        ActorY              = 11000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 56,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13840,
        TriggerZ            = -24000,
        TriggerY            = -20,
        TriggerRange        = 1000,
        ActorX              = 13000,
        ActorZ              = -23000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 59,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16020,
        TriggerZ            = -24000,
        TriggerY            = 2290,
        TriggerRange        = 1000,
        ActorX              = 16000,
        ActorZ              = -23000,
        ActorY              = 3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 60,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15850,
        TriggerZ            = -24000,
        TriggerY            = -2290,
        TriggerRange        = 1000,
        ActorX              = 16000,
        ActorZ              = -23000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 61,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35300,
        TriggerZ            = -42000,
        TriggerY            = 8010,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = -41000,
        ActorY              = 8000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 62,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35300,
        TriggerZ            = -42000,
        TriggerY            = 14020,
        TriggerRange        = 1000,
        ActorX              = -36000,
        ActorZ              = -41000,
        ActorY              = 14000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 63,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36140,
        TriggerZ            = -22500,
        TriggerY            = -25880,
        TriggerRange        = 1000,
        ActorX              = -36760,
        ActorZ              = -22400,
        ActorY              = -25510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 64,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_422",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_64F",          # 02, 2
        "Function_3_DBA",          # 03, 3
        "Function_4_DE4",          # 04, 4
        "Function_5_DFD",          # 05, 5
        "Function_6_E22",          # 06, 6
        "Function_7_15E4",         # 07, 7
        "Function_8_1600",         # 08, 8
        "Function_9_1635",         # 09, 9
        "Function_10_1656",        # 0A, 10
        "Function_11_1CB1",        # 0B, 11
        "Function_12_1DB7",        # 0C, 12
        "Function_13_2230",        # 0D, 13
        "Function_14_2383",        # 0E, 14
        "Function_15_2526",        # 0F, 15
        "Function_16_262E",        # 10, 16
        "Function_17_2686",        # 11, 17
        "Function_18_26D0",        # 12, 18
        "Function_19_270C",        # 13, 19
        "Function_20_273A",        # 14, 20
        "Function_21_2842",        # 15, 21
        "Function_22_289A",        # 16, 22
        "Function_23_28E4",        # 17, 23
        "Function_24_2920",        # 18, 24
        "Function_25_294E",        # 19, 25
        "Function_26_2A3D",        # 1A, 26
        "Function_27_2AF0",        # 1B, 27
        "Function_28_2BA3",        # 1C, 28
        "Function_29_2C56",        # 1D, 29
        "Function_30_2D09",        # 1E, 30
        "Function_31_2DBC",        # 1F, 31
        "Function_32_2E6F",        # 20, 32
        "Function_33_2F22",        # 21, 33
        "Function_34_2FDE",        # 22, 34
        "Function_35_3091",        # 23, 35
        "Function_36_3144",        # 24, 36
        "Function_37_31F7",        # 25, 37
        "Function_38_32DE",        # 26, 38
        "Function_39_33BC",        # 27, 39
        "Function_40_347F",        # 28, 40
        "Function_41_353B",        # 29, 41
        "Function_42_35F7",        # 2A, 42
        "Function_43_36B3",        # 2B, 43
        "Function_44_376F",        # 2C, 44
        "Function_45_382B",        # 2D, 45
        "Function_46_38E7",        # 2E, 46
        "Function_47_39A3",        # 2F, 47
        "Function_48_3A68",        # 30, 48
        "Function_49_3B24",        # 31, 49
        "Function_50_3BE0",        # 32, 50
        "Function_51_3C9C",        # 33, 51
        "Function_52_3D58",        # 34, 52
        "Function_53_3E14",        # 35, 53
        "Function_54_3F2A",        # 36, 54
        "Function_55_3F78",        # 37, 55
        "Function_56_3FD1",        # 38, 56
        "Function_57_4180",        # 39, 57
        "Function_58_4236",        # 3A, 58
        "Function_59_42E1",        # 3B, 59
        "Function_60_4454",        # 3C, 60
        "Function_61_4635",        # 3D, 61
        "Function_62_478F",        # 3E, 62
        "Function_63_48E4",        # 3F, 63
        "Function_64_4AB8",        # 40, 64
    )


    def Function_0_422(): pass

    label("Function_0_422")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_46E"),
        (101, "loc_475"),
        (102, "loc_47C"),
        (103, "loc_483"),
        (104, "loc_48A"),
        (105, "loc_491"),
        (106, "loc_498"),
        (107, "loc_49F"),
        (108, "loc_4A6"),
        (109, "loc_4AD"),
        (110, "loc_4B4"),
        (111, "loc_4BB"),
        (112, "loc_4C2"),
        (115, "loc_4C9"),
        (SWITCH_DEFAULT, "loc_4D0"),
    )


    label("loc_46E")

    Event(0, 25)
    Jump("loc_4D0")

    label("loc_475")

    Event(0, 26)
    Jump("loc_4D0")

    label("loc_47C")

    Event(0, 27)
    Jump("loc_4D0")

    label("loc_483")

    Event(0, 28)
    Jump("loc_4D0")

    label("loc_48A")

    Event(0, 29)
    Jump("loc_4D0")

    label("loc_491")

    Event(0, 30)
    Jump("loc_4D0")

    label("loc_498")

    Event(0, 31)
    Jump("loc_4D0")

    label("loc_49F")

    Event(0, 32)
    Jump("loc_4D0")

    label("loc_4A6")

    Event(0, 33)
    Jump("loc_4D0")

    label("loc_4AD")

    Event(0, 34)
    Jump("loc_4D0")

    label("loc_4B4")

    Event(0, 35)
    Jump("loc_4D0")

    label("loc_4BB")

    Event(0, 36)
    Jump("loc_4D0")

    label("loc_4C2")

    Event(0, 37)
    Jump("loc_4D0")

    label("loc_4C9")

    Event(0, 38)
    Jump("loc_4D0")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_4F6")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Event(0, 13)
    Jump("loc_51F")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_50C")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 58)
    Jump("loc_51F")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_51F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_51F")

    Return()

    # Function_0_422 end

    def Function_1_520(): pass

    label("Function_1_520")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD8730, 0x23007E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_53F")
    OP_71(0x409, 0x0)
    ExitThread()

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_1B(0x0, 0x0, 0x27)
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)
    OP_1B(0x3, 0x0, 0x2A)
    OP_1B(0x4, 0x0, 0x2B)
    OP_1B(0x5, 0x0, 0x2C)
    OP_1B(0x6, 0x0, 0x2D)
    OP_1B(0x7, 0x0, 0x2E)
    OP_1B(0x8, 0x0, 0x2F)
    OP_1B(0x9, 0x0, 0x30)
    OP_1B(0xA, 0x0, 0x31)
    OP_1B(0xB, 0x0, 0x32)
    OP_1B(0xC, 0x0, 0x33)
    OP_1B(0xF, 0x0, 0x34)

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A2")
    OP_82(0x8F, 0x0)
    OP_82(0x90, 0x0)
    OP_82(0x92, 0x0)

    label("loc_5A2")

    OP_82(0x93, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5B5")
    OP_82(0x94, 0x0)
    Jump("loc_5B8")

    label("loc_5B5")

    OP_82(0x95, 0x0)

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA")
    OP_6F(0x0, 0)
    Jump("loc_5D1")

    label("loc_5CA")

    OP_6F(0x0, 60)

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3")
    OP_6F(0x1, 0)
    Jump("loc_5EA")

    label("loc_5E3")

    OP_6F(0x1, 60)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    OP_6F(0x2, 0)
    Jump("loc_603")

    label("loc_5FC")

    OP_6F(0x2, 60)

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    OP_6F(0x4, 0)
    Jump("loc_61C")

    label("loc_615")

    OP_6F(0x4, 60)

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E")
    OP_6F(0x5, 0)
    Jump("loc_635")

    label("loc_62E")

    OP_6F(0x5, 60)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647")
    OP_6F(0x6, 0)
    Jump("loc_64E")

    label("loc_647")

    OP_6F(0x6, 60)

    label("loc_64E")

    Return()

    # Function_1_520 end

    def Function_2_64F(): pass

    label("Function_2_64F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x109, 14250, 6000, -2420, 180)
    SetChrPos(0x10F, 13310, 6000, -1330, 180)
    SetChrPos(0x107, 15140, 6000, -1550, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(13750, 6000, -880, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(221, 0)

    def lambda_706():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_706)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 14180, 6000, -1600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_777():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_777)

    def lambda_789():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_789)

    def lambda_79B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_79B)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    def lambda_7C6():
        OP_6D(13300, 6000, -4850, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C6)

    def lambda_7DE():
        OP_8E(0xFE, 0x36D8, 0x1770, 0xFFFFE728, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DE)
    Sleep(300)

    def lambda_7FE():
        OP_8E(0xFE, 0x326E, 0x1770, 0xFFFFEC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7FE)
    Sleep(300)

    def lambda_81E():
        OP_8E(0xFE, 0x398A, 0x1770, 0xFFFFEB56, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_81E)
    WaitChrThread(0x109, 0x0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    WaitChrThread(0x10F, 0x0)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    WaitChrThread(0x107, 0x0)
    OP_43(0x107, 0x0, 0x0, 0x5)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #0
        0x109,
        "#1067F#5PJust how long does this place go on for?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 225, 400)

    ChrTalk(    #1
        0x107,
        (
            "#063F#5PIt's so strange, too...\x02\x03",

            "The shadow towers were weird enough,\x01",
            "but even they made a lot more sense than\x01",
            "this does.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1444F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x107,
        "#064F#6PIs something wrong, Ries?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 315, 400)
    Sleep(300)

    ChrTalk(    #4
        0x109,
        "#1079F#6PWhat'd you go all quiet for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1440F#5PWell...I was just wondering what that is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1064F#6PWhat what is?\x02",
    )

    CloseMessageWindow()

    def lambda_A34():
        OP_6D(180, 2950, -41080, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A34)

    def lambda_A4C():
        OP_67(0, 9940, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A4C)

    def lambda_A64():
        OP_6B(3820, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A64)

    def lambda_A74():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A74)

    def lambda_A84():
        OP_6E(437, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_A84)

    def lambda_A94():
        OP_8C(0x109, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A94)
    Sleep(100)
    OP_8C(0x107, 225, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 7240, 6000, -8350, 225)
    SetChrPos(0x10F, 8280, 6000, -7480, 225)
    SetChrPos(0x107, 8630, 6000, -9100, 225)

    ChrTalk(    #7
        0x109,
        "#1079F#4S...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x107,
        (
            "#065FWh-Wh-Wha...?\x02\x03",

            "What's the Arseille doing here?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(5890, 6000, -9350, 0)
    OP_67(0, 9610, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(255000, 0)
    OP_6E(363, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #9
        0x10F,
        "#1444F#6PYou recognize this ship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1067F#5PUh-huh... It belongs to the royal family of Liberl.\x02\x03",

            "We used it to get on top of that floating city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#6PInteresting...\x02\x03",

            "#1440FDo you have any idea how something like that\x01",
            "could've possibly have ended up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x107,
        "#063F#6PMaybe it was sent here the same way we were?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#5PI don't think we'll get anywhere speculating.\x01",
            "Could've come in our way. Could've come in\x01",
            "some other way. We just don't know.\x02\x03",

            "#1063FThe best thing for us to do now is to see what\x01",
            "the guys inside have to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2610)
    OP_28(0x29, 0x1, 0x100)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_64F end

    def Function_3_DBA(): pass

    label("Function_3_DBA")

    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_3_DBA end

    def Function_4_DE4(): pass

    label("Function_4_DE4")

    Sleep(300)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_4_DE4 end

    def Function_5_DFD(): pass

    label("Function_5_DFD")

    Sleep(300)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_5_DFD end

    def Function_6_E22(): pass

    label("Function_6_E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 1)), scpexpr(EXPR_END)), "loc_E2A")
    Return()

    label("loc_E2A")

    EventBegin(0x0)
    OP_8C(0x0, 180, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_EB1")

    label("loc_E5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E89")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_EB1")

    label("loc_E89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB1")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_EB1")


    def lambda_EB7():
        OP_6D(13130, -6000, -86940, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EB7)

    def lambda_ECF():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_ECF)

    def lambda_EE7():
        OP_6B(3900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EE7)

    def lambda_EF7():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_EF7)

    def lambda_F07():
        OP_6E(210, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_F07)

    def lambda_F17():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_F17)
    OP_8C(0x2, 180, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 14140, -6000, -75560, 180)
    SetChrPos(0x10F, 14740, -6000, -74930, 180)
    SetChrPos(0x107, 13390, -6000, -74550, 180)
    OP_43(0x109, 0x0, 0x0, 0x7)
    OP_43(0x10F, 0x0, 0x0, 0x8)
    OP_43(0x107, 0x0, 0x0, 0x9)
    Sleep(4000)

    def lambda_F7E():
        OP_6D(14830, -6000, -87100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F7E)

    def lambda_F96():
        OP_67(0, 5550, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F96)

    def lambda_FAE():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_FAE)

    def lambda_FBE():
        OP_6E(230, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_FBE)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #14
        0x109,
        "#1079F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x107,
        (
            "#560F#11PThis is like that monument in the area\x01",
            "we started in.\x02\x03",

            "Though it's not glowing like that one is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#1446F#12PThe one in that garden had no glow in\x01",
            "the beginning, either.\x02\x03",

            "#1440FKevin, do you want to give it a try?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        "#1060F#5PI was just thinking the same thing.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1117():
        OP_6D(14000, -6000, -87100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1117)

    def lambda_112F():
        OP_8E(0xFE, 0x3DE0, 0xFFFFE890, 0xFFFEA714, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_112F)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    LoadEffect(0x1, "map\\mp252_01.eff")
    PlayEffect(0x1, 0x0, 0x109, 0, 1280, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x90, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(300)

    ChrTalk(    #18
        0x107,
        "#064F#11POooh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1447F#12PI suspected as much.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    def lambda_12D7():
        OP_6D(15720, -6000, -86900, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12D7)
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #20
        0x109,
        (
            "#1065F#5PWhen we activated the first monument, it said,\x01",
            "'Release my brethren...'\x02\x03",

            "#1060FI guess now we know what it meant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        (
            "#560F#11PThen...\x02\x03",

            "Then do you think this monument might have\x01",
            "the same power as the other one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1060F#5PMost likely.\x02\x03",

            "It should come in handy, at least.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05Inspecting monuments scattered around\x01",
            "throughout the game allows you to use\x01",
            "the cube to restore their power.\x02\x03",

            "Much like the one in the base area,\x01",
            "you can use these to restore HP/EP,\x01",
            "buy equipment, and make quartz.\x02\x03",

            "They also function as checkpoints,\x01",
            "allowing you to warp to them using\x01",
            "the cube.\x02\x03",

            "In addition, any new items available\x01",
            "will be added to the base monument's\x01",
            "stock as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x2611)
    OP_A2(0x2584)
    OP_AA(256)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_E22 end

    def Function_7_15E4(): pass

    label("Function_7_15E4")

    OP_8E(0xFE, 0x41FA, 0xFFFFE890, 0xFFFEA584, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_15E4 end

    def Function_8_1600(): pass

    label("Function_8_1600")

    Sleep(200)
    OP_8E(0xFE, 0x3D04, 0xFFFFE890, 0xFFFECD52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4722, 0xFFFFE890, 0xFFFEA688, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_1600 end

    def Function_9_1635(): pass

    label("Function_9_1635")

    Sleep(600)
    OP_8E(0xFE, 0x41A0, 0xFFFFE890, 0xFFFEAC5A, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_9_1635 end

    def Function_10_1656(): pass

    label("Function_10_1656")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13730, -21000, -17890, 180)
    SetChrPos(0x10F, -14740, -21000, -17070, 180)
    SetChrPos(0x107, -12800, -21000, -17100, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-13870, -21000, -16930, 0)
    OP_67(0, 8820, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(315000, 0)
    OP_6E(249, 0)

    def lambda_16F9():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16F9)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -13770, -21000, -17100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_176A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_176A)

    def lambda_177C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_177C)

    def lambda_178E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_178E)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    Sleep(800)

    def lambda_17B4():
        OP_6D(-18430, -21500, -25500, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17B4)

    def lambda_17CC():
        OP_67(0, 9750, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17CC)

    def lambda_17E4():
        OP_6B(6090, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_17E4)

    def lambda_17F4():
        OP_6C(315000, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_17F4)

    def lambda_1804():
        OP_6E(348, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1804)

    def lambda_1814():
        OP_8E(0xFE, 0xFFFFCA86, 0xFFFFADF8, 0xFFFFAC40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1814)
    Sleep(300)

    def lambda_1834():
        OP_8E(0xFE, 0xFFFFC464, 0xFFFFADF8, 0xFFFFB15E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1834)
    Sleep(300)

    def lambda_1854():
        OP_8E(0xFE, 0xFFFFCCAC, 0xFFFFADF8, 0xFFFFB0A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1854)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1893")
    OP_82(0x94, 0x0)
    Jump("loc_1896")

    label("loc_1893")

    OP_82(0x95, 0x0)

    label("loc_1896")

    OP_6D(-45080, -23200, -19600, 0)
    OP_67(0, 2150, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(322000, 0)
    OP_6E(453, 0)

    def lambda_18D9():
        OP_6D(-23280, -23750, -23050, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18D9)

    def lambda_18F1():
        OP_67(0, 3010, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18F1)

    def lambda_1909():
        OP_6B(6800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1909)

    def lambda_1919():
        OP_6C(302000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1919)

    def lambda_1929():
        OP_6E(456, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1929)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x2)
    Fade(500)
    OP_44(0x109, 0x2)
    OP_44(0x10F, 0x1)
    OP_6D(-14340, -21000, -20010, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(3530, 0)
    OP_6C(315000, 0)
    OP_6E(249, 0)
    OP_D0(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D3")
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1A08")

    label("loc_19D3")

    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1A08")

    OP_0D()
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        "#1442F#5PWhat a beautiful airship...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #25
        0x107,
        (
            "#061F#6PHeehee. It's not just pretty, either.\x01",
            "It's got really high specs, too!\x02\x03",

            "#560FLast I heard, its top speed was raised\x01",
            "to 3,600 SPH.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #26
        0x10F,
        "#1444F#5P3,600 SPH? That's even faster than a Merkabah.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x107,
        "#064F#6PWhat's a Merkabah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1840F#6POh, it's a kind of airship the church uses.\x02\x03",

            "#1065F#6PAnyway, never mind that now. Something's up\x01",
            "here.\x02\x03",

            "#1063FIt doesn't look like there's anyone inside at all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C0E():
        OP_8C(0x107, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1C0E)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #29
        0x107,
        (
            "#063F#5PY-Yeah. You're right...\x02\x03",

            "And the orbal engines don't seem to be on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10F,
        "#1443F#5PWe ought to be on guard inside.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2612)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_1656 end

    def Function_11_1CB1(): pass

    label("Function_11_1CB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    SetChrFlags(0x107, 0x80)
    OP_6D(13090, -6000, -88500, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(231000, 0)
    OP_6E(300, 0)
    FadeToBright(2000, 0)

    def lambda_1D18():
        OP_6D(14080, -3250, -97550, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D18)

    def lambda_1D30():
        OP_67(0, 3490, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D30)

    def lambda_1D48():
        OP_6B(4200, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D48)

    def lambda_1D58():
        OP_6C(180000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1D58)

    def lambda_1D68():
        OP_6E(300, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1D68)
    WaitChrThread(0x109, 0x0)
    Fade(1000)

    def lambda_1D82():
        OP_6B(3600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D82)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_11_1CB1 end

    def Function_12_1DB7(): pass

    label("Function_12_1DB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -13730, -21000, -17890, 180)
    SetChrPos(0x10F, -14740, -21000, -17070, 180)
    SetChrPos(0x10E, -12800, -21000, -17100, 180)
    SetChrPos(0x107, -13790, -21000, -16210, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-14330, -21000, -16760, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(315000, 0)
    OP_6E(231, 0)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -13770, -21000, -17100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_1ED7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1ED7)

    def lambda_1EE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1EE9)

    def lambda_1EFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1EFB)

    def lambda_1F0D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1F0D)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x109, -13930, -21000, -17890, 180)
    SetChrPos(0x10F, -14940, -21000, -17070, 180)
    SetChrPos(0x10E, -12800, -21000, -17100, 180)
    SetChrPos(0x107, -13790, -21000, -16210, 180)
    OP_6D(-11900, -17250, -18810, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(5950, 0)
    OP_6C(215000, 0)
    OP_6E(429, 0)

    def lambda_1FBE():
        OP_67(0, 3210, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FBE)

    def lambda_1FD6():
        OP_6B(3720, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1FD6)
    OP_0D()
    SetChrChipByIndex(0x10E, 10)

    def lambda_1FEC():
        OP_8E(0xFE, 0xFFFFCAC2, 0xFFFFADF8, 0xFFFFAD9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1FEC)
    Sleep(300)

    def lambda_200C():
        OP_8E(0xFE, 0xFFFFC824, 0xFFFFADF8, 0xFFFFB26C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_200C)
    Sleep(200)

    def lambda_202C():
        OP_8E(0xFE, 0xFFFFC568, 0xFFFFADF8, 0xFFFFB55A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_202C)
    Sleep(300)

    def lambda_204C():
        OP_8E(0xFE, 0xFFFFCFA4, 0xFFFFADF8, 0xFFFFB71C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_204C)
    SetChrChipByIndex(0x10E, 65535)
    SetChrSubChip(0x10E, 0)
    WaitChrThread(0x10E, 0x0)
    OP_8C(0x10E, 225, 400)
    WaitChrThread(0x107, 0x0)
    OP_8C(0x107, 225, 400)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x3)
    OP_0D()
    Fade(500)
    SetChrPos(0x109, -14020, -21000, -20490, 180)
    SetChrPos(0x10F, -15580, -21000, -19920, 135)
    SetChrPos(0x10E, -14110, -21000, -21940, 180)
    SetChrPos(0x107, -13150, -21000, -19770, 180)
    OP_6D(-14420, -21000, -20820, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(3760, 0)
    OP_6C(315000, 0)
    OP_6E(234, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #31
        0x10E,
        "#178F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1067F#2PWhat do you want to do, Julia?\x02\x03",

            "Do you want to have a look around yourself\x01",
            "in case you notice something we didn't?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    ChrTalk(    #33
        0x10E,
        (
            "#170F#6PIf you wouldn't mind letting me, then I think\x01",
            "it would help set me at ease.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_12_1DB7 end

    def Function_13_2230(): pass

    label("Function_13_2230")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-11520, -21000, 16780, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(6280, 0)
    OP_6C(314000, 0)
    OP_6E(477, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)

    def lambda_2293():
        OP_6D(-20620, -21000, -28170, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2293)

    def lambda_22AB():
        OP_67(0, 8860, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_22AB)

    def lambda_22C3():
        OP_6B(6670, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22C3)

    def lambda_22D3():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_22D3)

    def lambda_22E3():
        OP_6E(471, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_22E3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_2302():
        OP_6D(-20620, -21000, -28170, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2302)

    def lambda_231A():
        OP_67(0, 8860, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_231A)

    def lambda_2332():
        OP_6B(5830, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2332)

    def lambda_2342():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2342)

    def lambda_2352():
        OP_6E(430, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2352)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x0)
    OP_A2(0x2506)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2230 end

    def Function_14_2383(): pass

    label("Function_14_2383")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2505")

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
        (0, "loc_241E"),
        (1, "loc_2499"),
        (2, "loc_24C7"),
        (SWITCH_DEFAULT, "loc_24F5"),
    )


    label("loc_241E")

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
    OP_1D(0xDC)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2502")

    label("loc_2499")

    OP_A9(0x14)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #35
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2502")

    label("loc_24C7")

    OP_A9(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2502")

    label("loc_24F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2502")

    label("loc_2502")

    Jump("loc_23C2")

    label("loc_2505")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_14_2383 end

    def Function_15_2526(): pass

    label("Function_15_2526")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_260E")
    OP_43(0x0, 0x1, 0x0, 0x13)
    OP_43(0x1, 0x1, 0x0, 0x12)
    OP_43(0x2, 0x1, 0x0, 0x11)
    OP_43(0x3, 0x1, 0x0, 0x10)
    WaitChrThread(0x3, 0x1)
    Jump("loc_2628")

    label("loc_260E")

    OP_43(0x0, 0x1, 0x0, 0x13)
    OP_43(0x1, 0x1, 0x0, 0x12)
    OP_43(0x2, 0x1, 0x0, 0x11)
    WaitChrThread(0x2, 0x1)

    label("loc_2628")

    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_15_2526 end

    def Function_16_262E(): pass

    label("Function_16_262E")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_262E end

    def Function_17_2686(): pass

    label("Function_17_2686")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_2686 end

    def Function_18_26D0(): pass

    label("Function_18_26D0")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_26D0 end

    def Function_19_270C(): pass

    label("Function_19_270C")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_270C end

    def Function_20_273A(): pass

    label("Function_20_273A")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_2822")
    OP_43(0x0, 0x1, 0x0, 0x18)
    OP_43(0x1, 0x1, 0x0, 0x17)
    OP_43(0x2, 0x1, 0x0, 0x16)
    OP_43(0x3, 0x1, 0x0, 0x15)
    WaitChrThread(0x3, 0x1)
    Jump("loc_283C")

    label("loc_2822")

    OP_43(0x0, 0x1, 0x0, 0x18)
    OP_43(0x1, 0x1, 0x0, 0x17)
    OP_43(0x2, 0x1, 0x0, 0x16)
    WaitChrThread(0x2, 0x1)

    label("loc_283C")

    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_273A end

    def Function_21_2842(): pass

    label("Function_21_2842")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_2842 end

    def Function_22_289A(): pass

    label("Function_22_289A")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_289A end

    def Function_23_28E4(): pass

    label("Function_23_28E4")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_28E4 end

    def Function_24_2920(): pass

    label("Function_24_2920")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_24_2920 end

    def Function_25_294E(): pass

    label("Function_25_294E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295F")
    Call(0, 2)
    Return()

    label("loc_295F")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 14250, 6000, -2420, 180)
    SetChrPos(0x1, 13310, 6000, -1330, 180)
    SetChrPos(0x2, 15140, 6000, -1550, 180)
    SetChrPos(0x3, 14290, 6000, -580, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 14180, 6000, -1600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_25_294E end

    def Function_26_2A3D(): pass

    label("Function_26_2A3D")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -13030, -2000, -87950, 90)
    SetChrPos(0x1, -13980, -2000, -88860, 90)
    SetChrPos(0x2, -14000, -2000, -87130, 90)
    SetChrPos(0x3, -14940, -2000, -87940, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -14030, -2000, -87980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_26_2A3D end

    def Function_27_2AF0(): pass

    label("Function_27_2AF0")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -42450, -12500, -51610, 315)
    SetChrPos(0x1, -41180, -12500, -51570, 315)
    SetChrPos(0x2, -42440, -12500, -52820, 315)
    SetChrPos(0x3, -41050, -12500, -53000, 315)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -41810, -12500, -52250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_27_2AF0 end

    def Function_28_2BA3(): pass

    label("Function_28_2BA3")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -47410, -12500, -46550, 135)
    SetChrPos(0x1, -48750, -12500, -46550, 135)
    SetChrPos(0x2, -47500, -12500, -45290, 135)
    SetChrPos(0x3, -48840, -12500, -45110, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -48090, -12500, -45900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_28_2BA3 end

    def Function_29_2C56(): pass

    label("Function_29_2C56")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -32490, -34000, 52160, 180)
    SetChrPos(0x1, -33430, -34000, 53080, 180)
    SetChrPos(0x2, -31510, -34000, 52990, 180)
    SetChrPos(0x3, -32549, -34000, 53930, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -32530, -34000, 53080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_29_2C56 end

    def Function_30_2D09(): pass

    label("Function_30_2D09")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 41070, -10000, -88080, 270)
    SetChrPos(0x1, 41880, -10000, -87160, 270)
    SetChrPos(0x2, 42110, -10000, -88980, 270)
    SetChrPos(0x3, 42920, -10000, -88010, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41920, -10000, -87970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_30_2D09 end

    def Function_31_2DBC(): pass

    label("Function_31_2DBC")

    OP_DE(0x0, 0x6, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 40130, -24000, -21130, 0)
    SetChrPos(0x1, 41040, -24000, -22250, 0)
    SetChrPos(0x2, 39350, -24000, -22180, 0)
    SetChrPos(0x3, 40210, -24000, -23250, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 40140, -24000, -22120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_31_2DBC end

    def Function_32_2E6F(): pass

    label("Function_32_2E6F")

    OP_DE(0x0, 0x7, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 24860, -16000, 13910, 90)
    SetChrPos(0x1, 23970, -16000, 12960, 90)
    SetChrPos(0x2, 23870, -16000, 14790, 90)
    SetChrPos(0x3, 22960, -16000, 13980, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 24050, -16000, 14020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_32_2E6F end

    def Function_33_2F22(): pass

    label("Function_33_2F22")

    OP_DE(0x0, 0x8, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 5020, -12500, 24040, 315)
    SetChrPos(0x1, 6300, -12500, 24020, 315)
    SetChrPos(0x2, 5070, -12500, 22630, 315)
    SetChrPos(0x3, 6460, -12500, 22700, 315)
    OP_69(0x0, 0x0)
    OP_6C(303000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 5650, -12500, 23280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_33_2F22 end

    def Function_34_2FDE(): pass

    label("Function_34_2FDE")

    OP_DE(0x0, 0x9, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 40, -12500, 28880, 135)
    SetChrPos(0x1, -1140, -12500, 28860, 135)
    SetChrPos(0x2, -70, -12500, 30160, 135)
    SetChrPos(0x3, -1260, -12500, 30080, 135)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -460, -12500, 29370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_34_2FDE end

    def Function_35_3091(): pass

    label("Function_35_3091")

    OP_DE(0x0, 0xA, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -24840, -4000, -6060, 270)
    SetChrPos(0x1, -23860, -4000, -5070, 270)
    SetChrPos(0x2, -23660, -4000, -7010, 270)
    SetChrPos(0x3, -22630, -4000, -6070, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -23750, -4000, -5960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_35_3091 end

    def Function_36_3144(): pass

    label("Function_36_3144")

    OP_DE(0x0, 0xB, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -39970, -8000, -27080, 0)
    SetChrPos(0x1, -38910, -8000, -28020, 0)
    SetChrPos(0x2, -40710, -8000, -28050, 0)
    SetChrPos(0x3, -39600, -8000, -29080, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -39940, -8000, -27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_36_3144 end

    def Function_37_31F7(): pass

    label("Function_37_31F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3206")
    Jump("loc_322B")

    label("loc_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_321A")
    Call(0, 12)
    Return()

    label("loc_321A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322B")
    Call(0, 10)
    Return()

    label("loc_322B")

    OP_DE(0x0, 0xC, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -13730, -21000, -17890, 180)
    SetChrPos(0x1, -14740, -21000, -17070, 180)
    SetChrPos(0x2, -12800, -21000, -17100, 180)
    SetChrPos(0x3, -13790, -21000, -16210, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -13770, -21000, -17100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    Return()

    # Function_37_31F7 end

    def Function_38_32DE(): pass

    label("Function_38_32DE")

    OP_DE(0x0, 0xF, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 14070, -10000, -114980, 0)
    SetChrPos(0x1, 15120, -10000, -116030, 0)
    SetChrPos(0x2, 13300, -10000, -116100, 0)
    SetChrPos(0x3, 14330, -10000, -116940, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 14180, -10000, -116030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 53)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_38_32DE end

    def Function_39_33BC(): pass

    label("Function_39_33BC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x3, 14250, 6000, -2420, 0)
    SetChrPos(0x2, 13310, 6000, -1330, 0)
    SetChrPos(0x1, 15140, 6000, -1550, 0)
    SetChrPos(0x0, 14290, 6000, -580, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 14180, 6000, -1600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7001   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_39_33BC end

    def Function_40_347F(): pass

    label("Function_40_347F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -13030, -2000, -87950, 270)
    SetChrPos(0x2, -13980, -2000, -88860, 270)
    SetChrPos(0x1, -14000, -2000, -87130, 270)
    SetChrPos(0x0, -14940, -2000, -87940, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -14030, -2000, -87980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_40_347F end

    def Function_41_353B(): pass

    label("Function_41_353B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -42450, -12500, -51610, 135)
    SetChrPos(0x2, -41180, -12500, -51570, 135)
    SetChrPos(0x1, -42440, -12500, -52820, 135)
    SetChrPos(0x0, -41050, -12500, -53000, 135)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -41810, -12500, -52250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_41_353B end

    def Function_42_35F7(): pass

    label("Function_42_35F7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -47410, -12500, -46550, 315)
    SetChrPos(0x2, -48750, -12500, -46550, 315)
    SetChrPos(0x1, -47500, -12500, -45290, 315)
    SetChrPos(0x0, -48840, -12500, -45110, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -48090, -12500, -45900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_42_35F7 end

    def Function_43_36B3(): pass

    label("Function_43_36B3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -32490, -34000, 52160, 0)
    SetChrPos(0x2, -33430, -34000, 53080, 0)
    SetChrPos(0x1, -31510, -34000, 52990, 0)
    SetChrPos(0x0, -32549, -34000, 53930, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -32530, -34000, 53080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_43_36B3 end

    def Function_44_376F(): pass

    label("Function_44_376F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 41070, -10000, -88080, 90)
    SetChrPos(0x2, 41880, -10000, -87160, 90)
    SetChrPos(0x1, 42110, -10000, -88980, 90)
    SetChrPos(0x0, 42920, -10000, -88010, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41920, -10000, -87970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_44_376F end

    def Function_45_382B(): pass

    label("Function_45_382B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 40130, -24000, -21130, 180)
    SetChrPos(0x2, 41040, -24000, -22250, 180)
    SetChrPos(0x1, 39350, -24000, -22180, 180)
    SetChrPos(0x0, 40210, -24000, -23250, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 40140, -24000, -22120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_45_382B end

    def Function_46_38E7(): pass

    label("Function_46_38E7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 24860, -16000, 13910, 270)
    SetChrPos(0x2, 23970, -16000, 12960, 270)
    SetChrPos(0x1, 23870, -16000, 14790, 270)
    SetChrPos(0x0, 22960, -16000, 13980, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 24050, -16000, 14020, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_46_38E7 end

    def Function_47_39A3(): pass

    label("Function_47_39A3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 5020, -12500, 24040, 135)
    SetChrPos(0x2, 6300, -12500, 24020, 135)
    SetChrPos(0x1, 5070, -12500, 22630, 135)
    SetChrPos(0x0, 6460, -12500, 22700, 135)
    OP_69(0x0, 0x0)
    OP_6C(303000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 5650, -12500, 23280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_47_39A3 end

    def Function_48_3A68(): pass

    label("Function_48_3A68")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 40, -12500, 28880, 315)
    SetChrPos(0x2, -1140, -12500, 28860, 315)
    SetChrPos(0x1, -70, -12500, 30160, 315)
    SetChrPos(0x0, -1260, -12500, 30080, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -460, -12500, 29370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_48_3A68 end

    def Function_49_3B24(): pass

    label("Function_49_3B24")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -24840, -4000, -6060, 90)
    SetChrPos(0x2, -23860, -4000, -5070, 90)
    SetChrPos(0x1, -23660, -4000, -7010, 90)
    SetChrPos(0x0, -22630, -4000, -6070, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -23750, -4000, -5960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_49_3B24 end

    def Function_50_3BE0(): pass

    label("Function_50_3BE0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -39970, -8000, -27080, 180)
    SetChrPos(0x2, -38910, -8000, -28020, 180)
    SetChrPos(0x1, -40710, -8000, -28050, 180)
    SetChrPos(0x0, -39600, -8000, -29080, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -39940, -8000, -27950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_50_3BE0 end

    def Function_51_3C9C(): pass

    label("Function_51_3C9C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -13730, -21000, -17990, 0)
    SetChrPos(0x2, -14740, -21000, -17170, 0)
    SetChrPos(0x1, -12800, -21000, -17200, 0)
    SetChrPos(0x0, -13790, -21000, -16309, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -13770, -21000, -17100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7002   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_51_3C9C end

    def Function_52_3D58(): pass

    label("Function_52_3D58")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 14070, -10000, -114980, 180)
    SetChrPos(0x2, 15120, -10000, -116030, 180)
    SetChrPos(0x1, 13300, -10000, -116100, 180)
    SetChrPos(0x0, 14330, -10000, -116940, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 14180, -10000, -116030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 54)
    NewScene("ED6_DT21/M7003   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_52_3D58 end

    def Function_53_3E14(): pass

    label("Function_53_3E14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E3D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E31():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3E31)

    label("loc_3E3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E66")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E5A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3E5A)

    label("loc_3E66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E8F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3E83)

    label("loc_3E8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EB8")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3EAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3EAC)

    label("loc_3EB8")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EE4")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3EE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EFB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3EFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F12")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3F12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F29")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3F29")

    Return()

    # Function_53_3E14 end

    def Function_54_3F2A(): pass

    label("Function_54_3F2A")


    def lambda_3F30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F30)

    def lambda_3F42():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F42)

    def lambda_3F54():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F54)

    def lambda_3F66():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F66)
    Sleep(1000)
    Return()

    # Function_54_3F2A end

    def Function_55_3F78(): pass

    label("Function_55_3F78")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
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

    # Function_55_3F78 end

    def Function_56_3FD1(): pass

    label("Function_56_3FD1")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -33230, -42000, 11430, 270)
    SetChrPos(0x1, -33200, -42000, 10050, 270)
    SetChrPos(0x2, -31470, -42000, 11450, 270)
    SetChrPos(0x3, -31070, -42000, 9670, 270)
    OP_6D(-35320, -42000, 10750, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A7")
    OP_28(0x24, 0x4, 0x2)
    OP_82(0x94, 0x2)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_40A7")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05#40WBring to me the only girl in a\x01",
            "band who takes to the skies.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4174")
    Call(0, 55)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4171")
    Call(0, 57)

    label("loc_4171")

    Jump("loc_4174")

    label("loc_4174")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_56_3FD1 end

    def Function_57_4180(): pass

    label("Function_57_4180")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)

    def lambda_41E9():
        OP_6B(3750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_41E9)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x1, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_57_4180 end

    def Function_58_4236(): pass

    label("Function_58_4236")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -33230, -42000, 11430, 270)
    SetChrPos(0x1, -33200, -42000, 10050, 270)
    SetChrPos(0x2, -31470, -42000, 11450, 270)
    SetChrPos(0x3, -31070, -42000, 9670, 270)
    OP_6D(-35320, -42000, 10750, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_58_4236 end

    def Function_59_42E1(): pass

    label("Function_59_42E1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x198, 1)"), scpexpr(EXPR_END)), "loc_434F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05Found \x1F\x98\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2688)
    Jump("loc_43B7")

    label("loc_434F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05Found \x1F\x98\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x98\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_43B7")

    Jump("loc_4446")

    label("loc_43BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "\x07\x05Don't you hate it when someone opens your door and doesn't close it\x01",
            "when they leave? *stares menacingly*\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA4, 0x0)

    label("loc_4446")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_59_42E1 end

    def Function_60_4454(): pass

    label("Function_60_4454")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_44C2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05Found \x1F\xF5\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2689)
    Jump("loc_452A")

    label("loc_44C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "\x07\x05Found \x1F\xF5\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF5\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_452A")

    Jump("loc_4627")

    label("loc_452D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x07\x05[27/36] With one particularly obnoxious clink, she set down her utensils\x01",
            "then glared at him with an uncomfortable firmness that would have a\x01",
            "lesser man avert his eyes in shame. She bit her bottom lip before asking:\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA5, 0x0)

    label("loc_4627")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_60_4454 end

    def Function_61_4635(): pass

    label("Function_61_4635")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_46A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05Found \x1F\x00\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268A)
    Jump("loc_470B")

    label("loc_46A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x07\x05Found \x1F\x00\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x00\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_470B")

    Jump("loc_4781")

    label("loc_470E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05Why is Deen called the Spinach Fiend, anyway? Does he just really like\x01",
            "Spinach?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA6, 0x0)

    label("loc_4781")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_61_4635 end

    def Function_62_478F(): pass

    label("Function_62_478F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4868")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_47FD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x05Found \x1F\x64\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268B)
    Jump("loc_4865")

    label("loc_47FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "\x07\x05Found \x1F\x64\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x64\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_4865")

    Jump("loc_48D6")

    label("loc_4868")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05Do you really have nothing better to do than open all of us a second time?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA7, 0x0)

    label("loc_48D6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_62_478F end

    def Function_63_48E4(): pass

    label("Function_63_48E4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x166, 1)"), scpexpr(EXPR_END)), "loc_4952")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x05Found \x1F\x66\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268C)
    Jump("loc_49BA")

    label("loc_4952")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "\x07\x05Found \x1F\x66\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x66\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_49BA")

    Jump("loc_4AAA")

    label("loc_49BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        (
            "\x07\x05[11/36] The face greeted customers with an aged brick that had long\x01",
            "eroded to the point of holes; the cracked windows, taped for stability\x01",
            "and adorned with cobwebs and insect droppings, were repugnant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA8, 0x0)

    label("loc_4AAA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_63_48E4 end

    def Function_64_4AB8(): pass

    label("Function_64_4AB8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B91")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x66, 1)"), scpexpr(EXPR_END)), "loc_4B26")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05Found \x1F\x66\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268D)
    Jump("loc_4B8E")

    label("loc_4B26")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "\x07\x05Found \x1F\x66\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x66\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_4B8E")

    Jump("loc_4BFA")

    label("loc_4B91")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05You took all my loot. How am I supposed to pay my room and board now?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA9, 0x0)

    label("loc_4BFA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_64_4AB8 end

    SaveToFile()

Try(main)
