from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0710   ._SN',
        MapName             = 'Event',
        Location            = 'E0710.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '朵洛希',                               # 9
        '奥托尔船长',                           # 10
        '乘务员托托',                           # 11
        '乘务员达罗',                           # 12
        '乘客',                                 # 13
        '乘客',                                 # 14
        '乘客',                                 # 15
        '乘客',                                 # 16
        '乘客',                                 # 17
        '乘客',                                 # 18
        '乘客',                                 # 19
        '小孩',                                 # 20
        '米拉诺',                               # 21
        '西蒙',                                 # 22
        '乘客',                                 # 23
        '乘务员撒里拿',                         # 24
        '乘客',                                 # 25
        '乘客',                                 # 26
        '乘客',                                 # 27
        '伊米尔',                               # 28
        '朵洛希',                               # 29
        '',                                     # 30
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH01443 ._CH',             # 01
        'ED6_DT07/CH01290 ._CH',             # 02
        'ED6_DT07/CH01293 ._CH',             # 03
        'ED6_DT07/CH01003 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01143 ._CH',             # 06
        'ED6_DT07/CH01430 ._CH',             # 07
        'ED6_DT07/CH01463 ._CH',             # 08
        'ED6_DT07/CH01213 ._CH',             # 09
        'ED6_DT07/CH01033 ._CH',             # 0A
        'ED6_DT07/CH01070 ._CH',             # 0B
        'ED6_DT07/CH01540 ._CH',             # 0C
        'ED6_DT07/CH01233 ._CH',             # 0D
        'ED6_DT07/CH01140 ._CH',             # 0E
        'ED6_DT07/CH01153 ._CH',             # 0F
        'ED6_DT07/CH01050 ._CH',             # 10
        'ED6_DT07/CH01450 ._CH',             # 11
        'ED6_DT06/CH20063 ._CH',             # 12
        'ED6_DT07/CH01120 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH01443P._CP',             # 01
        'ED6_DT07/CH01290P._CP',             # 02
        'ED6_DT07/CH01293P._CP',             # 03
        'ED6_DT07/CH01003P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01143P._CP',             # 06
        'ED6_DT07/CH01430P._CP',             # 07
        'ED6_DT07/CH01463P._CP',             # 08
        'ED6_DT07/CH01213P._CP',             # 09
        'ED6_DT07/CH01033P._CP',             # 0A
        'ED6_DT07/CH01070P._CP',             # 0B
        'ED6_DT07/CH01540P._CP',             # 0C
        'ED6_DT07/CH01233P._CP',             # 0D
        'ED6_DT07/CH01140P._CP',             # 0E
        'ED6_DT07/CH01153P._CP',             # 0F
        'ED6_DT07/CH01050P._CP',             # 10
        'ED6_DT07/CH01450P._CP',             # 11
        'ED6_DT06/CH20063P._CP',             # 12
        'ED6_DT07/CH01120P._CP',             # 13
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59020,
        Z                   = -600,
        Y                   = 49310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65537,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 60800,
        Z                   = -2000,
        Y                   = 53360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 59190,
        Z                   = -1950,
        Y                   = 54200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 116700,
        Z                   = 100,
        Y                   = 5260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 114220,
        Z                   = 100,
        Y                   = -1580,
        Direction           = 134,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 115460,
        Z                   = 100,
        Y                   = -2460,
        Direction           = 11,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 116610,
        Z                   = 0,
        Y                   = 10650,
        Direction           = 44,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 117450,
        Z                   = 100,
        Y                   = 3240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 89250,
        Z                   = 100,
        Y                   = -4890,
        Direction           = 351,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 85400,
        Z                   = 100,
        Y                   = -4820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 86390,
        Z                   = 0,
        Y                   = -3790,
        Direction           = 219,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 88880,
        Z                   = 100,
        Y                   = -1240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 87830,
        Z                   = 0,
        Y                   = 170,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 89500,
        Z                   = 0,
        Y                   = 9180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 86690,
        Z                   = 0,
        Y                   = 47770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 91250,
        Z                   = 0,
        Y                   = 48900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 91360,
        Z                   = 100,
        Y                   = 47150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 57350,
        Z                   = 0,
        Y                   = -1850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 31490,
        Z                   = 0,
        Y                   = -7680,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 59790,
        Z                   = -460,
        Y                   = 47840,
        Direction           = 331,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_3EA",          # 00, 0
        "Function_1_5C2",          # 01, 1
        "Function_2_5C8",          # 02, 2
        "Function_3_745",          # 03, 3
        "Function_4_8D3",          # 04, 4
        "Function_5_A0B",          # 05, 5
        "Function_6_A43",          # 06, 6
        "Function_7_ACC",          # 07, 7
        "Function_8_BE6",          # 08, 8
        "Function_9_CA0",          # 09, 9
        "Function_10_D95",         # 0A, 10
        "Function_11_EBD",         # 0B, 11
        "Function_12_F8C",         # 0C, 12
        "Function_13_106B",        # 0D, 13
        "Function_14_1113",        # 0E, 14
        "Function_15_11AD",        # 0F, 15
        "Function_16_1252",        # 10, 16
        "Function_17_1359",        # 11, 17
        "Function_18_1474",        # 12, 18
        "Function_19_1549",        # 13, 19
        "Function_20_1664",        # 14, 20
        "Function_21_177F",        # 15, 21
        "Function_22_1882",        # 16, 22
        "Function_23_1982",        # 17, 23
        "Function_24_2415",        # 18, 24
        "Function_25_2498",        # 19, 25
    )


    def Function_0_3EA(): pass

    label("Function_0_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3FD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_3FD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_42D"),
        (102, "loc_42D"),
        (103, "loc_42D"),
        (104, "loc_42D"),
        (105, "loc_42D"),
        (106, "loc_42D"),
        (107, "loc_42D"),
        (109, "loc_42D"),
        (110, "loc_42D"),
        (115, "loc_42D"),
        (SWITCH_DEFAULT, "loc_5C1"),
    )


    label("loc_42D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 3)), scpexpr(EXPR_END)), "loc_448")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 4)), scpexpr(EXPR_END)), "loc_459")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 5)), scpexpr(EXPR_END)), "loc_46A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 2)), scpexpr(EXPR_END)), "loc_47B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 3)), scpexpr(EXPR_END)), "loc_48C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 4)), scpexpr(EXPR_END)), "loc_49D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 5)), scpexpr(EXPR_END)), "loc_4AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 6)), scpexpr(EXPR_END)), "loc_4BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 7)), scpexpr(EXPR_END)), "loc_4D0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 0)), scpexpr(EXPR_END)), "loc_4E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 1)), scpexpr(EXPR_END)), "loc_4F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 2)), scpexpr(EXPR_END)), "loc_503")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 3)), scpexpr(EXPR_END)), "loc_514")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 4)), scpexpr(EXPR_END)), "loc_525")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 5)), scpexpr(EXPR_END)), "loc_536")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 6)), scpexpr(EXPR_END)), "loc_547")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B6, 7)), scpexpr(EXPR_END)), "loc_558")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B7, 0)), scpexpr(EXPR_END)), "loc_569")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B7, 1)), scpexpr(EXPR_END)), "loc_57A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B7, 2)), scpexpr(EXPR_END)), "loc_58B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B7, 3)), scpexpr(EXPR_END)), "loc_59C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B7, 4)), scpexpr(EXPR_END)), "loc_5AD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    Event(0, 25)

    label("loc_5BE")

    Jump("loc_5C1")

    label("loc_5C1")

    Return()

    # Function_0_3EA end

    def Function_1_5C2(): pass

    label("Function_1_5C2")

    OP_22(0x7A, 0x1, 0x46)
    Return()

    # Function_1_5C2 end

    def Function_2_5C8(): pass

    label("Function_2_5C8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ED")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_72F")

    label("loc_5ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_72F")

    label("loc_606")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_72F")

    label("loc_61F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_638")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_72F")

    label("loc_638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_72F")

    label("loc_651")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_72F")

    label("loc_66A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_72F")

    label("loc_683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_72F")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_72F")

    label("loc_6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_72F")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_72F")

    label("loc_6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_72F")

    label("loc_700")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_719")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_72F")

    label("loc_719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_72F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_744")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_72F")

    label("loc_744")

    Return()

    # Function_2_5C8 end

    def Function_3_745(): pass

    label("Function_3_745")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7D0")

    ChrTalk(    #0
        0xFE,
        "真、真是纠缠不清的小姑娘呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "（难、难道让我\x01",
            "　这么一个作风硬派的人\x01",
            "　说出曾经想成为蛋糕师傅吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CF")

    label("loc_7D0")


    ChrTalk(    #2
        0x11,
        (
            "哎？就算让我告诉你\x01",
            "我小时候的梦想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "那、那样的事情\x01",
            "一般是不好对别人说的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x24,
        (
            "#153F……啊，又被搪塞过去了～！\x02\x03",

            "#155F我是在取材呢，\x01",
            "请认真地回答我嘛～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1066F（好像在行使\x01",
            "　记者的特权啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_A2(0x25F3)

    label("loc_8CF")

    TalkEnd(0xFE)
    Return()

    # Function_3_745 end

    def Function_4_8D3(): pass

    label("Function_4_8D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_95A")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #6
        0xFE,
        (
            "贝根连峰是在利贝尔\x01",
            "和卡尔瓦德的国境边界上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "越过那座山之后，\x01",
            "格兰赛尔就近在眼前了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_A07")

    label("loc_95A")


    ChrTalk(    #8
        0x12,
        "马上就到贝根连峰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        "附近气流很乱，请多加注意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x13,
        "知道啦～\x02",
    )

    Jump("loc_9C2")

    label("loc_9C2")

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        (
            "你以为我是谁啊。\x01",
            "我已经在这条航路上掌舵三年了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_A2(0x25AA)

    label("loc_A07")

    TalkEnd(0xFE)
    Return()

    # Function_4_8D3 end

    def Function_5_A0B(): pass

    label("Function_5_A0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_A3B")

    ChrTalk(    #12
        0xFE,
        "……前进方向是西北西！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3F")

    label("loc_A3B")

    Call(0, 4)

    label("loc_A3F")

    TalkEnd(0xFE)
    Return()

    # Function_5_A0B end

    def Function_6_A43(): pass

    label("Function_6_A43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_AC4")

    ChrTalk(    #13
        0xFE,
        (
            "#151F顺便说一下，\x01",
            "我的梦想是成为一名怪盗，哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1068F（绝对是受到了哪本小说的影响吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC8")

    label("loc_AC4")

    Call(0, 3)

    label("loc_AC8")

    TalkEnd(0xFE)
    Return()

    # Function_6_A43 end

    def Function_7_ACC(): pass

    label("Function_7_ACC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B55")

    ChrTalk(    #15
        0xFE,
        (
            "据说即使在缔结了互不侵犯条约之后，\x01",
            "也偶尔会有一些事件发生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "那家伙虽然说自己没有受过伤，\x01",
            "但我还是感到担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE2")

    label("loc_B55")


    ChrTalk(    #17
        0xFE,
        (
            "我要去看望一下\x01",
            "住在格兰赛尔的孙子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "唔，算来算去\x01",
            "已经三年没见了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "听说好像发生了很多事情，\x01",
            "我可是提心吊胆呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x25AB)

    label("loc_BE2")

    TalkEnd(0xFE)
    Return()

    # Function_7_ACC end

    def Function_8_BE6(): pass

    label("Function_8_BE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(    #20
        0xFE,
        (
            "我知道你是以\x01",
            "成为工程师为目标的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "但是，\x01",
            "是不是时常放松一下比较好呢？\x02",
        )
    )

    Jump("loc_C4C")

    label("loc_C4C")

    CloseMessageWindow()
    Jump("loc_C9C")

    label("loc_C50")


    ChrTalk(    #22
        0xFE,
        "喂喂，你可别太勉强自己了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "你一向都是这么容易冲动……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x25AC)

    label("loc_C9C")

    TalkEnd(0xFE)
    Return()

    # Function_8_BE6 end

    def Function_9_CA0(): pass

    label("Function_9_CA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D11")

    ChrTalk(    #24
        0xFE,
        (
            "我去参加乌尔努社应聘考试，\x01",
            "在面试那一轮就遭到淘汰了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "这、这次绝对\x01",
            "要干出一番事业！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D91")

    label("loc_D11")


    ChrTalk(    #26
        0xFE,
        (
            "首、首先是去走访\x01",
            "蔡斯市的中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "这是学习最前沿的导力技术的\x01",
            "独一无二的机会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "绝、绝对不能错过！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x25F4)

    label("loc_D91")

    TalkEnd(0xFE)
    Return()

    # Function_9_CA0 end

    def Function_10_D95(): pass

    label("Function_10_D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(    #29
        0xFE,
        (
            "连续乘坐火车和飞船，\x01",
            "这已经是第三天了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "终于要到了呢～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB9")

    label("loc_DEB")


    ChrTalk(    #31
        0xFE,
        (
            "最后目击到古代龙的地点——\x01",
            "利贝尔。\x02",
        )
    )

    Jump("loc_E21")

    label("loc_E21")

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "呼呼，终于来到了这片地方。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "现在还没有后续的目击情报，\x01",
            "手头的线索只有这里了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "好，等到了以后，\x01",
            "先去向琉肯先生\x01",
            "打听一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x25AD)

    label("loc_EB9")

    TalkEnd(0xFE)
    Return()

    # Function_10_D95 end

    def Function_11_EBD(): pass

    label("Function_11_EBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(    #35
        0xFE,
        (
            "定期船的客席\x01",
            "总是被打扫得干干净净呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "呵呵，我在使用的时候\x01",
            "也不舍得把它弄脏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F88")

    label("loc_F28")


    ChrTalk(    #37
        0xFE,
        (
            "呵呵，定期船的客席\x01",
            "总是被打扫得干干净净呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "嗯，服务业\x01",
            "就应该做到这种程度。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x25AE)

    label("loc_F88")

    TalkEnd(0xFE)
    Return()

    # Function_11_EBD end

    def Function_12_F8C(): pass

    label("Function_12_F8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FEC")

    ChrTalk(    #39
        0xFE,
        (
            "我以前曾经在\x01",
            "特迪斯海的波涛中劈波斩浪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "这也是时代演进的表现啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_FEC")


    ChrTalk(    #41
        0xFE,
        (
            "我以前是个水手。\x01",
            "现在则和大家一样乘坐飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "这家伙比船要快得多，\x01",
            "而且又不像导力巴士那样\x01",
            "颠得人屁股疼。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_A2(0x25AF)

    label("loc_1067")

    TalkEnd(0xFE)
    Return()

    # Function_12_F8C end

    def Function_13_106B(): pass

    label("Function_13_106B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(    #43
        0xFE,
        (
            "这个孩子，\x01",
            "真是安静不下来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "为什么不能老实点呢！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_110F")

    label("loc_10BD")


    ChrTalk(    #45
        0xFE,
        (
            "啊啊，真是的……\x01",
            "给我老实坐好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "马上就要到了，\x01",
            "别再胡闹了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x25B0)

    label("loc_110F")

    TalkEnd(0xFE)
    Return()

    # Function_13_106B end

    def Function_14_1113(): pass

    label("Function_14_1113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1169")

    ChrTalk(    #47
        0xFE,
        (
            "不要啦～\x01",
            "我都已经坐烦了。\x02",
        )
    )

    Jump("loc_1149")

    label("loc_1149")

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "妈妈～这样就好了吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11A9")

    label("loc_1169")


    ChrTalk(    #49
        0xFE,
        "妈妈，我可以看外面吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "你听见了吗，妈妈～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x25B1)

    label("loc_11A9")

    TalkEnd(0xFE)
    Return()

    # Function_14_1113 end

    def Function_15_11AD(): pass

    label("Function_15_11AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_11FC")

    ChrTalk(    #51
        0xFE,
        (
            "唉，\x01",
            "真是固执啊……\x02",
        )
    )

    Jump("loc_11D7")

    label("loc_11D7")

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "至少也听一下\x01",
            "我的愿望嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124E")

    label("loc_11FC")


    ChrTalk(    #53
        0xFE,
        (
            "妹妹那家伙，\x01",
            "真是固执啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "难得的观光旅行，\x01",
            "就这样给糟蹋了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x25B2)

    label("loc_124E")

    TalkEnd(0xFE)
    Return()

    # Function_15_11AD end

    def Function_16_1252(): pass

    label("Function_16_1252")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_12B9")

    ChrTalk(    #55
        0xFE,
        (
            "哥哥总是自己一个人\x01",
            "随便做决定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "一点也不考虑我的感受。\x01",
            "……真是让人生气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1355")

    label("loc_12B9")


    ChrTalk(    #57
        0xFE,
        "不，我绝对不会让步的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "参观了格兰赛尔城之后，\x01",
            "我要去艾尔贝离宫看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "竟然说要参观钓鱼场什么的……\x01",
            "哥哥，你到底在说什么胡话啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x25B3)

    label("loc_1355")

    TalkEnd(0xFE)
    Return()

    # Function_16_1252 end

    def Function_17_1359(): pass

    label("Function_17_1359")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_13EA")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #60
        0xFE,
        (
            "哎呀～\x01",
            "那个老头太烦人了～……\x02",
        )
    )

    Jump("loc_1397")

    label("loc_1397")

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "我已经１６岁了不是吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "想去哪里，要做什么，\x01",
            "那是我的自由吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1470")

    label("loc_13EA")


    ChrTalk(    #63
        0xFE,
        "唉～怎么觉得这么累啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "再说了，\x01",
            "为什么我非要这么大老远的\x01",
            "跑来见那个老头不可呢？\x02",
        )
    )

    Jump("loc_1453")

    label("loc_1453")

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "真是难以接受。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_A2(0x25B4)

    label("loc_1470")

    TalkEnd(0xFE)
    Return()

    # Function_17_1359 end

    def Function_18_1474(): pass

    label("Function_18_1474")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_14E9")

    ChrTalk(    #66
        0xFE,
        (
            "啊啊，\x01",
            "不过说老实话，\x01",
            "也有想偷看一下的心情呢。\x02",
        )
    )

    Jump("loc_14BC")

    label("loc_14BC")

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "又想看，\x01",
            "又不想看……\x02",
        )
    )

    Jump("loc_14E5")

    label("loc_14E5")

    CloseMessageWindow()
    Jump("loc_1545")

    label("loc_14E9")


    ChrTalk(    #68
        0xFE,
        (
            "我、我对高的地方\x01",
            "最没办法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "不，倒不至于像\x01",
            "所谓的恐高症那么厉害……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    OP_A2(0x25B5)

    label("loc_1545")

    TalkEnd(0xFE)
    Return()

    # Function_18_1474 end

    def Function_19_1549(): pass

    label("Function_19_1549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(    #70
        0xFE,
        (
            "马上就到终点站\x01",
            "利贝尔王国的首都格兰赛尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "现在请再一次确认\x01",
            "您是否有遗忘的随身物品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1660")

    label("loc_15C4")


    ChrTalk(    #72
        0xFE,
        (
            "这位乘客，\x01",
            "您听到广播了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "马上就到终点站\x01",
            "利贝尔王国的首都格兰赛尔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "现在请再一次确认\x01",
            "您是否有遗忘的随身物品。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    OP_A2(0x25B6)

    label("loc_1660")

    TalkEnd(0xFE)
    Return()

    # Function_19_1549 end

    def Function_20_1664(): pass

    label("Function_20_1664")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_16D5")

    ChrTalk(    #75
        0xFE,
        (
            "别看那个交涉人很年轻，\x01",
            "但还真是难缠……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "嗯～\x01",
            "下次到底能不能搞定呢……\x02",
        )
    )

    Jump("loc_16D1")

    label("loc_16D1")

    CloseMessageWindow()
    Jump("loc_177B")

    label("loc_16D5")


    ChrTalk(    #77
        0xFE,
        (
            "别看那个交涉人很年轻，\x01",
            "但还真是难缠……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "这样也好，反正我这边\x01",
            "也找了优秀的情报专家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "下一次一定要谈到六四……\x01",
            "不，七三分成！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x25B7)

    label("loc_177B")

    TalkEnd(0xFE)
    Return()

    # Function_20_1664 end

    def Function_21_177F(): pass

    label("Function_21_177F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_17F6")

    ChrTalk(    #80
        0xFE,
        (
            "可、可是直到最后\x01",
            "米拉诺小姐不也坚持住了要求吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "还、还没有到\x01",
            "必输无疑的地步吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187E")

    label("loc_17F6")


    ChrTalk(    #82
        0xFE,
        "唉，真是了不起的谈判啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "竟然能和\x01",
            "米拉诺小姐力争到底……\x02",
        )
    )

    Jump("loc_1854")

    label("loc_1854")

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "世、世界真是广阔呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x25B8)

    label("loc_187E")

    TalkEnd(0xFE)
    Return()

    # Function_21_177F end

    def Function_22_1882(): pass

    label("Function_22_1882")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1902")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #85
        0xFE,
        (
            "客人，\x01",
            "这里是不可以进去的。\x02",
        )
    )

    Jump("loc_18C3")

    label("loc_18C3")

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "万一被什么东西刮到，\x01",
            "就有可能会受伤呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_197E")

    label("loc_1902")


    ChrTalk(    #87
        0xFE,
        "嗯，导力压没有异常。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #88
        0xFE,
        (
            "啊，这位客人。\x01",
            "请不要进入这个地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    OP_A2(0xF)
    OP_A2(0x25F5)

    label("loc_197E")

    TalkEnd(0xFE)
    Return()

    # Function_22_1882 end

    def Function_23_1982(): pass

    label("Function_23_1982")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 87790, -1000, 52910, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 89250, -1000, 52840, 270)
    OP_6D(88990, 0, 47310, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(27000, 0)
    OP_6E(317, 0)

    def lambda_19F8():
        OP_6D(89180, -1000, 54020, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19F8)

    def lambda_1A10():
        OP_67(0, 6430, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A10)

    def lambda_1A28():
        OP_6C(27000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A28)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #89
        0x10,
        (
            "#150F#2P哈～原来如此～\x02\x03",

            "凯文先生是为了\x01",
            "继续调查那件事，\x01",
            "才又来到利贝尔的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1060F#6P嗯，就是这样。\x02\x03",

            "#1064F对了，朵洛希。\x01",
            "你怎么会乘坐国际定期船的呢？\x02\x03",

            "刚才你提到东方人街，\x01",
            "难道又是去取材旅行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "#151F#2P嘿嘿，你说对了～\x02\x03",

            "#150F这次也是奈尔前辈\x01",
            "吩咐我一个人去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        (
            "#1060F#6P嗯～\x01",
            "那个人还真是大胆啊。\x02\x03",

            "竟然把国外的取材旅行\x01",
            "只交给朵洛希一个人去做，\x01",
            "是不是有些……\x02\x03",

            "#1071F……但是，话说回来。\x01",
            "就是因为背负责任，\x01",
            "人才会有所成长的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#151F#2P呵呵，就交给我吧～\x02\x03",

            "最开始本来应该\x01",
            "是去柏斯超市取材的，\x01",
            "所以没问题的啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1064F#6P#3S啊……？#2S\x02\x03",

            "#2S我说……\x01",
            "奈尔先生所说的取材\x01",
            "原来是去柏斯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        (
            "#153F#2P嗯，应该是那样的～\x02\x03",

            "可是我在定期船的座位上睡着了，\x01",
            "一睁开眼，就到了\x01",
            "卡尔瓦德共和国的首都了呢～\x02\x03",

            "还会有这种不可思议的事情啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1068F#6P这显然就是\x01",
            "上错了船嘛！\x02\x03",

            "#1063F而且难道你就这样\x01",
            "在共和国待了很多天吗！？\x02\x03",

            "签证和旅费之类的要怎么办！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x10,
        (
            "#151F#2P那个嘛，正好在空港\x01",
            "遇到了利贝尔大使馆的人，\x01",
            "就给我发了临时的证件～\x02\x03",

            "在取材旅行中\x01",
            "也遇到了很多好心的人，\x01",
            "所以也不用担心没钱花～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x109,
        (
            "#1068F#6P唉……\x01",
            "要发牢骚的地方太多了，\x01",
            "就算是我也不知道该从哪入手……\x02\x03",

            "#1060F但是，既然变成了这样，\x01",
            "奈尔先生想必\x01",
            "也会很担心你吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "#150F#2P嗯～很难说啊。\x02\x03",

            "昨天，我联络他说要回编辑部时，\x01",
            "听他声音好像肚子很疼的样子～\x02\x03",

            "#151F果然，\x01",
            "过量吸烟对身体不好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x109,
        (
            "#1068F#6P（那个与其说是吸烟造成的，\x01",
            "　不如说是紧张造成的神经性胃炎吧……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #101
        (
            "\x07\x05——各位乘客，感谢您乘坐本日的\x01",
            "国际定期船『格雷特纳号』，\x01",
            "本社在此致以真诚的谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #102
        (
            "\x07\x05再过３０分钟左右，\x01",
            "本次航班将要到达终点站——\x01",
            "利贝尔王国的首都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #103
        (
            "\x07\x05请确认好自己的随身行李，\x01",
            "并且在着陆前回到自己的座位上。\x01",
            "谢谢合作。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #104
        (
            "\x07\x05——那么请继续享受\x01",
            "这段快乐的空中之旅。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    ChrTalk(    #105
        0x109,
        (
            "#1075F#6P嗯……\x01",
            "已经快要到了啊。\x02\x03",

            "#1060F我想在登陆之前\x01",
            "在船上散散步……\x02\x03",

            "朵洛希，你打算怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "#150F#2P嗯～是啊～\x02\x03",

            "好不容易才搭乘的国际定期船，\x01",
            "我也想要到更多的地方\x01",
            "去拍摄一下啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x109,
        "#1066F#6P这样啊，那就加油吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "#151F#2P嘿嘿。\x01",
            "那么，一会儿再见了～\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_23AB():

        label("loc_23AB")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_23AB")

    QueueWorkItem2(0x109, 3, lambda_23AB)
    OP_43(0x10, 0x0, 0x0, 0x18)

    def lambda_23C3():
        OP_6D(89330, -1000, 49990, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23C3)

    def lambda_23DB():
        OP_6B(2380, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23DB)

    def lambda_23EB():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_23EB)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_44(0x109, 0x3)
    OP_8C(0x109, 180, 0)
    OP_A2(0x25E6)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_23_1982 end

    def Function_24_2415(): pass

    label("Function_24_2415")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8F(0xFE, 0x15E50, 0xFFFFFC18, 0xC760, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x15798, 0x64, 0xAD5C, 0x7D0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2463():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2463)
    OP_8F(0xFE, 0x156F8, 0x64, 0xA8F2, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x7, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x10, 0x80)
    Return()

    # Function_24_2415 end

    def Function_25_2498(): pass

    label("Function_25_2498")

    EventBegin(0x0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #109
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #110
        (
            "\x07\x05本次航班\x01",
            "即将到达终点站，\x01",
            "利贝尔王国首都格兰赛尔。\x02",
        )
    )

    Jump("loc_251F")

    label("loc_251F")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #111
        (
            "\x07\x05着陆的时候会有少许摇晃，\x01",
            "请各位乘客尽快回到座位上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2498 end

    SaveToFile()

Try(main)
