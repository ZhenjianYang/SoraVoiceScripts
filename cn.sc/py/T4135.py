from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '莉西娅',                               # 9
        '馆长',                                 # 10
        '森特',                                 # 11
        '吉米',                                 # 12
        '王都市民',                             # 13
        '王都市民',                             # 14
        '王都市民',                             # 15
        '王都市民',                             # 16
        '王都市民',                             # 17
        '玲',                                   # 18
        '提妲',                                 # 19
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
        "Function_5_A3F",          # 05, 5
        "Function_6_142D",         # 06, 6
        "Function_7_1AEE",         # 07, 7
        "Function_8_21AC",         # 08, 8
        "Function_9_22D4",         # 09, 9
        "Function_10_2398",        # 0A, 10
        "Function_11_23E5",        # 0B, 11
        "Function_12_240F",        # 0C, 12
        "Function_13_2433",        # 0D, 13
        "Function_14_249C",        # 0E, 14
        "Function_15_24E9",        # 0F, 15
        "Function_16_2869",        # 10, 16
        "Function_17_2E0C",        # 11, 17
        "Function_18_2E54",        # 12, 18
        "Function_19_2E9C",        # 13, 19
        "Function_20_2EE4",        # 14, 20
        "Function_21_2F2C",        # 15, 21
        "Function_22_330D",        # 16, 22
        "Function_23_337C",        # 17, 23
        "Function_24_33EB",        # 18, 24
        "Function_25_345A",        # 19, 25
        "Function_26_34C9",        # 1A, 26
        "Function_27_3524",        # 1B, 27
        "Function_28_35C0",        # 1C, 28
        "Function_29_3639",        # 1D, 29
        "Function_30_37AB",        # 1E, 30
        "Function_31_3947",        # 1F, 31
        "Function_32_3AA2",        # 20, 32
        "Function_33_3BBB",        # 21, 33
        "Function_34_3C9B",        # 22, 34
        "Function_35_3D65",        # 23, 35
        "Function_36_3E6C",        # 24, 36
        "Function_37_3F7E",        # 25, 37
        "Function_38_40EE",        # 26, 38
        "Function_39_42A9",        # 27, 39
        "Function_40_43D5",        # 28, 40
        "Function_41_44BF",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_704")

    ChrTalk(    #0
        0x8,
        (
            "欢迎光临，\x01",
            "历史资料馆免费开放中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "为了让市民朋友\x01",
            "能有所放松，\x01",
            "女王陛下作了这一决定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3B")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x8,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "后来有没有找到\x01",
            "和你们同行的那位小姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1000F嗯、嗯……\x02\x03",

            "没事了，\x01",
            "我们已经找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "是吗？太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "听到昨夜发生的事件，\x01",
            "我就有点担心\x01",
            "那位小姐了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "听说已经找到了，\x01",
            "我总算放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1647)
    Jump("loc_86F")

    label("loc_814")


    ChrTalk(    #8
        0x8,
        (
            "听到昨夜发生的事件，\x01",
            "我就有点担心\x01",
            "那位小姐了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "听说已经找到了，\x01",
            "我总算放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86F")

    Jump("loc_A3B")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_8EC")

    ChrTalk(    #10
        0x8,
        (
            "线索就是『你知道哪儿有\x01",
            "没有颜色的鱼吗？』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "和你们一起的那位小姐用\x01",
            "一种很恶作剧的表情\x01",
            "这么说道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_END)), "loc_936")

    ChrTalk(    #12
        0x8,
        (
            "和你们一起的那位\x01",
            "小妹妹来过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "我想她应该\x01",
            "还在馆内。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E")

    label("loc_936")


    ChrTalk(    #14
        0x8,
        (
            "我如果看见你们要找的\x01",
            "那位小姐我会联系协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "入口仅此一处，\x01",
            "应该不会漏看的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E")

    Jump("loc_A3B")

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CA")

    ChrTalk(    #16
        0x8,
        (
            "本馆很快就要关门了。\x01",
            "欢迎您下次光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3B")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A0F")

    ChrTalk(    #17
        0x8,
        (
            "最近，馆长和研究员\x01",
            "都很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "希望他们保重身体……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3B")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_A3B")

    ChrTalk(    #19
        0x8,
        (
            "欢迎光临，\x01",
            "欢迎光临历史资料馆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3B")

    TalkEnd(0x8)
    Return()

    # Function_4_698 end

    def Function_5_A3F(): pass

    label("Function_5_A3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AE2")

    ChrTalk(    #20
        0xFE,
        (
            "历史资料馆这边没什么\x01",
            "具体的损失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "不过人民生活受到冲击的\x01",
            "事实仍然无法改变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "通过这次的事件终于知道\x01",
            "我们平时是多么依赖导力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE2")

    Jump("loc_1429")

    label("loc_AE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(    #23
        0xFE,
        (
            "这次事件从管理的角度来看\x01",
            "也算是积累了好的经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "必须防范类似事件的\x01",
            "再度发生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1429")

    label("loc_B53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF0")

    ChrTalk(    #25
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "埃尔赛尤的照片\x01",
            "后来顺利找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1004F这样啊……\x02\x03",

            "#1007F非常抱歉。\x01",
            "没能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "哪里哪里，\x01",
            "别介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "既然顺利找回来了，\x01",
            "也就没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1008F很感激您能这么说。\x02\x03",

            "#1015F那么……\x01",
            "是在哪儿找到的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "令人不可思议的是\x01",
            "居然是在关闭中的竞技场\x01",
            "找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "好像是做定期检查的\x01",
            "警卫员找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F唔～想不到\x01",
            "是在那种地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x4000)
    OP_A2(0x3)
    Jump("loc_1429")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_EC6")

    ChrTalk(    #34
        0xFE,
        (
            "要不要再\x01",
            "看一次卡片？\x02",
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
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA5")
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05　　美丽的公主及其随从啊。　　\x01",
            "　　 高尚的白鹰剪影画\x01",
            "　　    飘落在我手中。　　\x02\x03",

            "　　  如果就想要寻求它\x01",
            "　　  就要回应我的挑战。 　\x02\x03",

            "　  第一把钥匙在老将之居。　　\x01",
            "　 探索『时间的旁观者』吧。　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #36
        0xFE,
        "那我就等着你们的好消息。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC3")

    label("loc_EA5")


    ChrTalk(    #37
        0xFE,
        "那我就等着你们的好消息。\x02",
    )

    CloseMessageWindow()

    label("loc_EC3")

    Jump("loc_F20")

    label("loc_EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_EE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_EE2")
    Call(1, 1)
    Jump("loc_EE6")

    label("loc_EE2")

    Call(1, 0)

    label("loc_EE6")

    Jump("loc_F20")

    label("loc_EE9")


    ChrTalk(    #38
        0xFE,
        (
            "嗯嗯……\x01",
            "真让人头痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "究竟是谁会这么做呢……\x02",
    )

    CloseMessageWindow()

    label("loc_F20")

    Jump("loc_1429")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_105B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")

    ChrTalk(    #40
        0xFE,
        (
            "吉米申请要当\x01",
            "研究员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "他虽然毫无经验，\x01",
            "不过经历很独特，\x01",
            "而且观点也很有趣。　　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "虽然要花点时间，\x01",
            "不过因为他有潜力，我们还是决定录用他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "各塔的装置和古代遗物……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "有很多事要调查，\x01",
            "希望他能多多活跃。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1058")

    label("loc_1015")


    ChrTalk(    #45
        0xFE,
        (
            "他似乎对财宝的传言和传说\x01",
            "相当地了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "是个很有趣的人才。\x02",
    )

    CloseMessageWindow()

    label("loc_1058")

    Jump("loc_1429")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_10EA")

    ChrTalk(    #47
        0xFE,
        (
            "塔的调查、研究和送来的\x01",
            "古代遗物的解析……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "有很多事要做，\x01",
            "人手实在不足啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "还好预算充裕，\x01",
            "要商量一下增加研究员的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1429")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1210")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B5")

    ChrTalk(    #50
        0xFE,
        (
            "我让卡兰大主教看了，\x01",
            "他说被送来的古代遗物\x01",
            "留在资料馆也没关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "古代遗物很可能和古代\x01",
            "塞姆里亚文明有关……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "能够把它作为研究对象\x01",
            "我也很期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "这也要感谢吉米。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_120D")

    label("loc_11B5")


    ChrTalk(    #54
        0xFE,
        (
            "古代遗物很可能和古代\x01",
            "塞姆里亚文明有关……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "能够把它作为研究对象\x01",
            "我也很期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120D")

    Jump("loc_1429")

    label("loc_1210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(    #56
        0xFE,
        (
            "虽然还有能量的古代遗物\x01",
            "必须交给七耀教会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "不过这次送来的\x01",
            "已经完全丧失了功能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "总之先跟七耀教会\x01",
            "打声招呼再收藏吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1429")

    label("loc_129D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C4")

    ChrTalk(    #59
        0xFE,
        (
            "以前暂居此地的\x01",
            "亚鲁瓦教授真了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "知识自不必说，\x01",
            "他那关于『七至宝』的\x01",
            "假说也非常有魅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "真想听听他对\x01",
            "古代遗迹之塔上\x01",
            "启动的神秘装置的见解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "因为他好像遍游过\x01",
            "那４座塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1015F（………………亚鲁瓦教授？）\x02\x03",

            "#1003F（咦……那是谁……\x01",
            " 好像听说过……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1429")

    label("loc_13C4")


    ChrTalk(    #64
        0xFE,
        (
            "以前暂居此地的\x01",
            "亚鲁瓦教授真了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "关于古代遗迹之塔上\x01",
            "启动的神秘装置，\x01",
            "真想听听他的见解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1429")

    TalkEnd(0xFE)
    Return()

    # Function_5_A3F end

    def Function_6_142D(): pass

    label("Function_6_142D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14EB")

    ChrTalk(    #66
        0xFE,
        (
            "我们正在研究的各地的\x01",
            "塔似乎发生了奇怪的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "塔顶被黑色的东西包着，\x01",
            "不过不久又恢复原样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "那到底是什么呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "对了，导力停止是发生在\x01",
            "塔的异变完全结束之后啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEA")

    label("loc_14EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1568")

    ChrTalk(    #70
        0xFE,
        (
            "在塞姆里亚时期\x01",
            "还有龙生存着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "对了，以前我读过以前\x01",
            "研究龙的人的报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "应该是一个住在\x01",
            "柏斯的人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEA")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_164A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_END)), "loc_15C6")

    ChrTalk(    #73
        0xFE,
        (
            "刚才有个穿白色礼服的\x01",
            "女孩子一个人在参观……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "……不知是不是迷路了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1647")

    label("loc_15C6")


    ChrTalk(    #75
        0xFE,
        (
            "那个持有古代遗物的\x01",
            "青年挺有意思的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "不愧是找寻过宝藏的人，\x01",
            "拥有考古和挖掘的潜质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "虽然他偶尔会说些\x01",
            "不知所云的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1647")

    Jump("loc_1AEA")

    label("loc_164A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C9")

    ChrTalk(    #78
        0xFE,
        (
            "唔……\x01",
            "研究停滞不前了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "这样下去的话，\x01",
            "赶不上结果发表了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "要是亚鲁瓦教授在，\x01",
            "就能和他谈谈了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEA")

    label("loc_16C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1727")

    ChrTalk(    #81
        0xFE,
        (
            "成为塞姆里亚文明消亡\x01",
            "契机的『大崩坏』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "说不定和塔的装置\x01",
            "有某种联系……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AEA")

    label("loc_1727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1AEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_196E")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #83
        0xFE,
        "哎呀……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004F好、好像见过你……\x02\x03",

            "#1008F……你是谁？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #85
        0xFE,
        "唉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "哈哈……我是在卢安委托\x01",
            "你们上塔拍照的森特啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1008F哦，对对。\x01",
            "我没忘记你。\x02\x03",

            "#1000F后来怎么样了？\x01",
            "有没有了解到什么关于塔的装置的情况？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "不……惭愧，\x01",
            "还没什么重要发现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "总之不管从什么角度来看，\x01",
            "不明的地方还是太多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "只知道塔本身是在\x01",
            "塞姆里亚时期建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "只能先从这点上\x01",
            "来解析资料了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1015F呼，考古学的结论也\x01",
            "不是那么容易就做的出呢。\x02\x03",

            "#1011F我只能为你\x01",
            "加油了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "嗯，这是探索遗失的古代睿智的\x01",
            "第一步，我会努力的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1648)
    Jump("loc_1AEA")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A65")

    ChrTalk(    #94
        0xFE,
        (
            "在古代遗迹之塔启动的神秘装置……\x01",
            "我的工作就是调查这个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "装置被安在遗迹塔的塔顶，\x01",
            "作用完全不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "研究还在进行，\x01",
            "不过还没什么重要的发现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "只知道塔本身是在\x01",
            "塞姆里亚时期建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "只能先好好从这点上\x01",
            "来解析资料了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1AEA")

    label("loc_1A65")


    ChrTalk(    #99
        0xFE,
        (
            "只知道塔本身是在\x01",
            "塞姆里亚时期建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "只能先好好从这点上\x01",
            "来解析资料了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "这是探索遗失的古代睿智的\x01",
            "第一步，我会努力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEA")

    TalkEnd(0xFE)
    Return()

    # Function_6_142D end

    def Function_7_1AEE(): pass

    label("Function_7_1AEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BAB")

    ChrTalk(    #102
        0xFE,
        (
            "就算不能用导力器，\x01",
            "也可以看着古代遗迹想象一下啊，\x01",
            "这样就可以使得思想插上翅膀了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "考古学在任何困境中\x01",
            "都能继续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "哇～这才是男人的浪漫！\x01",
            "我不会这么容易就被击倒的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1C20")

    ChrTalk(    #105
        0xFE,
        (
            "哇～我被这座历史资料馆\x01",
            "雇用了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "对我来说就像是拿着工资\x01",
            "来寻找宝藏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "我真是开心得\x01",
            "要发狂了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C7D")

    ChrTalk(    #108
        0xFE,
        (
            "穿白色礼服的女孩子？\x01",
            "刚才还在这里的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "应该还没\x01",
            "走远。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D13")

    label("loc_1C7D")


    ChrTalk(    #110
        0xFE,
        "……穿白衣服的女孩子？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 400)

    ChrTalk(    #111
        0xFE,
        "她应该是在那……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #112
        0xFE,
        "哇～？ 不见了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xF6, 400)

    ChrTalk(    #113
        0xFE,
        (
            "不过刚才确实在的，\x01",
            "应该还没走远。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D13")

    Jump("loc_1D8B")

    label("loc_1D16")


    ChrTalk(    #114
        0xFE,
        (
            "哇～钱也没了，\x01",
            "得回卢安了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "不过我在这儿找到了\x01",
            "男人的新浪漫——考古学……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "感觉就这样回去\x01",
            "有点浪费了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_21A8")

    label("loc_1D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1C")

    ChrTalk(    #117
        0xFE,
        "哇～这儿真了不起！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "想不到古代还有这种东西……\x01",
            "完全可以称为人类的宝藏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "……莫非考古学是更\x01",
            "胜于寻宝的男人的浪漫？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1E7F")

    ChrTalk(    #120
        0xFE,
        "那东西我已经交给馆长了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "他们在研究是不是能由资料馆收藏，\x01",
            "我在一边参观一边等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A8")

    label("loc_1E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_21A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_205A")

    ChrTalk(    #122
        0xFE,
        (
            "历史资料馆……\x01",
            "嗯，应该就是这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1000F咦？这不是吉米先生吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "啊？　对了，你是\x01",
            "在蔡斯救过我的游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1000F你在这里干什么啊？\x02\x03",

            "哦，对了……你是来\x01",
            "那个古代遗物的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "是啊，就算失去了力量，不过\x01",
            "还是不知道这东西会引起什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "我打算放在这里委托他们调查。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1000F是吗，很好很好。\x02\x03",

            "如果你能顺便放弃寻宝而\x01",
            "认真工作的话就更了不起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "哇，你嘴好厉害……\x01",
            "不过那是没的商量的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "除非我能找到比\x01",
            "寻宝更浪漫的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2159")

    label("loc_205A")


    ChrTalk(    #131
        0xFE,
        (
            "历史资料馆……\x01",
            "嗯，应该没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "这里一定能保管\x01",
            "东西应该会留下来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1000F古代遗物！？\x02\x03",

            "那如果是真东西的话\x01",
            "得送去七耀教会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "哇～是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "不过这已经\x01",
            "失去了力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "总之希望他们查一下，\x01",
            "调查，就过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1000F哦，原来如此……\x02",
    )

    CloseMessageWindow()

    label("loc_2159")

    OP_A2(0x1649)
    Jump("loc_21A8")

    label("loc_215F")


    ChrTalk(    #138
        0xFE,
        (
            "准备让他们帮我\x01",
            "调查失去了力量的古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "首先得去见负责人……\x02",
    )

    CloseMessageWindow()

    label("loc_21A8")

    TalkEnd(0xFE)
    Return()

    # Function_7_1AEE end

    def Function_8_21AC(): pass

    label("Function_8_21AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_220C")

    ChrTalk(    #140
        0xFE,
        (
            "#060F能发明接近这种原理的\x01",
            "东西的人真了不起。\x02\x03",

            "我也想有一天\x01",
            "能发明这样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D0")

    label("loc_220C")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #141
        0xFE,
        (
            "#560F啊，姐姐。\x02\x03",

            "#060F纺车虽然结构很简单，\x01",
            "不过却浓缩着很多发明在里面。\x02\x03",

            "能发明接近这种原理的\x01",
            "东西的人真了不起。\x02\x03",

            "#061F我也想有一天\x01",
            "能发明这样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1016F（又开始了啊……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_22D0")

    TalkEnd(0xFE)
    Return()

    # Function_8_21AC end

    def Function_9_22D4(): pass

    label("Function_9_22D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_231F")

    ChrTalk(    #143
        0xFE,
        (
            "#267F提妲一见到机器\x01",
            "就会立即忘乎所以。\x02\x03",

            "一直是这样的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2394")

    label("loc_231F")


    ChrTalk(    #144
        0xFE,
        (
            "#266F提妲一见到机器\x01",
            "就会立即忘乎所以。\x02\x03",

            "#267F一直是这样的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1016F对、对不起。\x01",
            "她可能一直是这样的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2394")

    TalkEnd(0xFE)
    Return()

    # Function_9_22D4 end

    def Function_10_2398(): pass

    label("Function_10_2398")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0xFE,
        (
            "女王陛下让这里\x01",
            "免费开放了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "小孩子也稍微\x01",
            "恢复了一些活力。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_2398 end

    def Function_11_23E5(): pass

    label("Function_11_23E5")

    TalkBegin(0xFE)

    ChrTalk(    #148
        0xFE,
        (
            "这东西就算没导力\x01",
            "也能使用吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_23E5 end

    def Function_12_240F(): pass

    label("Function_12_240F")

    TalkBegin(0xFE)

    ChrTalk(    #149
        0xFE,
        (
            "哈哈，这设计\x01",
            "真独特……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_240F end

    def Function_13_2433(): pass

    label("Function_13_2433")

    TalkBegin(0xFE)

    ChrTalk(    #150
        0xFE,
        (
            "哟，以前是用\x01",
            "这样的东西的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "如果导力就一直不恢复的话\x01",
            "就要回到使用这个的时代了吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2433 end

    def Function_14_249C(): pass

    label("Function_14_249C")

    TalkBegin(0xFE)

    ChrTalk(    #152
        0xFE,
        (
            "我是为了调节心情\x01",
            "才来的这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "希望一切都能\x01",
            "快点恢复原状……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_249C end

    def Function_15_24E9(): pass

    label("Function_15_24E9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2500")
    Call(0, 27)
    Call(0, 28)

    label("loc_2500")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    def lambda_2557():
        OP_6D(1000, 4000, -2000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2557)
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
            "#1015F#5P我记得你说昨天\x01",
            "也路过这里的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x107,
        (
            "#067F#1P嗯，只是眺望了\x01",
            "一下而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #156
        0x8,
        (
            "#3P欢迎。\x01",
            "您是游客吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2665():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2665)

    def lambda_267D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_267D)
    Sleep(100)

    def lambda_2690():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2690)
    Sleep(100)

    def lambda_26A3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_26A3)
    Sleep(100)

    def lambda_26B6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26B6)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #157
        0x101,
        (
            "#1016F#1P嗯，我们在\x01",
            "找人……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #158
        "\x07\x05向接待处的女性说明了玲的外貌特征。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #159
        0x8,
        (
            "啊，就是昨天\x01",
            "那边的这位小姐在一起的\x01",
            "穿白色礼服的小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x107,
        (
            "#560F#1P啊，应该是的\x01",
            "你还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "呵呵，因为两位小姐\x01",
            "很惹人注目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "很遗憾，今天\x01",
            "她没来过这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1015F#1P这样啊……\x01",
            "可能在别的地方。\x02\x03",

            "#1006F如果那孩子来了的话\x01",
            "能不能请你传口信\x01",
            "让她回协会？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        "好的，我明白了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_A2(0x162F)
    OP_28(0x8C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_15_24E9 end

    def Function_16_2869(): pass

    label("Function_16_2869")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2880")
    Call(0, 27)
    Call(0, 28)

    label("loc_2880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2935")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没看到『在历史资料馆听玲说话１』】\x01",      # 0
            "【◇已看到『在历史资料馆听玲说话１』】\x01",      # 1
            "【◇什么也没有变更】\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2929"),
        (1, "loc_292F"),
        (SWITCH_DEFAULT, "loc_2935"),
    )


    label("loc_2929")

    OP_A3(0x162F)
    Jump("loc_2935")

    label("loc_292F")

    OP_A2(0x162F)
    Jump("loc_2935")

    label("loc_2935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C43")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    def lambda_2994():
        OP_6D(1000, 4000, -2000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2994)
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
            "#1015F#5P我记得你说昨天\x01",
            "也路过这里的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x107,
        (
            "#067F#1P嗯，只是眺望了\x01",
            "一下而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #167
        0x8,
        (
            "#3P你好。\x01",
            "您是游客吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AA3():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AA3)

    def lambda_2ABB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ABB)
    Sleep(100)

    def lambda_2ACE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2ACE)
    Sleep(100)

    def lambda_2AE1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2AE1)
    Sleep(100)

    def lambda_2AF4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2AF4)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #168
        0x101,
        (
            "#1006F#1P嗯，我们在\x01",
            "找人……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #169
        "\x07\x05向接待处的女性说明了玲的外貌特征。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #170
        0x8,
        (
            "啊，就是昨天\x01",
            "那边的这位小姐在一起的\x01",
            "穿白色礼服的小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x107,
        (
            "#560F#1P啊，应该是的\x01",
            "你还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "呵呵，因为两位小姐\x01",
            "很惹人注目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "如果说的是那位小姐\x01",
            "刚才已经来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        (
            "我想她应该\x01",
            "还在馆内。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2C43")

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
        "啊，尊敬的顾客。\x02",
    )

    CloseMessageWindow()

    def lambda_2D05():
        OP_6D(2500, 0, -5250, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D05)

    def lambda_2D1D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D1D)
    Sleep(100)

    def lambda_2D30():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2D30)
    Sleep(100)

    def lambda_2D43():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2D43)
    Sleep(100)

    def lambda_2D56():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2D56)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #176
        0x8,
        (
            "那位小妹妹\x01",
            "来过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "我想她应该\x01",
            "还在馆内。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D97")


    ChrTalk(    #178
        0x101,
        "#1006F#1P哦，这样啊！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DDB")

    ChrTalk(    #179
        0x106,
        (
            "#051F#6P好。\x01",
            "赶紧抓住她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFC")

    label("loc_2DDB")


    ChrTalk(    #180
        0x103,
        (
            "#021F#6P呵呵，终于\x01",
            "逮到了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFC")

    OP_4B(0x8, 255)
    OP_A2(0x1630)
    OP_28(0x8C, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_16_2869 end

    def Function_17_2E0C(): pass

    label("Function_17_2E0C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_2E33():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E33)
    OP_8E(0xFE, 0x15E, 0x0, 0xFFFFEC46, 0x7D0, 0x0)
    Return()

    # Function_17_2E0C end

    def Function_18_2E54(): pass

    label("Function_18_2E54")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_2E7B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E7B)
    OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFEBEC, 0x7D0, 0x0)
    Return()

    # Function_18_2E54 end

    def Function_19_2E9C(): pass

    label("Function_19_2E9C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_2EC3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EC3)
    OP_8E(0xFE, 0xE6, 0x0, 0xFFFFE660, 0x7D0, 0x0)
    Return()

    # Function_19_2E9C end

    def Function_20_2EE4(): pass

    label("Function_20_2EE4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -250, -9500, 0)

    def lambda_2F0B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F0B)
    OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFE660, 0x7D0, 0x0)
    Return()

    # Function_20_2EE4 end

    def Function_21_2F2C(): pass

    label("Function_21_2F2C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F43")
    Call(0, 27)
    Call(0, 28)

    label("loc_2F43")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0x8, 255)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_2F6B"),
        (104, "loc_2FAB"),
        (SWITCH_DEFAULT, "loc_2FEB"),
    )


    label("loc_2F6B")

    OP_6D(-5980, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_2FEB")

    label("loc_2FAB")

    OP_6D(5990, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_2FEB")

    label("loc_2FEB")

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
        (103, "loc_304B"),
        (104, "loc_305A"),
        (SWITCH_DEFAULT, "loc_305D"),
    )


    label("loc_304B")

    TurnDirection(0x101, 0x11, 400)
    Sleep(500)
    Jump("loc_305D")

    label("loc_305A")

    Jump("loc_305D")

    label("loc_305D")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #181
        0x101,
        "#1004F#6P咦？\x02",
    )

    CloseMessageWindow()
    OP_6D(2500, 0, -5250, 2000)

    ChrTalk(    #182
        0x11,
        (
            "#1306F#6P我说，姐姐。\x02\x03",

            "你知道哪儿有\x01",
            "没有颜色的鱼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x11,
        "#263F#6P呵呵，再见。\x02",
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x1A)
    Sleep(500)

    def lambda_310F():

        label("loc_310F")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_310F")

    QueueWorkItem2(0x8, 1, lambda_310F)

    ChrTalk(    #185 op#5
        0x8,
        "啊……\x05\x02",
    )

    Sleep(2000)

    ChrTalk(    #186
        0x8,
        (
            "#5P喂，小妹妹！\x01",
            "有你认识的人……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -840, 1270, 3460, 0)
    SetChrPos(0x107, 230, 1270, 3460, 0)
    SetChrPos(0xF7, -680, 1270, 3460, 0)
    SetChrPos(0xF9, 350, 1270, 3460, 0)

    def lambda_31A5():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFEB7E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31A5)
    Sleep(100)

    def lambda_31C5():
        OP_8E(0xFE, 0xE6, 0x0, 0xFFFFEA48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_31C5)
    Sleep(500)

    def lambda_31E5():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0xFFFFF02E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_31E5)
    Sleep(100)

    def lambda_3205():
        OP_8E(0xFE, 0x15E, 0x0, 0xFFFFF02E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3205)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #187
        0x101,
        "#1020F#5P等、等等，玲！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        "#065F#5P小玲，等等！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)

    def lambda_3266():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3266)
    Sleep(300)

    def lambda_3286():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3286)
    Sleep(300)

    def lambda_32A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32A6)

    def lambda_32B8():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_32B8)
    Sleep(300)

    def lambda_32D8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_32D8)

    def lambda_32EA():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_32EA)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4101   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2F2C end

    def Function_22_330D(): pass

    label("Function_22_330D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_332D"),
        (104, "loc_3341"),
        (SWITCH_DEFAULT, "loc_3355"),
    )


    label("loc_332D")

    SetChrPos(0xFE, -5150, 6550, 10500, 180)
    Jump("loc_3355")

    label("loc_3341")

    SetChrPos(0xFE, 5340, 6550, 10500, 180)
    Jump("loc_3355")

    label("loc_3355")


    def lambda_335B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_335B)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    Return()

    # Function_22_330D end

    def Function_23_337C(): pass

    label("Function_23_337C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_339C"),
        (104, "loc_33B0"),
        (SWITCH_DEFAULT, "loc_33C4"),
    )


    label("loc_339C")

    SetChrPos(0xFE, -6400, 6540, 10480, 180)
    Jump("loc_33C4")

    label("loc_33B0")

    SetChrPos(0xFE, 6600, 6550, 10500, 180)
    Jump("loc_33C4")

    label("loc_33C4")


    def lambda_33CA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33CA)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
    Return()

    # Function_23_337C end

    def Function_24_33EB(): pass

    label("Function_24_33EB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_340B"),
        (104, "loc_341F"),
        (SWITCH_DEFAULT, "loc_3433"),
    )


    label("loc_340B")

    SetChrPos(0xFE, -5150, 6550, 10500, 180)
    Jump("loc_3433")

    label("loc_341F")

    SetChrPos(0xFE, 5340, 6550, 10500, 180)
    Jump("loc_3433")

    label("loc_3433")


    def lambda_3439():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3439)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
    Return()

    # Function_24_33EB end

    def Function_25_345A(): pass

    label("Function_25_345A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_347A"),
        (104, "loc_348E"),
        (SWITCH_DEFAULT, "loc_34A2"),
    )


    label("loc_347A")

    SetChrPos(0xFE, -6400, 6540, 10480, 180)
    Jump("loc_34A2")

    label("loc_348E")

    SetChrPos(0xFE, 6600, 6550, 10500, 180)
    Jump("loc_34A2")

    label("loc_34A2")


    def lambda_34A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34A8)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
    Return()

    # Function_25_345A end

    def Function_26_34C9(): pass

    label("Function_26_34C9")

    OP_8C(0xFE, 225, 400)
    OP_8E(0xFE, 0x0, 0x0, 0xFFFFE2B4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0xFFFFDF3A, 0x7D0, 0x0)

    def lambda_34FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34FE)
    OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFDAE4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_34C9 end

    def Function_27_3524(): pass

    label("Function_27_3524")

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
        (0, "loc_35A1"),
        (1, "loc_35A7"),
        (SWITCH_DEFAULT, "loc_35AD"),
    )


    label("loc_35A1")

    OP_A2(0x1200)
    Jump("loc_35AD")

    label("loc_35A7")

    OP_A2(0x1201)
    Jump("loc_35AD")

    label("loc_35AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_35BB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_35BF")

    label("loc_35BB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_35BF")

    Return()

    # Function_27_3524 end

    def Function_28_35C0(): pass

    label("Function_28_35C0")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_35FF")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_3619")

    label("loc_35FF")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_3619")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_28_35C0 end

    def Function_29_3639(): pass

    label("Function_29_3639")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #189
        (
            "\x07\x05【『四轮之塔』的外壁】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　这块朴素的石壁，是从『大崩坏』后所建\x01",
            "的『四轮之塔』上作为研究资料切割出来的。\x01",
            "其上所绘制的纹样是同时代建筑物中的典型，\x01",
            "据说描述的是持杖的祭司，以及展翅的神祗的\x01",
            "身姿。关于其与七耀教会成立之后的代表神格\x01",
            "『空之女神』的关系，各方面的研究仍在进行\x01",
            "中。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_29_3639 end

    def Function_30_37AB(): pass

    label("Function_30_37AB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #190
        (
            "\x07\x05【七耀历１１５０～１２００年\x01",
            "　　　　　　　～导力革命以后的世界～】\x01",
            "　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\x01",
            "十年。世界以惊人的速度进步着，接连不断地\x01",
            "开拓岀导力技术新的应用领域。堪称其象征的\x01",
            "就是飞船。\x01",
            "　　\x01",
            "　　利贝尔王国定期飞船的运航已经成为国民\x01",
            "们习以为常的交通方式，近年来埃雷波尼亚帝\x01",
            "国等其他国家也开始正式引进飞船制造业，使\x01",
            "得飞船级的船体逐步实用化。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_37AB end

    def Function_31_3947(): pass

    label("Function_31_3947")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        (
            "\x07\x05【七耀历以前\x01",
            "　　　　　～古代塞姆里亚文明～】\x01",
            "　　距今约１２００年前，当时繁荣绝顶的塞\x01",
            "姆里亚文明突然迎来了终结，失去了文明的人\x01",
            "们开始度过漫长的暗黑时代。\x01",
            "　　\x01",
            "　　第一层的展示物据考证是『大崩坏』之后\x01",
            "所制造的遗物。虽然据判断并非古代文明的直\x01",
            "接遗物，但因受到其深刻影响，学术方面的价\x01",
            "值极高。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_31_3947 end

    def Function_32_3AA2(): pass

    label("Function_32_3AA2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #192
        (
            "\x07\x05【古代的照明器具】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　专用于焚烧篝火的容器。在塔之类被认为\x01",
            "与祭祀仪式有关联的建筑物中频繁被使用，其\x01",
            "具体用途不仅仅是照明，在宗教上可能也拥有\x01",
            "某种程度的意义。当然这点目前还只是推测罢\x01",
            "了。  \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_3AA2 end

    def Function_33_3BBB(): pass

    label("Function_33_3BBB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #193
        (
            "\x07\x05【浮雕石柱】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\x01",
            "底被打捞上来，可以看出与『四轮之塔』的壁\x01",
            "画类似的纹样在其上也被反复使用。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_33_3BBB end

    def Function_34_3C9B(): pass

    label("Function_34_3C9B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #194
        (
            "\x07\x05【瓷工艺的地板】\x01",
            "　　　　　　　　　　　年代：七耀历以前？\x01",
            "　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\x01",
            "的天然石块巧妙拼接，作出朴素而美妙的花纹\x01",
            "样式。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_3C9B end

    def Function_35_3D65(): pass

    label("Function_35_3D65")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #195
        (
            "\x07\x05【七耀历１～５００年左右\x01",
            "　　　　　　　　～暗黑时代的到来～】\x01",
            "　　由于『大崩坏』而导致文明尽失，世界陷\x01",
            "入了长期的混乱时代。\x01",
            "　　大小各异的国家、势力使得无尽的战争持\x01",
            "续了约５００年间，后世称此时代为『暗黑时\x01",
            "代』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_3D65 end

    def Function_36_3E6C(): pass

    label("Function_36_3E6C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #196
        (
            "\x07\x05【骑士们的武具】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　日夜征战的时代中，战士们的集团拥有社\x01",
            "会性的强大影响力，最终成长为特权的骑士阶\x01",
            "级。\x01",
            "　　他们佩戴着如展品所示的武具投身沙场，\x01",
            "获得战利品和领土，势力不断扩大。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_3E6C end

    def Function_37_3F7E(): pass

    label("Function_37_3F7E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #197
        (
            "\x07\x05【七耀历５００～１１００年左右\x01",
            "　　　　　　～七耀教会带来的安定期～】\x01",
            "　　七耀教会登上历史舞台，正值暗黑时代末\x01",
            "期，七耀历５００年左右。\x01",
            "　　以『空之女神』为中心所整理的教义，通\x01",
            "过教会救济民众的社会活动，瞬间深入人心。\x01",
            "　　它的权威很快成长到连贵族、骑士阶级也\x01",
            "无法忽视的地步，其后以教会为中心的新秩序\x01",
            "便逐步形成了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_37_3F7E end

    def Function_38_40EE(): pass

    label("Function_38_40EE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #198
        (
            "\x07\x05【古代文明的遗物——\x01",
            "　　　　　　　　『古代遗产』】\x01",
            "　　　　　　　　　　　　　　　年代：不明\x01",
            "　　『古代遗产』是从各地发现的古代遗迹中\x01",
            "出土的诸如器物、杖等形态各异、不可思议的\x01",
            "遗物。\x01",
            "　　在七耀教会的教义中，作为与女神赐予的\x01",
            "『七至宝』相关的物品，其回收成为教会必须\x01",
            "履行的义务之一。展品的『古代遗产』也是教\x01",
            "会所回收的物品。\x01",
            "　　许多传闻称其拥有超常的力量，但此展品\x01",
            "已经失去能力，无法启动。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_40EE end

    def Function_39_42A9(): pass

    label("Function_39_42A9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #199
        (
            "\x07\x05【七耀教会的祭具】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　七耀教会创造岀种种的宗教艺术，由此开\x01",
            "始教会开拓出一个稳定的时代。据考证，『空\x01",
            "之女神』的圣像也是由此时起被塑造为现今的\x01",
            "姿态。此外，现在所使用的祭祀道具多数也是\x01",
            "在这个时代被定型的。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_42A9 end

    def Function_40_43D5(): pass

    label("Function_40_43D5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #200
        (
            "\x07\x05【七耀教会圣典的抄本】\x01",
            "　　　　　　　　年代：七耀历５００年左右\x01",
            "　　暗黑时代末期的原始七耀教会所使用的圣\x01",
            "典抄本。中世纪没有印刷技术，因此这本书是\x01",
            "由人手工抄写在兽皮制的纸张上的。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_43D5 end

    def Function_41_44BF(): pass

    label("Function_41_44BF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #201
        (
            "\x07\x05【中世纪的纺纱机】\x01",
            "　　　　　　　　年代：七耀历９００年左右\x01",
            "　　纺纱用的手工机械。到了稳定的中世纪，\x01",
            "农民的生活逐渐富裕，作为商品作物的棉花栽\x01",
            "培日渐繁盛。为了收入货币，这个时代的手工\x01",
            "业也开始发展。\x01",
            "　　C37259\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_44BF end

    SaveToFile()

Try(main)
