from ED6ScenarioHelper import *

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
        'Kilika',                               # 9
        'Professor Alba',                       # 10
        'Dorothy',                              # 11
        'Factory Chief Murdock',                # 12
        'Stain',                                # 13
        'Elwyn',                                # 14
        'Ada',                                  # 15
        'Knowles',                              # 16
        'Didi',                                 # 17
        'Elkan',                                # 18
        'Gundolf',                              # 19
        'Wong',                                 # 20
        'Bruno',                                # 21
        'Monika',                               # 22
        'Karl',                                 # 23
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
        'ED6_DT07/CH02050 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT07/CH02620 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01750 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
        'ED6_DT07/CH01530 ._CH',             # 0C
        'ED6_DT07/CH02490 ._CH',             # 0D
        'ED6_DT07/CH01190 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02050P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT07/CH02620P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01750P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
        'ED6_DT07/CH01530P._CP',             # 0C
        'ED6_DT07/CH02490P._CP',             # 0D
        'ED6_DT07/CH01190P._CP',             # 0E
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
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 9,
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
        TalkFunctionIndex   = 18,
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
        TalkFunctionIndex   = 19,
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
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_952",          # 01, 1
        "Function_2_974",          # 02, 2
        "Function_3_98A",          # 03, 3
        "Function_4_9AE",          # 04, 4
        "Function_5_B1C",          # 05, 5
        "Function_6_B90",          # 06, 6
        "Function_7_C11",          # 07, 7
        "Function_8_CD4",          # 08, 8
        "Function_9_D21",          # 09, 9
        "Function_10_21E7",        # 0A, 10
        "Function_11_2369",        # 0B, 11
        "Function_12_2E6A",        # 0C, 12
        "Function_13_37E8",        # 0D, 13
        "Function_14_3A14",        # 0E, 14
        "Function_15_3D88",        # 0F, 15
        "Function_16_4B42",        # 10, 16
        "Function_17_56B9",        # 11, 17
        "Function_18_62EA",        # 12, 18
        "Function_19_6306",        # 13, 19
        "Function_20_630B",        # 14, 20
        "Function_21_6EDD",        # 15, 21
        "Function_22_7FCE",        # 16, 22
        "Function_23_9743",        # 17, 23
        "Function_24_BB38",        # 18, 24
        "Function_25_D399",        # 19, 25
        "Function_26_E533",        # 1A, 26
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3A0")
    OP_A3(0x3FA)
    Event(0, 23)

    label("loc_3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_3B1")
    SoundLoad(131)
    OP_A3(0x3FB)
    Event(0, 25)

    label("loc_3B1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3BD"),
        (SWITCH_DEFAULT, "loc_412"),
    )


    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC")
    OP_A2(0x50C)
    Event(0, 20)

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF")
    OP_A2(0x538)
    Event(0, 21)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7")
    SetMapFlags(0x10000000)
    OP_A2(0x55A)
    Event(0, 22)

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40F")
    SetMapFlags(0x10000000)
    OP_A2(0x560)
    Event(0, 24)

    label("loc_40F")

    Jump("loc_412")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)
    Jump("loc_951")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_51F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1150, 1000, 50950, 91)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 22260, 0, 2140, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 51500, 4000, 3030, 274)
    Jump("loc_951")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5A5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_5A2")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3790, 0, -2310, 278)
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_5A2")

    Jump("loc_951")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_61D")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 52110, 0, 50520, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 59030, 0, 54500, 355)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_69A")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1780, 1000, 53000, 183)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -710, 1000, 50990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2940, 1000, 53000, 269)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4070, 0, -700, 0)
    Jump("loc_951")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6E6")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1780, 1000, 53000, 183)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 54570, 0, 540, 351)
    Jump("loc_951")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_732")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -970, 1000, 51000, 352)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_799")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 61100, 2000, 2280, 11)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 3500, 0, 47710, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    Jump("loc_951")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_856")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 61100, 2000, 2280, 11)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 25360, 0, -2660, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 27160, 0, -2710, 284)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)

    label("loc_853")

    Jump("loc_951")

    label("loc_856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_8D5")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)
    Jump("loc_951")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_951")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 52200, 0, 53610, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1780, 1000, 53000, 183)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55570, 0, 51740, 63)
    OP_43(0x10, 0x0, 0x0, 0x3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 52970, 0, 2400, 172)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 54960, 4000, 2770, 11)

    label("loc_951")

    Return()

    # Function_0_392 end

    def Function_1_952(): pass

    label("Function_1_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96A")
    OP_B1("t3120_y")
    Jump("loc_973")

    label("loc_96A")

    OP_B1("t3120_n")

    label("loc_973")

    Return()

    # Function_1_952 end

    def Function_2_974(): pass

    label("Function_2_974")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_974")

    label("loc_989")

    Return()

    # Function_2_974 end

    def Function_3_98A(): pass

    label("Function_3_98A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AD")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_98A")

    label("loc_9AD")

    Return()

    # Function_3_98A end

    def Function_4_9AE(): pass

    label("Function_4_9AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(    #0
        0xFE,
        "It sure is noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Are the kids skipping Sunday\x01",
            "School again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_A11")

    OP_A2(0xB)

    ChrTalk(    #2
        0xFE,
        (
            "This orbal gun is able to maximize the\x01",
            "energy output of its control orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It's a little off-balance and needs\x01",
            "a little more polish, but still, it's\x01",
            "up to spec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "We're progressing nicely.\x01",
            "We'll have a production unit\x01",
            "on the shelves in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B18")

    TalkEnd(0xFE)
    Return()

    # Function_4_9AE end

    def Function_5_B1C(): pass

    label("Function_5_B1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(    #5
        0xA,
        (
            "#150FEstelle! Let me know if you\x01",
            "find out anything, okay?\x02\x03",

            "This has 'SCOOP' written all\x01",
            "over it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8C")

    TalkEnd(0xFE)
    Return()

    # Function_5_B1C end

    def Function_6_B90(): pass

    label("Function_6_B90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_C0D")

    ChrTalk(    #6
        0xFE,
        "Product Descriptions...ugh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Rate of fire...accuracy index...\x01",
            "projected run time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "It's all so dry!\x02",
    )

    CloseMessageWindow()

    label("loc_C0D")

    TalkEnd(0xFE)
    Return()

    # Function_6_B90 end

    def Function_7_C11(): pass

    label("Function_7_C11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_C74")

    ChrTalk(    #9
        0xFE,
        "What was it? Zhon? No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Vahn? Was that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "No, that's not right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD0")

    label("loc_C74")

    OP_A2(0x9)

    ChrTalk(    #12
        0xFE,
        (
            "You know the guy I hired as my\x01",
            "last bodyguard, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "What was his name again?\x02",
    )

    CloseMessageWindow()

    label("loc_CD0")

    TalkEnd(0xFE)
    Return()

    # Function_7_C11 end

    def Function_8_CD4(): pass

    label("Function_8_CD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_D1D")

    ChrTalk(    #14
        0x9,
        (
            "#130FThis looks like quite a mess.\x02\x03",

            "Do try to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1D")

    TalkEnd(0xFE)
    Return()

    # Function_8_CD4 end

    def Function_9_D21(): pass

    label("Function_9_D21")

    TalkBegin(0x8)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8C")
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x40)"), scpexpr(EXPR_END)), "loc_E11")
    Sleep(200)

    ChrTalk(    #15
        0x8,
        (
            "#790FWelcome back. It looks like\x01",
            "you've finished your job.\x02\x03",

            "If you clear any other contracts,\x01",
            "make sure you come here and\x01",
            "report it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E83")

    label("loc_E11")

    Sleep(200)

    ChrTalk(    #16
        0x8,
        (
            "#790FNothing to report today?\x02\x03",

            "If you clear any other contracts,\x01",
            "make sure you come here and\x01",
            "report it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E83")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_E8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9D")
    TalkEnd(0x8)
    Return()

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_10D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 3)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #17
        0x8,
        (
            "#790FI think it might be best if you\x01",
            "left as soon as possible.\x02\x03",

            "Goddess watch over you.\x01",
            "Be careful out there, you two.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D6")

    label("loc_F2A")

    OP_A2(0x57B)

    ChrTalk(    #18
        0x8,
        (
            "#790FDid you finish all the \x01",
            "boarding paperwork?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#505FYeah, about that...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Estelle explained about the Royal Army\x01",
            "inspection and canceling the airship ticket.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #21
        0x8,
        (
            "#792FI...see.\x02\x03",

            "#790FThey're moving faster than\x01",
            "I thought.\x02\x03",

            "I think it might be best if you\x01",
            "left as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#010FThat was our plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#000FBye, Kilika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#790FGoddess watch over you.\x01",
            "Be careful out there, you two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D6")

    Jump("loc_21E3")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1177")

    ChrTalk(    #25
        0x8,
        (
            "#790FThe airship to the capital leaves\x01",
            "at eleven o'clock.\x02\x03",

            "You should get to the platform\x01",
            "and square away any paperwork\x01",
            "as quickly as you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(    #26
        0x8,
        (
            "#790FTake that machine Tita told you\x01",
            "about, as well.\x02\x03",

            "I'll collect all the data about\x01",
            "the base that I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1292")

    label("loc_11F9")


    ChrTalk(    #27
        0x8,
        (
            "#790FThe factory ship should be just\x01",
            "about ready.\x02\x03",

            "Head to the platform as soon\x01",
            "as you're ready.\x02\x03",

            "May the Goddess Aidios watch\x01",
            "over you. Stay safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1292")

    Jump("loc_21E3")

    label("loc_1295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1348")

    ChrTalk(    #28
        0x8,
        (
            "#790FThe road to Leiston Fortress starts\x01",
            "from the east exit.\x02\x03",

            "The road splits into three at one\x01",
            "point. When it does, take the\x01",
            "north road.\x02\x03",

            "And keep your eyes open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1390")

    ChrTalk(    #29
        0x8,
        (
            "#790FI'll contact the Royal Army.\x02\x03",

            "All right, go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1406")

    label("loc_1390")

    OP_A2(0x0)

    ChrTalk(    #30
        0x8,
        (
            "#790FIf there's any news, I'll have\x01",
            "Wong get in contact with you.\x02\x03",

            "You need to get to the Carnelia\x01",
            "Tower now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1406")

    Jump("loc_21E3")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1493")

    ChrTalk(    #31
        0x8,
        (
            "#790FThe two of you get yourselves\x01",
            "to the central factory now.\x02\x03",

            "Assess the situation and take\x01",
            "any necessary action.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1656")

    label("loc_1493")

    OP_A2(0x0)

    ChrTalk(    #32
        0x8,
        (
            "#790FPerfect. You two showed up\x01",
            "just in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#004FWhat's the matter, Kilika?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#014FWe've heard there's some kind of\x01",
            "situation at the central factory...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#792FWe haven't received a full report on\x01",
            "the situation there yet ourselves.\x02\x03",

            "All of our bracers are currently\x01",
            "in the field.\x02\x03",

            "I need the two of you to get to\x01",
            "the central factory now.\x02\x03",

            "Assess the situation and take\x01",
            "any necessary action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#006FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        "#012FUnderstood.\x02",
    )

    CloseMessageWindow()

    label("loc_1656")

    Jump("loc_21E3")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 2)), scpexpr(EXPR_END)), "loc_16E3")

    ChrTalk(    #38
        0x8,
        (
            "#790FThis is an important support\x01",
            "mission for the professor.\x02\x03",

            "Elmo may not be that far away,\x01",
            "but stay on the alert.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A1")

    label("loc_16E3")

    OP_A2(0x57A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1782")

    ChrTalk(    #39
        0x8,
        (
            "#790FHello, Tita.\x02\x03",

            "I've heard you're on your way\x01",
            "out to Elmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        (
            "#060FThat's right.\x02\x03",

            "Grandpa wants me to go and fix\x01",
            "the pump for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C8")

    label("loc_1782")


    ChrTalk(    #41
        0x8,
        (
            "#790FHello, you two.\x02\x03",

            "I've heard you're on your way\x01",
            "out to Elmo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_183B")

    ChrTalk(    #42
        0x101,
        (
            "#000FYeah, that's right.\x02\x03",

            "I guess Hazel's called you guys\x01",
            "about it already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "#790FThat's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CE")

    label("loc_183B")


    ChrTalk(    #44
        0x101,
        (
            "#004FI swear, Kilika, you've got the\x01",
            "sharpest ears of anybody I've\x01",
            "ever met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#790FHazel from the factory called\x01",
            "me with the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")


    ChrTalk(    #46
        0x8,
        (
            "#790FWe have your assignment.\x02\x03",

            "It's a support mission for \x01",
            "the professor.\x02\x03",

            "Elmo may not be that far away,\x01",
            "but stay on the alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#006FWe will.\x02\x03",

            "Time to get going.\x01",
            "See you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#010FWe'll return soon.\x02",
    )

    CloseMessageWindow()

    label("loc_19A1")

    Jump("loc_21E3")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A11")

    ChrTalk(    #49
        0x8,
        (
            "#790FGood luck with the job!\x02\x03",

            "#791FWe at the guild have our eyes\x01",
            "on that orbment, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9C")

    label("loc_1A11")

    OP_A2(0x0)

    ChrTalk(    #50
        0x8,
        (
            "#790FJoshua. Estelle.\x02\x03",

            "#791FThis looks like a big job,\x01",
            "but good luck with it.\x02\x03",

            "We at the guild have our eyes\x01",
            "on that orbment, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9C")

    Jump("loc_21E3")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE3")
    OP_A2(0x512)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3730, 0, 600, 0)
    SetChrPos(0x102, 4430, 0, -700, 0)
    SetChrPos(0x101, 3170, 0, -710, 0)
    SetChrPos(0x107, 4059, 0, -1760, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #51
        0x8,
        (
            "#791F#4PGood morning. That was some\x01",
            "day yesterday, wasn't it?\x02\x03",

            "When you are ready, we'd like\x01",
            "your full report on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#506FBusiness as usual, Kilika?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#792F#4PI've heard the basics from the\x01",
            "factory chief already...\x02\x03",

            "But I'd like to expand that account\x01",
            "with some first-hand details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#012FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #55
        "\x07\x05Joshua explained the details of the orbal blackout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #56
        0x8,
        (
            "#790F#4PI see...\x02\x03",

            "So the orbment that was sent to\x01",
            "Cassius in secret was in fact\x01",
            "something dangerous...\x02\x03",

            "The guild is very interested in these \x01",
            "developments. We need to continue working\x01",
            "with Professor Russell for the present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#006FWe thought you'd say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#010FWhen we have more information,\x01",
            "we'll contact you immediately.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1EA0")

    label("loc_1DE3")


    ChrTalk(    #59
        0x8,
        (
            "#790FSo that black orbment was in\x01",
            "fact something dangerous...\x02\x03",

            "The guild is very interested in these \x01",
            "developments. We need to continue working\x01",
            "with Professor Russell for the present.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA0")

    Jump("loc_21E3")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_213F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F3F")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #60
        0x8,
        (
            "#790FProfessor Russell's private laboratory\x01",
            "is in the southwest corner of town.\x02\x03",

            "Go out of the guild entrance and\x01",
            "make a left.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213C")

    label("loc_1F3F")

    OP_A2(0x0)
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #61
        0x8,
        (
            "#790FJoshua. Estelle.\x02\x03",

            "Professor Russell's private laboratory\x01",
            "is in the southwest corner of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#004FKilika, are you psychic?\x02\x03",

            "How did you know we were on\x01",
            "our way to the professor's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#792FCome now.\x02\x03",

            "You're with the professor's\x01",
            "granddaughter, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#008FOh yeah.\x02\x03",

            "Guess this saves me the time\x01",
            "of reporting in, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#790FThe professor is a very busy man.\x01",
            "Don't keep him waiting.\x02\x03",

            "Bye, Tita. Keep your eye on those\x01",
            "two for me, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        "#060FY-Yes, ma'am, I will...\x02",
    )

    CloseMessageWindow()

    label("loc_213C")

    Jump("loc_21E3")

    label("loc_213F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21E3")

    ChrTalk(    #67
        0x8,
        (
            "#790FFirst go the central factory and\x01",
            "meet with the factory chief,\x01",
            "Murdock.\x02\x03",

            "You should be able to get\x01",
            "some sort of information\x01",
            "about this orbment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    TalkEnd(0x8)
    Return()

    # Function_9_D21 end

    def Function_10_21E7(): pass

    label("Function_10_21E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2232")

    ChrTalk(    #68
        0xFE,
        (
            "I'm glad there wasn't any damage\x01",
            "to my store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_2232")

    OP_A2(0x1)

    ChrTalk(    #69
        0xFE,
        (
            "I was so surprised when the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I'd heard there were some rare\x01",
            "quartz crystals that could do\x01",
            "such a thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "...I didn't know it could be done\x01",
            "over such a wide radius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "If that were weaponized, any\x01",
            "arms race between countries\x01",
            "would be completely upset.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2365")

    TalkEnd(0xFE)
    Return()

    # Function_10_21E7 end

    def Function_11_2369(): pass

    label("Function_11_2369")

    TalkBegin(0xD)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E1")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_23CA")
    OP_A9(0x4C)
    Jump("loc_23D8")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23D6")
    OP_A9(0x4B)
    Jump("loc_23D8")

    label("loc_23D6")

    OP_A9(0x3E)

    label("loc_23D8")

    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_23E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F2")
    TalkEnd(0xD)
    Return()

    label("loc_23F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24DC")

    ChrTalk(    #73
        0xD,
        (
            "Good morning and welcome to\x01",
            "Bell Station!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        (
            "We have a wide selection of\x01",
            "the finest quality goods,\x01",
            "suited for your every need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        "So...buy somethin' will ya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        (
            "This store's success hinges on\x01",
            "all of my customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_24DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2533")

    ChrTalk(    #77
        0xD,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "Here at Bell Station we have\x01",
            "anything you might need!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_2533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_276B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25E4")

    ChrTalk(    #79
        0xD,
        "My wife finally understands...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xD,
        (
            "...and told me I didn't have to\x01",
            "expand our product line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xD,
        (
            "My wife finally gets it. That\x01",
            "alone is a huge motivator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2768")

    label("loc_25E4")

    OP_A2(0x2)

    ChrTalk(    #82
        0xD,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xD,
        "I'm having a great day so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xD,
        (
            "Finally, my wife seems to be\x01",
            "getting what I'm doing... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xD,
        (
            "She told me that we don't need\x01",
            "to expand our product line any\x01",
            "more than we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        (
            "Running your own business can\x01",
            "be tough, so finding ways to\x01",
            "economize is top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xD,
        (
            "And not being forced to expand\x01",
            "will go a long way for both my\x01",
            "wallet and my customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2768")

    Jump("loc_2E66")

    label("loc_276B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_28C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27F8")

    ChrTalk(    #88
        0xD,
        (
            "Hmm...usually my wife gets\x01",
            "angry at me when I cut prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xD,
        (
            "But she's been in good spirits\x01",
            "lately. What's going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BF")

    label("loc_27F8")

    OP_A2(0x2)

    ChrTalk(    #90
        0xD,
        "My wife's been acting strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xD,
        (
            "She knows that during the incident\x01",
            "at the central factory I was giving\x01",
            "some of our products away for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "But she hasn't said a word about\x01",
            "it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BF")

    Jump("loc_2E66")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_293A")

    ChrTalk(    #93
        0xD,
        (
            "My wife Ada gets such a stiff\x01",
            "neck sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "She went to the church to get\x01",
            "some medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2B")

    label("loc_293A")

    OP_A2(0x2)

    ChrTalk(    #95
        0xD,
        (
            "My wife Ada gets such a stiff\x01",
            "neck sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xD,
        (
            "She went to the church to get\x01",
            "some medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        (
            "I know they're researching\x01",
            "medicine at the central\x01",
            "factory as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "But they still have nothing on\x01",
            "the traditional remedies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2B")

    Jump("loc_2E66")

    label("loc_2A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AC9")

    ChrTalk(    #99
        0xD,
        (
            "My oldest boy has got quite an\x01",
            "interest in product placement\x01",
            "and presentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        (
            "If I left him alone he'd spend\x01",
            "all day doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_2AC9")

    OP_A2(0x2)
    TurnDirection(0xD, 0xF, 400)

    ChrTalk(    #101
        0xD,
        "Knowles!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "You need to stop handling the\x01",
            "merchandise so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "Remember your promise?\x01",
            "One arrangement per day.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_2B53")

    Jump("loc_2E66")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BDC")

    ChrTalk(    #104
        0xD,
        (
            "The orbment in the center of town\x01",
            "actually stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "Guess this world is still full\x01",
            "of surprises, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CE9")

    label("loc_2BDC")

    OP_A2(0x2)

    ChrTalk(    #106
        0xD,
        "Were you all okay last night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "I'd thought the lights had just\x01",
            "broken or something and was\x01",
            "on my way to the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "When I got outside though, \x01",
            "the entire town was dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        (
            "I don't have to be a genius to\x01",
            "know that something wasn't\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE9")

    Jump("loc_2E66")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2DE6")

    ChrTalk(    #110
        0xD,
        (
            "I'd love it if everybody thought\x01",
            "of my place as the little\x01",
            "'neighborhood' store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "I try to keep a little something\x01",
            "for everyone on the shelves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xD,
        (
            "It's hard to balance the logistics,\x01",
            "but nothing worthwhile ever came\x01",
            "easy, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E66")

    ChrTalk(    #113
        0xD,
        (
            "Come on in!\x01",
            "Welcome to Bell Station!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "We're the only store that carries\x01",
            "everything from food to everyday\x01",
            "goods!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E66")

    TalkEnd(0xD)
    Return()

    # Function_11_2369 end

    def Function_12_2E6A(): pass

    label("Function_12_2E6A")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2E77")
    Jump("loc_2F04")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2F04")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF3")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_2EDC")
    OP_A9(0x4C)
    Jump("loc_2EEA")

    label("loc_2EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2EE8")
    OP_A9(0x4B)
    Jump("loc_2EEA")

    label("loc_2EE8")

    OP_A9(0x3E)

    label("loc_2EEA")

    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_2EF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F04")
    TalkEnd(0xE)
    Return()

    label("loc_2F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F74")

    ChrTalk(    #115
        0xE,
        (
            "Looks like another hard month\x01",
            "ahead for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xE,
        (
            "But we'll be ready for it and\x01",
            "get through it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E4")

    label("loc_2F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FA8")

    ChrTalk(    #117
        0xE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xE,
        "Welcome to Bell Station!\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E4")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_30BF")

    ChrTalk(    #119
        0xE,
        (
            "I had a long talk with my husband\x01",
            "this morning about the direction\x01",
            "of this store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xE,
        (
            "We decided not to expand our\x01",
            "line of merchandise any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xE,
        (
            "And I'm to be in charge of\x01",
            "product ordering and stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xE,
        (
            "I wonder how it'll go. We won't\x01",
            "know without trying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E4")

    label("loc_30BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_32C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_31E6")

    ChrTalk(    #123
        0xE,
        (
            "But still...I think I'm starting to\x01",
            "see what my husband is trying\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xE,
        (
            "My husband is a bit more of a\x01",
            "dreamer than a salesman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xE,
        (
            "...but he really wants to help\x01",
            "this community.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xE,
        (
            "It'd be so amazing if we could\x01",
            "build the kind of store that\x01",
            "realizes that dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_31E6")

    OP_A2(0x3)

    ChrTalk(    #127
        0xE,
        (
            "Today, my husband was out at\x01",
            "the central factory after the\x01",
            "incident giving out free supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xE,
        (
            "It's going to put us into the\x01",
            "red for the month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xE,
        (
            "...but that's fine. We'll just\x01",
            "consider it pro bono.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BE")

    Jump("loc_37E4")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3354")

    ChrTalk(    #130
        0xE,
        (
            "I can't believe the central factory\x01",
            "was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "How did my husband figure out\x01",
            "that something had happened\x01",
            "so quickly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3403")

    label("loc_3354")

    OP_A2(0x3)

    ChrTalk(    #132
        0xE,
        (
            "Is it true that someone attacked\x01",
            "the central factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xE,
        (
            "My husband left a little while ago,\x01",
            "and he still hasn't come home yet... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        "I hope nothing's happened...\x02",
    )

    CloseMessageWindow()

    label("loc_3403")

    Jump("loc_37E4")

    label("loc_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_34BD")

    ChrTalk(    #135
        0xE,
        (
            "My husband said that something\x01",
            "seemed wrong and then he rushed\x01",
            "out of the store. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "He took a lot of merchandise\x01",
            "along with him, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xE,
        "What is he thinking...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E4")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_35D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3558")

    ChrTalk(    #138
        0xE,
        (
            "Oh well. I still have plenty\x01",
            "of work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xE,
        (
            "I'll just tidy up and then go to\x01",
            "the church to get some medicine\x01",
            "for my stiff neck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D3")

    label("loc_3558")

    OP_A2(0x3)

    ChrTalk(    #140
        0xE,
        (
            "We've been able to accomplish\x01",
            "so much due to the orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xE,
        (
            "But yesterday's incident made\x01",
            "me start thinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D3")

    Jump("loc_37E4")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_374D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3682")

    ChrTalk(    #142
        0xE,
        (
            "If we don't keep our best selling\x01",
            "product in stock, we won't make\x01",
            "any profits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        (
            "Oh, my shoulders are so stiff it's\x01",
            "started to give me a headache.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374A")

    label("loc_3682")

    OP_A2(0x3)

    ChrTalk(    #144
        0xE,
        (
            "My husband never orders the\x01",
            "proper amounts of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xE,
        (
            "I keep telling him to take more\x01",
            "care of the merchandise that\x01",
            "sells better...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xE,
        (
            "Doesn't he know anything about\x01",
            "being a salesman?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374A")

    Jump("loc_37E4")

    label("loc_374D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_37E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_37A5")

    ChrTalk(    #147
        0xE,
        (
            "Looking at our books makes my\x01",
            "neck and shoulders start acting\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E4")

    label("loc_37A5")

    OP_A2(0x3)

    ChrTalk(    #148
        0xE,
        "...Oh dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "This month's going to be\x01",
            "a tight one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E4")

    TalkEnd(0xE)
    Return()

    # Function_12_2E6A end

    def Function_13_37E8(): pass

    label("Function_13_37E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3835")

    ChrTalk(    #150
        0xFE,
        "That was strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Mom actually paid Dad\x01",
            "a compliment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A10")

    label("loc_3835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_38CB")

    ChrTalk(    #152
        0xFE,
        (
            "Dad took a lot of stuff with\x01",
            "him when he left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I can understand the food and\x01",
            "medicine, but why dolls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "What a mess this is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A10")

    label("loc_38CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_390F")

    ChrTalk(    #155
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "...There. Perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "It's fine as it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A10")

    label("loc_390F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3999")

    ChrTalk(    #158
        0xFE,
        (
            "Dad told me to only rearrange\x01",
            "the shelves once a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "But I've got to put back the\x01",
            "stuff that customers moved!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A10")

    label("loc_3999")

    OP_A2(0x4)

    ChrTalk(    #160
        0xFE,
        (
            "And this fish should go a little\x01",
            "more to the left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "...There we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Everything's all balanced now.\x02",
    )

    CloseMessageWindow()

    label("loc_3A10")

    TalkEnd(0xFE)
    Return()

    # Function_13_37E8 end

    def Function_14_3A14(): pass

    label("Function_14_3A14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3AAB")

    ChrTalk(    #163
        0xFE,
        (
            "Hurry, Doctor!\x01",
            "It's an emergency!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Mommy's neck is stiff again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "What's that, you say? We must\x01",
            "contact Father Vixen at once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3AE7")

    ChrTalk(    #166
        0xFE,
        (
            "It isn't dark outside like it\x01",
            "was yesterday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3B16")

    ChrTalk(    #167
        0xFE,
        "Mommy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "Where'd Daddy go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3B78")

    ChrTalk(    #169
        0xFE,
        "Yesterday it was dark out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "It was like when I stick my\x01",
            "head under the covers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3C38")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #171
        0xFE,
        (
            "Professor! The orbal...pr-pr-...\x01",
            "precushion is dropping!\x01",
            "We need MOAR POWAH STAT!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "What's that? But the Orbal\x01",
            "Engine readings are green!\x01",
            "GREEEEEN, I TELL YOU!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4F")

    label("loc_3C38")

    OP_A2(0x5)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #173
        0xFE,
        "It's TITA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Tita, let's play Orbaldilly Engineers\x01",
            "again! This time I get to hobgoblin\x01",
            "the ding-bezel-orbalerator, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x107,
        (
            "#560FSorry, Didi. I have to show my\x01",
            "friends around first.\x02\x03",

            "#061FMaybe next time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "Oookaaay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Yes, MA'AM, PROFESSOR TITA!\x02",
    )

    CloseMessageWindow()

    label("loc_3D4F")

    Jump("loc_3D84")

    label("loc_3D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D84")

    ChrTalk(    #178
        0xFE,
        (
            "Who are you guys?\x01",
            "Pirates? Or ninjas?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D84")

    TalkEnd(0xFE)
    Return()

    # Function_14_3A14 end

    def Function_15_3D88(): pass

    label("Function_15_3D88")

    TalkBegin(0x11)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF4")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_3DE9")
    OP_A9(0x42)
    Jump("loc_3DEB")

    label("loc_3DE9")

    OP_A9(0x3D)

    label("loc_3DEB")

    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_3DF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E05")
    TalkEnd(0x11)
    Return()

    label("loc_3E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3EE3")

    ChrTalk(    #179
        0x11,
        (
            "Say what you like, Stain has it\x01",
            "pretty well made. I should learn\x01",
            "from his example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        (
            "I think he's a bit too set in his\x01",
            "ways of course, but..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x11,
        (
            "That's all part of the learning\x01",
            "experience, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF5")

    label("loc_3EE3")

    OP_A2(0x6)

    ChrTalk(    #182
        0x11,
        (
            "Yesterday I talked to Stain,\x01",
            "the owner, about our stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "I decided to try going with his\x01",
            "recommendations this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x11,
        (
            "That doesn't mean I've started\x01",
            "subscribing to his 'Dependable\x01",
            "Above All' philosophy yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x11,
        (
            "But it's all part of the\x01",
            "learning experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF5")

    Jump("loc_4B3E")

    label("loc_3FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_413C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4086")

    ChrTalk(    #186
        0x11,
        (
            "I didn't think Karl'd ever say\x01",
            "that about Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x11,
        (
            "Guess he's started thinking\x01",
            "like him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x11,
        "Great. It's spreading.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4139")

    label("loc_4086")

    OP_A2(0x6)

    ChrTalk(    #189
        0x11,
        (
            "Early this morning Karl came to\x01",
            "the store and said, 'I get what\x01",
            "Stain means now,' and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x11,
        (
            "I didn't think Karl'd ever say\x01",
            "that about Stain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x11,
        "Maybe he's...right?\x02",
    )

    CloseMessageWindow()

    label("loc_4139")

    Jump("loc_4B3E")

    label("loc_413C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_419F")

    ChrTalk(    #192
        0x11,
        "That engineer, Karl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x11,
        (
            "It seems like Stain's indoctrinated\x01",
            "him at last.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_419F")

    OP_A2(0x6)

    ChrTalk(    #194
        0x11,
        (
            "Early this morning Karl came to\x01",
            "the store and said, 'I get what\x01",
            "Stain means now,' and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x11,
        "What could have happened?\x02",
    )

    CloseMessageWindow()

    label("loc_4222")

    Jump("loc_4B3E")

    label("loc_4225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4282")

    ChrTalk(    #196
        0x11,
        "Hey, thanks for staying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "I'm not closing up just yet,\x01",
            "so take your time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3E")

    label("loc_4282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_42E9")

    ChrTalk(    #198
        0x11,
        "Was anything damaged?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x11,
        (
            "I hope this doesn't disrupt the\x01",
            "research timetable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4361")

    label("loc_42E9")

    OP_A2(0x6)

    ChrTalk(    #200
        0x11,
        (
            "Hey, did you hear?! The central\x01",
            "factory was attacked! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x11,
        (
            "I was inside the store talking,\x01",
            "so I didn't see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4361")

    Jump("loc_4B3E")

    label("loc_4364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_44E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_43D2")

    ChrTalk(    #202
        0x11,
        "Now THAT is an orbal gun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x11,
        (
            "If it were a little better balanced,\x01",
            "it'd sell like mad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E2")

    label("loc_43D2")

    OP_A2(0x6)

    ChrTalk(    #204
        0x11,
        (
            "Karl from the central factory\x01",
            "brought over an experimental\x01",
            "orbal gun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x11,
        (
            "It's a fine weapon. Got some\x01",
            "real power behind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        (
            "It's a bit unbalanced and kind\x01",
            "of finicky sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x11,
        (
            "...but I think you can overlook that\x01",
            "in light of its raw stopping power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E2")

    Jump("loc_4B3E")

    label("loc_44E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_46FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4569")

    ChrTalk(    #208
        0x11,
        (
            "I really hope Karl brings us a\x01",
            "test unit soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        (
            "It's about the only thing I look\x01",
            "forward to these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FB")

    label("loc_4569")

    OP_A2(0x6)

    ChrTalk(    #210
        0x11,
        "Hello, come on in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x11,
        (
            "Stain, the owner, and I had\x01",
            "some words again about\x01",
            "stocking policies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x11,
        (
            "He just doesn't want us to carry\x01",
            "any of the experimental orbal\x01",
            "weapons here yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x11,
        (
            "I tried sticking to my ideas, but\x01",
            "in the end it's not my decision.\x01",
            "It's his store, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x11,
        (
            "I really hope Karl brings us a\x01",
            "test unit soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        (
            "It's about the only thing I look\x01",
            "forward to these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46FB")

    Jump("loc_4B3E")

    label("loc_46FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_478A")

    ChrTalk(    #216
        0x11,
        (
            "There's something big going on\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x11,
        (
            "All of their measuring devices\x01",
            "have to be going nuts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4825")

    label("loc_478A")

    OP_A2(0x6)

    ChrTalk(    #218
        0x11,
        (
            "Last night I was tinkering with\x01",
            "that orbal gun...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x11,
        (
            "When suddenly my analyzer just\x01",
            "went dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x11,
        (
            "I thought for a second I had\x01",
            "broken the gun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4825")

    Jump("loc_4B3E")

    label("loc_4828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_48C4")

    ChrTalk(    #221
        0x11,
        (
            "I can appreciate the owner's\x01",
            "philosophy about dependability\x01",
            "as much as anybody...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x11,
        (
            "...but he's too hardheaded about\x01",
            "it sometimes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7B")

    label("loc_48C4")

    OP_A2(0x6)

    ChrTalk(    #223
        0x11,
        (
            "This store's owner is Stain,\x01",
            "the guy who lives just next\x01",
            "door to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x11,
        (
            "He's really pushing for us not to carry\x01",
            "any of the new cutting-edge weaponry.\x01",
            "Takes the joy out of the job, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x11,
        (
            "He says that the newest stuff\x01",
            "isn't reliable enough for him to\x01",
            "stock in good faith...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x11,
        (
            "But he's turning down the newest prototypes from\x01",
            "the best factory inventors! Some of these things\x01",
            "can perforate a Rhinocider! What a waste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A7B")

    Jump("loc_4B3E")

    label("loc_4A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B3E")

    ChrTalk(    #227
        0x11,
        (
            "Greetings, weapon enthusiasts!\x01",
            "Welcome to Stain Arms & Guards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x11,
        (
            "Do the sight of fell accoutrements make\x01",
            "your palms sweaty? Well, shop here!\x01",
            "We cater to the violently-inclined!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3E")

    TalkEnd(0x11)
    Return()

    # Function_15_3D88 end

    def Function_16_4B42(): pass

    label("Function_16_4B42")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4BE2")

    ChrTalk(    #229
        0xFE,
        (
            "I know the scientists are leery,\x01",
            "but I think we should trust\x01",
            "Agate on this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "There are things sometimes that\x01",
            "we just gotta do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB7")

    label("loc_4BE2")


    ChrTalk(    #231
        0xFE,
        (
            "Hey, you guys. I heard about your\x01",
            "little rescue mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I know it's not the ending you're\x01",
            "looking for, but we ought to trust\x01",
            "Agate on this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "He'll be able to get those\x01",
            "scientists out of there safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB7")

    Jump("loc_56B5")

    label("loc_4CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_END)), "loc_4D8E")

    ChrTalk(    #234
        0xFE,
        (
            "Glad to see Wong working\x01",
            "so hard in my absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I was worried he was going to\x01",
            "get down on himself because\x01",
            "of the incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Guess Kilika knocked that\x01",
            "nonsense out of him, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5192")

    label("loc_4D8E")

    OP_A2(0x57E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_4E50")

    ChrTalk(    #237
        0x101,
        "#000FGundolf!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        "#010FYou're back from the capital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Yeah, I got the news. I flew\x01",
            "back quick as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "I got the rundown from Kilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "...but is Agate okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F34")

    label("loc_4E50")


    ChrTalk(    #242
        0xFE,
        (
            "You guys are those junior\x01",
            "bracers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "I'm Gundolf, Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "I got the news and came from\x01",
            "my other assignment in the\x01",
            "capital as soon as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "I got the rundown from Kilika,\x01",
            "but is Agate all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F34")


    ChrTalk(    #246
        0x101,
        (
            "#000FHe seems past the worst of it.\x02\x03",

            "Wait a second, are you one\x01",
            "of Agate's friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "Yeah, we've run into each other\x01",
            "a few times out in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "He's kind of made a name for\x01",
            "himself by doing the stuff that's\x01",
            "patently insane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "But what doesn't kill him only\x01",
            "makes him stronger, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "You guys and Agate are okay\x01",
            "to handle the rest of this\x01",
            "assignment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "I should be able to help out a\x01",
            "little with some of the smaller\x01",
            "details, if you want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#000FThanks, Gundolf!\x02\x03",

            "That'd be great of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        "#010FThank you again, Gundolf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "No problem.\x01",
            "I'm counting on you, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5192")

    Jump("loc_56B5")

    label("loc_5195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_56B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5639")
    OP_A2(0x57D)
    OP_4A(0x13, 255)
    OP_4A(0x12, 255)

    ChrTalk(    #255
        0x13,
        "What? An assignment?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x13,
        "You? Now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x12,
        "Yeah, just a little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x12,
        (
            "The army kind of asked for me\x01",
            "specifically...so I'm off to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x12,
        (
            "It's not just you, anyway...\x01",
            "you've got those two juniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x12,
        (
            "Put your heads together. You'll\x01",
            "be fine. I won't be gone more\x01",
            "than a couple of days or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x13,
        "Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x13,
        "I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x12,
        "Good. And relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x12,
        "Hello.  \x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(    #265
        0x12,
        "Who's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x12,
        "You guys have good timing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542A")
    OP_A2(0x57C)

    ChrTalk(    #267
        0x13,
        "...Excuse me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #268
        0x13,
        (
            "You wouldn't, by any chance,\x01",
            "be junior bracers would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#000FWhat?\x02\x03",

            "Y-Yeah, we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        "#010FI'm Junior Bracer Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#000FI'm Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5478")

    label("loc_542A")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #272
        0x13,
        "Estelle, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x13,
        (
            "You've shown up at quite a\x01",
            "convenient time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5478")


    ChrTalk(    #274
        0x12,
        "So, it IS you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x12,
        "Just like Kilika said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x102,
        (
            "#010FExcuse me...are you on your\x01",
            "way to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x12,
        (
            "Yeah, I was. A small...request...\x01",
            "came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x12,
        (
            "I'm leaving things here in Zeiss\x01",
            "to you two and Wong for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x12,
        "Don't burn the place down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x13,
        (
            "...So, yes.\x01",
            "We could use your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        "#000FSure. You can rely on us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x12,
        (
            "It's settled then. I'll leave\x01",
            "things to you all.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_4B(0x12, 255)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_56B5")

    label("loc_5639")


    ChrTalk(    #284
        0x12,
        (
            "Don't do anything that'll make\x01",
            "me regret leaving you guys in\x01",
            "charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x12,
        (
            "Make sure you give them a\x01",
            "proper hand, Wong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B5")

    TalkEnd(0x12)
    Return()

    # Function_16_4B42 end

    def Function_17_56B9(): pass

    label("Function_17_56B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_5809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5759")

    ChrTalk(    #286
        0xFE,
        (
            "I heard you were on your way\x01",
            "to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "It'll be fine...you two are going\x01",
            "to make great bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "Good luck to you both.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5806")

    label("loc_5759")

    OP_A2(0x8)

    ChrTalk(    #289
        0xFE,
        "Hello, you two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "I heard about how well your\x01",
            "rescue mission went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "It's still too early to pat ourselves\x01",
            "on the backs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "...but you did good. Thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_5806")

    Jump("loc_62E6")

    label("loc_5809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAD")
    OP_A2(0x57D)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)

    ChrTalk(    #293
        0x13,
        "What? An assignment?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x13,
        "You? Now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x12,
        "Yeah, just a little one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x12,
        (
            "The army kind of asked for me\x01",
            "specifically...so I'm off to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x12,
        (
            "It's not just you, anyway...\x01",
            "you've got those two juniors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x12,
        (
            "Put your heads together. You'll\x01",
            "be fine. I won't be gone more\x01",
            "than a couple of days or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x13,
        "Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x13,
        "I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x12,
        "Good. And relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x12,
        "Hello.  \x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x0, 400)

    ChrTalk(    #303
        0x12,
        "Who's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x12,
        "You guys have good timing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9E")
    OP_A2(0x57C)

    ChrTalk(    #305
        0x13,
        "...Excuse me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #306
        0x13,
        (
            "You wouldn't, by any chance,\x01",
            "be junior bracers would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        (
            "#000FWhat?\x02\x03",

            "Y-Yeah, we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        "#010FI'm Junior Bracer Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        "#000FI'm Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AEC")

    label("loc_5A9E")

    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #310
        0x13,
        "Estelle, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x13,
        (
            "You've shown up at quite a\x01",
            "convenient time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AEC")


    ChrTalk(    #312
        0x12,
        "So, it IS you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x12,
        "Just like Kilika said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x102,
        (
            "#010FExcuse me...are you on your\x01",
            "way to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x12,
        (
            "Yeah, I was. A small...request...\x01",
            "came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x12,
        (
            "I'm leaving things here in Zeiss\x01",
            "to you two and Wong for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x12,
        "Don't burn the place down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x13,
        (
            "...So, yes.\x01",
            "We could use your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#000FSure. You can rely on us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x102,
        "#010FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x12,
        (
            "It's settled then. I'll leave\x01",
            "things to you all.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    Jump("loc_5D29")

    label("loc_5CAD")


    ChrTalk(    #322
        0xFE,
        (
            "Gundolf won't be here for the\x01",
            "time being...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "We'll just have to make that\x01",
            "much extra effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "Got it, you two?\x02",
    )

    CloseMessageWindow()

    label("loc_5D29")

    Jump("loc_62E6")

    label("loc_5D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_611F")
    OP_A2(0x57C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D8C")

    ChrTalk(    #325
        0xFE,
        "Oh, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "Strange, seeing you in the\x01",
            "weapons shop...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB4")

    label("loc_5D8C")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #327
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "If it isn't Tita!\x02",
    )

    CloseMessageWindow()

    label("loc_5DB4")


    ChrTalk(    #329
        0xFE,
        "Hey...these guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x107,
        (
            "#060FThat's right. They're bracers.\x02\x03",

            "I'm showing them to my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        "Yeah, I thought so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "I'm Wong, Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "I'm new here myself, so we're\x01",
            "kind of in the same boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#000FIs that right? Well, it's great\x01",
            "to meet you.\x02\x03",

            "I'm Junior Bracer Estelle.\x01",
            "This is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x102,
        (
            "#010FJoshua.\x02\x03",

            "A pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        (
            "I'd heard from Kilika earlier\x01",
            "about some pretty amazing\x01",
            "juniors coming to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "Your reputation precedes you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        "#008FAw, you're making me blush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x102,
        (
            "#010FI'm afraid we're not quite as\x01",
            "good as you might have heard.\x01",
            "We were just lucky.\x02\x03",

            "We had the help of some amazing\x01",
            "senior bracers and some very\x01",
            "generous civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "Ha, charisma is a praise-worthy\x01",
            "quality too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "At any rate, we're understaffed.\x01",
            "We need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "Welcome aboard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        "#001FThank you, Wong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        "#010FIndeed. Thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6184")

    label("loc_611F")


    ChrTalk(    #345
        0xFE,
        (
            "Estelle, Joshua...we're counting\x01",
            "on you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "Even if it is just a temporary assignment...\x02",
    )

    CloseMessageWindow()

    label("loc_6184")

    Jump("loc_62E6")

    label("loc_6187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_62E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6232")

    ChrTalk(    #347
        0xFE,
        "Balance or effectiveness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "Well, whichever is more important\x01",
            "is ultimately up to the individual to\x01",
            "decide, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        "It certainly isn't up to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_62E6")

    label("loc_6232")

    OP_A2(0x8)

    ChrTalk(    #350
        0xFE,
        "Decisions...decisions...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "Do I want a balanced general\x01",
            "use weapon or do I want an\x01",
            "ace-in-the-hole cannon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "I ought to just buy both and stop\x01",
            "wasting time worrying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E6")

    TalkEnd(0xFE)
    Return()

    # Function_17_56B9 end

    def Function_18_62EA(): pass

    label("Function_18_62EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6301")
    Call(0, 12)
    Jump("loc_6305")

    label("loc_6301")

    Call(0, 11)

    label("loc_6305")

    Return()

    # Function_18_62EA end

    def Function_19_6306(): pass

    label("Function_19_6306")

    Call(0, 15)
    Return()

    # Function_19_6306 end

    def Function_20_630B(): pass

    label("Function_20_630B")

    EventBegin(0x0)
    OP_6D(2000, 0, -5200, 0)
    SetChrPos(0x101, 2400, 0, -5400, 0)
    SetChrPos(0x102, 1300, 0, -5500, 0)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #353
        0x101,
        "#501FHi there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x102,
        "#010FPardon us.\x02",
    )

    CloseMessageWindow()

    def lambda_6382():
        OP_6D(3600, 0, 520, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6382)

    def lambda_639A():
        OP_8E(0xFE, 0xED8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_639A)
    Sleep(500)

    def lambda_63BA():
        OP_8E(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63BA)
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #355
        0x8,
        "Eastern Woman",
        "#792F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        "#006FUmm... See, we're--\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #357
        0x8,
        "Eastern Woman",
        (
            "#790F...finally here, I see.\x02\x03",

            "#790FEstelle... Joshua...\x01",
            "Welcome to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        "#014FYou know us?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #360
        0x8,
        "Eastern Woman",
        (
            "#792FI've already been briefed of\x01",
            "your arrival from one Jean,\x01",
            "at the Ruan branch.\x02\x03",

            "A girl with chestnut hair, tied in\x01",
            "twin ponytails, and a boy with\x01",
            "black hair and amber eyes...\x02\x03",

            "#791FThat is you, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#008FI...okay.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #362
        0x8,
        "Eastern Woman",
        (
            "#790FMy name is Kilika. Zeiss\x01",
            "welcomes your service.\x02\x03",

            "It's a pleasure to make\x01",
            "your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        "#006FOh, uh, same here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x102,
        "#010FThe pleasure is ours.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x8,
        (
            "#790FI know you've only just arrived, but I'd\x01",
            "like to proceed with the formalities of\x01",
            "changing your affiliation.\x02\x03",

            "If you'll just sign these documents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #367
        "\x07\x05Estelle and Joshua signed the assignment-change forms.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #368
        0x8,
        (
            "#792F...That should do it.\x02\x03",

            "#790FYou are both now affiliates of\x01",
            "the Zeiss regional guild.\x02\x03",

            "There are no urgent matters that\x01",
            "must be seen to, currently.\x02\x03",

            "You're free to check the bulletin\x01",
            "board and work at your own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#007FThat's kind of disappointing...\x01",
            "but hey, a little peace and\x01",
            "quiet can be a good thing.\x02\x03",

            "#002FOh, right.\x01",
            "I had a question to ask...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x8,
        "#792FAbout Cassius, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        "#004FShe can read minds!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x102,
        (
            "#014FDid Jean tell you about him,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x8,
        (
            "#790FThe whole sordid matter.\x02\x03",

            "I'm sorry to have to say that\x01",
            "Cassius is not currently in\x01",
            "the Zeiss region.\x02\x03",

            "He only stops in every\x01",
            "few months or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x101,
        "#505F*sigh* Figures...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x102,
        (
            "#013FThat just leaves Grancel,\x01",
            "or maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#792FI believe I might be able\x01",
            "to provide you with a lead\x01",
            "in another matter.\x02\x03",

            "Please, take this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #377
        "\x07\x00Received '\x07\x02Attn. Factory Chief\x07\x00'.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x360, 1)

    ChrTalk(    #378
        0x101,
        "#004FWhat's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x8,
        (
            "#790FIt is a letter of introduction \x01",
            "to the head of the central \x01",
            "factory: one Mr. Murdock.\x02\x03",

            "He is basically like the mayor\x01",
            "of the Zeiss region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x102,
        (
            "#012FIs this in regards to the matter\x01",
            "of the black orbment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x8,
        (
            "#790FThe stories of the mayor's residence\x01",
            "paint it as a very mysterious item.\x02\x03",

            "I'd suggest that you consult\x01",
            "with the factory chief, and\x01",
            "see what he has to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x101,
        (
            "#008FW-Wow. You've really got\x01",
            "this all planned out...\x02\x03",

            "Do you have some kind of\x01",
            "super power, Kilika?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x8,
        (
            "#790FMy business is to provide support\x01",
            "for bracers, such as yourselves.\x02\x03",

            "I simply decipher the intelligence\x01",
            "that's provided and pass it on, as\x01",
            "the mandates of my job require.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        "#506FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x102,
        (
            "#019FWe really appreciate your\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x8,
        (
            "#791FThink nothing of it.\x02\x03",

            "I trust that you will return\x01",
            "to assist us, should a major\x01",
            "incident occur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x101,
        (
            "#008FHa ha ha... You can count on\x01",
            "us when the time comes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x102,
        (
            "#010FWell, do you want to go ahead\x01",
            "and see the factory chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#006FSounds good to me.\x02",
    )

    CloseMessageWindow()
    OP_28(0x53, 0x3, 0x2)
    OP_28(0x53, 0x3, 0x4)
    OP_28(0x3F, 0x4, 0x2)
    OP_28(0x3F, 0x4, 0x4)
    OP_28(0x3F, 0x1, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_20_630B end

    def Function_21_6EDD(): pass

    label("Function_21_6EDD")

    EventBegin(0x0)
    OP_6D(1370, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 760, 0, -4930, 0)
    SetChrPos(0x101, 1850, 0, -5150, 0)
    SetChrPos(0x107, 1150, 0, -5860, 0)
    SetChrPos(0x106, 2350, 0, -5930, 0)

    def lambda_6F66():

        label("loc_6F66")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F66")

    QueueWorkItem2(0x101, 1, lambda_6F66)

    def lambda_6F77():

        label("loc_6F77")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F77")

    QueueWorkItem2(0x102, 1, lambda_6F77)

    def lambda_6F88():

        label("loc_6F88")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F88")

    QueueWorkItem2(0x106, 1, lambda_6F88)

    def lambda_6F99():

        label("loc_6F99")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F99")

    QueueWorkItem2(0x107, 1, lambda_6F99)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4070, 0, -700, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #390
        0x8,
        "#790F#3PYou have impeccable timing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        "#004FOh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        "#014FIt's you...\x02",
    )

    CloseMessageWindow()

    def lambda_7022():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7022)
    Sleep(400)

    ChrTalk(    #393
        0x9,
        (
            "#130FOh, my. Estelle and Joshua...?\x02\x03",

            "I haven't seen you two in some\x01",
            "time. You're doing well, I hope?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_709F():
        OP_6D(3150, 0, -410, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_709F)

    def lambda_70B7():
        OP_8E(0xFE, 0xBF4, 0x0, 0xFFFFF9D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70B7)
    Sleep(100)

    def lambda_70D7():
        OP_8E(0xFE, 0x884, 0x0, 0xFFFFFB96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70D7)
    Sleep(50)

    def lambda_70F7():
        OP_8E(0xFE, 0xF82, 0x0, 0xFFFFF574, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_70F7)
    Sleep(100)

    def lambda_7117():
        OP_8E(0xFE, 0xA46, 0x0, 0xFFFFF542, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7117)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #394
        0x101,
        (
            "#501FProfessor Alba?\x01",
            "What are you doing in Zeiss?\x02\x03",

            "Tell me you got an escort\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x8,
        (
            "#792FNever mind that. We've learned\x01",
            "the whereabouts of the criminals.\x02\x03",

            "This gentleman is an eyewitness.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #396
        0x101,
        "#004FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x106,
        "#054FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x9,
        (
            "#131F#4PHmmm... I thought what I saw\x01",
            "might be significant.\x02\x03",

            "Good, then.\x01",
            "I'm glad I came.\x02\x03",

            "Anyway, I'd been doing field\x01",
            "research on the tower, up\x01",
            "until a short time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x101,
        (
            "#002FYou're talking about one of\x01",
            "the Tetracyclic Towers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x106,
        (
            "#552FIt'd have to be the Carnelia\x01",
            "Tower, north of the plains\x01",
            "road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x9,
        (
            "#131F#4PYes, and I saw several soldiers\x01",
            "enter the structure.\x02\x03",

            "I initially thought them to be\x01",
            "members of the Royal Army, but...\x02\x03",

            "They seemed to be sticking to the shadows,\x01",
            "and I heard them mention something about a\x01",
            "kidnapping and an escape route.\x02\x03",

            "I was greatly unsettled by the\x01",
            "whole matter, so I came directly\x01",
            "here to tell what I saw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x102,
        (
            "#012FThese soldiers... What kind of\x01",
            "uniforms were they wearing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x9,
        (
            "#130F#4PLet me think... It was a blue and\x01",
            "white uniform. Very sharp-looking.\x02\x03",

            "Just as one would expect from Her\x01",
            "Majesty's native land. Even the\x01",
            "military dresses stylishly.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x106, 0xFF)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #404
        0x106,
        (
            "#057F#2PThat's gotta be them...\x01",
            "C'mon, we have to hurry\x01",
            "to the Carnelia Tower!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_766D():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_766D)

    def lambda_767B():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_767B)

    ChrTalk(    #405
        0x101,
        "#005F#3PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x102,
        "#012FAcknowledged!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x107,
        "#065FU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_44(0x106, 0xFF)
    OP_44(0x107, 0xFF)

    def lambda_76D0():
        OP_6D(3060, 0, -1580, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76D0)

    def lambda_76E8():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76E8)

    def lambda_76F6():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76F6)
    TurnDirection(0x106, 0x107, 400)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #408
        0x107,
        (
            "#062FPlease...\x02\x03",

            "Take me with you...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x101,
        "#004F#4PTita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x102,
        "#013F#3PWell...\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)

    ChrTalk(    #411
        0x106,
        "#050F#4PHey, runt.\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0xFF)
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #412
        0x107,
        "#065FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x106,
        (
            "#050F#4PThere's no good reason for\x01",
            "us to bring you along.\x02\x03",

            "Use that brain of yours\x01",
            "for some common sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x107,
        (
            "#063FB-But...!!\x02\x03",

            "Grandpa was kidnapped!\x01",
            "I... I have to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x106,
        (
            "#053F#4PTime is mira, kid, so let\x01",
            "me put it to you straight.\x02\x03",

            "#057FYou're just gonna get in\x01",
            "the way. You stay behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x107,
        "#065F...!\x02",
    )

    OP_9E(0x107, 0xF, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(    #417
        0x101,
        (
            "#005FHey, hold on a second!\x01",
            "Where do you get off,\x01",
            "talking to her like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x106,
        (
            "#057F#4POh, shut it.\x01",
            "You know I'm right.\x02\x03",

            "We can't afford to pick up some\x01",
            "amateur's slack... Much less a\x01",
            "goddamned kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x101,
        "#003FW-Well...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 600)

    ChrTalk(    #420
        0x101,
        (
            "#009FJoshua! Don't just stand there!\x01",
            "Say something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x102,
        (
            "#013FI'm sorry...but I'm with him\x01",
            "on this.\x02\x03",

            "There's not a chance in the world\x01",
            "that those men aren't expecting\x01",
            "us to be on their trail.\x02\x03",

            "As much as I'd like to have her\x01",
            "with us, it's just too dangerous\x01",
            "to bring her along.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #422
        0x107,
        "#065FJ-Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        "#007F*sigh*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #424
        0x101,
        (
            "#003F#4P...I'm sorry, Tita. I guess\x01",
            "we can't take you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #425
        0x107,
        "#065FEs... Estelle...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x107, 0x14, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #426
        0x107,
        (
            "#069FHow... How can you be\x01",
            "so mean?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C01():

        label("loc_7C01")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7C01")

    QueueWorkItem2(0x101, 1, lambda_7C01)

    def lambda_7C12():

        label("loc_7C12")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7C12")

    QueueWorkItem2(0x102, 1, lambda_7C12)

    def lambda_7C23():

        label("loc_7C23")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_7C23")

    QueueWorkItem2(0x106, 1, lambda_7C23)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 225, 800)

    def lambda_7C4D():
        OP_6D(2320, 0, -1650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C4D)
    OP_8E(0x107, 0x6C2, 0x0, 0xFFFFEDFE, 0x1388, 0x0)
    OP_8E(0x107, 0x5F0, 0x0, 0xFFFFE87C, 0x1388, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)
    OP_8E(0x107, 0x6F4, 0x0, 0xFFFFE160, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)

    ChrTalk(    #427
        0x101,
        "#004FTita!\x02",
    )

    CloseMessageWindow()

    def lambda_7CCC():
        OP_8E(0xFE, 0x924, 0x0, 0xFFFFF57E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CCC)
    Sleep(50)
    OP_8E(0x102, 0x8FC, 0x0, 0xFFFFF8E4, 0xFA0, 0x0)

    def lambda_7D00():
        OP_8F(0xFE, 0x924, 0x0, 0xFFFFF57E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D00)

    def lambda_7D1B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D1B)

    def lambda_7D29():

        label("loc_7D29")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_7D29")

    QueueWorkItem2(0x102, 1, lambda_7D29)

    ChrTalk(    #428
        0x102,
        (
            "#012F...Wait, Estelle.\x02\x03",

            "#015FLeave her be, for now.\x02\x03",

            "The best thing we can do for\x01",
            "her is to save the professor.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #429
        0x101,
        "#007FI know...but I just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x106,
        "#053FTODAY, people...\x02",
    )

    CloseMessageWindow()

    def lambda_7E0E():
        OP_6D(3150, 0, -410, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7E0E)
    TurnDirection(0x106, 0x8, 400)

    def lambda_7E2D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E2D)
    Sleep(50)

    def lambda_7E40():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E40)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #431
        0x106,
        (
            "#054FKilika! You can contact the\x01",
            "army, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x8,
        (
            "#790FYes. May the fortunes of\x01",
            "war smile upon you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x9,
        (
            "#131F#4PIt seems that something major\x01",
            "is going on...\x02\x03",

            "Please, take care of yourselves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 1570, 0, -3490, 180)
    SetChrPos(0x102, 1570, 0, -3490, 180)
    SetChrPos(0x106, 1570, 0, -3490, 180)
    OP_6D(1570, 0, -3490, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_8C(0x9, 0, 400)
    Sleep(500)
    FadeToBright(1000, 0)
    SetChrPos(0x107, 720, 0, -2310, 0)
    OP_28(0x41, 0x1, 0x100)
    OP_28(0x41, 0x1, 0x200)
    RemoveParty(0x6, 0xFF)
    EventEnd(0x0)
    Return()

    # Function_21_6EDD end

    def Function_22_7FCE(): pass

    label("Function_22_7FCE")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(2000, 0, -5200, 0)
    OP_4A(0x8, 255)
    OP_4A(0xA, 0)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, 1440, 0, -6280, 0)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 2400, 0, -5400, 0)
    SetChrPos(0x102, 1300, 0, -5500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #434
        0x101,
        "#001FMorning, Kilika!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    def lambda_806E():
        OP_6D(3600, 0, 600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_806E)

    def lambda_8086():
        OP_8E(0xFE, 0xED8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8086)
    Sleep(300)

    def lambda_80A6():
        OP_8E(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80A6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #436
        0x8,
        (
            "#4P#790FAnd to you both.\x02\x03",

            "Has Zin already left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x102,
        (
            "#010FYes. He took an airliner to\x01",
            "Grancel some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#000FI wish you could have\x01",
            "come to see him off.\x02\x03",

            "Speaking of which, do you two\x01",
            "know each other, somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x8,
        (
            "#4P#792FA bit, quite some time ago.\x02\x03",

            "#790FBut that's beside the point. Have\x01",
            "you noticed the strange current in\x01",
            "the air? The winds are shifting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        (
            "#507FHey, no changing the subject!\x02\x03",

            "#004F...Wait, we are talking about\x01",
            "the weather, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x102,
        (
            "#012FHave you learned something\x01",
            "about that airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x8,
        (
            "#4P#790FNot a thing.\x02\x03",

            "But I believe this disquieting\x01",
            "atmosphere is related to the\x01",
            "Royal Army mobilizing.\x02\x03",

            "For one thing, I've sent a message to the\x01",
            "army headquarters at Leiston Fortress,\x01",
            "but there's been no response.\x02\x03",

            "Secondly, all the mandatory\x01",
            "inspections throughout the\x01",
            "kingdom have been lifted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x101,
        (
            "#009FWhat?!\x01",
            "What's THAT all about?\x02\x03",

            "This isn't about another turf \x01",
            "war, like with the sky bandits,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x102,
        (
            "#013FNo... It would be strange for\x01",
            "them to call off inspections,\x01",
            "if that were the case.\x02\x03",

            "If they had caught the culprits\x01",
            "themselves, surely they would\x01",
            "have sent word around.\x02\x03",

            "#012FMaybe there IS something\x01",
            "in the air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x8,
        (
            "#4P#792FIncidentally, I've not been able to\x01",
            "contact the Intelligence Division\x01",
            "at Leiston Fortress, either.\x02\x03",

            "It is possible that the Royal\x01",
            "Army has some sort of internal\x01",
            "issue going on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x101,
        (
            "#002F'Some sort of'... Oh, WAIT!\x02\x03",

            "The stuff that Dorothy shot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        (
            "#012FThe picture of those guys in\x01",
            "black wearing the Royal Guard\x01",
            "uniforms...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 1440, 0, -6280, 0)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    OP_22(0x6, 0x0, 0x64)

    ChrTalk(    #448
        0xA,
        "#2PSomeone mention my name...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_872A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_872A)

    def lambda_8738():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8738)
    OP_6D(2680, 0, -3240, 1500)

    ChrTalk(    #449
        0x101,
        "#501FDorothy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x102,
        "#010FSpeak of the devil, and yea verily...\x02",
    )

    CloseMessageWindow()

    def lambda_879A():
        OP_6D(3300, 0, -730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_879A)

    def lambda_87B2():

        label("loc_87B2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87B2")

    QueueWorkItem2(0x8, 1, lambda_87B2)

    def lambda_87C3():

        label("loc_87C3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87C3")

    QueueWorkItem2(0x101, 1, lambda_87C3)

    def lambda_87D4():

        label("loc_87D4")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_87D4")

    QueueWorkItem2(0x102, 1, lambda_87D4)
    OP_8E(0xA, 0xECE, 0x0, 0xFFFFF6FA, 0xBB8, 0x0)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #451
        0xA,
        (
            "#152FWow... What an ordeal.\x02\x03",

            "I finally got in touch with\x01",
            "my editor's office, and Nial\x01",
            "happened to be there.\x02\x03",

            "When I told him about giving up\x01",
            "my photo-quartz to the army, he\x01",
            "just about blew his stack!\x02\x03",

            "It's soooooo unfair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x101,
        (
            "#004F#4P...Which means they haven't\x01",
            "given it back yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xA,
        (
            "#154FRight! I mean, how rude is that?\x02\x03",

            "And after I'd gone to the trouble\x01",
            "of going to Leiston Fortress to\x01",
            "get it back, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        (
            "#506F#4PWow...\x01",
            "You've got some fire to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xA,
        (
            "#151FHee hee... Well, I guess I have to\x01",
            "have one redeeming trait, right?\x02\x03",

            "Anyway, I didn't have any other\x01",
            "option but to just take a picture\x01",
            "of the fort for the paper!\x02\x03",

            "It does make for a great shot,\x01",
            "though... It lights up all pretty\x01",
            "at night.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #456
        0x101,
        "#509F#4PYou took a pretty picture. Of the fort.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x102,
        (
            "#014FNot to mention, you're supposed to\x01",
            "obtain permission to photograph any\x01",
            "part of a military installation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xA,
        (
            "#151FCome on... It's not like\x01",
            "it's that big a deal. ㈱\x02\x03",

            "Here, take a look.\x01",
            "I just developed it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C07():
        OP_6D(3600, 0, 600, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C07)
    OP_8E(0xA, 0x1220, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xA, 0x1234, 0x0, 0xFFFFFD3A, 0x7D0, 0x0)
    OP_8C(0x101, 45, 0)
    Sleep(500)
    OP_8C(0x101, 45, 0)
    OP_8C(0x102, 45, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #459
        "\x07\x05Dorothy placed the photo on the counter.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AD(0x40024, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #460
        (
            "#010FHeeey...\x01",
            "That IS a pretty nice shot.\x02\x03",

            "#010FSo this is Leiston Fortress...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #461
        (
            "#006FWow, Dorothy... You've really\x01",
            "got a good eye for this.\x02\x03",

            "#004F...Wait a sec...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #462
        "#014FWhat's wrong, Estelle?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #463
        (
            "#505FIt might be just my imagination,\x01",
            "but do you see anything there,\x01",
            "on the top right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #464
        (
            "#014FWha...\x02\x03",

            "#012F...You're right.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 250, -1, -1)
    SetChrName("Kilika")

    AnonymousTalk(    #465
        (
            "#790FIt's not very clear, but there's\x01",
            "definitely a small shadow there.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("Dorothy")

    AnonymousTalk(    #466
        (
            "#153F*whistles* \x01",
            "You've got a sharp eye, Estelle.\x02\x03",

            "#153FI mean, I took the picture, and\x01",
            "I didn't notice that at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #467
        (
            "#502FHeh heh...\x01",
            "Well, what can I say? ♪\x02\x03",

            "#000FWell, it is just a silhouette.\x01",
            "Maybe it's an army ship?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #468
        (
            "#012F...No. That's no guard ship...\x02\x03",

            "#012FThis is that small airship\x01",
            "from before.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #469
        "#004FBefore...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("Kilika")

    AnonymousTalk(    #470
        (
            "#792FIt's the same silhouette as\x01",
            "the ship that the professor\x01",
            "was taken away in.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #471
        "#013FRight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    SetMessageWindowPos(150, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #472
        "#505FHmmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x56)
    SetMessageWindowPos(150, 400, -1, -1)

    AnonymousTalk(    #473
        "#004F#5SWait, WHAT?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_44(0x8, 0xFF)
    OP_8C(0x8, 180, 0)
    OP_8C(0xA, 270, 0)
    TurnDirection(0x101, 0x102, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #474
        0x101,
        (
            "#005F#4PH-Hold on just one second!\x02\x03",

            "Why would THAT ship be\x01",
            "anywhere near here?\x02\x03",

            "This IS a Royal Army\x01",
            "installation, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #475
        0x102,
        (
            "#015FCalm down, Estelle.\x02\x03",

            "There are plenty of possibilities\x01",
            "to consider before we go jumping\x01",
            "to conclusions.\x02\x03",

            "#012FMaybe we should go straight\x01",
            "to Leiston Fortress and ask\x01",
            "what this is about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x101,
        "#004F#4PWhat?! \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x8,
        (
            "#4P#792FI see. You intend to put it\x01",
            "to them directly. Provoke a\x01",
            "response, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_932E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_932E)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #478
        0x102,
        (
            "#012FDo you think that would\x01",
            "be a bad idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x8,
        (
            "#4P#790FNot at all.\x01",
            "You have my authorization.\x02\x03",

            "This has the potential to\x01",
            "be a huge disaster.\x02\x03",

            "Whatever might be going on\x01",
            "there, this matter must be\x01",
            "handled delicately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x101,
        (
            "#007FEeeep... You're starting to\x01",
            "scare me, Kilika.\x02\x03",

            "#002FBut you're probably right.\x01",
            "We have to handle this\x01",
            "VERY carefully.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94A2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94A2)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #481
        0x101,
        (
            "#002FHey, Dorothy? Can we have\x01",
            "a copy of this picture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xA,
        (
            "#150F#2PSure.\x02\x03",

            "After all, you guys have\x01",
            "done a lot for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x101,
        "#006FThanks! I owe you one!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #484
        "\x07\x00Received \x07\x02Dorothy's Photograph\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x358, 1)

    ChrTalk(    #485
        0x8,
        (
            "#4P#790FIf you intend to go to Leiston Fortress,\x01",
            "you'll need to leave via the east\x01",
            "entrance and take the Ritter Roadway.\x02\x03",

            "#790FWhen you reach the three-way fork in the road,\x01",
            "stay on the northern fork and you'll eventually\x01",
            "wind up in front of the fort's main gate.\x02\x03",

            "Please use the utmost caution.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96DC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96DC)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #486
        0x101,
        "#006FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x102,
        "#010FAcknowledged.\x02",
    )

    CloseMessageWindow()
    OP_28(0x43, 0x4, 0x2)
    OP_28(0x43, 0x4, 0x4)
    OP_28(0x43, 0x1, 0x1)
    OP_28(0x33, 0x4, 0x40)
    OP_4B(0xA, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0xD)
    Return()

    # Function_22_7FCE end

    def Function_23_9743(): pass

    label("Function_23_9743")

    EventBegin(0x0)
    OP_6D(3230, 0, 280, 0)
    AddParty(0x6, 0xFF)
    AddParty(0x5, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 4500, 0, -720, 270)
    SetChrPos(0x101, 3500, 0, -710, 90)
    SetChrPos(0x102, 2390, 0, -700, 90)
    SetChrPos(0x106, 1750, 0, -6420, 0)
    SetChrPos(0x107, 680, 0, -6020, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #488
        0xB,
        (
            "#2P#805FI just can't believe that\x01",
            "Professor Russell is at\x01",
            "Leiston Fortress...\x02\x03",

            "A-Are you absolutely certain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x8,
        (
            "#4P#790FMiss Dorothy's photograph and\x01",
            "the shutdown of orbal power in\x01",
            "the gate...\x02\x03",

            "These two things, combined, make\x01",
            "the conclusion inescapable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xB,
        (
            "#2P#805FB-But the central factory and the Royal Army\x01",
            "have always had excellent relations.\x02\x03",

            "And now I'm expected to believe this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x102,
        (
            "#012FIt's not as if the internal\x01",
            "command structure of the military\x01",
            "is all run by a single entity.\x02\x03",

            "The people who attacked the factory were seen\x01",
            "escaping, and they looked like Royal Guardsmen.\x01",
            "That in itself is a clue.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A39():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9A39)

    def lambda_9A47():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A47)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #492
        0x101,
        "#6P#505FOh, and that would mean...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[The business with the Royal Guardsmen is unrelated?]\x01",      # 0
            "[The Royal Guardsmen are behind the whole thing?]\x01",          # 1
            "[The Royal Guardsmen are being set up?]\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B63"),
        (1, "loc_9C90"),
        (2, "loc_9DA1"),
        (SWITCH_DEFAULT, "loc_9E40"),
    )


    label("loc_9B63")


    ChrTalk(    #493
        0x101,
        (
            "#6P#004FThe business with the Royal\x01",
            "Guardsmen is unrelated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x102,
        (
            "#012FRight... I don't think they\x01",
            "have anything at all to do\x01",
            "with this.\x02\x03",

            "And if we go with that, then\x01",
            "it seems pretty likely that\x01",
            "there's been a frame-up.\x02\x03",

            "This may be some form of internal\x01",
            "conspiracy within the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x43, 0x1)
    Jump("loc_9E40")

    label("loc_9C90")


    ChrTalk(    #495
        0x101,
        (
            "#6P#004FThe Royal Guardsmen are behind\x01",
            "the whole thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x102,
        (
            "#017FWell, it's not outside the\x01",
            "realm of possibility...\x02\x03",

            "#012F...but I think it's more\x01",
            "likely that there's been\x01",
            "some kind of frame-up.\x02\x03",

            "This may be some form of internal\x01",
            "conspiracy within the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E40")

    label("loc_9DA1")


    ChrTalk(    #497
        0x101,
        (
            "#6P#004FThe Royal Guardsmen are being\x01",
            "set up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x102,
        (
            "#012FMy thoughts exactly.\x02\x03",

            "This may be some form of internal\x01",
            "conspiracy within the Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x43, 0x3)
    Jump("loc_9E40")

    label("loc_9E40")


    ChrTalk(    #499
        0xB,
        (
            "#2P#806FMmm... This is unpleasant to\x01",
            "think about.\x02\x03",

            "But how could the professor get\x01",
            "caught up in something like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(100)

    ChrTalk(    #500
        0x106,
        (
            "#2PSounds like you've found a lead on our\x01",
            "friendly neighborhood criminals.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)

    def lambda_9F57():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F57)

    def lambda_9F65():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F65)

    def lambda_9F73():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F73)

    def lambda_9F81():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9F81)

    def lambda_9F8F():
        OP_6D(2020, 0, -2230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F8F)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #501
        0x101,
        "#501FWha... Agate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x102,
        (
            "#010FGood to see you back on\x01",
            "your feet.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9FF2():
        OP_6D(2920, 0, -480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FF2)

    def lambda_A00A():

        label("loc_A00A")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A00A")

    QueueWorkItem2(0xB, 1, lambda_A00A)

    def lambda_A01B():

        label("loc_A01B")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A01B")

    QueueWorkItem2(0x101, 1, lambda_A01B)

    def lambda_A02C():

        label("loc_A02C")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_A02C")

    QueueWorkItem2(0x102, 1, lambda_A02C)

    def lambda_A03D():
        OP_8E(0xFE, 0xDD4, 0x0, 0xFFFFF8B2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A03D)
    Sleep(300)

    def lambda_A05D():
        OP_8E(0xFE, 0x988, 0x0, 0xFFFFF920, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A05D)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #503
        0x106,
        (
            "#552FYeah, I just woke up a few\x01",
            "minutes ago.\x02\x03",

            "It was a little weird, waking up\x01",
            "in a strange place after being\x01",
            "put to bed like some baby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x101,
        (
            "#008F#4POh, for the love of... Everyone\x01",
            "was worried about you, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x102,
        (
            "#010FAre you sure you're okay with\x01",
            "moving around so soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0x106,
        (
            "#051FYeah... Sleeping so damn much\x01",
            "didn't give me any other option\x01",
            "than to recover.\x02\x03",

            "I'm feeling pretty much back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #507
        0x107,
        (
            "#065F#3PB-But, Agate... You should\x01",
            "probably rest some more...\x02\x03",

            "You just got the poison out of\x01",
            "your system, and the doctor\x01",
            "said--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #508
        0x106,
        (
            "#2P#551FI just said, I'm fine.\x02\x03",

            "I've been training for years.\x01",
            "It's not that rough on someone\x01",
            "like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x107,
        "#069F#3PMmm... *sniffle*...\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #510
        0x106,
        (
            "#2P#055FAll right, all right! I get it!\x02\x03",

            "I won't overdo it or anything\x01",
            "until I'm back to normal. That\x01",
            "cool with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x107,
        "#067F#3PHee hee... Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x106,
        "#2P#552FDamn kids...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        (
            "#001F#4PHa ha ha... Even the mighty\x01",
            "Agate is no match for Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x102,
        (
            "#019FI guess it's hard to say no to someone\x01",
            "who's kept a constant vigil over you\x01",
            "and nursed you back to health.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #515
        0x106,
        (
            "#551FAhh, shut up.\x02\x03",

            "#051FGetting back to the point... It\x01",
            "looks like a lot's been going on\x01",
            "while I've been out of commission.\x02\x03",

            "Mind filling me in on\x01",
            "the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x101,
        "#006F#4PSure.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #517
        (
            "\x07\x05Estelle explained that all signs pointed to Professor Russell being held\x01",
            "captive at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #518
        0x107,
        (
            "#065FI still can't believe that\x01",
            "Grandpa's in there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x106,
        (
            "#552FI wouldn't have thought those\x01",
            "goons in the black clothes\x01",
            "were army types, either...\x02\x03",

            "#053FHeh... And suddenly, I'm\x01",
            "feeling better than ever.\x02\x03",

            "What say we go and settle\x01",
            "our debts right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x101,
        "#002F#4P'Settle our debts'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x106,
        (
            "#057FAin't it obvious? We sneak\x01",
            "into Leiston Fortress.\x02\x03",

            "We'll bust the prof out, and\x01",
            "they'll never know what hit\x01",
            "'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x101,
        (
            "#006F#4PAhh, okay. Like settling\x01",
            "everything in one big stroke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x8,
        "#790FI'm afraid it's not that simple.\x02",
    )

    CloseMessageWindow()

    def lambda_A83E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A83E)

    def lambda_A84C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A84C)

    def lambda_A85A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A85A)

    def lambda_A868():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A868)
    Sleep(500)

    ChrTalk(    #524
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x8,
        (
            "#792FThe Bracer Guild has a long-standing policy of\x01",
            "non-intervention when it comes to a nation's\x01",
            "military.\x02\x03",

            "Article Three of the guild code:\x01",
            "'Bracers and Non-Involvement in Military or\x01",
            "Political Matters.'\x02\x03",

            "'A bracer will recognize a nation's sovereignty,\x01",
            "and may not interfere with nor arrest any person\x01",
            "of national military or political standing.'\x02\x03",

            "#790FOr to put it more simply, as long as the\x01",
            "army is playing dumb about this, our hands are\x01",
            "tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0x106,
        "#552FOh, you've gotta be kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x101,
        (
            "#005FNo way...\x01",
            "That doesn't make sense!\x02\x03",

            "You mean that we can witness a crime, but if\x01",
            "it's done by a soldier or a politician, we\x01",
            "just have to pretend we didn't see anything?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0x8,
        (
            "#791FEssentially, yes. There is, however, a\x01",
            "loophole.\x02\x03",

            "Article Two of the guild code:\x01",
            "'Bracers and Their Duty to the People.'\x02\x03",

            "'In the event of unjust imperilment of citizens,\x01",
            "the bracer's sworn duty is to bear the\x01",
            "responsibility for the citizen(s)' safety.'\x02\x03",

            "#792FDo you understand the significance of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0x102,
        (
            "#010FI see... The professor's not\x01",
            "a politician or a soldier.\x02\x03",

            "He's a civilian, whom we're\x01",
            "sworn to protect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #530
        0x101,
        "#501FS-So then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x8,
        (
            "#790FThe rest hinges upon you, Mr. Murdock.\x02\x03",

            "In this case, we are obligated to oppose\x01",
            "the Royal Army and save Professor Russell.\x01",
            "Will you help us?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD85():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD85)

    def lambda_AD93():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD93)

    def lambda_ADA1():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_ADA1)
    TurnDirection(0x107, 0xB, 400)

    ChrTalk(    #532
        0xB,
        (
            "#803F...Stupid question.\x02\x03",

            "The factory needs him... Ah, \x01",
            "hell, all of Liberl needs him.\x02\x03",

            "#800FGo and get him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x107,
        (
            "#560F#3PMr. Murdock! Thank you,\x01",
            "thank you, THANK YOU!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x107, 400)

    ChrTalk(    #534
        0xB,
        (
            "#801FNo need to thank me. I owe\x01",
            "Professor Russell for all\x01",
            "he's taught me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0x8,
        (
            "#792FAnd so we have adequate\x01",
            "justification to proceed.\x02\x03",

            "Bracers Agate, Estelle and Joshua...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF1B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AF1B)

    def lambda_AF29():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF29)

    def lambda_AF37():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF37)

    def lambda_AF45():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AF45)

    def lambda_AF53():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AF53)
    Sleep(500)

    ChrTalk(    #536
        0x8,
        (
            "#791FYou are hereby ordered to proceed\x01",
            "to Leiston Fortress and rescue\x01",
            "Professor Russell.\x02\x03",

            "It is not as above-board as you may\x01",
            "be accustomed to, but it is the request\x01",
            "of the Bracer Guild, nevertheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0x101,
        "#508FNow you're talking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0x102,
        "#010FAcknowledged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #539
        0x106,
        (
            "#051FHeh. Bring it on!\x02\x03",

            "If we're doing this, we have to\x01",
            "figure out how we're getting in\x01",
            "there.\x02\x03",

            "Leiston Fortress is pretty damned\x01",
            "famous for being impossible to\x01",
            "break into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0x102,
        (
            "#012FThat's true. It's easy to say we're going\x01",
            "to do it, but putting it into practice is\x01",
            "going to take some serious planning.\x02\x03",

            "There has to be some way of getting\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0x8,
        (
            "#792FUnfortunately, the security there is\x01",
            "nigh unto perfect.\x02\x03",

            "Approaching from the lake would likely\x01",
            "be impossible, since it's monitored by\x01",
            "a network of orbal sensors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0x106,
        "#552FHeh... I figured as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x102,
        (
            "#012FAnd a frontal assault would\x01",
            "be tantamount to suicide.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #544
        0x101,
        (
            "#501F#3PHey, Mr. Murdock?\x02\x03",

            "You know that orange airship\x01",
            "that goes to Leiston Fortress?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B35C():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B35C)

    def lambda_B36A():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B36A)

    def lambda_B378():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B378)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #545
        0xB,
        (
            "#802FYes...\x01",
            "That's the Leibnitz.\x02\x03",

            "It makes periodic stops to inspect\x01",
            "the equipment at the fort to make\x01",
            "sure it's performing properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #546
        0x101,
        (
            "#006F#3PIs there any way we could sneak\x01",
            "into the fortress on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xB,
        (
            "#805FNo. All of the crew members go\x01",
            "through a thorough security\x01",
            "check as soon as they land.\x02\x03",

            "It'd be impossible to just\x01",
            "sneak away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0x106,
        (
            "#050FHow about stowing away\x01",
            "in the cargo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0xB,
        (
            "#800FNo good. Each container is scanned\x01",
            "with a bio-sensor for living creatures,\x01",
            "and they check each and every one.\x02\x03",

            "Plus, those sensors were designed\x01",
            "by Professor Russell himself.\x02\x03",

            "They can even pick up one\x01",
            "little mouse in a huge mass of stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x101,
        "#007F#3PHmmm... Well, damn.\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #551
        0x107,
        "#064F...Oh!\x02",
    )

    CloseMessageWindow()

    def lambda_B65E():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B65E)

    def lambda_B66C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B66C)

    def lambda_B67A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B67A)

    ChrTalk(    #552
        0x101,
        "#002F#4PWhat is it, sweetie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0x107,
        (
            "#560FDon't you remember?!\x02\x03",

            "Grandpa's invention! From when\x01",
            "I was showing you around!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0x101,
        (
            "#505F#4PLemme think...\x02\x03",

            "#004F...AH-HA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0x102,
        (
            "#4P#010FWhen we were helping with the\x01",
            "experiments on a new type of\x01",
            "orbment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x107,
        (
            "#061FYeah!\x02\x03",

            "It produces a force field that\x01",
            "can disrupt the bio-sensors!\x02\x03",

            "We've already tested that it works,\x01",
            "so everything will be fine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x106,
        "#2P#054FWha... Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0xB,
        (
            "#803FI had no idea the professor had\x01",
            "ever made anything like that...\x02\x03",

            "#800FWhere is this device, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x107,
        (
            "#560FI guess it must be right where\x01",
            "he left it, in his laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x8,
        (
            "#791FThen we have no time to lose.\x01",
            "Hurry and retrieve this device.\x02\x03",

            "In the meantime, I will gather\x01",
            "and collate whatever data I\x01",
            "can on Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #561
        0x106,
        "#051FGot it. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #562
        0x8,
        (
            "#791FI'll leave the arrangement of\x01",
            "a delivery via the Leibnitz\x01",
            "to you, Mr. Murdock.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 400)

    ChrTalk(    #563
        0xB,
        (
            "#804FA-All right. I'll talk to Gustav.\x02\x03",

            "Just come to the airfield when\x01",
            "you're ready!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x20)
    OP_28(0x43, 0x1, 0x40)

    def lambda_BA6B():

        label("loc_BA6B")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA6B")

    QueueWorkItem2(0x101, 1, lambda_BA6B)

    def lambda_BA7C():

        label("loc_BA7C")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA7C")

    QueueWorkItem2(0x102, 1, lambda_BA7C)

    def lambda_BA8D():

        label("loc_BA8D")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA8D")

    QueueWorkItem2(0x106, 1, lambda_BA8D)

    def lambda_BA9E():

        label("loc_BA9E")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_BA9E")

    QueueWorkItem2(0x107, 1, lambda_BA9E)
    OP_8C(0xB, 180, 400)
    OP_8E(0xB, 0x114E, 0x0, 0xFFFFF4AC, 0xFA0, 0x0)
    OP_8E(0xB, 0x65E, 0x0, 0xFFFFE80E, 0xFA0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_BAE3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BAE3)
    OP_8E(0xB, 0x6F4, 0x0, 0xFFFFE1BA, 0xFA0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xB, 0x4)
    OP_8E(0xB, 0x780, 0xFFFFFE0C, 0xFFFFDBB6, 0xFA0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_23_9743 end

    def Function_24_BB38(): pass

    label("Function_24_BB38")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrPos(0x101, 1520, 0, -4610, 0)
    SetChrPos(0x102, 2390, 0, -5240, 0)
    SetChrPos(0x106, 640, 0, -5220, 0)
    SetChrPos(0x107, 1640, 0, -5990, 0)
    OP_4A(0x8, 255)
    OP_6D(2370, 0, -2250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #564
        0x101,
        (
            "#006FWe're back, Kilika!\x01",
            "And we have the device!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BBDE():
        OP_6D(3130, 0, 650, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BBDE)

    def lambda_BBF6():
        OP_8E(0xFE, 0xE2E, 0x0, 0xFFFFFD1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BBF6)
    Sleep(300)

    def lambda_BC16():
        OP_8E(0xFE, 0x104A, 0x0, 0xFFFFF916, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC16)
    Sleep(300)

    def lambda_BC36():
        OP_8E(0xFE, 0xB04, 0x0, 0xFFFFFA92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_BC36)
    Sleep(300)

    def lambda_BC56():
        OP_8E(0xFE, 0xC30, 0x0, 0xFFFFF6DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_BC56)

    def lambda_BC71():

        label("loc_BC71")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC71")

    QueueWorkItem2(0x101, 1, lambda_BC71)

    def lambda_BC82():

        label("loc_BC82")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC82")

    QueueWorkItem2(0x102, 1, lambda_BC82)

    def lambda_BC93():

        label("loc_BC93")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BC93")

    QueueWorkItem2(0x107, 1, lambda_BC93)

    def lambda_BCA4():

        label("loc_BCA4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_BCA4")

    QueueWorkItem2(0x106, 1, lambda_BCA4)
    WaitChrThread(0x106, 0x2)

    ChrTalk(    #565
        0x8,
        (
            "#790FI have also finished my preparations.\x02\x03",

            "Now, what I am about to show\x01",
            "you is not to be spoken of\x01",
            "to anyone else.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #566
        "\x07\x00Received \x07\x02Leiston Fortress Map\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x359, 1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_AD(0x40025, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #567
        "#051FHeh! Well, would you look at that.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #568
        (
            "#014FThese are the schematics for\x01",
            "Leiston Fortress?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 350, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #569
        (
            "#064FWow... It sure is big.\x02\x03",

            "#062FAnd Grandpa's in there somewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #570
        (
            "#509FIsn't the layout of the\x01",
            "fort a military secret?\x02\x03",

            "How'd the guild get its\x01",
            "hands on it?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 0, -1, -1)
    SetChrName("Kilika")

    AnonymousTalk(    #571
        (
            "#792FThe guild has ways of obtaining\x01",
            "information. It is best that you not know.\x02\x03",

            "#790FThe Bracer Guild is a much more complex\x01",
            "organization than it may appear, and you would\x01",
            "do well to remember that.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #572
        "#004FO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #573
        0x8,
        (
            "#790FI don't think I need to remind\x01",
            "you that this is an exceptionally unique case.\x02\x03",

            "Relations between the army and the guild have\x01",
            "traditionally been excellent in Liberl, even\x01",
            "relative to other surrounding nations.\x02\x03",

            "It is absolutely crucial that we not cause any\x01",
            "ill will. The guild can ill afford hostilities\x01",
            "with the army.\x02\x03",

            "Do I make myself clear, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0x106,
        (
            "#053FHeh. Yeah, I guess.\x02\x03",

            "#057FBut if I see the men in black clothes,\x01",
            "they're going to have a hot date with\x01",
            "the business end of my sword.\x02\x03",

            "Soldiers or not, I've been looking for\x01",
            "them so long now that I think they'd be\x01",
            "offended if I DIDN'T kick their asses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #575
        0x8,
        (
            "#790FDo what you must. I just ask\x01",
            "that you take no lives.\x02\x03",

            "#792FEstelle and Joshua.\x02\x03",

            "Legally, I should not entrust\x01",
            "a task like this to junior\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #576
        0x101,
        (
            "#005FWhoa, whoa, wait a second!\x01",
            "I don't like what you're\x01",
            "driving at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0x102,
        (
            "#012FWe're already a part of this.\x01",
            "Please, allow us to see it\x01",
            "through to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0x8,
        (
            "#791FI thought you might say that,\x01",
            "and I don't intend to stand\x01",
            "in your way.\x02\x03",

            "But it must be said that\x01",
            "you answer to Zeiss.\x02\x03",

            "As such, if worse comes to worst, I\x01",
            "will accept full responsibility for\x01",
            "your actions. You needn't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0x101,
        "#003FK-Kilika...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #580
        0x102,
        (
            "#015FI'm sorry... We've caused\x01",
            "so much trouble for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x8,
        (
            "#790FNow, then...Tita.\x02\x03",

            "Since you're not a bracer, I\x01",
            "have no authority over you...\x02\x03",

            "...but are you truly set in\x01",
            "your course?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #582
        0x107,
        (
            "#064FI...\x02\x03",

            "#062FYes, ma'am. I am.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5AB():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5AB)

    def lambda_C5B9():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5B9)

    def lambda_C5C7():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C5C7)
    OP_6D(3240, 0, -550, 1000)

    ChrTalk(    #583
        0x101,
        (
            "#004F#4PWh-What?\x01",
            "What's this all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #584
        0x102,
        "#014F#4PYou don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0x107,
        (
            "#063FUmm...\x02\x03",

            "I'm the only one who knows\x01",
            "how to operate the device.\x02\x03",

            "So...I'm going with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x101,
        "#004F#4PWhat?! \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0x102,
        "#012F#4PWell, it is a very complicated orbment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0x107,
        (
            "#562FI'm sorry...\x02\x03",

            "I don't want to cause any trouble,\x01",
            "but I have to go, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #589
        0x106,
        "#552F#4PYou gotta be shittin' me.\x02",
    )

    CloseMessageWindow()

    def lambda_C759():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C759)

    def lambda_C767():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C767)
    TurnDirection(0x107, 0x106, 400)
    Sleep(400)

    ChrTalk(    #590
        0x106,
        (
            "#057F#4PListen, pipsqueak.\x01",
            "I ain't hearin' this crap.\x02\x03",

            "What the hell are we supposed\x01",
            "to do with a kid on a mission\x01",
            "this dangerous, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #591
        0x107,
        (
            "#065FB-But...\x02\x03",

            "You need me to operate\x01",
            "the device...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0x106,
        (
            "#054F#4PThen forget that idea!\x02\x03",

            "We'll find another way to\x01",
            "sneak in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0x101,
        (
            "#002F#4P...\x02\x03",

            "#007FAll right, enough. Lighten up.\x02\x03",

            "Why are you so damned stubborn?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(    #594
        0x106,
        "#055F#6PYou wanna run that by me again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0x101,
        (
            "#009F#4PTita's ready, and she said\x01",
            "she wants to help.\x02\x03",

            "And her help will make it\x01",
            "easier for us to sneak in.\x02\x03",

            "All that improves our chances of\x01",
            "getting the professor out safely.\x02\x03",

            "I want to know why you're so\x01",
            "against it NOW, of all times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #596
        0x106,
        (
            "#057F#6PYou little...\x02\x03",

            "Have you even thought about her being\x01",
            "a civilian? And a KID, besides? And\x01",
            "you're okay with putting her in danger?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #597
        0x101,
        (
            "#006F#4PI don't like it any more than you\x01",
            "do, but we'll keep her safe.\x02\x03",

            "We're bracers. That's our job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #598
        0x106,
        (
            "#552F#6P...\x02\x03",

            "You sure talk a big game,\x01",
            "for a rookie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #599
        0x102,
        (
            "#015F#4PAnd what does experience\x01",
            "have to do with this?\x02\x03",

            "Bracers aren't the only ones\x01",
            "who feel that some people are\x01",
            "worth protecting.\x02\x03",

            "#010FIsn't supporting that ideal what\x01",
            "we're supposed to be all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #600
        0x106,
        "#057F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #601
        0x107,
        (
            "#065FEstelle... Joshua...\x02\x03",

            "#562FU-Umm...Agate...? I'm sorry\x01",
            "that I make you so mad.\x02\x03",

            "But my grandpa is everything\x01",
            "to me.\x02\x03",

            "All I want is for him to be okay...\x02\x03",

            "...so I'm going to do everything\x01",
            "I can to make sure he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #602
        0x106,
        "#552F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0x107,
        (
            "#063FBesides, you helped me\x01",
            "when I needed it...\x02\x03",

            "So let me do the same for\x01",
            "Estelle and Joshua...and\x01",
            "for you.\x02\x03",

            "I swear that I'll be good...\x01",
            "and I'll follow orders.\x02\x03",

            "#068FPlease...\x01",
            "I'm begging you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0x101,
        "#008F#4POh, sweetie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0x102,
        (
            "#010F#4PI didn't realize you'd put\x01",
            "so much thought into this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #606
        0x106,
        "#053F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #607
        0x106,
        (
            "#057F#4PHmph. I don't buy it.\x02\x03",

            "If you really want to help us that badly,\x01",
            "without getting in our way...then follow\x01",
            "orders, and stay here. You got it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #608
        0x107,
        "#562F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #609
        0x106,
        (
            "#552F#4PBut we really don't have any\x01",
            "other way to get in there...\x02\x03",

            "I'd rather not do this.\x02\x03",

            "#053FTruth be told, I can think of a few\x01",
            "thousand things I'd RATHER do, but\x01",
            "I'll let it slide, this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0x107,
        (
            "#560FI...\x02\x03",

            "#067FThank you, Agate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #611
        0x106,
        (
            "#051F#4PYou got no reason to thank me.\x02\x03",

            "You fall behind, you get\x01",
            "LEFT behind.\x02\x03",

            "Just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #612
        0x107,
        "#560FA-All right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #613
        0x101,
        (
            "#509F#4PI swear, one of these days...\x01",
            "By the GODDESS, you're a jerk!\x02\x03",

            "Why can't you just be nice and\x01",
            "appreciate what she's saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #614
        0x102,
        (
            "#019F#4PSettle down, Estelle.\x02\x03",

            "He's just the type who speaks, ah...\x01",
            "'colorfully' when he's embarrassed.\x01",
            "It's a defense mechanism.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(    #615
        0x106,
        "#055F#6PBoth of you, SHUT IT.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #616
        0x107,
        "#067F*giggle*\x02",
    )

    CloseMessageWindow()

    def lambda_D1C6():
        OP_6D(3130, 0, 650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D1C6)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #617
        0x8,
        (
            "#792FHa ha... Now, I trust that\x01",
            "the matter has been settled.\x02\x03",

            "#791FThe Leibnitz will soon\x01",
            "be ready to set off.\x02\x03",

            "When you are ready, please\x01",
            "proceed to the airfield.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D28C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D28C)

    def lambda_D29A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D29A)

    def lambda_D2A8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_D2A8)
    TurnDirection(0x107, 0x8, 400)
    Sleep(400)

    ChrTalk(    #618
        0x101,
        "#006FWill do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #619
        0x106,
        (
            "#051FLater, Kilika. Take care of\x01",
            "talking with the army for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #620
        0x8,
        (
            "#791FI have appropriate responses\x01",
            "lined up, should they decide\x01",
            "to question us.\x02\x03",

            "Aidios keep you.\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x200)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_24_BB38 end

    def Function_25_D399(): pass

    label("Function_25_D399")

    EventBegin(0x0)
    OP_6D(3310, 0, -200, 0)
    OP_67(0, 6580, -10000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x101, 2770, 0, -720, 0)
    SetChrPos(0x102, 4310, 0, -890, 0)
    SetChrPos(0xB, 3260, 0, -2080, 0)
    ClearChrFlags(0xB, 0x80)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0xB, 0x8, 0)
    OP_4A(0x8, 255)
    OP_3F(0x35A, 1)
    OP_3F(0x362, 1)
    OP_3F(0x364, 1)
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

    ChrTalk(    #621
        0xB,
        (
            "#803FSo you were able to get the\x01",
            "professor out safely...?\x02\x03",

            "And you even got the logic\x01",
            "unit back. I don't even have\x01",
            "the words...\x02\x03",

            "#800FThank you...both of you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #622
        0x101,
        (
            "#506F#4PWell, we didn't really do\x01",
            "all that much.\x02\x03",

            "Really, we were just there\x01",
            "as backup for Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0x102,
        (
            "#010F#4PIf you really want to express your gratitude,\x01",
            "I'd suggest you direct it toward him, since\x01",
            "he kept the professor safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #624
        0xB,
        (
            "#805FI certainly will.\x02\x03",

            "It'll be nice when all this\x01",
            "craziness ends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0x8,
        (
            "#792FAll we can do now is put\x01",
            "our faith in Agate.\x02\x03",

            "#790FIt does seem that Colonel\x01",
            "Richard has something in\x01",
            "mind for Grancel, however.\x02\x03",

            "He means to use that black\x01",
            "orbment...that thing he called\x01",
            "the 'Gospel.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #626
        0x101,
        (
            "#007F#4PYeah... I don't know exactly\x01",
            "what it's used for...\x02\x03",

            "But we've been asked by the professor\x01",
            "to talk to Her Majesty about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #627
        0xB,
        (
            "#803FOuch. That's when you know things\x01",
            "have gotten very, very serious.\x02\x03",

            "#800FI'm pretty sure that the professor\x01",
            "is on good terms with her.\x02\x03",

            "It's not unusual for him to \x01",
            "have access to top secret\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #628
        0x102,
        (
            "#012FAnyway, that's the gist of our\x01",
            "request from him. Unlikely as\x01",
            "it sounds.\x02\x03",

            "#012FKilika? Do you think it would\x01",
            "be safe for us to go to Grancel,\x01",
            "given the current climate?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D923():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D923)

    ChrTalk(    #629
        0x8,
        (
            "#792FThere's currently no evidence to suggest\x01",
            "that you were involved with the security\x01",
            "breach at the fort, so it should be fine.\x02\x03",

            "#790FIndeed, I'd advise you to go there\x01",
            "before a full investigation is begun.\x02\x03",

            "It's quite likely that a thorough\x01",
            "search of the central factory\x01",
            "will be performed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #630
        0xB,
        (
            "#806FAgreed. Which means that now's\x01",
            "the time to figure out what to\x01",
            "do about it.\x02\x03",

            "#800FI wish both of you the best\x01",
            "of luck on your journey.\x02\x03",

            "Please be sure to deliver\x01",
            "the professor's message.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DB1E():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB1E)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #631
        0x101,
        (
            "#006F#4PYou can count on us! Consider\x01",
            "it in Her Majesty's hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #632
        0x102,
        (
            "#012F#4PTake care of yourself,\x01",
            "Mr. Murdock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #633
        0xB,
        (
            "#801FYeah... Now's not the time\x01",
            "to let my guard down with\x01",
            "the army around.\x02\x03",

            "So I'll be off now.\x01",
            "Safe journey to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 400)
    OP_8E(0xB, 0x60E, 0x0, 0xFFFFE796, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_DC44():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DC44)
    OP_8E(0xB, 0x690, 0x0, 0xFFFFE053, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #634
        0x101,
        (
            "#006FWell, then... I guess there's\x01",
            "no time like the present, huh?\x02\x03",

            "We should try to get an \x01",
            "audience with Her Majesty,\x01",
            "as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #635
        0x102,
        (
            "#010F#4PIf that's the plan, we need to\x01",
            "take the next airliner out.\x02\x03",

            "It would take us half a day to reach\x01",
            "Grancel on foot. An airship would\x01",
            "only take an hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #636
        0x101,
        (
            "#505FYeah, that's true...\x02\x03",

            "I kinda thought it'd be cool\x01",
            "to walk all the way around\x01",
            "the kingdom, but oh, well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #637
        0x8,
        (
            "#790FAll right.\x01",
            "Wait just a moment.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DE55():
        OP_6D(3570, 0, 620, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DE55)

    def lambda_DE6D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE6D)

    def lambda_DE7B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE7B)
    OP_8E(0x8, 0x14E6, 0x0, 0x4C4, 0x7D0, 0x0)

    def lambda_DE9D():

        label("loc_DE9D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DE9D")

    QueueWorkItem2(0x101, 1, lambda_DE9D)

    def lambda_DEAE():

        label("loc_DEAE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_DEAE")

    QueueWorkItem2(0x102, 1, lambda_DEAE)
    OP_8E(0x8, 0x1504, 0x0, 0x9C4, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(    #638
        0x8,
        (
            "#792FBracer Guild...\x02\x03",

            "Good afternoon.\x01",
            "Always a pleasure.\x02\x03",

            "Yes...\x01",
            "If you would, please.\x02\x03",

            "Two to Grancel... Right... Yes,\x01",
            "bill it to the usual account.\x02\x03",

            "#791FThank you. Goodbye.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(300)
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x13B0, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #639
        0x101,
        (
            "#501F...?\x01",
            "What was that all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #640
        0x102,
        (
            "#010F#3PWas that the reception\x01",
            "desk at the terminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #641
        0x8,
        (
            "#791F#4PYes. You now have guaranteed seats\x01",
            "on a Grancel-bound airliner.\x02\x03",

            "We are paying your way, so all\x01",
            "you need to do is check in.\x02\x03",

            "Also, take this with you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #642
        "\x07\x00Received \x07\x02Recommendation\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33A, 1)

    ChrTalk(    #643
        0x101,
        "#004FWhoa, wait, what?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #644
        0x102,
        (
            "#019F#3PTh-This really isn't necessary...\x01",
            "You've already done so much\x01",
            "for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #645
        0x8,
        (
            "#791F#4PThe tickets are simply a business\x01",
            "expense, related to delivering\x01",
            "the professor's message.\x02\x03",

            "The letter of recommendation is\x01",
            "for the superlative job you did\x01",
            "in rescuing the professor.\x02\x03",

            "Accept it, and be proud of\x01",
            "what you've accomplished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #646
        0x101,
        (
            "#008FR-Right!\x02\x03",

            "Thank you, Kilika!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x41, 0x4, 0x10)
    OP_28(0x43, 0x4, 0x10)
    Sleep(100)
    OP_AF(0x40, 0x41)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(100)
    OP_AF(0x40, 0x43)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #647
        0x102,
        "#010F#3PThank you...for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #648
        0x8,
        (
            "#792F#4PHa ha... I believe I said before\x01",
            "that this is simply my duty.\x02\x03",

            "#791FNow...your flight leaves at 11:00.\x02\x03",

            "You'll want to get to the\x01",
            "terminal before then, so as\x01",
            "to have time to check in.\x02\x03",

            "Aidios keep you.\x01",
            "Be well in your travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #649
        0x101,
        "#006FWe will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #650
        0x102,
        "#010F#3PThank you, again...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x601)
    OP_28(0x54, 0x1, 0x1)
    OP_28(0x42, 0x4, 0x10)
    OP_28(0x42, 0x4, 0x20)
    OP_28(0x44, 0x4, 0x10)
    OP_28(0x44, 0x4, 0x20)
    OP_28(0x2B, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E502")
    OP_28(0x2D, 0x4, 0x40)

    label("loc_E502")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E510")
    OP_28(0x2E, 0x4, 0x40)

    label("loc_E510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E51E")
    OP_28(0x2F, 0x4, 0x40)

    label("loc_E51E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E52C")
    OP_28(0x30, 0x4, 0x40)

    label("loc_E52C")

    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_25_D399 end

    def Function_26_E533(): pass

    label("Function_26_E533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E550")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_E56D")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0x34, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E588")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_E5A3")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_E5BE")
    OP_2A(0x2D, 0x32, 0x2A, 0x28, 0x2B, 0x2C, 0x33, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_E5D1")
    OP_2A(0x2D, 0x32, 0x2A, 0xFFFF)
    Jump("loc_E5DF")

    label("loc_E5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E5DF")
    OP_2A(0x2D, 0x32, 0xFFFF)

    label("loc_E5DF")

    TalkEnd(0xFF)
    Return()

    # Function_26_E533 end

    SaveToFile()

Try(main)
