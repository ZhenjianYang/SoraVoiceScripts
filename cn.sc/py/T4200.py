from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '士兵丹',                               # 9
        '士兵阿尔兹',                           # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '王国军士兵',                           # 14
        '王国军士兵',                           # 15
        '王国军士兵',                           # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军士兵',                           # 21
        '王国军士兵',                           # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王国军士兵',                           # 25
        '幻惑之铃露茜奥拉',                     # 26
        '瘦狼瓦鲁特',                           # 27
        '怪盗布卢布兰',                         # 28
        '歼灭天使玲',                           # 29
        '亡命装甲兵',                           # 30
        '亡命装甲兵',                           # 31
        '亡命装甲兵',                           # 32
        '瘦狼瓦鲁特的残像',                     # 33
        '瘦狼瓦鲁特的残像',                     # 34
        '游客',                                 # 35
        '游客',                                 # 36
        '游客',                                 # 37
        '游客',                                 # 38
        '游客',                                 # 39
        '王都格兰赛尔·北街区',                 # 40
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
        'ED6_DT06/CH20043 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT06/CH20043P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        X                   = 6640,
        Z                   = 0,
        Y                   = 24120,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = 2060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 8130,
        Z                   = 0,
        Y                   = 11800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 6210,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 12840,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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


    DeclEvent(
        X                   = -4500,
        Y                   = -2000,
        Z                   = 37000,
        Range               = 4200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9470,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -5250,
        Y                   = -1000,
        Z                   = 28530,
        Range               = 4870,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7468,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = -11120,
        TriggerZ            = 0,
        TriggerY            = 19460,
        TriggerRange        = 1000,
        ActorX              = -15170,
        ActorZ              = -2000,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_546",          # 00, 0
        "Function_1_63B",          # 01, 1
        "Function_2_781",          # 02, 2
        "Function_3_8FE",          # 03, 3
        "Function_4_922",          # 04, 4
        "Function_5_946",          # 05, 5
        "Function_6_185D",         # 06, 6
        "Function_7_2588",         # 07, 7
        "Function_8_26D7",         # 08, 8
        "Function_9_289E",         # 09, 9
        "Function_10_29AB",        # 0A, 10
        "Function_11_2AA7",        # 0B, 11
        "Function_12_2CCB",        # 0C, 12
        "Function_13_36C5",        # 0D, 13
        "Function_14_36D1",        # 0E, 14
        "Function_15_3A6B",        # 0F, 15
        "Function_16_3C8B",        # 10, 16
        "Function_17_3DF4",        # 11, 17
        "Function_18_4692",        # 12, 18
        "Function_19_46C0",        # 13, 19
        "Function_20_46EE",        # 14, 20
        "Function_21_4742",        # 15, 21
        "Function_22_485F",        # 16, 22
        "Function_23_5241",        # 17, 23
        "Function_24_56A2",        # 18, 24
        "Function_25_56B8",        # 19, 25
        "Function_26_57F4",        # 1A, 26
        "Function_27_5930",        # 1B, 27
        "Function_28_5A6C",        # 1C, 28
        "Function_29_5BF0",        # 1D, 29
        "Function_30_5D5D",        # 1E, 30
        "Function_31_5EE1",        # 1F, 31
        "Function_32_5F68",        # 20, 32
        "Function_33_5FC1",        # 21, 33
    )


    def Function_0_546(): pass

    label("Function_0_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_55B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 16)

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57B")
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_591")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_611")

    label("loc_591")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A5"),
        (101, "loc_5DB"),
        (102, "loc_5F6"),
        (SWITCH_DEFAULT, "loc_611"),
    )


    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C5")
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_5D8")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    OP_A2(0x1627)

    label("loc_5D8")

    Jump("loc_611")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F3")
    SetMapFlags(0x10000000)
    OP_A3(0x203F)
    Event(0, 17)

    label("loc_5F3")

    Jump("loc_611")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    SetMapFlags(0x10000000)
    OP_A2(0x203F)
    Event(0, 17)

    label("loc_60E")

    Jump("loc_611")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_63A")
    SetChrPos(0x8, -2009, 0, 41980, 180)
    SetChrPos(0x9, 2270, 0, 41980, 180)

    label("loc_63A")

    Return()

    # Function_0_546 end

    def Function_1_63B(): pass

    label("Function_1_63B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x550), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_682")
    OP_B1("t4200_y")
    Jump("loc_68B")

    label("loc_682")

    OP_B1("t4200_n")

    label("loc_68B")

    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_6E2")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_END)), "loc_6D1")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 141)
    OP_72(0x2, 0x4)

    label("loc_6D1")

    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 15)
    OP_64(0x0, 0x1)

    label("loc_6E2")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6F8")
    OP_6F(0x0, 450)
    Jump("loc_77B")

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_710")
    OP_6F(0x0, 450)
    Jump("loc_717")

    label("loc_710")

    OP_6F(0x0, 0)

    label("loc_717")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_723"),
        (SWITCH_DEFAULT, "loc_73E"),
    )


    label("loc_723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73E")
    OP_6F(0x0, 450)
    OP_A2(0x2)
    Jump("loc_73E")

    label("loc_73E")

    Jump("loc_77B")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_759")
    OP_6F(0x0, 0)
    Jump("loc_760")

    label("loc_759")

    OP_6F(0x0, 450)

    label("loc_760")

    Jump("loc_77B")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_774")
    OP_6F(0x0, 450)
    Jump("loc_77B")

    label("loc_774")

    OP_6F(0x0, 0)

    label("loc_77B")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_63B end

    def Function_2_781(): pass

    label("Function_2_781")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8E8")

    label("loc_7A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8E8")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8E8")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8E8")

    label("loc_7F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8E8")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8E8")

    label("loc_823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8E8")

    label("loc_83C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8E8")

    label("loc_855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8E8")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_887")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8E8")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8E8")

    label("loc_8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8E8")

    label("loc_8B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8E8")

    label("loc_8D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8E8")

    label("loc_8FD")

    Return()

    # Function_2_781 end

    def Function_3_8FE(): pass

    label("Function_3_8FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_921")
    OP_8D(0xFE, 2620, 2600, -590, 3530, 2000)
    Jump("Function_3_8FE")

    label("loc_921")

    Return()

    # Function_3_8FE end

    def Function_4_922(): pass

    label("Function_4_922")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_945")
    OP_8D(0xFE, -1730, 10700, -4110, 14100, 2000)
    Jump("Function_4_922")

    label("loc_945")

    Return()

    # Function_4_922 end

    def Function_5_946(): pass

    label("Function_5_946")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_970")

    ChrTalk(    #0
        0xFE,
        (
            "喔，是你们……\x01",
            "请进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_99B")

    ChrTalk(    #1
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDA")

    label("loc_99B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 160, 0, 39870, 0)
    SetChrPos(0x101, 80, 0, 38310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E5")
    SetChrPos(0x106, -740, 0, 36890, 0)
    Jump("loc_9F6")

    label("loc_9E5")

    SetChrPos(0x103, -740, 0, 36890, 0)

    label("loc_9F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A17")
    SetChrPos(0xF9, 710, 0, 37200, 0)
    Jump("loc_A28")

    label("loc_A17")

    SetChrPos(0xF8, 710, 0, 37200, 0)

    label("loc_A28")

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 180, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #2
        0x8,
        "#5P公主殿下，您要进入城内吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#041F#2P嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "#5P谨遵殿下之名！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(500)
    OP_22(0xD2, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 450)
    OP_70(0x0, 0x1C2)
    Sleep(6700)
    OP_8C(0x9, 180, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #5
        0x8,
        "#1K#1P请进！\x02",
    )


    ChrTalk(    #6
        0x9,
        "#1K#2P请进！\x02",
    )

    OP_56(0x1)
    OP_59()
    Fade(500)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x0)

    label("loc_BDA")

    Jump("loc_C37")

    label("loc_BDD")


    ChrTalk(    #7
        0xFE,
        "终于抓到凯诺娜上尉了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "这样的话女王陛下\x01",
            "也能集中精力在条约的\x01",
            "签字仪式上了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C37")

    Jump("loc_1859")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D97")
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #9
        0xFE,
        "公主殿下有何吩咐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#040F丹先生，请问你\x01",
            "有没有见过穿白色礼服的\x01",
            "这么大的一个女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "穿白色礼服的女孩子……唔……\x01",
            "不记得有这样的人进了城堡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "刚才在王都前的广场巡逻时\x01",
            "好像也没有看到过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        (
            "#040F是吗……\x01",
            "谢谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "对、对不起。\x01",
            "没能帮上您的忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#040F不，我才是打扰了你的工作\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E09")

    label("loc_D97")


    ChrTalk(    #16
        0xFE,
        (
            "你们在找穿白色\x01",
            "礼服的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "唔……应该没有进入城堡。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "刚才在王都前的广场巡逻时\x01",
            "好像也没有看到过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E09")

    OP_A2(0x164C)
    Jump("loc_E4A")

    label("loc_E0F")


    ChrTalk(    #19
        0xFE,
        "穿白色礼服的女孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "我记得几天前\x01",
            "好像见过……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    Jump("loc_1859")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9A")

    ChrTalk(    #21
        0xFE,
        "公主殿下，您辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "已经是黄昏了，\x01",
            "请您出去时小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_EB0")

    ChrTalk(    #23
        0xFE,
        "请进！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1B")
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(    #24
        0x8,
        "#5P科洛蒂娅殿下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#5P如果需要进入城堡\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F47")

    label("loc_F1B")


    ChrTalk(    #26
        0x8,
        (
            "#5P需要进入城堡的话\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F47")

    Jump("loc_1859")

    label("loc_F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_1228")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107A")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x105, 300)
    Sleep(700)

    ChrTalk(    #27
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "如果需要进入城堡\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#041F#2P好的，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x1671)
    Jump("loc_11F4")

    label("loc_107A")


    ChrTalk(    #33
        0x8,
        (
            "#5P怎么了？\x01",
            "#5P您是不是还是想进去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x105, 300)
    TurnDirection(0x9, 0x105, 300)
    Sleep(400)

    ChrTalk(    #35
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "如果需要进入城堡\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1016F#2P（不、不愧是科洛丝……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x1671)

    label("loc_11F4")

    Jump("loc_1225")

    label("loc_11F7")


    ChrTalk(    #41
        0x8,
        (
            "#5P需要进入城堡的话，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1225")

    Jump("loc_1859")

    label("loc_1228")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16B3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141C")
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #45
        0x8,
        "咦？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 300)

    ChrTalk(    #46
        0x9,
        (
            "#5P那几位是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A7")

    ChrTalk(    #48
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_13A7")


    ChrTalk(    #49
        0x8,
        (
            "真让我吃惊。\x01",
            "好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "想进城堡的话，\x01",
            "随时招呼我们一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1006F#2P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    Jump("loc_16B0")

    label("loc_141C")

    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x8,
        "哟？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#5P你们是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E6")

    ChrTalk(    #55
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_14E6")


    ChrTalk(    #56
        0x8,
        (
            "哈哈……\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1015F#2P不，不是这样的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "如果需要进入城堡，\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        "#041F#2P好的，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    label("loc_16B0")

    Jump("loc_1859")

    label("loc_16B3")

    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x8,
        "哟？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#5P你们是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177D")

    ChrTalk(    #70
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_177D")


    ChrTalk(    #71
        0x8,
        (
            "哈哈……\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1000F#2P不，今天\x01",
            "只是路过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "是吗，想进城堡的话，\x01",
            "随时招呼我们一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1001F#2P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)

    label("loc_1859")

    TalkEnd(0x8)
    Return()

    # Function_5_946 end

    def Function_6_185D(): pass

    label("Function_6_185D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18B8")

    ChrTalk(    #77
        0xFE,
        (
            "科洛蒂娅殿下\x01",
            "应该在城堡里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "不过她现在应该很忙，\x01",
            "大概不能见你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_18B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18E3")

    ChrTalk(    #79
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B22")

    label("loc_18E3")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 160, 0, 39870, 0)
    SetChrPos(0x101, 80, 0, 38310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192D")
    SetChrPos(0x106, -740, 0, 36890, 0)
    Jump("loc_193E")

    label("loc_192D")

    SetChrPos(0x103, -740, 0, 36890, 0)

    label("loc_193E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195F")
    SetChrPos(0xF9, 710, 0, 37200, 0)
    Jump("loc_1970")

    label("loc_195F")

    SetChrPos(0xF8, 710, 0, 37200, 0)

    label("loc_1970")

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 180, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #80
        0x8,
        "#5P公主殿下，您要进入城内吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        "#041F#2P嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "#5P谨遵殿下之名！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(500)
    OP_22(0xD2, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 450)
    OP_70(0x0, 0x1C2)
    Sleep(6700)
    OP_8C(0x9, 180, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #83
        0x8,
        "#1K#1P请进！\x02",
    )


    ChrTalk(    #84
        0x9,
        "#1K#2P请进！\x02",
    )

    OP_56(0x1)
    OP_59()
    Fade(500)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x0)

    label("loc_1B22")

    Jump("loc_1B74")

    label("loc_1B25")


    ChrTalk(    #85
        0xFE,
        (
            "情报部的家伙们真把\x01",
            "我们整得够呛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "能抓到他们说实话让我松了一口气。\x02",
    )

    CloseMessageWindow()

    label("loc_1B74")

    Jump("loc_2584")

    label("loc_1B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1B9E")

    ChrTalk(    #87
        0xFE,
        (
            "哟，今天也需要\x01",
            "进去吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC9")

    ChrTalk(    #88
        0xFE,
        (
            "科洛蒂娅殿下，\x01",
            "欢迎您！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BDF")

    ChrTalk(    #89
        0xFE,
        "请进！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C4C")
    TurnDirection(0x9, 0x105, 0)

    ChrTalk(    #90
        0x9,
        "#5P科洛蒂娅殿下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#5P如果需要进入城堡，\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C78")

    label("loc_1C4C")


    ChrTalk(    #92
        0x9,
        (
            "#5P如果需要进入城堡，\x01",
            "请随时命令我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C78")

    Jump("loc_2584")

    label("loc_1C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_1F61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F32")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAD")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 300)
    Sleep(700)

    ChrTalk(    #93
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "如果需要进入城堡，\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        "#041F#2P好的，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x1671)
    Jump("loc_1F2F")

    label("loc_1DAD")


    ChrTalk(    #99
        0x9,
        (
            "#5P有何吩咐？\x01",
            "#5P您还是有事要进城里吗......\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 300)
    TurnDirection(0x9, 0x105, 300)
    Sleep(400)

    ChrTalk(    #101
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "如果需要进入城堡，\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1016F#2P（不、不愧是科洛丝……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x1671)

    label("loc_1F2F")

    Jump("loc_1F5E")

    label("loc_1F32")


    ChrTalk(    #107
        0x9,
        (
            "#5P如果需要进入城堡，\x01",
            "请随时命令我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5E")

    Jump("loc_2584")

    label("loc_1F61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23DE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2147")
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #108
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #111
        0x8,
        "咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "#5P那几位是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D2")

    ChrTalk(    #114
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_20D2")


    ChrTalk(    #115
        0x8,
        (
            "真让我吃惊。\x01",
            "好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "想进城堡的话，\x01",
            "随时招呼我们一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1006F#2P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    Jump("loc_23DB")

    label("loc_2147")

    TurnDirection(0x8, 0x0, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x8,
        "咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        (
            "#5P你们是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2211")

    ChrTalk(    #121
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_2211")


    ChrTalk(    #122
        0x8,
        (
            "哈哈……\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015F#2P不，不是这样的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #127
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "如果需要进入城堡，\x01",
            "请随时命令我们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#041F#2P好的，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    label("loc_23DB")

    Jump("loc_2584")

    label("loc_23DE")

    TurnDirection(0x8, 0x0, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x9,
        "咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "#5P你们是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A8")

    ChrTalk(    #136
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    label("loc_24A8")


    ChrTalk(    #137
        0x8,
        (
            "哈哈……\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1000F#2P不，今天\x01",
            "只是路过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "是吗，想进城堡的话，\x01",
            "随时招呼我们一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1001F#2P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)

    label("loc_2584")

    TalkEnd(0x9)
    Return()

    # Function_6_185D end

    def Function_7_2588(): pass

    label("Function_7_2588")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2595")
    Jump("loc_26D3")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25E9")

    ChrTalk(    #143
        0xFE,
        (
            "情报部的余党之前\x01",
            "终于被抓住了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "女神有眼，\x01",
            "不让他们再干坏事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_25E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_262A")

    ChrTalk(    #145
        0xFE,
        (
            "话说回来，\x01",
            "瓦雷利亚湖真宽广……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "好像海一样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_262A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_265B")

    ChrTalk(    #147
        0xFE,
        (
            "好久没这么\x01",
            "悠闲地看夕阳了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_265B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(    #148
        0xFE,
        (
            "呵呵，鱼儿也\x01",
            "游得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "唔～早知道应该\x01",
            "带钓竿来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D3")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_26D3")

    ChrTalk(    #150
        0xFE,
        (
            "唔唔，这附近\x01",
            "好像很适合钓鱼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D3")

    TalkEnd(0xFE)
    Return()

    # Function_7_2588 end

    def Function_8_26D7(): pass

    label("Function_8_26D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_26E4")
    Jump("loc_289A")

    label("loc_26E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_276D")

    ChrTalk(    #151
        0xFE,
        (
            "情报部和亲卫队好像\x01",
            "进行了战斗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "正好在我观光的时候\x01",
            "发生了大事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "希望不要再像以前那样，\x01",
            "连飞船也搭不了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289A")

    label("loc_276D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_27BF")

    ChrTalk(    #154
        0xFE,
        (
            "不知道能不能见到\x01",
            "科洛蒂娅公主……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "我还从来没见过\x01",
            "公主殿下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289A")

    label("loc_27BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2815")

    ChrTalk(    #156
        0xFE,
        (
            "这座城门前的广场，\x01",
            "给人的感觉真舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "景色也好，\x01",
            "风也清爽……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289A")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2847")

    ChrTalk(    #158
        0xFE,
        "我进城堡看过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "真的很不错！\x02",
    )

    CloseMessageWindow()
    Jump("loc_289A")

    label("loc_2847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(    #160
        0xFE,
        (
            "我是第一次近距离\x01",
            "看到格兰赛尔城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "果然和照片上的\x01",
            "气势完全不一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289A")

    TalkEnd(0xFE)
    Return()

    # Function_8_26D7 end

    def Function_9_289E(): pass

    label("Function_9_289E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28AB")
    Jump("loc_29A7")

    label("loc_28AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(    #162
        0xFE,
        "港口竟然发生了那样的事件……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2908")

    ChrTalk(    #163
        0xFE,
        (
            "太棒了，我傍晚一定\x01",
            "要去港口看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2958")

    ChrTalk(    #164
        0xFE,
        (
            "伫立在晚霞中的\x01",
            "城堡可是很浪漫的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "明天去哪里\x01",
            "参观呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_2958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(    #166
        0xFE,
        (
            "这地方……\x01",
            "风特别舒服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_29A7")

    ChrTalk(    #167
        0xFE,
        (
            "他难得旅行一次，\x01",
            "特别兴奋。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A7")

    TalkEnd(0xFE)
    Return()

    # Function_9_289E end

    def Function_10_29AB(): pass

    label("Function_10_29AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_29B8")
    Jump("loc_2AA3")

    label("loc_29B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_29E1")

    ChrTalk(    #168
        0xFE,
        (
            "昨天我们俩去\x01",
            "港口参观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA3")

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2A14")

    ChrTalk(    #169
        0xFE,
        (
            "今天要不要去大圣堂\x01",
            "和格兰赛尔港呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA3")

    label("loc_2A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A53")

    ChrTalk(    #170
        0xFE,
        (
            "王都的景点太多，\x01",
            "好是好，不过也让人犹豫……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA3")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2A77")

    ChrTalk(    #171
        0xFE,
        "那么接下来去哪儿呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AA3")

    label("loc_2A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2AA3")

    ChrTalk(    #172
        0xFE,
        (
            "哟！　你好。\x01",
            "王都真是个好地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA3")

    TalkEnd(0xFE)
    Return()

    # Function_10_29AB end

    def Function_11_2AA7(): pass

    label("Function_11_2AA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2AB4")
    Jump("loc_2CC7")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B4A")

    ChrTalk(    #173
        0xFE,
        "呀──────！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "听我说听我说，昨天我见到\x01",
            "急奔向港口的尤莉亚大人了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "后来情报部的人\x01",
            "就被逮捕了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "我真是被电到了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC7")

    label("loc_2B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2BA8")

    ChrTalk(    #177
        0xFE,
        (
            "要想见到尤莉亚大人，\x01",
            "就只能去当她的女佣了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "不过现在没有在\x01",
            "招聘女佣呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC7")

    label("loc_2BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1F")

    ChrTalk(    #179
        0xFE,
        (
            "我混在城里的游客中，\x01",
            "还去了亲卫队的驻所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "可还是没见到\x01",
            "尤莉亚大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "啊～她去\x01",
            "哪里了啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC7")

    label("loc_2C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2C87")

    ChrTalk(    #182
        0xFE,
        (
            "我所崇拜的尤莉亚大人……\x01",
            "到底怎样才能见到呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "果然还是以参观为名\x01",
            "混进城堡内最好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC7")

    label("loc_2C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2CC7")

    ChrTalk(    #184
        0xFE,
        (
            "我是王室亲卫队的粉丝。\x01",
            "当然最喜欢其中的尤莉亚大人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC7")

    TalkEnd(0xFE)
    Return()

    # Function_11_2AA7 end

    def Function_12_2CCB(): pass

    label("Function_12_2CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CD8")
    Return()

    label("loc_2CD8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_END)), "loc_2E36")
    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 38470, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x8,
        "公主殿下，您好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#5P您辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        (
            "#041F#2P丹先生和阿尔兹先生\x01",
            "执行任务也辛苦了。\x02\x03",

            "#542F这次我想带艾丝蒂尔\x01",
            "她们进城……\x02\x03",

            "可以放行吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339B")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_30AA")
    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 36000, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #188
        0x8,
        "哟，是你们啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1015F#2P嗯，我们这次是为了\x01",
            "游击士的工作来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x105, 0xFFFFFE52, 0x0, 0x9646, 0x7D0, 0x0)

    ChrTalk(    #192
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02\x03",

            "#542F我想带艾丝蒂尔\x01",
            "她们进去……\x02\x03",

            "可以放行吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339B")

    label("loc_30AA")

    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 36000, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x8,
        "咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "#5P你们是……\x01",
            "在武术大会上获得了冠军的……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1006F#2P嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x108,
        "#071F#2P上次真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "哈哈……\x01",
            "今天有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "如果想见谁的话，\x01",
            "我进去帮你们通报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x9,
        (
            "#5P或者说你们想\x01",
            "进去参观？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#1015F#2P嗯，我们这次是为了\x01",
            "游击士的工作来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x105, 0xFFFFFE52, 0x0, 0x9646, 0x7D0, 0x0)

    ChrTalk(    #204
        0x105,
        (
            "#048F#2P好久不见了。\x01",
            "丹先生、阿尔兹先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #205
        0x8,
        "公主殿下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        (
            "#5P科洛蒂娅殿下！\x01",
            "我不知道您回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x105,
        (
            "#041F#2P呵呵，这次是因为\x01",
            "有事，顺路过来看看。\x02\x03",

            "#542F我想带艾丝蒂尔\x01",
            "她们进去……\x02\x03",

            "可以放行吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339B")


    ChrTalk(    #208
        0x8,
        "当然没问题！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x9,
        "#5P谨遵殿下之名！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1016F#2P（不、不愧是科洛丝……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x104,
        "#031F（哟，科洛丝很得人心呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x108,
        "#070F#2P（难怪公爵会闹别扭了。）\x02",
    )

    CloseMessageWindow()

    def lambda_343C():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343C)

    def lambda_3454():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3454)

    def lambda_3464():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3464)
    OP_8E(0x9, 0x6E, 0x2EE, 0xADD4, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x105, 0x2)

    ChrTalk(    #213
        0x9,
        (
            "科洛丝殿下和\x01",
            "艾丝蒂尔小姐一行入内！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x9,
        "开门！\x02",
    )

    CloseMessageWindow()

    def lambda_34C9():
        OP_6D(70, 3450, 44190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34C9)

    def lambda_34E1():
        OP_67(0, 7620, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34E1)

    def lambda_34F9():
        OP_8E(0x8, 0xFFFFF704, 0x2EE, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_34F9)
    OP_8E(0x9, 0x992, 0x2EE, 0xAE38, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #215
        0x8,
        "#1K#1P请进！\x02",
    )


    ChrTalk(    #216
        0x9,
        "#1K#2P请进！\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #217
        0x105,
        (
            "#048F#5P呵呵……\x01",
            "各位辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_35A3():
        OP_6D(530, 0, 40500, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A3)

    def lambda_35BB():
        OP_67(0, 6000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_35BB)
    Sleep(500)
    OP_8C(0x105, 135, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #218
        0x105,
        (
            "#040F#5P艾丝蒂尔\x01",
            "我们进去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #219
        0x101,
        "#1008F#6P嗯、嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    Fade(500)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x1623)
    EventEnd(0x0)
    Return()

    # Function_12_2CCB end

    def Function_13_36C5(): pass

    label("Function_13_36C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_36CD")
    Return()

    label("loc_36CD")

    OP_A2(0x1627)
    Return()

    # Function_13_36C5 end

    def Function_14_36D1(): pass

    label("Function_14_36D1")

    EventBegin(0x0)
    SetChrPos(0x101, -310, 750, 49090, 180)
    SetChrPos(0x105, 720, 750, 48910, 180)
    SetChrPos(0x104, 990, 750, 50200, 180)
    SetChrPos(0x108, -540, 750, 50010, 180)
    OP_6D(120, 750, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_3763():
        OP_8E(0xFE, 0xFFFFFF2E, 0x2EE, 0xAC3A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3763)
    Sleep(200)

    def lambda_3783():
        OP_8E(0xFE, 0x26C, 0x2EE, 0xAB86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3783)
    Sleep(200)

    def lambda_37A3():
        OP_8E(0xFE, 0x3DE, 0x2EE, 0xB090, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37A3)
    Sleep(200)

    def lambda_37C3():
        OP_8E(0xFE, 0xFFFFFDE4, 0x2EE, 0xAFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37C3)
    WaitChrThread(0x108, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3877")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇听说了奈尔不在】\x01",      # 0
            "【◇没听说奈尔不在】\x01",      # 1
            "【◇什么也没有变更】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_386B"),
        (1, "loc_3871"),
        (SWITCH_DEFAULT, "loc_3877"),
    )


    label("loc_386B")

    OP_A2(0x1680)
    Jump("loc_3877")

    label("loc_3871")

    OP_A3(0x1680)
    Jump("loc_3877")

    label("loc_3877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_391D")

    ChrTalk(    #220
        0x104,
        (
            "#030F哟，已经傍晚了啊……\x01",
            "时间过得真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x105,
        (
            "#040F奈尔先生也该……\x01",
            "也回通讯社了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1011F#6P啊，也是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x108,
        (
            "#070F#5P好。\x01",
            "我们去通讯社看看吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BD")

    label("loc_391D")


    ChrTalk(    #224
        0x104,
        (
            "#030F哟，已经傍晚了啊……\x01",
            "时间过得真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        (
            "#040F只剩下利贝尔\x01",
            "通讯社还没去了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        "#1006F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x108,
        (
            "#070F#5P时间也差不多了。\x01",
            "快去拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 0)
    OP_6D(50, 750, 44240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -60, 750, 44250, 180)
    SetChrPos(0x1, -60, 750, 44250, 180)
    SetChrPos(0x2, -60, 750, 44250, 180)
    SetChrPos(0x3, -60, 750, 44250, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1627)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_36D1 end

    def Function_15_3A6B(): pass

    label("Function_15_3A6B")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 4900, 3600, 4050, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -100, 3300, -2001, 0, 0, 0, 1400, 1700, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -7410, 3800, 18520, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6100, 3500, 18170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -460, 3000, -2230, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 4970, 3000, 4050, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -7410, 3400, 18520, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6100, 3000, 18170, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_15_3A6B end

    def Function_16_3C8B(): pass

    label("Function_16_3C8B")

    SetChrPos(0xA, -2680, 0, 22070, 315)
    SetChrPos(0xB, -2480, 0, 20750, 180)
    SetChrPos(0xC, -1140, 0, 22210, 0)
    SetChrPos(0xD, -410, 0, 21460, 90)
    SetChrPos(0xE, 310, 0, 20760, 135)
    SetChrPos(0xF, 2220, 0, 22250, 270)
    SetChrPos(0x10, 2740, 0, 22270, 270)
    SetChrPos(0x11, 4170, 0, 21930, 225)
    SetChrPos(0x12, 4430, 0, 21030, 135)
    SetChrPos(0x13, -1230, 0, 19640, 0)
    SetChrPos(0x14, 400, 0, 19130, 270)
    SetChrPos(0x15, -3570, 0, 19150, 0)
    SetChrPos(0x16, -3030, 0, 21970, 270)
    SetChrPos(0x17, 2740, 0, 19290, 0)
    SetChrPos(0x18, -2190, 0, 18550, 135)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Return()

    # Function_16_3C8B end

    def Function_17_3DF4(): pass

    label("Function_17_3DF4")

    EventBegin(0x0)
    OP_D2(0x2701C8, 0x2701CD, 0x2)
    OP_D2(0x2701C6, 0x2701CB, 0x3)
    OP_D2(0x2701C9, 0x2701CE, 0x4)
    OP_D2(0x260003, 0x260008, 0x5)
    OP_D2(0x2601A7, 0x2601AC, 0x6)
    OP_D2(0x2600A0, 0x2600A5, 0x7)
    OP_D2(0x2601A7, 0x2601AC, 0x8)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    SetChrPos(0x1B, -290, 0, 28660, 0)
    SetChrPos(0x1C, -1380, 0, 26510, 0)
    SetChrPos(0x19, -70, 0, 24500, 0)
    SetChrPos(0x1A, 1500, 0, 26000, 0)
    SetChrChipByIndex(0x19, 2)
    SetChrChipByIndex(0x1A, 3)
    SetChrChipByIndex(0x1B, 4)
    SetChrChipByIndex(0x1C, 5)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(640, 0, 18960, 0)
    OP_67(0, 7320, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(33000, 0)
    OP_6E(332, 0)
    LoadEffect(0x3, "scraft\\sc007_10.eff")
    LoadEffect(0x4, "map\\mp002_00.eff")
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_3F5C():
        OP_8E(0xFE, 0xFFFFFE8E, 0x0, 0xA262, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3F5C)

    def lambda_3F77():
        OP_8E(0xFE, 0xFFFFF984, 0x0, 0x9FCE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3F77)

    def lambda_3F92():
        OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0x9BFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3F92)

    def lambda_3FAD():
        OP_8E(0xFE, 0x41A, 0x0, 0xA05A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3FAD)

    def lambda_3FC8():
        OP_6D(1440, 750, 44680, 6500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3FC8)

    def lambda_3FE0():
        OP_67(0, 3770, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_3FE0)

    def lambda_3FF8():
        OP_6B(2380, 6500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3FF8)

    def lambda_4008():
        OP_6E(507, 6500)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_4008)
    WaitChrThread(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 7)
    SetChrSubChip(0x1A, 0)
    WaitChrThread(0x19, 0x3)

    ChrTalk(    #228
        0x1C,
        (
            "#264F#6P哎呀……\x01",
            "城门给关起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x1B,
        (
            "#230F#6P嗯，这座王城是旧式建筑，\x01",
            "所以也可以用人力来开关城门。\x02\x03",

            "当然，肯定也要费不少力气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x19,
        (
            "#244F#4P呵呵……\x01",
            "真是辛苦他们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 90, 400)
    Sleep(300)

    ChrTalk(    #231
        0x1C,
        (
            "#261F#6P那怎么办？\x01",
            "我还是把『帕蒂尔·玛蒂尔』叫来吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x20)
    OP_8C(0x1A, 270, 400)
    Sleep(300)

    ChrTalk(    #232
        0x1A,
        (
            "#254F#2P喂喂。\x01",
            "把那种大家伙叫来的话，\x01",
            "咱们不就没的玩了吗。\x02\x03",

            "#252F这里就交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 135, 400)
    OP_8C(0x19, 45, 400)

    ChrTalk(    #233
        0x1C,
        "#267F#6P你要怎么做？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1A,
        "#252F#2P哼哼……好好看着吧！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x20)
    OP_8C(0x1A, 0, 400)

    def lambda_41E2():
        OP_6D(1050, 750, 46640, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41E2)

    def lambda_41FA():
        OP_6B(1950, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41FA)

    def lambda_420A():

        label("loc_420A")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_420A")

    QueueWorkItem2(0x1B, 2, lambda_420A)

    def lambda_421B():

        label("loc_421B")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_421B")

    QueueWorkItem2(0x1C, 2, lambda_421B)

    def lambda_422C():

        label("loc_422C")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_422C")

    QueueWorkItem2(0x19, 2, lambda_422C)
    ClearChrFlags(0x1A, 0x20)
    SetChrChipByIndex(0x1A, 3)
    OP_8E(0x1A, 0x12C, 0x2EE, 0xAFDC, 0x7D0, 0x0)
    OP_44(0x1B, 0x2)
    OP_44(0x1C, 0x2)
    OP_44(0x19, 0x2)
    OP_8C(0x1B, 0, 400)
    OP_8C(0x19, 0, 400)
    OP_8C(0x1C, 0, 400)
    WaitChrThread(0x101, 0x1)
    Fade(250)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 8)
    OP_0D()
    Sleep(500)
    OP_99(0x1A, 0x0, 0x2, 0x7D0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    SetChrPos(0x20, 300, 750, 45020, 0)
    SetChrChipByIndex(0x20, 8)
    SetChrSubChip(0x20, 2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x40)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    SetChrPos(0x21, 300, 750, 45020, 0)
    SetChrChipByIndex(0x21, 8)
    SetChrSubChip(0x21, 2)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x40)
    Sleep(500)

    def lambda_4318():
        OP_6B(1800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4318)
    PlayEffect(0x3, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(    #235 op#A op#5
        0x1A,
        "#257F#6P#30A#100W喝啊啊啊啊啊啊……！\x05\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    Sleep(1500)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_43AE():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43AE)

    def lambda_43BE():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_43BE)

    def lambda_43CE():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_43CE)
    OP_43(0x20, 0x0, 0x0, 0x12)
    OP_43(0x21, 0x0, 0x0, 0x13)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x12C, 0x64, 0xBB8, 0x12C)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Fade(500)
    Sleep(300)
    OP_43(0x1A, 0x3, 0x0, 0x14)
    SetChrPos(0x1A, 0, 750, 45050, 0)
    SetChrPos(0x20, 0, 750, 45050, 0)
    SetChrPos(0x21, 0, 750, 45050, 0)
    OP_6D(0, 3940, 46030, 0)
    OP_67(0, 3560, -10000, 0)
    OP_6B(1690, 0)
    OP_6C(0, 0)
    OP_6E(566, 0)

    def lambda_4496():
        OP_6B(1890, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_4496)
    Sleep(450)
    OP_22(0x13C, 0x0, 0x64)
    Sleep(1350)
    OP_22(0xF6, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0xFF, 0, 500, 43120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x1, 0x2)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x1A, 0x3)
    Sleep(500)
    Fade(500)
    OP_6D(1000, 750, 44760, 0)
    OP_67(0, 3770, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(507, 0)
    SetMapFlags(0x10)
    SetChrPos(0x1A, 410, 750, 45020, 0)
    SetChrPos(0x20, 300, 750, 45020, 0)
    SetChrPos(0x21, 300, 750, 45020, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #236
        0x1C,
        (
            "#261F#6P哇……！\x01",
            "好厉害呀！瓦鲁特！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x19,
        "#241F#6P这就是泰斗流的奥义……寸劲吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1B,
        (
            "#231F#6P呵呵……\x01",
            "威力还是这么惊人啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 7)
    SetChrFlags(0x1A, 0x20)
    Sleep(300)
    OP_8C(0x1A, 225, 400)
    Sleep(300)

    ChrTalk(    #239
        0x1A,
        (
            "#250F#5P嘿嘿……\x01",
            "雕虫小技，不值一提啦。\x02\x03",

            "#252F好，让我再把这扇门也轰开吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3DF4 end

    def Function_18_4692(): pass

    label("Function_18_4692")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_4692 end

    def Function_19_46C0(): pass

    label("Function_19_46C0")

    OP_91(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_46C0 end

    def Function_20_46EE(): pass

    label("Function_20_46EE")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x10)
    OP_72(0x1, 0x800)
    OP_B0(0x1, 0x19)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x19)
    OP_73(0x1)
    Sleep(500)
    OP_B0(0x1, 0x23)
    OP_6F(0x1, 25)
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    Return()

    # Function_20_46EE end

    def Function_21_4742(): pass

    label("Function_21_4742")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 7)), scpexpr(EXPR_END)), "loc_47CF")
    OP_6D(4310, 0, -4910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 4310, 0, -4910, 0)
    SetChrPos(0x1, 4310, 0, -4910, 0)
    SetChrPos(0x2, 4310, 0, -4910, 0)
    SetChrPos(0x3, 4310, 0, -4910, 0)
    Jump("loc_4850")

    label("loc_47CF")

    OP_6D(-2630, 0, -4930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2630, 0, -4930, 0)
    SetChrPos(0x1, -2630, 0, -4930, 0)
    SetChrPos(0x2, -2630, 0, -4930, 0)
    SetChrPos(0x3, -2630, 0, -4930, 0)

    label("loc_4850")

    OP_69(0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_4742 end

    def Function_22_485F(): pass

    label("Function_22_485F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_486C")
    Return()

    label("loc_486C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_488C")
    Call(0, 31)
    Call(0, 32)
    FadeToBright(0, 0)

    label("loc_488C")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48EB")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4929")

    label("loc_48EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4912")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4929")

    label("loc_4912")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4929")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4955")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4993")

    label("loc_4955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4993")

    label("loc_497C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4993")

    Sleep(1000)

    def lambda_499E():
        OP_6D(2450, 750, 48690, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_499E)

    def lambda_49B6():
        OP_67(0, 6680, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49B6)

    def lambda_49CE():
        OP_6B(2570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49CE)

    def lambda_49DE():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_49DE)
    OP_6E(403, 3000)
    Sleep(1000)
    Fade(500)
    OP_6D(490, 0, 35190, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(32000, 0)
    OP_6E(358, 0)
    SetChrPos(0x101, -760, 0, 34260, 0)
    SetChrPos(0x102, 620, 0, 34280, 0)
    SetChrPos(0xF8, -1040, 0, 32729, 0)
    SetChrPos(0xF9, 600, 0, 32930, 0)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_D2(0x290188, 0x29018C, 0x2)
    OP_D2(0x270110, 0x270120, 0x8)
    OP_D2(0x270111, 0x270121, 0x9)
    OP_D2(0x270130, 0x270140, 0xA)
    OP_D2(0x270131, 0x270141, 0xB)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_4ADB"),
        (5, "loc_4AF2"),
        (6, "loc_4B09"),
        (7, "loc_4B20"),
        (SWITCH_DEFAULT, "loc_4B37"),
    )


    label("loc_4ADB")

    OP_D2(0x701D0, 0x701DC, 0xC)
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_4B37")

    label("loc_4AF2")

    OP_D2(0x70218, 0x70224, 0xC)
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_4B37")

    label("loc_4B09")

    OP_D2(0x70230, 0x7023C, 0xC)
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_4B37")

    label("loc_4B20")

    OP_D2(0x70248, 0x70254, 0xC)
    OP_D2(0x70249, 0x70255, 0xD)
    Jump("loc_4B37")

    label("loc_4B37")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_4B50"),
        (5, "loc_4B67"),
        (6, "loc_4B7E"),
        (7, "loc_4B95"),
        (SWITCH_DEFAULT, "loc_4BAC"),
    )


    label("loc_4B50")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_4BAC")

    label("loc_4B67")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_4BAC")

    label("loc_4B7E")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_4BAC")

    label("loc_4B95")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_4BAC")

    label("loc_4BAC")

    OP_0D()
    Sleep(500)

    ChrTalk(    #240
        0x101,
        "#1020F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#1044F#4P这……\x01",
            "大概是徒手破坏后的痕迹。\x02\x03",

            "#1042F恐怕是『瘦狼』的绝技……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C59")

    ChrTalk(    #242
        0x108,
        (
            "#074F啊啊……\x01",
            "是零距离吐劲的奥义“寸劲”。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C80")

    ChrTalk(    #243
        0x106,
        "#055F真、真的吗……\x02",
    )

    CloseMessageWindow()

    label("loc_4C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CA7")

    ChrTalk(    #244
        0x107,
        "#065F呜、呜啊啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CD2")

    ChrTalk(    #245
        0x103,
        "#025F好惊人的破坏力……\x02",
    )

    CloseMessageWindow()

    label("loc_4CD2")


    ChrTalk(    #246
        0x101,
        (
            "#1007F#6P怎么可能……\x01",
            "这也太强了吧…\x02\x03",

            "#1005F……啊！\x01",
            "现在可不是钦佩的时候！\x02\x03",

            "必须要赶快追上他们──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)

    ChrTalk(    #247
        0x102,
        "#1046F#4P艾丝蒂尔！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4DC9():
        OP_96(0xFE, 0x834, 0x0, 0x8458, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DC9)
    Sleep(50)

    def lambda_4DEC():
        OP_96(0xFE, 0xFFFFF7CC, 0x0, 0x8458, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DEC)
    OP_43(0x1D, 0x0, 0x0, 0x19)

    def lambda_4E11():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x7724, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4E11)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x1A)

    def lambda_4E3B():
        OP_96(0xFE, 0x4B0, 0x0, 0x7724, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4E3B)
    OP_43(0x1F, 0x0, 0x0, 0x1B)
    SetChrPos(0x1D, 0, 12000, 38000, 180)
    SetChrPos(0x1E, 4000, 12000, 40000, 180)
    SetChrPos(0x1F, -4000, 12000, 40000, 180)
    SetChrChipByIndex(0x1D, 2)
    SetChrChipByIndex(0x1E, 2)
    SetChrChipByIndex(0x1F, 2)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(2190, 3130, 40810, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0x101, -670, 0, 30300, 0)
    SetChrPos(0x102, 950, 0, 30290, 0)
    SetChrPos(0xF8, -990, 0, 28900, 0)
    SetChrPos(0xF9, 1050, 0, 29020, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 10)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 12)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 14)
    OP_43(0x1D, 0x3, 0x0, 0x18)
    OP_43(0x1E, 0x3, 0x0, 0x18)
    OP_43(0x1F, 0x3, 0x0, 0x18)

    def lambda_4FA1():
        OP_8F(0xFE, 0x0, 0x9C4, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4FA1)
    Sleep(200)

    def lambda_4FC1():
        OP_8F(0xFE, 0xFA0, 0x9C4, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4FC1)
    Sleep(200)

    def lambda_4FE1():
        OP_8F(0xFE, 0xFFFFF060, 0x9C4, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4FE1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5006():
        OP_6D(2080, 0, 40810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5006)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0x2)
    OP_23(0x77)
    Sleep(1000)

    def lambda_5034():
        OP_6D(2710, 0, 37470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5034)

    def lambda_504C():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_504C)

    def lambda_5064():
        OP_6B(3540, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5064)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #248
        0x101,
        "#1005F#6P竟然出现在这里……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50BC")

    ChrTalk(    #249
        0x106,
        "#054F毁掉它们！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5105")

    label("loc_50BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50E2")

    ChrTalk(    #250
        0x108,
        "#076F击毁它们！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5105")

    label("loc_50E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5105")

    ChrTalk(    #251
        0x103,
        "#024F收拾它们！\x02",
    )

    CloseMessageWindow()

    label("loc_5105")


    def lambda_510B():
        OP_6D(730, 0, 34730, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_510B)

    def lambda_5123():
        OP_67(0, 5690, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5123)

    def lambda_513B():
        OP_6B(2580, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_513B)

    def lambda_514B():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_514B)

    def lambda_5166():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5166)

    def lambda_5181():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_5181)

    def lambda_519C():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_519C)

    def lambda_51B7():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51B7)

    def lambda_51D2():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_51D2)

    def lambda_51ED():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_51ED)
    Sleep(200)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    OP_44(0x1D, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x1F, 0x0)
    Battle(0x550, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 23)
    Return()

    # Function_22_485F end

    def Function_23_5241(): pass

    label("Function_23_5241")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x1D, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x1F, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    LoadEffect(0x1, "map\\\\mpsibuk.eff")
    OP_D2(0x290188, 0x29018C, 0x2)
    OP_D2(0x270110, 0x270120, 0x8)
    OP_D2(0x270111, 0x270121, 0x9)
    OP_D2(0x270130, 0x270140, 0xA)
    OP_D2(0x270131, 0x270141, 0xB)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_52C7"),
        (5, "loc_52DE"),
        (6, "loc_52F5"),
        (7, "loc_530C"),
        (SWITCH_DEFAULT, "loc_5323"),
    )


    label("loc_52C7")

    OP_D2(0x701D0, 0x701DC, 0xC)
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_5323")

    label("loc_52DE")

    OP_D2(0x70218, 0x70224, 0xC)
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_5323")

    label("loc_52F5")

    OP_D2(0x70230, 0x7023C, 0xC)
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_5323")

    label("loc_530C")

    OP_D2(0x70248, 0x70254, 0xC)
    OP_D2(0x70249, 0x70255, 0xD)
    Jump("loc_5323")

    label("loc_5323")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_533C"),
        (5, "loc_5353"),
        (6, "loc_536A"),
        (7, "loc_5381"),
        (SWITCH_DEFAULT, "loc_5398"),
    )


    label("loc_533C")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_5398")

    label("loc_5353")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_5398")

    label("loc_536A")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_5398")

    label("loc_5381")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_5398")

    label("loc_5398")

    SetChrPos(0x101, -990, 0, 32820, 270)
    SetChrPos(0x102, 450, 0, 32800, 90)
    SetChrPos(0xF8, -1100, 0, 31260, 270)
    SetChrPos(0xF9, 460, 0, 31240, 90)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 10)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 12)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 14)
    OP_6D(1820, 0, 35140, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(44000, 0)
    OP_6E(399, 0)
    SetChrChipByIndex(0x1D, 2)
    SetChrChipByIndex(0x1E, 2)
    SetChrChipByIndex(0x1F, 2)
    OP_43(0x1D, 0x3, 0x0, 0x18)
    OP_43(0x1E, 0x3, 0x0, 0x18)
    OP_43(0x1F, 0x3, 0x0, 0x18)
    SetChrPos(0x1D, 6510, 1500, 36000, 270)
    SetChrPos(0x1E, 6700, 1200, 31600, 270)
    SetChrPos(0x1F, -5430, 1700, 34200, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")

    def lambda_54C4():
        OP_6D(40, 0, 32430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54C4)

    def lambda_54DC():
        OP_67(0, 6230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54DC)

    def lambda_54F4():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_54F4)
    OP_43(0x1D, 0x0, 0x0, 0x1C)
    OP_43(0x1E, 0x0, 0x0, 0x1D)
    OP_43(0x1F, 0x0, 0x0, 0x1E)
    FadeToBright(1000, 0)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x1E, 0x1)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-10, 0, 32470, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #252
        0x101,
        (
            "#1005F#5P呼……\x01",
            "这、这可不是开玩笑的！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 500)

    ChrTalk(    #253
        0x102,
        (
            "#1042F#5P没时间了……\x01",
            "总之先要进去！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x203D)
    Sleep(100)
    Fade(500)
    OP_6D(-480, 0, 33720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -480, 0, 33720, 0)
    SetChrPos(0x1, -480, 0, 33720, 0)
    SetChrPos(0x2, -480, 0, 33720, 0)
    SetChrPos(0x3, -480, 0, 33720, 0)
    OP_0D()
    Call(0, 15)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_5241 end

    def Function_24_56A2(): pass

    label("Function_24_56A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_24_56A2")

    label("loc_56B7")

    Return()

    # Function_24_56A2 end

    def Function_25_56B8(): pass

    label("Function_25_56B8")

    PlayEffect(0x0, 0xFF, 0xFF, 2200, 0, 36450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 1030, 0, 34940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 80, 0, 33190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -1300, 0, 31960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -2130, 0, 30270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_25_56B8 end

    def Function_26_57F4(): pass

    label("Function_26_57F4")

    PlayEffect(0x0, 0xFF, 0xFF, -1840, 0, 36190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -580, 0, 34220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 330, 0, 32790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 1800, 0, 31190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 2680, 0, 30010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_26_57F4 end

    def Function_27_5930(): pass

    label("Function_27_5930")

    PlayEffect(0x0, 0xFF, 0xFF, -80, 0, 36860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 30, 0, 34690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 60, 0, 32710, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 210, 0, 30920, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 60, 0, 29140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_27_5930 end

    def Function_28_5A6C(): pass

    label("Function_28_5A6C")

    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_5A7B():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_5A7B)
    OP_44(0xFE, 0x3)

    def lambda_5A99():
        OP_8F(0xFE, 0x196E, 0xFFFFF060, 0x8CA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A99)
    PlayEffect(0x0, 0x0, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x0, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0x1, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)

    def lambda_5B9C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5B9C)
    OP_22(0xDC, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    Sleep(200)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x0, 0x2)
    Return()

    # Function_28_5A6C end

    def Function_29_5BF0(): pass

    label("Function_29_5BF0")

    Sleep(400)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_5C04():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C04)
    OP_44(0xFE, 0x3)

    def lambda_5C22():
        OP_8F(0xFE, 0x1A2C, 0xFFFFF060, 0x7B70, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C22)
    PlayEffect(0x0, 0x2, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x2, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x3, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)
    PlayEffect(0x1, 0x2, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x2, 0x2)
    Return()

    # Function_29_5BF0 end

    def Function_30_5D5D(): pass

    label("Function_30_5D5D")

    Sleep(600)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_5D71():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D71)
    OP_44(0xFE, 0x3)

    def lambda_5D8F():
        OP_8F(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0x8598, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D8F)
    PlayEffect(0x0, 0x4, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x5, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x4, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0x5, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)

    def lambda_5E92():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E92)
    PlayEffect(0x1, 0x4, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    Sleep(200)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x4, 0x2)
    Return()

    # Function_30_5D5D end

    def Function_31_5EE1(): pass

    label("Function_31_5EE1")

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
        (0, "loc_5F5B"),
        (1, "loc_5F61"),
        (SWITCH_DEFAULT, "loc_5F67"),
    )


    label("loc_5F5B")

    OP_A2(0x1200)
    Jump("loc_5F67")

    label("loc_5F61")

    OP_A2(0x1201)
    Jump("loc_5F67")

    label("loc_5F67")

    Return()

    # Function_31_5EE1 end

    def Function_32_5F68(): pass

    label("Function_32_5F68")

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

    # Function_32_5F68 end

    def Function_33_5FC1(): pass

    label("Function_33_5FC1")

    EventBegin(0x1)

    ChrTalk(    #254
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_5FED():
        OP_6D(-13180, -1000, 19320, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5FED)

    def lambda_6005():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6005)

    def lambda_6015():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_6015)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #255
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60AD")
    OP_C0(0xE, 0x2D, 0xFFFFD490, 0x0, 0x4C4A, 0x10E, 0xFFFFC4BE, 0xFFFFF63C, 0x4A4C)
    OP_6D(-9930, 0, 19230, 0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_60BC")

    label("loc_60AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60BC")
    EventEnd(0x1)

    label("loc_60BC")

    Return()

    # Function_33_5FC1 end

    SaveToFile()

Try(main)
