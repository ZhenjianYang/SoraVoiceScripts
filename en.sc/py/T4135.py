from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4135_1 ._SN',
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
        'Licia',                                # 9
        'Museum Director',                      # 10
        'Santos',                               # 11
        'Jimmy',                                # 12
        'Capital Citizen',                      # 13
        'Capital Citizen',                      # 14
        'Capital Citizen',                      # 15
        'Capital Citizen',                      # 16
        'Capital Citizen',                      # 17
        'Renne',                                # 18
        'Tita',                                 # 19
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT27/CH03060 ._CH',             # 05
        'ED6_DT07/CH01230 ._CH',             # 06
        'ED6_DT07/CH01170 ._CH',             # 07
        'ED6_DT07/CH01000 ._CH',             # 08
        'ED6_DT07/CH01020 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT27/CH03060P._CP',             # 05
        'ED6_DT07/CH01230P._CP',             # 06
        'ED6_DT07/CH01170P._CP',             # 07
        'ED6_DT07/CH01000P._CP',             # 08
        'ED6_DT07/CH01020P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = -5910,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -69160,
        Z                   = 0,
        Y                   = 57560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -69000,
        Z                   = 0,
        Y                   = -1470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2380,
        Z                   = 0,
        Y                   = -5360,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 72040,
        Z                   = 0,
        Y                   = 2820,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 72050,
        Z                   = 0,
        Y                   = 1820,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 7500,
        Z                   = 4000,
        Y                   = -990,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -1050,
        Z                   = 0,
        Y                   = 66030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 3870,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -1050,
        Z                   = 0,
        Y                   = 66290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 2580,
        TriggerZ            = 0,
        TriggerY            = -5970,
        TriggerRange        = 800,
        ActorX              = 4400,
        ActorZ              = 1700,
        ActorY              = -5910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5090,
        TriggerZ            = 0,
        TriggerY            = 2190,
        TriggerRange        = 800,
        ActorX              = 5090,
        ActorZ              = 800,
        ActorY              = 2190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7840,
        TriggerZ            = 4000,
        TriggerY            = 6700,
        TriggerRange        = 800,
        ActorX              = 7840,
        ActorZ              = 5700,
        ActorY              = 6700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75860,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 75860,
        ActorZ              = 1500,
        ActorY              = -2000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73200,
        TriggerZ            = 0,
        TriggerY            = 710,
        TriggerRange        = 800,
        ActorX              = 73200,
        ActorZ              = 800,
        ActorY              = 710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68740,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 68740,
        ActorZ              = 800,
        ActorY              = 7310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73480,
        TriggerZ            = 0,
        TriggerY            = 6420,
        TriggerRange        = 800,
        ActorX              = 73480,
        ActorZ              = 800,
        ActorY              = 6420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75820,
        TriggerZ            = 4000,
        TriggerY            = 8010,
        TriggerRange        = 800,
        ActorX              = 75820,
        ActorZ              = 5700,
        ActorY              = 8010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71960,
        TriggerZ            = 4000,
        TriggerY            = 9290,
        TriggerRange        = 800,
        ActorX              = 71960,
        ActorZ              = 4800,
        ActorY              = 9290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 0,
        TriggerY            = 77880,
        TriggerRange        = 800,
        ActorX              = -20,
        ActorZ              = 1700,
        ActorY              = 77880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -770,
        TriggerZ            = 0,
        TriggerY            = 72650,
        TriggerRange        = 800,
        ActorX              = -770,
        ActorZ              = 800,
        ActorY              = 72650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 66550,
        TriggerRange        = 1200,
        ActorX              = 7000,
        ActorZ              = 800,
        ActorY              = 66550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1770,
        TriggerZ            = 0,
        TriggerY            = 66890,
        TriggerRange        = 800,
        ActorX              = 1770,
        ActorZ              = 800,
        ActorY              = 66890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3790,
        TriggerZ            = 0,
        TriggerY            = 64959,
        TriggerRange        = 800,
        ActorX              = -3790,
        ActorZ              = 800,
        ActorY              = 64959,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_45A",          # 00, 0
        "Function_1_629",          # 01, 1
        "Function_2_67D",          # 02, 2
        "Function_3_693",          # 03, 3
        "Function_4_698",          # 04, 4
        "Function_5_BF5",          # 05, 5
        "Function_6_1A8E",         # 06, 6
        "Function_7_25AC",         # 07, 7
        "Function_8_2F7D",         # 08, 8
        "Function_9_3118",         # 09, 9
        "Function_10_3241",        # 0A, 10
        "Function_11_32BE",        # 0B, 11
        "Function_12_32F4",        # 0C, 12
        "Function_13_331F",        # 0D, 13
        "Function_14_33BC",        # 0E, 14
        "Function_15_3440",        # 0F, 15
        "Function_16_383F",        # 10, 16
        "Function_17_3EE7",        # 11, 17
        "Function_18_3F2F",        # 12, 18
        "Function_19_3F77",        # 13, 19
        "Function_20_3FBF",        # 14, 20
        "Function_21_4007",        # 15, 21
        "Function_22_4409",        # 16, 22
        "Function_23_4478",        # 17, 23
        "Function_24_44E7",        # 18, 24
        "Function_25_4556",        # 19, 25
        "Function_26_45C5",        # 1A, 26
        "Function_27_4620",        # 1B, 27
        "Function_28_46BB",        # 1C, 28
        "Function_29_4734",        # 1D, 29
        "Function_30_48CF",        # 1E, 30
        "Function_31_4AF3",        # 1F, 31
        "Function_32_4D4E",        # 20, 32
        "Function_33_4E3D",        # 21, 33
        "Function_34_4F2A",        # 22, 34
        "Function_35_501A",        # 23, 35
        "Function_36_51A7",        # 24, 36
        "Function_37_539F",        # 25, 37
        "Function_38_55C4",        # 26, 38
        "Function_39_57F1",        # 27, 39
        "Function_40_59B2",        # 28, 40
        "Function_41_5AF1",        # 29, 41
    )


    def Function_0_45A(): pass

    label("Function_0_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_48E")
    SetChrPos(0xB, -950, 0, 74090, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_5B1")

    label("loc_48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4BA")
    SetChrPos(0x9, -69470, 0, 57290, 273)
    SetChrPos(0xB, -71620, 0, 57130, 86)
    Jump("loc_5B1")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4D5")
    SetChrPos(0xB, -950, 0, 74090, 90)
    Jump("loc_5B1")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_520")
    SetChrPos(0xB, 69710, 0, 7140, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    SetChrPos(0x9, 7000, 4000, -3740, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    SetChrFlags(0x9, 0x10)

    label("loc_51D")

    Jump("loc_5B1")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_594")
    SetChrPos(0xB, 4170, 0, 2620, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_565")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2990, 0, 67900, 165)
    OP_43(0x11, 0x0, 0x0, 0x2)

    label("loc_565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_591")
    SetChrPos(0x9, 7000, 4000, -3740, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_591")
    SetChrFlags(0x9, 0x10)

    label("loc_591")

    Jump("loc_5B1")

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5B1")
    SetChrPos(0x9, -930, 0, 71060, 90)
    SetChrFlags(0xB, 0x80)

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_5C7")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_628")

    label("loc_5C7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5DB"),
        (103, "loc_610"),
        (104, "loc_610"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F3")
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_60D")

    label("loc_5F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_60D")

    Jump("loc_628")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_625")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_625")

    Jump("loc_628")

    label("loc_628")

    Return()

    # Function_0_45A end

    def Function_1_629(): pass

    label("Function_1_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_645")
    OP_B1("t4135_y")
    Jump("loc_64E")

    label("loc_645")

    OP_B1("t4135_n")

    label("loc_64E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_67C")
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67C")
    OP_72(0x1, 0x4)

    label("loc_67C")

    Return()

    # Function_1_629 end

    def Function_2_67D(): pass

    label("Function_2_67D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_692")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_67D")

    label("loc_692")

    Return()

    # Function_2_67D end

    def Function_3_693(): pass

    label("Function_3_693")

    Call(0, 4)
    Return()

    # Function_3_693 end

    def Function_4_698(): pass

    label("Function_4_698")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_740")

    ChrTalk(    #0
        0x8,
        (
            "Welcome.\x01",
            "The History Museum is open for free to all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "At the behest of the queen, who hopes our service\x01",
            "will help the citizens relax in some way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF1")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x8,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Did you find the young lady you were\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1000FY-Yeah...\x02\x03",

            "Don't worry, we found her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "I see, that's good to hear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            " When I heard about the incident late last night,\x01",
            "I was worried about the young lady...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "I'm very relieved to hear you found her.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1647)
    Jump("loc_91E")

    label("loc_893")


    ChrTalk(    #8
        0x8,
        (
            " When I heard about the incident late last night,\x01",
            "I was worried about the young lady...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "I'm very relieved to hear you found her.\x02",
    )

    CloseMessageWindow()

    label("loc_91E")

    Jump("loc_BF1")

    label("loc_921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_9DD")

    ChrTalk(    #10
        0x8,
        (
            "The young lady asked me, 'Do you know\x01",
            "where the colorless fish are?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "She had the most devilish expression on her\x01",
            "face when she asked, this little lady of yours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(    #12
        0x8,
        (
            "If you're looking for the young lady,\x01",
            "I saw her a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "I believe she's within the building.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE7")

    label("loc_A51")


    ChrTalk(    #14
        0x8,
        (
            "If we find the young lady you're looking for,\x01",
            "we'll contact the guild immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "This is the only entrance,\x01",
            "so I doubt I missed anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7")

    Jump("loc_BF1")

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B47")

    ChrTalk(    #16
        0x8,
        (
            "The museum will be closing momentarily.\x01",
            "We eagerly await your next visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF1")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_BBD")

    ChrTalk(    #17
        0x8,
        (
            "Lately, even the museum head and\x01",
            "the curators seem to be very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "I hope they don't fall ill...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF1")

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_BF1")

    ChrTalk(    #19
        0x8,
        "Welcome, welcome to the History Museum.\x02",
    )

    CloseMessageWindow()

    label("loc_BF1")

    TalkEnd(0x8)
    Return()

    # Function_4_698 end

    def Function_5_BF5(): pass

    label("Function_5_BF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CDC")

    ChrTalk(    #20
        0xFE,
        (
            "There's no particular damage to the\x01",
            "History Museum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Even so, it doesn't change that\x01",
            "it makes daily life hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "This event has made it very clear just how\x01",
            "heavily we were relying on orbal energy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDC")

    Jump("loc_1A8A")

    label("loc_CDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(    #23
        0xFE,
        (
            "This has been a good experience\x01",
            "from a management perspective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I will need to be careful to ensure it never\x01",
            "happens again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #25
        0xFE,
        "Ohh, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "We did end up finding the photo of the Arseille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1004FOh...\x02\x03",

            "#1007FI'm sorry that we couldn't be of much help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "No, no, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "It's back safe. That's what matters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1008FI appreciate you saying that.\x02\x03",

            "#1015FSo...where did you find it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Surprisingly, it was apparently found in\x01",
            "the closed Grand Arena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "A member of the maintenance staff found\x01",
            "it during a periodic inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007FHmmm, to think it'd be found there\x01",
            "of all places.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x4000)
    OP_A2(0x3)
    Jump("loc_1A8A")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_121A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_11BB")

    ChrTalk(    #34
        0xFE,
        "Would you like to see the card again?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05'Beauteous princess and her companions. The image\x01",
            "of the proud white falcon has fallen into my hands.'\x02\x03",

            "Should you seek it, then answer to my challenge.'\x02\x03",

            "'The first key is in the residence of the aged\x01",
            "general. Search the [Onlooker of Time].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #36
        0xFE,
        "Well, then, I expect good news.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B8")

    label("loc_1193")


    ChrTalk(    #37
        0xFE,
        "Well, then, I expect good news.\x02",
    )

    CloseMessageWindow()

    label("loc_11B8")

    Jump("loc_1217")

    label("loc_11BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_11DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_11D7")
    Call(1, 1)
    Jump("loc_11DB")

    label("loc_11D7")

    Call(1, 0)

    label("loc_11DB")

    Jump("loc_1217")

    label("loc_11DE")


    ChrTalk(    #38
        0xFE,
        "This is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Who could have done this...\x02",
    )

    CloseMessageWindow()

    label("loc_1217")

    Jump("loc_1A8A")

    label("loc_121A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(    #40
        0xFE,
        (
            "I've had a request from Jimmy. Apparently\x01",
            "he wants to become a curator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "He has no experience, but given his history he\x01",
            "has a very unique and interesting perspective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I imagine it will take some time, but he IS\x01",
            "promising, so I think I'll employ him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "The devices and artifacts in each tower...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "There's a mountain of things I'd like to\x01",
            "investigate, so I need him to work hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1427")

    label("loc_13BE")


    ChrTalk(    #45
        0xFE,
        (
            "He is familiar with rumors and legends\x01",
            "of treasure, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Quite the interesting personage.\x02",
    )

    CloseMessageWindow()

    label("loc_1427")

    Jump("loc_1A8A")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(    #47
        0xFE,
        (
            "The investigation and research of the towers,\x01",
            "and analysis of artifacts brought to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "There's so much to do, we can't\x01",
            "help but lack people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Thankfully, we have a budget surplus,\x01",
            "so I can consider hiring new curators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1683")

    ChrTalk(    #50
        0xFE,
        (
            "I had Archbishop Currant take a look at it,\x01",
            "but apparently the History Museum is free\x01",
            "to keep the artifact that was brought to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "There's a high possibility for artifacts\x01",
            "to be related to ancient Zemuria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I am greatly looking forward to using\x01",
            "it as a subject of investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I'm quite thankful to Jimmy.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1722")

    label("loc_1683")


    ChrTalk(    #54
        0xFE,
        (
            "There's a high possibility for artifacts\x01",
            "to be related to ancient Zemuria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I am greatly looking forward to using\x01",
            "it as a subject of investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1722")

    Jump("loc_1A8A")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1814")

    ChrTalk(    #56
        0xFE,
        (
            "Functioning artifacts must be turned\x01",
            "over to the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "This thing that was brought to us seems\x01",
            "completely nonfunctional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I suppose I will add it to our collection after\x01",
            "inquiring with the Septian Church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D2")

    ChrTalk(    #59
        0xFE,
        (
            "Professor Alba, who was staying here before,\x01",
            "was quite the man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "His theory about the Sept-Terrions, or Seven\x01",
            "Treasures, was quite charming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I'd like to hear his opinion about the mysterious\x01",
            "devices in the ancient towers that have\x01",
            "activated recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Apparently he investigated the towers\x01",
            "across the regions, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1015F(...Professor Alba?)\x02\x03",

            "#1003F(Huh... Who was that...? It seems familiar...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1A8A")

    label("loc_19D2")


    ChrTalk(    #64
        0xFE,
        (
            "Professor Alba, who was staying here before,\x01",
            "was quite the man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I'd like to hear his opinion about the mysterious\x01",
            "devices in the ancient towers that have\x01",
            "activated recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8A")

    TalkEnd(0xFE)
    Return()

    # Function_5_BF5 end

    def Function_6_1A8E(): pass

    label("Function_6_1A8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BE2")

    ChrTalk(    #66
        0xFE,
        (
            "Something strange has happened to the towers\x01",
            "in each region that we were researching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "The top of the towers were engulfed in some\x01",
            "strange blackness, and then went back to\x01",
            "normal after a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "I wonder what that was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Actually, the orbal shutdown started when all\x01",
            "of the towers' abnormalities had stopped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A8")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1CAD")

    ChrTalk(    #70
        0xFE,
        (
            "There were still dragons alive during the\x01",
            "Zemurian age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Now that I think about it, I read a report from\x01",
            "a person researching the ancient dragons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I believe they lived in Bose...\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A8")

    label("loc_1CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_END)), "loc_1D28")

    ChrTalk(    #73
        0xFE,
        (
            "There was a girl here in white\x01",
            "clothes looking around before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "She wasn't a lost child, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E1E")

    label("loc_1D28")


    ChrTalk(    #75
        0xFE,
        (
            "The young man who brought that artifact\x01",
            "in is pretty interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "He's got some talent for excavation and\x01",
            "archeology, which I guess makes sense\x01",
            "given he was a treasure hunter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Sometimes he says some incomprehensible\x01",
            "stuff, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_25A8")

    label("loc_1E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EE3")

    ChrTalk(    #78
        0xFE,
        "Hmm... The investigation's hit a dead end...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "At this rate, I'm not going to make\x01",
            "the announcement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "If Professor Alba was here, I could've\x01",
            "consulted with him, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A8")

    label("loc_1EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1F7F")

    ChrTalk(    #81
        0xFE,
        (
            "The Great Collapse that was the trigger to\x01",
            "the destruction of the Zemurian culture...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Perhaps it has something to do with the towers...\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A8")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_25A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F0")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #83
        0xFE,
        "Oh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004FY-You, aren't you...\x02\x03",

            "#1008FWho are you again?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #85
        0xFE,
        "Ouch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Ahaha... I'm Santos with the History Museum.\x01",
            "I asked you to take photos of the tower in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1008FAh, yeah, yeah, I remember now.\x02\x03",

            "#1000FSo how'd it go after that? Find out\x01",
            "anything about the tower device?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "No... Embarrassingly, I haven't really had\x01",
            "any success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Everything about it is just so unknown...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "However, we do know the tower itself was\x01",
            "built during the ancient Zemurian era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "First, I suppose I need to check out what\x01",
            "references we have in that area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1015FHmmm, archeology doesn't seem like the kind of\x01",
            "thing that comes up with results that easily, huh.\x02\x03",

            "#1011FI guess all I can say is 'good luck'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Yes, I'll do my best thinking of this as the first\x01",
            "step to uncovering lost, ancient knowledge.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1648)
    Jump("loc_25A8")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BA")

    ChrTalk(    #94
        0xFE,
        (
            "Those mysterious devices in the ancient\x01",
            "towers that activated... Investigating them\x01",
            "is my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "The devices are placed on the roofs of the\x01",
            "ruin towers, and their purpose is completely\x01",
            "unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "We're continuing to research them, but we\x01",
            "still haven't had any significant success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "However, we did discover the towers themselves\x01",
            "were built in the Zemurian age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I'll just have to slowly peruse through\x01",
            "references about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_25A8")

    label("loc_24BA")


    ChrTalk(    #99
        0xFE,
        (
            "We did discover the towers themselves\x01",
            "were built in the Zemurian age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I'll just have to slowly peruse\x01",
            "through references about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I'll do my best thinking of this as the first\x01",
            "step to uncovering lost, ancient knowledge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A8")

    TalkEnd(0xFE)
    Return()

    # Function_6_1A8E end

    def Function_7_25AC(): pass

    label("Function_7_25AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_26B4")

    ChrTalk(    #102
        0xFE,
        (
            "Even without orbments, you can still look at\x01",
            "ancient relics and imagine the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Archeology should be something doable\x01",
            "even in the greatest trials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Wooooo! This is a true man's romance! I'm not\x01",
            "gonna get down over something like this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F79")

    label("loc_26B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2753")

    ChrTalk(    #105
        0xFE,
        (
            "Woohooo!\x01",
            "The History Museum is willing to hire me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "To me it's like getting paid to treasure hunt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "I feel so happy I could just dance!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F79")

    label("loc_2753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_296E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_289C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(    #108
        0xFE,
        (
            "The girl in a white dress was here just\x01",
            "a bit ago!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "I don't think she could've gone that far.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_27D7")


    ChrTalk(    #110
        0xFE,
        "...A girl in a white dress?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 400)

    ChrTalk(    #111
        0xFE,
        "Well, there...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #112
        0xFE,
        "Whoa! She's gone!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xF6, 400)

    ChrTalk(    #113
        0xFE,
        (
            "But, she was here until just a bit ago,\x01",
            "so she can't have gone that far.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2899")

    Jump("loc_296B")

    label("loc_289C")


    ChrTalk(    #114
        0xFE,
        (
            "*sigh* I'm just wasting money at this point.\x01",
            "I need to get back to Ruan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "But this new man's romance I've discovered\x01",
            "here called archeology...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "I feel as if it would be a waste to just go home.\x02",
    )

    CloseMessageWindow()

    label("loc_296B")

    Jump("loc_2F79")

    label("loc_296E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A64")

    ChrTalk(    #117
        0xFE,
        "Whooooa, this is incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "To think there were things like this in the\x01",
            "ancient past... Truly, they are the treasures\x01",
            "of humanity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Could archeology be the greatest man's romance\x01",
            "that surpasses even treasure hunting?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F79")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2B31")

    ChrTalk(    #120
        0xFE,
        "I handed over that thing to the Museum Director.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Apparently they're looking into whether or not\x01",
            "it's something the museum can hold onto, so I'm\x01",
            "having a wander while they check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F79")

    label("loc_2B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D9E")

    ChrTalk(    #122
        0xFE,
        "The History Museum... Yep, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1000FOh, Jimmy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Whoa. Hey, you're the bracers who saved\x01",
            "me in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1000FWhat are you doing here?\x02\x03",

            "Ah, right...\x01",
            "You're delivering that artifact, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Yeah, it may have lost its power, but\x01",
            "who knows what it might do, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "I'll hand it over to the experts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1000FGood idea.\x02\x03",

            "If you'd also give up on treasure hunting\x01",
            "and get a real job, that'd be even better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Ouch, ouch... But, I'm afraid I can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I suppose it'd be different if I could find\x01",
            "something even more romantic than\x01",
            "being a treasure hunter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2D9E")


    ChrTalk(    #131
        0xFE,
        (
            "The History Museum...\x01",
            "Whoa, yeah, this is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "I'm sure I can leave an artifact here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1000FArtifact?!\x02\x03",

            "In that case, you need to deliver it to\x01",
            "the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Whoa, is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "But, this is an artifact that's already lost\x01",
            "its power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I figured I'd get the History Museum to\x01",
            "take a look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1000FAh, okay...\x02",
    )

    CloseMessageWindow()

    label("loc_2EFD")

    OP_A2(0x1649)
    Jump("loc_2F79")

    label("loc_2F03")


    ChrTalk(    #138
        0xFE,
        (
            "I plan on getting them to examine my little\x01",
            "defunct find here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "First I need to find the person in charge...\x02",
    )

    CloseMessageWindow()

    label("loc_2F79")

    TalkEnd(0xFE)
    Return()

    # Function_7_25AC end

    def Function_8_2F7D(): pass

    label("Function_8_2F7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FFE")

    ChrTalk(    #140
        0xFE,
        (
            "#060FThe person who created this theory's\x01",
            "pretty incredible, huh.\x02\x03",

            "I wanna invent something like this someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_2FFE")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #141
        0xFE,
        (
            "#560FAh, Estelle.\x02\x03",

            "#060FThe spinning wheel's really simple, but it\x01",
            "condensed a lot of different inventions into it.\x02\x03",

            "The person who created this is pretty\x01",
            "incredible, huh.\x02\x03",

            "#061FI wanna invent something like this someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1016F(And she's gotten started...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3114")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F7D end

    def Function_9_3118(): pass

    label("Function_9_3118")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_318F")

    ChrTalk(    #143
        0xFE,
        (
            "#267FTita always gets this weird look in her eyes\x01",
            "when she sees a machine.\x02\x03",

            "Is she always like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323D")

    label("loc_318F")


    ChrTalk(    #144
        0xFE,
        (
            "#266FTita always gets this weird look in her eyes\x01",
            "when she sees a machine.\x02\x03",

            "#267FIs she always like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1016FS-Sorry. That's pretty much her default setting.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_323D")

    TalkEnd(0xFE)
    Return()

    # Function_9_3118 end

    def Function_10_3241(): pass

    label("Function_10_3241")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0xFE,
        (
            "Apparently the queen mandated that attendance\x01",
            "is free for this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "Seems to have cheered my children up.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_3241 end

    def Function_11_32BE(): pass

    label("Function_11_32BE")

    TalkBegin(0xFE)

    ChrTalk(    #148
        0xFE,
        "I bet we could use this without orbals...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_32BE end

    def Function_12_32F4(): pass

    label("Function_12_32F4")

    TalkBegin(0xFE)

    ChrTalk(    #149
        0xFE,
        "Haha, what a curious design...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_32F4 end

    def Function_13_331F(): pass

    label("Function_13_331F")

    TalkBegin(0xFE)

    ChrTalk(    #150
        0xFE,
        (
            "Wooow. So they used stuff like this in the past,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "If orbal energy never returns, I guess we'll\x01",
            "go back to the era when we used these.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_331F end

    def Function_14_33BC(): pass

    label("Function_14_33BC")

    TalkBegin(0xFE)

    ChrTalk(    #152
        0xFE,
        (
            "I came here thinking it might be at\x01",
            "least a chance to clear my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "I hope everything goes back to normal soon...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_33BC end

    def Function_15_3440(): pass

    label("Function_15_3440")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3457")
    Call(0, 27)
    Call(0, 28)

    label("loc_3457")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    def lambda_34AE():
        OP_6D(1000, 4000, -2000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34AE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #154
        0x101,
        (
            "#1015F#6PYou said you came in here\x01",
            "before, right, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x107,
        "#067F#3PYeah, we looked at everything.\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #156
        0x8,
        "#3PGood day! Are you visitors?\x02",
    )

    CloseMessageWindow()

    def lambda_35D8():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35D8)

    def lambda_35F0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35F0)
    Sleep(100)

    def lambda_3603():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3603)
    Sleep(100)

    def lambda_3616():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3616)
    Sleep(100)

    def lambda_3629():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3629)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #157
        0x101,
        (
            "#1016F#1PUm, we're looking for someone,\x01",
            "actually...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #158
        "\x07\x05Estelle described Renne to the receptionist.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #159
        0x8,
        (
            "Oh! That young lady in the white dress\x01",
            "who was with the girl you're\x01",
            "accompanying today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x107,
        (
            "#560F#1PYeah, that's her!\x01",
            "You remembered us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        "Well, you two stood out a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "I'm afraid I haven't seen her today,\x01",
            "though, no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1015F#1PNuts... She must be somewhere else.\x02\x03",

            "#1006FIf you see her, contact the guild\x01",
            "at once, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        "Yes, I will.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_A2(0x162F)
    OP_28(0x8C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_15_3440 end

    def Function_16_383F(): pass

    label("Function_16_383F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3856")
    Call(0, 27)
    Call(0, 28)

    label("loc_3856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391F")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set 'Inquiring about Renne at the Museum 1' as not seen \x01",      # 0
            "Set 'Inquiring about Renne at the Museum 1' as seen\x01",           # 1
            "No change\x01",                                                     # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3913"),
        (1, "loc_3919"),
        (SWITCH_DEFAULT, "loc_391F"),
    )


    label("loc_3913")

    OP_A3(0x162F)
    Jump("loc_391F")

    label("loc_3919")

    OP_A2(0x162F)
    Jump("loc_391F")

    label("loc_391F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB5")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    def lambda_397E():
        OP_6D(1000, 4000, -2000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_397E)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #165
        0x101,
        (
            "#1015F#6PYou said you came in here\x01",
            "before, right, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x107,
        "#067F#3PYeah, we looked at everything!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #167
        0x8,
        "#3PGood day! Are you visitors?\x02",
    )

    CloseMessageWindow()

    def lambda_3AA9():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA9)

    def lambda_3AC1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AC1)
    Sleep(100)

    def lambda_3AD4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3AD4)
    Sleep(100)

    def lambda_3AE7():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3AE7)
    Sleep(100)

    def lambda_3AFA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3AFA)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #168
        0x101,
        (
            "#1006F#1PUm, we're looking for someone,\x01",
            "actually...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #169
        "\x07\x05Estelle described Renne to the receptionist.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #170
        0x8,
        (
            "Oh! That young lady in the white dress\x01",
            "who was with the girl you're\x01",
            "accompanying today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x107,
        (
            "#560F#1PYeah, that's her!\x01",
            "You remembered us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        "Well, you two stood out a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        "And yes, I saw her just a little while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        (
            "She should still be in the museum,\x01",
            "I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E57")

    label("loc_3CB5")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_43(0xF9, 0x1, 0x0, 0x14)
    WaitChrThread(0xF9, 0x1)
    OP_0D()

    ChrTalk(    #175
        0x8,
        "Oh, hello again!\x02",
    )

    CloseMessageWindow()

    def lambda_3D77():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D77)

    def lambda_3D8F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D8F)
    Sleep(100)

    def lambda_3DA2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3DA2)
    Sleep(100)

    def lambda_3DB5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3DB5)
    Sleep(100)

    def lambda_3DC8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3DC8)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #176
        0x8,
        (
            "If you're still looking for that young lady,\x01",
            "I saw her just a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        "She should still be in the museum, I believe.\x02",
    )

    CloseMessageWindow()

    label("loc_3E57")


    ChrTalk(    #178
        0x101,
        "#1006F#1PAwesome! Thanks!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3EAC")

    ChrTalk(    #179
        0x106,
        "#051F#5PAll right. Let's go catch her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED7")

    label("loc_3EAC")


    ChrTalk(    #180
        0x103,
        "#021F#5POkay! Let's go trap a kitten.\x02",
    )

    CloseMessageWindow()

    label("loc_3ED7")

    OP_4B(0x8, 255)
    OP_A2(0x1630)
    OP_28(0x8C, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_16_383F end

    def Function_17_3EE7(): pass

    label("Function_17_3EE7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_3F0E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F0E)
    OP_8E(0xFE, 0x15E, 0x0, 0xFFFFEC46, 0x7D0, 0x0)
    Return()

    # Function_17_3EE7 end

    def Function_18_3F2F(): pass

    label("Function_18_3F2F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_3F56():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F56)
    OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFEBEC, 0x7D0, 0x0)
    Return()

    # Function_18_3F2F end

    def Function_19_3F77(): pass

    label("Function_19_3F77")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_3F9E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F9E)
    OP_8E(0xFE, 0xE6, 0x0, 0xFFFFE660, 0x7D0, 0x0)
    Return()

    # Function_19_3F77 end

    def Function_20_3FBF(): pass

    label("Function_20_3FBF")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_3FE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FE6)
    OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFE660, 0x7D0, 0x0)
    Return()

    # Function_20_3FBF end

    def Function_21_4007(): pass

    label("Function_21_4007")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401E")
    Call(0, 27)
    Call(0, 28)

    label("loc_401E")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0x8, 255)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4046"),
        (104, "loc_4086"),
        (SWITCH_DEFAULT, "loc_40C6"),
    )


    label("loc_4046")

    OP_6D(-5980, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_40C6")

    label("loc_4086")

    OP_6D(5990, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_40C6")

    label("loc_40C6")

    FadeToBright(2000, 0)
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(400)
    OP_43(0x107, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x18)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    WaitChrThread(0xF9, 0x1)
    OP_0D()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2600, 0, -5900, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4126"),
        (104, "loc_4135"),
        (SWITCH_DEFAULT, "loc_4138"),
    )


    label("loc_4126")

    TurnDirection(0x101, 0x11, 400)
    Sleep(500)
    Jump("loc_4138")

    label("loc_4135")

    Jump("loc_4138")

    label("loc_4138")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #181
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()
    OP_6D(2500, 0, -5250, 2000)

    ChrTalk(    #182
        0x11,
        (
            "#1306F#6PHey, miss.\x02\x03",

            "Do you know where the colorless fish are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x11,
        "#263F#6PHeehee! Goodbye!\x02",
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x1A)
    Sleep(500)

    def lambda_41F7():

        label("loc_41F7")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_41F7")

    QueueWorkItem2(0x8, 1, lambda_41F7)

    ChrTalk(    #185 op#5
        0x8,
        "Ah, well...\x05\x02",
    )

    Sleep(2000)

    ChrTalk(    #186
        0x8,
        (
            "#6PAh, miss, pardon me!\x01",
            "Your friends are--\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -840, 1270, 3460, 0)
    SetChrPos(0x107, 230, 1270, 3460, 0)
    SetChrPos(0xF7, -680, 1270, 3460, 0)
    SetChrPos(0xF9, 350, 1270, 3460, 0)

    def lambda_429C():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFEB7E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_429C)
    Sleep(100)

    def lambda_42BC():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFFEA48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_42BC)
    Sleep(500)

    def lambda_42DC():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF02E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_42DC)
    Sleep(100)

    def lambda_42FC():
        OP_8E(0xFE, 0x15E, 0x0, 0xFFFFF02E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_42FC)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #187
        0x101,
        "#1020F#5PWait, RENNE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        "#065F#5PRenne! Please wait!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)

    def lambda_4362():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4362)
    Sleep(300)

    def lambda_4382():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4382)
    Sleep(300)

    def lambda_43A2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43A2)

    def lambda_43B4():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_43B4)
    Sleep(300)

    def lambda_43D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_43D4)

    def lambda_43E6():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_43E6)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4101   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_21_4007 end

    def Function_22_4409(): pass

    label("Function_22_4409")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4429"),
        (104, "loc_443D"),
        (SWITCH_DEFAULT, "loc_4451"),
    )


    label("loc_4429")

    SetChrPos(0xFE, -5150, 6550, 10500, 180)
    Jump("loc_4451")

    label("loc_443D")

    SetChrPos(0xFE, 5340, 6550, 10500, 180)
    Jump("loc_4451")

    label("loc_4451")


    def lambda_4457():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4457)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    Return()

    # Function_22_4409 end

    def Function_23_4478(): pass

    label("Function_23_4478")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4498"),
        (104, "loc_44AC"),
        (SWITCH_DEFAULT, "loc_44C0"),
    )


    label("loc_4498")

    SetChrPos(0xFE, -6400, 6540, 10480, 180)
    Jump("loc_44C0")

    label("loc_44AC")

    SetChrPos(0xFE, 6600, 6550, 10500, 180)
    Jump("loc_44C0")

    label("loc_44C0")


    def lambda_44C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44C6)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
    Return()

    # Function_23_4478 end

    def Function_24_44E7(): pass

    label("Function_24_44E7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4507"),
        (104, "loc_451B"),
        (SWITCH_DEFAULT, "loc_452F"),
    )


    label("loc_4507")

    SetChrPos(0xFE, -5150, 6550, 10500, 180)
    Jump("loc_452F")

    label("loc_451B")

    SetChrPos(0xFE, 5340, 6550, 10500, 180)
    Jump("loc_452F")

    label("loc_452F")


    def lambda_4535():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4535)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
    Return()

    # Function_24_44E7 end

    def Function_25_4556(): pass

    label("Function_25_4556")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_4576"),
        (104, "loc_458A"),
        (SWITCH_DEFAULT, "loc_459E"),
    )


    label("loc_4576")

    SetChrPos(0xFE, -6400, 6540, 10480, 180)
    Jump("loc_459E")

    label("loc_458A")

    SetChrPos(0xFE, 6600, 6550, 10500, 180)
    Jump("loc_459E")

    label("loc_459E")


    def lambda_45A4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45A4)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
    Return()

    # Function_25_4556 end

    def Function_26_45C5(): pass

    label("Function_26_45C5")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0x0, 0x0, 0xFFFFE2B4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0xFFFFDF3A, 0x7D0, 0x0)

    def lambda_45FA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45FA)
    OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_45C5 end

    def Function_27_4620(): pass

    label("Function_27_4620")

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
        (0, "loc_469C"),
        (1, "loc_46A2"),
        (SWITCH_DEFAULT, "loc_46A8"),
    )


    label("loc_469C")

    OP_A2(0x1200)
    Jump("loc_46A8")

    label("loc_46A2")

    OP_A2(0x1201)
    Jump("loc_46A8")

    label("loc_46A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_46B6")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_46BA")

    label("loc_46B6")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_46BA")

    Return()

    # Function_27_4620 end

    def Function_28_46BB(): pass

    label("Function_28_46BB")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_46FA")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_4714")

    label("loc_46FA")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_4714")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_28_46BB end

    def Function_29_4734(): pass

    label("Function_29_4734")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #189
        (
            "\x07\x05[Tetracyclic Tower Outer Wall Segment]         Age: Pre-Septian?\x01",
            "This wall segment was cut and carried from a Tetracyclic Tower--\x01",
            "a structure built shortly after the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #190
        (
            "\x07\x05Depicted upon it are a staff-wielding priest and a winged god-\x01",
            "like being, typical of period frescas. Scholars continue to\x01",
            "examine the design for any connection with Aidios.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_29_4734 end

    def Function_30_48CF(): pass

    label("Function_30_48CF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        (
            "\x07\x05[Septian 1150-1200  ~The Orbal Post-Revolutionary World~]\x01",
            "It's been only 50 years since Prof. C. Epstein invented orbments,\x01",
            "and world technology has advanced at lightning speed ever since.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #192
        (
            "\x07\x05Perhaps the most notable representative of these advances is the\x01",
            "modern orbal-powered airship. These 'orbalships' are already used\x01",
            "extensively in Liberl, but neighboring nations such as Erebonia\x01",
            "have also begun to devote themselves to their manufacture as well,\x01",
            "and smaller-sized airships are also used.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_48CF end

    def Function_31_4AF3(): pass

    label("Function_31_4AF3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #193
        (
            "\x07\x05[Pre-Septian Calendar  ~The Ancient Civilization of Zemuria~]\x01",
            "Around 1,200 years ago, the advanced civilization of Zemuria was\x01",
            "at its peak. Then, suddenly and inexplicably, it disappeared.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #194
        (
            "\x07\x05A 'Great Collapse' occurred, destroying the Zemurian culture and\x01",
            "plunging its people into a dark age of ruin. The items exhibited\x01",
            "on the first floor are from the very beginning of this era. They\x01",
            "aren't believed to be products of the ancient civilization itself,\x01",
            "but nonetheless, its influence is clearly visible upon them, giving\x01",
            "them immense academic worth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_31_4AF3 end

    def Function_32_4D4E(): pass

    label("Function_32_4D4E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #195
        (
            "\x07\x05[Ancient Lantern]                              Age: Pre-Septian?\x01",
            "A device built to hold fire. Most often found near towers and\x01",
            "other ceremonial structures. May have religious significance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_4D4E end

    def Function_33_4E3D(): pass

    label("Function_33_4E3D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #196
        (
            "\x07\x05[Stone Pillar with Relief]                     Age: Pre-Septian?\x01",
            "Found at the bottom of Lake Valleria. Adorned with reliefs\x01",
            "similar to those found on the walls of the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_33_4E3D end

    def Function_34_4F2A(): pass

    label("Function_34_4F2A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #197
        (
            "\x07\x05[Floor Tile]                                   Age: Pre-Septian?\x01",
            "A piece of tiled floor from inside a ruined building. Broken\x01",
            "stones fit together to create beautiful and intricate patterns.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_4F2A end

    def Function_35_501A(): pass

    label("Function_35_501A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #198
        (
            "\x07\x05[Septian Calendar 1-500  ~The Dark Age of Ruin~]\x01",
            "Immediately following the Great Collapse, the world was plunged\x01",
            "into confusion, signaling the beginning of what came to be\x01",
            "referred to as the Dark Ages.\x02\x03",

            "This era was defined by almost endless conflict between various\x01",
            "powers and numerous nations, large and small, and lasted for\x01",
            "roughly 500 years.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_501A end

    def Function_36_51A7(): pass

    label("Function_36_51A7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #199
        (
            "\x07\x05[Knights' Equipment]                    Age: Septian Calendar 500\x01",
            "In an era defined by conflict, war became a way of life, and as a\x01",
            "result, warriors came to wield great influence in society. This\x01",
            "eventually led to them becoming a privileged social class of their\x01",
            "own.\x02\x03",

            "The knights wielded armaments like these when they went out onto \x01",
            "the battlefield, returning with more spoils and land, and gradually\x01",
            "increasing their influence and power all the more.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_51A7 end

    def Function_37_539F(): pass

    label("Function_37_539F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #200
        (
            "\x07\x05[Septian Calendar 500-1100  ~The Septian Era~]\x01",
            "The first appearance of the Septian Church occurred around the\x01",
            "year 500 and marked the end of the Dark Ages.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #201
        (
            "\x07\x05The church, centered around the 'Goddess of the Sky' Aidios and\x01",
            "espousing an ideology of human salvation, began to take an active\x01",
            "role in society and rapidly permeated social consciousness.\x01",
            "Eventually, the nobility and knight class could no longer ignore\x01",
            "the church's power, and a new order was established with the\x01",
            "church at the center.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_37_539F end

    def Function_38_55C4(): pass

    label("Function_38_55C4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #202
        (
            "\x07\x05[Ancient Artifacts]                                 Age: Unknown\x01",
            "'Artifact' (noun) - A relic of any shape or size found in an\x01",
            "ancient ruin and generally of unknown or uncertain purpose.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #203
        (
            "\x07\x05The church believes these artifacts have some connection with\x01",
            "the Sept-Terrions--gifts from Aidios--and their recovery is\x01",
            "one of the duties that the church fulfills.\x01",
            "Artifacts are said to have supernatural powers, but those on\x01",
            "display here are all ones that have since lost said powers and\x01",
            "are no longer functional.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_55C4 end

    def Function_39_57F1(): pass

    label("Function_39_57F1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #204
        (
            "\x07\x05[Church Ritual Items]          Age: Septian Calendar 900 (approx.)\x01",
            "The church has long been a source of art, and this has been true\x01",
            "since the dawn of the Septian Era. It was around the year 900,\x01",
            "however, that the current likeness of Aidios is thought to have\x01",
            "been first created. Likewise, many of the ritual items used by\x01",
            "the church today first assumed their present forms in this time\x01",
            "period, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_57F1 end

    def Function_40_59B2(): pass

    label("Function_40_59B2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #205
        (
            "\x07\x05[Church Testaments, Manuscript]        Age: Septian Calendar 500\x01",
            "A handwritten copy of the scriptures used by the church at the\x01",
            "end of the Dark Ages. The ability to print did not exist in the\x01",
            "Middle Ages, leaving no choice but to copy by hand onto pieces\x01",
            "of parchment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_59B2 end

    def Function_41_5AF1(): pass

    label("Function_41_5AF1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #206
        (
            "\x07\x05[Medieval Loom]                        Age: Septian Calendar 900\x01",
            "A man-powered machine used to spin thread. As the Septian Era\x01",
            "continued and people became accustomed to peace, cotton and\x01",
            "other crops became more widely cultivated and sold. This was\x01",
            "also the era in which handicrafts with the intent to obtain money\x01",
            "came into practice.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_5AF1 end

    SaveToFile()

Try(main)
