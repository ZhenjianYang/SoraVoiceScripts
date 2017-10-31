from ED6SCScenarioHelper import *

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
            'ED6_DT21/T0121   ._SN',
            'ED6_DT21/T0121_1 ._SN',
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
        'Aina',                                 # 9
        'Scherazard',                           # 10
        'Agate',                                # 11
        'Olivier',                              # 12
        'Kloe',                                 # 13
        'Tita',                                 # 14
        'Zin',                                  # 15
        'Mayor Klaus',                          # 16
        'Rinon',                                # 17
        'Ridge',                                # 18
        'Bloom',                                # 19
        'Kitty',                                # 20
        'Fate',                                 # 21
        'Mine Chief Gaton',                     # 22
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
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00053 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT07/CH00073 ._CH',             # 0A
        'ED6_DT07/CH02350 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01760 ._CH',             # 0D
        'ED6_DT07/CH01010 ._CH',             # 0E
        'ED6_DT26/CH20241 ._CH',             # 0F
        'ED6_DT07/CH01770 ._CH',             # 10
        'ED6_DT26/CH20311 ._CH',             # 11
        'ED6_DT06/CH20049 ._CH',             # 12
        'ED6_DT07/CH01020 ._CH',             # 13
        'ED6_DT07/CH01530 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00053P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT07/CH00073P._CP',             # 0A
        'ED6_DT07/CH02350P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01760P._CP',             # 0D
        'ED6_DT07/CH01010P._CP',             # 0E
        'ED6_DT26/CH20241P._CP',             # 0F
        'ED6_DT07/CH01770P._CP',             # 10
        'ED6_DT26/CH20311P._CP',             # 11
        'ED6_DT06/CH20049P._CP',             # 12
        'ED6_DT07/CH01020P._CP',             # 13
        'ED6_DT07/CH01530P._CP',             # 14
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -355,
        Z                   = 0,
        Y                   = 71450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2110,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2380,
        Y                   = 0,
        Z                   = 109620,
        Range               = 5580,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1B0E4,
        Unknown_18          = 0x10000,
        Unknown_1C          = 12,
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
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
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
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_39E",          # 00, 0
        "Function_1_77C",          # 01, 1
        "Function_2_7C3",          # 02, 2
        "Function_3_940",          # 03, 3
        "Function_4_9C1",          # 04, 4
        "Function_5_9C6",          # 05, 5
        "Function_6_9CB",          # 06, 6
        "Function_7_235C",         # 07, 7
        "Function_8_5012",         # 08, 8
        "Function_9_5660",         # 09, 9
        "Function_10_614B",        # 0A, 10
        "Function_11_6922",        # 0B, 11
        "Function_12_6C10",        # 0C, 12
        "Function_13_6E2A",        # 0D, 13
        "Function_14_720F",        # 0E, 14
        "Function_15_7331",        # 0F, 15
        "Function_16_7573",        # 10, 16
        "Function_17_7756",        # 11, 17
        "Function_18_7931",        # 12, 18
        "Function_19_7A5A",        # 13, 19
        "Function_20_7CC5",        # 14, 20
        "Function_21_879F",        # 15, 21
        "Function_22_B074",        # 16, 22
        "Function_23_B090",        # 17, 23
        "Function_24_B0C0",        # 18, 24
        "Function_25_B0DC",        # 19, 25
        "Function_26_B111",        # 1A, 26
        "Function_27_B158",        # 1B, 27
        "Function_28_B1C0",        # 1C, 28
        "Function_29_B228",        # 1D, 29
        "Function_30_B290",        # 1E, 30
        "Function_31_CAE4",        # 1F, 31
        "Function_32_CB00",        # 20, 32
        "Function_33_CB35",        # 21, 33
        "Function_34_CB5B",        # 22, 34
        "Function_35_CBB0",        # 23, 35
        "Function_36_CBF2",        # 24, 36
        "Function_37_E67D",        # 25, 37
        "Function_38_E7AF",        # 26, 38
        "Function_39_E800",        # 27, 39
        "Function_40_E889",        # 28, 40
    )


    def Function_0_39E(): pass

    label("Function_0_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F6")
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD")
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_3F3")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_3F3")

    label("loc_3E2")

    SetChrPos(0x13, 44360, 0, -2420, 270)

    label("loc_3F3")

    Jump("loc_4D4")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_441")
    SetChrPos(0x11, 4300, 0, 114900, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_426")
    SetChrPos(0x12, 44800, 0, 2410, 180)

    label("loc_426")

    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_474")
    SetChrPos(0x11, -1050, 0, 67400, 180)
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_4D4")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, 47500, 0, -1110, 270)
    Jump("loc_4D4")

    label("loc_4CF")

    SetChrFlags(0x13, 0x80)

    label("loc_4D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_52C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_55F")
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 18)
    Jump("loc_564")

    label("loc_55F")

    SetChrChipByIndex(0xB, 9)

    label("loc_564")

    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_598")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_5E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62A")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 7)
    SetChrPos(0x9, 1060, 200, 69820, 360)

    label("loc_62A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_657")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_67A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6C6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F0)
    Event(1, 4)
    Jump("loc_77B")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6DC")
    SetMapFlags(0x10000000)
    OP_A3(0x10F1)
    Event(1, 5)
    Jump("loc_77B")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_6F2")
    SetMapFlags(0x10000000)
    OP_A3(0x10F2)
    Event(0, 36)
    Jump("loc_77B")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_708")
    SetMapFlags(0x10000000)
    OP_A3(0x10F3)
    Event(1, 3)
    Jump("loc_77B")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_71E")
    SetMapFlags(0x10000000)
    OP_A3(0x10F4)
    Event(1, 18)
    Jump("loc_77B")

    label("loc_71E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_72A"),
        (SWITCH_DEFAULT, "loc_77B"),
    )


    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_742")
    SetMapFlags(0x10000000)
    Event(1, 7)
    Jump("loc_778")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75A")
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_778")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_778")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_778")

    Jump("loc_77B")

    label("loc_77B")

    Return()

    # Function_0_39E end

    def Function_1_77C(): pass

    label("Function_1_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A0")
    OP_B1("t0121_y")
    Jump("loc_7A9")

    label("loc_7A0")

    OP_B1("t0121_n")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 3)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C2")

    Return()

    # Function_1_77C end

    def Function_2_7C3(): pass

    label("Function_2_7C3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_92A")

    label("loc_7E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_92A")

    label("loc_801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_92A")

    label("loc_81A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_92A")

    label("loc_833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_92A")

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_865")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_92A")

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_92A")

    label("loc_87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_92A")

    label("loc_897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_92A")

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_92A")

    label("loc_8C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_92A")

    label("loc_8E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_92A")

    label("loc_8FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_92A")

    label("loc_914")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_92A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_92A")

    label("loc_93F")

    Return()

    # Function_2_7C3 end

    def Function_3_940(): pass

    label("Function_3_940")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C0")
    OP_8E(0xFE, 0x18D8, 0x0, 0xFFFFFC5E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x18D8, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x1630, 0x0, 0xFFFFF178, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1716, 0x0, 0xFFFFED54, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(3000)
    Jump("Function_3_940")

    label("loc_9C0")

    Return()

    # Function_3_940 end

    def Function_4_9C1(): pass

    label("Function_4_9C1")

    Call(0, 6)
    Return()

    # Function_4_9C1 end

    def Function_5_9C6(): pass

    label("Function_5_9C6")

    Call(0, 7)
    Return()

    # Function_5_9C6 end

    def Function_6_9CB(): pass

    label("Function_6_9CB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A42")
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
    Jump("loc_A46")

    label("loc_A42")

    Call(6, 5)

    label("loc_A46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE4")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x3)

    ChrTalk(    #0
        0x8,
        (
            "#740FI'd call this a job well done.\x02\x03",

            "Let me know if you finish any more\x01",
            "requests on the board, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEA")

    label("loc_AE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_B5D")

    ChrTalk(    #1
        0x8,
        (
            "#740FI'd call this a job well done.\x02\x03",

            "Let me know if you finish any more\x01",
            "requests on the board, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEA")

    label("loc_B5D")


    ChrTalk(    #2
        0x8,
        (
            "#740FDoesn't look like you have anything\x01",
            "to report at the moment.\x02\x03",

            "Let me know if you finish any more\x01",
            "requests on the board, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEA")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D04")

    ChrTalk(    #3
        0x8,
        (
            "#740FNeed me to get in contact with the gang?\x02\x03",

            "No problem. I'll give the other branches a\x01",
            "call right now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Aina contacted the other branches and had members on\x01",
            "standby assemble.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_D04")

    TalkEnd(0x8)
    Return()

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1C")
    TalkEnd(0x8)
    Return()

    label("loc_D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_E7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D81")

    ChrTalk(    #5
        0x8,
        (
            "#740FYou guys did great work out there today.\x02\x03",

            "I hope you'll keep up the pace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E77")

    label("loc_D81")


    ChrTalk(    #6
        0x8,
        (
            "#740FWe weren't prepared for just how much the\x01",
            "Orbal Shutdown Phenomenon would affect\x01",
            "us.\x02\x03",

            "We need to be able to anticipate situations\x01",
            "like the Malga Mine incident.\x02\x03",

            "All of you need to be careful. Whatever you\x01",
            "do, don't let your guard down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E77")

    Jump("loc_2358")

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_END)), "loc_F2B")

    ChrTalk(    #7
        0x8,
        (
            "#740FTurns out that news from earlier wasn't\x01",
            "nearly as urgent as we thought.\x02\x03",

            "Just swing by the branch whenever you\x01",
            "happen to stop by the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1060")

    label("loc_F2B")


    ChrTalk(    #8
        0x8,
        (
            "#740FFor now, why not patrol the area after checking the\x01",
            "board?\x02\x03",

            "I'm curious about what's happening at the mine.\x01",
            "Last I heard, Ridge was on security until we finished\x01",
            "laying out the plans to block off that monster's nest.\x02\x03",

            "I'd feel more at ease if you checked in over there to\x01",
            "see how things are going. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1060")

    OP_A2(0x1)
    Jump("loc_10FD")

    label("loc_1066")


    ChrTalk(    #9
        0x8,
        (
            "#740FFor now, why not patrol the area after checking the\x01",
            "board?\x02\x03",

            "I'd feel more at ease if you checked in over there to\x01",
            "see how things are going. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FD")

    Jump("loc_2358")

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_13BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1312")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B2")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(    #10
        0x8,
        "#740FHey, Olivier. Feeling better?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x104,
        (
            "#035FBut of course.\x02\x03",

            "Such a trifling amount of alcohol isn't\x01",
            "enough to fell one such as I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#740FThat's what I like to hear!\x02\x03",

            "#741FWe'll have to hit it even harder next time\x01",
            "we go out drinking. What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x104,
        (
            "#037FHa... Haha... Ha...\x01",
            "I...would be...honored...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F(I've never seen such naked fear in\x01",
            "a man's eyes.)\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x76, 0x1, 0x400)
    Jump("loc_130F")

    label("loc_12B2")


    ChrTalk(    #15
        0x8,
        (
            "#740FIt's been a while since I've gone out\x01",
            "drinking. It was nice.\x02\x03",

            "Take care, you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130F")

    Jump("loc_13BA")

    label("loc_1312")


    ChrTalk(    #16
        0x8,
        (
            "#740FOlivier's on standby on the second floor.\x02\x03",

            "He's a bit slow on the uptake right now,\x01",
            "but I'm sure he'll be able to do his job\x01",
            "just fine.\x02\x03",

            "Take care, you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BA")

    Jump("loc_1626")

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(    #17
        0x8,
        (
            "#740FI've already ordered tickets to Bose for\x01",
            "you.\x02\x03",

            "Just let Alan at the landing port know\x01",
            "and he should get you all squared away.\x02\x03",

            "Take care, you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1626")

    label("loc_1465")


    ChrTalk(    #18
        0x8,
        (
            "#740FI've already ordered you tickets for the\x01",
            "next scheduled liner.\x02\x03",

            "Just let Alan at the landing port know\x01",
            "and he should get you all squared away.\x02\x03",

            "#744FAt this point, the only region where there\x01",
            "hasn't been an 'experiment' is Bose.\x02\x03",

            "I'm worried that they're just going to keep\x01",
            "getting tougher and tougher...\x02\x03",

            "#740FNot anything you can't handle, though.\x01",
            "I know we can count on you.\x02\x03",

            "Keep up the good work, okay? I'm always\x01",
            "rooting for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1626")

    Jump("loc_2358")

    label("loc_1629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_188B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_170E")

    ChrTalk(    #19
        0x8,
        (
            "#740FGiven that you've chosen to step willingly\x01",
            "into their trap, I'm not going to waste time\x01",
            "telling you to be careful.\x02\x03",

            "Show them what a bracer can do. Give that\x01",
            "no-good criminal the beating of their life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1888")

    label("loc_170E")


    ChrTalk(    #20
        0x8,
        (
            "#740FYou have my full backing as guild manager.\x02\x03",

            "Going to Mistwald isn't much different than\x01",
            "jumping right into a trap, but I know you don't\x01",
            "have much of a choice.\x02\x03",

            "I'm not going to waste time telling you to be\x01",
            "careful. You know what you're getting into.\x02\x03",

            "Show them what a bracer can do. Give that\x01",
            "no-good criminal the beating of their life!\x02\x03",

            "How's that for a pep talk?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1888")

    Jump("loc_2358")

    label("loc_188B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1976")

    ChrTalk(    #21
        0x8,
        (
            "#740FBeen a while since you've visited the farm,\x01",
            "isn't it? Remember to turn south once you've\x01",
            "gone west on Milch Main Road.\x02\x03",

            "The fog out there is just awful, so it won't be\x01",
            "easy to navigate. Proceed with caution.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_1976")


    ChrTalk(    #22
        0x8,
        (
            "#740FYour job is to help evacuate everyone at\x01",
            "Perzel Farm.\x02\x03",

            "Been a while since you've visited, right?\x01",
            "Remember to turn south once you've gone\x01",
            "west on Milch Main Road.\x02\x03",

            "The fog's gotten even worse since yesterday.\x01",
            "It's nearly impossible to see through.\x02\x03",

            "I know you might think you know the way,\x01",
            "but the fog won't make it easy on you.\x01",
            "Proceed with caution. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1AE2")

    Jump("loc_2358")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_20A3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_END)), "loc_1B07")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_END)), "loc_1B18")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_1B29")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B29")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B52"),
        (1, "loc_1CD5"),
        (2, "loc_1D7E"),
        (4, "loc_1E22"),
        (3, "loc_1ECD"),
        (5, "loc_1F3A"),
        (6, "loc_1FAA"),
        (7, "loc_2019"),
        (SWITCH_DEFAULT, "loc_209D"),
    )


    label("loc_1B52")


    ChrTalk(    #23
        0x8,
        (
            "#740FI want you to check just how much the fog covers.\x02\x03",

            "The most efficient way to go about it is so check\x01",
            "the Elize Highway to the south, the Milch Main Road\x01",
            "to the west, and the Malga Trail to the north.\x02\x03",

            "Try to see how far along the fog reaches along all\x01",
            "three roads.\x02\x03",

            "It's getting harder to see what's in front of you by\x01",
            "the day, so proceed carefully with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1CD5")


    ChrTalk(    #24
        0x8,
        (
            "#740FSounds like things are going smoothly\x01",
            "enough.\x02\x03",

            "All that's left is the Milch Main Road\x01",
            "to the west and the Malga Trail to the\x01",
            "north.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1D7E")


    ChrTalk(    #25
        0x8,
        (
            "#740FSounds like things are going smoothly\x01",
            "enough.\x02\x03",

            "All that's left is Elize Highway to the\x01",
            "south and the Malga Trail to the north.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1E22")


    ChrTalk(    #26
        0x8,
        (
            "#740FSounds like things are going smoothly\x01",
            "enough.\x02\x03",

            "All that's left is the Elize Highway to\x01",
            "the south and the Milch Main Road to\x01",
            "the west.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1ECD")


    ChrTalk(    #27
        0x8,
        (
            "#740FAll that's left for your investigation is the\x01",
            "Malga Trail to the north.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1F3A")


    ChrTalk(    #28
        0x8,
        (
            "#740FAll that's left for your investigation is the\x01",
            "Milch Main Road to the west.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_1FAA")


    ChrTalk(    #29
        0x8,
        (
            "#740FAll that's left for your investigation is the\x01",
            "Elize Highway to the south.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A0")

    label("loc_2019")


    ChrTalk(    #30
        0x8,
        (
            "#743FI thought you said something about\x01",
            "going home?\x02\x03",

            "#740FGo on. You can get back to work on\x01",
            "the fog investigation afterward. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_209D")

    Jump("loc_20A0")

    label("loc_20A0")

    Jump("loc_2358")

    label("loc_20A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 5)), scpexpr(EXPR_END)), "loc_2260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20E2")

    ChrTalk(    #31
        0x8,
        "#740FGo on home for now, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_225D")

    label("loc_20E2")

    TurnDirection(0x8, 0x142, 0)

    ChrTalk(    #32
        0x8,
        "#740FSir, are you from the Septian Church?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x142,
        "#1060FThat's right. Kevin Graham's the name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#742F(I'm not sure what happened, but I've\x01",
            "never seen Estelle this out of sorts.)\x02\x03",

            "#740F(I know it's a lot to ask, but could I ask\x01",
            "you to stay with her until she's calmed\x01",
            "down?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x142,
        "#1060F(Trust me, I'm on top of it.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "#740FThank you, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#505FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_225D")

    Jump("loc_2358")

    label("loc_2260")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 400)
    Sleep(600)
    OP_63(0x8)

    ChrTalk(    #38
        0x8,
        (
            "#743F...Estelle?!\x02\x03",

            "What's wrong? I thought you were going\x01",
            "to be in Grancel for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#000FHa ha, well, Joshua came home early,\x01",
            "so I'm trying to catch up with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#743FHe did...?\x02\x03",

            "#742F...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102D)

    label("loc_2358")

    TalkEnd(0x8)
    Return()

    # Function_6_9CB end

    def Function_7_235C(): pass

    label("Function_7_235C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2374")
    Call(0, 20)
    Jump("loc_5011")

    label("loc_2374")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23D0")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B6")
    OP_A9(0x6)
    Jump("loc_23B8")

    label("loc_23B6")

    OP_A9(0x2)

    label("loc_23B8")

    TalkEnd(0x10)
    Return()

    label("loc_23BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D0")
    TalkEnd(0x10)
    Return()

    label("loc_23D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A5")
    TurnDirection(0x10, 0x101, 0)

    ChrTalk(    #41
        0x10,
        "Hey-hey! Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "At long last, the two of you have\x01",
            "made your long-awaited appearance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1008FUh, appearance? We're not ghosts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1040FYou're the same as you ever were,\x01",
            "Rinon.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #45
        0x10,
        (
            "I'm always as good as my business.\x01",
            "And business is great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "W-Well, I guess I do kinda have a vague\x01",
            "sense of unease about my future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1044FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1011FDid something happen?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #49
        0x10,
        "N-No... Never mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "Well, putting me aside, this is your\x01",
            "first time back home in a while, right,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "Times may be hard with all the stuff going\x01",
            "on right now, but I hope you'll have the\x01",
            "chance to take a breather soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#1048FYes, well...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x2098)
    Jump("loc_2CE3")

    label("loc_26A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_27B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2743")

    ChrTalk(    #53
        0x10,
        "Kitty just got back from a delivery.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "She sure was acting super cheerful\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "I guess something good happened?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_27AF")

    label("loc_2743")


    ChrTalk(    #56
        0x10,
        (
            "Kitty was all smiles after she\x01",
            "returned from that last delivery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "I guess something good happened?\x02",
    )

    CloseMessageWindow()

    label("loc_27AF")

    Jump("loc_2CE3")

    label("loc_27B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_29C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2882")

    ChrTalk(    #58
        0x10,
        (
            "Times may be hard with all the stuff going\x01",
            "on right now, but I hope you'll have the\x01",
            "chance to take a breather soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "Especially you, Joshua. This is your\x01",
            "first time back in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BF")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2935")

    ChrTalk(    #60
        0x10,
        "Hey, Estelle, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "I heard there was some trouble\x01",
            "over at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "I guess it comes as no surprise, seeing\x01",
            "as the orbments all suddenly cut out. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_29BF")

    label("loc_2935")


    ChrTalk(    #63
        0x10,
        (
            "I heard there was some trouble\x01",
            "over at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "I guess it comes as no surprise, seeing\x01",
            "as the orbments all suddenly cut out. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BF")

    Jump("loc_2CE3")

    label("loc_29C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0D")

    ChrTalk(    #65
        0x102,
        "#1044FBy the way, Rinon?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #66
        0x10,
        "Hmm? What is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x13, 400)

    ChrTalk(    #67
        0x102,
        "#1040FIs that a new employee over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        "Y-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "She's s-something like a part-timer,\x01",
            "or a freeloader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "My mother brought her, so I'm having\x01",
            "her help around the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1035FI-I see...\x01",
            "(Sounds like he's in a tight spot...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20D6)
    Jump("loc_2CE3")

    label("loc_2B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C22")

    ChrTalk(    #72
        0x10,
        (
            "The store's been running pretty\x01",
            "smoothly ever since Kitty arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "She's really opened up to me.\x01",
            "We're practically family now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "And don't get me wrong, that's a\x01",
            "good thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "I just kind of feel like a puppet being\x01",
            "strung along sometimes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2CE3")

    label("loc_2C22")


    ChrTalk(    #76
        0x10,
        (
            "She's really opened up to me.\x01",
            "We're practically family now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "And don't get me wrong, that's a\x01",
            "good thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "*sigh* I feel like things are going\x01",
            "EXACTLY as my mother planned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE3")

    Jump("loc_500E")

    label("loc_2CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 6)), scpexpr(EXPR_END)), "loc_2F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2DD8")

    ChrTalk(    #79
        0x10,
        (
            "Apparently, Kitty's going to be\x01",
            "staying around here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        "I have to admit, she's been a huge help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "But I can't shake the feeling like\x01",
            "everything's going according to my\x01",
            "mother's plans... *siiigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F17")

    label("loc_2DD8")


    ChrTalk(    #82
        0x10,
        (
            "Kitty's going to be staying around here\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10,
        (
            "She said she's using this experience\x01",
            "to help train her for when she sets up\x01",
            "her own shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "And it's...it's hard to describe. I'm kind\x01",
            "of happy, and I'm kind of scared, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10,
        (
            "I admit that having her around the store\x01",
            "has been a huge help, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2F17")

    Jump("loc_3111")

    label("loc_2F1A")

    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #86
        0x10,
        "Hey, Estelle, Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        "I heard you're heading out soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1016FWow, news sure travels fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#020FMmmhmm. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "Thanks to you, I've been able to\x01",
            "resume ordering stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "If you need anything, you should\x01",
            "buy it before you leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1000FYeah, thanks, Rinon.\x02\x03",

            "If you get any more rare sneakers\x01",
            "in stock, hold onto them for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        "Haha, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10,
        "Good luck, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x103,
        (
            "#027FWe'll come back to shop during\x01",
            "our downtime, promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1001FLater, Rinon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x1A56)

    label("loc_3111")

    Jump("loc_500E")

    label("loc_3114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_31AC")

    ChrTalk(    #97
        0x10,
        (
            "I guess it makes sense since she\x01",
            "does work at the department store\x01",
            "in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10,
        "Kitty does a good job around here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_31AC")


    ChrTalk(    #99
        0x10,
        "Oh, right. See that woman over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "That's Kitty. She's from the capital,\x01",
            "and she's helping out at the store\x01",
            "for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        (
            "It's, um, it's sort of a short-term,\x01",
            "part-time job.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3275")

    Jump("loc_380F")

    label("loc_3278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_34B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32FD")

    ChrTalk(    #102
        0x10,
        "Kitty's a hard worker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        (
            "I gotta admit, if I were to pick a partner\x01",
            "for my life, I'd pick someone like her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B0")

    label("loc_32FD")


    ChrTalk(    #104
        0x10,
        "Kitty's a hard worker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "That whole thing about helping out at\x01",
            "the store was originally my mom's\x01",
            "suggestion, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "From the way she acts, it looks like\x01",
            "she really does enjoy the work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "I'm not exactly searching for a wife\x01",
            "like my mom was doing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "I gotta admit, if I were to pick a partner\x01",
            "for my life, I'd pick someone like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "I feel like I could get along well with\x01",
            "someone who likes shop work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_34B0")

    Jump("loc_380F")

    label("loc_34B3")

    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #110
        0x10,
        "Oh, Estelle! You finally came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1017FIt's been ages, Rinon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "I'd heard from one of my customers\x01",
            "that you finally showed your face\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10,
        (
            "I've been waiting for you to drop in\x01",
            "ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1025FAww, sorry it took me so long.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        "No, no. No problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10,
        "Still, what a time to come back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        "The fog's been really bad today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1007FYeah, seriously...\x02\x03",

            "#1015FOh, yeah, that reminds me...\x01",
            "Was everything okay last night?\x02\x03",

            "Did anything happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10,
        "No, nothing in particular happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        (
            "Wait, a red-haired bracer did drop by\x01",
            "before I went to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10,
        (
            "He said he was on patrol.\x01",
            "He a friend of yours from work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1006FYeah, that's Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        "#027FGuess he was making his rounds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        (
            "Given the craziness,\x01",
            "I'm glad you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x10,
        "If you need anything, come on by.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x1885)

    label("loc_380F")

    Jump("loc_500E")

    label("loc_3812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_43C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_END)), "loc_3B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_38BB")

    ChrTalk(    #127
        0x10,
        (
            "She certainly works like someone\x01",
            "from the capital department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x10,
        (
            "Sometimes, I just get lost in that\x01",
            "bright smile of hers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B46")

    label("loc_38BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A1E")

    ChrTalk(    #129
        0x10,
        (
            "Kitty told me she sells tea at the\x01",
            "capital's department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "That explains why she seems to\x01",
            "know everything and anything about\x01",
            "tea and snacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10,
        (
            "She's got a good sense for product\x01",
            "displays and selecting accessories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10,
        (
            "More than anything, though, her bright\x01",
            "smile and the efficient way she deals\x01",
            "with customers is amazing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3B46")

    label("loc_3A1E")


    ChrTalk(    #133
        0x10,
        "Oh, Estelle. Still need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10,
        "Oh, yeah. I'm sure you've seen her, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10,
        "There's a girl working outside, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10,
        (
            "That's Kitty. She's helping around the\x01",
            "store for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x10,
        (
            "W-Well, it's basically a short-term,\x01",
            "part-time job until the scheduled liners\x01",
            "resume service.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x1885)

    label("loc_3B46")

    Jump("loc_4360")

    label("loc_3B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3BC6")

    ChrTalk(    #138
        0x10,
        (
            "She certainly works like someone\x01",
            "from the capital department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x10,
        "Kitty's very good at her job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CDF")

    label("loc_3BC6")


    ChrTalk(    #140
        0x10,
        "Oh, yeah. I'm sure you've seen her, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10,
        "There's a girl working outside, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10,
        (
            "That's Kitty. She's from the capital, and\x01",
            "she's helping around the store for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10,
        (
            "W-Well, it's basically a short-term,\x01",
            "part-time job until the scheduled liners\x01",
            "resume service.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3CDF")

    Jump("loc_4360")

    label("loc_3CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_4004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3D61")

    ChrTalk(    #144
        0x10,
        (
            "She certainly works like someone from\x01",
            "the capital's department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x10,
        "Kitty's very good at her job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4001")

    label("loc_3D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3EC2")

    ChrTalk(    #146
        0x10,
        (
            "She told me she sells tea at the\x01",
            "capital's department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "That explains why she seems to\x01",
            "know everything and anything about\x01",
            "tea and snacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x10,
        (
            "She's got a good sense for product\x01",
            "displays and selecting accessories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        (
            "More than anything, though, her bright\x01",
            "smile and the efficient way she deals\x01",
            "with customers is amazing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_4001")

    label("loc_3EC2")


    ChrTalk(    #150
        0x10,
        (
            "Morning, Estelle.\x01",
            "Fog's still thick as a wall today, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x10,
        "Oh, yeah. I'm sure you've seen her, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x10,
        "There's a girl working outside, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        (
            "That's Kitty. She's helping around the\x01",
            "store for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10,
        (
            "W-Well, it's basically a short-term,\x01",
            "part-time job until the scheduled liners\x01",
            "resume service.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x1885)

    label("loc_4001")

    Jump("loc_4360")

    label("loc_4004")

    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #155
        0x10,
        "Oh, Estelle! You finally came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1017FIt's been ages, Rinon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        (
            "I'd heard from one of my customers\x01",
            "that you finally showed your face\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10,
        (
            "I've been waiting for you to drop in\x01",
            "ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1025FAww, sorry it took me so long.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10,
        "No, no. No problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10,
        "Still, what a time to come back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        "The fog's been really bad today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1007FYeah, seriously...\x02\x03",

            "#1015FOh, yeah, that reminds me...\x01",
            "Was everything okay last night?\x02\x03",

            "Did anything happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        "Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        "No, nothing in particular happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10,
        (
            "Wait, a red-haired bracer did drop by\x01",
            "before I went to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10,
        (
            "He said he was on patrol.\x01",
            "He a friend of yours from work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#1006FYeah, that's Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        "#027FGuess he was making his rounds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10,
        (
            "Given the craziness,\x01",
            "I'm glad you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x10,
        "If you need anything, come on by.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x1885)

    label("loc_4360")

    Jump("loc_43BD")

    label("loc_4363")


    ChrTalk(    #172
        0x10,
        "If you need anything, come on by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10,
        (
            "We've got everything from candy to\x01",
            "magazines!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BD")

    Jump("loc_500E")

    label("loc_43C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_4630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_449E")

    ChrTalk(    #174
        0x10,
        (
            "My mother came back from the capital\x01",
            "with some woman I've never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        (
            "Did sh-she seriously found a wife for\x01",
            "me to marry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        (
            "Crap... I never should've\x01",
            "let her go to the capital...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_462D")

    label("loc_449E")


    ChrTalk(    #177
        0x10,
        (
            "My mom came back on that last\x01",
            "scheduled liner from the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10,
        (
            "But, wouldn't you know it! She brought\x01",
            "home some woman I've never seen\x01",
            "before in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10,
        (
            "She said they'd met on the airship,\x01",
            "but since this is my mom we're talking\x01",
            "about here, that's totally suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10,
        (
            "Did sh-she seriously found a wife for\x01",
            "me to marry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10,
        (
            "I'm probably just being paranoid,\x01",
            "but then again...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_462D")

    Jump("loc_4B01")

    label("loc_4630")

    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_END)), "loc_46AD")

    ChrTalk(    #182
        0x10,
        "Oh, Estelle. You finally came back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1000FYep. It's been ages, Rinon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_475D")

    label("loc_46AD")


    ChrTalk(    #184
        0x10,
        "Hey, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x10,
        "It's been a while. When did you get home?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1000FPretty much now.\x02\x03",

            "You seem like you're doing all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10,
        "I'm doing great, as a matter of fact.\x02",
    )

    CloseMessageWindow()

    label("loc_475D")


    ChrTalk(    #188
        0x10,
        (
            "So, I heard you went off to do some\x01",
            "training somewhere nuts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10,
        "How'd that turn out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1001FOh, boy, it went gre--\x02\x03",

            "#1015F...Wait, when did I tell you about\x01",
            "my training, Rinon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x10,
        (
            "Haha, don't underestimate neighborhood\x01",
            "gossip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x10,
        (
            "I'm pretty sure everyone knows you went\x01",
            "out to train, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#1016FAhaha... I should've seen that coming. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x103,
        "#020FHaha, it's business as usual in Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x10,
        "By the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x10,
        "This weather sure is weird, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10,
        (
            "I heard the Bose-bound passenger\x01",
            "ships are all grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1007FYeah, we also got stopped by that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x103,
        (
            "#027FWell, since we're stuck here, we plan\x01",
            "on investigating this fog.\x02\x03",

            "The guild would also like to get a better\x01",
            "picture of the situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #200
        0x10,
        "Got'cha. That's encouraging to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10,
        "Just be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x10,
        (
            "Something's strange about this fog.\x01",
            "It doesn't feel normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x103,
        "#020FYes. We'll be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1002FYeah...\x02\x03",

            "#1000FSee ya, Rinon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1885)

    label("loc_4B01")

    Jump("loc_500E")

    label("loc_4B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_500E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_END)), "loc_4BA9")

    ChrTalk(    #205
        0x10,
        (
            "In other news, my mother's been\x01",
            "out scouring the countryside high\x01",
            "and low to find me a wife. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x10,
        "I wish she'd just let it be, already!\x02",
    )

    CloseMessageWindow()
    Jump("loc_500E")

    label("loc_4BA9")


    ChrTalk(    #207
        0x10,
        "Oh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x10,
        "Well, I'll be! It's Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10,
        (
            "It's been ages!\x01",
            "When did you get back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#001FHi, Rinon. I literally just got back now.\x01",
            "You look well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x10,
        "You bet I am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x10,
        (
            "Oh, yeah! We should be getting\x01",
            "the latest Stregas in soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        "#501FWhoa, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x142,
        (
            "#1060FRight, those limited edition ones to\x01",
            "celebrate the 50th anniversary of the\x01",
            "Strega Corporation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x10,
        "Oh, sir, you know a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x142,
        (
            "#1061FHey, what can I say?\x01",
            "A man's gotta love him some kicks.\x02\x03",

            "#1062FI mean, check it! I'm wearing some\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x142, 200)
    TurnDirection(0x101, 0x142, 300)
    Sleep(500)

    ChrTalk(    #217
        0x10,
        "Oh, those are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#004FI...saw those in a magazine.\x02\x03",

            "They're an international-only model,\x01",
            "not sold in Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x142,
        "#1061FBingo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#007FI wanted some, but I couldn't find a way\x01",
            "to import them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x142,
        (
            "#1064FHang on, Estelle, you're big into sneakers\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#506FUh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x142,
        (
            "#1061FCool! Glad we have a shared interest!\x02\x03",

            "#1062FYes, indeed, this too is the guiding\x01",
            "hand of She Above!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        (
            "#509FHang on. Sneakers?\x01",
            "On a priest of the church?\x01",
            "Is that seriously okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10,
        "Wait, this guy's a priest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x142,
        "#1061FD'aww, come on, I'm outnumbered here!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102C)

    label("loc_500E")

    TalkEnd(0x10)

    label("loc_5011")

    Return()

    # Function_7_235C end

    def Function_8_5012(): pass

    label("Function_8_5012")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_501F")
    Jump("loc_565C")

    label("loc_501F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_533F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 7)), scpexpr(EXPR_END)), "loc_50F7")

    ChrTalk(    #227
        0xFE,
        (
            "I know you guys have a hard\x01",
            "mission ahead of you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "You leave the branch to me.\x01",
            "Just focus on your own stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I can handle the jobs that come\x01",
            "by the branch on my own, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_533C")

    label("loc_50F7")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #230
        0xFE,
        "Hey, Schera. I heard from Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "You're heading out to Bose next, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x103,
        "#020FYes, that's the plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1007FSorry, Ridge.\x02\x03",

            "Feels like we're always shoving\x01",
            "off our work on you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #234
        0xFE,
        "Nah, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I've always leaned on Cassius and\x01",
            "Schera until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "I'll manage. It'll be a good opportunity\x01",
            "for me to stand on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x103,
        (
            "#526FI like your style, Ridge!\x02\x03",

            "We'll be away for a while, but hold\x01",
            "down the fort while we're gone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #238
        0xFE,
        "Yeah, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "I hope you guys have a nice trip to Bose.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A57)

    label("loc_533C")

    Jump("loc_565C")

    label("loc_533F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_5489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_53BC")

    ChrTalk(    #240
        0xFE,
        (
            "I'm sure the bell sound I heard came\x01",
            "from Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "It was very faint, but it was a lovely sound.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5486")

    label("loc_53BC")


    ChrTalk(    #242
        0xFE,
        (
            "I'm sure the bell sound I heard came\x01",
            "from Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "It was very faint, but it was a lovely sound.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "To think something like this could happen\x01",
            "while I was away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "My timing sucks...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_5486")

    Jump("loc_565C")

    label("loc_5489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_565C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_54FB")

    ChrTalk(    #246
        0xFE,
        (
            "Congratulations on your promotion to\x01",
            "senior bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "Can't wait to work with you again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_565C")

    label("loc_54FB")


    ChrTalk(    #248
        0xFE,
        "Yo, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "I heard from Aina. Congrats on your\x01",
            "promotion to senior bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        "#006FHaha, thanks, Ridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "Where're Schera and Joshua, though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "Would've expected to see them with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        (
            "#000FSchera's still in Grancel.\x02\x03",

            "Joshua came back home a little ahead\x01",
            "of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "Weird. All right, well, can't wait to work\x01",
            "together again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_565C")

    TalkEnd(0x11)
    Return()

    # Function_8_5012 end

    def Function_9_5660(): pass

    label("Function_9_5660")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_56F0")

    ChrTalk(    #255
        0xFE,
        (
            "The ceremony today was quite lovely.\x01",
            "It really hit me right in the heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I want Rinon to have a ceremony that\x01",
            "lovely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6139")

    label("loc_56F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579E")

    ChrTalk(    #257
        0xFE,
        "The store's been busy all morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Everyone's coming to buy candles\x01",
            "and lamps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "Even though there's a wedding\x01",
            "ceremony today! Really, now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_57F7")

    label("loc_579E")


    ChrTalk(    #260
        0xFE,
        "The store's been busy all morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Everyone's coming to buy candles\x01",
            "and lamps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57F7")

    Jump("loc_6139")

    label("loc_57FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_5C01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_586B")

    ChrTalk(    #262
        0xFE,
        (
            "Thanks to all this, I've remembered\x01",
            "that dish for the first time in a long time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5954")

    label("loc_586B")


    ChrTalk(    #263
        0xFE,
        "Oh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "You must be having a hard time\x01",
            "humoring that old man's whims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "Though I will say it was nice to dig\x01",
            "up memories of that old dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "A part of me is thankful to that old\x01",
            "rascal for reminding me of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5954")

    Jump("loc_5BFE")

    label("loc_5957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_59FB")

    ChrTalk(    #267
        0xFE,
        (
            "I just feel bad for making you all run\x01",
            "around on such a strange errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "There's such a thing as being a little\x01",
            "too generous. Keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BFE")

    label("loc_59FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A26")
    Call(1, 1)
    Jump("loc_5BFE")

    label("loc_5A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5AC4")

    ChrTalk(    #269
        0xFE,
        "I can tell that Rinon is fond of Kitty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "All that's left is to watch and wait.\x01",
            "The bait's in the water, so we'll see\x01",
            "if he takes the hook.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BFE")

    label("loc_5AC4")


    ChrTalk(    #271
        0xFE,
        (
            "Kitty's going to be working at our\x01",
            "store for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "Personally, I'm overjoyed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "I can tell that Rinon is fond of Kitty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "All that's left is to watch and wait.\x01",
            "The bait's in the water, so we'll see\x01",
            "if he takes the hook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "I feel like things'll go better if I just\x01",
            "let them flow naturally.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5BFE")

    Jump("loc_6139")

    label("loc_5C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5C6D")

    ChrTalk(    #276
        0xFE,
        "Rinon's been very impressed with Kitty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "Yes! I've got a good feeling about this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CE6")

    label("loc_5C6D")


    ChrTalk(    #278
        0xFE,
        "Kitty's been working so hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "It's not easy to impress Rinon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "Yes! I've got a good feeling about this.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5CE6")

    Jump("loc_6139")

    label("loc_5CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_5D97")

    ChrTalk(    #281
        0xFE,
        (
            "Kitty's going to be working in the store\x01",
            "from this point forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "I can hear her cheerful voice from\x01",
            "here. It feels nice to have someone\x01",
            "like her around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6139")

    label("loc_5D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_5F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5E4F")

    ChrTalk(    #283
        0xFE,
        "Apparently, that girl intends to go to Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "The scheduled liners stopping is quite\x01",
            "the trouble for people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "For now, she's been welcomed into\x01",
            "our home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F5F")

    label("loc_5E4F")


    ChrTalk(    #286
        0xFE,
        "I met this lovely young lady on the airship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "Unfortunately, due to this fog, she can't go\x01",
            "to her destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "I felt bad for her, so until the ships are\x01",
            "moving again, I welcomed her into my\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "We should help one another out when\x01",
            "times are tough.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5F5F")

    Jump("loc_6139")

    label("loc_5F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_6139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6023")

    ChrTalk(    #290
        0xFE,
        (
            "I've been working so hard trying to\x01",
            "find a bride for my son, and yet he's\x01",
            "completely uninterested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "Such a lack of appreciation for one's\x01",
            "own mother! It's scandalous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6139")

    label("loc_6023")


    ChrTalk(    #292
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "I've had no luck at all finding a good\x01",
            "bride for Rinon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "At this point, I think I'll have to take\x01",
            "my search to the rest of the country!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "It would be good to start at a place\x01",
            "where many people gather...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "Ah, I know! I should begin in the capital.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_6139")

    TalkEnd(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_614A")
    OP_8C(0x12, 180, 0)

    label("loc_614A")

    Return()

    # Function_9_5660 end

    def Function_10_614B(): pass

    label("Function_10_614B")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_61EE")

    ChrTalk(    #297
        0xFE,
        "My, that sure was a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "I didn't think I'd catch the wedding\x01",
            "bouquet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "Heehee, I wonder if it'll actually work\x01",
            "its magic on me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691E")

    label("loc_61EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D1")

    ChrTalk(    #300
        0xFE,
        "Welcome to Rinon General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "We've had a lot of customers today.\x01",
            "I guess that probably has something\x01",
            "to do with all the orbments stopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "Everyone seems to be looking for\x01",
            "emergency gear.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_638F")

    label("loc_62D1")


    ChrTalk(    #303
        0xFE,
        (
            "We've had a lot of customers today.\x01",
            "I guess that probably has something\x01",
            "to do with all the orbments stopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "If there's anything you're looking for,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638F")

    Jump("loc_691E")

    label("loc_6392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_654C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6439")

    ChrTalk(    #305
        0xFE,
        (
            "I've decided to abandon my trip to\x01",
            "Bose and spend my vacation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "I plan on using this opportunity to\x01",
            "study for when I start my own shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6549")

    label("loc_6439")


    ChrTalk(    #307
        0xFE,
        "Welcome to Rinon General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "I've decided to stay here for a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "I plan on using this opportunity to\x01",
            "study for when I start my own shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "Besides, the store owner, Rinon,\x01",
            "has been very good to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "It's as comfortable as being home here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_6549")

    Jump("loc_691E")

    label("loc_654C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_669E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_65E5")

    ChrTalk(    #312
        0xFE,
        (
            "You're bracers, right? In that case,\x01",
            "I recommend some of these handy\x01",
            "medicines to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "You won't regret buying some,\x01",
            "I swear!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_669B")

    label("loc_65E5")


    ChrTalk(    #314
        0xFE,
        (
            "Welcome! Are you members of the\x01",
            "Bracer Guild, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "In that case, I recommend some\x01",
            "of these handy medicines to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "You won't regret buying some,\x01",
            "I swear!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_669B")

    Jump("loc_691E")

    label("loc_669E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_6772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_66D7")

    ChrTalk(    #317
        0xFE,
        "Welcome! Feel free to look around.\x02",
    )

    CloseMessageWindow()
    Jump("loc_676F")

    label("loc_66D7")


    ChrTalk(    #318
        0xFE,
        "Welcome to Rinon General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "We have a wide selection of everyday\x01",
            "needs, from food to magazines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "Please, feel free to look around.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_676F")

    Jump("loc_691E")

    label("loc_6772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_691E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_682D")

    ChrTalk(    #321
        0xFE,
        (
            "I'll be here until the scheduled liners\x01",
            "resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "I plan to help out with the store as\x01",
            "much as I can. They're been so kind\x01",
            "to me, so it's only right that I help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691E")

    label("loc_682D")


    ChrTalk(    #323
        0xFE,
        (
            "I decided to take Miss Bloom up\x01",
            "on her offer and stay with them for\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "I'd like to help out at the store, too,\x01",
            "if I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "I work at the department store in\x01",
            "the capital, so I'm sure I can handle\x01",
            "dealing with customers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_691E")

    TalkEnd(0x13)
    Return()

    # Function_10_614B end

    def Function_11_6922(): pass

    label("Function_11_6922")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B34")

    ChrTalk(    #326
        0xFE,
        "Oh, Estelle...and Joshua, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        "#1030FIt's been a while, Fate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "You two have grown so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "What a relief! Looks like you're\x01",
            "doing just fine as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x102,
        "#1030FYes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "Times are hard for the kingdom\x01",
            "now, as I'm sure you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "And Cassius must be busy now\x01",
            "that's he's back in the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "I know you two will do all in your\x01",
            "power as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        "#1000FYou bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x102,
        (
            "#1030FIf anything should trouble you,\x01",
            "please contact the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        "Of course. Take care.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x209B)
    Jump("loc_6C0C")

    label("loc_6B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6B8B")

    ChrTalk(    #337
        0xFE,
        "If anything happens, I'll contact the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "Of course. Take care.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C0C")

    label("loc_6B8B")


    ChrTalk(    #339
        0xFE,
        (
            "When I woke up this morning,\x01",
            "my orbal light wasn't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "I came out to try and get some\x01",
            "kind of light for my house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C0C")

    TalkEnd(0x14)
    Return()

    # Function_11_6922 end

    def Function_12_6C10(): pass

    label("Function_12_6C10")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CA0")
    Jump("loc_6CE2")

    label("loc_6CA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CBC")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CE2")

    label("loc_6CBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CD8")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CE2")

    label("loc_6CD8")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CE2")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #341
        0xA,
        "#051FYo, what's up?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6D74"),
        (SWITCH_DEFAULT, "loc_6DAE"),
    )


    label("loc_6D74")


    ChrTalk(    #342
        0xA,
        "#051FYeah, yeah, I got it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA7")
    Call(0, 19)
    Jump("loc_6DAB")

    label("loc_6DA7")

    Call(0, 18)

    label("loc_6DAB")

    Jump("loc_6E21")

    label("loc_6DAE")


    ChrTalk(    #343
        0xA,
        (
            "#052FWhat, changed your mind?\x02\x03",

            "#050FWell, if you ever need somebody to\x01",
            "swing a sword around, gimme a call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E21")

    label("loc_6E21")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_12_6C10 end

    def Function_13_6E2A(): pass

    label("Function_13_6E2A")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EBA")
    Jump("loc_6EFC")

    label("loc_6EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6ED6")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EFC")

    label("loc_6ED6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EF2")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EFC")

    label("loc_6EF2")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EFC")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F48")

    ChrTalk(    #344
        0xB,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_7206")

    label("loc_6F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F90")

    ChrTalk(    #345
        0xB,
        (
            "#038FGhhh... Greetings.\x02\x03",

            "D-Did you need something...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FF4")

    label("loc_6F90")


    ChrTalk(    #346
        0xB,
        (
            "#030FGood day.\x02\x03",

            "There is purpose etched upon your\x01",
            "lovely features...but first, perhaps a\x01",
            "song?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF4")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7127")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7052"),
        (SWITCH_DEFAULT, "loc_70B9"),
    )


    label("loc_7052")


    ChrTalk(    #347
        0xB,
        (
            "#037FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_7124")

    label("loc_70B9")


    ChrTalk(    #348
        0xB,
        (
            "#037FOh? Changed your mind?\x02\x03",

            "Well, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7124")

    label("loc_7124")

    Jump("loc_7206")

    label("loc_7127")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7134"),
        (SWITCH_DEFAULT, "loc_719B"),
    )


    label("loc_7134")


    ChrTalk(    #349
        0xB,
        (
            "#030FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_7206")

    label("loc_719B")


    ChrTalk(    #350
        0xB,
        (
            "#030FOh? Changed your mind?\x02\x03",

            "Well, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7206")

    label("loc_7206")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_13_6E2A end

    def Function_14_720F(): pass

    label("Function_14_720F")

    TalkBegin(0xC)

    ChrTalk(    #351
        0xC,
        (
            "#040FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_729A"),
        (SWITCH_DEFAULT, "loc_72CB"),
    )


    label("loc_729A")


    ChrTalk(    #352
        0xC,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_732D")

    label("loc_72CB")


    ChrTalk(    #353
        0xC,
        (
            "#040FI'll stay here for a bit, then.\x02\x03",

            "If you need me for anything,\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_732D")

    label("loc_732D")

    TalkEnd(0xC)
    Return()

    # Function_14_720F end

    def Function_15_7331(): pass

    label("Function_15_7331")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7371")

    ChrTalk(    #354
        0xD,
        (
            "#560FOh, hi, Agate!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73D4")

    label("loc_7371")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73AB")

    ChrTalk(    #355
        0xD,
        "#060FHi, Estelle! What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_73D4")

    label("loc_73AB")


    ChrTalk(    #356
        0xD,
        (
            "#060FHi, guys!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73D4")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7428"),
        (SWITCH_DEFAULT, "loc_74A4"),
    )


    label("loc_7428")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7465")

    ChrTalk(    #357
        0xD,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_748A")

    label("loc_7465")


    ChrTalk(    #358
        0xD,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_748A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_749D")
    Call(0, 19)
    Jump("loc_74A1")

    label("loc_749D")

    Call(0, 18)

    label("loc_74A1")

    Jump("loc_756F")

    label("loc_74A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7514")

    ChrTalk(    #359
        0xD,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756C")

    label("loc_7514")


    ChrTalk(    #360
        0xD,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756C")

    Jump("loc_756F")

    label("loc_756F")

    TalkEnd(0xD)
    Return()

    # Function_15_7331 end

    def Function_16_7573(): pass

    label("Function_16_7573")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7603")
    Jump("loc_7645")

    label("loc_7603")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_761F")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7645")

    label("loc_761F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_763B")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7645")

    label("loc_763B")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7645")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #361
        0xE,
        "#070FHey, how's it going?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76DD"),
        (SWITCH_DEFAULT, "loc_7723"),
    )


    label("loc_76DD")


    ChrTalk(    #362
        0xE,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_771C")
    Call(0, 19)
    Jump("loc_7720")

    label("loc_771C")

    Call(0, 18)

    label("loc_7720")

    Jump("loc_774D")

    label("loc_7723")


    ChrTalk(    #363
        0xE,
        "#070FI'll be here if you need me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_774D")

    label("loc_774D")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_16_7573 end

    def Function_17_7756(): pass

    label("Function_17_7756")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_77E6")
    Jump("loc_7828")

    label("loc_77E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7802")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7828")

    label("loc_7802")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_781E")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7828")

    label("loc_781E")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7828")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #364
        0x9,
        "#020FHm? What is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78BB"),
        (SWITCH_DEFAULT, "loc_78DC"),
    )


    label("loc_78BB")


    ChrTalk(    #365
        0x9,
        "#020FNeed some help?\x02",
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_7928")

    label("loc_78DC")


    ChrTalk(    #366
        0x9,
        (
            "#020FI'll hang around here for a bit, then.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7928")

    label("loc_7928")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_17_7756 end

    def Function_18_7931(): pass

    label("Function_18_7931")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_799C")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_799C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79E5")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_79CF")
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 18)
    Jump("loc_79D4")

    label("loc_79CF")

    SetChrChipByIndex(0xB, 9)

    label("loc_79D4")

    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_79E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A08")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_7A08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A2B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_7A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A58")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_7A58")

    OP_0D()
    Return()

    # Function_18_7931 end

    def Function_19_7A5A(): pass

    label("Function_19_7A5A")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_A3(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AF7")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 7)
    SetChrPos(0x9, 1060, 200, 69820, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ADC")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7ADC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF7")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7AF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B5A")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3F")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5A")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7BB3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B98")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7B98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB3")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C16")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BFB")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C16")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_7C16")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7CC4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #367
        (
            "\x07\x05One of the members on standby was equipped with a Zero Field\x01",
            "Generator. Recovering it and adding it to party inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_7CC4")

    Return()

    # Function_19_7A5A end

    def Function_20_7CC5(): pass

    label("Function_20_7CC5")

    EventBegin(0x0)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D71")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as first re-meeting with Rinon\x01",      # 0
            "Set as already met with Rinon\x01",           # 1
            "No change\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7D65"),
        (1, "loc_7D6B"),
        (SWITCH_DEFAULT, "loc_7D71"),
    )


    label("loc_7D65")

    OP_A3(0x1885)
    Jump("loc_7D71")

    label("loc_7D6B")

    OP_A2(0x1885)
    Jump("loc_7D71")

    label("loc_7D71")

    Fade(1000)
    OP_6D(4490, 0, 1340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 3390, 0, 50, 0)
    SetChrPos(0x103, 4490, 0, 50, 0)
    SetChrPos(0x107, 3240, 0, -1100, 0)
    SetChrPos(0x105, 4350, 0, -1100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FDA")

    ChrTalk(    #368
        0x10,
        "#6POh! Estelle, welcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#1017F#2PRinon! Hi! Sorry I haven't\x01",
            "been in for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x10,
        (
            "#6PIt's okay. I heard from others that\x01",
            "you got back all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x10,
        (
            "#6PI've really been looking forward\x01",
            "to seeing you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        (
            "#1025F#2PReally? Yikes, I'm sorry I didn't\x01",
            "stop in earlier, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x10,
        "#6PNo, no, it's okay. I'm just glad you're safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x10,
        (
            "#6PStill, you picked a heck of a\x01",
            "time to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x10,
        (
            "#6PIt's crazy out there.\x01",
            "That fog STILL hasn't let up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8035")

    label("loc_7FDA")


    ChrTalk(    #376
        0x10,
        "#6PGood morning, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x10,
        (
            "#6PCrazy out there, huh?\x01",
            "That fog still hasn't let up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8035")


    ChrTalk(    #378
        0x101,
        (
            "#1007F#2PTell me about it.\x02\x03",

            "#1015FThat reminds me, how was last night?\x02\x03",

            "Did anything happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x10,
        "#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x10,
        "#6POh, uh, nothing happened, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x10,
        (
            "#6PI guess the biggest event of the evening was\x01",
            "that red-headed bracer who stopped\x01",
            "in before I went to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x10,
        (
            "#6PHe said he was on patrol.\x01",
            "Is he a friend of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x101,
        "#1006F#2PYeah, his name's Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x103,
        (
            "#027FSounds like the gentlemen\x01",
            "are taking their 'manly' patrol seriously,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x107,
        (
            "#064F#2PHmm...\x02\x03",

            "#560FHey, Estelle?\x02\x03",

            "Could we buy something for Agate?\x01",
            "Oh, and everyone else, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8282():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8282)
    Sleep(100)

    def lambda_8295():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8295)
    Sleep(100)

    def lambda_82A8():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_82A8)
    Sleep(200)

    ChrTalk(    #386
        0x101,
        "#1018F#5POoh, nice idea, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x105,
        (
            "#048F#2PWhy not something sweet, then?\x02\x03",

            "It would be a nice pick-me-up\x01",
            "if they're tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x10,
        (
            "#6PSweet, eh? Might I recommend some of this\x01",
            "new chocolate I just got in, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x10,
        (
            "#6PIt's a good, dark-style chocolate that's\x01",
            "a bit more bitter. I find guys tend to really\x01",
            "like it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #390
        "#6P#15W\x07\x05The chocolate's price is 200 mira per bar.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    CloseMessageWindow()

    def lambda_8424():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8424)
    Sleep(100)

    def lambda_8437():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8437)
    Sleep(100)

    def lambda_844A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_844A)
    Sleep(200)

    ChrTalk(    #391
        0x101,
        (
            "#1006F#2P600 mira for all three, then.\x02\x03",

            "Though, uh, I dunno if we should count\x01",
            "Olivier since I kinda doubt he actually\x01",
            "patrolled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x105,
        (
            "#045FNow, now, we should, um...\x01",
            "assume the best.\x02\x03",

            "#542FHow about we all pitch in to show\x01",
            "our thanks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x107,
        "#061F#2PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x103,
        (
            "#021FWell, I suppose it won't hurt to treat\x01",
            "them once in a while.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Add 150 mira\x01",      # 0
            "Add Nothing\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_868D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8617")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_868D")

    label("loc_8617")


    ChrTalk(    #395
        0x10,
        "#6PThank you! Hope they enjoy it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #396
        "\x07\x00Received #1015i x3.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F7, 3)
    SubMira(150)

    label("loc_868D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_878F")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #397
        0x103,
        (
            "#023F#4PHm? We seem to be a bit short.\x02\x03",

            "#025FAh well. I'll cover the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x10,
        "#6PThank you! Hope they enjoy it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #399
        "\x07\x00Received #1015i x3.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F7, 3)

    ChrTalk(    #400
        0x101,
        "#1019F(Erp. Now I feel kinda guilty.)\x02",
    )

    CloseMessageWindow()

    label("loc_878F")

    OP_A2(0xA)
    OP_A2(0x181D)
    OP_A2(0x1885)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_20_7CC5 end

    def Function_21_879F(): pass

    label("Function_21_879F")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 4410, 0, 109480, 0)
    SetChrPos(0x107, 4410, 0, 109480, 0)
    SetChrPos(0x103, 4410, 0, 109480, 0)
    SetChrPos(0x105, 4410, 0, 109480, 0)
    SetChrPos(0xA, 300, 0, 116600, 0)
    SetChrPos(0xE, 1600, 0, 116590, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #401
        0x101,
        "#2PMornin'!\x02",
    )

    CloseMessageWindow()

    def lambda_8896():

        label("loc_8896")

        TurnDirection(0xA, 0x101, 400)
        OP_48()
        Jump("loc_8896")

    QueueWorkItem2(0xA, 1, lambda_8896)

    def lambda_88A7():

        label("loc_88A7")

        TurnDirection(0xE, 0x103, 400)
        OP_48()
        Jump("loc_88A7")

    QueueWorkItem2(0xE, 1, lambda_88A7)

    ChrTalk(    #402
        0x107,
        "#5PGood morning!\x02",
    )

    CloseMessageWindow()

    def lambda_88CE():
        OP_6D(-150, 0, 116560, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88CE)
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(700)
    OP_43(0x103, 0x1, 0x0, 0x17)
    Sleep(700)
    OP_43(0x107, 0x1, 0x0, 0x18)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x19)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)

    ChrTalk(    #403
        0x8,
        "#740FAh, good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xA,
        "#051F#4PThere you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0xE,
        "#070F#4PYou slept well last night, I hope?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        (
            "#1006F#5PYeah, thanks.\x01",
            "Definitely recharged my batteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x103,
        (
            "#524F#5PWhile not necessary, the extra rest was\x01",
            "appreciated. Thanks, you two.\x02\x03",

            "The night patrol wasn't too rough, I hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x107,
        "#560F#5PUm, thank you for doing that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0xE,
        (
            "#071F#4PHah, not at all.\x01",
            "We slept in shifts, so we're fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xA,
        (
            "#051F#4P'Course, there's one of us still passed\x01",
            "out at the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB8")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't seen Olivier at the hotel\x01",      # 0
            "Set as saw Olivier at the hotel\x01",               # 1
            "No change\x01",                                     # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8BAC"),
        (1, "loc_8BB2"),
        (SWITCH_DEFAULT, "loc_8BB8"),
    )


    label("loc_8BAC")

    OP_A3(0x1886)
    Jump("loc_8BB8")

    label("loc_8BB2")

    OP_A2(0x1886)
    Jump("loc_8BB8")

    label("loc_8BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 6)), scpexpr(EXPR_END)), "loc_8C5F")

    ChrTalk(    #411
        0x105,
        "#542F#5PI'm guessing you mean Olivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        (
            "#1006F#5PYeah, we saw him asleep over\x01",
            "at the hotel.\x02\x03",

            "I guess he actually did do his\x01",
            "part last night, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CC8")

    label("loc_8C5F")


    ChrTalk(    #413
        0x105,
        "#542F#5PI'm guessing you mean Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x101,
        (
            "#1004F#5PWhoa! So he really did do his part\x01",
            "last night?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CC8")


    ChrTalk(    #415
        0xE,
        (
            "#070F#4PHahah! That he did.\x02\x03",

            "He wouldn't stop complaining, but I think\x01",
            "some of it was just for show. He did his\x01",
            "job well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x103,
        (
            "#021F#5PWe'll be sure to thank him\x01",
            "later, then.\x02\x03",

            "#022FSo...what's the situation?\x01",
            "Did anything happen overnight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x8,
        (
            "#744FThe night patrol may have been a good idea,\x01",
            "because we've heard no new reports of\x01",
            "people collapsing.\x02\x03",

            "#742FBut...it's as we feared. All of yesterday's\x01",
            "victims are still out cold...and still\x01",
            "completely unresponsive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        "#1007F#5POh, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x107,
        "#063F#5PThat's awful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x103,
        (
            "#022F#5PAlso...do we know of any changes to\x01",
            "the fog?\x02\x03",

            "I swear it's thicker than it was yesterday,\x01",
            "but at this point I'm not sure I trust\x01",
            "myself to make a judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x8,
        (
            "#742FNo, it's definitely getting thicker.\x02\x03",

            "Not only that, but we do have reports of\x01",
            "the size of the cloud expanding, as well.\x02\x03",

            "#744FThe entirety of the Malga Trail is now blanketed,\x01",
            "all the way to the mine entrance, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x101,
        "#1002F#5PReally? Crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x105,
        (
            "#043F#5PIf this gets much worse, keeping people\x01",
            "safe will be impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x8,
        (
            "#740FWell, it's not ALL bad news.\x02\x03",

            "Between the reports from us and others,\x01",
            "the Royal Army's agreed to dispatch two\x01",
            "full squads here.\x02\x03",

            "They'll take over the defense of the city\x01",
            "proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1018F#5PReally? Sweet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x8,
        (
            "#741FYes. They'll be coming from Bose,\x01",
            "over the Verte Bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x103,
        (
            "#021F#5PThat'll be a relief.\x02\x03",

            "If the army can take care of the city,\x01",
            "that leaves us free to investigate the\x01",
            "entire region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0xA,
        (
            "#051F#4PRight on.\x02\x03",

            "This gives us the chance we need to find\x01",
            "that Ouroboros clown and bury 'er.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xE,
        (
            "#074F#4PHmm. My guess is that our suspect must be\x01",
            "concealing herself in the region's more\x01",
            "remote areas...\x02\x03",

            "#072FBut that gives us a huge amount of ground\x01",
            "to cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x101,
        (
            "#1007F#5PYeah. Rolent, as a region, isn't that big,\x01",
            "but just the seven of us can't search the\x01",
            "whole thing with a fine-toothed comb...\x02\x03",

            "#1015FI wonder if there's anything specific we\x01",
            "should do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x8,
        (
            "#740FWell. On that note...\x02\x03",

            "How about I press-gang you into helping\x01",
            "with the evacuation of civilians to the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x101,
        "#1004F#5PHuh? Evacuating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x8,
        (
            "#744FIt seems all but certain that the 'comas'\x01",
            "occur within the fog.\x02\x03",

            "#742FAnd now the fog's reach is growing...\x02\x03",

            "Like I said, we received word earlier that\x01",
            "it's reached the Malga Mine...and it's\x01",
            "also reached the Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        "#1020F#5PThe Perzel Farm too now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x103,
        (
            "#026F#5PI see.\x02\x03",

            "#020FSo we need to bring the Perzels and the\x01",
            "miners back into the city, where the army\x01",
            "unit can keep them safe, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x8,
        (
            "#740FYes. You can consider it a guild-assigned\x01",
            "mission--pay and all.\x02\x03",

            "Think you could do that before you go\x01",
            "looking for them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xA,
        (
            "#053F#4PKeepin' the civvies safe does take\x01",
            "priority, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xE,
        (
            "#070F#4PAs I remember, the mine is some distance\x01",
            "from the city, yes? And it sounds like\x01",
            "the same is true of this Perzel Farm.\x02\x03",

            "If that's the case, it would be wise to\x01",
            "split into two groups. We needn't take\x01",
            "all seven of us to one location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x103,
        (
            "#027F#5PAs much as I'm sure Will and Chere Perzel\x01",
            "would love to see a small army of bracers\x01",
            "show up at their door, I agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        (
            "#1015F#5PWell, um, speaking of which, can we go to\x01",
            "the farm, then?\x02\x03",

            "It's, um, run by the family of an old\x01",
            "friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xE,
        (
            "#073F#4PAh, I see.\x02\x03",

            "#070FAgate, Olivier and I will evacuate the mine,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xA,
        (
            "#051F#4PYeah, sounds like a plan.\x02\x03",

            "C'mon, let's go haul Blondie out of bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(2000)
    SetChrPos(0xB, 4250, 0, 108920, 0)

    NpcTalk(    #443
        0xB,
        "Man's Voice",
        (
            "#2PHmph! 'Haul' me out of bed?\x01",
            "What cruel summoning is this?\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 15)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_9A58():
        OP_6D(2550, 0, 112570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A58)

    def lambda_9A70():

        label("loc_9A70")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9A70")

    QueueWorkItem2(0x101, 1, lambda_9A70)
    Sleep(50)

    def lambda_9A86():

        label("loc_9A86")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9A86")

    QueueWorkItem2(0xA, 1, lambda_9A86)
    Sleep(50)

    def lambda_9A9C():

        label("loc_9A9C")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9A9C")

    QueueWorkItem2(0x103, 1, lambda_9A9C)
    Sleep(50)

    def lambda_9AB2():

        label("loc_9AB2")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9AB2")

    QueueWorkItem2(0xE, 1, lambda_9AB2)
    Sleep(50)

    def lambda_9AC8():

        label("loc_9AC8")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9AC8")

    QueueWorkItem2(0x107, 1, lambda_9AC8)
    Sleep(50)

    def lambda_9ADE():

        label("loc_9ADE")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9ADE")

    QueueWorkItem2(0x105, 1, lambda_9ADE)
    Sleep(100)
    WaitChrThread(0x101, 0x0)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    Sleep(500)

    def lambda_9B05():
        OP_6D(650, 0, 116600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9B05)
    WaitChrThread(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x105, 0x1)
    OP_8C(0x103, 180, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #444
        0xE,
        "#071F#4PAh, you're awake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        "#1007F#4PWhy are you strumming your lute?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xB,
        (
            "#031FAh, my rose, but the weather casts\x01",
            "a pall on men's hearts this day!\x02\x03",

            "I thought to perhaps brighten the mood\x01",
            "a little with a lovely serenade.\x02\x03",

            "Consider it a ray of sunshine, piercing\x01",
            "through the gloom, courtesy of Olivier\x01",
            "Lenheim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xA,
        "#551F#4PHow the hell can you be so cheery so early?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x101,
        (
            "#1006F#4PIt does sound like you were actually doing\x01",
            "your part out there, though.\x02\x03",

            "I'll admit, you can be a good guy when\x01",
            "you want to be, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x103,
        "#021F#2PIndeed! Well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xB,
        (
            "#031FHa-ha-ha! I merely did my duty as a\x01",
            "gentleman and defender of love.\x02\x03",

            "#030FTo be honest, I had thought about stopping\x01",
            "by Estelle's home while I was on patrol\x01",
            "for...a visit.\x02\x03",

            "#034FBut the fog was so thick I could barely\x01",
            "even find the city gate! It was a tragedy,\x01",
            "I tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        (
            "#1019F#4PSeriously? Just when I was reversing\x01",
            "my opinion of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x8,
        "#740FLet me get Olivier up to speed...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 116530, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -890, 0, 116590, 135)
    OP_8C(0x101, 0, 0)
    OP_8C(0x103, 0, 0)
    OP_8C(0x107, 0, 0)
    OP_8C(0x105, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #453
        0xB,
        (
            "#033F#6PA very bracer-like mission, hmm?\x02\x03",

            "#030FVery well. Allow me to help.\x02\x03",

            "#031FCome! Let us away to the farm\x01",
            "with the fair lady!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #454
        0xA,
        (
            "#555F#4PWe SAID you're comin' with US!\x02\x03",

            "The hell, are you gettin' it wrong on\x01",
            "purpose at this point?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #455
        0xB,
        (
            "#031F#6POooooh. I did not realize you wanted me\x01",
            "so badly, Agate.\x02\x03",

            "#037FWhy, if you keep being that forceful,\x01",
            "you'll scare me away, my lover. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xA,
        (
            "#055F#4POkay, hang on, I am NOT\x01",
            "your--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #457
        0x107,
        (
            "#065F#5PWha...? Whaaa...? 'L-Lover'?!\x01",
            "I didn't know you were...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x107, 400)

    ChrTalk(    #458
        0xA,
        (
            "#055F#4PTita! Don't listen to a word he says,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x101,
        (
            "#1007F#5PAnd, well, so much for any hope of\x01",
            "taking THIS job seriously...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x103,
        (
            "#021F#2PIt's better than being too serious.\x02\x03",

            "#027FAnyway, if we've fulfilled our tomfoolery\x01",
            "quotient for the day, we really should\x01",
            "get to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xA,
        "#551F#4PYeah, we should. Really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xE,
        "#070F#4PWe're off to the mine, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3B0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as didn't buy chocolates\x01",      # 0
            "Set as bought chocolates\x01",          # 1
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
        (0, "loc_A3A4"),
        (1, "loc_A3AA"),
        (SWITCH_DEFAULT, "loc_A3B0"),
    )


    label("loc_A3A4")

    OP_A3(0x181D)
    Jump("loc_A3B0")

    label("loc_A3AA")

    OP_A2(0x181D)
    Jump("loc_A3B0")

    label("loc_A3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A437")
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #463
        0xB,
        "#031F#6PFarewell for now, fair ladies.\x02",
    )

    CloseMessageWindow()

    def lambda_A3F6():

        label("loc_A3F6")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_A3F6")

    QueueWorkItem2(0x101, 1, lambda_A3F6)

    def lambda_A407():

        label("loc_A407")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_A407")

    QueueWorkItem2(0x103, 1, lambda_A407)

    def lambda_A418():

        label("loc_A418")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_A418")

    QueueWorkItem2(0x105, 1, lambda_A418)

    def lambda_A429():

        label("loc_A429")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_A429")

    QueueWorkItem2(0x107, 1, lambda_A429)
    Jump("loc_AAF0")

    label("loc_A437")


    ChrTalk(    #464
        0x107,
        "#064F#5PAh! Estelle, the gift!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0x101, 0x107, 400)

    def lambda_A47F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A47F)

    def lambda_A48D():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A48D)

    def lambda_A49B():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A49B)

    ChrTalk(    #465
        0x101,
        "#1006F#2POh, yeah, we did pick these up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xA,
        "#052F#4PThe what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xE,
        "#073F#4PWhat's this?\x02",
    )

    CloseMessageWindow()
    OP_8F(0x101, 0x2C6, 0x0, 0x1BF44, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #468
        "\x07\x05Estelle handed the package of chocolates to Tita.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x3F7, 3)

    ChrTalk(    #469
        0x101,
        (
            "#1001F#2PGo on, you. This was your idea,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x107,
        "#560F#5PO-Okay!\x02",
    )

    CloseMessageWindow()

    def lambda_A5D8():
        OP_8F(0xFE, 0xFFFFFEAC, 0x0, 0x1C05C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5D8)

    def lambda_A5F3():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5F3)
    Sleep(500)

    def lambda_A606():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A606)

    def lambda_A614():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A614)

    def lambda_A622():
        OP_8F(0xFE, 0x1D6, 0x0, 0x1C1C4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A622)
    WaitChrThread(0x101, 0x1)

    def lambda_A642():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A642)
    WaitChrThread(0x107, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #471
        0x107,
        (
            "#560F#6PAgate, Zin, Olivier?\x02\x03",

            "Thank you for all your hard work last night.\x02\x03",

            "#061FUm, um... This is for you!\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x107, 0x1D6, 0x0, 0x1C43A, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #472
        "\x07\x05Tita handed over the chocolates.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_A73F():
        OP_8F(0xFE, 0x1D6, 0x0, 0x1C2C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A73F)
    Sleep(500)

    ChrTalk(    #473
        0xA,
        "#055F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0xB,
        "#033F#6POh, my.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xE,
        "#073F#4POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x103,
        (
            "#021F#2PHeehee! Consider it a thank-you note from\x01",
            "those who enjoyed a full night's sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x105,
        "#048F#5PWe all chipped in a little on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x101,
        "#1006F#6PEnjoy them, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xE,
        (
            "#071F#4PExcellent. A bit of chocolate can be a\x01",
            "good pick-me-up for a last stretch of\x01",
            "road. Thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xB,
        (
            "#031F#6PAh, the taste of your love!\x01",
            "I shall treasure it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0xA,
        "#555F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x107,
        "#065F#6PA-Agate...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x105,
        "#043F#5PDo you not like chocolate, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xA,
        (
            "#552F#4PNah. It...ain't that.\x02\x03",

            "#551FIt's just... Gah, you guys do some\x01",
            "embarrassing stuff sometimes,\x01",
            "y'know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x101,
        "#1001F#6PHaha! He's embarrassed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x103,
        (
            "#027F#2PSomeone still needs a bit of\x01",
            "practice at being sociable, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xA,
        (
            "#055F#4PAw, shaddap.\x02\x03",

            "#051FAh, whatever. It'll be handy if we get\x01",
            "hungry on the road... Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x107,
        "#067F#6PYou're welcome!\x02",
    )

    CloseMessageWindow()

    def lambda_AAB2():

        label("loc_AAB2")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_AAB2")

    QueueWorkItem2(0x101, 1, lambda_AAB2)

    def lambda_AAC3():

        label("loc_AAC3")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_AAC3")

    QueueWorkItem2(0x103, 1, lambda_AAC3)

    def lambda_AAD4():

        label("loc_AAD4")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_AAD4")

    QueueWorkItem2(0x105, 1, lambda_AAD4)

    def lambda_AAE5():

        label("loc_AAE5")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_AAE5")

    QueueWorkItem2(0x107, 1, lambda_AAE5)

    label("loc_AAF0")


    def lambda_AAF6():
        OP_6D(2550, 0, 112570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AAF6)
    OP_43(0xE, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x1C)
    Sleep(700)
    OP_43(0xB, 0x1, 0x0, 0x1D)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_END)), "loc_AD7B")

    def lambda_AB53():
        OP_6D(-530, 0, 115950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AB53)
    Sleep(500)
    TurnDirection(0x101, 0x103, 400)

    def lambda_AB77():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AB77)
    Sleep(50)

    def lambda_AB8A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB8A)
    Sleep(50)

    def lambda_AB9D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AB9D)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #489
        0x101,
        (
            "#1006F#6PAnyway, we ought to get over to\x01",
            "the Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x105,
        "#041FAfter you, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x107,
        (
            "#560F#4PHey, Estelle? You said a friend of yours\x01",
            "lives there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x101,
        (
            "#1011F#6PUh-huh. She's an old, ooooold friend from\x01",
            "Sunday School named Tio Perzel.\x02\x03",

            "She lives out there with her parents and\x01",
            "her younger twin siblings, Will and Chere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x103,
        (
            "#026FWe WILL be escorting minors--er, not\x01",
            "counting Tita, since she's armed--so\x01",
            "we'll have to stay alert on this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFE3")

    label("loc_AD7B")


    def lambda_AD81():
        OP_6D(-530, 0, 115950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AD81)
    Sleep(500)
    TurnDirection(0x101, 0x105, 400)

    def lambda_ADA5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ADA5)
    Sleep(50)

    def lambda_ADB8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADB8)
    Sleep(50)

    def lambda_ADCB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_ADCB)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #494
        0x101,
        (
            "#1006F#6PRight, so we should get to the\x01",
            "Perzel Farm on the double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x105,
        "#041FAfter you, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x107,
        (
            "#560F#5PHey, Estelle? You said a friend of yours\x01",
            "lives there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x101,
        (
            "#1011F#7PUh-huh. She's an old, ooooold friend from Sunday\x01",
            "School named Tio Perzel.\x02\x03",

            "She lives out there with the rest of her family--\x01",
            "her grandfather Franz, her grandmother Hannah,\x01",
            "and her twin siblings, Will and Chere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x103,
        (
            "#026FWe WILL be escorting minors--er, not\x01",
            "counting Tita, since she's armed--so\x01",
            "we'll have to stay alert on this one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFE3")

    TurnDirection(0x103, 0x8, 400)

    def lambda_AFF0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AFF0)

    def lambda_AFFE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFFE)

    def lambda_B00C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B00C)

    ChrTalk(    #499
        0x103,
        "#020F#5PWell, we're off, Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x8,
        "#741F#4PGood luck out there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x181E)
    OP_28(0x91, 0x4, 0x2)
    OP_28(0x91, 0x4, 0x8)
    OP_28(0x91, 0x1, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_21_879F end

    def Function_22_B074(): pass

    label("Function_22_B074")

    OP_8E(0xFE, 0x2C6, 0x0, 0x1C138, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_B074 end

    def Function_23_B090(): pass

    label("Function_23_B090")

    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1C138, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_B090 end

    def Function_24_B0C0(): pass

    label("Function_24_B0C0")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1BC88, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_24_B0C0 end

    def Function_25_B0DC(): pass

    label("Function_25_B0DC")

    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1BC88, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_25_B0DC end

    def Function_26_B111(): pass

    label("Function_26_B111")


    def lambda_B117():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B117)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x636, 0x0, 0x1B738, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_26_B111 end

    def Function_27_B158(): pass

    label("Function_27_B158")

    OP_8E(0xFE, 0xA8C, 0x0, 0x1C6E2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA3C, 0x0, 0x1B45E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_B19A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B19A)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_B158 end

    def Function_28_B1C0(): pass

    label("Function_28_B1C0")

    OP_8E(0xFE, 0xA8C, 0x0, 0x1C6E2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA3C, 0x0, 0x1B45E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_B202():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B202)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_B1C0 end

    def Function_29_B228(): pass

    label("Function_29_B228")

    OP_8E(0xFE, 0xFFFFFC36, 0x0, 0x1BE0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_B26A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B26A)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_B228 end

    def Function_30_B290(): pass

    label("Function_30_B290")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_20(0x1F4)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 4410, 0, 109480, 0)
    SetChrPos(0x107, 4410, 0, 109480, 0)
    SetChrPos(0x103, 4410, 0, 109480, 0)
    SetChrPos(0x105, 4410, 0, 109480, 0)
    SetChrPos(0xB, -700, 0, 116590, 45)
    SetChrPos(0xA, 500, 0, 116600, 0)
    SetChrPos(0xE, 1800, 0, 116590, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B3CC():

        label("loc_B3CC")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_B3CC")

    QueueWorkItem2(0xA, 1, lambda_B3CC)

    def lambda_B3DD():

        label("loc_B3DD")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_B3DD")

    QueueWorkItem2(0xE, 1, lambda_B3DD)

    def lambda_B3EE():

        label("loc_B3EE")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_B3EE")

    QueueWorkItem2(0xB, 1, lambda_B3EE)

    def lambda_B3FF():
        OP_6D(-150, 0, 116560, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B3FF)
    OP_43(0x101, 0x1, 0x0, 0x1F)
    OP_43(0x103, 0x1, 0x0, 0x20)
    OP_43(0x107, 0x1, 0x0, 0x21)
    OP_43(0x105, 0x1, 0x0, 0x22)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xB, 0x1)

    ChrTalk(    #501
        0xA,
        "#051F#4PHey, finally back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xE,
        (
            "#073F#4PHow did it go? I did not think\x01",
            "it would take that long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x103,
        "#025F#5PIt went...well. A lot happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x101,
        (
            "#1015F#5PAgate, have you guys already been to\x01",
            "the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xA,
        (
            "#051F#4POh, yeah. That was a milk run.\x01",
            "They were contacted ahead of time.\x02\x03",

            "They were ready to move pretty much\x01",
            "the instant we arrived. We got back\x01",
            "real quick too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xE,
        (
            "#074F#4PWe were, however, attacked by bizarre\x01",
            "monsters on the way back.\x02\x03",

            "We were just discussing them with Aina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0x101,
        "#1004F#5PWeird monsters?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x21)
    Sleep(400)

    ChrTalk(    #508
        0xB,
        (
            "#032F#6PYes, things which appeared from the fog...\x01",
            "and melted back into it upon defeat.\x02\x03",

            "'Fog beasts,' one could say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x101,
        "#1020F#5PThat's like-!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x105,
        "#042F#5PJust the same as the ones we fought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xA,
        (
            "#052F#4PThey showed up at the farm, too?\x01",
            "Figures...\x02\x03",

            "You guys get hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x107,
        "#063F#5PWell, um...we're okay, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        "#1003F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0xA,
        "#555F#4P...That look can't mean anything good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0x8,
        (
            "#742FIt sounds like something happened.\x01",
            "Can you give us a report?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x103,
        "#022F#5POf course.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #517
        "\x07\x05Scherazard explained what transpired at the farm.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #518
        0x8,
        "#745FI see... Damn, just a moment too late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x103,
        (
            "#522F#5PThe fault lies with me.\x02\x03",

            "If we'd gotten there a bit faster,\x01",
            "we'd have apprehended the suspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x101,
        (
            "#1003F#5PNo... It's my fault, really, Schera.\x02\x03",

            "I'm the one who wasn't able to get it\x01",
            "together fast enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x8,
        (
            "#742FI don't think anyone's to blame, really.\x02\x03",

            "From the sound of things, it seems like\x01",
            "you were lured into a trap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x101,
        "#1004F#5PA trap?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xE,
        (
            "#074F#4PYes, think about it. You heard the sound\x01",
            "of a bell the moment you stepped onto\x01",
            "the farm.\x02\x03",

            "The fog beasts were waiting for you,\x01",
            "and the front door was locked.\x02\x03",

            "#072FIt sounds as though it was set up so that\x01",
            "you couldn't make it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x101,
        (
            "#1020F#5PWait, you think it was DELIBERATE?\x01",
            "Like, finding Tio and everything?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xB,
        (
            "#032F#6PQuite. In fact, when combined with the\x01",
            "coma cases we know of so far, I'd say\x01",
            "our 'woman in black' is very clever.\x02\x03",

            "She specifically moved ahead of you to put\x01",
            "people you knew and wanted to protect to\x01",
            "sleep.\x02\x03",

            "#035FHeh... It seems we really are being\x01",
            "taunted now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0x101,
        (
            "#1015F#5PI guess...\x02\x03",

            "It's so weird, though. I have no idea who\x01",
            "this woman could be!\x02\x03",

            "And, I mean, I'm upset and kinda scared,\x01",
            "but she hasn't really 'taunted' us the\x01",
            "same way the others did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x103,
        "#522F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 4250, 0, 108920, 0)
    ClearChrFlags(0x11, 0x80)
    OP_4A(0x11, 255)

    NpcTalk(    #528
        0x11,
        "Man's Voice",
        "#2PYo, I'm back!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BE83():
        OP_6D(2550, 0, 112570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE83)
    Sleep(50)

    def lambda_BEA0():

        label("loc_BEA0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BEA0")

    QueueWorkItem2(0x101, 1, lambda_BEA0)
    Sleep(50)

    def lambda_BEB6():

        label("loc_BEB6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BEB6")

    QueueWorkItem2(0x103, 1, lambda_BEB6)
    Sleep(50)

    def lambda_BECC():

        label("loc_BECC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BECC")

    QueueWorkItem2(0x105, 1, lambda_BECC)
    Sleep(50)

    def lambda_BEE2():

        label("loc_BEE2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BEE2")

    QueueWorkItem2(0x107, 1, lambda_BEE2)
    Sleep(50)

    def lambda_BEF8():

        label("loc_BEF8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BEF8")

    QueueWorkItem2(0xA, 1, lambda_BEF8)
    Sleep(50)

    def lambda_BF0E():

        label("loc_BF0E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BF0E")

    QueueWorkItem2(0xB, 1, lambda_BF0E)
    Sleep(50)

    def lambda_BF24():

        label("loc_BF24")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_BF24")

    QueueWorkItem2(0xE, 1, lambda_BF24)
    WaitChrThread(0x101, 0x0)
    OP_43(0x11, 0x1, 0x0, 0x23)
    Sleep(500)

    def lambda_BF46():
        OP_6D(650, 0, 116600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BF46)
    WaitChrThread(0x11, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #529
        0x101,
        "#1004F#4PHuh? Ridge?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #530
        0x103,
        (
            "#020F#2POh, Ridge. You were escorting that\x01",
            "group to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x11,
        (
            "#5PYeah, I left Grancel this morning and just\x01",
            "got back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x11,
        "#5PBut, man, what the heck's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x11,
        (
            "#5PThe fog's getting thicker, and now there're\x01",
            "soldiers patrolling the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0x8,
        "#742FQuite a bit has happened since last night...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #535
        "\x07\x05Aina and the team explained events to Ridge.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #536
        0x11,
        "#5PWhoa. Sounds like I missed a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0x11,
        (
            "#5PGuess I picked a bad time to take\x01",
            "a hike. Sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0x101,
        (
            "#1006F#4PIt's okay. With the passenger ships stopped,\x01",
            "we gotta keep travelers safe, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #539
        0x103,
        (
            "#027F#2PAnd we hardly have time to take those\x01",
            "kinds of jobs ourselves.\x02\x03",

            "Thank you for your help on that front,\x01",
            "Ridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0x11,
        "#5PUh, yeah, no problem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0x11,
        (
            "#5PThough... Hey. Back up a step.\x01",
            "You said something about the sound\x01",
            "of a bell, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0x11,
        (
            "#5PThat's like something you heard\x01",
            "from the fog, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x103,
        "#025F#2PYes, that's about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x101,
        (
            "#1007F#4PWe don't know why it's being rung,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x11,
        "#5PHuh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #546
        0x103,
        (
            "#023F#2PRidge? It looks like this, uh, rings a bell,\x01",
            "if you'll forgive the expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0x11,
        (
            "#5PKinda. Thing is, I was comin' up the\x01",
            "Elize Highway just now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0x11,
        (
            "#5PI could've sworn I heard the sound of a bell\x01",
            "as I was passin' along.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #549
        0x101,
        "#1005F#4PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x103,
        (
            "#024F#2PRidge, where EXACTLY did you hear it?!\x01",
            "This could be vital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0x11,
        "#5PEr, whoa! Give me a sec...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0x11,
        (
            "#5PI think it was...just after I left the\x01",
            "Gurune Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0x11,
        "#5PSo it must've come from inside Mistwald.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0x103,
        "#022F#2PMistwald...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0xE,
        (
            "#072F#4PThat's the forest to the southeast\x01",
            "of the city, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x11,
        (
            "#5PAt first I thought there might be someone\x01",
            "there, so I called out in the direction\x01",
            "of the sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x11,
        (
            "#5PI didn't get any answer, though, so I figured\x01",
            "I must've imagined it...until you mentioned\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0xB,
        (
            "#032F#7PHmmmm.\x02\x03",

            "I wonder if it was rung intentionally,\x01",
            "knowing this report would reach us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x105,
        "#042F#5PIn other words...a taunt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0xA,
        "#057F#4PTch. Sons of...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x101,
        "#1002F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #562
        0x101,
        "#1002F#6PSchera...what do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #563
        0x103,
        "#026F#2PHmm.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #564
        0x103,
        (
            "#022F#2PThis is so obviously a trap they may as\x01",
            "well hang a sign on it, but we've got no\x01",
            "choice but to leap into it anyway.\x02\x03",

            "This is a taunt we'll have to answer.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #565
        (
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_6D(17370, 0, 123310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 255)
    OP_A2(0x1823)
    OP_28(0x92, 0x4, 0x2)
    OP_28(0x92, 0x4, 0x8)
    OP_28(0x92, 0x1, 0x1)
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    OP_6D(1370, 0, 113410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1370, 0, 113410, 180)
    SetChrPos(0x1, 1370, 0, 113410, 180)
    SetChrPos(0x2, 1370, 0, 113410, 180)
    SetChrPos(0x3, 1370, 0, 113410, 180)
    OP_69(0x0, 0x0)
    OP_1D(0xA)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_B290 end

    def Function_31_CAE4(): pass

    label("Function_31_CAE4")

    OP_8E(0xFE, 0x2C6, 0x0, 0x1C138, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_31_CAE4 end

    def Function_32_CB00(): pass

    label("Function_32_CB00")

    Sleep(500)
    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1C138, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_32_CB00 end

    def Function_33_CB35(): pass

    label("Function_33_CB35")

    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0x2E4, 0x0, 0x1BC88, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_33_CB35 end

    def Function_34_CB5B(): pass

    label("Function_34_CB5B")

    Sleep(500)
    Sleep(500)
    Sleep(500)

    def lambda_CB70():
        OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_CB70)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x105, 0x3)
    OP_8E(0xFE, 0x730, 0x0, 0x1BC88, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_CB5B end

    def Function_35_CBB0(): pass

    label("Function_35_CBB0")


    def lambda_CBB6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CBB6)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x636, 0x0, 0x1B738, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_35_CBB0 end

    def Function_36_CBF2(): pass

    label("Function_36_CBF2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC12")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_CC12")

    Call(0, 37)
    OP_4A(0x8, 255)
    OP_6D(400, 0, 117350, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 610, 0, 116590, 0)
    SetChrPos(0x103, 1630, 0, 116600, 0)
    SetChrPos(0x107, 1490, 0, 115380, 0)
    SetChrPos(0x105, -10, 0, 115840, 0)
    SetChrPos(0x108, 980, 0, 114460, 0)
    SetChrPos(0x104, 2630, 0, 114990, 0)
    SetChrPos(0x106, -240, 0, 114330, 0)
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #566
        0x8,
        "#744FI see... What a mess this was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #567
        0x103,
        (
            "#522F#3PI'm sorry, Aina.\x02\x03",

            "I should've spoken to everyone\x01",
            "about my suspicions sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x8,
        (
            "#740FIt's not a problem, Schera.\x02\x03",

            "Even if we had known it was an acquaintance\x01",
            "of yours, it sounds like it wouldn't have helped\x01",
            "much.\x02\x03",

            "#741FJust pay for my drinks next time\x01",
            "and we'll call it even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x103,
        "#021F#3PYou got it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #570
        0x101,
        (
            "#1016F#6PUm, given the way you two drink, I'm not\x01",
            "sure that's the best promise to make,\x01",
            "Schera...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x104, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #571
        0x104,
        "#034F*shudder*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0x8,
        (
            "#740FThe fog has cleared and everyone who\x01",
            "was asleep has awoken.\x02\x03",

            "#741FGreat work, everyone.\x02\x03",

            "You actually cleared several full jobs on\x01",
            "this one, so let me pay them all out\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x90, 0x4, 0x10)
    OP_AF(0x3, 0x90)
    Sleep(100)
    OP_28(0x91, 0x4, 0x10)
    OP_AF(0x3, 0x91)
    Sleep(100)
    OP_28(0x92, 0x4, 0x10)
    OP_AF(0x3, 0x92)
    Sleep(100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #573
        0x101,
        (
            "#1007F#6PI dunno. It still feels like we didn't\x01",
            "manage a real solution to this one,\x01",
            "either.\x02\x03",

            "And now the Gospel can mess with people's\x01",
            "minds, too!\x02\x03",

            "#1015FThat's, like, pure orbal fiction as far\x01",
            "as most people are concerned, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0x107,
        (
            "#063F#5PY-Yeah... That one's the hardest to\x01",
            "explain so far!\x02\x03",

            "I think I need to call Grandpa or\x01",
            "send him a letter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #575
        0x106,
        (
            "#053FWell, either way, all we can do is wait\x01",
            "for Gramps to finish picking apart the\x01",
            "Gospel he's got on hand.\x02\x03",

            "#050FMore to the point, I think the society's\x01",
            "really starting to tip their hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #576
        0x108,
        (
            "#074FAdding in this event...\x02\x03",

            "#072F...we know of five 'Enforcers' in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0x8,
        "#744FYes...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x6E)
    Sleep(500)
    OP_AD(0x240089, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Aina")

    AnonymousTalk(    #578
        "\x07\x00#742FEnforcer No. X, Bleublanc the Phantom Thief.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #579
        "#742FEnforcer No. VIII, Walter the Direwolf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x2400D5, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #580
        "#742FEnforcer No. XV, Renne the Angel of Slaughter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008C, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #581
        "#742FEnforcer No. VI, Luciola the Bewitching Bell.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008D, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #582
        "#742FAnd Enforcer No. 0, Campanella the Fool.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008E, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("Aina")

    AnonymousTalk(    #583
        (
            "#744FAnd in addition to those five, we have also heard two names\x01",
            "repeatedly: The 'professor' and 'Loewe.'\x02\x03",

            "#742FIt seems likely one of those two is the man we know as\x01",
            "'Lieutenant Lorence.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x101)

    AnonymousTalk(    #584
        (
            "#1003FYeah, that seems right.\x02\x03",

            "And Luciola said I know both of them...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x105)

    AnonymousTalk(    #585
        (
            "#043FIt's very possible 'Lorence Belgar' was\x01",
            "a false or even stolen identity.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    OP_0D()

    ChrTalk(    #586
        0x106,
        (
            "#555FWhat gets me is that this whole mess is\x01",
            "supposed to be the work of seven people.\x02\x03",

            "That's just the craziest damn thing I've\x01",
            "ever heard. Seven people did all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0x103,
        (
            "#026F#6PIt does seem incredible, but I'm perfectly\x01",
            "willing to believe it.\x02\x03",

            "#022FWe'll need to be prepared for anything,\x01",
            "even more so than before.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #588
        0x101,
        (
            "#1026F#6PUm, Schera... Are you sure you want...?\x01",
            "I mean...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #589
        0x103,
        (
            "#524F#4PHoney, didn't you hear me earlier?\x01",
            "Liberl is my home.\x02\x03",

            "You don't need a special reason to\x01",
            "protect your homeland.\x02\x03",

            "Even if that means fighting a memory\x01",
            "from your old home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #590
        0x101,
        "#1026F#6PSchera...\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x108)
    Sleep(500)

    ChrTalk(    #591
        0x108,
        (
            "#070FWell, keep in mind, Scherazard...\x02\x03",

            "It doesn't have to end that way\x01",
            "for you, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x103, 0x108, 400)

    ChrTalk(    #592
        0x103,
        "#023F#2PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0x108,
        (
            "#074FWalter and I accepted a long time ago\x01",
            "that it has to end in battle between us.\x02\x03",

            "The only way we have to say anything to\x01",
            "each other is with our fists.\x02\x03",

            "#070FBut that's not necessarily true for you\x01",
            "and 'Miss Luci,' you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0x103,
        "#522F#2PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0x101,
        (
            "#1006F#6PI think Zin has a point.\x02\x03",

            "Schera, you've still got a lot of time\x01",
            "to figure out what you want to do.\x02\x03",

            "And I think I know what I want to do,\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #596
        0x103,
        "#023F#2PWhat?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #597
        0x101,
        (
            "#1011F#4PHey...everyone?\x02\x03",

            "I realize it's kind of late,\x01",
            "but there's something I need\x01",
            "to show you all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB3E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DB3E)
    Sleep(100)
    TurnDirection(0xF9, 0x101, 400)

    ChrTalk(    #598
        0x106,
        "#052FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #599
        0x105,
        "#044F#6PEstelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #600
        0x103,
        "#023F#2PWait, Estelle, are you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #601
        0x101,
        (
            "#1012F#4PYeah... It's time.\x02\x03",

            "#1025FEveryone. I got this photo from\x01",
            "Nial and Dorothy a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Fade(250)
    SetChrChipByIndex(0x101, 17)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #602
        "\x07\x05Estelle passed the photo around to everyone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x106)

    AnonymousTalk(    #603
        (
            "\x07\x00#555FThis is...what, that thing where the\x01",
            "bandit ship got retaken?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x104)

    AnonymousTalk(    #604
        (
            "#033FAhh, I...see.\x01",
            "So that is how it played out, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 280, -1, -1)
    OP_61(0x108)

    AnonymousTalk(    #605
        (
            "#073FWell, I recognize the girl on\x01",
            "the left. She's one of the Capuas\x01",
            "from the tournament.\x02\x03",

            "And on the...right...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x105)

    AnonymousTalk(    #606
        "#043F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x107)

    AnonymousTalk(    #607
        "#065F#6PJOSHUA?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x3E8)
    OP_21()
    OP_AE(0xC8)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #608
        0x101,
        (
            "#1007F#4PUm... I'm sorry I kept quiet about this\x01",
            "until now.\x02\x03",

            "#1003FIt was kind of a shock, so I just couldn't\x01",
            "come out and say it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #609
        0x107,
        "#063F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0x105,
        "#043F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #611
        0x101,
        (
            "#1002F#4PI don't know what Joshua thinks he's doing,\x01",
            "but...I think he's trying, in his own way,\x01",
            "to fight the society.\x02\x03",

            "I don't think he joined the Capuas to do\x01",
            "bad things. But he still, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #612
        0x8,
        (
            "#744FWe understand, Estelle.\x02\x03",

            "#740FBesides, his lower face is covered in this\x01",
            "photo...so I certainly can't say for\x01",
            "sure this is Joshua Bright. No, sir.\x02\x03",

            "We'll keep this internal to the guild for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #613
        0x101,
        "#1017F#6PThanks, Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #614
        0x105,
        (
            "#043F#6PBut, Estelle, are you sure?\x02\x03",

            "You've finally found a clue about Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #615
        0x101,
        (
            "#1012F#4PYeah... I'm sure.\x02\x03",

            "#1006FMy connection to Joshua isn't\x01",
            "going anywhere. Not so long as\x01",
            "I remain myself, you know?\x02\x03",

            "Now that I think of it that way,\x01",
            "I'm not going crazy over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #616
        0x105,
        "#044F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #617
        0x101,
        (
            "#1006F#4PWe're walking down different paths,\x01",
            "but I know our destination's the same.\x02\x03",

            "#1012FSo I'm going to keep going my\x01",
            "own way for now.\x02\x03",

            "If I don't, I'll never become the kind of\x01",
            "person I NEED to become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #618
        0x105,
        "#542F#6PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #619
        0x101,
        (
            "#1008F#4PHeheh... Well, despite trying to act cool...\x02\x03",

            "I gotta admit, I really want to know just\x01",
            "what's going on between Joshua and\x01",
            "Miss Tomboy there.\x02\x03",

            "#1007FI've still got a long way to go, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #620
        0x105,
        "#045F#6PHaha. Oh, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #621
        0x103,
        (
            "#021F#2PLooks like you've really made up\x01",
            "your mind.\x02\x03",

            "#027FYour dream in the forest must've been\x01",
            "something else, hmmm?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #622
        0x101,
        (
            "#1017F#6PYeah.\x02\x03",

            "I was given a chance to remember my\x01",
            "bond with Joshua...\x02\x03",

            "And I remembered my mother's warmth.\x02\x03",

            "#1001FI guess I can actually be thankful to\x01",
            "the Gospel this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0x107,
        "#061F#5PHeehee! I guess so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #624
        0x106,
        (
            "#051FIt'd take a train to stop you\x01",
            "at this point, I swear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0x104,
        (
            "#031FAh, even Gospels cannot stand before\x01",
            "our Estelle. Inspiring!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 38)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E588")
    OP_A2(0x183C)

    label("loc_E588")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E599")
    OP_A2(0x183D)

    label("loc_E599")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5AA")
    OP_A2(0x183E)

    label("loc_E5AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5BB")
    OP_A2(0x183F)

    label("loc_E5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5CC")
    OP_A2(0x1840)

    label("loc_E5CC")

    OP_AD(0x2400B1, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1843)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x126), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0x11, 0x0, 0x0, 0x0)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E647")
    ShowSaveMenu()

    label("loc_E647")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A3(0x1843)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_36_CBF2 end

    def Function_37_E67D(): pass

    label("Function_37_E67D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E6B6")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E6EF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6D7")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_E6DB")

    label("loc_E6D7")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_E6DB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E73C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E710")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_E728")

    label("loc_E710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E724")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_E728")

    label("loc_E724")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_E728")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E789")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E75D")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_E775")

    label("loc_E75D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E771")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_E775")

    label("loc_E771")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_E775")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E789")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E7AE")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E7AE")

    Return()

    # Function_37_E67D end

    def Function_38_E7AF(): pass

    label("Function_38_E7AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E7BF")
    RemoveParty(0x7, 0xFF)

    label("loc_E7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E7CF")
    RemoveParty(0x4, 0xFF)

    label("loc_E7CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E7DF")
    RemoveParty(0x6, 0xFF)

    label("loc_E7DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E7EF")
    RemoveParty(0x3, 0xFF)

    label("loc_E7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E7FF")
    RemoveParty(0x5, 0xFF)

    label("loc_E7FF")

    Return()

    # Function_38_E7AF end

    def Function_39_E800(): pass

    label("Function_39_E800")

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
        (0, "loc_E87C"),
        (1, "loc_E882"),
        (SWITCH_DEFAULT, "loc_E888"),
    )


    label("loc_E87C")

    OP_A2(0x1200)
    Jump("loc_E888")

    label("loc_E882")

    OP_A2(0x1201)
    Jump("loc_E888")

    label("loc_E888")

    Return()

    # Function_39_E800 end

    def Function_40_E889(): pass

    label("Function_40_E889")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_40_E889 end

    SaveToFile()

Try(main)
