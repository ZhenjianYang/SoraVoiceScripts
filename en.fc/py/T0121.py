from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0121   ._SN',
            'ED6_DT01/T0121_1 ._SN',
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
        'Aina',                                 # 9
        'Scherazard',                           # 10
        'Ridge',                                # 11
        'Rinon',                                # 12
        'Bloom',                                # 13
        'Yuni',                                 # 14
        'Orvid',                                # 15
        'Mayor Klaus',                          # 16
        'Target Camera',                        # 17
        'Tarot',                                # 18
        'Tarot',                                # 19
        'Tarot',                                # 20
        'Tarot',                                # 21
        'Tarot',                                # 22
        'Tarot',                                # 23
    )

    DeclEntryPoint(
        Unknown_00              = 4250,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 2,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 4250,
        Unknown_04              = 0,
        Unknown_08              = -2000,
        Unknown_0C              = 4,
        Unknown_0E              = 90,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 315,
        Unknown_34              = 315,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 2,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01010 ._CH',             # 03
        'ED6_DT07/CH01760 ._CH',             # 04
        'ED6_DT07/CH01170 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH02350 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT06/CH20133 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01010P._CP',             # 03
        'ED6_DT07/CH01760P._CP',             # 04
        'ED6_DT07/CH01170P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH02350P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT06/CH20133P._CP',             # 0A
    )

    DeclNpc(
        X                   = 750,
        Z                   = 0,
        Y                   = 118600,
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
        X                   = 200,
        Z                   = 0,
        Y                   = 74200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -355,
        Z                   = 0,
        Y                   = 71450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -295,
        Z                   = 0,
        Y                   = 116400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = -3100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 82247,
        Z                   = 0,
        Y                   = 2548,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
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
        Unknown3            = 458761,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524297,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589833,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 655369,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 720905,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 786441,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2700,
        Y                   = -500,
        Z                   = 109000,
        Range               = -1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1B580,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 2900,
        Y                   = -500,
        Z                   = 110700,
        Range               = 5300,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x1ABBC,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1271,
        TriggerZ            = 0,
        TriggerY            = 116402,
        TriggerRange        = 800,
        ActorX              = 750,
        ActorZ              = 1500,
        ActorY              = 118600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F6",          # 00, 0
        "Function_1_606",          # 01, 1
        "Function_2_660",          # 02, 2
        "Function_3_676",          # 03, 3
        "Function_4_69A",          # 04, 4
        "Function_5_69F",          # 05, 5
        "Function_6_777",          # 06, 6
        "Function_7_4AEF",         # 07, 7
        "Function_8_59F0",         # 08, 8
        "Function_9_59F5",         # 09, 9
        "Function_10_7F55",        # 0A, 10
        "Function_11_8C5E",        # 0B, 11
        "Function_12_8D15",        # 0C, 12
        "Function_13_8DC1",        # 0D, 13
        "Function_14_8E6D",        # 0E, 14
        "Function_15_9226",        # 0F, 15
        "Function_16_98B7",        # 10, 16
        "Function_17_9DF0",        # 11, 17
        "Function_18_B1F4",        # 12, 18
        "Function_19_B3D3",        # 13, 19
        "Function_20_B402",        # 14, 20
        "Function_21_B436",        # 15, 21
        "Function_22_B465",        # 16, 22
        "Function_23_D3AD",        # 17, 23
        "Function_24_E356",        # 18, 24
        "Function_25_E3A1",        # 19, 25
        "Function_26_E3C2",        # 1A, 26
        "Function_27_E3DE",        # 1B, 27
        "Function_28_E3FF",        # 1C, 28
        "Function_29_E465",        # 1D, 29
        "Function_30_E4B8",        # 1E, 30
        "Function_31_EC4D",        # 1F, 31
    )


    def Function_0_3F6(): pass

    label("Function_0_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 41, 0, 116398, 0)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_41F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5649, 0, 114874, 0)

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_44D")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_459")
    ClearChrFlags(0xD, 0x80)

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_485")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0xA, -355, 0, 71450, 180)

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_496")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4C9")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4DC")
    SetChrFlags(0x9, 0x80)
    OP_A3(0x3FA)
    Event(0, 16)

    label("loc_4DC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4F0"),
        (103, "loc_54A"),
        (106, "loc_5D8"),
        (SWITCH_DEFAULT, "loc_5EC"),
    )


    label("loc_4F0")

    ClearMapFlags(0x1)
    SetChrPos(0x101, 1500, 0, 116000, 0)
    SetChrPos(0x102, 700, 0, 115200, 0)
    OP_6D(611, 0, 116942, 0)
    OP_6C(315000, 0)
    FadeToBright(1000, 0)
    OP_B1("t0121_y")
    Event(0, 30)
    Jump("loc_5EC")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 4)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B")
    ClearMapFlags(0x1)
    SetChrPos(0x101, 2400, 0, 111120, 0)
    SetChrPos(0x102, 3790, 0, 110540, 0)
    FadeToBright(500, 0)
    Event(0, 18)

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x268)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    Event(0, 17)

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D5")

    def lambda_5BC():

        label("loc_5BC")

        TurnDirection(0x9, 0x0, 0)
        OP_48()
        Jump("loc_5BC")

    QueueWorkItem2(0x9, 1, lambda_5BC)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    Event(0, 14)

    label("loc_5D5")

    Jump("loc_5EC")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    Event(0, 22)

    label("loc_5E9")

    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_605")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    Jump("loc_605")

    label("loc_605")

    Return()

    # Function_0_3F6 end

    def Function_1_606(): pass

    label("Function_1_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_633")
    OP_B1("t0121_y")
    Jump("loc_63C")

    label("loc_633")

    OP_B1("t0121_n")

    label("loc_63C")

    OP_64(0x0, 0x2)
    OP_64(0x1, 0x2)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F")
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_65F")
    OP_65(0x3, 0x1)

    label("loc_65F")

    Return()

    # Function_1_606 end

    def Function_2_660(): pass

    label("Function_2_660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_675")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_660")

    label("loc_675")

    Return()

    # Function_2_660 end

    def Function_3_676(): pass

    label("Function_3_676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_699")
    OP_8D(0xFE, 960, -4400, 2700, -2500, 3000)
    Jump("Function_3_676")

    label("loc_699")

    Return()

    # Function_3_676 end

    def Function_4_69A(): pass

    label("Function_4_69A")

    Call(0, 6)
    Return()

    # Function_4_69A end

    def Function_5_69F(): pass

    label("Function_5_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_6B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2")
    Call(0, 6)

    label("loc_6B2")

    Jump("loc_776")

    label("loc_6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_6F7")

    ChrTalk(    #0
        0x9,
        "#020FHey, you two! Hurry up and report.\x02",
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_6F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(    #1
        0x9,
        (
            "#020FQuit screwing around and check\x01",
            "the job description.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_773")

    ChrTalk(    #2
        0x9,
        "#020FQuit wasting time and go get them.\x02",
    )

    CloseMessageWindow()

    label("loc_773")

    TalkEnd(0x9)

    label("loc_776")

    Return()

    # Function_5_69F end

    def Function_6_777(): pass

    label("Function_6_777")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81B")
    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_0D()
    Call(1, 2)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81B")
    TalkEnd(0x8)
    Return()

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_917")
    OP_A2(0x5)

    ChrTalk(    #3
        0x8,
        (
            "#740FOh, you haven't left yet?\x02\x03",

            "In order to reach Bose, you'll\x01",
            "need to head west on the Milch\x01",
            "Main Road.\x02\x03",

            "I'll contact the Bracer Guild branch\x01",
            "and let them know you're coming.\x02\x03",

            "Make sure to be extra careful\x01",
            "while you're away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C")

    label("loc_917")


    ChrTalk(    #4
        0x8,
        (
            "#740FIn order to reach Bose, you'll\x01",
            "need to head west on the Milch\x01",
            "Main Road.\x02\x03",

            "Make sure to be extra careful\x01",
            "while you're away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C")

    Jump("loc_4AE9")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_214C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2016")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1078, 0, 116398, 0)
    TurnDirection(0x101, 0x9, 0)
    SetChrPos(0x102, 1078, 0, 115280, 0)
    TurnDirection(0x102, 0x9, 0)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0x9, 0x101, 0)
    OP_6D(270, 0, 117230, 0)
    OP_6B(2800, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #5
        0x9,
        "#020F#3POh, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#004F#4PSchera? What are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FThis is a rare occasion.\x01",
            "You're usually out and about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#020F#3PI just finished the jobs I took\x01",
            "over for your father.\x02\x03",

            "#020FAnd I was reporting to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#001F#4PSo you finished your load, too,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "#027F#3PSomehow or other, I guess.\x02\x03",

            "#027FI heard from Aina that you guys\x01",
            "aren't doing too bad yourselves.\x02\x03",

            "#027FI guess everything I went through\x01",
            "to train the two of you amounted\x01",
            "to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#008F#4PTee hee. We're grateful, too.\x02\x03",

            "#008FWell, I guess we'll report in as\x01",
            "well then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #12
        0x8,
        (
            "#740FGo ahead.\x01",
            "Let's hear what you've got.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05Reported about escorting the reporters.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x1, 0x100)
    Sleep(100)
    OP_AF(0x4, 0x19)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #14
        0x8,
        (
            "#741FGood work, you two.\x02\x03",

            "How about you, Scherazard? Don't\x01",
            "you think they've done a fine job?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(    #15
        0x9,
        (
            "#022F#3PThey still have a long way to go.\x01",
            "Their actions in the tower show\x01",
            "a lot of wasted effort.\x02\x03",

            "#022FWhen it's just the two of you, that's\x01",
            "one thing, but when it comes to\x01",
            "escorting someone, you get a C-.\x02\x03",

            "#022FYou need to work carefully and\x01",
            "deliberately with everything you do.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #16
        0x101,
        "#007F#4PThat's harsh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_EE5")


    ChrTalk(    #17
        0x9,
        (
            "#027F#3PFor a bunch of newbies, you did\x01",
            "an average job.\x02\x03",

            "#027FBut you shouldn't be satisfied with\x01",
            "that level of work.\x02\x03",

            "#027FEspecially you, Estelle.\x01",
            "You're always the first to get\x01",
            "on that high horse of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#502F#4POkay, okay, I get it already.\x02",
    )

    CloseMessageWindow()

    label("loc_FE6")


    ChrTalk(    #19
        0x8,
        "#741FGreat work, all of you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #20
        0x8,
        (
            "#740FI'm surprised that we were able to\x01",
            "fill the work gap left by Cassius\x01",
            "so quickly.\x02\x03",

            "I wonder if we'll be able to relax \x01",
            "for a bit now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#000F#6PI don't know... I can imagine that the\x01",
            "down time might be a bit of a drag.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #22
        0x102,
        (
            "#010FWell, that won't be a problem since there\x01",
            "are plenty of other small jobs like patrolling\x01",
            "the roads and exterminating monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#027F#3PHeehee...\x01",
            "It's been a while since I've been\x01",
            "able to take a break.\x02\x03",

            "#021FAll right! It's time for my reward!\x01",
            "I'm going to drink until I can't drink\x01",
            "anymore tonight!\x02\x03",

            "#021FEstelle, Joshua.\x01",
            "You two join me as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #24
        0x101,
        (
            "#004F#4PEh... We have to watch you get plastered\x01",
            "and make a fool of yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#022F#3POh, so what you're saying is that\x01",
            "you're turning down my invitation?\x02\x03",

            "#022FYou've got a lot of nerve to do something\x01",
            "like that to your mentor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#007F#4PWhat am I supposed to say?\x01",
            "Your drinking habits are intolerable.\x02\x03",

            "#007FYou cause a ruckus, dance like a\x01",
            "maniac and try to strip in public...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#017FAgreed... It's pretty embarrassing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#745FScherazard...just where do you\x01",
            "think you're going to take\x01",
            "these underage kids...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#024F#3PCome on...the alcohol is what\x01",
            "makes things entertaining.\x02\x03",

            "#025FBut if you're so against coming along\x01",
            "with me, then I don't need you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#501F#4PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "#020F#3PYup.\x02",
    )

    CloseMessageWindow()
    OP_92(0x9, 0x102, 0x2BC, 0xBB8, 0x0)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x9, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x9,
        (
            "#021F#1PInstead, I'll just have Joshua make\x01",
            "up for your absence.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #33
        0x102,
        (
            "#018FWhy me...?\x02\x03",

            "#018FU-Umm, Schera...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#005F#2PN-Now hold on a minute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "#027F#1PTeehee...\x01",
            "Joshua, you look like you'll\x01",
            "make a fine companion.\x02\x03",

            "#027FWhether we're talking booze or\x01",
            "something else behind closed\x01",
            "doors, I'll help break you in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#014FB-Break me in...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#009F#2PAll right, you big pervert, Joshua!\x01",
            "Why are you drooling like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#012FI-It's not what you think!\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xF, 4147, 0, 110113, 315)

    NpcTalk(    #39
        0xF,
        "Old man's voice",
        "W-We've got a major problem!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    TurnDirection(0x101, 0xF, 0)
    OP_8E(0xF, 0x6AC, 0x0, 0x1B280, 0xFA0, 0x0)
    TurnDirection(0x9, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    TurnDirection(0x101, 0xF, 0)
    OP_8E(0xF, 0x4A6, 0x0, 0x1BB8E, 0xFA0, 0x0)
    OP_43(0x101, 0x1, 0x0, 0x19)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    OP_6D(810, 0, 115660, 1000)

    ChrTalk(    #40
        0x101,
        "#004F#4PHuh? Mayor Klaus?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "#603F*wheeze* *cough* *pant*\x02\x03",

            "#604FEstelle, Joshua...and Scherazard.\x01",
            "Am I glad to see you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#014F(S-Saved by the bell...!)\x01",
            "What's wrong, sir? And why\x01",
            "are you in such a hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "#604FTh-This is terrible!\x02\x03",

            "M-My home! Disaster!\x01",
            "I-It's gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#008F#4PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "#025FAll right, calm down, Mayor Klaus.\x02\x03",

            "#020FTake a deep breath and let it out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x9, 400)

    ChrTalk(    #46
        0xF,
        (
            "#604FHaaaaa...\x02\x03",

            "#603FSuuuuu... Haaaaa...\x02\x03",

            "#603F...\x02\x03",

            "#602F...Apparently, it seems as though my\x01",
            "home was robbed while I was out.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#004F#4PWhaaaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#022FThat's not being calm at all,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "#602FI had something to speak with\x01",
            "Father Divine about, so I was\x01",
            "over at the chapel and...\x02\x03",

            "When I came home, it was rather odd for no one\x01",
            "to greet me at the door, so I looked around and\x01",
            "the rooms were in a state of great disarray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#002F#4PW-Wait...what about your\x01",
            "wife and Lita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xF,
        (
            "#600FDon't worry. They're both fine. I found\x01",
            "them locked up in the attic room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#007F#4PTh-That's a relief to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#022FIt's lucky that no harm\x01",
            "came to anyone.\x02\x03",

            "#022FIt won't get us anywhere just sitting\x01",
            "around here, so could you take us\x01",
            "to the crime scene, Mayor Klaus?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#602FAbsolutely.\x01",
            "I appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#002F#4PWait for me, I'm going, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#012FGood idea. We may be able to\x01",
            "be of some help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        "#025FWell, if you insist.\x02",
    )

    CloseMessageWindow()

    def lambda_1ED4():
        OP_6D(270, 0, 117230, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1ED4)
    TurnDirection(0x9, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #59
        0x9,
        (
            "#022FAina. We'll be at the mayor's place\x01",
            "investigating the incident.\x02\x03",

            "#022FIf you have anything come up, just\x01",
            "toss it on Ridge's shoulders.\x02\x03",

            "#022FI'm sure he's just relaxing at\x01",
            "the bar, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#742FYes, I'll do that. And everyone,\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T0210   ._SN", 1, 0, 0)
    IdleLoop()
    Jump("loc_2149")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B5")

    ChrTalk(    #61
        0x8,
        (
            "#740FIt must have been a pretty bold\x01",
            "group to rob the mayor's house\x01",
            "in broad daylight.\x02\x03",

            "I'm counting on you three to handle\x01",
            "the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_20B5")


    ChrTalk(    #62
        0x8,
        (
            "#740FHow's the investigation coming\x01",
            "along?\x02\x03",

            "Ridge is managing to take care\x01",
            "of everything else.\x02\x03",

            "You guys keep your focus on\x01",
            "the investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2149")

    Jump("loc_4AE9")

    label("loc_214C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_2327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A8")
    OP_A2(0x5)

    ChrTalk(    #63
        0x8,
        (
            "#740FOh right, Rinon's mother came here\x01",
            "trying to set me up with her son.\x02\x03",

            "#741FIt seems that she's been out asking\x01",
            "all the girls in town about the same\x01",
            "thing.\x02\x03",

            "I'm sorry to say this, but I'm not\x01",
            "ready to get married.\x02\x03",

            "#740FAlthough if some handsome stranger\x01",
            "showed up on my doorstep one day,\x01",
            "I just might change my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2324")

    label("loc_22A8")


    ChrTalk(    #64
        0x8,
        (
            "#740FSo you're heading to the Esmelas\x01",
            "Tower, huh? Be careful.\x02\x03",

            "Even if you know the place,\x01",
            "you shouldn't get careless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2324")

    Jump("loc_4AE9")

    label("loc_2327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE8")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x250)
    OP_0D()

    ChrTalk(    #65
        0x8,
        (
            "#740FGood work. It looks like you ran into a\x01",
            "bit of trouble at the mine though, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#004F#6PHuh? How'd you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#740FI got a call from the mine.\x01",
            "They said that they were incredibly\x01",
            "grateful to the both of you.\x02\x03",

            "Now, how about you give me a\x01",
            "report of what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        "#010FOkay, then. This is what happened...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_AF(0x4, 0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #69
        0x8,
        (
            "#740FVery nice! It looks like you\x01",
            "did much more than anyone was\x01",
            "expecting from you.\x02\x03",

            "Dealing with unexpected accidents is\x01",
            "also a part of our mission as bracers.\x02\x03",

            "I hope to see more great things from\x01",
            "you in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x101,
        "#001F#6PYou just leave that to us!☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#015FWell, you don't have to worry about\x01",
            "Estelle missing anything since her\x01",
            "nose is always in everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#502F#6PYeah, what he said...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #73
        0x101,
        (
            "#005F#4PHey! Why are you saying that\x01",
            "I'm super-nosy like that?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #74
        0x102,
        (
            "#015FBecause you are.\x02\x03",

            "Your skills lie in being direct,\x01",
            "nosy, and naive, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#009F#4PIsn't that being a bit harsh, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#019FAre you sure about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#740FAll right, that's enough, you two.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #78
        0x8,
        (
            "#740FOkay, this is the last of the jobs\x01",
            "you'll be doing for Cassius.\x02\x03",

            "You've heard of the Liberl News, right?\x01",
            "You'll be cooperating with them to get\x01",
            "some coverage for a news story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#004F#6PIsn't that the name of the news\x01",
            "magazine we bought the other day?\x02\x03",

            "#004FWhat are the chances of that\x01",
            "happening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        (
            "#010FWhen you say 'cooperating with\x01",
            "them to get some coverage'...just\x01",
            "exactly what does that entail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#740FIt seems that they're looking for a\x01",
            "skilled guide because they want to\x01",
            "get some shots of a dangerous place.\x02\x03",

            "You'll need to ask the reporters\x01",
            "directly for the details.\x02\x03",

            "The reporter and camerawoman\x01",
            "from the news service are staying\x01",
            "at the Hotel Rolent.\x02\x03",

            "Here's a referral from the guild.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #82
        "\x07\x00Received \x07\x02Guild Referral\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x19, 0x4, 0x4)
    OP_28(0x19, 0x1, 0x1)
    OP_28(0x19, 0x1, 0x2)
    OP_3E(0x324, 1)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #83
        0x101,
        (
            "#000F#4PAll right, how about we get over to\x01",
            "the hotel and talk to these people?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #84
        0x102,
        "#010FGood idea, let's go.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2DC2")

    label("loc_2BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3F")
    OP_A2(0x5)

    ChrTalk(    #85
        0x8,
        (
            "#740FOh, right, Rinon's mother came here\x01",
            "trying to set me up with her son.\x02\x03",

            "#741FIt seems that she's been out asking\x01",
            "all the girls in town about the same\x01",
            "thing.\x02\x03",

            "I'm sorry to say this, but I'm not\x01",
            "ready to get married.\x02\x03",

            "#740FAlthough, if some handsome stranger\x01",
            "showed up on my doorstep one day,\x01",
            "I just might change my mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC2")

    label("loc_2D3F")


    ChrTalk(    #86
        0x8,
        (
            "#740FThe client for your next job is\x01",
            "staying at the Hotel Rolent.\x02\x03",

            "Show him your referral and ask\x01",
            "him directly about the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC2")

    Jump("loc_4AE9")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C3")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x23A)

    ChrTalk(    #87
        0x8,
        (
            "#740FGood morning! How did the\x01",
            "job at the farm go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#000F#6PUm...we hit a few bumps in\x01",
            "the road, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#010FLet me give you a brief report\x01",
            "of the details.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #90
        "\x07\x05Joshua gives Aina a rundown of last night's events at the farm.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_AF(0x4, 0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #91
        0x8,
        (
            "#740FI see. So, you ended up setting the\x01",
            "monsters free because the Perzel\x01",
            "family requested you to do so?\x02\x03",

            "I think it was premature on their part,\x01",
            "but I won't pursue the matter any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#004F#6PIs it okay to leave things at that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#740FThe mission of a bracer is to protect\x01",
            "civilians and uphold justice...\x02\x03",

            "However, there are many ways we can protect\x01",
            "those around us, and there are as many forms\x01",
            "of justice as there are stars in the heavens.\x02\x03",

            "As a bracer, it is your job to be able\x01",
            "to discern these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#012FIndeed. Our work has very profound\x01",
            "implications if you think about it in\x01",
            "that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "#744FThat's because we aren't an organization that\x01",
            "deals strictly with monster problems--we also\x01",
            "intervene when disputes arise between nations.\x02\x03",

            "To become a high-ranking bracer, one must have\x01",
            "more than combat strength. A well-honed mind and\x01",
            "flexible problem-solving skills are also required.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#012FA sharp mind and problem-solving\x01",
            "ability, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#007F#6PSerious? The road to the big leagues\x01",
            "sounds a lot steeper than I originally\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#741FHa ha. Well, then your only choice\x01",
            "is to devote yourself to working hard\x01",
            "every day. \x02\x03",

            "#740FAnd since you're both here, why\x01",
            "don't I give you the details of\x01",
            "your next job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#006F#6PThose are the words I've been\x01",
            "waiting to hear!\x02\x03",

            "#006FI'm ready for anything so what've you\x01",
            "got lined up for us this time? Another\x01",
            "monster that needs a good whipping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#740FNot this time. This next job will\x01",
            "entail the transportation of goods.\x02\x03",

            "And get this, your client is none\x01",
            "other than Mayor Klaus, himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#004F#6PReally? A request from the mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#014FDo you think it'll be all right leaving\x01",
            "such an important task up to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#740FFrom what I've heard,\x01",
            "it's a pretty simple job.\x02\x03",

            "In any case, I'd like you to speak with\x01",
            "the mayor directly about the job details.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x3, 0x1, 0x1)
    OP_28(0x3, 0x4, 0x4)
    EventEnd(0x0)
    Jump("loc_3881")

    label("loc_36C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_3767")

    ChrTalk(    #104
        0x8,
        (
            "#744FI guess I didn't get enough to\x01",
            "drink last night.\x02\x03",

            "#740FMaybe I should have had Schera join\x01",
            "me for a bit longer instead of heading\x01",
            "home early...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3881")

    label("loc_3767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_37C9")

    ChrTalk(    #105
        0x8,
        (
            "#740FThat's right. You'll be heading to\x01",
            "the Malga Mine.\x02\x03",

            "Good luck and be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3881")

    label("loc_37C9")


    ChrTalk(    #106
        0x8,
        (
            "#740FPlease ask Mayor Klaus directly\x01",
            "regarding the details of the next job.\x02\x03",

            "Mayor Klaus' residence is at the\x01",
            "east end of town.\x02\x03",

            "...But I'm guessing you already\x01",
            "know that, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3881")

    Jump("loc_4AE9")

    label("loc_3884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDA")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1390, 0, 115970, 0)
    SetChrPos(0x102, 410, 0, 115820, 0)
    OP_8C(0x8, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x3E8)
    OP_A2(0x22C)
    OP_28(0x2, 0x4, 0x4)
    OP_28(0x2, 0x1, 0x1)
    OP_28(0x2, 0x1, 0x2)

    ChrTalk(    #107
        0x8,
        (
            "#740FOh, good morning Estelle and Joshua.\x02\x03",

            "Has your father already left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#000F#6PYep, just barely.\x02\x03",

            "#000FThat's why we came here to find\x01",
            "out about the jobs he left for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "#740FSure.\x02\x03",

            "There are a total of three jobs\x01",
            "I have lined up for you.\x02\x03",

            "For the first one, I'd like you to head\x01",
            "out to the farm west of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#004F#6PThe farm west of here?\x01",
            "Isn't that where Tio lives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#743FTio? I seem to have heard that\x01",
            "name somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FTio Perzel. She was one of our\x01",
            "classmates at Sunday School.\x02\x03",

            "#010FShe's also the Perzel Farm\x01",
            "owner's daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#740FOh, really?\x02\x03",

            "It's actually the Perzel Farm that\x01",
            "put in a request to have someone\x01",
            "exterminate some monsters.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        (
            "#004F#6PAre they really having problems\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#740FFortunately nobody has been hurt, but the\x01",
            "owner and his family are upset over their\x01",
            "fields being destroyed by the creatures.\x02\x03",

            "Therefore, the guild received an\x01",
            "extermination request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#002F#6PI never would have expected something\x01",
            "like that to happen...\x02\x03",

            "#002FOkay! We'll head out there,\x01",
            "right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "#740FHere. Take this with you.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #118
        "\x07\x00Received \x07\x02Guild Referral\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x320, 1)

    ChrTalk(    #119
        0x8,
        (
            "#740FThis document certifies that you\x01",
            "were dispatched by the guild.\x02\x03",

            "Please give it to the owner of\x01",
            "the farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#501F#6PWe already know Tio's father pretty well,\x01",
            "so I don't think this is necessary...\x02\x03",

            "#501FBut, we'll take it just in case.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_3F98")

    label("loc_3EDA")


    ChrTalk(    #121
        0x8,
        (
            "#740FThe first job I'm going to have you\x01",
            "do is a monster extermination at\x01",
            "the Perzel Farm.\x02\x03",

            "The farm can be reached by heading\x01",
            "south at the break along the Milch\x01",
            "Main Road.\x02\x03",

            "Good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F98")

    Jump("loc_4AE9")

    label("loc_3F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_40F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408E")
    OP_A2(0x5)

    ChrTalk(    #122
        0x8,
        (
            "#741FI'm sure today was tough for your\x01",
            "first day as bracers.\x02\x03",

            "But you had a fine showing.\x01",
            "I'll see you two tomorrow.\x02\x03",

            "#740FI think this letter addressed to\x01",
            "your father is important, so don't\x01",
            "forget to give it to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_408E")


    ChrTalk(    #123
        0x8,
        (
            "#740FI think this letter addressed to\x01",
            "your father is important, so don't\x01",
            "forget to give it to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F6")

    Jump("loc_4AE9")

    label("loc_40F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_41AA")

    ChrTalk(    #124
        0x8,
        (
            "#740FI'm counting on you to bring\x01",
            "back those boys safely.\x02\x03",

            "The Esmelas Tower is at the west\x01",
            "end of the Malga Trail.\x02\x03",

            "The Malga Trail is through the gate\x01",
            "in town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE9")

    label("loc_41AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B4")
    OP_A2(0x5)

    ChrTalk(    #125
        0x8,
        (
            "#740FCongratulations! You two are now\x01",
            "official members of the Bracer Guild.\x02\x03",

            "From now on I'm going to be passing\x01",
            "jobs out to you like candy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#502F'Bring it on!' is all I have to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#010FI look forward to working with\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4326")

    label("loc_42B4")


    ChrTalk(    #128
        0x8,
        (
            "#740FFrom now on I'm going to be passing\x01",
            "jobs out to you like candy.\x02\x03",

            "I hope you'll work hard for\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4326")

    Jump("loc_4AE9")

    label("loc_4329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_43E1")

    ChrTalk(    #129
        0x8,
        (
            "#740FIf you've passed your qualification exam\x01",
            "then there's one thing left to do.\x02\x03",

            "When you want to report that you've\x01",
            "finished a job, please select the\x01",
            "'Report' option.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE9")

    label("loc_43E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4417")

    ChrTalk(    #130
        0x8,
        "#740FThe bulletin board is over there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AE9")

    label("loc_4417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4A39")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0xD)

    ChrTalk(    #131
        0x8,
        (
            "#740FThese are very important, so make\x01",
            "sure not to lose them.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #132
        "\x07\x00Received \x07\x02Bracer Notebook\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x208, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x102, 0x9, 400)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x320)

    ChrTalk(    #133
        0x9,
        (
            "#020FBracer notebooks serve as the\x01",
            "official way to record the status\x01",
            "of your current jobs.\x02\x03",

            "#020FAlso, anything you may hear or\x01",
            "anything that you may find and\x01",
            "where...\x02\x03",

            "#020FThese kinds of trivial things can\x01",
            "often become clues.\x02\x03",

            "#020FNo matter how insignificant something\x01",
            "may seem, always write it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        "#010F#2P#1KUnderstood.\x02",
    )


    ChrTalk(    #135
        0x101,
        (
            "#509F#4P#1K(Crap, this sounds like it's going\x01",
            "to be a pain...)\x02",
        )
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #136
        0x9,
        (
            "#026FOh?\x02\x03",

            "Please tell me it was my ears playing\x01",
            "tricks on me, because I swear I only\x01",
            "got one response.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#506FUh...I-I'm sure there were two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x9,
        (
            "#020FKeeping an accurate account of events\x01",
            "is an important duty for ALL bracers.\x02\x03",

            "So, get with the program and stop\x01",
            "trying to make this out to be more\x01",
            "than it really is, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#007FOkay, okay, I got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x9,
        (
            "#020FMake sure you do...\x02\x03",

            "#020FAll right then, let's begin.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 135, 400)

    ChrTalk(    #141
        0x9,
        (
            "#020FLook over by the door. You can see\x01",
            "that there's a bulletin board standing\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0x102, 135, 400)
    OP_6D(3915, 0, 113532, 1000)

    ChrTalk(    #142
        0x9,
        (
            "#020FFirst, I want you to go and check\x01",
            "the job description posted there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #143
        (
            "\x07\x05※When the bulletin board is approached, a '!' mark will appear. Pressing\x01",
            "the OK button will display the job list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #144
        "\x07\x05※By selecting the job names on the list, you can view their details.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)

    def lambda_4A27():

        label("loc_4A27")

        TurnDirection(0x9, 0x0, 0)
        OP_48()
        Jump("loc_4A27")

    QueueWorkItem2(0x9, 1, lambda_4A27)
    OP_65(0x3, 0x1)
    Jump("loc_4AE9")

    label("loc_4A39")


    ChrTalk(    #145
        0x8,
        (
            "#740FOnce you finish today's training,\x01",
            "you'll finally be recognized as\x01",
            "members of the Bracer Guild.\x02\x03",

            "Scherazard's waiting for you upstairs.\x02\x03",

            "Good luck to the both of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE9")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_6_777 end

    def Function_7_4AEF(): pass

    label("Function_7_4AEF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C93")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #146
        0xFE,
        (
            "Sch-Schera! I heard that you're taking\x01",
            "these two and heading to Bose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x103,
        "#020FYep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Without Cassius around will I be\x01",
            "able to handle the jobs...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        (
            "#024FWhat are you babbling about?\x01",
            "You're supposed to be a man, right?\x02\x03",

            "#020FThe work may get a bit tougher to deal\x01",
            "with while we're gone, but I'm counting\x01",
            "on you.\x02\x03",

            "#020FDon't let me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "I-I'll do my best!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CF6")

    label("loc_4C93")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #151
        0xFE,
        (
            "Schera, I'll put everything I have\x01",
            "into these jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Please take care of yourself.\x02",
    )

    CloseMessageWindow()

    label("loc_4CF6")

    Jump("loc_59EC")

    label("loc_4CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFD")
    OP_A2(0x6)

    ChrTalk(    #153
        0xFE,
        (
            "Oh, Estelle and Joshua. I heard about\x01",
            "the incident at the mayor's residence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "There's not much you could have\x01",
            "done when those criminals took\x01",
            "off in an airship like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Anyway, I'd like to say thanks for\x01",
            "all your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E3C")

    label("loc_4DFD")


    ChrTalk(    #156
        0xFE,
        (
            "By the way, what's with all that\x01",
            "baggage you're carrying?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3C")

    Jump("loc_59EC")

    label("loc_4E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4F88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2C")
    OP_A2(0x6)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #157
        0xFE,
        (
            "Oh, Schera...so, are all three of\x01",
            "you working together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#020FThat's right.\x02\x03",

            "The extra work I'm leaving behind\x01",
            "might be a bit of a strain, but I'm\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "A-Absolutely! I'll do my best!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F85")

    label("loc_4F2C")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #160
        0xFE,
        (
            "I'll take care of all the little jobs, so\x01",
            "you just focus on the job at hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F85")

    Jump("loc_59EC")

    label("loc_4F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_5100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BB")
    OP_A2(0x6)

    ChrTalk(    #161
        0xFE,
        "I've been thinking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "There's another really capable bracer\x01",
            "from the same year as Schera in the\x01",
            "Bose area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "I've heard he's been about as\x01",
            "successful as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "*sigh*\x01",
            "All these bracers are unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "This is my 3rd year in the guild...\x01",
            "I've got to work harder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50FD")

    label("loc_50BB")


    ChrTalk(    #166
        0xFE,
        (
            "This is my 3rd year in the guild...\x01",
            "I've got to work harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FD")

    Jump("loc_59EC")

    label("loc_5100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_5406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538F")
    OP_A2(0x6)

    ChrTalk(    #167
        0xFE,
        (
            "So you two were trained by\x01",
            "Schera, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#000FYep, you got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "So I guess we're in the same boat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "In fact, it's my pride and joy that\x01",
            "I trained under Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "She's considered to be one of the\x01",
            "best bracers in the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I've worked together with her and\x01",
            "I can tell you that her nickname,\x01",
            "'Silver Streak', isn't for show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#004FIt...isn't?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Beginning with your father, Cassius,\x01",
            "the Rolent branch is blessed with\x01",
            "some extremely skilled bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#501FI guess Schera is really talented\x01",
            "then, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        (
            "#010FHearing this coming from someone\x01",
            "else makes me realize it all over\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5403")

    label("loc_538F")


    ChrTalk(    #177
        0xFE,
        (
            "With Schera and your father, Cassius,\x01",
            "the Rolent branch is really blessed with\x01",
            "some extremely skilled bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5403")

    Jump("loc_59EC")

    label("loc_5406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_57BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_574D")
    OP_A2(0x6)

    ChrTalk(    #178
        0xFE,
        (
            "It seems as though your father\x01",
            "is going to be gone on business\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#009FThe second you think my dad's been\x01",
            "home for a bit, he strolls right\x01",
            "back out the door.\x02\x03",

            "I wonder if he's really working\x01",
            "sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Cassius is in every way the veteran\x01",
            "member of the Rolent branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "It seems like until recently, Cassius\x01",
            "was handling all the important\x01",
            "requests single-handedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#004FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Yep, it seems like he only just started \x01",
            "leaving some of these jobs up to Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "It looks like he gets a lot of direct\x01",
            "requests from other branches as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "That's why he's gone so often.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        "#004FI had no idea...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#010FWell, he's the type of person that\x01",
            "never talks about work while he's\x01",
            "at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#007FYeah, whenever he's at home he\x01",
            "just seems like a no-good middle-\x01",
            "aged man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BA")

    label("loc_574D")


    ChrTalk(    #189
        0xFE,
        (
            "There are a lot of bracers out there\x01",
            "who really respect your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "I guess I'm one of them, too.\x02",
    )

    CloseMessageWindow()

    label("loc_57BA")

    Jump("loc_59EC")

    label("loc_57BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_59C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5958")
    OP_A2(0x6)

    ChrTalk(    #191
        0xA,
        "Hi there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#000FOh, hi, Ridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        (
            "It looks like your training is\x01",
            "over, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "I'm humbled to know that you two\x01",
            "are the youngest ever to pass the\x01",
            "bracer exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xA,
        (
            "I look forward to working with you\x01",
            "in the same capacity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        "#010FOurselves as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "I have to get back to work now,\x01",
            "but if there's something you don't\x01",
            "understand, give me a holler.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59BE")

    label("loc_5958")


    ChrTalk(    #198
        0xA,
        (
            "I have to get back to work now,\x01",
            "but if there's something you don't\x01",
            "understand, give me a holler.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BE")

    Jump("loc_59EC")

    label("loc_59C1")


    ChrTalk(    #199
        0xA,
        (
            "このタイミングでは\x01",
            "僕は配置なしです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59EC")

    TalkEnd(0xA)
    Return()

    # Function_7_4AEF end

    def Function_8_59F0(): pass

    label("Function_8_59F0")

    Call(0, 9)
    Return()

    # Function_8_59F0 end

    def Function_9_59F5(): pass

    label("Function_9_59F5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_END)), "loc_5A85")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A74")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5A5D")
    OP_A9(0x8)
    Jump("loc_5A6B")

    label("loc_5A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_5A69")
    OP_A9(0x7)
    Jump("loc_5A6B")

    label("loc_5A69")

    OP_A9(0x2)

    label("loc_5A6B")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_5A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A85")
    TalkEnd(0xB)
    Return()

    label("loc_5A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC7")
    OP_A2(0x4)

    ChrTalk(    #200
        0xB,
        (
            "Well, that's an awful lot of baggage\x01",
            "you have. Off on vacation, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        "Where are you headed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#000FUh, well, it's no pleasure trip, but\x01",
            "we're headed to Bose for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xB,
        (
            "Bose, did you say? But the airliners\x01",
            "have been grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xB,
        (
            "Don't tell me you're planning to\x01",
            "foot it the whole way...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#010FThat's right, we are. We've been told\x01",
            "that the trip is doable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xB,
        (
            "That's true. It's not so far,\x01",
            "but it's not that close either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xB,
        "It must be tough being a bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xB,
        (
            "Are all your preparations in order?\x01",
            "Do take care of yourselves!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D91")

    label("loc_5CC7")


    ChrTalk(    #209
        0xB,
        (
            "Bose is a merchant city, you know.\x01",
            "I haven't been there for a while\x01",
            "myself, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "Went there several times in the past\x01",
            "to learn how to run a business. It\x01",
            "was...an illuminating experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D91")

    Jump("loc_7F51")

    label("loc_5D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_605D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FFC")
    OP_A2(0x4)

    ChrTalk(    #211
        0xB,
        (
            "Hi there. What brings all three\x01",
            "of you together like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#000FUm, we have a job that needs\x01",
            "taking care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xB,
        "Working hard, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xB,
        (
            "Oh, that reminds me. The accessory\x01",
            "you ordered came in, Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xB,
        (
            "It had to come all the way from the\x01",
            "Republic, so it took some time to\x01",
            "get it in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x103,
        (
            "#020FOh, really? I certainly appreciate\x01",
            "you going through the trouble for\x01",
            "me.\x02\x03",

            "Right now, I'm in the middle of something,\x01",
            "though, so I'll have to stop by again later\x01",
            "to pick it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xB,
        (
            "Sure thing. I'll be here when you\x01",
            "get done with whatever it is you've\x01",
            "got on your plate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_605A")

    label("loc_5FFC")


    ChrTalk(    #218
        0xB,
        (
            "When the three of you are finished\x01",
            "with your job, come back and have\x01",
            "a look at my wares.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_605A")

    Jump("loc_7F51")

    label("loc_605D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_628B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E0")
    OP_A2(0x4)

    ChrTalk(    #219
        0xB,
        (
            "Recently, it seems like whenever\x01",
            "I go out on the street, I get a lot\x01",
            "of strange looks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xB,
        (
            "It appears that my mom's started\x01",
            "up the 'bride hunt' again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xB,
        (
            "When I first heard about what was\x01",
            "going on I thought I was going to\x01",
            "die of sheer embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xB,
        (
            "No matter how many times I tell\x01",
            "her to knock it off, she just keeps\x01",
            "doing it. What am I going to do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6288")

    label("loc_61E0")


    ChrTalk(    #223
        0xB,
        (
            "It appears that my mom's started\x01",
            "up the 'bride hunt' again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xB,
        (
            "When I first heard about what was\x01",
            "going on I thought I was going to\x01",
            "die of sheer embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6288")

    Jump("loc_7F51")

    label("loc_628B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_63C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6377")
    OP_A2(0x4)

    ChrTalk(    #225
        0xB,
        (
            "My mother suddenly started talking\x01",
            "about trying to set me up with\x01",
            "someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xB,
        (
            "I told her I wasn't planning on getting\x01",
            "married for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xB,
        (
            "But she doesn't listen to a word\x01",
            "I say! This is just great...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C3")

    label("loc_6377")


    ChrTalk(    #228
        0xB,
        (
            "I'm just not ready for the responsibilities\x01",
            "of a family at this point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C3")

    Jump("loc_7F51")

    label("loc_63C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65AA")
    OP_A2(0x4)

    ChrTalk(    #229
        0xB,
        (
            "Hey there, Estelle. Have you been\x01",
            "busy lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xB,
        (
            "I've been kind of sad you haven't\x01",
            "been by to buy junk food lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#018FNow that you mention it, she\x01",
            "had been disappearing pretty often\x01",
            "on the way home from training...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #232
        0x101,
        (
            "#009FH-Hey! There's nothing wrong\x01",
            "with that...\x02\x03",

            "Eating cookies and snacks is\x01",
            "the right of any girl my age.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(    #233
        0xB,
        (
            "Ha ha, stop by again when you've\x01",
            "got a day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xB,
        (
            "I'll look into those sneakers you\x01",
            "like so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6614")

    label("loc_65AA")


    ChrTalk(    #235
        0xB,
        (
            "Ha ha, stop by again when you've\x01",
            "got a day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xB,
        (
            "I'll look into those sneakers you\x01",
            "like so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6614")

    Jump("loc_7F51")

    label("loc_6617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_66BA")

    ChrTalk(    #237
        0xB,
        (
            "It looks like the Linde just arrived\x01",
            "at the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xB,
        (
            "I'm sure the products I ordered from\x01",
            "Bose have come, so I've got to go\x01",
            "pick them up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F51")

    label("loc_66BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_6780")

    ChrTalk(    #239
        0xB,
        (
            "Hey there, Rolent's two newest bracers.\x01",
            "I look forward to your success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xB,
        (
            "I'm about ready to close up shop, so\x01",
            "if you have any purchases to make,\x01",
            "I ask that you be quick about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F51")

    label("loc_6780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B33")
    OP_A2(0x208)
    OP_A2(0x4)

    ChrTalk(    #241
        0x101,
        "#001FGood morning, Mr. Rinon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xB,
        "Hello there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xB,
        (
            "You're up rather early today. Did you\x01",
            "come to buy a new pair of shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#004FNow that you mention it, are there\x01",
            "any new ones in stock?\x02\x03",

            "#001FYou know, like...the newest Stregas?!!!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #245
        0x102,
        (
            "#018FUnbelievable. You've actually already\x01",
            "forgotten why we came in here to begin\x01",
            "with.\x02\x03",

            "We're not here to shop.\x01",
            "We're supposed to be buying a copy\x01",
            "of the Liberl News for Dad, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#008FAh ha ha... Of course! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xB,
        (
            "Ha ha, you've always been a big\x01",
            "collector of those shoes, haven't\x01",
            "you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xB,
        (
            "I'm afraid that the new Stregas\x01",
            "aren't out yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xB,
        (
            "If you're after the latest issue of the\x01",
            "Liberl News though, I should have\x01",
            "them in around noon.\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(    #250
        0x101,
        (
            "#505FNoon, huh? ...That's right in the\x01",
            "middle of our training at the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xB, 500)

    ChrTalk(    #251
        0x102,
        (
            "#010FWe'll stop by again after our\x01",
            "training is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xB,
        "Sure. I'll be waiting for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EF7")

    label("loc_6B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DFB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BB0")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6B99")
    OP_A9(0x8)
    Jump("loc_6BA7")

    label("loc_6B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_6BA5")
    OP_A9(0x7)
    Jump("loc_6BA7")

    label("loc_6BA5")

    OP_A9(0x2)

    label("loc_6BA7")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_6BB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BC1")
    TalkEnd(0xB)
    Return()

    label("loc_6BC1")

    OP_A2(0x209)

    ChrTalk(    #253
        0xB,
        (
            "So the two of you are going to\x01",
            "be bracers, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xB,
        (
            "I'm jealous. I wanted to be a bracer\x01",
            "when I was a kid, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x102)

    ChrTalk(    #255
        0x102,
        (
            "#011FYou could probably say that every boy\x01",
            "in Liberl wants to be a bracer at least\x01",
            "once in their lives.\x02\x03",

            "Except that this one's a girl...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #256
        0x101,
        (
            "#009FWhy do you have to make such a\x01",
            "big deal out of things, Joshua?\x02\x03",

            "There are other female bracers like\x01",
            "Schera, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #257
        0x102,
        "#010FI didn't mean it in a bad way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xB,
        "Well, hang in there and study hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xB,
        (
            "When I get my copies of the Liberl\x01",
            "News in, I'll set one aside for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EF7")

    label("loc_6DFB")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E70")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6E59")
    OP_A9(0x8)
    Jump("loc_6E67")

    label("loc_6E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_END)), "loc_6E65")
    OP_A9(0x7)
    Jump("loc_6E67")

    label("loc_6E65")

    OP_A9(0x2)

    label("loc_6E67")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_6E70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E81")
    TalkEnd(0xB)
    Return()

    label("loc_6E81")


    ChrTalk(    #260
        0xB,
        "Well, hang in there and study hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xB,
        (
            "When I get my copies of the Liberl\x01",
            "News in, I'll set one aside for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF7")

    Jump("loc_7F51")

    label("loc_6EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773A")
    EventBegin(0x0)
    OP_A2(0x20A)
    Fade(1000)
    OP_6D(3870, 0, 1030, 0)
    SetChrPos(0x101, 3420, 0, 50, 0)
    SetChrPos(0x102, 4360, 0, 40, 0)
    OP_8C(0xB, 180, 0)
    OP_0D()

    ChrTalk(    #262
        0xB,
        "Hello there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xB,
        (
            "What are you in the market for today?\x01",
            "A new pair of shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#004FNow that you mention it, are there\x01",
            "any new ones in stock?\x02\x03",

            "#001FYou know, like...the newest Stregas?!!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x102,
        (
            "#018FUnbelievable. You've actually already\x01",
            "forgotten why we came in here to begin\x01",
            "with.\x02\x03",

            "We're not here to shop.\x01",
            "We're supposed to be buying a copy\x01",
            "of the Liberl News for Dad, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#008FAh ha ha... Of course!☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xB,
        (
            "Ha ha, you've always been a big\x01",
            "collector of those shoes, haven't\x01",
            "you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xB,
        (
            "I'm afraid that the new Stregas\x01",
            "aren't out yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xB,
        (
            "I do, however, have some copies\x01",
            "of the Liberl News in if that's what\x01",
            "you're after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        "#006FAll right, I'll take one copy then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xB,
        "That comes to 100 mira, please.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_724D")
    SubMira(100)
    Jump("loc_7315")

    label("loc_724D")


    ChrTalk(    #272
        0x101,
        "#004FCrap, we're short on cash!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x102,
        (
            "#017FAnd after Dad told you like a million\x01",
            "times not to waste money...\x02\x03",

            "#018FI guess I'll have to cover it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x101,
        "#007FI-I'm really sorry about this...\x02",
    )

    CloseMessageWindow()

    label("loc_7315")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #275
        "\x07\x00Purchased \x07\x02Liberl News - Issue 1\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x207)
    OP_3E(0x347, 1)

    ChrTalk(    #276
        0x101,
        (
            "#000FI know my dad always buys a copy\x01",
            "of this magazine...\x02\x03",

            "#000FBut does it really sell that well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xB,
        (
            "It sure does. The Liberl News has an excellent\x01",
            "reporter and camerawoman who have done a great\x01",
            "job reporting the latest and most reliable news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xB,
        (
            "They're even supposed to have a running\x01",
            "story related to Queen Alicia's birthday\x01",
            "celebration.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20B)

    ChrTalk(    #279
        0xB,
        (
            "But enough about that, why don't\x01",
            "you tell me how you did today?\x01",
            "Did you make it as bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xB,
        (
            "Today was your last day of training,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#502FYep. Everything went smoothly, too.\x02\x03",

            "#004FBut how did you know about all\x01",
            "that, Mr. Rinon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xB,
        (
            "Ha ha, in a certain sense, both you\x01",
            "and Joshua are like celebrities here\x01",
            "in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xB,
        (
            "I tend to hear a lot from customers\x01",
            "coming through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        (
            "#509FI shouldn't have expected anything less\x01",
            "from Rolent... The grapevine around here\x01",
            "is seriously something to be reckoned with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x102,
        (
            "#019FNo kidding. The women here especially\x01",
            "love to gossip...\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    EventEnd(0x0)
    Jump("loc_77E9")

    label("loc_773A")

    SetChrName("Rinon")

    ChrTalk(    #286
        0xB,
        (
            "Congratulations on passing the\x01",
            "bracer exam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xB,
        (
            "And in following with this joyous occasion,\x01",
            "how about you buy something, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xB,
        "I'll even give you a discount.\x02",
    )

    CloseMessageWindow()

    label("loc_77E9")

    Jump("loc_7F51")

    label("loc_77EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD3")
    EventBegin(0x0)
    OP_A2(0x20A)
    Fade(1000)
    OP_6D(3870, 0, 1030, 0)
    SetChrPos(0x101, 3420, 0, 50, 0)
    SetChrPos(0x102, 4360, 0, 40, 0)
    OP_8C(0xB, 180, 0)
    OP_0D()
    SetChrName("Rinon")

    ChrTalk(    #289
        0xB,
        "Hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xB,
        (
            "How can I help you?\x01",
            "Did you manage to become bracers?\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(    #291
        0x101,
        (
            "#502FYou bet we did!\x02\x03",

            "#502FMaybe I should have you start\x01",
            "calling me 'Hyper-Bracer Estelle'\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x102,
        (
            "#010FBy the way, Mr. Rinon.\x01",
            "Did the Liberl News come in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xB,
        "Yeah, it came in a little after noon.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #294
        0x101,
        "#009FDon't brush me off like that, you two!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #295
        0x101,
        "#007FOh, whatever...I'll take one copy then.\x02",
    )

    CloseMessageWindow()
    SetChrName("Rinon")

    ChrTalk(    #296
        0xB,
        "That comes to 100 mira, please.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A43")
    SubMira(100)
    Jump("loc_7B0B")

    label("loc_7A43")


    ChrTalk(    #297
        0x101,
        "#004FCrap, we're short on cash!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x102,
        (
            "#017FAnd after Dad told you like a million\x01",
            "times not to waste money...\x02\x03",

            "#018FI guess I'll have to cover it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#007FI-I'm really sorry about this...\x02",
    )

    CloseMessageWindow()

    label("loc_7B0B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #300
        "\x07\x00Purchased \x07\x02Liberl News - Issue 1\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x207)
    OP_3E(0x347, 1)

    ChrTalk(    #301
        0x101,
        (
            "#000FI know my dad always buys a copy\x01",
            "of this magazine...\x02\x03",

            "#000FBut does it really sell that well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xB,
        (
            "It sure does. The Liberl News has an excellent\x01",
            "reporter and camerawoman who have done a great\x01",
            "job reporting the latest and most reliable news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xB,
        (
            "They're even supposed to have a running\x01",
            "story related to Queen Alicia's birthday\x01",
            "celebration.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    EventEnd(0x0)
    Jump("loc_7F51")

    label("loc_7CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA2")
    OP_A2(0x20B)

    ChrTalk(    #304
        0x101,
        (
            "#505FBy the way, Mr. Rinon.\x02\x03",

            "#505FHow did you know that today was\x01",
            "our last day of training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xB,
        (
            "Ha ha, in a certain sense, both you\x01",
            "and Joshua are like celebrities here\x01",
            "in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xB,
        (
            "I tend to hear a lot from customers\x01",
            "coming through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        (
            "#509FI shouldn't have expected anything less\x01",
            "from Rolent... The grapevine around here\x01",
            "is seriously something to be reckoned with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        (
            "#019FNo kidding. The women here especially\x01",
            "love to gossip...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F51")

    label("loc_7EA2")

    SetChrName("Rinon")

    ChrTalk(    #309
        0xB,
        (
            "Congratulations on passing the\x01",
            "bracer exam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xB,
        (
            "And in following with this joyous occasion,\x01",
            "how about you buy something, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xB,
        "I'll even give you a discount.\x02",
    )

    CloseMessageWindow()

    label("loc_7F51")

    TalkEnd(0xB)
    Return()

    # Function_9_59F5 end

    def Function_10_7F55(): pass

    label("Function_10_7F55")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_80AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8023")
    OP_A2(0x7)

    ChrTalk(    #312
        0xFE,
        (
            "Are you going on a trip with\x01",
            "all that luggage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "Let me know if you find anyone\x01",
            "there who might make a good bride\x01",
            "for my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "I'll fly out there to meet them\x01",
            "in person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80A9")

    label("loc_8023")


    ChrTalk(    #315
        0xFE,
        (
            "Are you going on a trip with\x01",
            "all that luggage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "Let me know if you find anyone\x01",
            "there who might make a good bride\x01",
            "for my son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80A9")

    Jump("loc_8C5A")

    label("loc_80AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_830E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82DF")
    OP_A2(0x7)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #317
        0xFE,
        (
            "Oh my, you with the silver hair.\x01",
            "Are you a foreigner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x103,
        (
            "#020FAre you talking to me? Yeah sure,\x01",
            "I guess I'm something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "You're definitely a suitable age,\x01",
            "but for a bride, you're a bit too...exotic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x103,
        "#023FHuh? A bride?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#501F(I definitely can't imagine Schera\x01",
            "being anyone's bride...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#018F(Yeah, they'd have to be able to\x01",
            "keep up with her drinking, at the\x01",
            "very least.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#004F(Yeah, and let's face it,\x01",
            "who can do that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x103,
        (
            "#025FHey, you two! What are you\x01",
            "whispering about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_830B")

    label("loc_82DF")


    ChrTalk(    #325
        0xFE,
        (
            "*sigh* Finding a bride is\x01",
            "hard work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_830B")

    Jump("loc_8C5A")

    label("loc_830E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_864D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85F3")
    OP_A2(0x7)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #326
        0xFE,
        (
            "Aren't you Cassius' daughter...\x01",
            "Estelle, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x101,
        "#001FUh, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "You look rather healthy and\x01",
            "seem like a cheerful, young girl at\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "So how would you feel about\x01",
            "becoming my son's new wife?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#004FExcuse me?\x02\x03",

            "#501FM-Me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "It seems like the young girls\x01",
            "these days don't mind marrying\x01",
            "older men, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#008FN-Now hold on just a darn minute!\x01",
            "I-I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "...So is that a no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "Admittedly, my son isn't as handsome\x01",
            "as your boyfriend over there with the\x01",
            "black hair...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #335
        0xFE,
        (
            "You, boy. Make sure to make\x01",
            "Estelle happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x102,
        "#014FH-Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#008F(This nutjob lady is totally mistaken...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x102,
        (
            "#010F(Ha ha... We'd probably best just\x01",
            "play along before things get more\x01",
            "complicated.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_864A")

    label("loc_85F3")


    ChrTalk(    #339
        0xFE,
        (
            "With all these women working\x01",
            "nowadays, it's hard work finding\x01",
            "a bride for my son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_864A")

    Jump("loc_8C5A")

    label("loc_864D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_86E6")

    ChrTalk(    #340
        0xFE,
        (
            "I secretly decided to start looking\x01",
            "for bridal candidates for my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "I've been talking to girls who seem\x01",
            "to be at an agreeable age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C5A")

    label("loc_86E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_8896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87F4")
    OP_A2(0x7)

    ChrTalk(    #342
        0xFE,
        (
            "It looks like my son is too busy\x01",
            "with running his store to worry\x01",
            "about other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "Men reach manhood status by having\x01",
            "a family and rearing children, not\x01",
            "by staying single.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "I guess this is my time to give a\x01",
            "helping hand as a mother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8893")

    label("loc_87F4")


    ChrTalk(    #345
        0xFE,
        (
            "Men reach manhood status by having\x01",
            "a family and rearing children, not\x01",
            "by staying single.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "I guess this is my time to give a\x01",
            "helping hand as a mother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8893")

    Jump("loc_8C5A")

    label("loc_8896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_8918")

    ChrTalk(    #347
        0xFE,
        (
            "Rinon's a hard worker and\x01",
            "a good son...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "But as a parent, I'd like him to take\x01",
            "a wife and set my mind at ease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C5A")

    label("loc_8918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_8A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C2")
    OP_A2(0x7)

    ChrTalk(    #349
        0xC,
        (
            "The sun's already setting?\x01",
            "I guess it's about time I got\x01",
            "dinner ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xC,
        (
            "I sure wish a woman who could cook\x01",
            "would appear in my son's life...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0A")

    label("loc_89C2")


    ChrTalk(    #351
        0xC,
        (
            "I sure wish a woman who could cook\x01",
            "would appear in Rinon's life...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0A")

    Jump("loc_8C5A")

    label("loc_8A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B3F")
    OP_A2(0x7)

    ChrTalk(    #352
        0xC,
        (
            "I'm so glad that Rinon's store\x01",
            "has finally got on track.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xC,
        (
            "It seems as though it has become much\x01",
            "easier to get products since he started\x01",
            "having them brought in by airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xC,
        (
            "Ever since the first orbments were\x01",
            "invented, this world has become a\x01",
            "much easier place to live in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA7")

    label("loc_8B3F")


    ChrTalk(    #355
        0xC,
        (
            "Ever since the first orbments were\x01",
            "invented, this world has become a\x01",
            "much easier place to live in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA7")

    Jump("loc_8C5A")

    label("loc_8BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C1F")
    OP_A2(0x7)

    ChrTalk(    #356
        0xC,
        (
            "The morning air is so crisp\x01",
            "and fresh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xC,
        (
            "Let's see, it's about time I water\x01",
            "my lovely flowers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C5A")

    label("loc_8C1F")


    ChrTalk(    #358
        0xC,
        (
            "Let's see, it's about time I water\x01",
            "my lovely flowers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C5A")

    TalkEnd(0xC)
    Return()

    # Function_10_7F55 end

    def Function_11_8C5E(): pass

    label("Function_11_8C5E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD2")
    OP_A2(0x8)

    ChrTalk(    #359
        0xD,
        (
            "I wonder if Luke and Pat\x01",
            "are all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xD,
        "I tried my best to stop them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xD,
        "*sniffle*\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D11")

    label("loc_8CD2")


    ChrTalk(    #362
        0xD,
        (
            "Estelle, Joshua. Please bring\x01",
            "them back safely. *sniffle*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D11")

    TalkEnd(0xD)
    Return()

    # Function_11_8C5E end

    def Function_12_8D15(): pass

    label("Function_12_8D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DC0")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x320)

    def lambda_8D39():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8D39)

    def lambda_8D47():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8D47)

    ChrTalk(    #363
        0x9,
        (
            "#024FAnd just where do you think you're going?\x01",
            "We aren't finished with training.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8DC0")

    Return()

    # Function_12_8D15 end

    def Function_13_8DC1(): pass

    label("Function_13_8DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E6C")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x320)

    def lambda_8DE5():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8DE5)

    def lambda_8DF3():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8DF3)

    ChrTalk(    #364
        0x9,
        (
            "#024FAnd just where do you think you're going?\x01",
            "We aren't finished with training.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8E6C")

    Return()

    # Function_13_8DC1 end

    def Function_14_8E6D(): pass

    label("Function_14_8E6D")

    EventBegin(0x0)
    OP_4A(0x8, 0)
    ClearChrFlags(0x9, 0x80)
    ClearMapFlags(0x1)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_6D(342, 0, 115532, 0)
    OP_6B(3000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(    #365
        0x9,
        (
            "#020FYour final training is how to\x01",
            "report to the guild.\x02\x03",

            "#020FWhenever you finish a job, it is\x01",
            "your duty to report the results\x01",
            "of your work to the guild.\x02\x03",

            "#020FReporting how you resolved the situation\x01",
            "and the steps you took to get there are\x01",
            "all part of your job as a bracer.\x02\x03",

            "#020FYou can report your results to the front desk in\x01",
            "each guild branch. And as you already know by\x01",
            "now, Aina is in charge here at the Rolent branch.\x02\x03",

            "#020FIn addition, this is where you\x01",
            "will be paid for your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x8,
        (
            "#740FI look forward to seeing great\x01",
            "things from the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x9,
        (
            "#020FNow that we're here, why don't\x01",
            "you both go ahead and report\x01",
            "the results of today's training.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #368
        (
            "\x07\x05※Upon approaching the counter, a TALK mark will appear. Pressing the OK\x01",
            "button will display a list of options. Select 'Report' to report to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4B(0x8, 0)
    EventEnd(0x0)
    Return()

    # Function_14_8E6D end

    def Function_15_9226(): pass

    label("Function_15_9226")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Sleep(500)
    OP_2A(0xA, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9245")
    EventEnd(0x1)
    Return()

    label("loc_9245")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #369
        (
            "\x07\x05※Details of the job confirmed on the bulletin board and other important\x01",
            "events will be automatically recorded in the Bracer Notebook.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #370
        (
            "\x07\x05※The Bracer Notebook can be easily found by clicking on the 'Books' tab\x01",
            "of the 'Items' menu. It can also be accessed by configuring a Bracer Book\x01",
            "shortcut button on the 'Configuration' menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0xE)
    Fade(1000)
    OP_6D(-91, 0, 115143, 0)
    OP_44(0x9, 0xFF)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(    #371
        0x9,
        (
            "#020FVery good.\x02\x03",

            "#020FIt looks like you were able to\x01",
            "see what was posted without\x01",
            "any trouble.\x02\x03",

            "#020FChecking the bulletin board is one\x01",
            "of the most basic functions a bracer\x01",
            "performs on their job.\x02\x03",

            "#020FChecking regularly to see whether or not there\x01",
            "are any urgent tasks which need immediate\x01",
            "attention is also an important duty for bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        (
            "#007FMan, all this talk about duty is\x01",
            "starting to cramp my style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x102,
        (
            "#010FSure, there are a lot of rules to follow,\x01",
            "but there's an equal level of responsibility\x01",
            "in the jobs themselves.\x02\x03",

            "#010FI think being a bracer calls for\x01",
            "much more than just someone\x01",
            "with a half-hearted attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x101,
        (
            "#006F...Umm, I guess you're right.\x02\x03",

            "I'll just have to be more motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x9,
        (
            "#020FHIs that so?\x01",
            "Had a change of heart, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x101,
        "#001FYou bet'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x9,
        (
            "#020FWell, before all that motivation\x01",
            "sneaks off somewhere, let's get\x01",
            "to work on your next task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x102,
        "#010FWhat will we be doing this time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x9,
        (
            "#020FWe'll be heading across the street to\x01",
            "Mr. Melders' orbal factory and learning\x01",
            "about how to use its services.\x02\x03",

            "#020FHe has graciously taken time out of his\x01",
            "work schedule to explain things, so make\x01",
            "sure to be on your best behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x101,
        "#501FO-kay.\x02",
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T0120   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_15_9226 end

    def Function_16_98B7(): pass

    label("Function_16_98B7")

    EventBegin(0x0)
    OP_6D(740, 0, 117300, 0)
    OP_6B(3000, 0)
    SetChrPos(0x101, 780, 0, 115570, 0)
    SetChrPos(0x103, -440, 0, 116340, 45)
    SetChrPos(0x102, 1860, 0, 116020, 0)
    OP_44(0x8, 0xFF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #381
        0x8,
        (
            "#740FI understand the situation now.\x02\x03",

            "To be frank though, with Scherazard\x01",
            "taking off after Cassius, I'm going\x01",
            "to be really short-handed.\x02\x03",

            "But since this involves him directly,\x01",
            "please don't worry about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x103,
        (
            "#020FI really appreciate this, Aina.\x02\x03",

            "#021FMake good use of Ridge while\x01",
            "we're gone.\x02\x03",

            "He should be able to deal with\x01",
            "at least three times his normal\x01",
            "workload.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x101,
        "#506FDon't you think that's a bit harsh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x8,
        (
            "#741FDon't worry. If things get too hectic,\x01",
            "I'll ask for help from the\x01",
            "Grancel Branch.\x02\x03",

            "#740FBy the way, Scherazard.\x01",
            "Can I get a minute?\x02\x03",

            "I'd like to talk with you about the\x01",
            "job you were going to do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x103,
        "#020FSure, no problem.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #386
        0x103,
        (
            "#020FEstelle, Joshua, could I have\x01",
            "you two wait upstairs?\x02\x03",

            "I'll be done in a minute.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #387
        0x102,
        "#010F#2PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        (
            "#3P#505F...\x02\x03",

            "#501FUm, Schera?\x02\x03",

            "If we're going to be waiting, would\x01",
            "you mind if we did it out in front\x01",
            "of the clock tower?\x02\x03",

            "I'd like to say 'Hi' to someone...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #389
        0x102,
        "#014F#2P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x103,
        (
            "#026FOh, yeah. That's right.\x02\x03",

            "#020FOkay. Then let's meet up in front\x01",
            "of the clock tower.\x02\x03",

            "As soon as I'm done here,\x01",
            "I'll head over there myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        "#3P#000FGot it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #392
        0x101,
        "#3P#501FCome on, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x102,
        "#014F#2PUh, sure...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x2, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_98B7 end

    def Function_17_9DF0(): pass

    label("Function_17_9DF0")

    EventBegin(0x0)
    OP_6D(590, 0, 117600, 0)
    OP_67(0, 8010, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 780, 0, 115570, 0)
    SetChrPos(0x103, -440, 0, 116340, 45)
    SetChrPos(0x102, 1860, 0, 116020, 0)
    OP_44(0x8, 0xFF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #394
        0x8,
        (
            "#742FIt looks like you've had a rough day.\x01",
            "Who'd have thought the sky bandits\x01",
            "would appear...\x02\x03",

            "#742FI don't blame you for letting\x01",
            "them escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x103,
        (
            "#025FNo, this time it was my fault.\x01",
            "I should have been more careful.\x02\x03",

            "I'm really far from being in the\x01",
            "same league as Cassius...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        (
            "#003FIt's not your fault, Schera.\x02\x03",

            "#003FI let my emotions get the best\x01",
            "of me and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x102,
        "#015F#2PI was careless as well...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_A08E")

    ChrTalk(    #398
        0x103,
        (
            "#020FNo, you guys did a great job. Your\x01",
            "on-site investigation of the mayor's\x01",
            "residence was flawless, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19B")

    label("loc_A08E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_A11F")

    ChrTalk(    #399
        0x103,
        (
            "#020FNo, you guys did a great job. I'd even give\x01",
            "you a passing grade for your on-site\x01",
            "investigation of the mayor's residence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19B")

    label("loc_A11F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_A19B")

    ChrTalk(    #400
        0x103,
        (
            "#020FNo, you guys did a great job. Your\x01",
            "on-site investigation of the mayor's\x01",
            "residence on the other hand...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19B")

    TurnDirection(0x103, 0x8, 400)
    Sleep(500)

    ChrTalk(    #401
        0x103,
        (
            "#027FDon't you think you should\x01",
            "recommend them, Aina?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x8,
        (
            "#741FYes. I was thinking the\x01",
            "same thing as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #403
        0x101,
        "#004FRecommend?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x102,
        "#014F#2PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x8,
        (
            "#740FHold your horses! First comes the\x01",
            "payment for a job well done.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_28(0x1A, 0x4, 0x10)
    OP_AF(0x4, 0x1A)
    OP_28(0x1B, 0x4, 0x10)
    OP_28(0x1B, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #406
        0x8,
        (
            "#740FThis is for you both, and\x01",
            "take this as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x330, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #407
        "\x07\x00Received \x07\x02Recommendation\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #408
        0x101,
        "#004FTh-This is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x8,
        (
            "#740FAs of now, you are both junior bracers.\x01",
            "In other words, bracers-in-training.\x02\x03",

            "In order to become senior bracers, you'll\x01",
            "need to receive recommendations from\x01",
            "all regional branches in the kingdom.\x02\x03",

            "This is your recommendation\x01",
            "from the Rolent branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x101,
        "#008FIs it really okay for us to have this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x102,
        (
            "#014F#2PI had heard that in order to become\x01",
            "a full-fledged bracer we'd need to\x01",
            "achieve something fairly noteworthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        (
            "#741FI think in light of the jobs performed in\x01",
            "your father's stead and your great showing\x01",
            "here, your achievements are sufficient.\x02\x03",

            "#740FHowever, those achievements are\x01",
            "only for your work here in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #413
        0x103,
        (
            "#027FYou'll need to receive recommendations\x01",
            "from the other regional branches after\x01",
            "achieving success there as well.\x02\x03",

            "#027FBose, Ruan, Zeiss, and finally, Grancel...\x02\x03",

            "#021FYou've still got a long road ahead of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #414
        0x101,
        (
            "#001FEven so, I'm really happy.\x01",
            "It was worth all the hard work!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #415
        0x101,
        (
            "#006FNow that we've come this far,\x01",
            "don't you think we should visit\x01",
            "the other regions too, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #416
        0x102,
        (
            "#019F#2PI figured you'd say as much.\x02\x03",

            "#010FI agree with you, but we can't\x01",
            "decide this all by ourselves.\x02\x03",

            "#010FWe should discuss it with\x01",
            "Dad when he gets home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        "#006FRight!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_A8C5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8C5)

    def lambda_A8D3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8D3)

    def lambda_A8E1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A8E1)
    Sleep(1000)
    OP_8C(0x8, 315, 400)

    ChrTalk(    #418
        0x8,
        "#743FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x101,
        "#501FThat's the telephone, right?\x02",
    )

    CloseMessageWindow()

    def lambda_A932():
        OP_6D(-660, 0, 118480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A932)
    OP_8E(0x8, 0xFFFFFE52, 0x0, 0x1D0CE, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #420
        0x8,
        (
            "#740F#6PHello, this is the Bracer Guild's Rolent\x01",
            "branch in the Liberl Kingdom.\x02\x03",

            "#743FAh...it's been a while since we\x01",
            "last talked, hasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #421
        0x8,
        (
            "#742F#6PI see...\x02\x03",

            "#742F...Are you sure?\x02\x03",

            "#744FThat's terrible...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #422
        0x101,
        "#505FI wonder if something happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x102,
        "#012F#2PIt looks that way to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x8,
        (
            "#743F#6PYes, that's right. He left on\x01",
            "business the other day...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_21()
    OP_63(0x8)

    ChrTalk(    #425
        0x8,
        "#742F#3S#6PWhat?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    OP_1D(0x51)
    Sleep(400)

    ChrTalk(    #426
        0x8,
        (
            "#745F#6PI apologize, but this is a little\x01",
            "difficult to believe...\x02\x03",

            "Understood. I'll pass on the news\x01",
            "to his family.\x02\x03",

            "#742FThey'll be fine...\x01",
            "They're bracers, too.\x02\x03",

            "Yes. And if you hear anything else,\x01",
            "please let me know.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #427
        0x101,
        "#505FWhat's wrong, Aina?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x103,
        (
            "#020FIt's unusual for you to be so\x01",
            "surprised like that.\x02\x03",

            "Who was calling?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    def lambda_AD45():
        OP_6D(590, 0, 117600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD45)
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x2EE, 0x0, 0x1CF48, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #429
        0x8,
        (
            "#742FThe Bose branch.\x01",
            "Something terrible has happened...\x02\x03",

            "The airliner, Linde, has disappeared\x01",
            "over the Bose region.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #430
        0x101,
        "#004FWhaaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x102,
        "#012F#2PHow is that possible?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x8,
        (
            "#744FI don't know any of the details,\x01",
            "but...\x02\x03",

            "The Royal Army is currently\x01",
            "conducting a wide-scale search.\x02\x03",

            "Due to this event, all other flights\x01",
            "have been postponed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x103,
        (
            "#022FWell, that explains the back-up\x01",
            "at the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x8,
        (
            "#745FAnd...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x101,
        "#505FAina?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x8,
        (
            "#742FEstelle, Joshua, please\x01",
            "brace yourselves.\x02\x03",

            "#742F...Your father, Cassius, was aboard\x01",
            "the airliner which went missing.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(    #437
        0x101,
        "#580F#3SWha...\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #438
        0x102,
        "#016F#2PImpossible...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x103,
        (
            "#023FThere's got to be some kind\x01",
            "of mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x8,
        (
            "#742FIt seems his name was on the\x01",
            "passenger list.\x02\x03",

            "Liberl Bracer Guild, Rolent branch,\x01",
            "Senior Bracer...\x02\x03",

            "Cassius Bright, 45.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x40041, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x11, 0x0)
    OP_A2(0x269)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-87490, 0, 61990, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1A5")
    ShowSaveMenu()

    label("loc_B1A5")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    NewScene("ED6_DT01/T0301   ._SN", 3, 0, 0)
    IdleLoop()
    Return()

    # Function_17_9DF0 end

    def Function_18_B1F4(): pass

    label("Function_18_B1F4")

    EventBegin(0x0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x13)
    OP_43(0x102, 0x0, 0x0, 0x14)
    OP_43(0x101, 0x1, 0x0, 0x15)
    OP_4A(0x8, 0)
    OP_A2(0x3)
    OP_A5(0x3)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #441
        0x8,
        (
            "#740FThere you two are. Good morning, Estelle.\x01",
            "Good morning, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x101,
        "#001FMorning, Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x3)
    OP_A5(0x0)
    OP_A5(0x1)
    OP_A5(0x3)

    ChrTalk(    #444
        0x101,
        "#000F#6PIs Schera here already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x8,
        (
            "#740FYes, she's waiting for you upstairs.\x02\x03",

            "Once you finish today's training,\x01",
            "you'll finally be recognized as\x01",
            "members of the Bracer Guild.\x02\x03",

            "Good luck to the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x101,
        "#006F#6PThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4B(0x8, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x204)
    EventEnd(0x0)
    Return()

    # Function_18_B1F4 end

    def Function_19_B3D3(): pass

    label("Function_19_B3D3")

    OP_A6(0x0)
    OP_8E(0xFE, 0x898, 0x0, 0x1B968, 0xBB8, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C520, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_19_B3D3 end

    def Function_20_B402(): pass

    label("Function_20_B402")

    OP_A6(0x1)
    Sleep(200)
    OP_8E(0xFE, 0x7D0, 0x0, 0x1B580, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2BC, 0x0, 0x1C200, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_20_B402 end

    def Function_21_B436(): pass

    label("Function_21_B436")

    OP_A6(0x3)
    OP_6D(1500, 0, 116000, 1200)
    OP_A3(0x3)
    OP_A6(0x3)
    OP_6D(740, 0, 117400, 1500)
    OP_A3(0x3)
    Return()

    # Function_21_B436 end

    def Function_22_B465(): pass

    label("Function_22_B465")

    FadeToBright(1000, 0)
    OP_6D(-90, 0, 72340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, -400, 700, 73300, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -100, 700, 73300, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 200, 700, 73300, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 500, 700, 73300, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 800, 700, 73300, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 200, 200, 74100, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_43(0x101, 0x0, 0x0, 0x18)
    OP_43(0x102, 0x0, 0x0, 0x1C)
    OP_43(0x9, 0x0, 0x0, 0x1D)
    SetChrSubChip(0x12, 8)
    SetChrSubChip(0x13, 9)
    SetChrSubChip(0x14, 10)
    SetChrSubChip(0x15, 11)
    SetChrSubChip(0x16, 7)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 1)
    SetChrFlags(0x9, 0x2)
    OP_0D()
    Sleep(1000)
    SetChrSubChip(0x9, 0)
    Sleep(200)
    Fade(1000)
    SetChrFlags(0x16, 0x80)
    SetChrSubChip(0x9, 1)
    SetChrSubChip(0x16, 12)
    Sleep(1000)
    OP_99(0x9, 0x1, 0x3, 0x3E8)
    Sleep(500)

    ChrTalk(    #448
        0x9,
        (
            "#026F#4P...\x02\x03",

            "The Star and The Hanged Man...\x02\x03",

            "The Hermit and The Magician...\x02\x03",

            "...and last of all, inversion through\x01",
            "The Wheel of Fortune...\x02\x03",

            "#025FHmmm, this is a difficult combination.\x01",
            "How should I interpret this...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -4850, -2000, 66000, 0)
    ClearChrFlags(0x101, 0x8)

    ChrTalk(    #449
        0x101,
        "#2PGood morning, Schera!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_99(0x9, 0x3, 0x1, 0x4B0)
    Sleep(100)
    Fade(1000)
    SetChrSubChip(0x16, 12)
    ClearChrFlags(0x16, 0x80)
    Sleep(400)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 8)
    SetChrSubChip(0x9, 0)
    Sleep(1000)

    def lambda_B729():
        OP_6D(-2250, 0, 73500, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B729)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A5(0x0)
    OP_A5(0x1)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #450
        0x9,
        (
            "#023F#4PWell, if it isn't Estelle and Joshua!\x02\x03",

            "#023FThis is a rare occasion for the both\x01",
            "of you to show up so early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        (
            "#006FSince it's my last day of training,\x01",
            "I figured, 'Why not?'\x02\x03",

            "I'm ready to get this show on the\x01",
            "road and become a bracer myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x9,
        (
            "#025F#4PI'll give you credit for your enthusiasm.\x02\x03",

            "#020FBut I'm going to work you hard today in\x01",
            "every way I can think of to make sure\x01",
            "that high-spirited attitude of yours holds up.\x02\x03",

            "I hope you're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x101,
        (
            "#009FI can feel that enthusiasm\x01",
            "dropping already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x9,
        (
            "#022F#4PQuiet, you! \x02\x03",

            "Every time I teach you something,\x01",
            "you somehow manage to forget it...\x02\x03",

            "This training is my way of trying to keep some of\x01",
            "that information in your head instead of letting\x01",
            "it dribble out your ears like it usually does.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #455
        0x101,
        (
            "#504FWaaaah! Joshuaaa!\x01",
            "Schera's picking on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x102,
        (
            "#010FDon't worry, Schera.\x02\x03",

            "While Estelle may hate studying and\x01",
            "rarely ever does her homework...\x02\x03",

            "...acts rashly, is overly naive, and\x01",
            "has a tendency to stick her nose\x01",
            "into everything...\x02\x03",

            "...her instincts are sharp, so I'm sure\x01",
            "she'll pick up on how to use an orbment\x01",
            "with some practice. Eventually. Probably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x9,
        (
            "#025F#4PI guess there's not much I can do\x01",
            "now except hope for the best...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #458
        0x101,
        (
            "#509FHold on a sec, Joshua...\x02\x03",

            "Somehow I get the feeling that you\x01",
            "weren't standing up for me...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #459
        0x102,
        (
            "#019FWell, that's odd... I'm positive I described\x01",
            "all your best traits accurately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        "#007FWhatever...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #461
        0x101,
        (
            "#501FBy the way, Schera, what were you\x01",
            "trying to predict with your tarot\x01",
            "cards?\x02\x03",

            "Your face was really intent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x9,
        (
            "#522F#4POh, this?\x02\x03",

            "I was just trying to get a vague\x01",
            "reading about what might happen\x01",
            "in the near future...\x02\x03",

            "Unfortunately, I don't seem to\x01",
            "have been in the right mindset\x01",
            "to interpret the cards correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x101,
        "#505FYou couldn't read the cards?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x102,
        "#014FNow that's surprising to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x9,
        (
            "#020F#4PActually, the more profound the\x01",
            "meaning of the cards, the more\x01",
            "difficult they become to interpret.\x02\x03",

            "#020FBut that's not important now.\x01",
            "I think it's time we start your\x01",
            "final training.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(500, 0, -1)
    Sleep(1000)
    SetChrPos(0x101, 500, 0, 72250, 0)
    SetChrPos(0x102, -500, 0, 72250, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrSubChip(0x9, 0)
    OP_6D(-440, 0, 73390, 0)
    FadeToBright(500, 0)
    Sleep(1000)

    ChrTalk(    #466
        0x9,
        (
            "#020F#4PI'll give you a brief rundown of all\x01",
            "the information we've covered in\x01",
            "your previous training.\x02\x03",

            "#020FThis is the minimal level of knowledge\x01",
            "that bracers should have in order to\x01",
            "function effectively.\x02\x03",

            "#020FAnd, Estelle, make sure you pay\x01",
            "especially close attention to what\x01",
            "I'm going to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x101,
        "#006F#6PYeah, yeah.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -56)
    OP_0D()
    Sleep(500)

    label("loc_C140")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCC0")
    SetChrName("Scherazard")

    AnonymousTalk(    #468
        "\x06\x07\x00#020FWhat would you like to know about?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_C257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C1FE")

    Menu(
        0,
        200,
        100,
        0,
        (
            "[About Orbments]\x01",                 # 0
            "[About the Bracer Guild.]\x01",        # 1
            "[About the Liberl Kingdom.]\x01",      # 2
            "[That's all.]\x01",                    # 3
        )
    )

    Jump("loc_C254")

    label("loc_C1FE")


    Menu(
        0,
        200,
        100,
        0,
        (
            "[About Orbments.]\x01",                # 0
            "[About Bracers.]\x01",                 # 1
            "[About the Liberl Kingdom.]\x01",      # 2
            "[That's all.]\x01",                    # 3
        )
    )


    label("loc_C254")

    Jump("loc_C29F")

    label("loc_C257")


    Menu(
        0,
        200,
        100,
        0,
        (
            "[About Orbments.]\x01",                # 0
            "[About Bracers.]\x01",                 # 1
            "[About the Liberl Kingdom.]\x01",      # 2
        )
    )


    label("loc_C29F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C2C9"),
        (1, "loc_C2CC"),
        (2, "loc_C2E0"),
        (3, "loc_C2F4"),
        (SWITCH_DEFAULT, "loc_C301"),
    )


    label("loc_C2C9")

    Jump("loc_C301")

    label("loc_C2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C2DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C2DD")

    Jump("loc_C301")

    label("loc_C2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C2F1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C2F1")

    Jump("loc_C301")

    label("loc_C2F4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C301")

    label("loc_C301")

    OP_A2(0xA)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C321"),
        (1, "loc_C571"),
        (2, "loc_C748"),
        (4, "loc_CA74"),
        (3, "loc_CCAB"),
        (SWITCH_DEFAULT, "loc_CCBB"),
    )


    label("loc_C321")

    OP_AD(0x40013, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Scherazard")

    AnonymousTalk(    #469
        (
            "#020FOrbments are mechanical devices which operate by using what is known\x01",
            "as 'orbal energy.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #470
        (
            "#020FA variety of effects can be produced depending on their structure and\x01",
            "the type of quartz, or processed septium, installed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #471
        "#020FAlthough it's only been about 50 years since their invention...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #472
        (
            "#020FThese devices play an integral role in all facets of life from lights,\x01",
            "heaters, and other everyday products to weapons, magic, and even airships.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #473
        (
            "#020FIn connection, this technological reform is commonly known as the\x01",
            "'Orbal Revolution.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCBB")

    label("loc_C571")

    OP_A2(0xB)
    OP_AD(0x40015, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Scherazard")

    AnonymousTalk(    #474
        (
            "#020FBracers are investigative and combat specialists who work to protect\x01",
            "civilians and maintain the stability of their respective regions.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #475
        (
            "#020FThey aid the community in various ways such as exterminating monsters, \x01",
            "preventing crime, finding lost items, and escorting people and goods.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #476
        (
            "#020FThe Bracer Guild, which has established branches across the continent,\x01",
            "manages the affairs of the bracers in each region.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCBB")

    label("loc_C748")

    OP_AD(0x40014, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Scherazard")

    AnonymousTalk(    #477
        (
            "#020FThe kingdom of Liberl in which we live sits on the western half of the\x01",
            "Zemurian continent, and abounds with nature and deep-rooted traditions.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #478
        (
            "#020FLiberl is proud to be one of the leading producers of septium on the\x01",
            "continent and is known for its high level of technology used to develop\x01",
            "orbments.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #479
        (
            "#020FOrbment technology has also been a key pillar of support for Liberl in\x01",
            "protecting its independence as it has contended with neighboring nations.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #480
        (
            "#020FTen years ago, when Liberl was invaded by the Erebonian Empire, it was\x01",
            "the use of orbal-powered airships that saved the kingdom from defeat.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #481
        (
            "#020FConsequently, even now, our relationship with the Empire is somewhat\x01",
            "sensitive. But, thanks to the queen's political finesse, Liberl enjoys peace.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCBB")

    label("loc_CA74")

    OP_AD(0x40015, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Scherazard")

    AnonymousTalk(    #482
        (
            "#020FThe Bracer Guild is a worldwide organization\x01",
            "of bracers established 50 years ago.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #483
        (
            "#020FAside from the Liberl Kingdom, there are numerous\x01",
            "other branches set up across the continent which\x01",
            "promote peace and stability within their areas.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #484
        (
            "#020FDue to its international and neutral nature, it\x01",
            "often mediates between disputing powers, and it\x01",
            "even played a role in ending the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #485
        (
            "#025FHowever, as a consequence of the various roles the\x01",
            "Bracer Guild is required to fulfill, it is often\x01",
            "short-handed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jump("loc_CCBB")

    label("loc_CCAB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_CCBB")

    label("loc_CCBB")

    OP_56(0x0)
    Jump("loc_C140")

    label("loc_CCC0")

    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #486
        0x9,
        (
            "#020F#4PLet's see...since we've got a mountain of stuff\x01",
            "to do today, I'll let you off the hook this time\x01",
            "with a condensed review.\x02\x03",

            "#020FI'm going to speed things up now and move\x01",
            "on to the practical portion of your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x101,
        (
            "#505F#6PUh, Schera?\x02\x03",

            "How is today's practical training\x01",
            "any different from the training\x01",
            "we've done before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x9,
        (
            "#020F#4PSince it's practical, that means you\x01",
            "will be experiencing things firsthand.\x02\x03",

            "#020FTherefore, I am going to have the\x01",
            "both of you run through everything\x01",
            "as if this were a real bracer job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x101,
        (
            "#501F#6PSo what you're saying is...\x02\x03",

            "There won't be any studying\x01",
            "at a desk involved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x9,
        (
            "#027F#4PYes, that's exactly what I'm saying.\x02\x03",

            "#027FThis time you'll have to go out\x01",
            "and make a physical effort to\x01",
            "accomplish your task.\x02\x03",

            "#027FI'll make sure to have you work up\x01",
            "a sweat, so I hope you're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        (
            "#001F#6PYes! That's seriously just what\x01",
            "the doctor ordered.\x02\x03",

            "#001FI didn't know what I was going\x01",
            "to do if I had to sit another day\x01",
            "with my tush parked at a desk.\x02\x03",

            "#001FI guess I got all worried for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x102,
        (
            "#010F#3PWell, suddenly you're all bright\x01",
            "and cheerful, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x9,
        (
            "#026F#4PLet's just hope that smile on your\x01",
            "face lasts until the end of today's\x01",
            "training...\x02\x03",

            "#020FOkay. Let's get cracking on\x01",
            "your first objective, shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x101,
        "#508F#6PLet's have at it!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-91, 0, 115143, 0)
    OP_4A(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, -764, 0, 114882, 90)
    SetChrPos(0x101, 811, 0, 115528, 270)
    SetChrPos(0x102, 811, 0, 114132, 270)
    OP_0D()

    ChrTalk(    #495
        0x9,
        (
            "#020FYour first objective will be to\x01",
            "confirm the details of the job\x01",
            "you will be performing.\x02\x03",

            "#020F...But before that, there is something\x01",
            "that we need to give the both of you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #496
        0x9,
        "#020FAina, are they ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x8,
        "#740FYes, they are.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #498
        0x9,
        (
            "#020FAll right, you two. Go get one\x01",
            "for each of yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_4B(0x8, 0)
    EventEnd(0x0)

    def lambda_D3A1():

        label("loc_D3A1")

        TurnDirection(0x9, 0x1, 0)
        OP_48()
        Jump("loc_D3A1")

    QueueWorkItem2(0x9, 1, lambda_D3A1)
    Return()

    # Function_22_B465 end

    def Function_23_D3AD(): pass

    label("Function_23_D3AD")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 500, 0, 72250, 0)
    SetChrPos(0x102, -500, 0, 72250, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 8)
    SetChrPos(0x9, 200, 200, 74100, 180)
    OP_6D(-440, 0, 73390, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(    #499
        0x9,
        (
            "#020F#4PLet me say it again. Good work, you two.\x01",
            "You have now officially completed the\x01",
            "entire training course.\x02\x03",

            "#020FFrom now on, you will be learning \x01",
            "from your own real-world experience.\x02\x03",

            "#026FWell then...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #500
        "\x07\x05Scherazard holds out two small boxes.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #501
        0x101,
        "#004F#6PAren't those boxes the ones...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x9,
        (
            "#027F#4PIn answer to your question, yes, these\x01",
            "are the boxes you retrieved during\x01",
            "today's test.\x02\x03",

            "#027FYou seem awfully curious to find\x01",
            "out what's inside, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x101,
        (
            "#501F#6PAre you saying that it's okay\x01",
            "if we open them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x9,
        (
            "#020F#4PThat's right.\x02\x03",

            "#020FWhy don't the both of you have\x01",
            "a look and see what's inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x101,
        "#001F#6PSweet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0x102,
        "#010F#3PAll right, let's have a look.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #507
        "\x07\x05Estelle and Joshua open the boxes.\x02",
    )

    CloseMessageWindow()
    OP_AD(0x40022, 0xBE, 0x64, 0x1F4)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #508
        "\x07\x00Received \x07\x02Junior Bracer Emblem\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_3E(0x35C, 1)

    ChrTalk(    #509
        0x101,
        "#004F#6PThis crest is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x102,
        "#010F#3PSo does this mean that we're...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x9,
        (
            "#026F#4PAhem!\x02\x03",

            "#022FEstelle Bright. Joshua Bright.\x02\x03",

            "#022FBeginning this day at 1500 hours, you are\x01",
            "both hereby appointed as junior bracers\x01",
            "within the Bracer Guild.\x02\x03",

            "#022FFrom here on, you will work as members of the\x01",
            "Bracer Guild to support the livelihood of those\x01",
            "around you, defend peace, and uphold justice.\x02\x03",

            "#021FCongratulations, you two.\x01",
            "And welcome into the fold.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #512
        0x101,
        (
            "#001F#4PDid you hear that, Joshua?!\x02\x03",

            "#001FWe've become members of\x01",
            "the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(    #513
        0x102,
        (
            "#015F#3PSo I'm a bracer now, huh...?\x02\x03",

            "#015F...\x02\x03",

            "#011FI think the realization is only\x01",
            "now just beginning to sink in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x101,
        (
            "#006F#4PCome on, Joshua!\x02\x03",

            "#006FYou should be jumping for joy or\x01",
            "running around and screaming at\x01",
            "the top of your lungs like this:\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #515
        0x101,
        (
            "#001F#4P#4SLOOK AT US NOW, WORLD!\x01",
            "WE DID IT!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #516
        0x102,
        (
            "#018F#3PI was happy until you made my\x01",
            "eardrums bleed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x9,
        (
            "#021F#4PI hate to interrupt the celebrations,\x01",
            "Estelle, but I need to take off now.\x02\x03",

            "#021FI have some backed up work that\x01",
            "needs my immediate attention.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 0)
    TurnDirection(0x102, 0x9, 0)

    ChrTalk(    #518
        0x101,
        (
            "#501F#6PWe understand. You have been spending\x01",
            "a lot of extra hours working with us\x01",
            "during this busy time for the guild.\x02\x03",

            "#501FBefore you head out, Schera,\x01",
            "I just wanted to say thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x102,
        (
            "#010F#3PLikewise. I appreciate all the trouble\x01",
            "you've gone through for us, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x9,
        (
            "#027F#4PDon't mention it. Training new recruits\x01",
            "is one of a bracer's many duties.\x02\x03",

            "#027FBelieve it or not I was once in your\x01",
            "shoes a long time ago when your\x01",
            "father, Cassius, trained me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x101,
        (
            "#501F#6PSo that's why you have so much\x01",
            "respect for my dad, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x9,
        (
            "#020F#4PThere's actually much more to it\x01",
            "than that, but I'll save that\x01",
            "conversation for another day.\x02\x03",

            "#020FAs for the both of you, work hard to become full-\x01",
            "fledged bracers early on so you can help guide\x01",
            "those new recruits who come after yourselves.\x02\x03",

            "#020FAnd in time, I hope to see you\x01",
            "both become respectable bracers\x01",
            "like your father.\x02\x03",

            "#021FAnyway, I'll leave you with\x01",
            "that thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrPos(0x9, 200, 0, 74100, 180)
    ClearChrFlags(0x9, 0x10)
    Sleep(500)

    def lambda_E00E():

        label("loc_E00E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_E00E")

    QueueWorkItem2(0x101, 3, lambda_E00E)

    def lambda_E01F():

        label("loc_E01F")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_E01F")

    QueueWorkItem2(0x102, 3, lambda_E01F)
    OP_43(0x9, 0x0, 0x0, 0x1D)
    Sleep(200)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A2(0x2)
    Sleep(500)
    ClearChrFlags(0x9, 0x4)
    OP_A5(0x2)
    OP_A3(0x1)
    OP_A3(0x0)
    Sleep(200)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)

    ChrTalk(    #523
        0x101,
        (
            "#505F#4PUm...\x01",
            "I just don't get it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(    #524
        0x102,
        "#014F#3PGet what?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #525
        0x101,
        (
            "#505F#4PThis is Scherazard, aka 'The Silver Streak',\x01",
            "one of the most skilled young bracers we're\x01",
            "talking about.\x02\x03",

            "#505FSo why is it that she holds Dad\x01",
            "in such high esteem?\x02\x03",

            "#007FHe just seems like nothing more than a no-good\x01",
            "middle-aged man who is always out doing who\x01",
            "knows what instead of being a father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0x102,
        (
            "#015F#3PA no-good middle-aged man, huh...?\x02\x03",

            "#015FFrom your viewpoint, it doesn't\x01",
            "come as a surprise that you\x01",
            "would see him in that fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x101,
        "#004F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0x102,
        (
            "#010F#3P...Never mind.\x02\x03",

            "#010FLet's hurry and head home.\x02\x03",

            "#010FWe should let Dad know that\x01",
            "we qualified as junior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0x101,
        "#006F#4PRight!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x205)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_D3AD end

    def Function_24_E356(): pass

    label("Function_24_E356")

    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFFED0E, 0x0, 0x11558, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0x118DC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x0)
    OP_A6(0x0)

    label("loc_E38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E3A0")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_E38E")

    label("loc_E3A0")

    Return()

    # Function_24_E356 end

    def Function_25_E3A1(): pass

    label("Function_25_E3A1")

    Sleep(600)
    OP_8E(0x101, 0x32A, 0x0, 0x1C4B2, 0x7D0, 0x0)
    TurnDirection(0x101, 0xF, 400)
    Return()

    # Function_25_E3A1 end

    def Function_26_E3C2(): pass

    label("Function_26_E3C2")

    OP_8E(0x102, 0x762, 0x0, 0x1C3CC, 0x7D0, 0x0)
    TurnDirection(0x102, 0xF, 400)
    Return()

    # Function_26_E3C2 end

    def Function_27_E3DE(): pass

    label("Function_27_E3DE")

    Sleep(300)
    OP_8E(0x9, 0xFFFFFFA6, 0x0, 0x1C246, 0x7D0, 0x0)
    TurnDirection(0x9, 0xF, 400)
    Return()

    # Function_27_E3DE end

    def Function_28_E3FF(): pass

    label("Function_28_E3FF")

    OP_A6(0x1)
    SetChrPos(0xFE, -4850, -2000, 66000, 0)
    ClearChrFlags(0xFE, 0x8)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFED0E, 0x0, 0x11558, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF24A, 0x0, 0x11A08, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_E452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E464")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("loc_E452")

    label("loc_E464")

    Return()

    # Function_28_E3FF end

    def Function_29_E465(): pass

    label("Function_29_E465")

    OP_A6(0x2)
    OP_8E(0xFE, 0xFFFFF45C, 0x0, 0x12174, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_8E(0xFE, 0xFFFFEC46, 0x0, 0x11422, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEC46, 0xFFFFF830, 0x1027A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Return()

    # Function_29_E465 end

    def Function_30_E4B8(): pass

    label("Function_30_E4B8")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4A(0x8, 0)
    OP_6B(2800, 0)
    SetChrPos(0x101, 1500, 0, 116000, 0)
    SetChrPos(0x102, 700, 0, 115200, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(    #530
        0x8,
        (
            "#740FIt seems like you've had\x01",
            "quite a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x101,
        (
            "#007FDad is just unbelievable...\x02\x03",

            "#007FThe second we get back to Rolent\x01",
            "he says, 'I'll leave the reporting to\x01",
            "you,' and takes off for home.\x02\x03",

            "#007FThe sheer nerve, I tell you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x102,
        (
            "#010FThere's no need to make a mountain\x01",
            "out of a mole hill over it. At least the\x01",
            "boys came back safe and sound.\x02\x03",

            "#010FAnyway, I think that's all\x01",
            "there is to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x1, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x4, 0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #533
        0x8,
        (
            "#740FYou did well for your first\x01",
            "assignment.\x02\x03",

            "From the details of your report\x01",
            "alone, I believe I can commend\x01",
            "you both for a job well done.\x02\x03",

            "You should be proud of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0x101,
        "#008FY-You really think so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0x8,
        (
            "#741FI know so. In fact, you'll do even\x01",
            "better on your next job.\x02\x03",

            "If anything else comes up,\x01",
            "I would appreciate your help again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0x101,
        "#003FSure...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #537
        0x102,
        (
            "#010F...\x02\x03",

            "#010FHow about we head home,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #538
        0x101,
        (
            "#000FI guess we'd better...\x02\x03",

            "#000FI've still got dinner to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #539
        0x8,
        (
            "#743FWould you mind holding on a second?\x01",
            "A letter arrived for your father just a\x01",
            "little while ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #540
        0x8,
        (
            "#740FUnfortunately, since he went straight home, \x01",
            "I never got a chance to give it to him.\x01",
            "Do you think you could deliver it instead?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #541
        "\x07\x00Received \x07\x02Letter to Cassius\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x336, 1)

    ChrTalk(    #542
        0x101,
        (
            "#000FI wonder if it's more work-related\x01",
            "stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x8,
        (
            "#740FI imagine so. The letter appears to\x01",
            "be from one of our foreign branches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x102,
        (
            "#014FOne of the guild's foreign\x01",
            "branches...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x8,
        (
            "#740FAs I'm sure you already know by\x01",
            "now, Liberl isn't the only country\x01",
            "where the Bracer Guild exists.\x02\x03",

            "On top of that, your father is widely known all\x01",
            "across the Zemurian Continent, so we can expect\x01",
            "these kinds of letters from time to time.\x02\x03",

            "If you two would be so kind as to\x01",
            "make sure that he gets this letter,\x01",
            "I would really appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x212)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4B(0x8, 0)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_30_E4B8 end

    def Function_31_EC4D(): pass

    label("Function_31_EC4D")


    ChrTalk(    #546
        0xB,
        (
            "One more thing before you go.\x01",
            "This gift is my way of saying\x01",
            "congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xB,
        (
            "It's a free sample item I received with\x01",
            "my shipment of goods--but don't hold\x01",
            "the 'free' part against me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #548
        "\x07\x00Received \x07\x02Recipe Book\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x20D, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(100)

    ChrTalk(    #549
        0x101,
        (
            "#004FWhat's this supposed to be for?\x01",
            "There's a ton of blank pages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x102,
        "#014FIt's...a Recipe Book, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0xB,
        (
            "You got it. When you get hurt fighting, if you\x01",
            "just limit yourself to healing balms all the time,\x01",
            "it's going to cut pretty deep into your wallets.\x02\x03",

            "This is where a Recipe Book comes into\x01",
            "play. If you eat food to recover your\x01",
            "strength instead, it's basically free.\x02\x03",

            "Assuming you have all the ingredients, anyway.\x01",
            "So, if you eat something new, write down what's\x01",
            "in it, and you'll have lots of recipes in no time.\x02\x03",

            "So how about we try this out?\x01",
            "Go ahead and eat this cookie,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #552
        "\x07\x00Received \x07\x02Maple Cookie\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #553
        0x101,
        (
            "#001FWell, I have made it a personal\x01",
            "rule to never turn down sweets.♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #554
        "\x06\x07\x00Ate \x07\x02Maple Cookie\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_31(0x0, 0xFD, 0x50)
    OP_AC(0x14)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #555
        "\x06\x07\x00Learned '\x07\x02Maple Cookie\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #556
        0xB,
        (
            "Basically, all you have to do is\x01",
            "eat the food to learn the recipe.\x01",
            "It's as simple as that.\x02\x03",

            "As you're traveling about, you should eat\x01",
            "\x07\x04whatever food you come across\x07\x00 that you\x01",
            "haven't had an opportunity to try before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x102,
        "#010FWell, that sounds pretty convenient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x101,
        (
            "#505FUm... It's not that I don't like\x01",
            "cooking and all, it's just that\x01",
            "I never seem to get any better...\x02\x03",

            "#006FI'd sure love to be able to increase\x01",
            "my repertoire and really shock my\x01",
            "dad's taste buds for once in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0xB,
        (
            "That's the spirit!\x02\x03",

            "And in passing, if you're in need of\x01",
            "any ingredients, I'd be delighted to\x01",
            "service your cooking needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x101,
        (
            "#001FYou really know how to solicit\x01",
            "your customers, Mr. Rinon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x102,
        (
            "#019FThank you for the recipe book.\x01",
            "We'll put it to good use.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #562
        (
            "\x07\x05※Eating the 'Recommended Dish' at restaurants or using 'To-Go Meals'\x01",
            "adds the recipe to the Recipe Book.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #563
        (
            "\x07\x05※By selecting the Recipe Book, all learned recipes will be displayed. As long\x01",
            "as the necessary ingredients are available, the food can be made.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #564
        (
            "\x07\x05※There are two types of food: 'Sit-Down' meals which must be eaten on\x01",
            "the spot and 'To-Go' meals which can be carried as items. 'Sit-Down'\x01",
            "meals cannot be carried as items.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #565
        (
            "\x07\x05※Ingredients used for cooking can be bought at a store or acquired from\x01",
            "monsters.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Return()

    # Function_31_EC4D end

    SaveToFile()

Try(main)
