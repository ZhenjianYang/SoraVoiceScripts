from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Dorothy',                              # 9
        'Captain Otl',                          # 10
        'Crew Member Todt',                     # 11
        'Crew Member Daro',                     # 12
        'Passenger',                            # 13
        'Passenger',                            # 14
        'Passenger',                            # 15
        'Passenger',                            # 16
        'Passenger',                            # 17
        'Passenger',                            # 18
        'Passenger',                            # 19
        'Child',                                # 20
        'Mirano',                               # 21
        'Simon',                                # 22
        'Passenger',                            # 23
        'Crew Member Salina',                   # 24
        'Passenger',                            # 25
        'Passenger',                            # 26
        'Passenger',                            # 27
        'Ymir',                                 # 28
        'Dorothy',                              # 29
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
        "Function_4_97B",          # 04, 4
        "Function_5_B04",          # 05, 5
        "Function_6_B3E",          # 06, 6
        "Function_7_BF7",          # 07, 7
        "Function_8_DB4",          # 08, 8
        "Function_9_F0B",          # 09, 9
        "Function_10_10C0",        # 0A, 10
        "Function_11_12A9",        # 0B, 11
        "Function_12_13E9",        # 0C, 12
        "Function_13_1587",        # 0D, 13
        "Function_14_16A5",        # 0E, 14
        "Function_15_1735",        # 0F, 15
        "Function_16_1842",        # 10, 16
        "Function_17_19BC",        # 11, 17
        "Function_18_1AF9",        # 12, 18
        "Function_19_1BE9",        # 13, 19
        "Function_20_1D81",        # 14, 20
        "Function_21_1F20",        # 15, 21
        "Function_22_2096",        # 16, 22
        "Function_23_21F5",        # 17, 23
        "Function_24_2ED9",        # 18, 24
        "Function_25_2F5C",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7E9")

    ChrTalk(    #0
        0xFE,
        "Wh-Who knew you'd be so persistent...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "(How can I get out of this? I can't tell her\x01",
            "a tough guy like me used to want to be a\x01",
            "pastry chef...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_977")

    label("loc_7E9")


    ChrTalk(    #2
        0x11,
        (
            "Why do you want to know what I wanted\x01",
            "to be as a child to begin with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "Th-That's not really something you normally tell\x01",
            "complete strangers with cameras in their hands,\x01",
            "you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x24,
        (
            "#153FI'm on to you, mister! You can't distract me!\x02\x03",

            "#155FThis is a serious news report here, so please\x01",
            "answer my questions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1066F(She sure is making good use of those \x01",
            "reporter's privileges.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_A2(0x25F3)

    label("loc_977")

    TalkEnd(0xFE)
    Return()

    # Function_3_745 end

    def Function_4_97B(): pass

    label("Function_4_97B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_A31")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #6
        0xFE,
        (
            "The Behgan Range is part of the border\x01",
            "between Liberl and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "As soon as we're over that, it'll be barely\x01",
            "any time before we're in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_B00")

    label("loc_A31")


    ChrTalk(    #8
        0x12,
        "We're approaching the Behgan Range.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "Be careful of potential air turbulence in this\x01",
            "area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x13,
        "I know, I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        (
            "I've been doing this route for three years now!\x01",
            "I know what I'm doing, man!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_A2(0x25AA)

    label("loc_B00")

    TalkEnd(0xFE)
    Return()

    # Function_4_97B end

    def Function_5_B04(): pass

    label("Function_5_B04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_B36")

    ChrTalk(    #12
        0xFE,
        "Heading west-northwest! Yahooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3A")

    label("loc_B36")

    Call(0, 4)

    label("loc_B3A")

    TalkEnd(0xFE)
    Return()

    # Function_5_B04 end

    def Function_6_B3E(): pass

    label("Function_6_B3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_BEF")

    ChrTalk(    #13
        0xFE,
        (
            "#151FBy the way, my dream was to become\x01",
            "a phantom thief! Isn't that cool?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1068F(No prizes for guessing what kinds of books\x01",
            "she must've read as a kid...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_BEF")

    Call(0, 3)

    label("loc_BF3")

    TalkEnd(0xFE)
    Return()

    # Function_6_B3E end

    def Function_7_BF7(): pass

    label("Function_7_BF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CEB")

    ChrTalk(    #15
        0xFE,
        (
            "I think a lot of people thought there wouldn't be\x01",
            "much in the way of trouble after the Non-Aggression\x01",
            "Pact was signed, but so much for that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Apparently my grandchild wasn't hurt during the\x01",
            "thing, but I'm still worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB0")

    label("loc_CEB")


    ChrTalk(    #17
        0xFE,
        "I'm off to see my grandchild in Grancel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "We haven't seen one another in three years now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I've been really worried, what with all the\x01",
            "trouble that's been happening in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x25AB)

    label("loc_DB0")

    TalkEnd(0xFE)
    Return()

    # Function_7_BF7 end

    def Function_8_DB4(): pass

    label("Function_8_DB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E8D")

    ChrTalk(    #20
        0xFE,
        (
            "I get that you want to be an orbal engineer and\x01",
            "all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "...but I think you could do with taking things a bit\x01",
            "easier. Getting yourself stressed out and worked\x01",
            "up will only help screw yourself up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F07")

    label("loc_E8D")


    ChrTalk(    #22
        0xFE,
        (
            "Don't go getting yourself TOO worked up now,\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "You'll just end up screwing up even more.\x01",
            "Like usual...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x25AC)

    label("loc_F07")

    TalkEnd(0xFE)
    Return()

    # Function_8_DB4 end

    def Function_9_F0B(): pass

    label("Function_9_F0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FE1")

    ChrTalk(    #24
        0xFE,
        (
            "I might've failed that interview to join the\x01",
            "Verne Company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "...but this is my chance to learn all about\x01",
            "cutting-edge orbal tech! And I'm gonna\x01",
            "master the heck out of it! ...I will! Really!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BC")

    label("loc_FE1")


    ChrTalk(    #26
        0xFE,
        (
            "Anyway, first thing is stopping by the\x01",
            "central factory in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "There's no better place to learn about\x01",
            "cutting-edge orbal tech than there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I-I'm gonna really have to make the most of it!\x01",
            "Really!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x25F4)

    label("loc_10BC")

    TalkEnd(0xFE)
    Return()

    # Function_9_F0B end

    def Function_10_10C0(): pass

    label("Function_10_10C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1137")

    ChrTalk(    #29
        0xFE,
        (
            "It's been three long days of traveling,\x01",
            "but I'm finally almost here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I can hardly wait to land!\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_1137")


    ChrTalk(    #31
        0xFE,
        "YES! I'm finally almost in Liberl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Why did I come, you ask? Because it's the last\x01",
            "spot that ancient dragon was sighted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "There's no information on where it went after it\x01",
            "showed up here, so if I want to try and pursue it,\x01",
            "this is the best place for me to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "As soon as we land, I need to go and talk to\x01",
            "Lyndon to see if he knows anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x25AD)

    label("loc_12A5")

    TalkEnd(0xFE)
    Return()

    # Function_10_10C0 end

    def Function_11_12A9(): pass

    label("Function_11_12A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1349")

    ChrTalk(    #35
        0xFE,
        (
            "The cleaning staff for these airships really\x01",
            "do a splendid job, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'm going to have to make sure I don't undo\x01",
            "their hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E5")

    label("loc_1349")


    ChrTalk(    #37
        0xFE,
        (
            "The cleaning staff for these airships really\x01",
            "do a splendid job, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "They're a fine role model for the rest of the\x01",
            "service industry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x25AE)

    label("loc_13E5")

    TalkEnd(0xFE)
    Return()

    # Function_11_12A9 end

    def Function_12_13E9(): pass

    label("Function_12_13E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1499")

    ChrTalk(    #39
        0xFE,
        (
            "Back in the day, I used to sail the rough waters\x01",
            "of the Titith Bay, but now? Give me a comfy \x01",
            "airship any day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "The times are always a-changing, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1583")

    label("loc_1499")


    ChrTalk(    #41
        0xFE,
        (
            "I used to be a sailor back in the day, but now \x01",
            "I always use airships to get around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "They're way faster than boats, for one thing,\x01",
            "and unlike orbal buses, you don't end up with\x01",
            "a sore ass after a long journey, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_A2(0x25AF)

    label("loc_1583")

    TalkEnd(0xFE)
    Return()

    # Function_12_13E9 end

    def Function_13_1587(): pass

    label("Function_13_1587")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1624")

    ChrTalk(    #43
        0xFE,
        (
            "I swear! Sometimes, I think this child has\x01",
            "ants in her pants or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Can she not sit down quietly for five blissful\x01",
            "minutes?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A1")

    label("loc_1624")


    ChrTalk(    #45
        0xFE,
        (
            "*sigh* No, you can't... Please,\x01",
            "sit down like a good girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "We're almost there now, anyway!\x01",
            "So just be quiet.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x25B0)

    label("loc_16A1")

    TalkEnd(0xFE)
    Return()

    # Function_13_1587 end

    def Function_14_16A5(): pass

    label("Function_14_16A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(    #47
        0xFE,
        "But I'm booored!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Come on. Just for a bit! Please?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_16EE")


    ChrTalk(    #49
        0xFE,
        "Mommy, can I go have a look outside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Can I? Can I?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_A2(0x25B1)

    label("loc_1731")

    TalkEnd(0xFE)
    Return()

    # Function_14_16A5 end

    def Function_15_1735(): pass

    label("Function_15_1735")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_17B7")

    ChrTalk(    #51
        0xFE,
        "*sigh* Her stubbornness drives me nuts sometimes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "She isn't even interested in listening to my \x01",
            "opinion...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183E")

    label("loc_17B7")


    ChrTalk(    #53
        0xFE,
        "My sister can be unbelievably stubborn sometimes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "How am I supposed to enjoy sightseeing when\x01",
            "she's being like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x25B2)

    label("loc_183E")

    TalkEnd(0xFE)
    Return()

    # Function_15_1735 end

    def Function_16_1842(): pass

    label("Function_16_1842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_18E6")

    ChrTalk(    #55
        0xFE,
        (
            "My brother is always so selfish. He only ever\x01",
            "thinks about what HE wants to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "He doesn't care what I want to do.\x01",
            "Augh! He makes me SO mad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B8")

    label("loc_18E6")


    ChrTalk(    #57
        0xFE,
        "No! I'm not budging on this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "We are going to Erbe Royal Villa after Grancel Castle,\x01",
            "and that is final!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I can't believe you're actually considering\x01",
            "just going around FISHING, of all things!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x25B3)

    label("loc_19B8")

    TalkEnd(0xFE)
    Return()

    # Function_16_1842 end

    def Function_17_19BC(): pass

    label("Function_17_19BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1A69")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #60
        0xFE,
        "Ugh... My dad's so annoying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "I'm SIXTEEN, you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I'm old enough to do whatever the hell I want\x01",
            "without him butting into my business!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF5")

    label("loc_1A69")


    ChrTalk(    #63
        0xFE,
        "Ugh... I don't even wanna be here right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Why do I even have to go out of my way to\x01",
            "see him, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "It's not fair!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_A2(0x25B4)

    label("loc_1AF5")

    TalkEnd(0xFE)
    Return()

    # Function_17_19BC end

    def Function_18_1AF9(): pass

    label("Function_18_1AF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1B54")

    ChrTalk(    #66
        0xFE,
        "Do I want to look out? I kind of do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "But I kind of don't, too... \x02",
    )

    CloseMessageWindow()
    Jump("loc_1BE5")

    label("loc_1B54")


    ChrTalk(    #68
        0xFE,
        "I-I'm really not very good with heights...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I mean, it's not phobia level or anything...\x01",
            "I'm just really not very good with them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    OP_A2(0x25B5)

    label("loc_1BE5")

    TalkEnd(0xFE)
    Return()

    # Function_18_1AF9 end

    def Function_19_1BE9(): pass

    label("Function_19_1BE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1C86")

    ChrTalk(    #70
        0xFE,
        (
            "We'll soon be arriving in Grancel City,\x01",
            "the terminus of this liner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Please ensure you have all belongings\x01",
            "with you once we disembark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7D")

    label("loc_1C86")


    ChrTalk(    #72
        0xFE,
        "Did you hear the announcement, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "If not, we will soon be arriving in Grancel City.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "So it might be wise to check you have all of\x01",
            "your belongings on your person while you still\x01",
            "have time to look for anything that is missing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    OP_A2(0x25B6)

    label("loc_1D7D")

    TalkEnd(0xFE)
    Return()

    # Function_19_1BE9 end

    def Function_20_1D81(): pass

    label("Function_20_1D81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1E15")

    ChrTalk(    #75
        0xFE,
        (
            "That bargainer really knew how to put up a good\x01",
            "fight for someone so young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "I wonder if I could convince him to work for me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F1C")

    label("loc_1E15")


    ChrTalk(    #77
        0xFE,
        (
            "That bargainer really knew how to put up a good\x01",
            "fight for someone so young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Still, I've got an excellent information dealer\x01",
            "working for me, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "So the next time we do business, it's going to be\x01",
            "a 6-4 deal in my favor! No, scratch that! 7-3!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x25B7)

    label("loc_1F1C")

    TalkEnd(0xFE)
    Return()

    # Function_20_1D81 end

    def Function_21_1F20(): pass

    label("Function_21_1F20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1FC2")

    ChrTalk(    #80
        0xFE,
        (
            "Still, while she might not have had the upper\x01",
            "hand, she did get what she wanted in the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "It's not like she really 'lost' or anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_1FC2")


    ChrTalk(    #82
        0xFE,
        (
            "Whew... That was one amazing business\x01",
            "discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I never thought I'd see the day when Mirano\x01",
            "wouldn't have the upper hand in one, but it\x01",
            "just happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "The world is full of surprises...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x25B8)

    label("loc_2092")

    TalkEnd(0xFE)
    Return()

    # Function_21_1F20 end

    def Function_22_2096(): pass

    label("Function_22_2096")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2142")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #85
        0xFE,
        (
            "Sorry, but I'm going to have to ask you not\x01",
            "to come down here, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "It's for your own safety. You might end up \x01",
            "tripping on something.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_21F1")

    label("loc_2142")


    ChrTalk(    #87
        0xFE,
        (
            "All right! The orbal pressure looks perfectly\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #88
        0xFE,
        (
            "Oh, sorry. I'm going to have to ask you not to\x01",
            "come down here, sir.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    OP_A2(0xF)
    OP_A2(0x25F5)

    label("loc_21F1")

    TalkEnd(0xFE)
    Return()

    # Function_22_2096 end

    def Function_23_21F5(): pass

    label("Function_23_21F5")

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

    def lambda_226B():
        OP_6D(89180, -1000, 54020, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_226B)

    def lambda_2283():
        OP_67(0, 6430, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2283)

    def lambda_229B():
        OP_6C(27000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_229B)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #89
        0x10,
        (
            "#150F#2POh, I see....\x02\x03",

            "So you're here to carry out a followup \x01",
            "investigation on all that trouble that\x01",
            "happened earlier in the year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1060F#6PThat's about the gist, yeah.\x02\x03",

            "#1064FCome to think of it, how'd you end up on\x01",
            "an international liner like this?\x02\x03",

            "You said you were in the Eastern Quarter,\x01",
            "right? Were you there to write about it for\x01",
            "the Liberl News?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "#151F#2PYep!\x02\x03",

            "#150FNial actually let me go on my own this time,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        (
            "#1060F#6PWow! That was...daring of him.\x02\x03",

            "I'm not sure I'd want to let you handle traveling\x01",
            "abroad for a report alone...\x02\x03",

            "#1071FThen again, it's only by taking on positions of\x01",
            "responsibility that people can properly grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#151F#2PHeehee. Oh, I'm doing plenty of that.\x02\x03",

            "I mean, I wasn't sure what I'd do when I ended up\x01",
            "in Calvard instead of Bose Market, but I managed\x01",
            "juuust fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1064F#6P#3S...Wait a second.#2S\x02\x03",

            "#2SNial told you to go to Bose? Not Calvard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        (
            "#153F#2PHe sure did!\x02\x03",

            "But then I got on the airship, fell asleep,\x01",
            "and before I knew it, I was chilling out in\x01",
            "Calvard's capital!\x02\x03",

            "Weird, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1068F#6PIt sounds like you got on the wrong airship to me!\x02\x03",

            "#1063FLet my brain catch up--so you were in the Republic\x01",
            "for literally DAYS when you weren't even supposed\x01",
            "to be there at all?!\x02\x03",

            "Did you even have enough money to manage?\x01",
            "Or--Aidios, help us--a passport?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x10,
        (
            "#151F#2PWell, fortunately, there was someone from the\x01",
            "Liberlian embassy at the airport who could issue\x01",
            "me a temporary passport, so that was okay...\x02\x03",

            "...and then toooooons of people were really nice\x01",
            "to me and helped while I was there, so I had all\x01",
            "the dough a girl could ask for!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x109,
        (
            "#1068F#6P*sigh* I don't even know where to start...\x02\x03",

            "#1060FNial must be worried sick about you, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "#150F#2PYou think?\x02\x03",

            "He didn't sound so hot when I called yesterday\x01",
            "to say I'd be coming back to the office today.\x02\x03",

            "#151FI keep telling him that all that smoking is bad for\x01",
            "him, but he never listens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x109,
        (
            "#1068F#6P(I don't think you can pin the crime on tobacco\x01",
            "this time, missy.)\x02",
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
    SetChrName("Female Voice")

    AnonymousTalk(    #101
        (
            "\x07\x05Thank you all for taking this journey aboard the\x01",
            "Gretna today.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #102
        (
            "\x07\x05We will be arriving at our terminal, Grancel City,\x01",
            "in roughly thirty minutes.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #103
        (
            "\x07\x05We ask that you take this chance to check that\x01",
            "you have all of your belongings with you and to\x01",
            "return to your seats before we begin our landing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #104
        (
            "\x07\x05Until then, please enjoy the remainder of your\x01",
            "flight.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    ChrTalk(    #105
        0x109,
        (
            "#1075F#6PWhew... Sounds like we're almost there.\x02\x03",

            "#1060FI'm gonna have a walk around the ship\x01",
            "to kill some of the last half hour.\x02\x03",

            "How 'bout you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "#150F#2PHmm... I'm not sure.\x02\x03",

            "I suppose I might as well go and snap some\x01",
            "more photos. It's not often I get to take an\x01",
            "international liner like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x109,
        "#1066F#6PSounds like a plan. See you later, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        "#151F#2PHeehee. Later!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2E6F():

        label("loc_2E6F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2E6F")

    QueueWorkItem2(0x109, 3, lambda_2E6F)
    OP_43(0x10, 0x0, 0x0, 0x18)

    def lambda_2E87():
        OP_6D(89330, -1000, 49990, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E87)

    def lambda_2E9F():
        OP_6B(2380, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E9F)

    def lambda_2EAF():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EAF)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_44(0x109, 0x3)
    OP_8C(0x109, 180, 0)
    OP_A2(0x25E6)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_23_21F5 end

    def Function_24_2ED9(): pass

    label("Function_24_2ED9")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8F(0xFE, 0x15E50, 0xFFFFFC18, 0xC760, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8F(0xFE, 0x15798, 0x64, 0xAD5C, 0x7D0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2F27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F27)
    OP_8F(0xFE, 0x156F8, 0x64, 0xA8F2, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x7, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x10, 0x80)
    Return()

    # Function_24_2ED9 end

    def Function_25_2F5C(): pass

    label("Function_25_2F5C")

    EventBegin(0x0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Female Voice")

    AnonymousTalk(    #109
        "\x07\x05This is a passenger announcement.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #110
        (
            "\x07\x05We'll soon be arriving in Grancel City,\x01",
            "the terminus of this liner.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #111
        (
            "\x07\x05We suggest that all passengers return to their\x01",
            "seats as soon as possible, as the airship may be\x01",
            "unsteady during landing.\x02",
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

    # Function_25_2F5C end

    SaveToFile()

Try(main)
