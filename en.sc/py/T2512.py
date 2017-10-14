from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Argyle',                               # 9
        'Dennis',                               # 10
        'Felicity',                             # 11
        'Reina',                                # 12
        'Alice',                                # 13
        'Monika',                               # 14
        'Ms. Millia',                           # 15
        'Mickey',                               # 16
        'Enhanced Jaeger',                      # 17
        'Enhanced Jaeger',                      # 18
        'Enhanced Jaeger',                      # 19
        'Enhanced Jaeger',                      # 20
        'Rhody',                                # 21
        'Roy',                                  # 22
        'Janitor Parkes',                       # 23
        'Taylor',                               # 24
        'Nikita',                               # 25
        'Targeting Camera',                     # 26
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
        'ED6_DT07/CH01360 ._CH',             # 00
        'ED6_DT07/CH01363 ._CH',             # 01
        'ED6_DT07/CH01090 ._CH',             # 02
        'ED6_DT07/CH01370 ._CH',             # 03
        'ED6_DT26/CH20208 ._CH',             # 04
        'ED6_DT07/CH01360 ._CH',             # 05
        'ED6_DT07/CH01580 ._CH',             # 06
        'ED6_DT26/CH20441 ._CH',             # 07
        'ED6_DT07/CH01370 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01430 ._CH',             # 0A
        'ED6_DT07/CH01080 ._CH',             # 0B
        'ED6_DT26/CH20501 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01360P._CP',             # 00
        'ED6_DT07/CH01363P._CP',             # 01
        'ED6_DT07/CH01090P._CP',             # 02
        'ED6_DT07/CH01370P._CP',             # 03
        'ED6_DT26/CH20208P._CP',             # 04
        'ED6_DT07/CH01360P._CP',             # 05
        'ED6_DT07/CH01580P._CP',             # 06
        'ED6_DT26/CH20441P._CP',             # 07
        'ED6_DT07/CH01370P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01430P._CP',             # 0A
        'ED6_DT07/CH01080P._CP',             # 0B
        'ED6_DT26/CH20501P._CP',             # 0C
    )

    DeclNpc(
        X                   = -30910,
        Z                   = 0,
        Y                   = 25940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -28980,
        Z                   = 0,
        Y                   = 970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -60900,
        Z                   = 0,
        Y                   = -2690,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -61500,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -60440,
        Z                   = 0,
        Y                   = 30850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -62350,
        Z                   = 0,
        Y                   = 25980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -31110,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -28350,
        Z                   = 0,
        Y                   = 29790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -29450,
        Z                   = 0,
        Y                   = 30290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -30710,
        Z                   = 0,
        Y                   = 28800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -30900,
        Z                   = 300,
        Y                   = 29850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -60450,
        Z                   = 0,
        Y                   = 28840,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -61710,
        Z                   = 0,
        Y                   = 29010,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -29730,
        TriggerZ            = 0,
        TriggerY            = 30330,
        TriggerRange        = 400,
        ActorX              = -31730,
        ActorZ              = 1500,
        ActorY              = 30100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_376",          # 00, 0
        "Function_1_62F",          # 01, 1
        "Function_2_6E1",          # 02, 2
        "Function_3_1611",         # 03, 3
        "Function_4_169C",         # 04, 4
        "Function_5_192C",         # 05, 5
        "Function_6_1B10",         # 06, 6
        "Function_7_1EAD",         # 07, 7
        "Function_8_223D",         # 08, 8
        "Function_9_231A",         # 09, 9
        "Function_10_2361",        # 0A, 10
        "Function_11_23F1",        # 0B, 11
        "Function_12_2513",        # 0C, 12
        "Function_13_2688",        # 0D, 13
        "Function_14_2817",        # 0E, 14
        "Function_15_291C",        # 0F, 15
        "Function_16_2921",        # 10, 16
        "Function_17_29CA",        # 11, 17
        "Function_18_2E56",        # 12, 18
        "Function_19_2F3D",        # 13, 19
        "Function_20_3013",        # 14, 20
        "Function_21_30E3",        # 15, 21
        "Function_22_319E",        # 16, 22
        "Function_23_3223",        # 17, 23
        "Function_24_327B",        # 18, 24
        "Function_25_32D4",        # 19, 25
        "Function_26_32DD",        # 1A, 26
        "Function_27_36D9",        # 1B, 27
        "Function_28_3835",        # 1C, 28
        "Function_29_3884",        # 1D, 29
        "Function_30_38D3",        # 1E, 30
        "Function_31_3922",        # 1F, 31
        "Function_32_3971",        # 20, 32
        "Function_33_4369",        # 21, 33
        "Function_34_4394",        # 22, 34
        "Function_35_43C6",        # 23, 35
        "Function_36_43F1",        # 24, 36
        "Function_37_441C",        # 25, 37
        "Function_38_4442",        # 26, 38
        "Function_39_4472",        # 27, 39
        "Function_40_447B",        # 28, 40
        "Function_41_499E",        # 29, 41
        "Function_42_4B02",        # 2A, 42
        "Function_43_4B60",        # 2B, 43
        "Function_44_4BB9",        # 2C, 44
        "Function_45_4C12",        # 2D, 45
        "Function_46_4C6B",        # 2E, 46
        "Function_47_519F",        # 2F, 47
        "Function_48_51D1",        # 30, 48
        "Function_49_5203",        # 31, 49
        "Function_50_5235",        # 32, 50
    )


    def Function_0_376(): pass

    label("Function_0_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -160, 0, -940, 10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xF, -27860, 0, 27430, 328)
    Jump("loc_548")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 2)), scpexpr(EXPR_END)), "loc_48C")
    SetChrPos(0x10, -1570, 0, -2940, 0)
    SetChrPos(0x11, 480, 0, -3440, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 8)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 12)
    SetChrSubChip(0x11, 11)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 4)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrPos(0x12, -88920, 0, -3130, 0)
    SetChrPos(0x13, -90170, 0, -3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 9)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 12)
    SetChrSubChip(0x13, 14)

    label("loc_4E7")

    Jump("loc_548")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_503")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_548")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_517")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_548")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_537")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -60520, 0, -2690, 90)
    Jump("loc_548")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_548")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_55E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_62E")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_574")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_62E")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_58A")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_62E")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5A0")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_62E")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_5B6")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 22)
    Jump("loc_62E")

    label("loc_5B6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5CE"),
        (107, "loc_5E6"),
        (109, "loc_5FE"),
        (116, "loc_616"),
        (SWITCH_DEFAULT, "loc_62E"),
    )


    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_5E3")

    Jump("loc_62E")

    label("loc_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FB")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_5FB")

    Jump("loc_62E")

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    SetMapFlags(0x10000000)
    Event(0, 39)

    label("loc_613")

    Jump("loc_62E")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B")
    SetMapFlags(0x10000000)
    Event(0, 46)

    label("loc_62B")

    Jump("loc_62E")

    label("loc_62E")

    Return()

    # Function_0_376 end

    def Function_1_62F(): pass

    label("Function_1_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_647")
    OP_B1("t2512_y")
    Jump("loc_650")

    label("loc_647")

    OP_B1("t2512_n")

    label("loc_650")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_66C")
    OP_65(0x0, 0x1)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    Jump("loc_6A9")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_684")
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_65(0x0, 0x1)
    Jump("loc_6A9")

    label("loc_684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_6A9")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_698")
    Jump("loc_6A9")

    label("loc_698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_6A2")
    Jump("loc_6A9")

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_6A9")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_6E0")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_6CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_6E0")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_6E0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_6E0")

    Return()

    # Function_1_62F end

    def Function_2_6E1(): pass

    label("Function_2_6E1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -61000, 0, -3720, 0)
    SetChrPos(0x105, -60410, 0, -4540, 0)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x19, 0x0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_0D()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    Sleep(400)

    ChrTalk(    #0
        0x101,
        "#1000FUm, excuse me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "#2P#4SAnd how come no one ever told me?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0x101, 0x1, 0x0, 0x3)
    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1004F#4P(Wh-Whoa...!)\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #3
        0xA,
        (
            "I already said that I'd spend my\x01",
            "vacation sightseeing across Liberl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "Why am I being forced to return\x01",
            "home NOW?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        "Felicity, please, calm yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "No! I refuse!\x01",
            "This time, I will say my piece!\x02",
        )
    )

    CloseMessageWindow()
    OP_91(0x101, 0x0, 0x0, 0x190, 0x3E8, 0x0)

    ChrTalk(    #7
        0x101,
        "#1015FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "Tests are FINALLY over, and I was\x01",
            "finally starting to plan all the things\x01",
            "I wanted to do for my vacation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "So why has a return ticket to the\x01",
            "Empire conveniently shown up on\x01",
            "my doorstop now, of all times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "You... You've been plotting against\x01",
            "me with Grandfather, haven't you?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #11
        0x101,
        "#1007F(Man, hard to get a word in edgewise.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#045F(Let's just see what happens.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "I truly believe it would be in\x01",
            "your best interests to keep these\x01",
            "complaints to yourself for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        (
            "They can only serve to make\x01",
            "things worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "Excuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "#3SEXCUSE ME?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "Have you forgotten your place?!\x01",
            "How dare you speak to your\x01",
            "mistress in such a manner!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BF0():
        OP_69(0x19, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF0)
    TurnDirection(0xA, 0x101, 400)
    Sleep(400)
    TurnDirection(0xB, 0x101, 400)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #18
        0xA,
        "...Oops.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1008FAh...haha... Pardon us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #20
        0xB,
        "(I did try to warn you...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        "#6PA-Ahem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "#6PDo you need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1016FY-Yeah... Sorry to butt in\x01",
            "while you're busy.\x02\x03",

            "We're in the middle of an\x01",
            "investigation, you see.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #25
        0xA,
        "#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "I see. You've come about that\x01",
            "little...incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        "#4PReina! Please, that's enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        (
            "#4PI can hardly bear to recall\x01",
            "such horrors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1002FDid something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "In fact, what we saw would qualify\x01",
            "as more than 'strange.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "It was a human form floating\x01",
            "in the air.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(15)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #33
        0x105,
        "#044FAh!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #34
        0xA,
        "#4P#3SReina...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1002FPlease, tell me everything you saw\x01",
            "in as much detail as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        (
            "I would love to. I believe I could share\x01",
            "enough information for the both of us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #37
        0xB,
        "Is that acceptable, Felicity?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0xA,
        "#4POooh... F-Fine, do whatever you want!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    OP_8E(0xA, 0xFFFF1398, 0x0, 0xFFFFF57E, 0x3E8, 0x0)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10D5():
        OP_69(0x19, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D5)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(1500)

    ChrTalk(    #39
        0xB,
        "It was the night before exams.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "Very suddenly, Felicity said there\x01",
            "was 'someone outside the window.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1002FOh, joy of joys... This already sounds\x01",
            "like the start of some ghost story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "When I peeked out the window,\x01",
            "I saw a human form floating above\x01",
            "the schoolhouse, just as she'd said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        "It spun, as if blown by the wind.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_1261():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1261)
    Sleep(1000)

    ChrTalk(    #44
        0xA,
        "#4POooh...\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0x3)

    ChrTalk(    #45
        0xB,
        (
            "Eventually, it disappeared towards\x01",
            "the back of the schoolhouse.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #46
        0xB,
        "And then came the worst part of all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "My lady, being struck by fear,\x01",
            "climbed into my bed, and--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_44(0xA, 0x3)

    def lambda_135D():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_135D)
    TurnDirection(0xA, 0xB, 10000)

    ChrTalk(    #48
        0xA,
        (
            "#4P#3SSurely that p-part isn't relevant\x01",
            "to their investigation, Reina!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1016FYeah, no need to be THAT specific.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xB,
        (
            "A pity... Just as it was getting\x01",
            "interesting, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1015FAnyway, to make a long story short...\x02\x03",

            "A human shape appeared in the sky above\x01",
            "the schoolhouse, spun around, then vanished\x01",
            "towards the back side of the schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "Yes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "Was that of any help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1018FMore than helpful! Thanks a lot.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #56
        0x105,
        (
            "#040FWe couldn't have asked for\x01",
            "a better testimony, really.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #57
        0x101,
        (
            "#1006F#6PAll right, I should jot this down\x01",
            "in my notebook right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 0)
    SetChrFlags(0xA, 0x10)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    EventEnd(0x0)
    Return()

    # Function_2_6E1 end

    def Function_3_1611(): pass

    label("Function_3_1611")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF38, 0x190, 0x1770)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF9C, 0x12C, 0x1770)
    OP_95(0x101, 0x0, 0x0, 0xFFFFFF9C, 0x64, 0x1770)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Return()

    # Function_3_1611 end

    def Function_4_169C(): pass

    label("Function_4_169C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")

    ChrTalk(    #58
        0xFE,
        (
            "I never thought something like this\x01",
            "would happen to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "If only I'd apologized to Reina sooner...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_179D")

    label("loc_1722")


    ChrTalk(    #60
        0xFE,
        (
            "If I knew something like this\x01",
            "was going to happen, I would have\x01",
            "apologized to Reina sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "Please, be safe...\x02",
    )

    CloseMessageWindow()

    label("loc_179D")

    Jump("loc_1928")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1812")

    ChrTalk(    #62
        0xFE,
        "I WILL go on vacation, and that's final!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I already said that I didn't want to go\x01",
            "home!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187D")

    label("loc_1812")

    OP_A2(0x2)

    ChrTalk(    #64
        0xFE,
        "I WILL go on vacation, and that's final!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "And there's no need for you to come\x01",
            "with me, either!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187D")

    Jump("loc_1928")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_191B")

    ChrTalk(    #66
        0xFE,
        "Oooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I wish we hadn't brought it up again.\x01",
            "Now I can't stop thinking about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "*siiigh* Just as I'd forgotten, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1928")

    label("loc_191B")

    OP_A2(0x1234)
    OP_28(0x83, 0x1, 0x20)
    Call(0, 2)

    label("loc_1928")

    TalkEnd(0xFE)
    Return()

    # Function_4_169C end

    def Function_5_192C(): pass

    label("Function_5_192C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1939")
    Jump("loc_1B0C")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19DA")

    ChrTalk(    #69
        0xFE,
        (
            "I'm afraid you have little choice\x01",
            "in the matter, my lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "There are number of high-class\x01",
            "parties you must attend to upon\x01",
            "your return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6A")

    label("loc_19DA")

    OP_A2(0x3)

    ChrTalk(    #71
        0xFE,
        (
            "My lady, your father would be\x01",
            "disappointed to hear you behaving\x01",
            "so selfishly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Your relations with him are so\x01",
            "very poor as it is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    Jump("loc_1B0C")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 4)), scpexpr(EXPR_END)), "loc_1AFF")

    ChrTalk(    #73
        0xFE,
        (
            "I wish that Felicity would learn to\x01",
            "compose herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Her cowardice would only be met\x01",
            "with disdain among fellow nobles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1AFF")

    OP_A2(0x1234)
    OP_28(0x83, 0x1, 0x20)
    Call(0, 2)

    label("loc_1B0C")

    TalkEnd(0xFE)
    Return()

    # Function_5_192C end

    def Function_6_1B10(): pass

    label("Function_6_1B10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(    #75
        0xFE,
        (
            "Everyone's distracted by what's\x01",
            "been going on, so now's my chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Time to study like crazy and get\x01",
            "ahead of the competition.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1C39")

    label("loc_1BB0")


    ChrTalk(    #77
        0xFE,
        (
            "I don't care about helping out with\x01",
            "school stuff on campus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "That kind of prep work should be\x01",
            "on the faculty, not the students.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C39")

    Jump("loc_1EA9")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CDE")

    ChrTalk(    #79
        0xFE,
        (
            "At the end of the day, club activities\x01",
            "are of no worth whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Students are here to study, study,\x01",
            "and study some more. That's all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D58")

    label("loc_1CDE")

    OP_A2(0x1)

    ChrTalk(    #81
        0xFE,
        (
            "Have fun wasting time on club\x01",
            "activities!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Meanwhile, I'll be racing to the\x01",
            "top of the class with my studies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D58")

    Jump("loc_1EA9")

    label("loc_1D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(    #83
        0xFE,
        "My tests went well enough, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Grades like mine should at least\x01",
            "put me near the top of the class.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA9")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E48")

    ChrTalk(    #85
        0xFE,
        "You don't need anything else, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Then leave me alone, please.\x01",
            "I'm trying to study.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA9")

    label("loc_1E48")

    OP_A2(0x1)

    ChrTalk(    #87
        0xFE,
        "What? I'm busy right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "...Odd occurrences during exams?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "No, nothing really.\x02",
    )

    CloseMessageWindow()

    label("loc_1EA9")

    TalkEnd(0xFE)
    Return()

    # Function_6_1B10 end

    def Function_7_1EAD(): pass

    label("Function_7_1EAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_20AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201C")

    ChrTalk(    #90
        0xFE,
        "Hey, bracers. Nice work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Still, keep on your toes. The case\x01",
            "may have been solved, but the real\x01",
            "work starts now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "None of the lights have worked\x01",
            "ever since orbal devices went on\x01",
            "the fritz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Until this thing gets sorted out,\x01",
            "we'll be engulfed in darkness in\x01",
            "the truest sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Heeheehee... I couldn't be happier.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_20A8")

    label("loc_201C")


    ChrTalk(    #95
        0xFE,
        (
            "I'm most at peace when wrapped\x01",
            "in a veil of darkness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Heeheehee... Truly, there is no\x01",
            "greater comfort than night's sweet\x01",
            "embrace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A8")

    Jump("loc_2239")

    label("loc_20AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_21AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2122")

    ChrTalk(    #97
        0xFE,
        (
            "You understand, right?\x01",
            "It's, y'know, like THAT.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Heeheehee...\x01",
            "What's so terrible about that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A9")

    label("loc_2122")

    OP_A2(0x0)

    ChrTalk(    #99
        0xFE,
        (
            "There's been a suspicious presence\x01",
            "slinking about the academy as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "Maybe one of THOSE is around.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "Heeheehee...\x02",
    )

    CloseMessageWindow()

    label("loc_21A9")

    Jump("loc_2239")

    label("loc_21AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_2239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21DB")

    ChrTalk(    #102
        0xFE,
        "Heeheehee... I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2239")

    label("loc_21DB")

    OP_A2(0x0)

    ChrTalk(    #103
        0xFE,
        (
            "Was there anything odd during\x01",
            "the exam period, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "Heeheehee... I wonder...\x02",
    )

    CloseMessageWindow()

    label("loc_2239")

    TalkEnd(0xFE)
    Return()

    # Function_7_1EAD end

    def Function_8_223D(): pass

    label("Function_8_223D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_2316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FB")

    ChrTalk(    #105
        0xFE,
        (
            "Frustrating as it is, we don't have\x01",
            "much choice but to wait right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Trying anything funny now would\x01",
            "just drag you guys down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "You be careful, okay?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2316")

    label("loc_22FB")


    ChrTalk(    #108
        0xFE,
        "You be careful, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_2316")

    TalkEnd(0xFE)
    Return()

    # Function_8_223D end

    def Function_9_231A(): pass

    label("Function_9_231A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_235D")

    ChrTalk(    #109
        0xFE,
        "We'll be on standby here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Take care, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_235D")

    TalkEnd(0xFE)
    Return()

    # Function_9_231A end

    def Function_10_2361(): pass

    label("Function_10_2361")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_23ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C8")

    ChrTalk(    #111
        0xFE,
        "P-Please, rescue everyone soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "I'll pray for your safety from here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_23ED")

    label("loc_23C8")


    ChrTalk(    #113
        0xFE,
        "P-Please, rescue everyone soon.\x02",
    )

    CloseMessageWindow()

    label("loc_23ED")

    TalkEnd(0xFE)
    Return()

    # Function_10_2361 end

    def Function_11_23F1(): pass

    label("Function_11_23F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 5)), scpexpr(EXPR_END)), "loc_250F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A5")

    ChrTalk(    #114
        0xFE,
        (
            "I'll be patient and wait here like\x01",
            "you asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I just hope Gerome isn't doing\x01",
            "anything stupid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "That impulsive streak of his has\x01",
            "me worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_250F")

    label("loc_24A5")


    ChrTalk(    #117
        0xFE,
        (
            "I'll be patient and wait here like\x01",
            "you asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I just hope Gerome isn't doing\x01",
            "anything stupid...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250F")

    TalkEnd(0xFE)
    Return()

    # Function_11_23F1 end

    def Function_12_2513(): pass

    label("Function_12_2513")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260B")

    ChrTalk(    #119
        0xFE,
        (
            "I'm gettin' my lamp all ready for\x01",
            "the night. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "It's a shame I couldn't find any\x01",
            "cute lamp shades...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I'll just have to make a dreamy,\x01",
            "strawberry-colored one instead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I should ask Kaden for help with\x01",
            "that later.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2684")

    label("loc_260B")


    ChrTalk(    #123
        0xFE,
        (
            "I need a strawberry-colored\x01",
            "lampshade filled with dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Teehee! I should ask Kaden for\x01",
            "help with that later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2684")

    TalkEnd(0xFE)
    Return()

    # Function_12_2513 end

    def Function_13_2688(): pass

    label("Function_13_2688")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277B")

    ChrTalk(    #125
        0xFE,
        "Nothing gets her down, does it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Alice is over there getting her\x01",
            "lamp ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "She said she doesn't like the\x01",
            "design much, but you wouldn't\x01",
            "know it by looking at her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I'm amazed she can bounce\x01",
            "back so quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2813")

    label("loc_277B")


    ChrTalk(    #129
        0xFE,
        "Nothing gets her down, does it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Alice is over there getting her\x01",
            "lamp ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I can't imagine another person\x01",
            "being as easygoing as she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2813")

    TalkEnd(0xFE)
    Return()

    # Function_13_2688 end

    def Function_14_2817(): pass

    label("Function_14_2817")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(    #132
        0xFE,
        (
            "Both his breathing and pulse\x01",
            "have finally stabilized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Right now, he's just tired and\x01",
            "sleeping soundly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "He'll be awake soon enough.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2918")

    label("loc_28C1")


    ChrTalk(    #135
        0xFE,
        (
            "Right now, he's just tired and\x01",
            "sleeping soundly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "He'll be awake soon enough.\x02",
    )

    CloseMessageWindow()

    label("loc_2918")

    TalkEnd(0xFE)
    Return()

    # Function_14_2817 end

    def Function_15_291C(): pass

    label("Function_15_291C")

    Call(0, 16)
    Return()

    # Function_15_291C end

    def Function_16_2921(): pass

    label("Function_16_2921")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_299C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2970")

    ChrTalk(    #137
        0x16,
        "Mmmhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        "Zzzzzz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)
    OP_A2(0x9)
    Jump("loc_2999")

    label("loc_2970")


    ChrTalk(    #139
        0x16,
        "Zzzzzz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)

    label("loc_2999")

    Jump("loc_29C6")

    label("loc_299C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 3)), scpexpr(EXPR_END)), "loc_29C6")

    ChrTalk(    #140
        0x16,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0xFFFFFED4, 1800, 0x1C, 0x21, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x16)

    label("loc_29C6")

    TalkEnd(0x16)
    Return()

    # Function_16_2921 end

    def Function_17_29CA(): pass

    label("Function_17_29CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9A")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #141
        0xFE,
        "Hey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Seriously, thanks. You really came\x01",
            "through for us this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1006FNo, no. It's thanks to you that the\x01",
            "guild got word about it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1043FShe's right, you know.\x02\x03",

            "We might not have been so lucky\x01",
            "if not for the reinforcements.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(400)

    ChrTalk(    #145
        0xFE,
        (
            "H-Hey, cut it out! I was only there\x01",
            "by pure coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I ain't got half the courage of that\x01",
            "old guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1002FHow is the janitor, by the way?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #148
        0xFE,
        "He's not too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "He's been really tired, though,\x01",
            "so he's still sound asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1007FPhew! That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "Yeah, I'm super relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "You can leave him to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I gotta at least take care of the\x01",
            "guy now, or I won't feel right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1025FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        "#1040FThanks. We'll leave it to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Well, if you get the chance,\x01",
            "come by the school again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "You guys're welcome any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1006FYeah, I promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x102,
        "#1040FWe'll see you, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D4)
    Jump("loc_2E52")

    label("loc_2D9A")


    ChrTalk(    #160
        0xFE,
        (
            "I'm gonna stay by his side for\x01",
            "a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I ran off on my own before, that\x01",
            "much is true...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I gotta at least take care of the\x01",
            "guy now, or I won't feel right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E52")

    TalkEnd(0xFE)
    Return()

    # Function_17_29CA end

    def Function_18_2E56(): pass

    label("Function_18_2E56")

    EventBegin(0x0)
    OP_D2(0x26000E, 0x260013, 0x16)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_6D(4730, -250, -1620, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_6D(-1280, -250, -1580, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2E56 end

    def Function_19_2F3D(): pass

    label("Function_19_2F3D")

    EventBegin(0x0)
    OP_D2(0x26000E, 0x260013, 0x16)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    OP_6D(-1280, -250, -1580, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2F3D end

    def Function_20_3013(): pass

    label("Function_20_3013")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x14, -29450, 0, 30290, 270)
    SetChrPos(0x15, -30710, 0, 28800, 0)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_6D(-31890, 0, 30730, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3013 end

    def Function_21_30E3(): pass

    label("Function_21_30E3")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x17, -60450, 0, 28840, 315)
    SetChrPos(0x18, -61710, 0, 29010, 45)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(-60840, 0, 29610, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FC)
    NewScene("ED6_DT21/T2500   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_21_30E3 end

    def Function_22_319E(): pass

    label("Function_22_319E")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_43(0x10, 0x1, 0x0, 0x17)
    OP_43(0x11, 0x1, 0x0, 0x18)
    OP_6D(-89450, 0, -3010, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FD)
    NewScene("ED6_DT21/T2500   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_22_319E end

    def Function_23_3223(): pass

    label("Function_23_3223")

    SetChrPos(0x10, -90230, -250, -6440, 180)
    SetChrChipByIndex(0x10, 22)
    ClearChrFlags(0x10, 0x80)

    label("loc_323E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_327A")
    OP_8C(0x10, 90, 400)
    Sleep(700)
    OP_8C(0x10, 0, 400)
    Sleep(700)
    OP_8C(0x10, 270, 400)
    Sleep(700)
    OP_8C(0x10, 180, 400)
    Sleep(700)
    Jump("loc_323E")

    label("loc_327A")

    Return()

    # Function_23_3223 end

    def Function_24_327B(): pass

    label("Function_24_327B")

    SetChrPos(0x11, -87160, 0, -3040, 270)
    ClearChrFlags(0x11, 0x80)

    label("loc_3291")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32D3")
    OP_8E(0x11, 0xFFFE90EE, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0x11, 0xFFFEAB88, 0x0, 0xFFFFF420, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("loc_3291")

    label("loc_32D3")

    Return()

    # Function_24_327B end

    def Function_25_32D4(): pass

    label("Function_25_32D4")

    Call(0, 26)
    Call(0, 27)
    Return()

    # Function_25_32D4 end

    def Function_26_32DD(): pass

    label("Function_26_32DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270110, 0x270120, 0xD)
    OP_D2(0x270111, 0x270121, 0xE)
    OP_D2(0x270130, 0x270140, 0xF)
    OP_D2(0x270131, 0x270141, 0x10)
    OP_D2(0x70326, 0x7032D, 0x11)
    OP_D2(0x70327, 0x7032E, 0x12)
    OP_D2(0x70318, 0x7031F, 0x13)
    OP_D2(0x70319, 0x70320, 0x14)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_D2(0x270327, 0x270331, 0x17)
    OP_D2(0x270313, 0x27031D, 0x18)
    OP_D2(0x270326, 0x270330, 0x19)
    OP_D2(0x270312, 0x27031C, 0x1A)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x10, 600, 0, -2740, 270)
    SetChrPos(0x11, -1130, 0, -2730, 90)
    SetChrChipByIndex(0x10, 4)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-1830, -250, -1580, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(315000, 0)
    OP_6E(301, 0)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_63(0x10)

    def lambda_3447():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3447)
    Sleep(100)
    OP_63(0x11)

    def lambda_345D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_345D)
    Sleep(400)

    def lambda_3470():
        OP_6D(-1210, 0, -4610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3470)
    OP_43(0x101, 0x1, 0x0, 0x1C)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x1D)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0x1E)
    Sleep(200)
    OP_43(0x10E, 0x1, 0x0, 0x1F)
    WaitChrThread(0x10E, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)

    ChrTalk(    #163
        0x10,
        "#4PWho the hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#4PPsh, can't believe we actually\x01",
            "missed some brats...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #165
        0x10,
        "#4PHang on, that badge!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        "#4PBracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10E,
        "#845F#1PQuite.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 13)
    SetChrChipByIndex(0x102, 15)
    SetChrChipByIndex(0x10A, 17)
    SetChrChipByIndex(0x10E, 19)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #168
        0x10A,
        "#815F#1PNice to BEAT you!\x02",
    )

    CloseMessageWindow()

    def lambda_35EA():
        OP_6D(-1230, 0, -3110, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35EA)

    def lambda_3602():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3602)

    def lambda_3612():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3612)
    Sleep(20)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x11, 0)

    def lambda_3641():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3641)
    Sleep(20)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 26)
    SetChrSubChip(0x11, 0)

    def lambda_3670():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3670)
    Sleep(20)

    def lambda_3690():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_3690)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x79B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_36D3"),
        (SWITCH_DEFAULT, "loc_36D8"),
    )


    label("loc_36D3")

    OP_B4(0x0)
    Jump("loc_36D8")

    label("loc_36D8")

    Return()

    # Function_26_32DD end

    def Function_27_36D9(): pass

    label("Function_27_36D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(390, 0, -5570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, 390, 0, -5570, 0)
    SetChrPos(0x1, 390, 0, -5570, 0)
    SetChrPos(0x2, 390, 0, -5570, 0)
    SetChrPos(0x3, 390, 0, -5570, 0)
    OP_69(0x0, 0x0)
    SetChrPos(0x10, -1570, 0, -2940, 0)
    SetChrPos(0x11, 480, 0, -3440, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 8)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 12)
    SetChrSubChip(0x11, 11)
    OP_A2(0x202A)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_27_36D9 end

    def Function_28_3835(): pass

    label("Function_28_3835")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 860, -500, -9240, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_385C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_385C)
    OP_8E(0xFE, 0x2DA, 0xFFFFFF06, 0xFFFFE2E6, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_3835 end

    def Function_29_3884(): pass

    label("Function_29_3884")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -290, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_38AB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38AB)
    OP_8E(0xFE, 0xFFFFFE2A, 0xFFFFFF06, 0xFFFFE2A0, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_29_3884 end

    def Function_30_38D3(): pass

    label("Function_30_38D3")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 860, -500, -9240, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_38FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38FA)
    OP_8E(0xFE, 0x4EC, 0xFFFFFEF2, 0xFFFFDE86, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_30_38D3 end

    def Function_31_3922(): pass

    label("Function_31_3922")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -290, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3949():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3949)
    OP_8E(0xFE, 0xFFFFFE52, 0xFFFFFECA, 0xFFFFDE86, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_31_3922 end

    def Function_32_3971(): pass

    label("Function_32_3971")

    EventBegin(0x0)
    OP_D2(0x7031D, 0x70324, 0xE)
    OP_D2(0x7031E, 0x70325, 0x10)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrPos(0x14, -29450, 0, 30290, 270)
    SetChrPos(0x15, -30710, 0, 28800, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, -31700, -50, 30400, 90)
    OP_71(0xF, 0x4)
    OP_72(0x10, 0x4)
    OP_6D(-31660, 0, 30680, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(315000, 0)
    OP_6E(381, 0)
    LoadEffect(0x0, "Craft\\\\cr000_00.eff")
    LoadEffect(0x1, "magic\\\\mg112_0.eff")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_3A7B():
        OP_6D(-30540, 0, 29960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A7B)

    def lambda_3A93():
        OP_67(0, 5780, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A93)

    def lambda_3AAB():
        OP_6B(2160, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3AAB)

    def lambda_3ABB():
        OP_6E(381, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3ABB)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3AE2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3AE2)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3B0C():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3B0C)
    OP_43(0x101, 0x1, 0x0, 0x21)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x22)
    Sleep(300)
    OP_43(0x10A, 0x1, 0x0, 0x23)
    Sleep(300)
    OP_43(0x10E, 0x1, 0x0, 0x24)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10A, 0x1)

    ChrTalk(    #169
        0x14,
        "#2PSweet Aidios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x15,
        "#6PIt's Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#1006F#1PHiya, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        "#1040F#5PLet me explain what's happening...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #173
        "\x07\x05Joshua explained the plan to free the captives.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #174
        0x14,
        (
            "#2POooh, okay...\x02\x03",

            "Oh, man, bracers are SO COOL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1016F#1PUh, thanks, I guess!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)
    Sleep(500)

    ChrTalk(    #176
        0x101,
        (
            "#1002F#5P...But more importantly,\x01",
            "is Mr. Parkes okay?!\x02\x03",

            "I'd heard he was shot...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 315, 400)

    ChrTalk(    #177
        0x15,
        (
            "#6PWe think so... The wound itself\x01",
            "doesn't look too bad.\x02\x03",

            "He just fell asleep after\x01",
            "we treated it.\x02\x03",

            "He said he was already wiped out\x01",
            "from the new semester and all, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1007F#5PThank Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#1043F#5PSo his pale complexion is\x01",
            "just from exhaustion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x10E,
        (
            "#840F#5PHmm...\x01",
            "May I see him for a moment?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E22():
        OP_6D(-31390, 0, 30690, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E22)
    OP_43(0x102, 0x0, 0x0, 0x25)
    Sleep(300)
    OP_43(0x10E, 0x0, 0x0, 0x26)
    Sleep(150)

    def lambda_3E52():

        label("loc_3E52")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3E52")

    QueueWorkItem2(0x101, 1, lambda_3E52)
    Sleep(50)

    def lambda_3E68():

        label("loc_3E68")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3E68")

    QueueWorkItem2(0x10A, 1, lambda_3E68)
    Sleep(50)

    def lambda_3E7E():

        label("loc_3E7E")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3E7E")

    QueueWorkItem2(0x15, 1, lambda_3E7E)
    Sleep(50)

    def lambda_3E94():

        label("loc_3E94")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_3E94")

    QueueWorkItem2(0x14, 1, lambda_3E94)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x14, 0x1)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #181
        0x10E,
        "#843F#5PBy my arts, be calm as ocean waves!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 16)
    OP_51(0x10E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x10E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x0, 0x0, 0x10E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    PlayEffect(0x1, 0x1, 0x16, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3FA5():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FA5)
    Sleep(100)

    def lambda_3FB8():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FB8)
    Sleep(100)

    def lambda_3FCB():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3FCB)
    Sleep(100)

    def lambda_3FDE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3FDE)
    Sleep(100)
    OP_8C(0x14, 270, 400)
    OP_83(0x1, 0x2)

    def lambda_3FFB():
        OP_6D(-31070, 0, 30140, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FFB)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x10E, 65535)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #182
        0x101,
        "#1004F#5PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        "#1040FThat never stops being impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10A,
        (
            "#811F#5PHeehee! Kurt's saved my butt with\x01",
            "that plenty of times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x14,
        (
            "#2PI'll be... He looks better than\x01",
            "he did a second ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x15,
        "#5PAnyway, let's let him sleep for now.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)
    Sleep(300)

    ChrTalk(    #187
        0x15,
        (
            "#5PThank you so much for\x01",
            "coming to save us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4150():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4150)
    Sleep(100)
    OP_8C(0x14, 135, 400)

    ChrTalk(    #188
        0x15,
        "#5PCan we do anything to help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#1054F#2PThe best thing you can do\x01",
            "is stay here until it's safe.\x02\x03",

            "It's still very dangerous outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x15,
        "#5PI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x14,
        "#5PBe careful out there!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #192
        (
            "\x07\x05Estelle checked the names of Rhody, Roy,\x01",
            "and Janitor Parkes off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x202B)
    OP_28(0xC0, 0x1, 0x1000)
    OP_28(0xC1, 0x2, 0x40)
    OP_28(0xC1, 0x1, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x15, 0, 0)
    OP_8C(0x14, 270, 0)
    OP_6D(-28710, 0, 27260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -28730, 0, 27100, 180)
    SetChrPos(0x1, -28730, 0, 27100, 180)
    SetChrPos(0x2, -28730, 0, 27100, 180)
    SetChrPos(0x3, -28730, 0, 27100, 180)
    OP_69(0x0, 0x0)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_32_3971 end

    def Function_33_4369(): pass

    label("Function_33_4369")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8D0A, 0x0, 0x6BD0, 0x1388, 0x0)
    Return()

    # Function_33_4369 end

    def Function_34_4394(): pass

    label("Function_34_4394")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF9188, 0x0, 0x6B8A, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_34_4394 end

    def Function_35_43C6(): pass

    label("Function_35_43C6")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF8DB4, 0x0, 0x66C6, 0x1388, 0x0)
    Return()

    # Function_35_43C6 end

    def Function_36_43F1(): pass

    label("Function_36_43F1")

    SetChrPos(0xFE, -28530, 0, 20820, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF9278, 0x0, 0x66C6, 0x1388, 0x0)
    Return()

    # Function_36_43F1 end

    def Function_37_441C(): pass

    label("Function_37_441C")

    OP_8E(0xFE, 0xFFFF9304, 0x0, 0x717A, 0x7D0, 0x0)

    def lambda_4436():

        label("loc_4436")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_4436")

    QueueWorkItem2(0x102, 1, lambda_4436)
    Return()

    # Function_37_441C end

    def Function_38_4442(): pass

    label("Function_38_4442")

    OP_8E(0xFE, 0xFFFF90FC, 0x0, 0x6D9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF8EA4, 0x0, 0x6FCC, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_38_4442 end

    def Function_39_4472(): pass

    label("Function_39_4472")

    Call(0, 40)
    Call(0, 41)
    Return()

    # Function_39_4472 end

    def Function_40_447B(): pass

    label("Function_40_447B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x270110, 0x270120, 0xD)
    OP_D2(0x270111, 0x270121, 0xE)
    OP_D2(0x270130, 0x270140, 0xF)
    OP_D2(0x270131, 0x270141, 0x10)
    OP_D2(0x70326, 0x7032D, 0x11)
    OP_D2(0x70327, 0x7032E, 0x12)
    OP_D2(0x70318, 0x7031F, 0x13)
    OP_D2(0x70319, 0x70320, 0x14)
    OP_D2(0x26000E, 0x260013, 0x16)
    OP_D2(0x270327, 0x270331, 0x17)
    OP_D2(0x270313, 0x27031D, 0x18)
    OP_D2(0x270326, 0x270330, 0x19)
    OP_D2(0x270312, 0x27031C, 0x1A)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x12, -91240, 0, -3150, 90)
    SetChrPos(0x13, -89920, 0, -3190, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_6D(-90060, 0, -2540, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_45B9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_45B9)
    Sleep(100)

    def lambda_45CC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_45CC)
    Sleep(400)

    def lambda_45DF():
        OP_6D(-89530, 0, -4660, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45DF)

    def lambda_45F7():
        OP_6B(3070, 1000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45F7)
    OP_43(0x101, 0x1, 0x0, 0x2A)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x2B)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0x2C)
    Sleep(200)
    OP_43(0x10E, 0x1, 0x0, 0x2D)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #193
        0x12,
        "#3PWho the hell are you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        "#3PWhat are you doing out here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1007F#2PThat is so totally our line.\x02\x03",

            "#1019FYou think creepo guys like you get\x01",
            "to hang out in a girls' dorm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x12,
        "#3PWait, what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10A,
        (
            "#1311F#2PThis is the realm of maidens whose\x01",
            "chastity and cuteness would shame\x01",
            "flowers!\x02\x03",

            "#816FYou could at least, like, put a ribbon\x01",
            "or something on first, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x12)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #198
        0x12,
        "#3P#3SStop screwing with us!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #199
        0x13,
        "#3PWhy'd you even make me THINK that?!\x02",
    )

    CloseMessageWindow()

    def lambda_487B():
        OP_6D(-89560, 0, -4540, 150)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_487B)

    def lambda_4893():
        OP_6B(2800, 150)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4893)

    def lambda_48A3():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48A3)
    Sleep(20)
    SetChrChipByIndex(0x12, 23)
    SetChrFlags(0x12, 0x1000)

    def lambda_48CD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_48CD)

    def lambda_48E8():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48E8)
    Sleep(20)
    SetChrChipByIndex(0x13, 24)
    SetChrFlags(0x13, 0x1000)

    def lambda_4912():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4912)

    def lambda_492D():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_492D)
    Sleep(20)

    def lambda_494D():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_494D)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    Battle(0x79C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4998"),
        (SWITCH_DEFAULT, "loc_499D"),
    )


    label("loc_4998")

    OP_B4(0x0)
    Jump("loc_499D")

    label("loc_499D")

    Return()

    # Function_40_447B end

    def Function_41_499E(): pass

    label("Function_41_499E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(-90270, 0, -5390, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x0, -90270, 0, -5390, 0)
    SetChrPos(0x1, -90270, 0, -5390, 0)
    SetChrPos(0x2, -90270, 0, -5390, 0)
    SetChrPos(0x3, -90270, 0, -5390, 0)
    OP_69(0x0, 0x0)
    SetChrPos(0x12, -88920, 0, -3130, 0)
    SetChrPos(0x13, -90170, 0, -3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 9)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 12)
    SetChrSubChip(0x13, 14)
    OP_A2(0x202C)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_41_499E end

    def Function_42_4B02(): pass

    label("Function_42_4B02")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 13)
    SetChrPos(0xFE, -90840, -500, -9250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4B2E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B2E)
    OP_8E(0xFE, 0xFFFE9E72, 0xFFFFFF06, 0xFFFFE430, 0x1388, 0x0)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_42_4B02 end

    def Function_43_4B60(): pass

    label("Function_43_4B60")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x102, 15)
    SetChrPos(0xFE, -89620, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4B8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B8C)
    OP_8E(0xFE, 0xFFFEA28C, 0xFFFFFF06, 0xFFFFE322, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_43_4B60 end

    def Function_44_4BB9(): pass

    label("Function_44_4BB9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10A, 17)
    SetChrPos(0xFE, -90840, -500, -9250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4BE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BE5)
    OP_8E(0xFE, 0xFFFE9C06, 0xFFFFFF06, 0xFFFFDEF4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_44_4BB9 end

    def Function_45_4C12(): pass

    label("Function_45_4C12")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10E, 19)
    SetChrPos(0xFE, -89620, -500, -9230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4C3E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C3E)
    OP_8E(0xFE, 0xFFFEA1F6, 0xFFFFFF06, 0xFFFFDF1C, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_45_4C12 end

    def Function_46_4C6B(): pass

    label("Function_46_4C6B")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x17, -60450, 0, 28840, 315)
    SetChrPos(0x18, -61710, 0, 29010, 45)
    SetChrPos(0xA, -60810, 0, 29920, 180)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(-60370, 0, 30030, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4D2B():
        OP_6D(-60370, 0, 28260, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D2B)

    def lambda_4D43():
        OP_6E(325, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4D43)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4D6A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D6A)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4D94():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4D94)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4DBE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DBE)
    OP_43(0x101, 0x1, 0x0, 0x2F)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x30)
    Sleep(400)
    OP_43(0x10A, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_43(0x10E, 0x1, 0x0, 0x32)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #200
        0xA,
        "#6PYou're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x18,
        "#3PEstelle? JOSHUA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        "#1017F#2PAhaha! Sorry to keep you waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        "#1040F#4PHere's what's going on...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #204
        "\x07\x05Joshua explained the plan to free the captives.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #205
        0x17,
        (
            "#6POkay, I see...\x02\x03",

            "Phew! I think my nerves are all shot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        "#6PSo, um, what should we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x18,
        "#3PShould we try to find the others?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1003F#2PNo way, not yet. There's still fighting\x01",
            "outside and you could get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#1042F#4PPlease, stay here for now and bar the\x01",
            "door. We'll let you know when it's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x18,
        "#3POkay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xA,
        "#6PWe'll do that. Good luck!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05Estelle checked the names of Nikita, Felicity,\x01",
            "and Taylor off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x202D)
    OP_28(0xC0, 0x1, 0x2000)
    OP_28(0xC1, 0x2, 0x100)
    OP_28(0xC1, 0x1, 0x200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x15, 0, 0)
    OP_8C(0x14, 0, 0)
    OP_6D(-61470, 0, 26430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -61470, 0, 26430, 180)
    SetChrPos(0x1, -61470, 0, 26430, 180)
    SetChrPos(0x2, -61470, 0, 26430, 180)
    SetChrPos(0x3, -61470, 0, 26430, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x18, 45, 0)
    OP_8C(0xA, 180, 0)
    OP_8C(0x17, 315, 0)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0xA, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_4C6B end

    def Function_47_519F(): pass

    label("Function_47_519F")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0F10, 0x0, 0x6806, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_47_519F end

    def Function_48_51D1(): pass

    label("Function_48_51D1")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF12B2, 0x0, 0x67F2, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_48_51D1 end

    def Function_49_5203(): pass

    label("Function_49_5203")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF0EC0, 0x0, 0x641E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_49_5203 end

    def Function_50_5235(): pass

    label("Function_50_5235")

    SetChrPos(0xFE, -61530, 0, 20850, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF137A, 0x0, 0x641E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_50_5235 end

    SaveToFile()

Try(main)
