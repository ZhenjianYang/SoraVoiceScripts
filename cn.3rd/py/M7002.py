from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        "Function_3_D4C",          # 03, 3
        "Function_4_D76",          # 04, 4
        "Function_5_D8F",          # 05, 5
        "Function_6_DB4",          # 06, 6
        "Function_7_14B6",         # 07, 7
        "Function_8_14D2",         # 08, 8
        "Function_9_1507",         # 09, 9
        "Function_10_1528",        # 0A, 10
        "Function_11_1B45",        # 0B, 11
        "Function_12_1C4B",        # 0C, 12
        "Function_13_2096",        # 0D, 13
        "Function_14_21E9",        # 0E, 14
        "Function_15_23A2",        # 0F, 15
        "Function_16_24AA",        # 10, 16
        "Function_17_2502",        # 11, 17
        "Function_18_254C",        # 12, 18
        "Function_19_2588",        # 13, 19
        "Function_20_25B6",        # 14, 20
        "Function_21_26BE",        # 15, 21
        "Function_22_2716",        # 16, 22
        "Function_23_2760",        # 17, 23
        "Function_24_279C",        # 18, 24
        "Function_25_27CA",        # 19, 25
        "Function_26_28B9",        # 1A, 26
        "Function_27_296C",        # 1B, 27
        "Function_28_2A1F",        # 1C, 28
        "Function_29_2AD2",        # 1D, 29
        "Function_30_2B85",        # 1E, 30
        "Function_31_2C38",        # 1F, 31
        "Function_32_2CEB",        # 20, 32
        "Function_33_2D9E",        # 21, 33
        "Function_34_2E5A",        # 22, 34
        "Function_35_2F0D",        # 23, 35
        "Function_36_2FC0",        # 24, 36
        "Function_37_3073",        # 25, 37
        "Function_38_315A",        # 26, 38
        "Function_39_3238",        # 27, 39
        "Function_40_32FB",        # 28, 40
        "Function_41_33B7",        # 29, 41
        "Function_42_3473",        # 2A, 42
        "Function_43_352F",        # 2B, 43
        "Function_44_35EB",        # 2C, 44
        "Function_45_36A7",        # 2D, 45
        "Function_46_3763",        # 2E, 46
        "Function_47_381F",        # 2F, 47
        "Function_48_38E4",        # 30, 48
        "Function_49_39A0",        # 31, 49
        "Function_50_3A5C",        # 32, 50
        "Function_51_3B18",        # 33, 51
        "Function_52_3BD4",        # 34, 52
        "Function_53_3C90",        # 35, 53
        "Function_54_3DA6",        # 36, 54
        "Function_55_3DF4",        # 37, 55
        "Function_56_3E68",        # 38, 56
        "Function_57_4009",        # 39, 57
        "Function_58_40BF",        # 3A, 58
        "Function_59_416A",        # 3B, 59
        "Function_60_428A",        # 3C, 60
        "Function_61_43AA",        # 3D, 61
        "Function_62_44CA",        # 3E, 62
        "Function_63_45EA",        # 3F, 63
        "Function_64_470A",        # 40, 64
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
        (
            "#1067F#5P唔……\x01",
            "好像还有后续啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 225, 400)

    ChrTalk(    #1
        0x107,
        (
            "#063F#5P话说回来……\x01",
            "这真是不可思议的地方呢。\x02\x03",

            "『四轮之塔』里面的空间\x01",
            "还能够让人理解……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1444F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x107,
        "#064F#6P莉丝姐姐？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 315, 400)
    Sleep(300)

    ChrTalk(    #4
        0x109,
        "#1079F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1440F#5P……嗯。\x01",
            "我在想，那是什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1064F#6P哦……\x02",
    )

    CloseMessageWindow()

    def lambda_A19():
        OP_6D(180, 2950, -41080, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A19)

    def lambda_A31():
        OP_67(0, 9940, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A31)

    def lambda_A49():
        OP_6B(3820, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A49)

    def lambda_A59():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A59)

    def lambda_A69():
        OP_6E(437, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_A69)

    def lambda_A79():
        OP_8C(0x109, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A79)
    Sleep(100)
    OP_8C(0x107, 225, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 7240, 6000, -8350, 225)
    SetChrPos(0x10F, 8280, 6000, -7480, 225)
    SetChrPos(0x107, 8630, 6000, -9100, 225)

    ChrTalk(    #7
        0x109,
        "#1079F#4S！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x107,
        (
            "#065F为、为、为……\x02\x03",

            "为什么埃尔赛尤号会！？\x02",
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
        "#1444F#6P……你知道这艘飞艇？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1067F#5P啊，是啊……\x01",
            "是利贝尔王家的飞艇，\x01",
            "『埃尔赛尤』号。\x02\x03",

            "在潜入那个浮游都市的时候\x01",
            "真是多亏了它呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#6P原来如此……\x02\x03",

            "#1440F……但是，\x01",
            "为什么那艘王家的飞艇会在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x107,
        (
            "#063F#6P是、是不是\x01",
            "跟我们一样被卷到\x01",
            "这个地方来的呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#5P或者是以和我们\x01",
            "不同的形式被弄进来的……\x02\x03",

            "#1063F……无论如何，\x01",
            "看来需要先想办法\x01",
            "到达那里再调查看看了。\x02",
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

    def Function_3_D4C(): pass

    label("Function_3_D4C")

    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Return()

    # Function_3_D4C end

    def Function_4_D76(): pass

    label("Function_4_D76")

    Sleep(300)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_4_D76 end

    def Function_5_D8F(): pass

    label("Function_5_D8F")

    Sleep(300)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_5_D8F end

    def Function_6_DB4(): pass

    label("Function_6_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 1)), scpexpr(EXPR_END)), "loc_DBC")
    Return()

    label("loc_DBC")

    EventBegin(0x0)
    OP_8C(0x0, 180, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF0")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_E43")

    label("loc_DF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1B")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_E43")

    label("loc_E1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E43")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_E43")


    def lambda_E49():
        OP_6D(13130, -6000, -86940, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E49)

    def lambda_E61():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E61)

    def lambda_E79():
        OP_6B(3900, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E79)

    def lambda_E89():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_E89)

    def lambda_E99():
        OP_6E(210, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_E99)

    def lambda_EA9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_EA9)
    OP_8C(0x2, 180, 400)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x109, 14140, -6000, -75560, 180)
    SetChrPos(0x10F, 14740, -6000, -74930, 180)
    SetChrPos(0x107, 13390, -6000, -74550, 180)
    OP_43(0x109, 0x0, 0x0, 0x7)
    OP_43(0x10F, 0x0, 0x0, 0x8)
    OP_43(0x107, 0x0, 0x0, 0x9)
    Sleep(4000)

    def lambda_F10():
        OP_6D(14830, -6000, -87100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F10)

    def lambda_F28():
        OP_67(0, 5550, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F28)

    def lambda_F40():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F40)

    def lambda_F50():
        OP_6E(230, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_F50)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #14
        0x109,
        "#1079F#6P这东西是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x107,
        (
            "#560F#11P和一开始那里的\x01",
            "大石碑很像呢。\x02\x03",

            "虽然不像那个一样\x01",
            "会发光……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#1446F#12P那个大石碑\x01",
            "最初也没有发光。\x02\x03",

            "#1440F……凯文。\x01",
            "试试看？\x02",
        )
    )

    Jump("loc_1046")

    label("loc_1046")

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1060F#5P啊啊，\x01",
            "我也正打算这么做呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1083():
        OP_6D(14000, -6000, -87100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1083)

    def lambda_109B():
        OP_8E(0xFE, 0x3DE0, 0xFFFFE890, 0xFFFEA714, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_109B)
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
        "#064F#11P哇哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1447F#12P不出所料，对吧。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    def lambda_1250():
        OP_6D(15720, -6000, -86900, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1250)
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #20
        0x109,
        (
            "#1065F#5P『解放吾等眷属』……\x02\x03",

            "#1060F那块石碑苏醒之时，\x01",
            "所说的就是这个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        (
            "#560F#11P嗯，这么说……\x02\x03",

            "这块石碑也拥有\x01",
            "同样的力量了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1060F#5P这个可能性很高。\x02\x03",

            "嗯，\x01",
            "探索时尽量利用它吧。\x02",
        )
    )

    Jump("loc_1368")

    label("loc_1368")

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05调查各地的『石碑』，\x01",
            "就能利用『方石』\x01",
            "使它们恢复力量。\x02\x03",

            "各地的石碑和据点的石碑一样，\x01",
            "可以回复ＨＰ和ＥＰ、购买武具，\x01",
            "以及制作结晶回路。\x02\x03",

            "而且，还可以作为\x01",
            "『方石』传送的目的地。\x02\x03",

            "此外，当在苏醒的石碑处\x01",
            "能够买到新物品的时候，\x01",
            "据点的石碑也会更新同样的物品。\x02",
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

    # Function_6_DB4 end

    def Function_7_14B6(): pass

    label("Function_7_14B6")

    OP_8E(0xFE, 0x41FA, 0xFFFFE890, 0xFFFEA584, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_14B6 end

    def Function_8_14D2(): pass

    label("Function_8_14D2")

    Sleep(200)
    OP_8E(0xFE, 0x3D04, 0xFFFFE890, 0xFFFECD52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4722, 0xFFFFE890, 0xFFFEA688, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_14D2 end

    def Function_9_1507(): pass

    label("Function_9_1507")

    Sleep(600)
    OP_8E(0xFE, 0x41A0, 0xFFFFE890, 0xFFFEAC5A, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_9_1507 end

    def Function_10_1528(): pass

    label("Function_10_1528")

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

    def lambda_15CB():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15CB)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -13770, -21000, -17100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_163C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_163C)

    def lambda_164E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_164E)

    def lambda_1660():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1660)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    Sleep(800)

    def lambda_1686():
        OP_6D(-18430, -21500, -25500, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1686)

    def lambda_169E():
        OP_67(0, 9750, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_169E)

    def lambda_16B6():
        OP_6B(6090, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_16B6)

    def lambda_16C6():
        OP_6C(315000, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_16C6)

    def lambda_16D6():
        OP_6E(348, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_16D6)

    def lambda_16E6():
        OP_8E(0xFE, 0xFFFFCA86, 0xFFFFADF8, 0xFFFFAC40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16E6)
    Sleep(300)

    def lambda_1706():
        OP_8E(0xFE, 0xFFFFC464, 0xFFFFADF8, 0xFFFFB15E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1706)
    Sleep(300)

    def lambda_1726():
        OP_8E(0xFE, 0xFFFFCCAC, 0xFFFFADF8, 0xFFFFB0A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1726)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1765")
    OP_82(0x94, 0x0)
    Jump("loc_1768")

    label("loc_1765")

    OP_82(0x95, 0x0)

    label("loc_1768")

    OP_6D(-45080, -23200, -19600, 0)
    OP_67(0, 2150, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(322000, 0)
    OP_6E(453, 0)

    def lambda_17AB():
        OP_6D(-23280, -23750, -23050, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17AB)

    def lambda_17C3():
        OP_67(0, 3010, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17C3)

    def lambda_17DB():
        OP_6B(6800, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17DB)

    def lambda_17EB():
        OP_6C(302000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_17EB)

    def lambda_17FB():
        OP_6E(456, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_17FB)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A5")
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_18DA")

    label("loc_18A5")

    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_18DA")

    OP_0D()
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        "#1442F#5P……好漂亮的飞艇啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #25
        0x107,
        (
            "#061F#6P嘿嘿……\x01",
            "不仅漂亮，\x01",
            "性能也很厉害哦。\x02\x03",

            "#560F听说最高速度\x01",
            "已经能够达到\x01",
            "时速３６００塞尔矩了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(300)

    ChrTalk(    #26
        0x10F,
        (
            "#1444F#5P３６００……\x01",
            "在『梅尔卡瓦』之上吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x107,
        "#064F#6P『梅尔卡瓦』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1840F#6P啊啊，是教会使用的飞行艇。\x02\x03",

            "#1065F#6P话说回来……\x01",
            "情况明显有点奇怪啊。\x02\x03",

            "#1063F好像没有人的气息似的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A9F():
        OP_8C(0x107, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1A9F)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #29
        0x107,
        (
            "#063F#5P是、是啊。\x02\x03",

            "看起来导力引擎\x01",
            "也不像在运作的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10F,
        (
            "#1443F#5P……如果要进去，\x01",
            "最好小心点呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2612)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_1528 end

    def Function_11_1B45(): pass

    label("Function_11_1B45")

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

    def lambda_1BAC():
        OP_6D(14080, -3250, -97550, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BAC)

    def lambda_1BC4():
        OP_67(0, 3490, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BC4)

    def lambda_1BDC():
        OP_6B(4200, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1BDC)

    def lambda_1BEC():
        OP_6C(180000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BEC)

    def lambda_1BFC():
        OP_6E(300, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1BFC)
    WaitChrThread(0x109, 0x0)
    Fade(1000)

    def lambda_1C16():
        OP_6B(3600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1C16)
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

    # Function_11_1B45 end

    def Function_12_1C4B(): pass

    label("Function_12_1C4B")

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

    def lambda_1D6B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D6B)

    def lambda_1D7D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1D7D)

    def lambda_1D8F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1D8F)

    def lambda_1DA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1DA1)
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

    def lambda_1E52():
        OP_67(0, 3210, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E52)

    def lambda_1E6A():
        OP_6B(3720, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1E6A)
    OP_0D()
    SetChrChipByIndex(0x10E, 10)

    def lambda_1E80():
        OP_8E(0xFE, 0xFFFFCAC2, 0xFFFFADF8, 0xFFFFAD9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1E80)
    Sleep(300)

    def lambda_1EA0():
        OP_8E(0xFE, 0xFFFFC824, 0xFFFFADF8, 0xFFFFB26C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EA0)
    Sleep(200)

    def lambda_1EC0():
        OP_8E(0xFE, 0xFFFFC568, 0xFFFFADF8, 0xFFFFB55A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1EC0)
    Sleep(300)

    def lambda_1EE0():
        OP_8E(0xFE, 0xFFFFCFA4, 0xFFFFADF8, 0xFFFFB71C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1EE0)
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
        "#178F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1067F#2P怎么办，尤莉亚小姐？\x02\x03",

            "以防万一，\x01",
            "要亲自确认一下舰内情况吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 0, 400)
    Sleep(300)

    ChrTalk(    #33
        0x10E,
        (
            "#170F#6P嗯……\x01",
            "可以的话，我希望能这么做。\x02",
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

    # Function_12_1C4B end

    def Function_13_2096(): pass

    label("Function_13_2096")

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

    def lambda_20F9():
        OP_6D(-20620, -21000, -28170, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_20F9)

    def lambda_2111():
        OP_67(0, 8860, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2111)

    def lambda_2129():
        OP_6B(6670, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2129)

    def lambda_2139():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2139)

    def lambda_2149():
        OP_6E(471, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2149)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_2168():
        OP_6D(-20620, -21000, -28170, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2168)

    def lambda_2180():
        OP_67(0, 8860, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2180)

    def lambda_2198():
        OP_6B(5830, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2198)

    def lambda_21A8():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_21A8)

    def lambda_21B8():
        OP_6E(430, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_21B8)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x0)
    OP_A2(0x2506)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2096 end

    def Function_14_21E9(): pass

    label("Function_14_21E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2216")

    label("loc_2216")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2229")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2381")

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

    Jump("loc_227B")

    label("loc_227B")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2298"),
        (1, "loc_2313"),
        (2, "loc_2342"),
        (SWITCH_DEFAULT, "loc_2371"),
    )


    label("loc_2298")

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
    OP_1D(0xDC)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_237E")

    label("loc_2313")

    OP_A9(0x14)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #35
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_233F")

    label("loc_233F")

    Jump("loc_237E")

    label("loc_2342")

    OP_A9(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #36
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_236E")

    label("loc_236E")

    Jump("loc_237E")

    label("loc_2371")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_237E")

    label("loc_237E")

    Jump("loc_2229")

    label("loc_2381")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_14_21E9 end

    def Function_15_23A2(): pass

    label("Function_15_23A2")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_248A")
    OP_43(0x0, 0x1, 0x0, 0x13)
    OP_43(0x1, 0x1, 0x0, 0x12)
    OP_43(0x2, 0x1, 0x0, 0x11)
    OP_43(0x3, 0x1, 0x0, 0x10)
    WaitChrThread(0x3, 0x1)
    Jump("loc_24A4")

    label("loc_248A")

    OP_43(0x0, 0x1, 0x0, 0x13)
    OP_43(0x1, 0x1, 0x0, 0x12)
    OP_43(0x2, 0x1, 0x0, 0x11)
    WaitChrThread(0x2, 0x1)

    label("loc_24A4")

    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_15_23A2 end

    def Function_16_24AA(): pass

    label("Function_16_24AA")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_24AA end

    def Function_17_2502(): pass

    label("Function_17_2502")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_2502 end

    def Function_18_254C(): pass

    label("Function_18_254C")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_254C end

    def Function_19_2588(): pass

    label("Function_19_2588")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC824, 0xFFFFAC04, 0xFFFF994E, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_2588 end

    def Function_20_25B6(): pass

    label("Function_20_25B6")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_269E")
    OP_43(0x0, 0x1, 0x0, 0x18)
    OP_43(0x1, 0x1, 0x0, 0x17)
    OP_43(0x2, 0x1, 0x0, 0x16)
    OP_43(0x3, 0x1, 0x0, 0x15)
    WaitChrThread(0x3, 0x1)
    Jump("loc_26B8")

    label("loc_269E")

    OP_43(0x0, 0x1, 0x0, 0x18)
    OP_43(0x1, 0x1, 0x0, 0x17)
    OP_43(0x2, 0x1, 0x0, 0x16)
    WaitChrThread(0x2, 0x1)

    label("loc_26B8")

    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_25B6 end

    def Function_21_26BE(): pass

    label("Function_21_26BE")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_26BE end

    def Function_22_2716(): pass

    label("Function_22_2716")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_2716 end

    def Function_23_2760(): pass

    label("Function_23_2760")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_2760 end

    def Function_24_279C(): pass

    label("Function_24_279C")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFC7F2, 0xFFFFADF8, 0xFFFFA6C8, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_24_279C end

    def Function_25_27CA(): pass

    label("Function_25_27CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27DB")
    Call(0, 2)
    Return()

    label("loc_27DB")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_25_27CA end

    def Function_26_28B9(): pass

    label("Function_26_28B9")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_26_28B9 end

    def Function_27_296C(): pass

    label("Function_27_296C")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_27_296C end

    def Function_28_2A1F(): pass

    label("Function_28_2A1F")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_28_2A1F end

    def Function_29_2AD2(): pass

    label("Function_29_2AD2")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_29_2AD2 end

    def Function_30_2B85(): pass

    label("Function_30_2B85")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_30_2B85 end

    def Function_31_2C38(): pass

    label("Function_31_2C38")

    OP_DE(0x0, 0x6, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_31_2C38 end

    def Function_32_2CEB(): pass

    label("Function_32_2CEB")

    OP_DE(0x0, 0x7, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_32_2CEB end

    def Function_33_2D9E(): pass

    label("Function_33_2D9E")

    OP_DE(0x0, 0x8, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_33_2D9E end

    def Function_34_2E5A(): pass

    label("Function_34_2E5A")

    OP_DE(0x0, 0x9, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_34_2E5A end

    def Function_35_2F0D(): pass

    label("Function_35_2F0D")

    OP_DE(0x0, 0xA, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_35_2F0D end

    def Function_36_2FC0(): pass

    label("Function_36_2FC0")

    OP_DE(0x0, 0xB, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_36_2FC0 end

    def Function_37_3073(): pass

    label("Function_37_3073")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3082")
    Jump("loc_30A7")

    label("loc_3082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3096")
    Call(0, 12)
    Return()

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A7")
    Call(0, 10)
    Return()

    label("loc_30A7")

    OP_DE(0x0, 0xC, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_37_3073 end

    def Function_38_315A(): pass

    label("Function_38_315A")

    OP_DE(0x0, 0xF, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_38_315A end

    def Function_39_3238(): pass

    label("Function_39_3238")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_39_3238 end

    def Function_40_32FB(): pass

    label("Function_40_32FB")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_40_32FB end

    def Function_41_33B7(): pass

    label("Function_41_33B7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_41_33B7 end

    def Function_42_3473(): pass

    label("Function_42_3473")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_42_3473 end

    def Function_43_352F(): pass

    label("Function_43_352F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_43_352F end

    def Function_44_35EB(): pass

    label("Function_44_35EB")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_44_35EB end

    def Function_45_36A7(): pass

    label("Function_45_36A7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_45_36A7 end

    def Function_46_3763(): pass

    label("Function_46_3763")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_46_3763 end

    def Function_47_381F(): pass

    label("Function_47_381F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_47_381F end

    def Function_48_38E4(): pass

    label("Function_48_38E4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_48_38E4 end

    def Function_49_39A0(): pass

    label("Function_49_39A0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_49_39A0 end

    def Function_50_3A5C(): pass

    label("Function_50_3A5C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_50_3A5C end

    def Function_51_3B18(): pass

    label("Function_51_3B18")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_51_3B18 end

    def Function_52_3BD4(): pass

    label("Function_52_3BD4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_52_3BD4 end

    def Function_53_3C90(): pass

    label("Function_53_3C90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CB9")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3CAD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3CAD)

    label("loc_3CB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CE2")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3CD6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3CD6)

    label("loc_3CE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D0B")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3CFF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3CFF)

    label("loc_3D0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D34")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3D28():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3D28)

    label("loc_3D34")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D60")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3D60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D77")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3D77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D8E")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3D8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA5")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3DA5")

    Return()

    # Function_53_3C90 end

    def Function_54_3DA6(): pass

    label("Function_54_3DA6")


    def lambda_3DAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3DAC)

    def lambda_3DBE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3DBE)

    def lambda_3DD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3DD0)

    def lambda_3DE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3DE2)
    Sleep(1000)
    Return()

    # Function_54_3DA6 end

    def Function_55_3DF4(): pass

    label("Function_55_3DF4")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
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

    Jump("loc_3E51")

    label("loc_3E51")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_55_3DF4 end

    def Function_56_3E68(): pass

    label("Function_56_3E68")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3E")
    OP_28(0x24, 0x4, 0x2)
    OP_82(0x94, 0x2)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3F3E")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05#40W　汝须将翱翔长空之一点红\x01",
            "　　 引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFD")
    Call(0, 55)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FFA")
    Call(0, 57)

    label("loc_3FFA")

    Jump("loc_3FFD")

    label("loc_3FFD")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_56_3E68 end

    def Function_57_4009(): pass

    label("Function_57_4009")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)

    def lambda_4072():
        OP_6B(3750, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4072)
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

    # Function_57_4009 end

    def Function_58_40BF(): pass

    label("Function_58_40BF")

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

    # Function_58_40BF end

    def Function_59_416A(): pass

    label("Function_59_416A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x198, 1)"), scpexpr(EXPR_END)), "loc_41DC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x00得到了\x1F\x98\x01\x07\x00。\x02",
    )

    Jump("loc_41C1")

    label("loc_41C1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2688)
    Jump("loc_4248")

    label("loc_41DC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "宝箱里装有\x1F\x98\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x98\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4229")

    label("loc_4229")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4248")

    Jump("loc_427C")

    label("loc_424B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_427C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_59_416A end

    def Function_60_428A(): pass

    label("Function_60_428A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_42FC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    Jump("loc_42E1")

    label("loc_42E1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2689)
    Jump("loc_4368")

    label("loc_42FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF5\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4349")

    label("loc_4349")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4368")

    Jump("loc_439C")

    label("loc_436B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_439C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_60_428A end

    def Function_61_43AA(): pass

    label("Function_61_43AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_441C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    Jump("loc_4401")

    label("loc_4401")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268A)
    Jump("loc_4488")

    label("loc_441C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x00\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4469")

    label("loc_4469")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_4488")

    Jump("loc_44BC")

    label("loc_448B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_44BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_61_43AA end

    def Function_62_44CA(): pass

    label("Function_62_44CA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45AB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_453C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        "\x07\x00得到了\x1F\x64\x01\x07\x00。\x02",
    )

    Jump("loc_4521")

    label("loc_4521")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268B)
    Jump("loc_45A8")

    label("loc_453C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        (
            "宝箱里装有\x1F\x64\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x64\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4589")

    label("loc_4589")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_45A8")

    Jump("loc_45DC")

    label("loc_45AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_45DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_62_44CA end

    def Function_63_45EA(): pass

    label("Function_63_45EA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x166, 1)"), scpexpr(EXPR_END)), "loc_465C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00得到了\x1F\x66\x01\x07\x00。\x02",
    )

    Jump("loc_4641")

    label("loc_4641")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268C)
    Jump("loc_46C8")

    label("loc_465C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "宝箱里装有\x1F\x66\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x66\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_46A9")

    label("loc_46A9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_46C8")

    Jump("loc_46FC")

    label("loc_46CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_46FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_63_45EA end

    def Function_64_470A(): pass

    label("Function_64_470A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47EB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x66, 1)"), scpexpr(EXPR_END)), "loc_477C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x00得到了\x1F\x66\x00\x07\x00。\x02",
    )

    Jump("loc_4761")

    label("loc_4761")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x268D)
    Jump("loc_47E8")

    label("loc_477C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "宝箱里装有\x1F\x66\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x66\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_47C9")

    label("loc_47C9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_47E8")

    Jump("loc_481C")

    label("loc_47EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_481C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_64_470A end

    SaveToFile()

Try(main)
