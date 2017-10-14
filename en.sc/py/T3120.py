from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3120   ._SN',
            'ED6_DT21/T3120_1 ._SN',
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
        'Kilika',                               # 9
        'Professor Russell',                    # 10
        'Tita',                                 # 11
        'Measure',                              # 12
        'Measure',                              # 13
        'Measure',                              # 14
        'Olivier',                              # 15
        'Kloe',                                 # 16
        'Factory Chief Murdock',                # 17
        'Zin',                                  # 18
        'Elwyn',                                # 19
        'Elkan',                                # 20
        'Ada',                                  # 21
        'Didi',                                 # 22
        'Wong',                                 # 23
        'Scherazard',                           # 24
        'Agate',                                # 25
        'Jimmy',                                # 26
        'Monika',                               # 27
        'ダミー',                               # 28
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00033 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT07/CH02620 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH00023 ._CH',             # 0F
        'ED6_DT07/CH00053 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00073 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH02490 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00033P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT07/CH02620P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH00023P._CP',             # 0F
        'ED6_DT07/CH00053P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00073P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH02490P._CP',             # 14
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1000,
        Y                   = 53000,
        Direction           = 183,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52970,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 172,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 52390,
        Z                   = 0,
        Y                   = 53790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55570,
        Z                   = 0,
        Y                   = 51740,
        Direction           = 63,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 25480,
        Z                   = 0,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = -3440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40,
        Z                   = 1000,
        Y                   = 50980,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -50,
        Y                   = 0,
        Z                   = -7200,
        Range               = 3010,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE98A,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_482",          # 00, 0
        "Function_1_771",          # 01, 1
        "Function_2_7BA",          # 02, 2
        "Function_3_861",          # 03, 3
        "Function_4_8B2",          # 04, 4
        "Function_5_8B7",          # 05, 5
        "Function_6_1385",         # 06, 6
        "Function_7_1943",         # 07, 7
        "Function_8_2056",         # 08, 8
        "Function_9_205B",         # 09, 9
        "Function_10_2BE5",        # 0A, 10
        "Function_11_4F88",        # 0B, 11
        "Function_12_5AA5",        # 0C, 12
        "Function_13_5D09",        # 0D, 13
        "Function_14_8F9D",        # 0E, 14
        "Function_15_92B4",        # 0F, 15
        "Function_16_B4B1",        # 10, 16
        "Function_17_B4E1",        # 11, 17
        "Function_18_B511",        # 12, 18
        "Function_19_B541",        # 13, 19
        "Function_20_B571",        # 14, 20
        "Function_21_BF93",        # 15, 21
        "Function_22_BFC4",        # 16, 22
        "Function_23_BFFE",        # 17, 23
        "Function_24_C038",        # 18, 24
        "Function_25_C072",        # 19, 25
        "Function_26_C0AC",        # 1A, 26
        "Function_27_C7C8",        # 1B, 27
        "Function_28_C860",        # 1C, 28
        "Function_29_C8C6",        # 1D, 29
    )


    def Function_0_482(): pass

    label("Function_0_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD")
    OP_A3(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23530, 200, -2100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 18)
    OP_A2(0x9)

    label("loc_4D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_508")
    SetChrPos(0xE, 23530, 200, -2100, 0)
    OP_A2(0xA)
    Jump("loc_51C")

    label("loc_508")

    SetChrPos(0xE, 23530, 200, 400, 180)
    OP_A3(0xA)

    label("loc_51C")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    OP_A2(0x9)

    label("loc_529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C")
    SetChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xF, 23530, 200, -2100, 0)
    OP_A2(0xB)
    Jump("loc_56F")

    label("loc_55B")

    SetChrPos(0xF, 23530, 200, 400, 180)
    OP_A3(0xB)

    label("loc_56F")

    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 7)
    OP_A2(0x9)

    label("loc_57C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 23530, 200, 400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 17)
    OP_A2(0x9)

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5C1")
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_601")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0x16, 61080, 2000, 2170, 0)
    Jump("loc_601")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5F0")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_601")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_601")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_601")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_643")
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x17, 23550, 200, 420, 180)

    label("loc_643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrChipByIndex(0x18, 16)
    SetChrPos(0x18, 26270, 200, -480, 90)

    label("loc_670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69D")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 17)
    SetChrPos(0xA, 28530, 200, -570, 270)

    label("loc_69D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CA")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 18)
    SetChrPos(0x11, 23550, 200, -2170, 0)

    label("loc_6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6E0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 16)
    Jump("loc_770")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6FF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_770")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_71E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_770")

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_734")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 13)
    Jump("loc_770")

    label("loc_734")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_740"),
        (SWITCH_DEFAULT, "loc_770"),
    )


    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_758")
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_76D")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    SetMapFlags(0x10000000)
    Event(1, 22)

    label("loc_76D")

    Jump("loc_770")

    label("loc_770")

    Return()

    # Function_0_482 end

    def Function_1_771(): pass

    label("Function_1_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 4)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B9")
    OP_44(0x15, 0x0)
    SetChrFlags(0x15, 0x10)
    OP_51(0x15, 0x1, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9")

    Return()

    # Function_1_771 end

    def Function_2_7BA(): pass

    label("Function_2_7BA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_7EB"),
        (1, "loc_7F7"),
        (2, "loc_803"),
        (3, "loc_80F"),
        (4, "loc_81B"),
        (5, "loc_827"),
        (6, "loc_833"),
        (SWITCH_DEFAULT, "loc_83F"),
    )


    label("loc_7EB")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_84B")

    label("loc_7F7")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_84B")

    label("loc_803")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_84B")

    label("loc_80F")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_84B")

    label("loc_81B")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_84B")

    label("loc_827")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_84B")

    label("loc_833")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_83F")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_84B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_860")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_860")

    Return()

    # Function_2_7BA end

    def Function_3_861(): pass

    label("Function_3_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_88E")

    label("loc_868")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88B")
    OP_8D(0xFE, 58120, 52460, 56040, 51120, 3000)
    Jump("loc_868")

    label("loc_88B")

    Jump("loc_8B1")

    label("loc_88E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B1")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("loc_88E")

    label("loc_8B1")

    Return()

    # Function_3_861 end

    def Function_4_8B2(): pass

    label("Function_4_8B2")

    Call(0, 5)
    Return()

    # Function_4_8B2 end

    def Function_5_8B7(): pass

    label("Function_5_8B7")

    TalkBegin(0x12)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_A9(0x9E)
    Jump("loc_8DE")

    label("loc_8DC")

    OP_A9(0x98)

    label("loc_8DE")

    TalkEnd(0x12)
    Return()

    label("loc_8E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F6")
    TalkEnd(0x12)
    Return()

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")

    ChrTalk(    #0
        0x12,
        (
            "A bit ago, someone came from the central\x01",
            "factory and bought some lamp oil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        (
            "They used nothing but orbal lights over there,\x01",
            "so I'm sure they're having a tough time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        (
            "Thanks to the glasses they designed, you\x01",
            "can even make it through the pitch black\x01",
            "dark of the Kaldia Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        "I feel kind of bad for just complaining now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B3A")

    label("loc_A5C")


    ChrTalk(    #4
        0x12,
        (
            "It's impossible to see anything in the Kaldia\x01",
            "Tunnel right now, so if you're going through\x01",
            "there, you'd better buy some glasses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x12,
        (
            "They're a special design from the central\x01",
            "factory that let you see in dark places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3A")

    Jump("loc_1381")

    label("loc_B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8E")

    ChrTalk(    #6
        0x12,
        "Welcome to Bell Station General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "Everyone seems pretty disturbed by all this.\x01",
            "I've had customers in and out of here all\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        (
            "Apparently the Kaldia Tunnel is pretty much\x01",
            "impassable in the dark, but with the goggles\x01",
            "here, no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "If you're going towards Ruan,\x01",
            "make sure you buy some.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_D9E")

    label("loc_C8E")


    ChrTalk(    #10
        0x12,
        (
            "Everyone seems pretty disturbed by all this.\x01",
            "I've had customers in and out of here all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "Apparently the Kaldia Tunnel is pretty much impassable\x01",
            "in the dark, but with the goggles here, no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        (
            "If you're going towards Ruan,\x01",
            "make sure you buy some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9E")

    Jump("loc_1381")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E2E")

    ChrTalk(    #13
        0x12,
        (
            "Seems like there won't be any\x01",
            "more earthquakes for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "The central factory announced it,\x01",
            "so it must be true.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC3")

    label("loc_E2E")


    ChrTalk(    #15
        0x12,
        "Welcome to Bell Station General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "Apparently there won't be any more earthquakes,\x01",
            "so why not celebrate by doing a little shopping?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EC3")

    Jump("loc_1381")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_10A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FA9")

    ChrTalk(    #17
        0x12,
        (
            "My wife went to go get some medicine\x01",
            "from the church, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "She's kind of late on her way back, though.\x01",
            "Wonder if something else came up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "Usually she comes right back after\x01",
            "a bit of prayer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109D")

    label("loc_FA9")


    ChrTalk(    #20
        0x12,
        "My wife goes to Church a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "She's got a really bad case of shoulder pain,\x01",
            "so she gets medicine from Father Vixen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "But, hmm... She's kind of late getting\x01",
            "back today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "Usually she comes right back\x01",
            "after a bit of prayer...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_109D")

    Jump("loc_1381")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #24
        0x12,
        (
            "The factory getting attacked is\x01",
            "still a nasty memory, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        (
            "Thanks to that, we were able to recall how\x01",
            "we felt when we started this business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1252")

    label("loc_114A")


    ChrTalk(    #26
        0x12,
        (
            "Before we opened, my wife and I fought\x01",
            "a bit over where to set up the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "But, after the central factory got attacked,\x01",
            "we spent some time really talking things over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "The two of us are really committed to\x01",
            "running a store both of us could love.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1252")

    Jump("loc_1381")

    label("loc_1255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1300")

    ChrTalk(    #29
        0x12,
        (
            "We're really proud of our wide selection\x01",
            "of stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "We've got everything from food to daily goods.\x01",
            "I'm sure you'll find what you're looking for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_1300")


    ChrTalk(    #31
        0x12,
        "Welcome to Bell Station General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "I refuse to give into any earthquakes,\x01",
            "so we're open for business today too!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1381")

    TalkEnd(0x12)
    Return()

    # Function_5_8B7 end

    def Function_6_1385(): pass

    label("Function_6_1385")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #33
        0xFE,
        (
            "Orbments aren't working, so chores have\x01",
            "become a real pain in the butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If I don't get the medicine for my shoulder,\x01",
            "doing any kind of work is quite painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "*sigh* I'd really love to take some time\x01",
            "off and relax at the Elmo hot springs.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_152F")

    label("loc_149A")


    ChrTalk(    #36
        0xFE,
        (
            "Chores are so difficult now that my shoulders\x01",
            "hurt even more than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I've got to go get some shoulder medicine\x01",
            "from the church, soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152F")

    Jump("loc_193F")

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164F")

    ChrTalk(    #38
        0xFE,
        (
            "Emergency goods are practically flying off\x01",
            "the shelves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "That just shows how much trouble\x01",
            "everyone's in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "If this situation keeps up, business\x01",
            "will be the least of our problems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I hope the central factory folk can\x01",
            "do something about it soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_16E3")

    label("loc_164F")


    ChrTalk(    #42
        0xFE,
        (
            "If this situation keeps up, business\x01",
            "will be the least of our problems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I hope the central factory folk can\x01",
            "do something about it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_193F")

    label("loc_16E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1763")

    ChrTalk(    #44
        0xFE,
        "Seems like the earthquakes have settled down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The church really is invaluable in\x01",
            "times of crisis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BF")

    label("loc_1763")


    ChrTalk(    #46
        0xFE,
        "Seems the earthquakes have settled down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Heehee. It was worth all that prayer.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_17BF")

    Jump("loc_193F")

    label("loc_17C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_193F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1875")

    ChrTalk(    #48
        0xFE,
        (
            "I'm going to go get some shoulder\x01",
            "medicine from Father Vixen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I'll also spend some real time praying there\x01",
            "for the earthquakes to stop while I'm at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_1875")


    ChrTalk(    #50
        0xFE,
        "I never want to experience another earthquake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I just can't calm down. The ground feels\x01",
            "like it could shake again at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Today I should probably spend some serious\x01",
            "time praying.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_193F")

    TalkEnd(0x14)
    Return()

    # Function_6_1385 end

    def Function_7_1943(): pass

    label("Function_7_1943")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE5")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #53
        0xFE,
        "Tiiita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Why isn't da owbments wowking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        (
            "#063FUmm, sorry.\x02\x03",

            "All of us are trying real hard to find\x01",
            "that out right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "Awww, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        (
            "#060FJust you hold on a bit longer.\x02\x03",

            "I promise I'll make it all better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Oh, okaaay. I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Guess imma pway da sushpenshun\x01",
            "fenomanon game till then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x107,
        (
            "#067FY-Yeah, good idea.\x01",
            "(Wh-What kind of game is that...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20C1)
    Jump("loc_1CCE")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B5F")

    ChrTalk(    #61
        0xFE,
        (
            "Untwil the owbments is wowking, I'm gonna\x01",
            "pway da sushpenshun fenomanon game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Bye, Tiiita.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1BCC")

    ChrTalk(    #63
        0xFE,
        "Mom's showlder is real hurty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I wonder if it's cause of the owbul sushpenshun\x01",
            "fenomanon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA0")

    ChrTalk(    #65
        0xFE,
        "Hey, look, look. I got a new game.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I thought it up. Let's pway pwetend sushpenshun\x01",
            "fenomanon.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    Sleep(500)

    ChrTalk(    #67
        0xFE,
        "Gooooo, owbuls suspend!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "Pew pew!\x02",
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x0)
    SetChrFlags(0xFE, 0x10)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x13)
    OP_A2(0x2)
    Jump("loc_1CCE")

    label("loc_1CA0")


    ChrTalk(    #69
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "(Da owbuls are now sushpended.)\x02",
    )

    CloseMessageWindow()

    label("loc_1CCE")

    Jump("loc_2052")

    label("loc_1CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D41")

    ChrTalk(    #71
        0xFE,
        (
            "Ah, but if qwakes come, then my bwother\x01",
            "will get mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "... Yeah, that would be baaad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1D41")


    ChrTalk(    #73
        0xFE,
        "Aww, there's not gonna be no more qwakes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "I kinda liked 'em.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D8B")

    Jump("loc_2052")

    label("loc_1D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DE4")

    ChrTalk(    #75
        0xFE,
        "Hmm, Mom's late today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "She always comes wight back, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E29")

    label("loc_1DE4")


    ChrTalk(    #77
        0xFE,
        "Hmm, Mom's late today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "She's not back from da Church...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1E29")

    Jump("loc_2052")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(    #79
        0xFE,
        "Pwaying pwetend qwuake is fun, huh.\x02",
    )

    CloseMessageWindow()

    def lambda_1E69():
        OP_9E(0xFE, 0x1E, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1E69)

    ChrTalk(    #80
        0xFE,
        "Gwaaah, another one!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1E9A")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #81
        0xFE,
        "Ah, Tiiita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Let's pway pwetend qwakes.\x01",
            "Come on, pwetend qwakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        (
            "#064FPretend earthquakes?\x02\x03",

            "You imitate an earthquake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "Yep, like this.\x02",
    )

    CloseMessageWindow()

    def lambda_1F53():
        OP_9E(0xFE, 0x1E, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1F53)

    ChrTalk(    #85
        0xFE,
        "Rrumbubububu...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Gwaaah, it's qwaaake!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1F9A")

    OP_44(0xFE, 0x1)
    Jump("loc_2052")

    label("loc_1FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1FFE")

    ChrTalk(    #87
        0xFE,
        "If you want Momma, she went to the church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "She went to get meeeeedicine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2052")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(    #89
        0xFE,
        "It's called qwake when the ground rumble-rumbles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "Didja know that?\x02",
    )

    CloseMessageWindow()

    label("loc_2052")

    TalkEnd(0x15)
    Return()

    # Function_7_1943 end

    def Function_8_2056(): pass

    label("Function_8_2056")

    Call(0, 9)
    Return()

    # Function_8_2056 end

    def Function_9_205B(): pass

    label("Function_9_205B")

    TalkBegin(0x13)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2089")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2080")
    OP_A9(0xA9)
    Jump("loc_2082")

    label("loc_2080")

    OP_A9(0x97)

    label("loc_2082")

    TalkEnd(0x13)
    Return()

    label("loc_2089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209A")
    TalkEnd(0x13)
    Return()

    label("loc_209A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2170")

    ChrTalk(    #91
        0x13,
        (
            "Guns have always been our main trade,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        (
            "This time we've got a bunch of\x01",
            "good close range weaponry in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x13,
        (
            "I didn't really want to, but...well,\x01",
            "sometimes you don't have a choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2215")

    label("loc_2170")


    ChrTalk(    #94
        0x13,
        (
            "We've shed some of our main stock of guns\x01",
            "and picked up some close range weaponry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x13,
        (
            "I didn't really want to, but...well,\x01",
            "sometimes you don't have a choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2215")

    Jump("loc_2BE1")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_23E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235C")

    ChrTalk(    #96
        0x13,
        (
            "Oh, man... Our big seller's always\x01",
            "been orbal guns, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x13,
        (
            "Thanks to this damned orbal shutdown thing\x01",
            "going on, our sales have redlined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        "Just what the heck is the central factory doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x13,
        (
            "My livelihood's on the line here!\x01",
            "Those researchers don't seem\x01",
            "to get that we're in a crisis here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_23E4")

    label("loc_235C")


    ChrTalk(    #100
        0x13,
        "Just what the heck is the central factory doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x13,
        (
            "I don't care about the theory.\x01",
            "Find the cause of the abnormality and fix it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E4")

    Jump("loc_2BE1")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2514")

    ChrTalk(    #102
        0x13,
        (
            "The Reinford Company in the Empire and\x01",
            "the Verne Company from the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x13,
        (
            "Those two are arguably the really\x01",
            "big orbal gun makers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x13,
        (
            "Of course, the Zeiss Central Factory's\x01",
            "no slouch, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x13,
        (
            "I'd love for the central factory mark to mean\x01",
            "the world's best someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263F")

    label("loc_2514")


    ChrTalk(    #106
        0x13,
        (
            "That reminds me, there's that non-aggression\x01",
            "pact signing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x13,
        (
            "We have dealings with Imperial gun makers,\x01",
            "so I'll admit I'm pretty interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        (
            "You've heard of the Reinford Company,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x13,
        (
            "They actually make more than just guns.\x01",
            "Tanks are also their specialty, as it happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_263F")

    Jump("loc_2BE1")

    label("loc_2642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_26F0")

    ChrTalk(    #110
        0x13,
        (
            "For Stain to like something even when\x01",
            "it's still in development is real rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x13,
        (
            "If they find a good tester, I'm sure\x01",
            "that'll turn into a bestseller.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2823")

    label("loc_26F0")


    ChrTalk(    #112
        0x13,
        (
            "A while ago, an acquaintance showed\x01",
            "a gun in development to Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x13,
        (
            "And if can you believe it, he actually\x01",
            "liked it for once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x13,
        (
            "Apparently we'll be carrying it once\x01",
            "they've got enough testing done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x13,
        (
            "Given that Stain even complemented it,\x01",
            "I'm sure it'll be a great gun once it's\x01",
            "finished.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2823")

    Jump("loc_2BE1")

    label("loc_2826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_29C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28A8")

    ChrTalk(    #116
        0x13,
        "Stain is not what you'd call a tactful guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x13,
        (
            "He reduces a lot of engineers to tears\x01",
            "with his critiques.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C5")

    label("loc_28A8")


    ChrTalk(    #118
        0x13,
        (
            "The owner of this shop's a person\x01",
            "named Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x13,
        (
            "He's kind of a hard-head, but he's\x01",
            "got a real eye for weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x13,
        (
            "Anyway, technologically-speaking, his critique\x01",
            "is precise and detailed, but so sharp that it's\x01",
            "kind of cruel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x13,
        "He's reduced a lot of engineers to tears.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_29C5")

    Jump("loc_2BE1")

    label("loc_29C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2BE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2AC2")

    ChrTalk(    #122
        0x13,
        (
            "That earthquake was a shock,\x01",
            "but I'm not that fussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x13,
        (
            "Earthquakes are just a natural phenomenon\x01",
            "that periodically occur. That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x13,
        (
            "I would hope that the people of this technology\x01",
            "town would respond a bit more calmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BE1")

    label("loc_2AC2")


    ChrTalk(    #125
        0x13,
        (
            "Hey, welcome.\x01",
            "Welcome to Stain Arms & Guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x13,
        (
            "That earthquake was a shock,\x01",
            "but I'm not that fussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x13,
        (
            "Earthquakes are just a natural phenomenon\x01",
            "that periodically occur. That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x13,
        (
            "I would hope that the people of this technology\x01",
            "town would respond a bit more calmly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2BE1")

    TalkEnd(0x13)
    Return()

    # Function_9_205B end

    def Function_10_2BE5(): pass

    label("Function_10_2BE5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353B")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 4360, 0, -720, 0)
    SetChrPos(0x102, 3220, 0, -700, 0)
    SetChrPos(0xF8, 4600, 0, -1800, 0)
    SetChrPos(0xF9, 3230, 0, -1800, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(    #129
        0x8,
        (
            "#790FYou seem to be keeping yourselves occupied.\x02\x03",

            "So, did the pump repair go well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1001F#6PYeah, totally...\x02\x03",

            "#1015FEr, actually, I should probably make a\x01",
            "formal report first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#1040F#6PWell, then, let's share the results.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #132
        "\x07\x05Estelle explained the details of the pump repair at Elmo.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #133
        0x8,
        (
            "#790FSounds more difficult than I'd thought\x01",
            "it would be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F87")

    label("loc_2E11")


    ChrTalk(    #134
        0x8,
        (
            "#790FI received word from the factory chief.\x01",
            "It sounds like you're rather busy.\x02\x03",

            "Did something come up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1011F#6PAh, right. We should make a report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#1035F#6PYeah, so actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #137
        "\x07\x05Estelle explained the details of the pump repair at Elmo.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #138
        0x8,
        (
            "#790FAhh... I see.\x02\x03",

            "Sounds like you've really been taking\x01",
            "bracer work to heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F87")


    ChrTalk(    #139
        0x101,
        (
            "#1015F#6PYeah, I know it's kind of a small thing\x01",
            "to worry about in an emergency like this,\x01",
            "but...\x02\x03",

            "#1002FI can't just abandon people in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308D")

    ChrTalk(    #140
        0x108,
        (
            "#070F#6PMmm, that's the true mentality of a bracer.\x02\x03",

            "I believe it was the right decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3164")

    label("loc_308D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3100")

    ChrTalk(    #141
        0x106,
        (
            "#051FWell, that's the whole reasoning behind\x01",
            "being a bracer.\x02\x03",

            "I think it was the right call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3164")

    label("loc_3100")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3164")

    ChrTalk(    #142
        0x103,
        (
            "#020FYes, that is the mentality of a bracer.\x02\x03",

            "I think it was the right decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3164")


    ChrTalk(    #143
        0x8,
        (
            "#792FThe second principle of the Bracer Guild\x01",
            "Code is prioritizing civilian safety.\x02\x03",

            "Your line of thinking, therefore, was correct.\x02\x03",

            "#791FYou can keep your head high when\x01",
            "you say what you've accomplished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1008F#6PAhaha, thanks.\x02\x03",

            "I feel a bit more confident hearing\x01",
            "that from you, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#1040F#6P... That ends our report.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC2, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_32C7")
    OP_A2(0x10)
    Jump("loc_32CA")

    label("loc_32C7")

    OP_A3(0x10)

    label("loc_32CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3395")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set area quest as unreported (QF_REPORT flag not set)\x01",      # 0
            "Set area quest as reported (QF_REPORT flag set)\x01",            # 1
            "No change\x01",                                                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3389"),
        (1, "loc_338F"),
        (SWITCH_DEFAULT, "loc_3395"),
    )


    label("loc_3389")

    OP_A3(0x10)
    Jump("loc_3395")

    label("loc_338F")

    OP_A2(0x10)
    Jump("loc_3395")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3472")

    ChrTalk(    #146
        0x8,
        (
            "#790FWell, then, I'll have your work assessed\x01",
            "immediately.\x02\x03",

            "When you're ready to be paid, give me your\x01",
            "report again in full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1011F#6PSo just come and report again to get paid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        "#790FYes, please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3532")

    label("loc_3472")


    ChrTalk(    #149
        0x8,
        (
            "#790FIt seems your work's already been assessed,\x01",
            "so that settles things.\x02\x03",

            "Carry on, then, but remain cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1006F#6PGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#1040F#6PYes. Well, then, if you'll pardon us...\x02",
    )

    CloseMessageWindow()

    label("loc_3532")

    OP_A2(0x20C7)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_353B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35AC")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                # 0
            "Report\x01",              # 1
            "About the Sign\x01",      # 2
            "End\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_36E0")

    label("loc_35AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3676")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3629")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                          # 0
            "Report\x01",                        # 1
            "Call Allies\x01",                   # 2
            "Ask to Call the Fortress\x01",      # 3
            "End\x01",                           # 4
        )
    )

    Jump("loc_365B")

    label("loc_3629")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                          # 0
            "Report\x01",                        # 1
            "Ask to Call the Fortress\x01",      # 2
            "End\x01",                           # 3
        )
    )


    label("loc_365B")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_36D9")

    label("loc_3676")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D5")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",             # 0
            "Report\x01",           # 1
            "Call Allies\x01",      # 2
            "End\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_36D9")

    label("loc_36D5")

    Call(6, 5)

    label("loc_36D9")

    Jump("loc_36E0")

    label("loc_36DC")

    Call(6, 5)

    label("loc_36E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3987")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37CE")

    ChrTalk(    #152
        0x8,
        (
            "#790FGood work.\x02\x03",

            "I've got the pay for all your investigations\x01",
            "to date ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_AF(0x9A, 0x85)
    Sleep(100)
    OP_28(0x86, 0x4, 0x20)
    OP_28(0x87, 0x4, 0x20)

    ChrTalk(    #153
        0x8,
        (
            "#790FBe sure to get everything ready\x01",
            "before you head to Elmo.\x02\x03",

            "Well, then, do be careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_37CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386C")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x9A)

    ChrTalk(    #154
        0x8,
        (
            "#790FGood work. It seems you've successfully\x01",
            "accomplished your goals.\x02\x03",

            "If you complete any missions,\x01",
            "come report them to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_386C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x9A)"), scpexpr(EXPR_END)), "loc_38F8")

    ChrTalk(    #155
        0x8,
        (
            "#790FGood work. It seems you've successfully\x01",
            "accomplished your goals.\x02\x03",

            "If you complete any missions,\x01",
            "come report them to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397E")

    label("loc_38F8")


    ChrTalk(    #156
        0x8,
        (
            "#790FOh, it doesn't look as if you have\x01",
            "anything to report at the moment.\x02\x03",

            "If you complete any missions,\x01",
            "come report them to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397E")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_3987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AFC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_39C0")
    Call(1, 12)
    Jump("loc_39D7")

    label("loc_39C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D3")
    Call(1, 9)
    Jump("loc_39D7")

    label("loc_39D3")

    Call(1, 10)

    label("loc_39D7")

    TalkEnd(0x8)
    Jump("loc_3AF8")

    label("loc_39DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AC8")

    ChrTalk(    #157
        0x8,
        (
            "#790FI'll call everyone over, then.\x02\x03",

            "Understood. I'll contact them immediately.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #158
        (
            "\x07\x05All branches were contacted and members on standby\x01",
            "were gathered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    TalkEnd(0x8)
    Jump("loc_3AF8")

    label("loc_3AC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AEF")
    Call(0, 26)
    TalkEnd(0x8)
    Jump("loc_3AF2")

    label("loc_3AEF")

    TalkEnd(0x8)

    label("loc_3AF2")

    Jump("loc_3AF8")

    label("loc_3AF5")

    TalkEnd(0x8)

    label("loc_3AF8")

    Return()

    label("loc_3AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B2E")
    Call(0, 26)
    TalkEnd(0x8)
    Return()

    label("loc_3B2E")

    TalkEnd(0x8)
    Return()

    label("loc_3B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B46")
    TalkEnd(0x8)
    Return()

    label("loc_3B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3BF2")

    ChrTalk(    #159
        0x8,
        (
            "#790FGood work repairing the pump.\x02\x03",

            "Such cases are important for bracers\x01",
            "to take on.\x02\x03",

            "Bracers must always keep in mind that\x01",
            "they are the ally of the people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F84")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_419C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF2")

    ChrTalk(    #160
        0x8,
        "#790FDid you get the Combustion Engine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1006FYeah, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x102,
        (
            "#1040FWe managed to borrow it successfully.\x02\x03",

            "It seems the people aboard\x01",
            "the patrol ship were fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "#790FI see, that's good news.\x02\x03",

            "I'll contact the fortress from my end.\x02\x03",

            "You all should continue with your current work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1040FUnderstood.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D7A")

    ChrTalk(    #165
        0x107,
        "#560FY-Yes! Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DD3")

    label("loc_3D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DAC")

    ChrTalk(    #166
        0x106,
        "#051FWell, let's get going.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DD3")

    label("loc_3DAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DD3")

    ChrTalk(    #167
        0x108,
        "#070FLet us be off.\x02",
    )

    CloseMessageWindow()

    label("loc_3DD3")


    ChrTalk(    #168
        0x8,
        "#790FDo be careful.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3E50")

    label("loc_3DF2")


    ChrTalk(    #169
        0x8,
        (
            "#790FI'll report about the patrol ship.\x02\x03",

            "You all should continue with your current work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E50")

    Jump("loc_4199")

    label("loc_3E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_END)), "loc_3F35")

    ChrTalk(    #170
        0x8,
        (
            "#790FThe Combustion Engine was apparently\x01",
            "loaded onto a patrol ship that made an\x01",
            "emergency landing in the plains.\x02\x03",

            "You'll have to investigate the Tratt Plains and\x01",
            "contact the person in charge there immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4199")

    label("loc_3F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_4199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_END)), "loc_3FBB")

    ChrTalk(    #171
        0x8,
        (
            "#790FAbout the message, apparently\x01",
            "it's not immediately urgent.\x02\x03",

            "Go check in when you next stop\x01",
            "by the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4199")

    label("loc_3FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40DC")

    ChrTalk(    #172
        0x8,
        (
            "#790FWe're near Leiston Fortress, so our concerns\x01",
            "for public safety aren't as significant.\x02\x03",

            "Still, you should probably check the board,\x01",
            "and also go visit the central factory, and\x01",
            "check up on Elmo.\x02\x03",

            "Even if they haven't contacted us,\x01",
            "there could be some kind of problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_4199")

    label("loc_40DC")


    ChrTalk(    #173
        0x8,
        (
            "#790FRegardless, I'd like you to check the board,\x01",
            "and also go visit the central factory, and\x01",
            "check up on Elmo.\x02\x03",

            "Even if they haven't contacted us,\x01",
            "there could be some kind of problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4199")

    Jump("loc_4F84")

    label("loc_419C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4226")

    ChrTalk(    #174
        0x8,
        (
            "#790FThere's still a lot we don't know\x01",
            "about artifacts.\x02\x03",

            "Hopefully this discovery will be some\x01",
            "kind of clue, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4760")

    label("loc_4226")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_42E5")

    ChrTalk(    #175
        0x8,
        (
            "#790FThere's a high possibility that he'll\x01",
            "continue to appear.\x02\x03",

            "Act with care in the capital.\x02\x03",

            "Go with the Goddess' blessing. And be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434E")

    label("loc_42E5")


    ChrTalk(    #176
        0x8,
        (
            "#790FI'll contact Elnan in the capital from my end.\x02\x03",

            "Go with the Goddess' blessing. And be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434E")

    Jump("loc_4760")

    label("loc_4351")


    ChrTalk(    #177
        0x8,
        (
            "#792FThat reminds me, did you notice?\x02\x03",

            "The guild sign's back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x101,
        "#1004FDid someone bring it in or something?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #179
        0x8,
        (
            "#790FFaye from the central factory found it.\x02\x03",

            "Apparently, it was in the underground\x01",
            "warehouse, of all places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1020FTh-The underground warehouse?!\x02\x03",

            "#1007FWhy the heck was it...? Never mind.\x01",
            "There's no point trying to follow that\x01",
            "weirdo's thought process.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_453E")

    ChrTalk(    #181
        0x106,
        (
            "#551FHe carried it in, probably.\x02\x03",

            "Dunno how, but he's clever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458F")

    label("loc_453E")


    ChrTalk(    #182
        0x103,
        (
            "#025FYes, of course he would have put it\x01",
            "somewhere like that.\x02\x03",

            "Very clever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458F")


    ChrTalk(    #183
        0x8,
        (
            "#792FAnyway, I'm canceling that request.\x02\x03",

            "It is a bit regrettable we couldn't\x01",
            "solve it on our own, but...\x02\x03",

            "#790FThere's a high possibility that\x01",
            "he'll continue to appear.\x02\x03",

            "Act with care in the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_468C")

    ChrTalk(    #184
        0x104,
        "#030FHeh, it seems wise.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46C9")

    label("loc_468C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46AE")

    ChrTalk(    #185
        0x107,
        "#062FY-Yes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_46C9")

    label("loc_46AE")


    ChrTalk(    #186
        0x101,
        "#1002FYeah... Got it.\x02",
    )

    CloseMessageWindow()

    label("loc_46C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_46F5")

    ChrTalk(    #187
        0x106,
        "#050FYeah, we'll be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4710")

    label("loc_46F5")


    ChrTalk(    #188
        0x103,
        "#020FYes, understood.\x02",
    )

    CloseMessageWindow()

    label("loc_4710")


    ChrTalk(    #189
        0x8,
        (
            "#790FWell, then, go with the Goddess' blessing. \x02\x03",

            "And be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_28(0x6C, 0x1, 0x4000)

    label("loc_4760")

    Jump("loc_4F84")

    label("loc_4763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_482C")

    ChrTalk(    #190
        0x8,
        (
            "#790FI'll leave the investigation of the guild\x01",
            "sign to you, then.\x02\x03",

            "It's not an urgent matter, though, so you\x01",
            "can carry out your search alongside your\x01",
            "investigations into the earthquake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F84")

    label("loc_482C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_48BC")

    ChrTalk(    #191
        0x8,
        (
            "#790FTo target Leiston Fortress...\x01",
            "Whoever is responsible doesn't have a lot\x01",
            "of common sense.\x02\x03",

            "Be very careful as you go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A42")

    label("loc_48BC")


    ChrTalk(    #192
        0x8,
        "#790FI heard you're heading to Elmo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#1016FWow. You really do know everything, Kilika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "#790FHazel contacted me.\x02\x03",

            "To target Leiston Fortress...\x01",
            "Whoever is responsible doesn't have a lot\x01",
            "of common sense.\x02\x03",

            "...Be very careful as you go.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_49DF")

    ChrTalk(    #195
        0x106,
        "#050FYeah, that's the plan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A00")

    label("loc_49DF")


    ChrTalk(    #196
        0x103,
        "#022FYes, we'll stay alert.\x02",
    )

    CloseMessageWindow()

    label("loc_4A00")


    ChrTalk(    #197
        0x8,
        "#790FThat is all. Now, hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1002FYeah, we're off.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4A42")

    Jump("loc_4F84")

    label("loc_4A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AFB")

    ChrTalk(    #199
        0x8,
        (
            "#790FOnce you're done returning the measuring\x01",
            "equipment, head to the central factory next.\x02\x03",

            "The professor should be on the fifth\x01",
            "floor in the Operations room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F84")

    label("loc_4AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4BDD")

    ChrTalk(    #200
        0x8,
        (
            "#790FThe measuring devices are to be placed in the\x01",
            "middle of the Tunnel, north of the plains,\x01",
            "and in front of Leiston Fortress.\x02\x03",

            "I've already contacted everyone necessary,\x01",
            "so you just need to head to the sites.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F84")

    label("loc_4BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4C81")

    ChrTalk(    #201
        0x8,
        (
            "#790FThe investigation of the earthquakes\x01",
            "isn't urgent.\x02\x03",

            "You can pace yourselves and do some of the\x01",
            "requests on the board while you're at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D81")

    label("loc_4C81")


    ChrTalk(    #202
        0x8,
        (
            "#790FWhat I'd like you to do is carry out some\x01",
            "questioning at the Wolf Fort.\x02\x03",

            "I've asked the Factory Chief to collect\x01",
            "information in Zeiss, so you can skip that.\x02\x03",

            "You can pace yourselves and do some of the\x01",
            "requests on the board while you're at it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4D81")

    Jump("loc_4F84")

    label("loc_4D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4E36")

    ChrTalk(    #203
        0x8,
        (
            "#790FThe investigation of the earthquakes\x01",
            "isn't a job with any great urgency.\x02\x03",

            "Why don't you go to Professor Russell's workshop and\x01",
            "see him and Tita first?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F84")

    label("loc_4E36")


    ChrTalk(    #204
        0x8,
        (
            "#790FWhat I'd like you to do is carry out some\x01",
            "questioning at the Wolf Fort.\x02\x03",

            "I've asked the Factory Chief to collect\x01",
            "information in Zeiss, so you can skip that.\x02\x03",

            "You can pace yourselves and do some of the\x01",
            "requests on the board while you're at it.\x02\x03",

            "Why don't you go to Professor Russell's workshop and\x01",
            "see him and Tita first?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4F84")

    TalkEnd(0x8)
    Return()

    # Function_10_2BE5 end

    def Function_11_4F88(): pass

    label("Function_11_4F88")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_4F95")
    OP_A2(0x5)

    label("loc_4F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5019")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Met Wong in previous game\x01",              # 0
            "Did not meet Won in previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_500D"),
        (1, "loc_5013"),
        (SWITCH_DEFAULT, "loc_5019"),
    )


    label("loc_500D")

    OP_A2(0x5)
    Jump("loc_5019")

    label("loc_5013")

    OP_A3(0x5)
    Jump("loc_5019")

    label("loc_5019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_50A7")

    ChrTalk(    #205
        0xFE,
        "Apparently Gundolf's coming back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "I wonder how long we're gonna be\x01",
            "understaffed like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5155")

    label("loc_50A7")


    ChrTalk(    #207
        0xFE,
        (
            "Apparently Gundolf's coming\x01",
            "back from the capital soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "That'll be a load off my shoulders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Still, I wonder how long we're gonna be\x01",
            "understaffed like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5155")

    Jump("loc_5339")

    label("loc_5158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_529C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_51DD")

    ChrTalk(    #210
        0xFE,
        (
            "After a bit, I'm gonna be out again\x01",
            "escorting a freight vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "Orbment exports are as steady as always.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5299")

    label("loc_51DD")


    ChrTalk(    #212
        0xFE,
        (
            "After a bit, I'm gonna be out again\x01",
            "escorting a freight vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Lately there've been a lot of dangerous\x01",
            "monsters on the roads, so that kinda job\x01",
            "has gotten pretty stressful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5299")

    Jump("loc_5339")

    label("loc_529C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_5339")

    ChrTalk(    #214
        0xFE,
        (
            "I intend to do the best job\x01",
            "I can on my end as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "When you've got an important investigation\x01",
            "to do, you can leave the small stuff to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5339")

    Jump("loc_53C7")

    label("loc_533C")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #216
        0xFE,
        (
            "Sorry for the trouble, but I hope you'll\x01",
            "help out around here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Let's both work together and\x01",
            "do our best, hey?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C7")

    Jump("loc_5AA1")

    label("loc_53CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_55EF")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550D")

    ChrTalk(    #218
        0xFE,
        "Hey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "Do you remember me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1001FOf course!\x02\x03",

            "You're Wong, with the Zeiss branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "Haha, thanks. Glad we got to meet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55EC")

    label("loc_550D")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #224
        0xFE,
        "Oh, hey, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1004FHuh...?\x02\x03",

            "#1018FAh, I was wondering who it was.\x01",
            "Hey, Wong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55EC")

    Jump("loc_5787")

    label("loc_55EF")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #228
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "Aren't you Estelle, that recently promoted senior?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#1004FUh, yeah, that's me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "Ah, 'scuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "I'm Wong. I'm with the Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1000FAh, I see.\x02\x03",

            "I'm Estelle Bright. Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "Yeah, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "I've heard about your work here and there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "After all the successes you've had, it's\x01",
            "only natural you're a full bracer already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5787")


    ChrTalk(    #237
        0x101,
        (
            "#1008FAhaha, thank you.\x02\x03",

            "But, I'm still in training.\x01",
            "I've got a lot to learn still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Never forget the attitude of a\x01",
            "beginner, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Pretty admirable sentiment.\x01",
            "I hope I can follow your example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "Incidentally, did you know Gundolf\x01",
            "is out on a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1011FAh, yeah, I heard from Jean.\x02\x03",

            "We came to Zeiss in part to help\x01",
            "pitch in while he's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "Ah, got'cha. Thanks, that'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Sorry for the trouble, but I hope you'll\x01",
            "help out around here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_59D9")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #244
        0xFE,
        (
            "Agate, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x106,
        "#051FYeah, same here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A38")

    label("loc_59D9")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #246
        0xFE,
        (
            "Scherazard, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x103,
        "#020FYes, same here.\x02",
    )

    CloseMessageWindow()

    label("loc_5A38")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #248
        0xFE,
        "I'll help out as best I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Well, then, let's all work\x01",
            "together and do our best.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0x6)

    label("loc_5AA1")

    TalkEnd(0x16)
    Return()

    # Function_11_4F88 end

    def Function_12_5AA5(): pass

    label("Function_12_5AA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5BCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B60")

    ChrTalk(    #250
        0xFE,
        (
            "I haven't seen the light of a lamp in a while.\x01",
            "It's beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "It's a little bit dim compared\x01",
            "to an orbment light, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "It has such warmth to it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_5BC8")

    label("loc_5B60")


    ChrTalk(    #253
        0xFE,
        (
            "I haven't seen the light of a lamp in a while.\x01",
            "It's beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "It exudes such a warm feeling.\x02",
    )

    CloseMessageWindow()

    label("loc_5BC8")

    Jump("loc_5D05")

    label("loc_5BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9E")

    ChrTalk(    #255
        0xFE,
        "I'm out buying lamp parts again today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "This kind of shopping is a lot more\x01",
            "straightforward for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "There's none of that vague 'buy whatever\x01",
            "looks delicious' nonsense.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_5D05")

    label("loc_5C9E")


    ChrTalk(    #258
        0xFE,
        "I'm out buying lamp parts again today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "Buying specific goods like this is\x01",
            "soooo much easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D05")

    TalkEnd(0xFE)
    Return()

    # Function_12_5AA5 end

    def Function_13_5D09(): pass

    label("Function_13_5D09")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D25")
    Call(0, 27)
    Call(0, 28)

    label("loc_5D25")

    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D3D")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_5D41")

    label("loc_5D3D")

    AddParty(0x3, 0xFA, 0xFF)

    label("loc_5D41")

    OP_6D(2340, 0, -5820, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 3120, 0, -700, 0)
    SetChrPos(0x101, 4170, 0, -700, 315)
    SetChrPos(0x104, 2450, 0, -1620, 0)
    SetChrPos(0xF7, 3600, 0, -1920, 0)
    SetChrPos(0x105, 4720, 0, -1960, 0)
    SetChrPos(0x107, 4190, 0, -3140, 0)
    SetChrPos(0x9, 3140, 0, -2970, 0)
    SetChrPos(0x10, 2029, 0, -2710, 0)
    FadeToBright(1000, 0)

    def lambda_5E24():
        OP_6D(2660, 0, -300, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E24)

    def lambda_5E3C():
        OP_67(0, 8000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E3C)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #260
        0x8,
        (
            "#792FI see...\x02\x03",

            "So the man in sunglasses\x01",
            "was Walter, as I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x11,
        (
            "#073F#6PYea--wait. What?\x02\x03",

            "As you...you suspected from the beginning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x8,
        (
            "#791FWhen I heard his physical description\x01",
            "and clothing, I thought it might be\x01",
            "possible.\x02\x03",

            "#792FMore to the point--you were careless.\x02\x03",

            "How could you allow him to\x01",
            "escape with a Gospel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        (
            "#075F#6POh, come on.\x01",
            "I didn't think it was that important!\x02\x03",

            "#072FDid you forget that you're the one who\x01",
            "shoved me off toward Elmo without so\x01",
            "much as half an explanation?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        (
            "#791FThat was a mistake on my part, yes.\x02\x03",

            "I thought, however, that you wouldn't\x01",
            "need me to spell out every single\x01",
            "detail for you, Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x11,
        (
            "#075F#6PErgh... You're far less cute\x01",
            "when you do that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x8,
        (
            "#792FRegardless. Estelle Bright, your\x01",
            "investigation into the earthquakes\x01",
            "is complete.\x02\x03",

            "#790FAllow me to give you your compensation\x01",
            "for this mission.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61EF")
    OP_AF(0x9A, 0x85)
    Sleep(100)
    OP_28(0x86, 0x4, 0x10)
    OP_28(0x86, 0x4, 0x20)
    OP_28(0x87, 0x4, 0x10)
    OP_28(0x87, 0x4, 0x20)

    label("loc_61EF")

    OP_28(0x88, 0x4, 0x10)
    OP_AF(0x9A, 0x88)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #267
        0x101,
        (
            "#1006F#5PThanks, Kilika.\x02\x03",

            "#1015FBut, uh, it sounds like you two know that\x01",
            "nut in the glasses. What's up with him?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #268
        0x11,
        "#074F#6PWe do. How do I even begin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x8,
        (
            "#791FQuite simply, Zin, Walter and I...\x02\x03",

            "We were fellow students.\x02\x03",

            "Walter was the elder student.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6362")

    ChrTalk(    #270
        0x106,
        (
            "#052F#5PElder student...\x01",
            "You mean your elder in martial arts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63B2")

    label("loc_6362")


    ChrTalk(    #271
        0x103,
        (
            "#023F#5PElder student... You mean he was\x01",
            "your elder in martial arts, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B2")

    OP_8C(0x11, 135, 400)

    ChrTalk(    #272
        0x11,
        (
            "#070F#6PWell, to be precise, Kilika wasn't a\x01",
            "student. Or just a student, anyway.\x02\x03",

            "She was Master Ryuga's--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#792FMy part does not matter.\x02\x03",

            "#790FWalter is a student of the Taito style.\x02\x03",

            "And six years ago, he left the dojo...\x01",
            "and it seems he was recruited by\x01",
            "Ouroboros soon after.\x02\x03",

            "#792FThat should explain everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x11,
        "#572F#6PKilika...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_65DE")

    ChrTalk(    #275
        0x106,
        (
            "#053F#5PNah, don't worry. I think that\x01",
            "IS all we need to hear.\x02\x03",

            "#552FSo he uses the same Taito\x01",
            "style you guys use, huh?\x02\x03",

            "That explains why he hits like\x01",
            "a frickin' airship, at any rate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6689")

    label("loc_65DE")


    ChrTalk(    #276
        0x103,
        (
            "#026F#5PNo, that's...all we need to\x01",
            "hear, she's right.\x02\x03",

            "#020FSo he uses the same Taito style\x01",
            "as the two of you, hmm?\x02\x03",

            "That explains his monstrous strength,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6689")


    ChrTalk(    #277
        0x11,
        (
            "#074F#6PHe's even stronger now than\x01",
            "he was in the dojo.\x02\x03",

            "#072FIt's safe to say he's a true master\x01",
            "of the style, now, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x8,
        (
            "#792FWhat is properly safe to say is\x01",
            "that he is incredibly dangerous.\x02\x03",

            "#791FIt seems likely we won't be dealing with\x01",
            "any more earthquakes, however.\x02\x03",

            "It is probably safe to relax our guard...\x01",
            "a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x10,
        (
            "#801F#1PSeems like it! I'll let the citizens\x01",
            "and workers know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x9,
        (
            "#104F#5PThey used yet another 'Gospel,' though.\x02\x03",

            "And they were using it in conjunction\x01",
            "with some kind of machine which\x01",
            "could stimulate septium veins.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68BC():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_68BC)

    def lambda_68D4():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68D4)

    def lambda_68E2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68E2)
    Sleep(50)

    def lambda_68F5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_68F5)

    def lambda_6903():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6903)
    Sleep(50)

    def lambda_6916():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6916)

    def lambda_6924():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6924)
    Sleep(50)

    def lambda_6937():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6937)
    Sleep(300)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B93")

    ChrTalk(    #281
        0x104,
        (
            "#030F#6PWell, when we consider what was done\x01",
            "with the 'hologram projector' beneath\x01",
            "the Jenis Royal Academy...\x02\x03",

            "It seems safe, to me, to assume the Gospel\x01",
            "massively increases the capabilities of\x01",
            "other orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x9,
        (
            "#102F#5PYes, I believe you are correct.\x02\x03",

            "Holographic projection and excitement\x01",
            "of septium veins are both possible, in\x01",
            "theory.\x02\x03",

            "What they do with these Gospels, however,\x01",
            "is completely beyond our understanding of\x01",
            "orbal technology.\x02\x03",

            "And I don't mean just my understanding...\x01",
            "I can't imagine anyone I know at any\x01",
            "famous factory managing any better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DE6")

    label("loc_6B93")


    ChrTalk(    #283
        0x105,
        (
            "#042F#2PAlso remember what Bleublanc did with that...\x01",
            "hologram projector beneath the academy...\x02\x03",

            "Whatever the Gospel may be, it is definitely\x01",
            "capable of forcing other orbal devices into feats\x01",
            "which greatly exceed their original designs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x9,
        (
            "#102F#5PI believe you are correct, milady.\x02\x03",

            "Holographic projection and excitement of\x01",
            "septium veins are both possible, in theory.\x02\x03",

            "What they do with these Gospels, however,\x01",
            "is completely beyond our understanding of\x01",
            "orbal technology.\x02\x03",

            "And I don't mean just my understanding...\x01",
            "I can't imagine anyone I know at any\x01",
            "famous factory managing any better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE6")


    ChrTalk(    #285
        0x10,
        (
            "#803F#6PIt's true...\x02\x03",

            "I doubt either the Verne Company in\x01",
            "Calvard, or the Reinford Company in\x01",
            "the Empire, could do such things.\x02\x03",

            "#800FEven the Epstein Foundation, for all\x01",
            "its progress in tactical orbments,\x01",
            "couldn't manage such feats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        (
            "#1002F#4PIn other words, the society's got crazy\x01",
            "super-technology nobody else does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x9,
        (
            "#100F#5PIndeed. They must have someone of tremendous\x01",
            "genius and skill working for them.\x02\x03",

            "#101FHeh heh... Well, I'll just have\x01",
            "to show them what-for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x107,
        "#065F#2PGrandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x10,
        (
            "#803F#6PI suppose we have no choice now.\x02\x03",

            "#800FWe've finished the Arseille's new orbal\x01",
            "engine, too, so we have free capacity.\x02\x03",

            "We'll devote the central factory's full\x01",
            "resources to analyzing the Gospel\x01",
            "sample we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x9,
        "#101F#5PHah! Of course we will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1006F#4PIf you can figure out what the\x01",
            "Gospels are, it'll be a big help.\x02\x03",

            "I mean, who knows what else they're\x01",
            "going to use them for after this?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_720C")

    ChrTalk(    #292
        0x106,
        (
            "#053F#6PBoth those clowns kept babbling\x01",
            "on about 'experiments,' too.\x02\x03",

            "#050FThey aren't gonna stop at two.\x01",
            "There'll be a third time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7294")

    label("loc_720C")


    ChrTalk(    #293
        0x103,
        (
            "#026F#6PTheir agents keep talking about\x01",
            "'experiments,' as well.\x02\x03",

            "#022FSomehow, I find it hard to believe\x01",
            "they'll only stop at two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7294")


    ChrTalk(    #294
        0x8,
        (
            "#792FIf Professor Russell will be taking care\x01",
            "of the analysis of the Gospel...\x02\x03",

            "#790FI believe it would be best if your\x01",
            "group moved on, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7330():
        OP_6D(2660, 0, -300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7330)

    def lambda_7348():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7348)

    def lambda_7356():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7356)
    Sleep(50)

    def lambda_7369():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7369)

    def lambda_7377():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7377)
    Sleep(50)

    def lambda_738A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_738A)

    def lambda_7398():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7398)
    Sleep(50)

    def lambda_73AB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_73AB)
    Sleep(500)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #295
        0x101,
        (
            "#1006F#5PYeah, I agree.\x02\x03",

            "We didn't catch the bad guy, but there\x01",
            "won't be any more earthquakes, at least.\x02\x03",

            "Any suggestion on where to go next,\x01",
            "Kilika?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x8,
        (
            "#791FThe central branch of the guild, in\x01",
            "Grancel, sent us a request for aid.\x02\x03",

            "They claim to have received an official mission\x01",
            "directly from the leadership of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        "#1004F#5PThe Royal Army? You mean from Dad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x8,
        (
            "#791FThey did not share any details.\x02\x03",

            "They did, however, request all of you by name.\x01",
            "There is a good chance this involves Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1015F#5PProbably, yeah.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7637")

    ChrTalk(    #300
        0x106,
        (
            "#051F#5PHeh. Well, if they're invitin' us,\x01",
            "we can't say no, can we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7696")

    label("loc_7637")


    ChrTalk(    #301
        0x103,
        (
            "#027F#5PHeehee. Well, we can hardly turn down\x01",
            "an invitation from the capital, now can we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7696")

    OP_8C(0x11, 135, 400)

    ChrTalk(    #302
        0x11,
        (
            "#071F#6PThen it's decided!\x02\x03",

            "Once we finish our last bits of business in Zeiss,\x01",
            "let us board the next flight to the capital!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #303
        0x101,
        (
            "#1001FSounds like a p-...Wait. 'We'?\x02\x03",

            "#1004FZin, are you coming with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x11,
        (
            "#070F#6PHey, now. Why do you think I came\x01",
            "all the way back here?\x02\x03",

            "Not only is Walter on the prowl, but you\x01",
            "are still searching for Joshua, yes?\x02\x03",

            "You can bet I'll help you,\x01",
            "in any way I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        "#1017FAww... Thanks, Zin.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_79DD")

    ChrTalk(    #306
        0x106,
        (
            "#053F#5PTo be honest, I'll be glad\x01",
            "to have you with us.\x02\x03",

            "#050FYour wolf friend nearly beat\x01",
            "us into raw meat.\x02\x03",

            "If you'd be willing, I'd like to\x01",
            "train with you to fight him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x11,
        (
            "#071F#6PHaha! That's a bit humble for you, Agate!\x02\x03",

            "#070FYou usually possess more confidence\x01",
            "in your own abilities. But very well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x106,
        (
            "#552F#5PHey, I ain't so thick that I don't\x01",
            "see how good you are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B34")

    label("loc_79DD")


    ChrTalk(    #309
        0x103,
        (
            "#021F#5PHaving you with us will be\x01",
            "like having a hundred men on our side.\x02\x03",

            "#027FThat fiend with the sunglasses\x01",
            "did nearly break us like twigs.\x02\x03",

            "If you can help us train to resist\x01",
            "him, it would be a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x11,
        (
            "#070F#6POf course!\x02\x03",

            "His moves are pretty special, but I can\x01",
            "teach you all some counters, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x103,
        "#021F#5PThank you!\x02",
    )

    CloseMessageWindow()

    label("loc_7B34")

    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7D7D")

    ChrTalk(    #312
        0x107,
        (
            "#062F#5PUm... Estelle? Agate?\x02\x03",

            "Can I...come too?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7BC4():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7BC4)

    def lambda_7BDC():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BDC)

    def lambda_7BEA():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BEA)
    Sleep(50)

    def lambda_7BFD():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7BFD)

    def lambda_7C0B():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C0B)
    Sleep(50)

    def lambda_7C1E():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7C1E)

    def lambda_7C2C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7C2C)
    Sleep(50)

    def lambda_7C3F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7C3F)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #313
        0x101,
        "#1004F#4PHUH?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x106,
        "#055F#6PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x107,
        (
            "#561F#5PWell, um, the society might use more\x01",
            "weird devices, or more Gospels...\x02\x03",

            "I, um, I think I might be\x01",
            "able to help if they do...\x02\x03",

            "#062FPlease! Take me with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        "#1003F#4PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x106,
        "#053F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 400)
    Sleep(300)

    ChrTalk(    #318
        0x106,
        "#050F#4PGramps. What do you think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FD3")

    label("loc_7D7D")


    ChrTalk(    #319
        0x107,
        (
            "#062F#5PUm... Estelle? Schera?\x02\x03",

            "Can I...come too?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7DED():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DED)

    def lambda_7E05():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E05)

    def lambda_7E13():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E13)
    Sleep(50)

    def lambda_7E26():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E26)

    def lambda_7E34():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E34)
    Sleep(50)

    def lambda_7E47():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7E47)

    def lambda_7E55():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7E55)
    Sleep(50)

    def lambda_7E68():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7E68)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #320
        0x101,
        "#1004F#4PHUH?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x103,
        "#023F#6PHmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x107,
        (
            "#561F#5PWell, um, the society might use more\x01",
            "weird devices, or more Gospels...\x02\x03",

            "I, um, I think I might be\x01",
            "able to help if they do...\x02\x03",

            "#062FPlease! Take me with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1003F#4PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x103,
        "#026F#6PWell, this is a bit of a pickle...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(300)

    ChrTalk(    #325
        0x103,
        (
            "#020F#4PI'd say it's up to Professor Russell.\x01",
            "Sir?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FD3")


    ChrTalk(    #326
        0x9,
        (
            "#104F#5PWell. I have to say that the\x01",
            "grandfather in me is filled with\x01",
            "terror at the mere idea.\x02\x03",

            "#100FBut as you can see, my little Tita is\x01",
            "quite stubborn, and I want to make\x01",
            "her dreams possible whenever I can.\x02\x03",

            "Go ahead, Tita. I won't stop you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #327
        0x107,
        "#560F#2PGrandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x9,
        (
            "#100F#5PThe Ouroboros clearly have a greater\x01",
            "technological edge than we could have\x01",
            "ever imagined.\x02\x03",

            "In that sense, Tita is absolutely correct.\x01",
            "She could be a great help to you.\x02\x03",

            "#101FI'd say you're getting quite a deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x10,
        (
            "#805F#6PYou're not selling a new product,\x01",
            "here, Professor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1007F#4PWell, uh, I'll admit having Tita\x01",
            "along really would help, but...\x02\x03",

            "#1003FBut if someone like that\x01",
            "man attacks us again, I...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_884F")

    ChrTalk(    #331
        0x106,
        (
            "#552F#4P...\x02\x03",

            "#053FNo... It's okay.\x02\x03",

            "We'll keep your granddaughter safe.\x01",
            "No matter what.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 315, 400)

    ChrTalk(    #332
        0x107,
        "#064F#5PA-Agate...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x9,
        "#103F#5POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#1004F#4PWhat th--\x01",
            "What's gotten into you?!\x02\x03",

            "I figured you'd be the one who'd\x01",
            "yell loudest about this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x106,
        (
            "#053F#6PBetween that clown and what we learned from that\x01",
            "psycho, I think it's safe to say the society gives\x01",
            "not one damn about the safety of civilians.\x02\x03",

            "That means there's no guarantee that Zeiss\x01",
            "is any more safe than...anywhere, really.\x02\x03",

            "#051FSo given that... What the hell, eh?\x01",
            "Might as well keep her where\x01",
            "we can keep an eye on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x107,
        "#560F#5PA-Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x9,
        (
            "#100F#5PYes... Distressing as it may be,\x01",
            "that's true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x104,
        (
            "#035F#6PHeheh. More to the point, you simply\x01",
            "want her to be some place where\x01",
            "you can easily protect her.\x02\x03",

            "#037FOur rough Raven wishes to be a white\x01",
            "knight! How chivalrous! How manly!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x106, 270, 600)

    ChrTalk(    #339
        0x106,
        "#055F#4PWh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#1006F#4POoooh, given THAT look, I think\x01",
            "Olivier's right on the mark!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x107,
        "#560F#5PUm, um! Is that true...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 135, 400)

    ChrTalk(    #342
        0x106,
        (
            "#551F#4PDon't listen to anything that idiot says.\x02\x03",

            "#555FLook, you better be able to\x01",
            "pull your own weight, got it?\x02\x03",

            "Don't get so lost in messin' with\x01",
            "machines you do somethin' stupid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x107,
        "#067F#5PHehehe... I'll be careful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x11,
        "#071F#6PHaha! Well, good to see that's settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x105,
        (
            "#048FHaha... It's good to see our\x01",
            "group getting so lively.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BAE")

    label("loc_884F")

    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #346
        0x105,
        (
            "#043F#2PUm, well, it occurs to me...\x02\x03",

            "Especially given what that...madman...\x01",
            "said, I don't believe the society cares\x01",
            "at all for the safety of civilians.\x02\x03",

            "I...don't think we can really say\x01",
            "she'll be all that safer here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        "#1004F#4POh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #348
        0x103,
        (
            "#027F#6PIn other words, she might actually be\x01",
            "SAFER traveling with us, hmm?\x02\x03",

            "Or at least, it's no more dangerous\x01",
            "than staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x105,
        "#542F#2PI think so, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x107,
        "#064F#5PKloe, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        (
            "#1007F#4PAaaagh, okay, okay, I get it.\x02\x03",

            "#1005FCome on, it's not like I wanted\x01",
            "to say goodbye to Tita either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x107,
        "#560F#5PEstelle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1013F#4PEr, that is, well...\x02\x03",

            "#1016FA-Anyway! We'll be counting on you, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x107,
        "#067F#5POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x11,
        "#071F#6PHaha! Well, good to see that's settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x104,
        (
            "#031F#6PAhh, our little group grows\x01",
            "livelier all the time!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B8E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8B8E)
    Sleep(50)

    def lambda_8BA1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8BA1)
    Sleep(50)

    label("loc_8BAE")

    OP_8C(0x107, 270, 400)
    OP_8C(0x9, 90, 400)

    ChrTalk(    #357
        0x9,
        (
            "#100F#5PTita, do take care.\x02\x03",

            "#101FI'll take care of unraveling the mystery of\x01",
            "this 'Gospel' business while you're gone,\x01",
            "don't worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x107,
        "#061F#2POkay! Good luck, Grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x10,
        (
            "#801F#6PDon't worry too much about\x01",
            "Professor Russell, everyone.\x02\x03",

            "I'll keep both eyes on him and make sure\x01",
            "he doesn't cause any catastrophes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x107,
        (
            "#067F#2PI'm counting on you,\x01",
            "Mr. Murdock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x9,
        (
            "#104F#5POh, don't you have a church or\x01",
            "something to run off to, Murdock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x8,
        "#792FHeehee...\x02",
    )

    CloseMessageWindow()

    def lambda_8D96():
        OP_6D(2660, 0, -300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D96)

    def lambda_8DAE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8DAE)

    def lambda_8DBC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DBC)
    Sleep(50)

    def lambda_8DCF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DCF)

    def lambda_8DDD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DDD)
    Sleep(50)

    def lambda_8DF0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8DF0)

    def lambda_8DFE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8DFE)
    Sleep(50)

    def lambda_8E11():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E11)

    def lambda_8E1F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8E1F)
    Sleep(200)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #363
        0x8,
        (
            "#791FI will contact Elnan at the Grancel\x01",
            "guildhouse.\x02\x03",

            "May the blessings of She Who Dwells Above\x01",
            "be with you. Take care on your journey.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x3F5, 1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE1")
    RemoveParty(0x4, 0xFF)
    Jump("loc_8EE4")

    label("loc_8EE1")

    RemoveParty(0x3, 0xFF)

    label("loc_8EE4")

    Sleep(1000)
    OP_AD(0x2400AF, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1484)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x124), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0xF, 0x0, 0x0, 0x0)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F64")
    ShowSaveMenu()

    label("loc_8F64")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    OP_20(0xBB8)
    Sleep(2000)
    OP_21()
    OP_A3(0x1484)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_5D09 end

    def Function_14_8F9D(): pass

    label("Function_14_8F9D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(4430, 0, 3750, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(327000, 0)
    OP_6E(272, 0)
    SetChrPos(0x8, 5380, 0, 2500, 270)
    OP_4A(0x8, 255)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #364
        0x8,
        (
            "#792FI see. I believe I understand\x01",
            "the situation.\x02\x03",

            "#791FThe army's detachment has already\x01",
            "begun its defensive plan here.\x02\x03",

            "They were entirely prepared for this,\x01",
            "so I do not believe guild support will\x01",
            "be necessary.\x02\x03",

            "#790F...\x02\x03",

            "#792FYou're heading for Carnelia\x01",
            "Tower next? Very good.\x02\x03",

            "#791FI wish you the best. Good luck.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #365
        0x8,
        (
            "#792F...As bad at hiding things as ever,\x01",
            "I see.\x02\x03",

            "#791FSix years and you still haven't\x01",
            "changed at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #366
        0x8,
        (
            "#790F#6PWell, then.\x02\x03",

            "It appears I have some\x01",
            "work to do, in that case.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_8F9D end

    def Function_15_92B4(): pass

    label("Function_15_92B4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92CB")
    Call(0, 27)
    Call(0, 29)

    label("loc_92CB")

    SetChrPos(0x101, 770, 0, -6100, 0)
    SetChrPos(0x102, 770, 0, -6100, 0)
    SetChrPos(0xF8, 770, 0, -6100, 0)
    SetChrPos(0xF9, 770, 0, -6100, 0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 3380, 0, 2350, 0)
    OP_6D(2880, 0, 2070, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(310, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93C5")

    ChrTalk(    #367
        0x8,
        "#792F#6PAh. Faster than I expected.\x02",
    )

    CloseMessageWindow()
    Jump("loc_941A")

    label("loc_93C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93FE")

    ChrTalk(    #368
        0x8,
        "#792F#6P*sigh* Later than I expected.\x02",
    )

    CloseMessageWindow()
    Jump("loc_941A")

    label("loc_93FE")


    ChrTalk(    #369
        0x8,
        "#792F#6PRight on time.\x02",
    )

    CloseMessageWindow()

    label("loc_941A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9676")

    ChrTalk(    #370
        0x108,
        "#2POh, come on...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x101, 1770, 0, -6100, 0)
    SetChrPos(0x102, 1770, 0, -6100, 0)
    SetChrPos(0xF8, 1770, 0, -6100, 0)
    SetChrPos(0xF9, 1770, 0, -6100, 0)

    def lambda_948E():
        OP_6D(2800, 0, 750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_948E)

    def lambda_94A6():
        OP_67(0, 6190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_94A6)

    def lambda_94BE():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_94BE)

    def lambda_94CE():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_94CE)
    OP_43(0x101, 0x1, 0x0, 0x10)
    OP_8C(0x8, 180, 400)
    OP_43(0x102, 0x1, 0x0, 0x11)

    def lambda_94F3():
        OP_8E(0xFE, 0xDAC, 0x0, 0x4B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_94F3)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #371
        0x108,
        (
            "#075F#6PHow could you know that\x01",
            "we'd be coming by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x8,
        (
            "#791FThat floating city is the source\x01",
            "of our current troubles, no?\x02\x03",

            "If you cannot reach it directly, the most\x01",
            "logical course of action is to ensure the\x01",
            "various guild branches are all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x108,
        "#072F#6PMmmmmrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x101,
        (
            "#1016F#6PHaha, come on, Zin,\x01",
            "she's got us there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D4")

    label("loc_9676")


    ChrTalk(    #375
        0x101,
        "#2POh, come on, Kilika...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x101, 1590, 0, -8119, 0)
    SetChrPos(0x102, 1590, 0, -8119, 0)
    SetChrPos(0xF8, 1590, 0, -8119, 0)
    SetChrPos(0xF9, 1590, 0, -8119, 0)

    def lambda_96E4():
        OP_6D(2800, 0, 750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96E4)

    def lambda_96FC():
        OP_67(0, 6190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_96FC)

    def lambda_9714():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9714)

    def lambda_9724():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9724)
    OP_43(0x101, 0x1, 0x0, 0x10)
    OP_8C(0x8, 180, 400)
    OP_43(0x102, 0x1, 0x0, 0x11)

    def lambda_9749():
        OP_8E(0xFE, 0xDAC, 0x0, 0x4B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9749)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #376
        0x101,
        (
            "#1008F#6PWere you seriously guessing that\x01",
            "we'd be coming by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x8,
        (
            "#791FThat floating city is the source\x01",
            "of our current troubles, no?\x02\x03",

            "If you cannot reach it directly, the most\x01",
            "logical course of action is to ensure the\x01",
            "various guild branches are all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x101,
        "#1016F#6PI, uh... Yeah, that's logical.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x102,
        "#1040FShe does have a point.\x02",
    )

    CloseMessageWindow()

    label("loc_98D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9908")

    ChrTalk(    #380
        0x107,
        "#067FHeehee... That's Kilika!\x02",
    )

    CloseMessageWindow()
    Jump("loc_998B")

    label("loc_9908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_993F")

    ChrTalk(    #381
        0x106,
        "#051FHeh... Never misses a beat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_998B")

    label("loc_993F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_998B")

    ChrTalk(    #382
        0x103,
        (
            "#021FHeh! Still two steps ahead\x01",
            "of everyone else, I see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998B")


    ChrTalk(    #383
        0x8,
        (
            "#792FSmall talk aside, you can imagine\x01",
            "how things have been here.\x02\x03",

            "#790FZeiss is practically built on a culture\x01",
            "of orbment worship at this point. Losing\x01",
            "them is a shock, to say the least.\x02\x03",

            "Chief Murdock has been trying his best, but\x01",
            "the citizens remain as panicked as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#1015F#6PI was afraid of that.\x01",
            "I hope he's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B3B")

    ChrTalk(    #385
        0x107,
        (
            "#063FIt'd be nice if we could help Mr. Murdock\x01",
            "out, but I dunno if we can...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B88")

    label("loc_9B3B")


    ChrTalk(    #386
        0x102,
        (
            "#1043FI'd like to help him, but I'm a little\x01",
            "unsure what we could do...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B88")


    ChrTalk(    #387
        0x8,
        (
            "#792FI'm sure he'd appreciate the company\x01",
            "for a moment, if nothing else.\x02\x03",

            "#790FThe other major problem facing\x01",
            "the city is the Kaldia Tunnel.\x02\x03",

            "With orbal lighting non-functional, passage\x01",
            "through it has become much harder.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D86")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as crossed Kaldia Tunnel to reach Zeiss\x01",      # 0
            "Set as entered tunnel from Air-Letten side\x01",       # 1
            "Set as entered tunnel from Zeiss side\x01",            # 2
            "Set as not entered tunnel\x01",                        # 3
            "No change\x01",                                        # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9D62"),
        (1, "loc_9D6B"),
        (2, "loc_9D74"),
        (3, "loc_9D7D"),
        (SWITCH_DEFAULT, "loc_9D86"),
    )


    label("loc_9D62")

    OP_A2(0x2081)
    OP_A2(0x2082)
    Jump("loc_9D86")

    label("loc_9D6B")

    OP_A2(0x2081)
    OP_A3(0x2082)
    Jump("loc_9D86")

    label("loc_9D74")

    OP_A3(0x2081)
    OP_A2(0x2082)
    Jump("loc_9D86")

    label("loc_9D7D")

    OP_A3(0x2081)
    OP_A3(0x2082)
    Jump("loc_9D86")

    label("loc_9D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E30")

    ChrTalk(    #388
        0x101,
        (
            "#1007F#6PNo kidding.\x02\x03",

            "We came through them on\x01",
            "the way here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x102,
        (
            "#1042FYou can barely see in front of yourself,\x01",
            "as things stand. It IS very dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F71")

    label("loc_9E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ECE")

    ChrTalk(    #390
        0x101,
        "#1007F#6PYeah, we poked our noses down there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x102,
        (
            "#1042FYou can barely see in front of yourself,\x01",
            "as things stand. It IS very dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F71")

    label("loc_9ECE")


    ChrTalk(    #392
        0x101,
        (
            "#1007F#6POh. Yeah. You kinda need lights\x01",
            "down there, don't you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x102,
        (
            "#1042FIf the lights aren't working, I can only imagine\x01",
            "how dangerous it is down there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F71")


    ChrTalk(    #394
        0x8,
        (
            "#792FThere's more.\x02\x03",

            "#790FThe water pump at Elmo is currently non-functional\x01",
            "and their hot springs are closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#1015F#6PAw, nuts.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A036")

    ChrTalk(    #396
        0x107,
        "#561FMrs. Mao must be really sad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A064")

    label("loc_A036")


    ChrTalk(    #397
        0x102,
        "#1043FMrs. Mao must be taking that hard.\x02",
    )

    CloseMessageWindow()

    label("loc_A064")


    ChrTalk(    #398
        0x8,
        (
            "#792F...That should be everything.\x02\x03",

            "#790FNow, it's my turn for questions,\x01",
            "if you don't mind.\x02\x03",

            "What happened after I left\x01",
            "the Carnelia Tower?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A123")

    ChrTalk(    #399
        0x108,
        "#072F#6PQuite a lot...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A142")

    label("loc_A123")


    ChrTalk(    #400
        0x101,
        "#1002F#6PA heck of a lot.\x02",
    )

    CloseMessageWindow()

    label("loc_A142")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #401
        (
            "\x07\x05Estelle and company explained how the floating\x01",
            "city appeared, and about the Zero Field Generator.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #402
        0x8,
        (
            "#792FI see. So it IS the Aureole.\x02\x03",

            "#790FIt seems this was guaranteed to happen\x01",
            "the moment they took the towers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A273")

    ChrTalk(    #403
        0x108,
        "#074F#6PYes... I think it was.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A291")

    label("loc_A273")


    ChrTalk(    #404
        0x102,
        "#1035FYes...most likely.\x02",
    )

    CloseMessageWindow()

    label("loc_A291")


    ChrTalk(    #405
        0x101,
        (
            "#1003F#6PWhen you think about it, heading to the\x01",
            "towers was probably a waste of time...\x02\x03",

            "#1007FIt's kinda depressing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x8,
        (
            "#792FWe have little time for regrets now.\x02\x03",

            "#791FIf nothing else, it sounds as though you\x01",
            "obtained a far greater understanding of\x01",
            "their plans in your visits to the towers.\x02\x03",

            "What we must focus on now is putting\x01",
            "what we know to use for the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#1025F#6PKilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x8,
        (
            "#791FWould you mind fixing my phone, by the way?\x02\x03",

            "Guiding you to a better future will be\x01",
            "hard if I can't get in touch, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A51C")

    ChrTalk(    #409
        0x108,
        (
            "#075F#6POy...\x02\x03",

            "#072FCome on, you had a nice feeling going.\x01",
            "Don't chain things together like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A51C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6A2")

    ChrTalk(    #410
        0x101,
        "#1016F#6PHahaha... Okay, okay.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #411
        0x101,
        "#1006F#4PWell, then, Tita, you have the honors!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #412
        0x107,
        "#061FOkay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 27)
    SetChrPos(0x107, 5350, 0, 2490, 270)
    OP_8C(0x8, 90, 0)
    OP_8C(0x101, 0, 0)
    OP_6D(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #413
        0x107,
        (
            "#560FAll done!\x01",
            "It should be fine now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #414
        "\x07\x05Tita flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_A7E2")

    label("loc_A6A2")


    ChrTalk(    #415
        0x101,
        "#1016F#6PHahaha... Okay, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x102,
        "#1040FJust give me just a moment here...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 27)
    SetChrPos(0x102, 5350, 0, 2490, 270)
    OP_8C(0x8, 90, 0)
    OP_6D(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #417
        0x102,
        "#1035FThat should do it...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #418
        "\x07\x05Joshua flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_A7E2")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #419
        0x8,
        (
            "#791F#6PAs I would expect of Professor Russell.\x01",
            "He's done well again.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)

    def lambda_A8A7():
        OP_6D(2850, 0, 1670, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A8A7)

    def lambda_A8BF():
        OP_67(0, 6270, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8BF)

    def lambda_A8D7():
        OP_6E(325, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8D7)

    def lambda_A8E7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A8E7)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A90C")
    OP_8C(0x107, 180, 400)
    Jump("loc_A913")

    label("loc_A90C")

    OP_8C(0x102, 180, 400)

    label("loc_A913")

    WaitChrThread(0x101, 0x0)

    ChrTalk(    #420
        0x8,
        (
            "#791F#4PThank you, everyone.\x01",
            "This will help tremendously.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as fixed all phones\x01",           # 0
            "Set as only fixed this phone\x01",      # 1
            "No change\x01",                         # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A9E5"),
        (1, "loc_A9EE"),
        (SWITCH_DEFAULT, "loc_A9F7"),
    )


    label("loc_A9E5")

    OP_A2(0x2001)
    OP_A2(0x2003)
    Jump("loc_A9F7")

    label("loc_A9EE")

    OP_A3(0x2001)
    OP_A3(0x2003)
    Jump("loc_A9F7")

    label("loc_A9F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5C")

    ChrTalk(    #421
        0x101,
        "#1016F#5PAww, nothing to it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x108,
        (
            "#071FHaha! That's an awfully honest\x01",
            "show of gratitude, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x8,
        (
            "#792F#4PWhat a thing to say, Zin.\x02\x03",

            "#791FI think I'm one of the most honest women\x01",
            "in the world. Wouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC7B")

    ChrTalk(    #424
        0x108,
        (
            "#075FI'd say it's less about 'honesty' and more\x01",
            "about not holding anything back...\x02\x03",

            "#070FAnyway. That's all the phone's repaired.\x02\x03",

            "We should return to the professor\x01",
            "and Captain Schwarz and inform\x01",
            "them of our success.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)

    ChrTalk(    #425
        0x8,
        (
            "#791F#4PThank you, everyone.\x02\x03",

            "This will assist a great deal\x01",
            "in keeping up with events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x108,
        "#070FDo you need our help with anything else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD59")

    label("loc_AC7B")


    ChrTalk(    #427
        0x108,
        (
            "#075FI'd say it's less about 'honesty' and more\x01",
            "about not holding anything back...\x02\x03",

            "#070FAnyway. We must depart soon\x01",
            "to assist the other guildhouses.\x02\x03",

            "Before we leave, though, is there\x01",
            "anything else we can help with?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD59")

    Jump("loc_B1BF")

    label("loc_AD5C")


    ChrTalk(    #428
        0x101,
        "#1016F#5PAww, nothing to it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADBE")

    ChrTalk(    #429
        0x102,
        "#1040FI'm glad we could be of assistance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADED")

    label("loc_ADBE")


    ChrTalk(    #430
        0x102,
        "#1040FI'm glad we could be of assistance.\x02",
    )

    CloseMessageWindow()

    label("loc_ADED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B02D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEAC")

    ChrTalk(    #431
        0x103,
        (
            "#020FWell, then!\x01",
            "That's all the phones made functional.\x02\x03",

            "We should let Professor Russell and Captain Schwarz\x01",
            "know about our success and what's been\x01",
            "going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF41")

    label("loc_AEAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF41")

    ChrTalk(    #432
        0x106,
        (
            "#051FAll right, that's all the phones workin' again.\x02\x03",

            "We oughtta get back to Gramps and the\x01",
            "captain and let 'em know what's what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF41")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)

    ChrTalk(    #433
        0x8,
        (
            "#791F#4PThank you, everyone.\x02\x03",

            "This will help a great deal\x01",
            "in keeping up with events.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFF9")

    ChrTalk(    #434
        0x103,
        (
            "#020FDo you need help with\x01",
            "anything else?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B02A")

    label("loc_AFF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B02A")

    ChrTalk(    #435
        0x106,
        "#051FAnything else we can do?\x02",
    )

    CloseMessageWindow()

    label("loc_B02A")

    Jump("loc_B1BF")

    label("loc_B02D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0D4")

    ChrTalk(    #436
        0x103,
        (
            "#020FWell, at this point, it's time to put\x01",
            "our weary feet back on the road to\x01",
            "help the other guildhouses.\x02\x03",

            "Need help with anything before we go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1BF")

    label("loc_B0D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B14D")

    ChrTalk(    #437
        0x106,
        (
            "#051FWell, we gotta get a move on and\x01",
            "get the rest of the guild going, but...\x02\x03",

            "Need anything else?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1BF")

    label("loc_B14D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1BF")

    ChrTalk(    #438
        0x107,
        (
            "#560FUm, we need to go and fix all the other phones.\x02\x03",

            "Do you need us to do stuff before we go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1BF")


    ChrTalk(    #439
        0x8,
        (
            "#791F#4PThis city lies in the shadow of Leiston Fortress,\x01",
            "so keeping order will not be difficult.\x01",
            "Still, if you could, check the board.\x02\x03",

            "And as I intimated earlier, checking on the\x01",
            "central factory and Elmo may be wise.\x02\x03",

            "Their problems seem to be\x01",
            "compounding themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        "#1006F#5PWill do, then!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B324")

    ChrTalk(    #441
        0x102,
        "#1040FWe'll keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B348")

    label("loc_B324")


    ChrTalk(    #442
        0x102,
        "#1040FWe'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    label("loc_B348")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #443
        (
            "\x07\x05With the phone fixed, you can call the team from\x01",
            "another branch to Zeiss. If you wish to call them,\x01",
            "select 'Call Allies' when speaking to Kilika.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2005)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B40E")
    OP_A2(0x2091)
    Jump("loc_B411")

    label("loc_B40E")

    OP_A3(0x2091)

    label("loc_B411")

    OP_28(0x9B, 0x2, 0x10)
    OP_28(0x9B, 0x1, 0x20)
    OP_6D(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2510, 0, -2680, 180)
    SetChrPos(0x1, 2510, 0, -2680, 180)
    SetChrPos(0x2, 2510, 0, -2680, 180)
    SetChrPos(0x3, 2510, 0, -2680, 180)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_92B4 end

    def Function_16_B4B1(): pass

    label("Function_16_B4B1")

    OP_8E(0xFE, 0xF3C, 0x0, 0xFFFFF268, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10EA, 0x0, 0xFFFFFD44, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_B4B1 end

    def Function_17_B4E1(): pass

    label("Function_17_B4E1")

    OP_8E(0xFE, 0xA5A, 0x0, 0xFFFFF38A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0xFFFFFD44, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_B4E1 end

    def Function_18_B511(): pass

    label("Function_18_B511")

    OP_8E(0xFE, 0xF3C, 0x0, 0xFFFFF268, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10EA, 0x0, 0xFFFFF8F8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_B511 end

    def Function_19_B541(): pass

    label("Function_19_B541")

    OP_8E(0xFE, 0xA5A, 0x0, 0xFFFFF38A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0xFFFFF8F8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_B541 end

    def Function_20_B571(): pass

    label("Function_20_B571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B58B")
    Return()

    label("loc_B58B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5AB")
    Call(0, 27)
    Call(0, 29)
    FadeToBright(0, 0)

    label("loc_B5AB")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #444
        0x101,
        "#1004FWhoa!\x02",
    )

    CloseMessageWindow()

    def lambda_B628():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B628)

    def lambda_B636():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B636)
    Sleep(100)

    def lambda_B649():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B649)
    OP_8C(0x3, 0, 400)

    ChrTalk(    #445
        0x8,
        (
            "#791F#3PAnd an immediate call.\x01",
            "Also not unexpected.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(3970, 0, 2180, 0)
    OP_67(0, 6980, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x101, 1770, 0, -6100, 0)
    SetChrPos(0x102, 1770, 0, -6100, 0)
    SetChrPos(0xF8, 1770, 0, -6100, 0)
    SetChrPos(0xF9, 1770, 0, -6100, 0)
    OP_8E(0x8, 0x14E6, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0x14E6, 0x0, 0x9BA, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x101, 0x0, 0x0, 0x15)

    ChrTalk(    #446
        0x8,
        (
            "#792FBracer Guild. Zeiss branch.\x02\x03",

            "#791F...Yes, I thought you'd be calling.\x02\x03",

            "My phone was fixed just moments ago.\x02\x03",

            "...Yes, that's right.\x01",
            "They're right here.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)

    def lambda_B84D():
        OP_6D(3720, 0, 1230, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B84D)

    def lambda_B865():
        OP_67(0, 6580, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B865)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #447
        0x101,
        "#1004F#1P(She's talking about us?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x102,
        (
            "#1044F#6P(It seems so.\x01",
            "I wonder what's going on.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x8,
        (
            "#792FHmm. Yes.\x02\x03",

            "...\x02\x03",

            "#791FUnderstood. I will tell them at once.\x02\x03",

            "I will contact you later to report on\x01",
            "the situation here.\x02\x03",

            "#792FYes. May Aidios be with you as well.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D8")

    ChrTalk(    #450
        0x108,
        "#073F#6PKilika, who was that?\x02",
    )

    Jump("loc_B9F7")

    label("loc_B9D8")


    ChrTalk(    #451
        0x108,
        "#073FKilika, who was that?\x02",
    )


    label("loc_B9F7")

    CloseMessageWindow()
    Jump("loc_BA2A")

    label("loc_B9FB")


    ChrTalk(    #452
        0x101,
        "#1015F#1PUm, Kilika, what was that about?\x02",
    )

    CloseMessageWindow()

    label("loc_BA2A")


    def lambda_BA30():
        OP_6D(3080, 0, 500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA30)
    OP_8E(0x8, 0x14B4, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #453
        0x8,
        (
            "#791FThat was Elnan at the Grancel branch.\x02\x03",

            "It seems Her Majesty the Queen would\x01",
            "like to speak with you.\x02\x03",

            "The message is to stop by the palace\x01",
            "if you visit Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        "#1004F#1PThe QUEEN?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB92")

    ChrTalk(    #455
        0x103,
        (
            "#023FWell, that's a bit of a shock.\x01",
            "I wonder what she wants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC65")

    label("loc_BB92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBD7")

    ChrTalk(    #456
        0x106,
        (
            "#052FKinda outta the blue...\x01",
            "Wonder what's up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC65")

    label("loc_BBD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC65")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC2E")

    ChrTalk(    #457
        0x108,
        (
            "#073F#6PThis is a surprise.\x01",
            "I wonder what she wants.\x02",
        )
    )

    Jump("loc_BC64")

    label("loc_BC2E")


    ChrTalk(    #458
        0x108,
        (
            "#073FThis is a surprise.\x01",
            "I wonder what she wants.\x02",
        )
    )


    label("loc_BC64")

    CloseMessageWindow()

    label("loc_BC65")


    ChrTalk(    #459
        0x8,
        (
            "#792FHe did not share details.\x02\x03",

            "#790FIt seemed to be something he did\x01",
            "not want to discuss on the phone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        (
            "#1015F#1PSomething you can't say over the phone...\x02\x03",

            "#1026FI get it, phone calls run the\x01",
            "risk of being intercepted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x102,
        "#1042F#6PIt must be something secret, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x8,
        (
            "#792FElnan made clear the situation is\x01",
            "not an emergency, however.\x02\x03",

            "#791FStopping by when you have time\x01",
            "will be enough, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x101,
        "#1006F#1PHmm. Okay, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE72")

    ChrTalk(    #464
        0x108,
        "#070F#6PWe will find a chance to visit, then!\x02",
    )

    Jump("loc_BEA1")

    label("loc_BE72")


    ChrTalk(    #465
        0x108,
        "#070FWe will find a chance to visit, then!\x02",
    )


    label("loc_BEA1")

    CloseMessageWindow()
    Jump("loc_BED6")

    label("loc_BEA5")


    ChrTalk(    #466
        0x102,
        "#1040F#6PWe'll try to find some time, then.\x02",
    )

    CloseMessageWindow()

    label("loc_BED6")

    OP_A2(0x2006)
    OP_28(0x9B, 0x1, 0x100)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2510, 0, -2680, 180)
    SetChrPos(0x1, 2510, 0, -2680, 180)
    SetChrPos(0x2, 2510, 0, -2680, 180)
    SetChrPos(0x3, 2510, 0, -2680, 180)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_20_B571 end

    def Function_21_BF93(): pass

    label("Function_21_BF93")

    OP_43(0x101, 0x1, 0x0, 0x10)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x11)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0xF9, 0x1)
    Return()

    # Function_21_BF93 end

    def Function_22_BFC4(): pass

    label("Function_22_BFC4")

    OP_8E(0xFE, 0x636, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC12, 0x0, 0xFFFFFD44, 0x7D0, 0x0)

    def lambda_BFF2():

        label("loc_BFF2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_BFF2")

    QueueWorkItem2(0xFE, 2, lambda_BFF2)
    Return()

    # Function_22_BFC4 end

    def Function_23_BFFE(): pass

    label("Function_23_BFFE")

    OP_8E(0xFE, 0x9E2, 0x0, 0xFFFFEE26, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF0A, 0x0, 0xFFFFFD44, 0x7D0, 0x0)

    def lambda_C02C():

        label("loc_C02C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C02C")

    QueueWorkItem2(0xFE, 2, lambda_C02C)
    Return()

    # Function_23_BFFE end

    def Function_24_C038(): pass

    label("Function_24_C038")

    OP_8E(0xFE, 0x636, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x91A, 0x0, 0xFFFFFAD8, 0x7D0, 0x0)

    def lambda_C066():

        label("loc_C066")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C066")

    QueueWorkItem2(0xFE, 2, lambda_C066)
    Return()

    # Function_24_C038 end

    def Function_25_C072(): pass

    label("Function_25_C072")

    OP_8E(0xFE, 0x9E2, 0x0, 0xFFFFEE26, 0x7D0, 0x0)
    OP_8E(0xFE, 0x122A, 0x0, 0xFFFFFC68, 0x7D0, 0x0)

    def lambda_C0A0():

        label("loc_C0A0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C0A0")

    QueueWorkItem2(0xFE, 2, lambda_C0A0)
    Return()

    # Function_25_C072 end

    def Function_26_C0AC(): pass

    label("Function_26_C0AC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0CC")
    Call(0, 27)
    Call(0, 29)
    FadeToBright(0, 0)

    label("loc_C0CC")

    Fade(1000)
    OP_6D(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 4360, 0, -720, 0)
    SetChrPos(0x102, 3220, 0, -700, 0)
    SetChrPos(0xF8, 4600, 0, -1800, 0)
    SetChrPos(0xF9, 3230, 0, -1800, 0)
    OP_8C(0x8, 180, 0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    OP_0D()

    ChrTalk(    #467
        0x8,
        "#790F#4POh... Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x101,
        "#1002F#6PYeah, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #469
        (
            "\x07\x05Estelle asked Kilika to inquire with Leiston Fortress\x01",
            "about the Combustion Engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #470
        0x8,
        (
            "#791F#4PThat's quite a bracer-oriented job\x01",
            "you're working on.\x02\x03",

            "The fortress phone should be working,\x01",
            "so I'll ask right away.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C2B7():
        OP_6D(3670, 0, 1500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2B7)
    OP_8E(0x8, 0x14E6, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0x14E6, 0x0, 0x9BA, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)
    OP_22(0x83, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(    #471
        0x8,
        (
            "#792F...\x02\x03",

            "#790FPardon me, this is the Zeiss Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #472
        0x8,
        (
            "#792F...Ah, I see.\x02\x03",

            "#791FI understand the circumstances.\x01",
            "I will let them know.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)

    def lambda_C403():
        OP_6D(2920, 0, 700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C403)
    OP_8E(0x8, 0x14B4, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #473
        0x8,
        (
            "#792F#4PTo cut to the chase, the Combustion Engine\x01",
            "isn't at the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        "#1020F#6PSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x102,
        "#1044F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x8,
        (
            "#790F#4PIt had just been loaded onto a patrol ship\x01",
            "to send it back to the central factory,\x01",
            "apparently.\x02\x03",

            "And that patrol ship had to make an emergency\x01",
            "landing on the Tratt Plains when the orbal\x01",
            "energy cut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x101,
        "#1004F#6PAh... Crap.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C607")

    ChrTalk(    #478
        0x108,
        "#070F#6PI see, so that's what's going on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C67D")

    label("loc_C607")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C640")

    ChrTalk(    #479
        0x103,
        "#027F#6PSo that's what's going on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C67D")

    label("loc_C640")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C67D")

    ChrTalk(    #480
        0x106,
        "#051F#6PI see, so that's what's going on.\x02",
    )

    CloseMessageWindow()

    label("loc_C67D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6DB")

    ChrTalk(    #481
        0x107,
        (
            "#560F#6PSo, then, we just have to ask the\x01",
            "soldiers on that patrol ship?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C728")

    label("loc_C6DB")


    ChrTalk(    #482
        0x102,
        (
            "#1040F#6PSo, then, we just have to ask the\x01",
            "soldiers on the patrol ship?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C728")


    ChrTalk(    #483
        0x8,
        (
            "#792F#4PThat would be the idea.\x02\x03",

            "#791FThe patrol ship should have landed somewhere on\x01",
            "the Tratt Plains, so you'll have to search for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x200C)
    OP_28(0xC2, 0x1, 0x10)
    OP_28(0xC2, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_26_C0AC end

    def Function_27_C7C8(): pass

    label("Function_27_C7C8")

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
        (0, "loc_C841"),
        (1, "loc_C847"),
        (SWITCH_DEFAULT, "loc_C84D"),
    )


    label("loc_C841")

    OP_A2(0x1200)
    Jump("loc_C84D")

    label("loc_C847")

    OP_A2(0x1201)
    Jump("loc_C84D")

    label("loc_C84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C85B")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_C85F")

    label("loc_C85B")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_C85F")

    Return()

    # Function_27_C7C8 end

    def Function_28_C860(): pass

    label("Function_28_C860")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C89A")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_C8B4")

    label("loc_C89A")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_C8B4")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_28_C860 end

    def Function_29_C8C6(): pass

    label("Function_29_C8C6")

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

    # Function_29_C8C6 end

    SaveToFile()

Try(main)
