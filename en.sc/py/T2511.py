from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2511   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2511.x',
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
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Targeting Camera',                     # 11
        'Deborah',                              # 12
        'Rhody',                                # 13
        'Richelle',                             # 14
        'Mickey',                               # 15
        'Dorothy',                              # 16
        'Roy',                                  # 17
        'Monika',                               # 18
        'Mr. Effort',                           # 19
        'Mr. Ratio',                            # 20
        'Ms. Wiola',                            # 21
        'Ms. Millia',                           # 22
        'Taylor',                               # 23
        'Enhanced Jaeger',                      # 24
        'Enhanced Jaeger',                      # 25
        'Enhanced Jaeger',                      # 26
        'Enhanced Jaeger',                      # 27
        'Enhanced Jaeger',                      # 28
        'Enhanced Jaeger',                      # 29
        'Purity',                               # 30
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT27/CH03004 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01360 ._CH',             # 04
        'ED6_DT07/CH01590 ._CH',             # 05
        'ED6_DT07/CH01080 ._CH',             # 06
        'ED6_DT06/CH20063 ._CH',             # 07
        'ED6_DT06/CH20064 ._CH',             # 08
        'ED6_DT07/CH01580 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT26/CH20396 ._CH',             # 0B
        'ED6_DT07/CH01460 ._CH',             # 0C
        'ED6_DT07/CH01660 ._CH',             # 0D
        'ED6_DT07/CH01210 ._CH',             # 0E
        'ED6_DT07/CH01430 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT27/CH03004P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01360P._CP',             # 04
        'ED6_DT07/CH01590P._CP',             # 05
        'ED6_DT07/CH01080P._CP',             # 06
        'ED6_DT06/CH20063P._CP',             # 07
        'ED6_DT06/CH20064P._CP',             # 08
        'ED6_DT07/CH01580P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT26/CH20396P._CP',             # 0B
        'ED6_DT07/CH01460P._CP',             # 0C
        'ED6_DT07/CH01660P._CP',             # 0D
        'ED6_DT07/CH01210P._CP',             # 0E
        'ED6_DT07/CH01430P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -31990,
        Z                   = 0,
        Y                   = 26660,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 29790,
        Z                   = 0,
        Y                   = 29100,
        Direction           = 0,
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
        X                   = 5350,
        Z                   = 0,
        Y                   = -2630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3450,
        Z                   = 0,
        Y                   = 240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -28450,
        Z                   = 0,
        Y                   = 27900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 27930,
        Z                   = 0,
        Y                   = 28500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 30410,
        Z                   = 0,
        Y                   = 25950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = -31760,
        Z                   = 0,
        Y                   = 58850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 60,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )


    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_496",          # 00, 0
        "Function_1_773",          # 01, 1
        "Function_2_81A",          # 02, 2
        "Function_3_92D",          # 03, 3
        "Function_4_AEB",          # 04, 4
        "Function_5_BC4",          # 05, 5
        "Function_6_10BE",         # 06, 6
        "Function_7_18A5",         # 07, 7
        "Function_8_1A25",         # 08, 8
        "Function_9_1B71",         # 09, 9
        "Function_10_1E50",        # 0A, 10
        "Function_11_1E55",        # 0B, 11
        "Function_12_23DF",        # 0C, 12
        "Function_13_2787",        # 0D, 13
        "Function_14_282A",        # 0E, 14
        "Function_15_28F3",        # 0F, 15
        "Function_16_2988",        # 10, 16
        "Function_17_2A4B",        # 11, 17
        "Function_18_3409",        # 12, 18
        "Function_19_3458",        # 13, 19
        "Function_20_34AC",        # 14, 20
        "Function_21_3500",        # 15, 21
        "Function_22_3554",        # 16, 22
        "Function_23_36D7",        # 17, 23
        "Function_24_37F3",        # 18, 24
        "Function_25_4402",        # 19, 25
        "Function_26_4453",        # 1A, 26
        "Function_27_44CC",        # 1B, 27
        "Function_28_4545",        # 1C, 28
        "Function_29_533D",        # 1D, 29
        "Function_30_678A",        # 1E, 30
        "Function_31_67CE",        # 1F, 31
        "Function_32_67FE",        # 20, 32
        "Function_33_6A7A",        # 21, 33
        "Function_34_6BD2",        # 22, 34
        "Function_35_6C0F",        # 23, 35
        "Function_36_6C7A",        # 24, 36
        "Function_37_6C83",        # 25, 37
        "Function_38_6F6B",        # 26, 38
        "Function_39_7098",        # 27, 39
        "Function_40_70E8",        # 28, 40
        "Function_41_7138",        # 29, 41
        "Function_42_7188",        # 2A, 42
        "Function_43_71D8",        # 2B, 43
        "Function_44_71ED",        # 2C, 44
        "Function_45_7202",        # 2D, 45
        "Function_46_7217",        # 2E, 46
        "Function_47_7240",        # 2F, 47
        "Function_48_76F7",        # 30, 48
        "Function_49_7746",        # 31, 49
        "Function_50_77A9",        # 32, 50
        "Function_51_780C",        # 33, 51
        "Function_52_786F",        # 34, 52
        "Function_53_7EC4",        # 35, 53
        "Function_54_7F27",        # 36, 54
        "Function_55_7F8A",        # 37, 55
        "Function_56_7FED",        # 38, 56
        "Function_57_803C",        # 39, 57
        "Function_58_80D4",        # 3A, 58
        "Function_59_812D",        # 3B, 59
        "Function_60_8131",        # 3C, 60
        "Function_61_8135",        # 3D, 61
        "Function_62_8139",        # 3E, 62
    )


    def Function_0_496(): pass

    label("Function_0_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_509")
    SetChrPos(0x9, 30280, 0, 53800, 0)
    SetChrPos(0x8, 30850, 0, 55200, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x10, 5350, 0, -10, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 31330, 0, 24430, 164)
    Jump("loc_69C")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_5F0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x12, -31080, 0, 27210, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -31090, 0, 25690, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x14, 30390, 0, 27920, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 30980, 0, 26960, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xB, 30510, 0, 25690, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_END)), "loc_5ED")
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 18)
    SetChrSubChip(0x17, 8)
    ClearChrFlags(0x18, 0x1)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 18)
    SetChrSubChip(0x18, 11)
    SetChrPos(0x17, 1340, 0, 39800, 0)
    SetChrPos(0x18, -2270, 0, 40010, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_5ED")

    Jump("loc_69C")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_61F")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, 31110, 0, 53120, 90)
    Jump("loc_69C")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_646")
    SetChrPos(0x8, 1400, 0, -2100, 180)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jump("loc_69C")

    label("loc_646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_655")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_69C")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_69C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -28500, 0, 58160, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_END)), "loc_697")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 5350, 0, -2630, 0)
    Jump("loc_69C")

    label("loc_697")

    SetChrFlags(0xE, 0x80)

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6B2")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_772")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6D1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 32)
    Jump("loc_772")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_6E7")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 33)
    Jump("loc_772")

    label("loc_6E7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_6FF"),
        (108, "loc_712"),
        (110, "loc_742"),
        (111, "loc_75A"),
        (SWITCH_DEFAULT, "loc_772"),
    )


    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70F")
    Event(0, 36)

    label("loc_70F")

    Jump("loc_772")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72A")
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_73F")

    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73F")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_73F")

    Jump("loc_772")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_757")

    Jump("loc_772")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76F")
    SetMapFlags(0x10000000)
    Event(0, 52)

    label("loc_76F")

    Jump("loc_772")

    label("loc_772")

    Return()

    # Function_0_496 end

    def Function_1_773(): pass

    label("Function_1_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_77D")
    Jump("loc_7C1")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_79C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 1)), scpexpr(EXPR_END)), "loc_795")
    OP_D2(0x26020B, 0x260210, 0x12)

    label("loc_795")

    OP_64(0x0, 0x1)
    Jump("loc_7C1")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_7A6")
    Jump("loc_7C1")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_7C1")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_7BA")
    Jump("loc_7C1")

    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_7C1")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D9")
    OP_B1("t2511_y")
    Jump("loc_7E2")

    label("loc_7D9")

    OP_B1("t2511_n")

    label("loc_7E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_7EC")
    Jump("loc_819")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_804")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_819")

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_819")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_819")

    Return()

    # Function_1_773 end

    def Function_2_81A(): pass

    label("Function_2_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_822")
    Return()

    label("loc_822")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_843")
    Jump("loc_844")

    label("loc_843")

    Return()

    label("loc_844")

    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_858")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92C")
    OP_8D(0xFE, 2050, 280, 6480, 1790, 2000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_924")
    OP_8B(0xFE, 0xEBA, 0xF78, 0x190)
    Sleep(400)
    OP_A2(0x3)
    SetChrChipByIndex(0xFE, 8)
    Sleep(2000)

    label("loc_8B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_917")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xF, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_914")
    Jump("loc_917")

    label("loc_914")

    Jump("loc_8B0")

    label("loc_917")

    Sleep(600)
    SetChrChipByIndex(0xFE, 7)
    OP_A3(0x3)

    label("loc_924")

    Sleep(400)
    Jump("loc_858")

    label("loc_92C")

    Return()

    # Function_2_81A end

    def Function_3_92D(): pass

    label("Function_3_92D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_9BA")

    ChrTalk(    #0
        0xFE,
        (
            "There was someone suspicious\x01",
            "hiding out in the old schoolhouse,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Sounds super scary, but also kind\x01",
            "of exciting!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7")

    label("loc_9BA")

    OP_A2(0x8)

    ChrTalk(    #2
        0xFE,
        "I just heard the juiciest rumor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Okay, so they're saying there was\x01",
            "someone suspicious hiding out in\x01",
            "the old schoolhouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "How exciting! It's like something\x01",
            "straight out of a novel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It's probably not the best thing to be\x01",
            "excited about, but it does fire up the\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7")

    TalkEnd(0xFE)
    Return()

    # Function_3_92D end

    def Function_4_AEB(): pass

    label("Function_4_AEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B1D")

    ChrTalk(    #6
        0xFE,
        "Today's as dull as ever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B60")

    label("loc_B1D")

    OP_A2(0x4)

    ChrTalk(    #7
        0xFE,
        "Hey, did you find anything out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "All right! FOOD TIME.\x02",
    )

    CloseMessageWindow()

    label("loc_B60")

    Jump("loc_BC0")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_BC0")

    ChrTalk(    #9
        0xFE,
        "What should I eat today...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Maybe I should just stick to the\x01",
            "meal set or...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC0")

    TalkEnd(0xFE)
    Return()

    # Function_4_AEB end

    def Function_5_BC4(): pass

    label("Function_5_BC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C49")

    ChrTalk(    #11
        0xFE,
        (
            "If you're looking for Jill,\x01",
            "she went off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "She said she had some\x01",
            "Student Council stuff to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCD")

    label("loc_C49")


    ChrTalk(    #13
        0xFE,
        "What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If you're looking for Jill,\x01",
            "she went off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "She said she had some\x01",
            "Student Council stuff to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_CCD")

    Jump("loc_10BA")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_D36")

    ChrTalk(    #16
        0xFE,
        "YES! Club starts up again tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I'm gonna fire a billion arrows\x01",
            "for practice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BA")

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_10BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D8C")

    ChrTalk(    #18
        0xFE,
        "Hey, hey? What happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Aww, come on. Tell me!\x01",
            "Pleeeease?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BA")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 5)), scpexpr(EXPR_END)), "loc_E0C")

    ChrTalk(    #20
        0xFE,
        (
            "Something weird happened during\x01",
            "exams, but I don't know the details.\x01",
            "I wish I knew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "So what was it, anyway?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BA")

    label("loc_E0C")

    OP_A2(0x7)
    OP_A2(0x1235)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #22
        0x101,
        "#1000FUm, got a sec?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Huh, do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002FYeah, I've got a question for you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #26
        0xFE,
        "A strange event during exam period...?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #27
        0xFE,
        (
            "Oooooh, like what? That sounds\x01",
            "fascinating! Did something happen?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        (
            "#1019FYou're entirely too excited about this,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        "#045FI-It probably means she doesn't know anything...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #30
        0x101,
        "#1007FGuess we gotta go somewhere else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "So, what happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Hey, come on. Tell meeeeeeeee.\x02",
    )

    CloseMessageWindow()

    label("loc_10BA")

    TalkEnd(0xFE)
    Return()

    # Function_5_BC4 end

    def Function_6_10BE(): pass

    label("Function_6_10BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(    #33
        0xFE,
        "You guys getting something to eat, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Once everything was settled and\x01",
            "I calmed down, I got real hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Haha. Guess it really doesn't take\x01",
            "much for people to put the past behind\x01",
            "them, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1232")

    label("loc_11A4")


    ChrTalk(    #36
        0xFE,
        (
            "The second I let myself relax,\x01",
            "I was STARVING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Haha. Guess it really doesn't take\x01",
            "much for people to put the past behind\x01",
            "them, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1232")

    Jump("loc_18A1")

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_13FA")
    TurnDirection(0xFE, 0x105, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(    #38
        0xFE,
        (
            "My match with Kloe will have to\x01",
            "wait until after break is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "But I'll be training between now and\x01",
            "then, so she better watch out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F7")

    label("loc_12DB")

    OP_A2(0x6)

    ChrTalk(    #40
        0xFE,
        (
            "I heard that you'll be going on break,\x01",
            "Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I was looking forward to our match,\x01",
            "too! It's a shame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#045FI'm sorry, Roy.\x02\x03",

            "I'll make it up to you when I come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Haha, I'll hold you to that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I'll be training between now and\x01",
            "then, so you better watch out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F7")

    Jump("loc_18A1")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_147E")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #45
        0xFE,
        (
            "Although, please be gentle with me\x01",
            "at the next club meeting, Kloe. I can\x01",
            "only take so many beatings...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150E")

    label("loc_147E")

    OP_A2(0x6)

    ChrTalk(    #46
        0xFE,
        (
            "From tomorrow onward, I'll be\x01",
            "practicing as hard as I can in the\x01",
            "name of the Fencing Club!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "I'd better prepare my gear while I can.\x02",
    )

    CloseMessageWindow()

    label("loc_150E")

    Jump("loc_18A1")

    label("loc_1511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_18A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 0)), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(    #48
        0xFE,
        (
            "Nothing really happened that I know of\x01",
            "during the exam period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I know there are weird rumors floating\x01",
            "around, but can't say I know the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A1")

    label("loc_15BC")

    OP_A2(0x1230)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #50
        0xFE,
        "Yo, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Are you getting ready for club, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#040FNo, I'm afraid not. Unfortunately,\x01",
            "I don't have the time right now.\x02\x03",

            "I'm checking around the school for\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "Huh? Checking for what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1002FWell, you see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #55
        (
            "\x07\x05Estelle explained that they were looking into any strange\x01",
            "events that might have occurred during the exam period.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #56
        0xFE,
        "Strange events?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Sorry, don't remember anything like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I know there are weird rumors floating\x01",
            "around, but can't say I know the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015FI see.\x02\x03",

            "Either way, thanks. We'll try someone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "I'm sorry I couldn't be more helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1000FNo worries.\x02\x03",

            "Thanks for your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "No problem.\x02",
    )

    CloseMessageWindow()

    label("loc_18A1")

    TalkEnd(0xFE)
    Return()

    # Function_6_10BE end

    def Function_7_18A5(): pass

    label("Function_7_18A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 3)), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #63
        0xF,
        (
            "#150FLet's seeee...\x01",
            "Next is a picture of the food!\x02\x03",

            "It looks so gooood. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A21")

    label("loc_1902")

    OP_A2(0x1263)
    TurnDirection(0xF, 0x101, 0)
    SetChrChipByIndex(0xFE, 7)
    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #64
        0x101,
        (
            "#1011FUh, Dorothy.\x02\x03",

            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        (
            "#150FI'm taking BEAUTIFUL pictures of the cafeteria.\x02\x03",

            "#151FI got some really cute shots of the seafood jelly.\x01",
            "It's sooooo jiggly. Pretty good, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1007F(I don't know what I expected...)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A21")
    SetChrChipByIndex(0xFE, 8)

    label("loc_1A21")

    TalkEnd(0xFE)
    Return()

    # Function_7_18A5 end

    def Function_8_1A25(): pass

    label("Function_8_1A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A59")

    ChrTalk(    #67
        0xFE,
        "Awww, goodbyes are so depressing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B6D")

    label("loc_1A59")

    OP_A2(0x1)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #68
        0xFE,
        "Kloe! Kloeee...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Uuuhh, I'm so sad. I thought we'd\x01",
            "both work together at club!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        (
            "#045FI'm sorry, Richelle.\x02\x03",

            "We'll practice hard together once\x01",
            "break is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "Oh, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I'll train my butt off until then,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        "#041FHaha, I can't wait.\x02",
    )

    CloseMessageWindow()

    label("loc_1B6D")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A25 end

    def Function_9_1B71(): pass

    label("Function_9_1B71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(    #74
        0xFE,
        "Man, bracers are so cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I've always thought way about bracers,\x01",
            "but seriously! They never fail to impress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Estelle, Joshua, you two should be\x01",
            "proud of yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I don't know what the future has in\x01",
            "store for me, but I hope it's something\x01",
            "as great as what you guys are doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1D2C")

    label("loc_1CB4")


    ChrTalk(    #78
        0xFE,
        "Man, bracers are so cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I've always thought way about bracers,\x01",
            "but seriously! They never fail to impress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2C")

    Jump("loc_1E4C")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D96")

    ChrTalk(    #80
        0xFE,
        "Clubs start up again today! Woo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I gotta get ready early so I can nab\x01",
            "a good spot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1D96")

    OP_A2(0x0)

    ChrTalk(    #82
        0xFE,
        "Clubs start up again today! Woo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I gotta get ready early so I can nab\x01",
            "a good spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I'm kinda worried my skills with\x01",
            "the bow have gotten rusty over the\x01",
            "exam period.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1B71 end

    def Function_10_1E50(): pass

    label("Function_10_1E50")

    Call(0, 11)
    Return()

    # Function_10_1E50 end

    def Function_11_1E55(): pass

    label("Function_11_1E55")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF2")

    ChrTalk(    #85
        0xB,
        (
            "Helping people is good and all,\x01",
            "but do be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xB,
        (
            "If the savior needs saving, well,\x01",
            "there's not much left, is there?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1F2A")

    label("loc_1EF2")


    ChrTalk(    #87
        0xB,
        (
            "Helping people is good and all,\x01",
            "but do be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2A")

    TalkEnd(0xB)
    Return()

    label("loc_1F2E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Young Lady Plate] - 800 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA9")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20BF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2085")
    SubMira(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #88
        "\x06Ate #2CYoung Lady Plate#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x4B0)
    OP_31(0x1, 0xFD, 0x4B0)
    OP_31(0x2, 0xFD, 0x4B0)
    OP_31(0x3, 0xFD, 0x4B0)
    OP_31(0x4, 0xFD, 0x4B0)
    OP_31(0x5, 0xFD, 0x4B0)
    OP_31(0x6, 0xFD, 0x4B0)
    OP_31(0x7, 0xFD, 0x4B0)
    OP_31(0x8, 0xFD, 0x4B0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2077")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_2045")
    Jump("loc_2077")

    label("loc_2045")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #89
        "\x06Learned [#2CYoung Lady Plate#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_2077")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_20AD")

    label("loc_2085")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #90
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_20AD")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_20BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D9")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_20D9")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215A")

    ChrTalk(    #91
        0xB,
        "Hey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        (
            "You're hungry, right? Make sure you eat!\x01",
            "No good comes from an empty stomach.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_21D7")

    label("loc_215A")


    ChrTalk(    #93
        0xB,
        (
            "Even without orbal devices,\x01",
            "I can still cook a mean lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "I'm a housewife! An orbal blackout's\x01",
            "got nothing on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D7")

    Jump("loc_23DB")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2252")

    ChrTalk(    #95
        0xB,
        "Phew! School with be on break soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xB,
        (
            "Knowing vacation is near always\x01",
            "makes the students brighten up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DB")

    label("loc_2252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_2377")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22FB")

    ChrTalk(    #97
        0xB,
        (
            "Clubs are starting up again now\x01",
            "that exams are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xB,
        (
            "Go exercise like crazy! And when\x01",
            "you're done, be sure to come here\x01",
            "and stuff your faces.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2374")

    label("loc_22FB")

    OP_A2(0x3)

    ChrTalk(    #99
        0xB,
        "At last, exam period is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xB,
        (
            "Students always seem to put\x01",
            "their health last during exams.\x01",
            "It worries me so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    Jump("loc_23DB")

    label("loc_2377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_23DB")

    ChrTalk(    #101
        0xB,
        "Good work with your tests.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "You're hungry, right? Go on!\x01",
            "Order whatever you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DB")

    TalkEnd(0xB)
    Return()

    # Function_11_1E55 end

    def Function_12_23DF(): pass

    label("Function_12_23DF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2459")

    ChrTalk(    #103
        0x9,
        (
            "#731FOnce it's all cleared up, let's go\x01",
            "have some fun at the cafeteria.\x02\x03",

            "#730FOkay, you two be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_264B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_251B")

    ChrTalk(    #104
        0x9,
        (
            "#730FSure, it's a spooky schoolhouse\x01",
            "now, but before that it was an old\x01",
            "fortress.\x02\x03",

            "It wouldn't be all that surprising\x01",
            "if it ended up having a few secret\x01",
            "underground rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2648")

    label("loc_251B")

    OP_A2(0x2)

    ChrTalk(    #105
        0x9,
        (
            "#730FA hidden staircase?\x02\x03",

            "There wasn't anything like that\x01",
            "mentioned in the documents.\x02\x03",

            "Anything's possible, though. I never\x01",
            "told you this, but before it was a spooky\x01",
            "schoolhouse, it was an old fortress.\x02\x03",

            "It wouldn't be all that surprising\x01",
            "if it ended up having a few secret\x01",
            "underground rooms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2648")

    Jump("loc_2783")

    label("loc_264B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_269F")

    ChrTalk(    #106
        0x9,
        (
            "#730FWe'll be on standby here in case\x01",
            "anything happens.\x02\x03",

            "Be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_269F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 7)), scpexpr(EXPR_END)), "loc_277C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26F9")

    ChrTalk(    #107
        0x9,
        (
            "#730FSorry to take up your time.\x02\x03",

            "Good luck with the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2779")

    label("loc_26F9")


    ChrTalk(    #108
        0x9,
        (
            "#730FHow's the investigation going?\x02\x03",

            "Things are going smoothly on\x01",
            "our end.\x02\x03",

            "There's not much left to check,\x01",
            "document-wise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2779")

    Jump("loc_2783")

    label("loc_277C")

    Call(0, 28)
    OP_A2(0x2)

    label("loc_2783")

    TalkEnd(0x9)
    Return()

    # Function_12_23DF end

    def Function_13_2787(): pass

    label("Function_13_2787")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_END)), "loc_2826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F6")

    ChrTalk(    #109
        0xFE,
        "I can't do anything. I feel so helpless...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Take care of our students for us!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_2826")

    label("loc_27F6")


    ChrTalk(    #111
        0xFE,
        "I can't do anything. I feel so helpless...\x02",
    )

    CloseMessageWindow()

    label("loc_2826")

    TalkEnd(0x12)
    Return()

    # Function_13_2787 end

    def Function_14_282A(): pass

    label("Function_14_282A")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 2)), scpexpr(EXPR_END)), "loc_28EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C6")

    ChrTalk(    #112
        0xFE,
        "Please...take care of our students.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "If something happens, come back\x01",
            "at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "We'll assist you as much as we can.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_28EF")

    label("loc_28C6")


    ChrTalk(    #115
        0xFE,
        "Please...take care of our students.\x02",
    )

    CloseMessageWindow()

    label("loc_28EF")

    TalkEnd(0x13)
    Return()

    # Function_14_282A end

    def Function_15_28F3(): pass

    label("Function_15_28F3")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_END)), "loc_2984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295B")

    ChrTalk(    #116
        0xFE,
        "Please...take care of our students.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "And take care of yourselves, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2984")

    label("loc_295B")


    ChrTalk(    #118
        0xFE,
        "Please...take care of our students.\x02",
    )

    CloseMessageWindow()

    label("loc_2984")

    TalkEnd(0x14)
    Return()

    # Function_15_28F3 end

    def Function_16_2988(): pass

    label("Function_16_2988")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 3)), scpexpr(EXPR_END)), "loc_2A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A05")

    ChrTalk(    #119
        0xFE,
        "It's still dangerous outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "We'll be on standby here.\x01",
            "Please, take care of our students.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_2A47")

    label("loc_2A05")


    ChrTalk(    #121
        0xFE,
        (
            "We'll be on standby here.\x01",
            "Please, take care of our students.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A47")

    TalkEnd(0x15)
    Return()

    # Function_16_2988 end

    def Function_17_2A4B(): pass

    label("Function_17_2A4B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A62")
    Call(0, 57)
    Call(0, 58)

    label("loc_2A62")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x9, 0)
    OP_6D(31390, 0, 55630, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2B19():
        OP_6D(29500, 0, 55100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B19)
    OP_43(0x101, 0x1, 0x0, 0x13)
    OP_43(0x102, 0x1, 0x0, 0x12)
    OP_43(0xF8, 0x1, 0x0, 0x15)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    OP_8C(0x9, 270, 400)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #122
        0x8,
        "#648F#4POhh, here they are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        "#731F#4PHey, hey! Things going okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1016F#6PSorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#1040F#6PYeah. I'm sure you've got a lot\x01",
            "on your plate, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "#730F#4PNah. We were just waiting,\x01",
            "for the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#644F#4PThis stuff is cake for members\x01",
            "of the Student Council.\x02\x03",

            "#645FNow's the real hard part, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        (
            "#1035F#6PYeah, you're right.\x02\x03",

            "#1043FYou'll be starting a new term under\x01",
            "these conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1004F#6POh, I guess you will, huh?\x02\x03",

            "#1015FWill things be okay here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#735F#4P...For now.\x02\x03",

            "#730FWe're trying to think up what we\x01",
            "can do as the Student Council.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#644F#4PAfter all, it's our academy.\x02\x03",

            "We want to do as much as we can\x01",
            "ourselves.\x02\x03",

            "#648FFor your sake, and for Kloe's, too.\x01",
            "She's already the best she can over\x01",
            "at the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1017F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "#731F#4POnce everything's settled, come by the\x01",
            "academy again.\x02\x03",

            "We'll get Kloe and have a party in\x01",
            "the cafeteria, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#641F#4PIn that case, we should get those\x01",
            "costumes from the school play and\x01",
            "make it a costume party!\x02\x03",

            "#648FAfter all, we'll have both knights AND\x01",
            "our fair princess in attendance. Heh.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #135
        0x101,
        (
            "#1018F#6PHaha, yeah! That sounds like it could\x01",
            "be really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1052F#6PFor some us, maybe...\x02\x03",

            "#1043FBesides, I...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #137
        0x101,
        "#1026F#3P(Joshua...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        (
            "#1043F#6PSay, Hans...?\x02\x03",

            "I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#733F#4PHm? What is it?\x02\x03",

            "#731FI see! I knew it. You can't forget those\x01",
            "profound, passionate nights spent gazing\x01",
            "longingly at one another, can you?\x02\x03",

            "#732FI guess it's time for me to face the facts\x01",
            "and accept your confession of love.\x01",
            "Which is no trouble at all, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#1052F#6PPlease, Hans...\x02\x03",

            "#1048FI'm trying to be serious here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x9,
        (
            "#736F#4PIf you want to talk about the past,\x01",
            "I'll be glad to hear you out any time.\x02\x03",

            "#732FOf course, I doubt anything you'd\x01",
            "say would change things between us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#1044F#6PMeaning...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#731F#4PBasically, we're friends.\x02\x03",

            "#730FYou've come back and you're here,\x01",
            "standing in front of me.\x02\x03",

            "That's what matters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1044F#6PAh...\x02\x03",

            "#1053FYeah... You're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "#649F#4P(Man, oh, man... Men are so clumsy.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(300)

    ChrTalk(    #146
        0x101,
        "#1008F#6P(Haha... Still, it's kinda nice.)\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_A2(0x9)
    OP_A2(0x20C0)
    EventEnd(0x0)
    Return()

    # Function_17_2A4B end

    def Function_18_3409(): pass

    label("Function_18_3409")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3430():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3430)
    OP_8E(0xFE, 0x6EAA, 0x0, 0xD5D4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_3409 end

    def Function_19_3458(): pass

    label("Function_19_3458")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3484():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3484)
    OP_8E(0xFE, 0x6EDC, 0x0, 0xD962, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_19_3458 end

    def Function_20_34AC(): pass

    label("Function_20_34AC")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_34D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34D8)
    OP_8E(0xFE, 0x6A9A, 0x0, 0xD84A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_20_34AC end

    def Function_21_3500(): pass

    label("Function_21_3500")

    Sleep(1800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25410, 0, 55980, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_352C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_352C)
    OP_8E(0xFE, 0x6AAE, 0x0, 0xDB88, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_3500 end

    def Function_22_3554(): pass

    label("Function_22_3554")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3643")

    ChrTalk(    #147
        0x8,
        (
            "#644FThings aren't exactly easy at the\x01",
            "school right now, but we'll pull through.\x02\x03",

            "#659FHeh heh heh... I can't wait for the\x01",
            "costume party. You're not getting out\x01",
            "of this one, Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        "#1048F(Wait, was she serious?)\x02",
    )

    CloseMessageWindow()
    OP_A3(0x9)
    Jump("loc_36D3")

    label("loc_3643")


    ChrTalk(    #149
        0x8,
        (
            "#644FThings aren't exactly easy at the\x01",
            "school right now, but we'll pull through.\x02\x03",

            "#659FHeh heh heh... I can't wait for the\x01",
            "costume party. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D3")

    TalkEnd(0x8)
    Return()

    # Function_22_3554 end

    def Function_23_36D7(): pass

    label("Function_23_36D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_37EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378F")

    ChrTalk(    #150
        0xFE,
        (
            "It's a new term, but crazy things\x01",
            "keep happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "*sigh* I wonder when things'll\x01",
            "be back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "I hope the Music Club starts back\x01",
            "up soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_37EF")

    label("loc_378F")


    ChrTalk(    #153
        0xFE,
        (
            "I wonder when things'll be back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I hope the Music Club starts back\x01",
            "up soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EF")

    TalkEnd(0xFE)
    Return()

    # Function_23_36D7 end

    def Function_24_37F3(): pass

    label("Function_24_37F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3804")
    Call(0, 57)

    label("loc_3804")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 30850, 0, 56600, 315)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x105, 30850, 0, 55280, 315)
    SetChrPos(0x104, 28700, 0, 55860, 45)
    SetChrPos(0x127, 28700, 0, 54720, 45)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 45)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_39D4")

    ChrTalk(    #155
        0x8,
        (
            "#647F#6POkay, let's divide up the jobs.\x02\x03",

            "#640FAgate and I will go question the teachers.\x01",
            "They should be in the faculty lounge right now.\x02\x03",

            "After that, we'll hunt down the rest of\x01",
            "the staff and interrogate them, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x106,
        "#051FEasy enough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AE3")

    label("loc_39D4")


    ChrTalk(    #157
        0x8,
        (
            "#647F#6POkay, let's divide up the jobs.\x02\x03",

            "#640FScherazard and I will go question the\x01",
            "teachers. They should be in the staff\x01",
            "room right now.\x02\x03",

            "After that, we'll hunt down the rest of\x01",
            "the staff and interrogate them, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#021FLeave it to us.\x01",
            "It shouldn't take long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE3")

    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #159
        0x8,
        (
            "#640F#6PHans will check the records in the reference\x01",
            "room and see if anything like this has\x01",
            "happened around here before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        "#730F#5PUnderstood!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #161
        0x8,
        (
            "#648F#6PEstelle and Kloe will be in charge\x01",
            "of interviewing students.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1006F#4POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x105,
        "#040F#2PWe'll do our best.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #164
        0x8,
        (
            "#641F#6PDorothy, Olivier, you two...er, investigate\x01",
            "the grounds as you see fit!\x02\x03",

            "I'll trust your...um, your artist's\x01",
            "intuition to find something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        "#035F#5PHeh, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x127,
        "#151FI'll do my beeeest! ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #167
        0x8,
        (
            "#644F#6POkay, so, everyone? Try and finish up your\x01",
            "investigations by nightfall and return here.\x02\x03",

            "All right! Faaaaall OUT!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D73():

        label("loc_3D73")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_3D73")

    QueueWorkItem2(0x101, 2, lambda_3D73)

    def lambda_3D84():

        label("loc_3D84")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_3D84")

    QueueWorkItem2(0x105, 1, lambda_3D84)
    OP_43(0x104, 0x1, 0x0, 0x19)
    Sleep(500)
    OP_43(0x127, 0x1, 0x0, 0x19)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x19)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x8, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x1)

    def lambda_3DD9():
        OP_6D(31890, 0, 57570, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DD9)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #168
        0x101,
        (
            "#1006F#6PShe really is good at this, huh?\x01",
            "I noticed it during the school festival, too.\x02\x03",

            "She CAN be pretty silly at times, but I guess\x01",
            "she leads the Student Council for a reason.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #169
        0x105,
        (
            "#041F#2PHeehee. Well, she does want to become a\x01",
            "politician, kind of like Maybelle of Bose.\x02\x03",

            "#040FShe was really frustrated when the election\x01",
            "began. She kept going on about how she could've\x01",
            "been a candidate if she were ten years older.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #170
        0x101,
        (
            "#1016F#6PUh, well, I...guess she could, yeah!\x02\x03",

            "#1004FOh, yeah, I was wondering. How much do\x01",
            "Jill and Hans know about you, Kloe? I know\x01",
            "you mentioned once they nicknamed you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#041F#2PHeehee... Yes, they did.\x01",
            "They essentially know everything.\x02\x03",

            "They saw through my disguise about\x01",
            "halfway into my first year here.\x02\x03",

            "#040FAside from them, only the dean\x01",
            "knows my 'true' identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1011F#6PThat makes sense, I guess.\x02\x03",

            "They do seem pretty comfortable hanging\x01",
            "out with you, even though they know about\x01",
            "your important royal stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x105,
        (
            "#048F#2PYes...just like you, Estelle.\x02\x03",

            "You are the best friends I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1016F#6PAh-haha! C'mon, you're embarrassing me,\x01",
            "here.\x02\x03",

            "#1006FAnyhow, let's go find some students to\x01",
            "interrogate.\x02\x03",

            "'Did you see anything weird during\x01",
            "the test period' should be good enough\x01",
            "without raising suspicion, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x105,
        (
            "#040F#2PYes, that should keep rumors\x01",
            "from spreading, I think.\x02\x03",

            "Remember, though, some of\x01",
            "the students may be back in their\x01",
            "dormitories already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1006F#6PGood point, we'll look there too.\x02\x03",

            "Off we go a-questioning, then!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x26, 0xFF)
    OP_A2(0x121E)
    OP_28(0x83, 0x1, 0x2)
    OP_28(0x83, 0x1, 0x4)
    OP_28(0x66, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_24_37F3 end

    def Function_25_4402(): pass

    label("Function_25_4402")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_4428():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4428)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_4402 end

    def Function_26_4453(): pass

    label("Function_26_4453")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x6F0E, 0x0, 0xD2BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6BC6, 0x0, 0xD9C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_44A1():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44A1)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_4453 end

    def Function_27_44CC(): pass

    label("Function_27_44CC")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x70E4, 0x0, 0xE452, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6BC6, 0x0, 0xD9C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x67C0, 0x0, 0xDAAC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_451A():
        OP_8E(0xFE, 0x605E, 0x0, 0xDA5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_451A)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_44CC end

    def Function_28_4545(): pass

    label("Function_28_4545")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, -29850, 0, 58500, 99)
    SetChrPos(0x105, -30230, 0, 57060, 31)
    OP_8C(0x9, 270, 0)
    SetChrSubChip(0x9, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #177
        0x9,
        "#730FHey, you two. How goes the questioning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1016F#6PWelllll, we've just started,\x01",
            "so we don't have much yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        "#040F#2PHave you had any luck with the records?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "#730FNot yet, but there aren't many\x01",
            "records that could be relevant,\x01",
            "so this shouldn't take long.\x02\x03",

            "#736F...Hey. I know you're busy, but could\x01",
            "I take a minute of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1004F#6PUh, sure.\x02\x03",

            "#1002F...Let me guess.\x01",
            "This is about Joshua, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#735FYeah.\x02\x03",

            "#732FI haven't heard all the details,\x01",
            "but he's gone missing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1025F#6PHe, uh, has...but don't worry.\x02\x03",

            "It's something he did on his own, so it's\x01",
            "basically like him running away from home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        (
            "#736FHm... I wonder.\x02\x03",

            "#730FI know I only spent a week\x01",
            "or so with him, but...\x02\x03",

            "Well, we really got along. Got to know each\x01",
            "other. We talked about a whole lot of things.\x02\x03",

            "He just could not shut up about his life\x01",
            "after he came to live with you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#1008F#6PEr, r-really?\x02\x03",

            "Th-That's so embarrassing...\x01",
            "I was such a tomboy...\x02\x03",

            "#1016FEr, I mean, I guess that's still true, but!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        (
            "#731FHaha! Well, I heard a lot of heartwarming\x01",
            "stories, I'll say that much!\x02\x03",

            "#730FThe thing is...I never heard a word\x01",
            "about anything before then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1026F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#736FOne time, I just kind of casually\x01",
            "asked about what his life was like\x01",
            "before he came to live with you...\x02\x03",

            "I'll never forget his expression when\x01",
            "I asked that. I'll never be ABLE to.\x02\x03",

            "#735FHis eyes just sort of clouded over. It was\x01",
            "like he was staring over a selge-long field of...\x01",
            "who knows what...that only he could see.\x02\x03",

            "#730FAfterwards, though, he just laughed it off and\x01",
            "pretended it never happened...while avoiding\x01",
            "the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#732FI don't really know his history...\x02\x03",

            "...but his leaving has something\x01",
            "to do with his early life, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1026F#6PYeah.\x02\x03",

            "We're pretty sure it does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x9,
        (
            "#735FI knew it.\x02\x03",

            "#730FWhenever we went to bed,\x01",
            "we'd always talk about how the\x01",
            "day went, right?\x02\x03",

            "How practice was going, for\x01",
            "example, or how delicious lunch\x01",
            "was. That sort of thing.\x02\x03",

            "#736FWhenever we did that, he got\x01",
            "this look...like he was looking at\x01",
            "something bright and beautiful.\x02\x03",

            "It was the expression of someone\x01",
            "looking at something they want but\x01",
            "can't have.\x02\x03",

            "And at the same time, he just sort\x01",
            "of seemed to...accept that it was\x01",
            "something he could never have.\x02\x03",

            "He never really lost that look\x01",
            "the entire time he was here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#1026F#6PJoshua...\x02\x03",

            "#1027FIt IS something you can have,\x01",
            "you giant idiot...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #194
        0x105,
        "#043F#2PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        (
            "#730FSo, yeah.\x02\x03",

            "I know I shouldn't really get\x01",
            "involved since I don't know you\x01",
            "two THAT well, but...\x02\x03",

            "Can I ask one favor of you?\x01",
            "Just one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "#732FIf you meet him again, don't\x01",
            "ever let him have that kind of\x01",
            "expression.\x02\x03",

            "He IS an idiot, thinking he can't\x01",
            "have that kind of life.\x02\x03",

            "He's got just as much of a right\x01",
            "to love, laugh, and enjoy life as\x01",
            "any of us do.\x02\x03",

            "Can you do that for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1025F#6PHans...\x02\x03",

            "#1012FYeah... Of course I can.\x02\x03",

            "#1018FI'll wake him up to that fact even\x01",
            "if I have to slap his cheeks beet\x01",
            "red in the process!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x105,
        (
            "#041F#2PHaha! Estelle...\x02\x03",

            "#048FIt may take that to really get him\x01",
            "to understand...but we'll do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "#734FOh, crud. Uh, sorry in advance, J.\x02\x03",

            "#730FMmm...\x01",
            "Felt good to get that off my chest.\x02\x03",

            "Sorry, I shouldn't take up too\x01",
            "much of your time.\x02\x03",

            "Good luck with your investigation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#1017F#6PYeah... Thanks, Hans.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x9, 400)

    ChrTalk(    #202
        0x105,
        "#041F#2PGood luck to you too, Hans!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    OP_A2(0x121F)
    EventEnd(0x0)
    Return()

    # Function_28_4545 end

    def Function_29_533D(): pass

    label("Function_29_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_534E")
    Call(0, 57)

    label("loc_534E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_536D")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5371")

    label("loc_536D")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5371")

    AddParty(0x3, 0xF8, 0xFF)
    AddParty(0x26, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    SetChrPos(0x101, 24710, 0, 55840, 90)
    SetChrPos(0x105, 24710, 0, 55840, 90)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)

    def lambda_5475():
        OP_6D(29490, 0, 57970, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5475)

    def lambda_548D():
        OP_8F(0x101, 0x69B4, 0x0, 0xD854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_548D)

    def lambda_54A8():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54A8)
    Sleep(200)

    def lambda_54BF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54BF)

    def lambda_54CD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_54CD)

    def lambda_54DB():

        label("loc_54DB")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_54DB")

    QueueWorkItem2(0x9, 1, lambda_54DB)

    def lambda_54EC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54EC)

    def lambda_54FA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_54FA)
    Sleep(300)

    def lambda_550D():
        OP_8F(0x105, 0x67E8, 0x0, 0xDBBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_550D)

    def lambda_5528():
        OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5528)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x105, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #203
        0x8,
        (
            "#644F#6PHeeey, you're back!\x02\x03",

            "#648FAll right, everyone, reports!\x01",
            "Hit me! In the face!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 30850, 0, 56600, 270)
    SetChrPos(0x105, 30850, 0, 55280, 270)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    OP_6D(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5784")

    ChrTalk(    #204
        0x106,
        (
            "#053F#2PWe talked to the entire staff,\x01",
            "but practically all of them came\x01",
            "up blank...\x02\x03",

            "#050FOnly one who saw anything\x01",
            "remotely weird was the janitor.\x02\x03",

            "He saw a suspicious person who\x01",
            "seemed to disappear right at the\x01",
            "gate to the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5861")

    label("loc_5784")


    ChrTalk(    #205
        0x103,
        (
            "#026F#2PWell, most of our interviews\x01",
            "with the staff were fruitless...\x02\x03",

            "#022FOnly the school janitor saw\x01",
            "someone suspicious.\x02\x03",

            "The suspect seemed to disappear\x01",
            "right outside the gate to the old\x01",
            "schoolhouse, apparently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5861")


    ChrTalk(    #206
        0x8,
        (
            "#644F#6PYeah, the teaching staff were all\x01",
            "too busy preparing for the tests,\x01",
            "so nobody saw anything useful.\x02\x03",

            "The cafeteria lady and Fauna,\x01",
            "the receptionist, also didn't\x01",
            "have much to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#6PI was kind of afraid of that...\x02\x03",

            "#1011FWell, for our part, we heard some\x01",
            "interesting stories from three students\x01",
            "in particular.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #208
        (
            "\x07\x05Estelle reported Patrick, Mickey,\x01",
            "and Felicity's stories to the group.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #209
        0x105,
        (
            "#043F#2PAll of them centered around the\x01",
            "rear of the school grounds, near\x01",
            "the old schoolhouse.\x02\x03",

            "That strikes me as too similar\x01",
            "to be mere coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x127,
        (
            "#150FI got some results toooo!\x02\x03",

            "#151FI took thirty pictures of the\x01",
            "students and teachers, and\x01",
            "fifty of the school's scenery!\x02\x03",

            "Heehee! They're all reeeeally\x01",
            "cute! I love this place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x104,
        (
            "#030F#5PSadly, my efforts failed to shine.\x02\x03",

            "#031FI did, however, cause several\x01",
            "beautiful kittens to flock to the\x01",
            "siren call of my lute.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x101,
        (
            "#1019F#6PSo you two accomplished LITERALLY\x01",
            "nothing. Like, at all.\x02\x03",

            "#1007FI mean, I wasn't expecting much,\x01",
            "but come on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x9,
        (
            "#735FSo that'd leave me for last, I suppose.\x02\x03",

            "#730FI looked over the records for\x01",
            "any similar cases.\x02\x03",

            "Problem is, everything here is so new,\x01",
            "there's nothing really in the way of\x01",
            "'ghost stories' and whatnot.\x02\x03",

            "Anything remotely relevant centers\x01",
            "around the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x127, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0x105)
    OP_63(0x104)
    OP_63(0x127)
    OP_63(0x8)
    OP_63(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5EE2")

    ChrTalk(    #214
        0x106,
        (
            "#552F#2PIn that case, that old ruin is suspicious\x01",
            "no matter how you slice it.\x02\x03",

            "What's the deal with that shack, anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F82")

    label("loc_5EE2")


    ChrTalk(    #215
        0x103,
        (
            "#025F#2PThe old schoolhouse again...\x01",
            "It's suspicious no matter how\x01",
            "you look at the case.\x02\x03",

            "#020FI'm a little unclear. What IS\x01",
            "the history of that building?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F82")


    ChrTalk(    #216
        0x8,
        (
            "#644F#6PIt's the original Jenis building. It's been\x01",
            "around for centuries, as far as I know.\x02\x03",

            "The new campus was finished about...twenty\x01",
            "years ago? The school moved here and the old\x01",
            "place has been closed off ever since.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x101,
        (
            "#1015F#6PWait, hang on. It's 'closed off,'\x01",
            "but I thought we popped in there\x01",
            "during the school festival.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 400)

    ChrTalk(    #218
        0x105,
        (
            "#542F#2PUnfortunately, some of the very\x01",
            "dangerous monsters that have been\x01",
            "wandering around got in after you left.\x02\x03",

            "We've had to leave it tightly locked\x01",
            "and abandoned ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x104,
        (
            "#035F#5POh, my... A stone ruin dating\x01",
            "back centuries...\x02\x03",

            "#030FIt strikes me as the perfect\x01",
            "haunt for a ghost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1007F#6PThanks a heap for pointing THAT out.\x02\x03",

            "Well, I really don't want to go, but\x01",
            "it's not like we have any other leads.\x02\x03",

            "#1008FIt's getting pretty late, though, so how\x01",
            "about we check it out tomorrow? Yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x104,
        (
            "#033F#5PWhy, Estelle, whatever makes now a\x01",
            "bad time? It doesn't seem that late.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x101,
        (
            "#1016F#6PEr, well, you see, it's almost nightfall.\x01",
            "And it might be...dangerous!\x01",
            "With the monsters. And stuff.\x02\x03",

            "It'll be a bit of a challenge during\x01",
            "the day, so I imagine it'd be stupidly\x01",
            "dangerous at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x104,
        (
            "#030F#5PAh, but is that not the point?\x02\x03",

            "#031FThe truly terrifying manifests best\x01",
            "under the light of the moon!\x02\x03",

            "If there is any time to grasp the true\x01",
            "nature of our specter, it is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x127,
        (
            "#151FYeah, yeah!\x02\x03",

            "You gotta get ghost pictures at night!\x01",
            "It's the law! Or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1019F#6PThe law in loony land, maybe...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #226
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x105,
        "#044F#2PEstelle? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1015F#6PUh, I dunno. Thought I saw something\x01",
            "outside the window.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6620():

        label("loc_6620")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6620")

    QueueWorkItem2(0xF7, 1, lambda_6620)

    def lambda_6631():

        label("loc_6631")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6631")

    QueueWorkItem2(0x105, 1, lambda_6631)

    def lambda_6642():

        label("loc_6642")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6642")

    QueueWorkItem2(0x104, 1, lambda_6642)

    def lambda_6653():

        label("loc_6653")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6653")

    QueueWorkItem2(0x127, 1, lambda_6653)

    def lambda_6664():

        label("loc_6664")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6664")

    QueueWorkItem2(0x8, 1, lambda_6664)

    def lambda_6675():

        label("loc_6675")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_6675")

    QueueWorkItem2(0x9, 1, lambda_6675)

    def lambda_6686():
        OP_6D(30490, 0, 59490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6686)

    def lambda_669E():
        OP_67(0, 6150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_669E)
    OP_8E(0x101, 0x794A, 0x0, 0xE4C0, 0x7D0, 0x0)
    OP_20(0xBB8)
    OP_8E(0x101, 0x771A, 0x0, 0xE862, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #229
        0x101,
        (
            "#1015FIt was sort of a white-ish shadow.\x01",
            "Probably just Sieg.\x02\x03",

            "#1019FH-Hold on.\x01",
            "A...white...shadow...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_533D end

    def Function_30_678A(): pass

    label("Function_30_678A")

    OP_8E(0x101, 0x6EB4, 0x0, 0xE38A, 0x7D0, 0x0)
    OP_8E(0x101, 0x7990, 0x0, 0xE54C, 0x7D0, 0x0)
    OP_8E(0x101, 0x7882, 0x0, 0xDEA8, 0x7D0, 0x0)
    OP_8C(0x101, 284, 400)
    Return()

    # Function_30_678A end

    def Function_31_67CE(): pass

    label("Function_31_67CE")

    OP_8E(0x105, 0x6F0E, 0x0, 0xE510, 0x7D0, 0x0)
    OP_8E(0x105, 0x7468, 0x0, 0xE358, 0x7D0, 0x0)
    TurnDirection(0x105, 0x9, 400)
    Return()

    # Function_31_67CE end

    def Function_32_67FE(): pass

    label("Function_32_67FE")

    SetChrPos(0x101, 30490, 0, 59490, 0)
    SetChrPos(0x105, 30850, 0, 55280, 270)
    SetChrPos(0xF7, 29800, 0, 53800, 0)
    SetChrPos(0x104, 28700, 0, 55860, 90)
    SetChrPos(0x127, 28700, 0, 54720, 90)
    SetChrPos(0x8, 29800, 0, 58200, 180)
    SetChrPos(0x9, 28700, 0, 57000, 90)
    TurnDirection(0xF7, 0x101, 0)
    TurnDirection(0x105, 0x101, 0)
    TurnDirection(0x104, 0x101, 0)
    TurnDirection(0x127, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0x9, 0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    OP_6D(30490, 0, 59490, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    FadeToBright(2000, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()

    ChrTalk(    #230
        0x105,
        "#043F#2PEstelle? What's...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #231
        0x101,
        (
            "#1008F#6PAh...ha...ha ha ha ha...\x02\x03",

            "#1007FHaaaaaauuuuugh...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 1)
    OP_0D()
    Sleep(500)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x127, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6A46")

    ChrTalk(    #232
        0x106,
        "#055F#2PH-Hey!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A5D")

    label("loc_6A46")


    ChrTalk(    #233
        0x103,
        "#023F#2PEstelle?!\x02",
    )

    CloseMessageWindow()

    label("loc_6A5D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2812   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_32_67FE end

    def Function_33_6A7A(): pass

    label("Function_33_6A7A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x17, 2350, 0, -610, 270)
    SetChrPos(0x18, 340, 0, -790, 90)
    SetChrPos(0x19, -80, 0, -4510, 180)
    SetChrPos(0x1A, -2400, 0, -3520, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    OP_D2(0x26000D, 0x260012, 0x11)
    OP_D2(0x26000E, 0x260013, 0x12)
    SetChrChipByIndex(0x17, 17)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 17)
    SetChrChipByIndex(0x1A, 18)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    OP_62(0x17, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x18, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    OP_43(0x19, 0x1, 0x0, 0x22)
    OP_43(0x1A, 0x1, 0x0, 0x23)
    SetChrFlags(0xB, 0x80)
    OP_6D(150, 2000, 4650, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(-110, 0, -3080, 4000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2500   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_33_6A7A end

    def Function_34_6BD2(): pass

    label("Function_34_6BD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C0E")
    OP_8C(0xFE, 135, 400)
    Sleep(700)
    OP_8C(0xFE, 180, 400)
    Sleep(700)
    OP_8C(0xFE, 225, 400)
    Sleep(700)
    OP_8C(0xFE, 180, 400)
    Sleep(700)
    Jump("Function_34_6BD2")

    label("loc_6C0E")

    Return()

    # Function_34_6BD2 end

    def Function_35_6C0F(): pass

    label("Function_35_6C0F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C79")
    OP_8E(0xFE, 0xFFFFE872, 0x0, 0xFFFFF524, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE8A4, 0x0, 0xFFFFFFEC, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFE872, 0x0, 0xFFFFF524, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF240, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("Function_35_6C0F")

    label("loc_6C79")

    Return()

    # Function_35_6C0F end

    def Function_36_6C7A(): pass

    label("Function_36_6C7A")

    Call(0, 37)
    Call(0, 38)
    Return()

    # Function_36_6C7A end

    def Function_37_6C83(): pass

    label("Function_37_6C83")

    EventBegin(0x0)
    OP_D2(0x26000D, 0x260012, 0x11)
    OP_D2(0x26020B, 0x260210, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270111, 0x270121, 0x14)
    OP_D2(0x270130, 0x270140, 0x15)
    OP_D2(0x270131, 0x270141, 0x16)
    OP_D2(0x70326, 0x7032D, 0x17)
    OP_D2(0x70327, 0x7032E, 0x18)
    OP_D2(0x70318, 0x7031F, 0x19)
    OP_D2(0x70319, 0x70320, 0x1A)
    OP_D2(0x26000E, 0x260013, 0x1B)
    OP_D2(0x270327, 0x270331, 0x1C)
    OP_D2(0x270313, 0x27031D, 0x1D)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x17, -1990, 0, 42080, 0)
    SetChrPos(0x18, 1610, 0, 41880, 0)
    SetChrChipByIndex(0x17, 17)
    SetChrChipByIndex(0x18, 27)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(550, 0, 52120, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(368, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x27)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0x10A, 0x1, 0x0, 0x29)

    def lambda_6DC7():
        OP_6D(1460, 0, 48750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DC7)

    def lambda_6DDF():
        OP_67(0, 4940, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6DDF)

    def lambda_6DF7():
        OP_6E(322, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6DF7)

    def lambda_6E07():
        OP_6B(3060, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6E07)
    Sleep(500)
    OP_43(0x10E, 0x1, 0x0, 0x2A)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #234
        0x17,
        "#5PGyah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x18,
        "#2PYou sons of...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #236
        0x101,
        "#1005F#6PThere they are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x10A,
        "#815F#6PHere we gooooo!\x02",
    )

    CloseMessageWindow()

    def lambda_6E8E():
        OP_6D(1410, 0, 48310, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E8E)

    def lambda_6EA6():
        OP_6B(2400, 600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6EA6)
    OP_43(0x101, 0x1, 0x0, 0x2B)
    Sleep(30)
    OP_43(0x10A, 0x1, 0x0, 0x2D)
    Sleep(50)
    OP_43(0x10E, 0x1, 0x0, 0x2E)
    Sleep(30)
    OP_43(0x102, 0x1, 0x0, 0x2C)
    Sleep(100)
    SetChrChipByIndex(0x17, 28)
    SetChrFlags(0x17, 0x1000)

    def lambda_6EF0():
        OP_8F(0xFE, 0xFFFFF934, 0x0, 0xAF1E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6EF0)
    Sleep(30)
    SetChrChipByIndex(0x18, 29)
    SetChrFlags(0x18, 0x1000)

    def lambda_6F1A():
        OP_8F(0xFE, 0x74E, 0x0, 0xB09A, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6F1A)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    Battle(0x7A1, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_6F65"),
        (SWITCH_DEFAULT, "loc_6F6A"),
    )


    label("loc_6F65")

    OP_B4(0x0)
    Jump("loc_6F6A")

    label("loc_6F6A")

    Return()

    # Function_37_6C83 end

    def Function_38_6F6B(): pass

    label("Function_38_6F6B")

    EventBegin(0x0)
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    OP_D2(0x26020B, 0x260210, 0x12)
    OP_6D(-150, 0, 42940, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 18)
    SetChrSubChip(0x17, 8)
    ClearChrFlags(0x18, 0x1)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 18)
    SetChrSubChip(0x18, 11)
    SetChrPos(0x0, -150, 0, 42940, 180)
    SetChrPos(0x1, -150, 0, 42940, 180)
    SetChrPos(0x2, -150, 0, 42940, 180)
    SetChrPos(0x3, -150, 0, 42940, 180)
    OP_69(0x0, 0x0)
    SetChrPos(0x17, 1340, 0, 39800, 0)
    SetChrPos(0x18, -2270, 0, 40010, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_A2(0x2021)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_38_6F6B end

    def Function_39_7098(): pass

    label("Function_39_7098")

    SetChrChipByIndex(0x101, 19)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF948, 0x0, 0xCA3A, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_39_7098 end

    def Function_40_70E8(): pass

    label("Function_40_70E8")

    SetChrChipByIndex(0x102, 21)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xCF62, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_40_70E8 end

    def Function_41_7138(): pass

    label("Function_41_7138")

    SetChrChipByIndex(0x10A, 23)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0x6C2, 0x0, 0xCD1E, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_41_7138 end

    def Function_42_7188(): pass

    label("Function_42_7188")

    SetChrChipByIndex(0x10E, 25)
    SetChrPos(0xFE, 0, -2000, 48020, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0xCD78, 0x1388, 0x0)
    OP_8E(0xFE, 0x35C, 0x0, 0xCFD0, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_42_7188 end

    def Function_43_71D8(): pass

    label("Function_43_71D8")

    OP_8E(0xFE, 0xFFFFF970, 0x0, 0xAE10, 0x1F40, 0x0)
    Return()

    # Function_43_71D8 end

    def Function_44_71ED(): pass

    label("Function_44_71ED")

    OP_8E(0xFE, 0xFFFFF844, 0x0, 0xB266, 0x1F40, 0x0)
    Return()

    # Function_44_71ED end

    def Function_45_7202(): pass

    label("Function_45_7202")

    OP_8E(0xFE, 0x64A, 0x0, 0xACF8, 0x1F40, 0x0)
    Return()

    # Function_45_7202 end

    def Function_46_7217(): pass

    label("Function_46_7217")

    OP_8E(0xFE, 0x794, 0x0, 0xCD28, 0x1F40, 0x0)
    OP_8E(0xFE, 0x5BE, 0x0, 0xB25C, 0x1F40, 0x0)
    Return()

    # Function_46_7217 end

    def Function_47_7240(): pass

    label("Function_47_7240")

    EventBegin(0x0)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_8C(0x12, 180, 0)
    OP_8C(0x13, 0, 0)
    OP_6D(-27920, 0, 27650, 0)
    OP_67(0, 5370, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x2, 0x10)
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    Sleep(300)

    def lambda_72D2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_72D2)
    Sleep(100)

    def lambda_72E5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_72E5)

    def lambda_72F3():
        OP_6D(-28660, 0, 27330, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_72F3)
    OP_43(0x102, 0x1, 0x0, 0x31)
    Sleep(250)
    OP_43(0x101, 0x1, 0x0, 0x30)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x32)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x33)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #238
        0x12,
        "#6PWho're...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x13,
        "#5PEstelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1016F#4PAhaha, that's us! Hiya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        "#1035F#4PYou're all safe, thank goodness.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #242
        "\x07\x05Estelle explained the plan to free the captives.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #243
        0x13,
        "#5PNow I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x12,
        "#6PThank you for your assistance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x12,
        (
            "#6PIs there anything we can do to\x01",
            "help you rescue the students?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10E,
        (
            "#842F#4PWe appreciate the thought, but the enemy\x01",
            "is a professional mercenary company.\x02\x03",

            "#843FThe best thing to do is remain here\x01",
            "until we are certain it is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x12,
        "#6PI see... You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x13,
        "#5PPlease, take care of the students!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x10A,
        "#816F#4PLeave it to us!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #250
        (
            "\x07\x05Estelle checked the names of Mr. Ratio and\x01",
            "Mr. Effort off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_71(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_6D(-29240, 0, 25720, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -29240, 0, 25720, 270)
    SetChrPos(0x1, -29240, 0, 25720, 270)
    SetChrPos(0x2, -29240, 0, 25720, 270)
    SetChrPos(0x3, -29240, 0, 25720, 270)
    OP_4B(0x12, 255)
    OP_4B(0x13, 255)
    OP_0D()
    OP_A2(0x2022)
    OP_28(0xC0, 0x1, 0x40)
    OP_28(0xC1, 0x2, 0x4)
    OP_28(0xC1, 0x1, 0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_47_7240 end

    def Function_48_76F7(): pass

    label("Function_48_76F7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_771E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_771E)
    OP_8E(0xFE, 0xFFFF8C9C, 0x0, 0x654A, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_48_76F7 end

    def Function_49_7746(): pass

    label("Function_49_7746")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_776D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_776D)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8D6E, 0x0, 0x6AD6, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_49_7746 end

    def Function_50_77A9(): pass

    label("Function_50_77A9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_77D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_77D0)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF8FEE, 0x0, 0x6310, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_50_77A9 end

    def Function_51_780C(): pass

    label("Function_51_780C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -26460, 0, 25950, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7833():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7833)
    OP_8E(0xFE, 0xFFFF91EC, 0x0, 0x650E, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFF9214, 0x0, 0x67B6, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_51_780C end

    def Function_52_786F(): pass

    label("Function_52_786F")

    EventBegin(0x0)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0xB, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(30820, 0, 27050, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_78F2():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_78F2)
    Sleep(100)

    def lambda_7905():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7905)
    Sleep(100)

    def lambda_7918():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7918)

    def lambda_7926():
        OP_6D(30250, 0, 27820, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7926)
    OP_43(0x101, 0x1, 0x0, 0x35)
    Sleep(250)
    OP_43(0x102, 0x1, 0x0, 0x36)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x37)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x38)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #251
        0xB,
        "#2PIt can't be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x14,
        (
            "Estelle and Joshua...\x01",
            "What on earth are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        "#1016F#5PAhaha... Sorry to surprise you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        "#1042F#6PActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #255
        "\x07\x05Joshua explained the plan to free the captives.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #256
        0x14,
        (
            "I see, so you're...\x02\x03",

            "Thank you so much for\x01",
            "coming to free us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x15,
        (
            "So how are things outside?\x02\x03",

            "Is there still fighting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x10E,
        (
            "#843F#5PThere's fighting at the gate and\x01",
            "jaegers still roam the grounds.\x01",
            "The situation is dangerous.\x02\x03",

            "#842FI must ask that you remain here\x01",
            "for your own safety until we've\x01",
            "secured the school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x15,
        "I see... If we must.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x14,
        (
            "Please, I beg you...make sure\x01",
            "the students stay safe for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xB,
        (
            "#2POh, I know!\x01",
            "Please, take these.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0xB, 0x7300, 0x0, 0x65F4, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #262
        "\x07\x00Received #452i x4.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x1C4, 4)
    OP_8F(0xB, 0x772E, 0x0, 0x645A, 0x7D0, 0x0)

    ChrTalk(    #263
        0x101,
        "#1011F#5PMs. Deborah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x10A,
        "#811F#1PWhoa, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xB,
        (
            "#2PIt's thanks for rescuing us!\x02\x03",

            "Now, being a hero is nice,\x01",
            "but take care, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        "#1054F#6PThank you. We'll be safe.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #267
        (
            "\x07\x05Estelle checked the names of Deborah, Ms. Wiola,\x01",
            "and Ms. Millia off the list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(500)
    OP_6D(28370, 0, 26480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 28370, 0, 26480, 90)
    SetChrPos(0x1, 28370, 0, 26480, 90)
    SetChrPos(0x2, 28370, 0, 26480, 90)
    SetChrPos(0x3, 28370, 0, 26480, 90)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x2023)
    OP_28(0xC0, 0x1, 0x80)
    OP_28(0xC1, 0x2, 0x10)
    OP_28(0xC1, 0x1, 0x20)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_52_786F end

    def Function_53_7EC4(): pass

    label("Function_53_7EC4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7EEB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7EEB)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x7030, 0x0, 0x6644, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_53_7EC4 end

    def Function_54_7F27(): pass

    label("Function_54_7F27")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7F4E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7F4E)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x703A, 0x0, 0x6ACC, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_54_7F27 end

    def Function_55_7F8A(): pass

    label("Function_55_7F8A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7FB1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7FB1)
    OP_8E(0xFE, 0x698C, 0x0, 0x65D6, 0xFA0, 0x0)
    OP_8E(0xFE, 0x6BA8, 0x0, 0x6B4E, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_55_7F8A end

    def Function_56_7FED(): pass

    label("Function_56_7FED")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 25350, 0, 25850, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8014():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8014)
    OP_8E(0xFE, 0x6A7C, 0x0, 0x64A0, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_56_7FED end

    def Function_57_803C(): pass

    label("Function_57_803C")

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
        (0, "loc_80B5"),
        (1, "loc_80BB"),
        (SWITCH_DEFAULT, "loc_80C1"),
    )


    label("loc_80B5")

    OP_A2(0x1200)
    Jump("loc_80C1")

    label("loc_80BB")

    OP_A2(0x1201)
    Jump("loc_80C1")

    label("loc_80C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_80CF")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_80D3")

    label("loc_80CF")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_80D3")

    Return()

    # Function_57_803C end

    def Function_58_80D4(): pass

    label("Function_58_80D4")

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

    # Function_58_80D4 end

    def Function_59_812D(): pass

    label("Function_59_812D")

    SetPlaceName(0x71)
    Return()

    # Function_59_812D end

    def Function_60_8131(): pass

    label("Function_60_8131")

    SetPlaceName(0x72)
    Return()

    # Function_60_8131 end

    def Function_61_8135(): pass

    label("Function_61_8135")

    SetPlaceName(0x75)
    Return()

    # Function_61_8135 end

    def Function_62_8139(): pass

    label("Function_62_8139")

    SetPlaceName(0x70)
    Return()

    # Function_62_8139 end

    SaveToFile()

Try(main)
