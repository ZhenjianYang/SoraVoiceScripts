from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Cassius',                              # 9
        'Scherazard',                           # 10
        'Bleublanc',                            # 11
        'Walter',                               # 12
        'Renne',                                # 13
        'Luciola',                              # 14
        'Queen Alicia',                         # 15
        'Princess Klaudia',                     # 16
        'Sieg',                                 # 17
        'Lt. Colonel Cid',                      # 18
        'Richard',                              # 19
        'Royal Guardsman',                      # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        "Bleublanc's Knife",                    # 27
        "Bleublanc's Afterimage",               # 28
        "Bleublanc's Afterimage",               # 29
        "Walter's Afterimage",                  # 30
        "Walter's Afterimage",                  # 31
        "Renne's Afterimage",                   # 32
        "Renne's Afterimage",                   # 33
        "Luciola's Afterimage",                 # 34
        "Luciola's Afterimage",                 # 35
        'Royal Guardsman',                      # 36
        'Royal Guardsman',                      # 37
    )

    DeclEntryPoint(
        Unknown_00              = -2780,
        Unknown_04              = 12000,
        Unknown_08              = 63200,
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH01320 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH01320P._CP',             # 02
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4210,
        Z                   = 18000,
        Y                   = 103250,
        Direction           = 183,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -4250,
        Z                   = 18000,
        Y                   = 103250,
        Direction           = 181,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = 27460,
        Y                   = 11000,
        Z                   = 81540,
        Range               = 32180,
        Unknown_10          = 0x34BC,
        Unknown_14          = 0x1444C,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -1730,
        Y                   = 19160,
        Z                   = 107150,
        Range               = 1680,
        Unknown_10          = 0x55E6,
        Unknown_14          = 0x1A7A2,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = -32759,
        Y                   = 15500,
        Z                   = 76820,
        Range               = -35080,
        Unknown_10          = 0x4074,
        Unknown_14          = 0x116D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -4630,
        Y                   = 16000,
        Z                   = 86040,
        Range               = 4660,
        Unknown_10          = 0x2EE0,
        Unknown_14          = 0x14974,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    ScpFunction(
        "Function_0_4E2",          # 00, 0
        "Function_1_5E5",          # 01, 1
        "Function_2_6ED",          # 02, 2
        "Function_3_703",          # 03, 3
        "Function_4_86D",          # 04, 4
        "Function_5_982",          # 05, 5
        "Function_6_AF5",          # 06, 6
        "Function_7_B18",          # 07, 7
        "Function_8_BA4",          # 08, 8
        "Function_9_C1F",          # 09, 9
        "Function_10_1FE4",        # 0A, 10
        "Function_11_2128",        # 0B, 11
        "Function_12_23B2",        # 0C, 12
        "Function_13_2E37",        # 0D, 13
        "Function_14_2E60",        # 0E, 14
        "Function_15_2E90",        # 0F, 15
        "Function_16_2EAC",        # 10, 16
        "Function_17_2ED2",        # 11, 17
        "Function_18_2F1F",        # 12, 18
        "Function_19_2F85",        # 13, 19
        "Function_20_2FEB",        # 14, 20
        "Function_21_3051",        # 15, 21
        "Function_22_30B7",        # 16, 22
        "Function_23_311D",        # 17, 23
        "Function_24_3183",        # 18, 24
        "Function_25_323E",        # 19, 25
        "Function_26_32F9",        # 1A, 26
        "Function_27_33B4",        # 1B, 27
        "Function_28_346F",        # 1C, 28
        "Function_29_352A",        # 1D, 29
        "Function_30_35E5",        # 1E, 30
        "Function_31_36A0",        # 1F, 31
        "Function_32_5CA6",        # 20, 32
        "Function_33_5D1C",        # 21, 33
        "Function_34_5D8A",        # 22, 34
        "Function_35_5E05",        # 23, 35
        "Function_36_5EC6",        # 24, 36
        "Function_37_5F21",        # 25, 37
        "Function_38_5FDE",        # 26, 38
        "Function_39_6010",        # 27, 39
        "Function_40_6026",        # 28, 40
        "Function_41_60E3",        # 29, 41
        "Function_42_6271",        # 2A, 42
        "Function_43_62DE",        # 2B, 43
        "Function_44_63A0",        # 2C, 44
        "Function_45_6459",        # 2D, 45
        "Function_46_64E0",        # 2E, 46
        "Function_47_74FB",        # 2F, 47
        "Function_48_7543",        # 30, 48
        "Function_49_75FD",        # 31, 49
        "Function_50_76B7",        # 32, 50
        "Function_51_7771",        # 33, 51
        "Function_52_782B",        # 34, 52
        "Function_53_78E5",        # 35, 53
        "Function_54_799F",        # 36, 54
        "Function_55_7A59",        # 37, 55
        "Function_56_7B13",        # 38, 56
        "Function_57_7B99",        # 39, 57
    )


    def Function_0_4E2(): pass

    label("Function_0_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4EC")
    Jump("loc_525")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_500")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_525")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_514")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_525")

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_525")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    SetChrPos(0x8, -43230, 16000, 80440, 270)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_570")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_5DA")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_597")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    SetChrPos(0x101, 29990, 10500, 78720, 0)
    Event(0, 6)
    Jump("loc_5DA")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_5B3")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 46)
    Jump("loc_5DA")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5C9")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_5DA")

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DA")
    Event(0, 5)

    label("loc_5DA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_4E2 end

    def Function_1_5E5(): pass

    label("Function_1_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_601")
    OP_B1("t4201_y")
    Jump("loc_60A")

    label("loc_601")

    OP_B1("t4201_n")

    label("loc_60A")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_72(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_62A")
    OP_6F(0x2, 0)
    Jump("loc_642")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_63B")
    OP_6F(0x2, 450)
    Jump("loc_642")

    label("loc_63B")

    OP_6F(0x2, 0)

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C3, 0x1, 0x50)

    label("loc_65C")

    OP_71(0x1, 0x4)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_696")

    label("loc_68D")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_696")

    SetMapFlags(0x2000000)
    OP_72(0x3, 0x10)
    OP_72(0x3, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_END)), "loc_6B6")
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)

    label("loc_6B6")

    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 11)

    label("loc_6C3")

    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EC")

    label("loc_6E2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EC")

    Return()

    # Function_1_5E5 end

    def Function_2_6ED(): pass

    label("Function_2_6ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_702")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6ED")

    label("loc_702")

    Return()

    # Function_2_6ED end

    def Function_3_703(): pass

    label("Function_3_703")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_744")

    ChrTalk(    #0
        0xFE,
        (
            "Beyond this point are\x01",
            "Queen Alicia's quarters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_869")

    label("loc_744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_7F1")

    ChrTalk(    #1
        0xFE,
        (
            "If you're looking for Her Majesty,\x01",
            "she's currently resting in her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I believe she just received a report\x01",
            "about the incident in the audience\x01",
            "chamber.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_869")

    label("loc_7F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_869")

    ChrTalk(    #3
        0xFE,
        "Why, Lady Klaudia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "If you're looking for Her Majesty\x01",
            "the queen, she's currently resting\x01",
            "in her room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869")

    TalkEnd(0xFE)
    Return()

    # Function_3_703 end

    def Function_4_86D(): pass

    label("Function_4_86D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8E8")

    ChrTalk(    #5
        0xFE,
        (
            "Her Majesty the Queen and\x01",
            "Princess Klaudia are currently\x01",
            "not in their rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "I just saw them leave.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97E")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_95C")

    ChrTalk(    #7
        0xFE,
        (
            "Have you heard the news?\x01",
            "The Arseille's been loaded with\x01",
            "its new engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I hope to see it soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97E")

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_97E")

    ChrTalk(    #9
        0xFE,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()

    label("loc_97E")

    TalkEnd(0xFE)
    Return()

    # Function_4_86D end

    def Function_5_982(): pass

    label("Function_5_982")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E6(0x1)
    OP_A2(0x1000)
    OP_1D(0x11)
    OP_11(0xFF, 0xFF, 0xFF, 0x59D8, 0x7C060, 0x0)
    SetChrFlags(0x101, 0x8)
    OP_77(0xE6, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(10, 12000, 28900, 0)
    OP_67(-10, 3030, -10000, 0)
    OP_6B(4780, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0xBB8)
    OP_DE("Grancel Castle")
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_A2E():
        OP_6D(-13000, 16500, 75510, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A2E)

    def lambda_A46():
        OP_67(-8000, 5500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A46)

    def lambda_A5E():
        OP_6C(45000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5E)

    def lambda_A6E():
        OP_6B(6000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A6E)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    def lambda_A8D():
        OP_6D(150, 18500, 104610, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A8D)

    def lambda_AA5():
        OP_67(0, 7270, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA5)

    def lambda_ABD():
        OP_6B(7610, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_ABD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_3E(0x35F, 1)
    FadeToDark(1500, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_982 end

    def Function_6_AF5(): pass

    label("Function_6_AF5")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x74EA, 0x2EE0, 0x144CE, 0x1388, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_AF5 end

    def Function_7_B18(): pass

    label("Function_7_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA3")
    EventBegin(0x0)

    ChrTalk(    #10
        0x101,
        (
            "#002F(Dad'll know something! I'm sure!)\x02\x03",

            "(Got to find him, got to find him...\x01",
            "Where is he?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_BA3")

    Return()

    # Function_7_B18 end

    def Function_8_BA4(): pass

    label("Function_8_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1E")
    EventBegin(0x0)

    ChrTalk(    #11
        0x101,
        (
            "#002F(Schera said Dad went\x01",
            "to the Garden Terrace...)\x02\x03",

            "(I HAVE to find him!)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_C1E")

    Return()

    # Function_8_BA4 end

    def Function_9_C1F(): pass

    label("Function_9_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2C")
    Return()

    label("loc_C2C")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    SetChrSubChip(0x8, 0)
    ClearMapFlags(0x1)

    ChrTalk(    #12
        0x101,
        "#587F#6PAh!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)
    Sleep(200)

    def lambda_C5F():
        OP_6D(-41470, 16000, 79880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5F)

    def lambda_C77():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C77)

    def lambda_C8F():
        OP_6B(1660, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C8F)

    def lambda_C9F():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C9F)

    def lambda_CAF():
        OP_6E(532, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_CAF)
    Sleep(3000)

    ChrTalk(    #13
        0x8,
        "#1128F#6PEstelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#002F#6PD-Dad...\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0x8, 0x7D0, 0x1770, 0x0)

    ChrTalk(    #15
        0x101,
        "#005FW-W-We have a problem--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1125F#6PI know.\x02\x03",

            "Joshua...is gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x1A)
    Sleep(500)

    ChrTalk(    #17
        0x101,
        (
            "#580FWh... What...?\x02\x03",

            "How do you know about that?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#1122F#6PAfter getting back from the meeting\x01",
            "last night, I found you asleep in one\x01",
            "of our beds.\x02\x03",

            "He left a note on the nightstand,\x01",
            "as well.\x02\x03",

            "Between the two...I have a fairly good\x01",
            "idea of what must have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#005FThen, then...!\x02\x03",

            "What the heck are you just\x01",
            "standing around here for?!\x02\x03",

            "We need to find Joshua fast befo--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "#1125F#6PStop, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#580FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#1122F#6PIf he has truly gone to ground, even I\x01",
            "have little hope of actually finding him.\x02\x03",

            "His skills are almost superhuman.\x01",
            "When we fought five years ago, I was\x01",
            "nearly killed...by an eleven-year-old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#587F...\x02\x03",

            "Okay. I only asked this once\x01",
            "before, a long time ago, but...\x02\x03",

            "Who... Who IS Joshua, exactly?\x01",
            "Why did you bring him into our\x01",
            "home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "#1128F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 500)
    Sleep(500)

    ChrTalk(    #25
        0x8,
        (
            "#1125F#6PThe Society of Ouroboros.\x01",
            "Your answer begins there, with an\x01",
            "organization few even know exists.\x02\x03",

            "They are an organization that seeks to manipulate\x01",
            "the world from the shadows, led by a leader called\x01",
            "the 'Grandmaster.'\x02\x03",

            "Joshua was in their employ as an assassin\x01",
            "when I first met him. I brought him home because\x01",
            "it was his only chance to live free of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#587FOuroboros...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1122F#6PEven the Bracer Guild knows very little about them,\x01",
            "and only top bracers even learn of their existence.\x02\x03",

            "Given that the response of the public to the\x01",
            "idea of Ouroboros' existence would be either panic\x01",
            "or skepticism, we don't acknowledge them publicly.\x02\x03",

            "But...they exist. There is no question of that.\x01",
            "And they've had plans in motion for years.\x02\x03",

            "The recent coup is just one example of their\x01",
            "machinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#587FWait! You mean...\x02\x03",

            "Lieutenant Lorence?! He was--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1122F#6PYes. We have absolutely no doubt he\x01",
            "was another senior agent from the society.\x02\x03",

            "Of course, we doubt he was acting as a\x01",
            "lone wolf. He must have had support to\x01",
            "accomplish what he did.\x02\x03",

            "#1125FSupport like Joshua, for example.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        (
            "#580FWait. What...?\x02\x03",

            "What the heck do you mean?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#1125F#6PHe stated as much in his note.\x02\x03",

            "Over the past five years, Joshua has been\x01",
            "passing along guild secrets to Ouroboros.\x02\x03",

            "He claims that he was under the influence\x01",
            "of some sort of mental control and didn't\x01",
            "even realize what he was doing himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#587FNo. No...\x02\x03",

            "#588FNo, he wouldn't...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(500)

    ChrTalk(    #33
        0x8,
        (
            "#1122F#6POuroboros' cunning is matched\x01",
            "only by their malevolence.\x02\x03",

            "Stay away from them, Estelle.\x01",
            "They're far too dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#004F...\x02\x03",

            "#586FO-Okay... I don't quite get all of this,\x01",
            "but I just want to make sure...\x01",
            "make sure I'm hearing this right.\x02\x03",

            "You're saying we should abandon\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "#1122F#6PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#005F#3SDad! ANSWER the question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1125F#6PI always knew this day would come.\x02\x03",

            "Even five years ago, when I took\x01",
            "him in, I knew we would someday\x01",
            "reach this moment.\x02\x03",

            "He swore something to me, that first\x01",
            "day he actually accepted he could be\x01",
            "part of our home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#587FWhat did he...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1122F#6PThe moment he became a burden\x01",
            "or a threat to us...\x02\x03",

            "The moment the society contacted\x01",
            "him or pursued him in any fashion...\x02\x03",

            "He would disappear from our lives.\x01",
            "'Like a shadow dispelled by the sun,'\x01",
            "he told me once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#587FWhat...?\x02\x03",

            "What's...that supposed to--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#1128F#6PEstelle. I understand how you feel.\x02\x03",

            "He was part of our family.\x01",
            "It isn't easy to just...say goodbye\x01",
            "so suddenly.\x02\x03",

            "#1125FBut there are some lines which a\x01",
            "man can never bring himself to cross.\x01",
            "Ever.\x02\x03",

            "#1122FSo, please, try to understand what Jo--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#586FYou knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "#1122F#6PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#586FYou knew that Joshua might leave\x01",
            "us someday and never said anything\x01",
            "to me or did anything about it...\x02\x03",

            "You knew...and you didn't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#1128F#6P...\x02\x03",

            "#1125FI'm...sorry, Este--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -23950, 14000, 71460, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    Sleep(500)

    ChrTalk(    #46
        0x101,
        "#583F#4SI HATE YOU!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_1C2F():
        OP_8E(0x101, 0xFFFF88E6, 0x36B0, 0x1108A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C2F)

    def lambda_1C4A():
        OP_6D(-32960, 16000, 72720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C4A)

    def lambda_1C62():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C62)

    def lambda_1C7A():
        OP_8E(0x9, 0xFFFF8B98, 0x36B0, 0x11594, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1C7A)
    WaitChrThread(0x9, 0x0)

    def lambda_1C9A():
        OP_8E(0x9, 0xFFFF822E, 0x3C8C, 0x1205C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C9A)
    Sleep(1000)

    def lambda_1CBA():
        OP_8E(0x101, 0xFFFFC702, 0x36B0, 0x12890, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1CBA)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 225, 400)
    OP_8C(0x9, 135, 400)
    Sleep(1000)
    Sleep(1000)
    OP_8C(0x9, 90, 400)
    Sleep(2000)
    TurnDirection(0x9, 0x8, 400)

    def lambda_1D05():
        OP_6D(-40820, 16000, 79520, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D05)

    def lambda_1D1D():
        OP_67(0, 7000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D1D)
    OP_8E(0x9, 0xFFFF63B6, 0x3E80, 0x131C8, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #47
        0x9,
        "#522F#4PCassius...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#1122F#1PSchera.\x02\x03",

            "I'm sorry you had to see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#522F#4PNo, it's...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#1128F#1PWhy do I get the feeling you're\x01",
            "biting back a lecture?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#524F#4PI stumbled into your life from a\x01",
            "disaster of my own. You saved me,\x01",
            "just as you did Joshua.\x02\x03",

            "I understand what both you and\x01",
            "Joshua must be thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#1125F#1PIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#025F#4PIf I may make a single comment,\x01",
            "though. From a woman's perspective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "#1124F#1POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#022F#4PAt this point, you and Joshua are, essentially,\x01",
            "the two most wretchedly miserable sons of dogs\x01",
            "I have EVER had the displeasure of knowing.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_C1F end

    def Function_10_1FE4(): pass

    label("Function_10_1FE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, 6360, 12000, 92750, 0)
    OP_6D(-1460, 12000, 55280, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(9570, 0)
    OP_6C(21000, 0)
    OP_6E(350, 0)
    StopSound(0x7D00, 0x61A80, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0xBB8)
    OP_DE("Grancel Castle")
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x493E0, 0x2710)

    def lambda_20A1():
        OP_6D(750, 20000, 110490, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_20A1)

    def lambda_20B9():
        OP_67(0, 6120, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_20B9)
    Sleep(1000)
    Sleep(1000)

    def lambda_20DB():
        OP_6B(8280, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_20DB)

    def lambda_20EB():
        OP_6C(33000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_20EB)

    def lambda_20FB():
        OP_6E(247, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_20FB)
    WaitChrThread(0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1FE4 end

    def Function_11_2128(): pass

    label("Function_11_2128")

    LoadEffect(0x1, "map\\\\mpsmk0.eff")
    LoadEffect(0x2, "map\\\\mpfire2.eff")
    LoadEffect(0x3, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x46)
    OP_22(0xAE, 0x1, 0x46)
    PlayEffect(0x3, 0xFF, 0xFF, -170, 12000, 68500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 30580, 16500, 91210, 0, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6310, 22500, 89250, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 16200, 15000, 54000, 0, 0, 0, 1400, 1800, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -21680, 15000, 54280, 0, 0, 0, 1500, 1900, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -40400, 20400, 74600, 0, 0, 0, 1500, 1800, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -24100, 16700, 90680, 0, 0, 0, 1300, 1500, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 30580, 16000, 91210, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 6310, 21950, 89250, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -40400, 19900, 74600, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -24100, 16300, 90680, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_11_2128 end

    def Function_12_23B2(): pass

    label("Function_12_23B2")

    EventBegin(0x0)
    OP_D2(0x2701C9, 0x2701CE, 0x3)
    OP_D2(0x270267, 0x270271, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x260052, 0x260057, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x27023F, 0x270249, 0x8)
    OP_D2(0x2701C8, 0x2701CD, 0x9)
    OP_D2(0x270253, 0x27025D, 0xA)
    OP_D2(0x600E8, 0x600ED, 0xB)
    OP_D2(0x600E7, 0x600EC, 0xC)
    OP_D2(0x2601BC, 0x2601C1, 0xD)
    OP_D2(0x2600A0, 0x2600A5, 0x22)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xD, 9)
    SetChrPos(0xA, 8600, 14000, 79010, 270)
    SetChrPos(0xC, 9600, 14000, 77740, 270)
    SetChrPos(0xD, 9800, 14000, 80570, 270)
    SetChrPos(0xB, 10800, 14000, 79250, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(8029, 14000, 79890, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    LoadEffect(0x0, "Craft\\\\cr161_00.eff")
    OP_43(0xA, 0x1, 0x0, 0xD)
    OP_43(0xC, 0x1, 0x0, 0xE)
    OP_43(0xD, 0x1, 0x0, 0xF)
    OP_43(0xB, 0x1, 0x0, 0x10)
    FadeToBright(1000, 0)

    def lambda_2516():
        OP_6D(-150, 14000, 82580, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2516)

    def lambda_252E():
        OP_67(0, 6170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_252E)

    def lambda_2546():
        OP_6C(31000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2546)

    def lambda_2556():
        OP_6B(3190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2556)

    def lambda_2566():
        OP_6E(346, 3000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2566)
    WaitChrThread(0xD, 0x1)
    Sleep(1000)
    OP_6D(730, 20000, 109310, 4000)
    Sleep(500)

    ChrTalk(    #56
        0xA,
        "#230F#5PHmm. So these are the queen's chambers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        "#240F#1POur destination, then.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0xB,
        (
            "#250F#5PThis sucks.\x02\x03",

            "The only one who didn't just fall\x01",
            "over was the old timer!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    ChrTalk(    #59
        0xD,
        "#241F#4PYes, he was quite an expert.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #60
        0xC,
        (
            "#269F#5PHe was still silly, though. There was\x01",
            "no way he could beat all of us.\x02\x03",

            "#263FStupid old man.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    ChrTalk(    #61
        0xA,
        (
            "#230F#6PHeh, come now, don't say that.\x02\x03",

            "He proved his worth through his loyalty.\x01",
            "Few men can claim as much.\x02\x03",

            "#231FAnd I must admit, Duke Dunan\x01",
            "was a little different than rumor\x01",
            "led me to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#244F#4PTrue. He did not seem like the\x01",
            "absolute debauchee from the reports.\x02\x03",

            "#240FI was still amused by how quickly he\x01",
            "passed out, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 12)
    SetChrChipByIndex(0x15, 12)
    SetChrChipByIndex(0x16, 12)
    SetChrChipByIndex(0x17, 12)
    SetChrChipByIndex(0x18, 12)
    SetChrChipByIndex(0x19, 12)
    SetChrPos(0x13, 380, 20000, 112380, 180)
    SetChrPos(0x14, 380, 20000, 113380, 180)
    SetChrPos(0x15, 380, 20000, 111380, 180)
    SetChrPos(0x16, 380, 20000, 112380, 180)
    SetChrPos(0x17, 380, 20000, 112380, 180)
    SetChrPos(0x18, 380, 20000, 113380, 180)
    SetChrPos(0x19, 380, 20000, 111380, 180)

    ChrTalk(    #63
        0x13,
        "#4PThey're here!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(550, 20000, 108990, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(31000, 0)
    OP_6E(319, 0)

    def lambda_29DD():
        OP_6D(250, 18000, 102900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29DD)
    OP_43(0x13, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x15, 0x1, 0x0, 0x13)
    Sleep(100)
    OP_43(0x16, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x17, 0x1, 0x0, 0x15)
    Sleep(100)
    OP_43(0x18, 0x1, 0x0, 0x16)
    Sleep(100)
    OP_43(0x19, 0x1, 0x0, 0x17)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #64
        0x18,
        (
            "#6PDamn it all...\x01",
            "If only Captain Schwarz were here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x15,
        (
            "#5PStop sniveling! We are the Royal Guard!\x01",
            "Show them what that means!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_8C(0xD, 0, 0)
    OP_8C(0xC, 0, 0)
    OP_8C(0xA, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xB,
        "#254F#2P*sigh* More small fry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        "#244F#4PThis IS getting rather tedious.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    Sleep(300)

    ChrTalk(    #68
        0xC,
        (
            "#261F#1PHeehee! Told you.\x02\x03",

            "#1306FOooh, I know. To make it fun, let's\x01",
            "see who can capture the queen first!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C1A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C1A)

    def lambda_2C28():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C28)
    WaitChrThread(0xA, 0x1)
    Sleep(300)

    ChrTalk(    #69
        0xA,
        "#231F#6POho, an interesting sport!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#252F#2PI'm game.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        "#241F#4PWell, then...let's play.\x02",
    )

    CloseMessageWindow()

    def lambda_2CA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2CA5)
    Sleep(100)

    def lambda_2CB8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CB8)
    Sleep(100)
    OP_8C(0xC, 0, 400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2CE0():
        OP_6D(390, 19000, 105520, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CE0)
    OP_7D(0x0, 0xA, 0xA, 0x64)
    OP_7D(0x0, 0xB, 0xA, 0x64)
    OP_7D(0x0, 0xC, 0xA, 0x64)
    OP_7D(0x0, 0xD, 0xA, 0x64)
    SetChrChipByIndex(0xA, 4)

    def lambda_2D1D():
        OP_8E(0xFE, 0x1EA, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2D1D)
    Sleep(100)
    SetChrChipByIndex(0xC, 8)

    def lambda_2D42():
        OP_8E(0xFE, 0xFFFFFB14, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D42)
    Sleep(100)
    SetChrChipByIndex(0xD, 10)

    def lambda_2D67():
        OP_8E(0xFE, 0x514, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D67)
    Sleep(100)
    SetChrSubChip(0xB, 2)
    SetChrChipByIndex(0xB, 6)
    SetChrFlags(0xB, 0x20)

    def lambda_2D96():
        OP_8E(0xFE, 0xFFFFFE2A, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D96)
    OP_43(0x13, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x19)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x16, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0x17, 0x1, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x18, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0x19, 0x1, 0x0, 0x1E)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_7D(0x1, 0xA, 0x0, 0x0)
    OP_7D(0x1, 0xC, 0x0, 0x0)
    OP_7D(0x1, 0xB, 0x0, 0x0)
    OP_7D(0x1, 0xD, 0x0, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_23B2 end

    def Function_13_2E37(): pass

    label("Function_13_2E37")

    OP_8E(0xFE, 0xA, 0x36B0, 0x13C40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0x36B0, 0x141E0, 0x7D0, 0x0)
    Return()

    # Function_13_2E37 end

    def Function_14_2E60(): pass

    label("Function_14_2E60")

    OP_8E(0xFE, 0xFFFFF9F2, 0x36B0, 0x13880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF9F2, 0x36B0, 0x13D12, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_2E60 end

    def Function_15_2E90(): pass

    label("Function_15_2E90")

    OP_8E(0xFE, 0x500, 0x36B0, 0x13DEE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_2E90 end

    def Function_16_2EAC(): pass

    label("Function_16_2EAC")

    OP_8E(0xFE, 0xFFFFFEF2, 0x36B0, 0x13894, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xB, 34)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_16_2EAC end

    def Function_17_2ED2(): pass

    label("Function_17_2ED2")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2EED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EED)
    OP_8E(0xFE, 0x5A, 0x4650, 0x18CE0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_17_2ED2 end

    def Function_18_2F1F(): pass

    label("Function_18_2F1F")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2F3F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F3F)
    OP_8E(0xFE, 0x398, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0x514, 0x4650, 0x18A06, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_18_2F1F end

    def Function_19_2F85(): pass

    label("Function_19_2F85")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2FA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FA5)
    OP_8E(0xFE, 0xFFFFFBC8, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFA9C, 0x4650, 0x18A6A, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_19_2F85 end

    def Function_20_2FEB(): pass

    label("Function_20_2FEB")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_300B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_300B)
    OP_8E(0xFE, 0xFFFFFFB0, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0x3F2, 0x4650, 0x1938E, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_20_2FEB end

    def Function_21_3051(): pass

    label("Function_21_3051")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_3071():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3071)
    OP_8E(0xFE, 0xFFFFFFB0, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFDB2, 0x4650, 0x1917C, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_21_3051 end

    def Function_22_30B7(): pass

    label("Function_22_30B7")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_30D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30D7)
    OP_8E(0xFE, 0x398, 0x4E20, 0x1A450, 0x1388, 0x0)
    OP_8E(0xFE, 0x924, 0x4650, 0x19230, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_22_30B7 end

    def Function_23_311D(): pass

    label("Function_23_311D")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_313D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_313D)
    OP_8E(0xFE, 0xFFFFFBC8, 0x4E20, 0x1A450, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF8EE, 0x4650, 0x193F2, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_23_311D end

    def Function_24_3183(): pass

    label("Function_24_3183")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_3193():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3193)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_31E8():
        OP_96(0xFE, 0xFFFFFD8A, 0x399E, 0x14D8E, 0x1388, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31E8)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_24_3183 end

    def Function_25_323E(): pass

    label("Function_25_323E")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_324E():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_324E)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_32A3():
        OP_96(0xFE, 0xAD2, 0x3C8C, 0x15342, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_32A3)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 6)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_25_323E end

    def Function_26_32F9(): pass

    label("Function_26_32F9")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_3309():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3309)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_335E():
        OP_96(0xFE, 0xFFFFE9BC, 0x4650, 0x15662, 0x1770, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_335E)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 7)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_26_32F9 end

    def Function_27_33B4(): pass

    label("Function_27_33B4")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_33C4():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33C4)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3419():
        OP_96(0xFE, 0xB72, 0x4074, 0x179D0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3419)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_27_33B4 end

    def Function_28_346F(): pass

    label("Function_28_346F")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_347F():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_347F)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_34D4():
        OP_96(0xFE, 0xFFFFF646, 0x445C, 0x181BE, 0x1388, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34D4)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 6)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_28_346F end

    def Function_29_352A(): pass

    label("Function_29_352A")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_353A():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_353A)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_358F():
        OP_96(0xFE, 0x170C, 0x4650, 0x17958, 0x1B58, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_358F)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_29_352A end

    def Function_30_35E5(): pass

    label("Function_30_35E5")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_35F5():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35F5)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_364A():
        OP_96(0xFE, 0xBC2, 0x4650, 0x18D9E, 0x1770, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_364A)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 3)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_30_35E5 end

    def Function_31_36A0(): pass

    label("Function_31_36A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36B2")
    Return()

    label("loc_36B2")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E9(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xCA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3786")
    EventBegin(0x0)
    OP_4F(0xCA, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E9(0x0)
    OP_6D(-250, 14000, 82500, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -250, 14000, 82500, 0)
    SetChrPos(0x1, -250, 14000, 82500, 0)
    SetChrPos(0x2, -250, 14000, 82500, 0)
    SetChrPos(0x3, -250, 14000, 82500, 0)
    EventEnd(0x0)
    Return()

    label("loc_3786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_379B")
    Call(0, 56)
    Call(0, 57)

    label("loc_379B")

    OP_6D(460, 14750, 85440, 0)
    OP_67(0, 4790, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(33000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, -580, 14750, 85180, 0)
    SetChrPos(0x102, 670, 14750, 85200, 0)
    SetChrPos(0xF8, -830, 14250, 84010, 0)
    SetChrPos(0xF9, 720, 14250, 84140, 0)
    OP_D2(0x2701C9, 0x2701CE, 0x3)
    OP_D2(0x270268, 0x270272, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x27022A, 0x270234, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x270240, 0x27024A, 0x8)
    OP_D2(0x2701C8, 0x2701CD, 0x9)
    OP_D2(0x270254, 0x27025E, 0xA)
    OP_D2(0x70141, 0x70145, 0xB)
    OP_D2(0x260052, 0x260057, 0xC)
    OP_D2(0x70182, 0x70186, 0xD)
    OP_D2(0x2702F0, 0x2702FA, 0xE)
    OP_D2(0x27026B, 0x270275, 0xF)
    OP_D2(0x260068, 0x26006D, 0x10)
    OP_D2(0x704AA, 0x704AE, 0x11)
    OP_D2(0x70180, 0x70184, 0x12)
    OP_D2(0x2702EA, 0x2702F4, 0x13)
    OP_D2(0x2702EB, 0x2702F5, 0x14)
    OP_D2(0x2702EC, 0x2702F6, 0x15)
    OP_D2(0x702D2, 0x702D9, 0x16)
    OP_D2(0x702D3, 0x702DA, 0x17)
    OP_D2(0x702D4, 0x702DB, 0x18)
    OP_D2(0x7052B, 0x7052F, 0x19)
    OP_D2(0x270110, 0x270120, 0x1A)
    OP_D2(0x270111, 0x270121, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    OP_D2(0x270131, 0x270141, 0x1D)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_3943"),
        (2, "loc_395A"),
        (6, "loc_3971"),
        (7, "loc_3988"),
        (SWITCH_DEFAULT, "loc_399F"),
    )


    label("loc_3943")

    OP_D2(0x70218, 0x70224, 0x1E)
    OP_D2(0x70219, 0x70225, 0x1F)
    Jump("loc_399F")

    label("loc_395A")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    OP_D2(0x701D1, 0x701DD, 0x1F)
    Jump("loc_399F")

    label("loc_3971")

    OP_D2(0x70230, 0x7023C, 0x1E)
    OP_D2(0x70231, 0x7023D, 0x1F)
    Jump("loc_399F")

    label("loc_3988")

    OP_D2(0x70248, 0x70254, 0x1E)
    OP_D2(0x70249, 0x70255, 0x1F)
    Jump("loc_399F")

    label("loc_399F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_39B8"),
        (2, "loc_39CF"),
        (6, "loc_39E6"),
        (7, "loc_39FD"),
        (SWITCH_DEFAULT, "loc_3A14"),
    )


    label("loc_39B8")

    OP_D2(0x70218, 0x70224, 0x20)
    OP_D2(0x70219, 0x70225, 0x21)
    Jump("loc_3A14")

    label("loc_39CF")

    OP_D2(0x701D0, 0x701DC, 0x20)
    OP_D2(0x701D1, 0x701DD, 0x21)
    Jump("loc_3A14")

    label("loc_39E6")

    OP_D2(0x70230, 0x7023C, 0x20)
    OP_D2(0x70231, 0x7023D, 0x21)
    Jump("loc_3A14")

    label("loc_39FD")

    OP_D2(0x70248, 0x70254, 0x20)
    OP_D2(0x70249, 0x70255, 0x21)
    Jump("loc_3A14")

    label("loc_3A14")

    OP_D2(0x2600A0, 0x2600A5, 0x22)
    OP_D2(0x2600AE, 0x2600B3, 0x23)
    OP_D2(0x26008F, 0x260094, 0x24)
    LoadEffect(0x0, "map\\mp009_00.eff")
    LoadEffect(0x4, "Craft\\cr161_00.eff")
    SoundLoad(163)
    SoundLoad(164)
    SoundLoad(503)
    SoundLoad(505)
    SoundLoad(571)
    SoundLoad(155)
    SoundLoad(214)
    SoundLoad(213)
    OP_84(0x1)
    OP_84(0x2)
    OP_0D()
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 34)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 11)
    SetChrChipByIndex(0xF, 13)
    SetChrPos(0xC, -1510, 18000, 102060, 180)
    SetChrPos(0xA, -220, 18000, 100200, 180)
    SetChrPos(0xB, 890, 18000, 103470, 180)
    SetChrPos(0xD, 1820, 18000, 101280, 180)
    SetChrPos(0xE, -290, 18000, 101770, 180)
    SetChrPos(0xF, 850, 18000, 101660, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    FadeToBright(500, 0)
    OP_0D()

    NpcTalk(    #72
        0xA,
        "Man's Voice",
        (
            "#4PAh! It seems you have more guests,\x01",
            "Queen Alicia.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCC")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C0A")

    label("loc_3BCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF3")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C0A")

    label("loc_3BF3")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3C0A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C36")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C74")

    label("loc_3C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5D")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C74")

    label("loc_3C5D")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3C74")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_3C86():
        OP_6D(850, 18000, 103170, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C86)

    def lambda_3C9E():
        OP_67(0, 4930, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C9E)

    def lambda_3CB6():
        OP_6B(2410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CB6)

    def lambda_3CC6():
        OP_6C(23000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CC6)

    def lambda_3CD6():
        OP_8F(0xFE, 0xFFFFFF24, 0x3E80, 0x16986, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CD6)
    Sleep(100)

    def lambda_3CF6():
        OP_8F(0xFE, 0x3CA, 0x3E80, 0x16968, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CF6)
    Sleep(50)

    def lambda_3D16():
        OP_8F(0xFE, 0xFFFFFEFC, 0x3E80, 0x1631E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3D16)
    Sleep(100)

    def lambda_3D36():
        OP_8F(0xFE, 0x3B6, 0x3E80, 0x1631E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3D36)
    WaitChrThread(0x101, 0x0)
    Sleep(100)

    ChrTalk(    #73
        0x101,
        "#1020F#1PKloe! Queen Alicia!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 26)
    SetChrChipByIndex(0x102, 28)
    SetChrChipByIndex(0xF8, 30)
    SetChrChipByIndex(0xF9, 32)

    ChrTalk(    #74
        0xF,
        "#403F#6PEstelle... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        "#093F#6PEveryone...thank you for coming.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E03")

    ChrTalk(    #76
        0x107,
        "#065F#5POh, no...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E70")

    label("loc_3E03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E2C")

    ChrTalk(    #77
        0x106,
        "#057F#5PDamn it...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E70")

    label("loc_3E2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E4E")

    ChrTalk(    #78
        0x103,
        "#523F#5PNo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E70")

    label("loc_3E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E70")

    ChrTalk(    #79
        0x108,
        "#077F#5PGuh...\x02",
    )

    CloseMessageWindow()

    label("loc_3E70")


    ChrTalk(    #80
        0x102,
        "#1043F#5PWe're too late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1005F#1PYou sons of... What do\x01",
            "you think you're doing?!\x02\x03",

            "Let go of Kloe and Her Majesty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xC,
        (
            "#1306F#6PHeehee! Sorry, but no.\x02\x03",

            "#261FThe professor asked us to do this\x01",
            "as a personal favor, so no can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1020F#1PThe professor?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        (
            "#1042F#5PWait, a personal...? So this has\x01",
            "nothing to do with the Gospel Plan,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        (
            "#263F#6PNope! Don't think so.\x02\x03",

            "#1305FHe said he wanted to slow you down\x01",
            "a little since you were doing more than\x01",
            "we thought you would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1019F#1POh, I'm so very sorry for trying to reverse\x01",
            "all the damage you guys are doing and\x01",
            "being a decent human being, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41AA")

    ChrTalk(    #87
        0xB,
        (
            "#252F#6PHeh, yeah, well, it's a pain.\x01",
            "You restored the guild phones, right?\x02\x03",

            "The professor wasn't a fan of that.\x02\x03",

            "He said he wanted to see you kids\x01",
            "flounderin' around a bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_427C")

    label("loc_41AA")


    ChrTalk(    #88
        0xD,
        (
            "#244F#6PIt HAS been problematic, you realize.\x01",
            "You restored the guild phones across\x01",
            "Liberl.\x02\x03",

            "#241FThe professor hadn't expected you to\x01",
            "do it so quickly.\x02\x03",

            "I gather he wanted to see you suffer a\x01",
            "little more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_427C")


    ChrTalk(    #89
        0x101,
        (
            "#1005F#1P...\x01",
            "What...in...?\x02\x03",

            "He had you attack Grancel for THAT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1043F#5PThat's...very like him.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43C6")

    ChrTalk(    #91
        0xD,
        (
            "#244F#6PIt is in fairly bad taste, I'll admit.\x02\x03",

            "#241FHowever, Loewe is securing the\x01",
            "floating city on his own.\x02\x03",

            "We had little better to do, so we\x01",
            "did the professor a favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        "#022F#5PLuci...why...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_44BC")

    label("loc_43C6")


    ChrTalk(    #93
        0xB,
        (
            "#250FYou got it. I thought it was a bit\x01",
            "lame myself.\x02\x03",

            "#252FThing is, Loewe got sent off to\x01",
            "secure that flyin' city alone.\x02\x03",

            "We had nothin' better to do, so we\x01",
            "said, sure, we'll throw you a bone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44BC")

    ChrTalk(    #94
        0x108,
        "#077F#5PWalter... Damn you!\x02",
    )

    CloseMessageWindow()

    label("loc_44BC")


    ChrTalk(    #95
        0xE,
        (
            "#094F#6P...I believe we understand now.\x02\x03",

            "#093FGiven that, am I not enough of a prize by\x01",
            "myself?\x02\x03",

            "Can I ask you to release Princess Klaudia?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)

    ChrTalk(    #96
        0xF,
        (
            "#402F#4PGrandmother, no!\x02\x03",

            "I'm the one who should...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "#230F#6PHmmmmm. It is true that the good\x01",
            "professor asked for one or the other...\x02\x03",

            "My, what a quandary we have on our\x01",
            "hands!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    ChrTalk(    #98
        0xD,
        (
            "#243F#4PWeren't you looking to take the\x01",
            "princess anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(300)

    ChrTalk(    #99
        0xA,
        (
            "#231F#6PHeh, well. A pet bird in a cage somehow\x01",
            "lacks charm.\x02\x03",

            "It may also be nice to see her elegance\x01",
            "shining even through captivity, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)
    Sleep(300)

    ChrTalk(    #100
        0xF,
        "#402F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1022F#1PYou, you... Don't even start...\x02\x03",

            "#1005FYou're REALLY out of your minds\x01",
            "if you think we'll let you do that!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_478D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_478D)
    Sleep(50)

    def lambda_47A0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47A0)
    Sleep(50)

    def lambda_47B3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_47B3)

    ChrTalk(    #102
        0xB,
        (
            "#252F#6PHa! Don't make me laugh.\x02\x03",

            "Even if we didn't have hostages,\x01",
            "are you seriously gonna take on\x01",
            "ALL of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        (
            "#261F#6PHeehee! That's riiight, I promised to\x01",
            "kill you all the next time we met.\x02\x03",

            "#1306FYou know what? This is a good chance.\x01",
            "Maybe I should just gut you all right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1020F#1PNgh...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(670, 16000, 93270, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(23000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, -220, 16000, 92550, 328)
    SetChrPos(0x102, 970, 16000, 92520, 328)
    SetChrPos(0xF8, -260, 16000, 90910, 328)
    SetChrPos(0xF9, 950, 16000, 90910, 328)
    OP_0D()

    ChrTalk(    #105
        0x102,
        (
            "#1035F#4P(Stay calm, Estelle.)\x02\x03",

            "#1042F(They're right. There's no way we can\x01",
            "fight all of them at once by ourselves.)\x02\x03",

            "(We need to wait for our chance.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1003F#6P(But...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "#231F#6PAh, alas, Joshua, it is fruitless.\x02\x03",

            "Perhaps had you been in the\x01",
            "shadows, you could have found\x01",
            "an opening. But as it stands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "#240F#4POut in the open like this,\x01",
            "your options are limited.\x02\x03",

            "There's little you can do,\x01",
            "Black Fang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1035F#4P...So it seems.\x02\x03",

            "#1040FIt also seems like I'm not the one\x01",
            "who needs to strike that opening.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)

    ChrTalk(    #110
        0xA,
        "#232F#6PWhat?\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10)
    Sleep(100)
    OP_1D(0x2C)
    Sleep(500)
    Fade(500)
    OP_6D(-3840, 18000, 103030, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 4)
    SetChrPos(0x11, -14000, 18000, 101730, 90)
    ClearChrFlags(0x11, 0x80)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0x21)
    Sleep(400)
    OP_43(0xC, 0x0, 0x0, 0x22)

    def lambda_4C3E():
        OP_6D(-2250, 18000, 102720, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C3E)

    def lambda_4C56():
        OP_67(0, 4650, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C56)

    def lambda_4C6E():
        OP_6B(2420, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C6E)
    OP_43(0xE, 0x0, 0x0, 0x24)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0xC, 0x0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0xC, 0x20)
    OP_22(0x9B, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xC, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)

    def lambda_4CE9():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_4CE9)

    def lambda_4D03():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4D03)

    def lambda_4D1D():
        OP_6E(391, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4D1D)

    def lambda_4D2D():
        OP_96(0xFE, 0xFFFFFB6E, 0x4650, 0x19118, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4D2D)

    def lambda_4D4B():
        OP_96(0xFE, 0xFFFFE746, 0x4650, 0x18F06, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4D4B)
    WaitChrThread(0x11, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xC, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xA, 0x0, 0x0, 0x23)
    Sleep(300)
    SetChrChipByIndex(0x11, 19)
    SetChrSubChip(0x11, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x11, 0xA, 0x64)
    OP_96(0x11, 0xFFFFE57A, 0x4650, 0x188DA, 0xC8, 0x1770)
    OP_7D(0x1, 0x11, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xA, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(    #111
        0x101,
        "#1004F#1PWhaaa...?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #112
        0x11,
        (
            "#701F#5PHello, everyone. Good work.\x02\x03",

            "#703FYour Majesty, Your Highness.\x01",
            "Forgive my tardiness.\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-1270, 18000, 103090, 800)

    ChrTalk(    #113
        0xF,
        "#409F#4PCid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        "#090F#4PThank you for coming.\x02",
    )

    CloseMessageWindow()
    Fade(225)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #115
        0xA,
        "#230F#4PAh. One of the Divine Blade's lieutenants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        (
            "#1306F#4PHeehee, that wasn't too bad!\x02\x03",

            "Just a bit more and you really\x01",
            "would've had us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        (
            "#701FYes, I'll admit I was surprised.\x02\x03",

            "#703FI didn't expect you to be able to\x01",
            "turn away such a blow so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#252F#4PAll right! This is turnin' into my kinda party.\x02\x03",

            "So you want to play, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x11,
        (
            "#703FI'll pass, for the moment.\x02\x03",

            "#701FReally, I'm just bait, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        "#254F#4PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        "#242F*gasp*!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 18)
    SetChrPos(0x10, -15190, 21000, 88030, 45)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x80)
    OP_22(0x197, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2590, 18000, 100370, 800)
    OP_43(0x10, 0x0, 0x0, 0x28)

    def lambda_50F1():
        OP_6D(2640, 18000, 103890, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50F1)

    def lambda_5109():
        OP_67(0, 6720, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5109)

    def lambda_5121():
        OP_6B(2170, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5121)

    def lambda_5131():
        OP_6C(21000, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5131)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #122
        0xD,
        "#245F#6PNnngh...\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x0, 0x0, 0x29)

    def lambda_5168():
        OP_6D(1730, 18750, 105300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5168)

    def lambda_5180():
        OP_67(0, 6520, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5180)

    def lambda_5198():
        OP_6B(2170, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5198)

    def lambda_51A8():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_51A8)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #123
        0xB,
        "#259F#3PTccch...\x02",
    )

    CloseMessageWindow()

    def lambda_51D8():
        OP_6D(-2940, 18610, 101150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51D8)

    def lambda_51F0():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51F0)

    def lambda_5200():
        OP_6E(300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5200)
    Sleep(1000)
    OP_43(0x11, 0x0, 0x0, 0x25)
    WaitChrThread(0x11, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0xC, 0x32, 0x64)
    OP_7D(0x0, 0xA, 0x32, 0x64)

    def lambda_5236():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5236)

    def lambda_5244():
        OP_96(0xFE, 0xFFFFF90C, 0x474A, 0x19668, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5244)

    def lambda_5262():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5262)

    def lambda_5270():
        OP_96(0xFE, 0xFFFFF98E, 0x4650, 0x18632, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5270)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #124 op#A op#5
        0xA,
        "#235F#10A#2PHmph!\x05\x02",
    )


    ChrTalk(    #125 op#A op#5
        0xC,
        "#1303F#10A#3PAaaah!\x05\x02",
    )

    Sleep(800)
    OP_7D(0x0, 0x11, 0x32, 0x64)
    OP_8C(0x11, 0, 800)
    SetChrChipByIndex(0x11, 21)

    def lambda_52E1():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_52E1)

    def lambda_52F1():
        OP_96(0xFE, 0xFFFFF808, 0x4650, 0x1930C, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_52F1)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_531E():
        OP_96(0xFE, 0xFFFFFA06, 0x4D26, 0x1A2D4, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_531E)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 180, 800)

    def lambda_5357():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5357)

    def lambda_5367():
        OP_96(0xFE, 0xFFFFF93E, 0x4650, 0x189DE, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5367)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0xA, 0x32, 0x1F4)
    SetChrChipByIndex(0xA, 36)

    def lambda_53A1():

        label("loc_53A1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_53A1")

    QueueWorkItem2(0xA, 2, lambda_53A1)

    def lambda_53B4():
        OP_96(0xFE, 0xFFFFF920, 0x5208, 0x17E08, 0xDAC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_53B4)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_7D(0x1, 0xA, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)

    def lambda_5401():

        label("loc_5401")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_5401")

    QueueWorkItem2(0x11, 2, lambda_5401)
    OP_43(0xA, 0x0, 0x0, 0x2D)
    Sleep(2000)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 23)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 20)

    def lambda_5432():
        OP_8F(0xFE, 0x104, 0x4650, 0x18F38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5432)

    def lambda_544D():
        OP_8F(0xFE, 0xFFFFFB3C, 0x4650, 0x18CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_544D)

    def lambda_5468():
        OP_8F(0xE, 0xFFFFFD62, 0x4650, 0x187EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5468)

    def lambda_5483():
        OP_8F(0xF, 0x21C, 0x4650, 0x188DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5483)

    def lambda_549E():
        OP_6D(960, 18500, 104830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_549E)

    def lambda_54B6():
        OP_67(0, 5600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54B6)

    def lambda_54CE():
        OP_6B(2910, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_54CE)

    def lambda_54DE():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_54DE)

    def lambda_54EE():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54EE)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 19)
    SetChrSubChip(0x11, 0)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0xC, 0x0, 0x0)
    OP_7D(0x1, 0xA, 0x0, 0x0)

    NpcTalk(    #126
        0x12,
        "Uniformed Man",
        "#115F#2PGood. I made it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xF,
        "#409FWhat in...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 1700, 16000, 92550, 328)
    SetChrPos(0x102, 2910, 16000, 92520, 328)
    SetChrPos(0xF8, 1700, 16000, 90910, 328)
    SetChrPos(0xF9, 2910, 16000, 90910, 328)

    def lambda_55BF():
        OP_6D(1120, 18500, 104420, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55BF)

    def lambda_55D7():
        OP_67(0, 6140, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_55D7)

    def lambda_55EF():
        OP_6B(2360, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55EF)

    def lambda_55FF():
        OP_6E(401, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_55FF)
    SetChrChipByIndex(0x101, 26)

    def lambda_5614():
        OP_8E(0xFE, 0x6A4, 0x4650, 0x18EA2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5614)
    Sleep(100)
    SetChrChipByIndex(0x102, 28)

    def lambda_5639():
        OP_8E(0xFE, 0xB5E, 0x4650, 0x18EB6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5639)
    Sleep(50)
    SetChrChipByIndex(0xF8, 30)

    def lambda_565E():
        OP_8E(0xFE, 0x6E0, 0x4650, 0x18894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_565E)
    Sleep(100)
    SetChrChipByIndex(0xF9, 32)

    def lambda_5683():
        OP_8E(0xFE, 0xB2C, 0x4650, 0x18894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5683)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 26)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 28)
    WaitChrThread(0xF8, 0x1)
    SetChrChipByIndex(0xF8, 30)
    WaitChrThread(0xF9, 0x1)
    SetChrChipByIndex(0xF9, 32)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56E7")

    ChrTalk(    #128
        0x106,
        "#055FWait a...\x02",
    )

    CloseMessageWindow()

    label("loc_56E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5707")

    ChrTalk(    #129
        0x107,
        "#065FHuuuh?!\x02",
    )

    CloseMessageWindow()

    label("loc_5707")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5729")

    ChrTalk(    #130
        0x103,
        "#023FOh, MY...\x02",
    )

    CloseMessageWindow()

    label("loc_5729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5754")

    ChrTalk(    #131
        0x108,
        "#073FTHAT'S unexpected.\x02",
    )

    CloseMessageWindow()

    label("loc_5754")


    ChrTalk(    #132
        0x101,
        "#1004F#2PR-R-R...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #133
        0x101,
        "#1005F#4S#2PRICHARD?! Colonel Richard?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #134
        0x12,
        (
            "#111F#5PHaha... Hello, Miss Bright.\x02\x03",

            "#110FYou shouldn't call me 'colonel,'\x01",
            "however.\x02\x03",

            "I have been stripped of my rank,\x01",
            "and am little more than a criminal\x01",
            "performing his penal service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1019F#2PBoy, that sure explains every\x01",
            "question I'd have about this.\x01",
            "'Don't call me colonel,' okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        "#096F#2PCol... Mr. Richard. It's been some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#115F#5PI am glad to see you and the\x01",
            "princess are well, Your Majesty.\x02\x03",

            "#112FI believe General Bright has already\x01",
            "briefed you on my circumstances...\x02\x03",

            "...so, please, allow me to shield\x01",
            "you from these criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        "#091F#2PBy all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xF,
        "#401F#2PThank you very much, Mr. Richard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#111F#5PThe pleasure is mine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016F#2PI sooo don't even know what's\x01",
            "going on anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#1040F#2PI think it's safe to say this story\x01",
            "is bigger than we are, as it were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "#232F#6PA pair of the Divine Blade's students...\x02\x03",

            "...our wayward Black Fang, and a group\x01",
            "of...better than average bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "#240F#6PI think we may have tarried for\x01",
            "too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x12,
        (
            "#115F#2PHeh. I appreciate the time, personally.\x02\x03",

            "#111FIncidentally, we've already handled\x01",
            "things in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_5C22():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C22)
    Sleep(50)

    def lambda_5C35():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C35)
    Sleep(50)

    def lambda_5C48():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5C48)
    Sleep(50)

    def lambda_5C5B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5C5B)
    Sleep(50)
    SetChrFlags(0xF, 0x20)

    def lambda_5C73():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5C73)

    def lambda_5C81():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C81)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_36A0 end

    def Function_32_5CA6(): pass

    label("Function_32_5CA6")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 13300, 23000, 107640, 225)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x10, 18)
    OP_8E(0x10, 0x550, 0x4C2C, 0x189C0, 0xFA0, 0x0)
    OP_8C(0x10, 315, 300)
    Sleep(500)
    OP_8F(0x10, 0x3D4, 0x477C, 0x189B6, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x10, 850, 18300, 100700, 3000)
    SetChrChipByIndex(0xF, 15)
    OP_0D()
    Return()

    # Function_32_5CA6 end

    def Function_33_5D1C(): pass

    label("Function_33_5D1C")

    OP_7D(0x0, 0x11, 0x32, 0x64)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 20)
    OP_8E(0x11, 0xFFFFE804, 0x4650, 0x18F06, 0x2710, 0x0)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)

    def lambda_5D57():
        OP_8F(0xFE, 0xFFFFF038, 0x490C, 0x18D8A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D57)

    def lambda_5D72():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D72)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_33_5D1C end

    def Function_34_5D8A(): pass

    label("Function_34_5D8A")

    OP_8C(0xFE, 270, 500)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_5DA1():
        OP_99(0xFE, 0xD, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5DA1)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 8)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0xFE, 0x32, 0x64)
    ClearChrFlags(0xFE, 0x20)

    def lambda_5DCD():
        OP_8F(0xFE, 0xFFFFF614, 0x490C, 0x18EB6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DCD)
    Sleep(200)

    def lambda_5DED():
        OP_99(0xFE, 0x7, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5DED)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_34_5D8A end

    def Function_35_5E05(): pass

    label("Function_35_5E05")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 4)

    def lambda_5E1D():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E1D)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5E37():
        OP_99(0xFE, 0x3, 0x6, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E37)

    def lambda_5E47():
        OP_96(0xFE, 0xFFFFF8E4, 0x4650, 0x189F2, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E47)
    Sleep(100)
    SetChrChipByIndex(0x1A, 35)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x1A, -1820, 18500, 100850, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x40)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_5E99():
        OP_8F(0xFE, 0xFFFFE250, 0x4650, 0x18D94, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5E99)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0x1A, 1)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_35_5E05 end

    def Function_36_5EC6(): pass

    label("Function_36_5EC6")


    def lambda_5ECC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5ECC)
    Sleep(50)

    def lambda_5EDF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5EDF)
    Sleep(50)

    def lambda_5EF2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5EF2)
    Sleep(50)

    def lambda_5F05():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5F05)
    Sleep(50)

    def lambda_5F18():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5F18)
    Return()

    # Function_36_5EC6 end

    def Function_37_5F21(): pass

    label("Function_37_5F21")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)

    def lambda_5F43():
        OP_99(0xFE, 0x1, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F43)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFEEB2, 0x4A38, 0x18628, 0x3E8, 0x1388)

    def lambda_5F6F():
        OP_8E(0xFE, 0xFFFFEEB2, 0x4650, 0x18628, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F6F)
    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0xFE, 0)

    def lambda_5F98():
        OP_6D(-680, 18000, 102860, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F98)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFF5D8, 0x4650, 0x18DC6, 0x1F4, 0x1388)
    SetChrSubChip(0xFE, 1)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_37_5F21 end

    def Function_38_5FDE(): pass

    label("Function_38_5FDE")

    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrPos(0xA, -1270, 18000, 101310, 270)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    Return()

    # Function_38_5FDE end

    def Function_39_6010(): pass

    label("Function_39_6010")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6025")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_39_6010")

    label("loc_6025")

    Return()

    # Function_39_6010 end

    def Function_40_6026(): pass

    label("Function_40_6026")


    def lambda_602C():

        label("loc_602C")

        TurnDirection(0xD, 0x10, 400)
        OP_48()
        Jump("loc_602C")

    QueueWorkItem2(0xD, 1, lambda_602C)
    OP_43(0x10, 0x1, 0x0, 0x27)
    OP_7D(0x0, 0xFE, 0x32, 0x64)
    OP_8F(0xFE, 0x898, 0x4970, 0x18C4A, 0x6D60, 0x0)
    SetChrChipByIndex(0xD, 10)
    SetChrSubChip(0xD, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_606F():
        OP_96(0xFE, 0x9B0, 0x4650, 0x194BA, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_606F)
    OP_8F(0xFE, 0x2670, 0x5D48, 0x1A5D6, 0x3E80, 0x0)
    OP_7D(0x1, 0x10, 0x0, 0x0)
    SetChrFlags(0xFE, 0x80)
    WaitChrThread(0xD, 0x1)

    def lambda_60B3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_60B3)
    Sleep(100)

    def lambda_60C6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_60C6)
    Sleep(100)
    OP_8C(0xE, 180, 400)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_40_6026 end

    def Function_41_60E3(): pass

    label("Function_41_60E3")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrChipByIndex(0x12, 23)
    SetChrPos(0x12, 10480, 18000, 96630, 315)
    SetChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)
    OP_8E(0x12, 0x198C, 0x4650, 0x18222, 0x2710, 0x0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_612A():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_612A)
    OP_96(0x12, 0x8F2, 0x4650, 0x1883A, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_6154():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6154)
    SetChrChipByIndex(0x12, 24)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x12, 0x1)

    def lambda_6171():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6171)

    def lambda_6181():
        OP_99(0xFE, 0x0, 0x9, 0xDAC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6181)

    def lambda_6191():
        OP_8F(0xFE, 0x960, 0x4650, 0x19258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6191)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xD, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)

    def lambda_61FC():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_61FC)

    def lambda_6216():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6216)
    OP_43(0xD, 0x1, 0x0, 0x2A)
    OP_8C(0xB, 90, 800)
    SetChrChipByIndex(0xB, 6)
    SetChrSubChip(0xB, 0)
    OP_43(0x12, 0x2, 0x0, 0x2C)
    OP_43(0xB, 0x0, 0x0, 0x2B)
    OP_8C(0xF, 0, 400)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0xB, 0x0)
    WaitChrThread(0x12, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_41_60E3 end

    def Function_42_6271(): pass

    label("Function_42_6271")

    OP_7D(0x0, 0xFE, 0x32, 0x64)

    def lambda_627F():
        OP_99(0xFE, 0x9, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_627F)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x91A, 0x493E, 0x19BB8, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x820, 0x4C2C, 0x1A1EE, 0x5DC, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_42_6271 end

    def Function_43_62DE(): pass

    label("Function_43_62DE")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_62FB():
        OP_8C(0xFE, 135, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62FB)
    OP_96(0xFE, 0x10E, 0x474A, 0x197D0, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_632F():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_632F)
    OP_96(0xFE, 0x3F2, 0x493E, 0x19B40, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0x212, 0x4D26, 0x1A374, 0x5DC, 0xFA0)
    SetChrSubChip(0xFE, 1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_43_62DE end

    def Function_44_63A0(): pass

    label("Function_44_63A0")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x20)
    OP_8C(0x12, 270, 800)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 2)

    def lambda_63C4():
        OP_96(0xFE, 0x6D6, 0x4650, 0x19442, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C4)
    OP_99(0xFE, 0x3, 0x5, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 315, 800)

    def lambda_63F7():
        OP_96(0xFE, 0x47E, 0x4650, 0x19618, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63F7)
    OP_99(0xFE, 0x6, 0x8, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 0, 800)

    def lambda_642A():
        OP_96(0xFE, 0x4BA, 0x474A, 0x19802, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_642A)
    OP_99(0xFE, 0x9, 0xF, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_44_63A0 end

    def Function_45_6459(): pass

    label("Function_45_6459")

    OP_7D(0x0, 0xA, 0x32, 0x1F4)
    OP_97(0xA, 0xFFFFFA24, 0x18A88, 0x249F0, 0x1B58, 0x1)
    OP_7D(0x1, 0xA, 0x0, 0x0)
    OP_8C(0xA, 180, 400)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    OP_8F(0xA, 0xFFFFFC18, 0x4A38, 0x19FA0, 0xFA0, 0x0)
    OP_44(0xA, 0x2)
    Fade(500)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -1000, 19500, 106400, 180)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0x11, 0x2)
    Return()

    # Function_45_6459 end

    def Function_46_64E0(): pass

    label("Function_46_64E0")

    EventBegin(0x0)
    OP_A3(0x10F2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64FA")
    Call(0, 56)
    Call(0, 57)

    label("loc_64FA")

    OP_D2(0x270266, 0x270270, 0x3)
    OP_D2(0x27026B, 0x270275, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x27026C, 0x270276, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x270257, 0x270261, 0x8)
    OP_D2(0x270252, 0x27025C, 0x9)
    OP_D2(0x270258, 0x270262, 0xA)
    OP_D2(0x70141, 0x70145, 0xB)
    OP_D2(0x70182, 0x70186, 0xF)
    OP_D2(0x2702EA, 0x2702F4, 0x13)
    OP_D2(0x2701D4, 0x2701D9, 0x14)
    OP_D2(0x702D2, 0x702D9, 0x16)
    OP_D2(0x2700B0, 0x2700B4, 0x17)
    OP_D2(0x704AA, 0x704AE, 0x18)
    OP_D2(0x270110, 0x270120, 0x1A)
    OP_D2(0x270130, 0x270140, 0x1C)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_65BD"),
        (2, "loc_65CA"),
        (6, "loc_65D7"),
        (7, "loc_65E4"),
        (SWITCH_DEFAULT, "loc_65F1"),
    )


    label("loc_65BD")

    OP_D2(0x70218, 0x70224, 0x1E)
    Jump("loc_65F1")

    label("loc_65CA")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    Jump("loc_65F1")

    label("loc_65D7")

    OP_D2(0x70230, 0x7023C, 0x1E)
    Jump("loc_65F1")

    label("loc_65E4")

    OP_D2(0x70248, 0x70254, 0x1E)
    Jump("loc_65F1")

    label("loc_65F1")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_660A"),
        (2, "loc_6617"),
        (6, "loc_6624"),
        (7, "loc_6631"),
        (SWITCH_DEFAULT, "loc_663E"),
    )


    label("loc_660A")

    OP_D2(0x70218, 0x70224, 0x20)
    Jump("loc_663E")

    label("loc_6617")

    OP_D2(0x701D0, 0x701DC, 0x20)
    Jump("loc_663E")

    label("loc_6624")

    OP_D2(0x70230, 0x7023C, 0x20)
    Jump("loc_663E")

    label("loc_6631")

    OP_D2(0x70248, 0x70254, 0x20)
    Jump("loc_663E")

    label("loc_663E")

    OP_D2(0x2600A0, 0x2600A5, 0x22)
    OP_D2(0x60028, 0x6002D, 0x23)
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 34)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 11)
    SetChrChipByIndex(0xF, 15)
    SetChrChipByIndex(0x11, 19)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x101, 26)
    SetChrChipByIndex(0x102, 28)
    SetChrChipByIndex(0xF8, 30)
    SetChrChipByIndex(0xF9, 32)
    SetChrPos(0x101, 1700, 18000, 102050, 180)
    SetChrPos(0x102, 2910, 18000, 102070, 180)
    SetChrPos(0xF8, 1760, 18000, 100500, 180)
    SetChrPos(0xF9, 2860, 18000, 100500, 180)
    SetChrPos(0x11, -1220, 18000, 101600, 0)
    SetChrPos(0x12, 260, 18000, 102200, 0)
    SetChrPos(0xE, -670, 18000, 100330, 180)
    SetChrPos(0xF, 540, 18000, 100570, 180)
    SetChrPos(0xC, -1530, 19750, 107270, 180)
    SetChrPos(0xA, -1000, 19500, 106400, 180)
    SetChrPos(0xB, 530, 19750, 107170, 180)
    SetChrPos(0xD, 1800, 19500, 106550, 180)
    SetChrPos(0x1A, -7600, 18000, 101780, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 35)
    SetChrSubChip(0x1A, 15)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    OP_6D(2280, 18000, 101560, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(33000, 0)
    OP_6E(401, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        (
            "#1004F#6PWhoa! The jaegers are being\x01",
            "pushed back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        "#1040F#6PVery impressive!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_689C")

    ChrTalk(    #149
        0x103,
        "#021F#6PHaven't lost their touch, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6908")

    label("loc_689C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D6")

    ChrTalk(    #150
        0x106,
        "#051F#6PHeh... Not too bad, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6908")

    label("loc_68D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6908")

    ChrTalk(    #151
        0x108,
        "#070F#6PNow that's impressive!\x02",
    )

    CloseMessageWindow()

    label("loc_6908")


    def lambda_690E():
        OP_6D(720, 19000, 105800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_690E)

    def lambda_6926():
        OP_67(0, 6080, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6926)

    def lambda_693E():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_693E)
    OP_8C(0x12, 0, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #152
        0x12,
        (
            "#112F#2PNow then, servants of Ouroboros.\x01",
            "What do you intend?\x02\x03",

            "You seemed quite eager for a fight.\x01",
            "Are we still desirous of violence?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69E4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69E4)
    Sleep(50)

    def lambda_69F7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69F7)
    Sleep(50)

    def lambda_6A0A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6A0A)
    Sleep(50)

    def lambda_6A1D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6A1D)
    Sleep(50)

    def lambda_6A30():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6A30)
    Sleep(50)
    SetChrFlags(0xF, 0x20)

    def lambda_6A48():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6A48)
    Sleep(400)

    ChrTalk(    #153
        0xB,
        "#254F#6PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xC,
        (
            "#266F#6P...You think you're funny?\x02\x03",

            "#262FIf it's gonna be like this,\x01",
            "I AM gonna call Pater-Ma--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#232F#6PStop, Renne. Our chance has\x01",
            "already slipped by.\x02\x03",

            "Trying to force the issue now would\x01",
            "only end in an ugly fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xD,
        (
            "#244F#6PThe capture of the royals was\x01",
            "ultimately an optional objective.\x02\x03",

            "#240FCome, let us pull back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        "#250F#6PHmph. Well, if we gotta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xC,
        "#262F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    OP_0D()
    SetChrChipByIndex(0xA, 6)
    PlayEffect(0x0, 0x0, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    Sleep(1500)

    ChrTalk(    #159
        0xA,
        (
            "#230F#6PLadies and gentlemen!\x01",
            "If you will pardon us.\x02\x03",

            "It should be just about time\x01",
            "for your next trial, however...\x02\x03",

            "I suggest you keep your wits\x01",
            "about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#1042F#2P...'Next trial'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1020F#2PWhat are you on about NOW?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        (
            "#244F#6PYou'll see soon enough.\x02\x03",

            "#241FGood day, then, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0xD, 8)
    Sleep(200)
    SetChrChipByIndex(0xD, 10)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    OP_43(0x1B, 0x0, 0x0, 0x30)
    OP_43(0x1C, 0x0, 0x0, 0x31)
    OP_43(0x1D, 0x0, 0x0, 0x32)
    OP_43(0x1E, 0x0, 0x0, 0x33)
    OP_43(0x1F, 0x0, 0x0, 0x34)
    OP_43(0x20, 0x0, 0x0, 0x35)
    OP_43(0x21, 0x0, 0x0, 0x36)
    OP_43(0x22, 0x0, 0x0, 0x37)
    Sleep(3000)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 8)
    OP_20(0xBB8)

    def lambda_6ECB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6ECB)

    def lambda_6EDD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_6EDD)

    def lambda_6EEF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6EEF)
    Sleep(300)

    def lambda_6F06():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6F06)

    def lambda_6F18():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6F18)

    def lambda_6F2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6F2A)
    Sleep(300)

    def lambda_6F41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6F41)

    def lambda_6F53():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6F53)

    def lambda_6F65():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6F65)
    Sleep(300)

    def lambda_6F7C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6F7C)

    def lambda_6F8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6F8E)

    def lambda_6FA0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6FA0)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2F)
    Sleep(500)

    ChrTalk(    #163
        0x101,
        "#1026F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1035F#2PThey've retreated...\x02",
    )

    CloseMessageWindow()
    OP_21()
    Sleep(100)
    OP_1D(0x1)
    Sleep(600)

    def lambda_7011():
        OP_6D(1170, 18000, 102460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7011)

    def lambda_7029():
        OP_67(0, 6050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7029)

    def lambda_7041():
        OP_6B(2330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7041)

    def lambda_7051():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7051)

    def lambda_7061():
        OP_6E(401, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7061)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrChipByIndex(0x11, 20)
    SetChrChipByIndex(0x12, 23)
    OP_0D()

    def lambda_709F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_709F)
    Sleep(50)

    def lambda_70B2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_70B2)
    Sleep(50)

    def lambda_70C5():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70C5)
    Sleep(50)

    def lambda_70D8():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70D8)
    Sleep(50)

    def lambda_70EB():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_70EB)
    Sleep(50)

    def lambda_70FE():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_70FE)
    Sleep(400)

    ChrTalk(    #165
        0x12,
        (
            "#110F#6PThe jaegers should pull out\x01",
            "of the city, as well.\x02\x03",

            "A shame we cannot pursue them,\x01",
            "but I suppose we can't be selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1020F#4PYeah... Er, wait! WAY more importantly!\x02\x03",

            "#1019FSo just what in the heck is COLONEL\x01",
            "RICHARD doing here?!\x02\x03",

            "I thought you were in prison for the\x01",
            "seriously grievous crime of being a\x01",
            "huge jerk!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    Sleep(300)

    ChrTalk(    #167
        0x12,
        "#115F#6PI said, I'm not a... Well, regardless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        (
            "#701F#5PBefore any of that, we\x01",
            "have to secure the city.\x02\x03",

            "Would you help us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1006F#4PEr, well...sure, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#1040F#4PWe'll help tend to the wounded\x01",
            "and with firefighting.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_22(0x87, 0x1, 0x3C)
    OP_22(0xAE, 0x1, 0x3C)
    Sleep(100)
    OP_22(0x87, 0x1, 0x32)
    OP_22(0xAE, 0x1, 0x32)
    Sleep(100)
    OP_22(0x87, 0x1, 0x28)
    OP_22(0xAE, 0x1, 0x28)
    Sleep(100)
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    Sleep(100)
    OP_22(0x87, 0x1, 0x14)
    OP_22(0xAE, 0x1, 0x14)
    Sleep(100)
    OP_22(0x87, 0x1, 0xA)
    OP_22(0xAE, 0x1, 0xA)
    Sleep(100)
    OP_23(0x87)
    OP_23(0xAE)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #171
        (
            "\x07\x05And so...with great difficulty, the society's invasion of Grancel\x01",
            "was repelled.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #172
        (
            "\x07\x05Estelle's group ran around the city, fighting fires and helping\x01",
            "the confused citizenry...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #173
        (
            "\x07\x05Eventually, the rest of the team arrived, having been contacted\x01",
            "by Elnan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x9C, 0x4, 0x10)
    OP_AF(0xCD, 0x9C)
    Sleep(1000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_46_64E0 end

    def Function_47_74FB(): pass

    label("Function_47_74FB")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_47_74FB end

    def Function_48_7543(): pass

    label("Function_48_7543")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    SetChrPos(0xFE, -1000, 19500, 106400, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_75C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75FC")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_75C8")

    label("loc_75FC")

    Return()

    # Function_48_7543 end

    def Function_49_75FD(): pass

    label("Function_49_75FD")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    SetChrPos(0xFE, -1000, 19500, 106400, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_7682")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76B6")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_7682")

    label("loc_76B6")

    Return()

    # Function_49_75FD end

    def Function_50_76B7(): pass

    label("Function_50_76B7")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 530, 19750, 107380, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_773C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7770")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_773C")

    label("loc_7770")

    Return()

    # Function_50_76B7 end

    def Function_51_7771(): pass

    label("Function_51_7771")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 530, 19750, 107380, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_77F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_782A")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_77F6")

    label("loc_782A")

    Return()

    # Function_51_7771 end

    def Function_52_782B(): pass

    label("Function_52_782B")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -1530, 19750, 107220, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_78B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78E4")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_78B0")

    label("loc_78E4")

    Return()

    # Function_52_782B end

    def Function_53_78E5(): pass

    label("Function_53_78E5")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -1530, 19750, 107220, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_796A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_799E")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_796A")

    label("loc_799E")

    Return()

    # Function_53_78E5 end

    def Function_54_799F(): pass

    label("Function_54_799F")

    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 2080, 19500, 106990, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_7A24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A58")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_7A24")

    label("loc_7A58")

    Return()

    # Function_54_799F end

    def Function_55_7A59(): pass

    label("Function_55_7A59")

    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 2080, 19500, 106990, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_7ADE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B12")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_7ADE")

    label("loc_7B12")

    Return()

    # Function_55_7A59 end

    def Function_56_7B13(): pass

    label("Function_56_7B13")

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
        (0, "loc_7B8C"),
        (1, "loc_7B92"),
        (SWITCH_DEFAULT, "loc_7B98"),
    )


    label("loc_7B8C")

    OP_A2(0x1200)
    Jump("loc_7B98")

    label("loc_7B92")

    OP_A2(0x1201)
    Jump("loc_7B98")

    label("loc_7B98")

    Return()

    # Function_56_7B13 end

    def Function_57_7B99(): pass

    label("Function_57_7B99")

    ClearMapFlags(0x1)
    OP_6D(-67910, 0, 1890, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_57_7B99 end

    SaveToFile()

Try(main)
