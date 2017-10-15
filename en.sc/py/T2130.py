from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2130   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2130   ._SN',
            'ED6_DT21/T2130_1 ._SN',
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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
        'Antonio',                              # 12
        'Father Theodore',                      # 13
        'Sister Frieda',                        # 14
        'Father Kevin',                         # 15
        'Eletta',                               # 16
        'Todd',                                 # 17
        'Atget',                                # 18
        'Louis',                                # 19
        'Burt',                                 # 20
        'Bargo',                                # 21
        'Terence',                              # 22
        'Jabu',                                 # 23
        'Picaro',                               # 24
        'Blaue',                                # 25
        'Dorothy',                              # 26
        'Targeting Camera',                     # 27
        'Antonio',                              # 28
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
        'ED6_DT07/CH02510 ._CH',             # 00
        'ED6_DT07/CH02520 ._CH',             # 01
        'ED6_DT07/CH02530 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01670 ._CH',             # 05
        'ED6_DT07/CH01410 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT26/CH20237 ._CH',             # 0A
        'ED6_DT07/CH01390 ._CH',             # 0B
        'ED6_DT07/CH01393 ._CH',             # 0C
        'ED6_DT07/CH00450 ._CH',             # 0D
        'ED6_DT07/CH00460 ._CH',             # 0E
        'ED6_DT07/CH00470 ._CH',             # 0F
        'ED6_DT27/CH04000 ._CH',             # 10
        'ED6_DT07/CH00120 ._CH',             # 11
        'ED6_DT07/CH00150 ._CH',             # 12
        'ED6_DT07/CH00454 ._CH',             # 13
        'ED6_DT07/CH00464 ._CH',             # 14
        'ED6_DT07/CH00474 ._CH',             # 15
        'ED6_DT06/CH20063 ._CH',             # 16
        'ED6_DT07/CH00122 ._CH',             # 17
        'ED6_DT07/CH01000 ._CH',             # 18
        'ED6_DT06/CH20064 ._CH',             # 19
        'ED6_DT07/CH01040 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02510P._CP',             # 00
        'ED6_DT07/CH02520P._CP',             # 01
        'ED6_DT07/CH02530P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01670P._CP',             # 05
        'ED6_DT07/CH01410P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT26/CH20237P._CP',             # 0A
        'ED6_DT07/CH01390P._CP',             # 0B
        'ED6_DT07/CH01393P._CP',             # 0C
        'ED6_DT07/CH00450P._CP',             # 0D
        'ED6_DT07/CH00460P._CP',             # 0E
        'ED6_DT07/CH00470P._CP',             # 0F
        'ED6_DT27/CH04000P._CP',             # 10
        'ED6_DT07/CH00120P._CP',             # 11
        'ED6_DT07/CH00150P._CP',             # 12
        'ED6_DT07/CH00454P._CP',             # 13
        'ED6_DT07/CH00464P._CP',             # 14
        'ED6_DT07/CH00474P._CP',             # 15
        'ED6_DT06/CH20063P._CP',             # 16
        'ED6_DT07/CH00122P._CP',             # 17
        'ED6_DT07/CH01000P._CP',             # 18
        'ED6_DT06/CH20064P._CP',             # 19
        'ED6_DT07/CH01040P._CP',             # 1A
    )

    DeclNpc(
        X                   = -4150,
        Z                   = 0,
        Y                   = 9070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1590,
        Z                   = 0,
        Y                   = 7520,
        Direction           = 322,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 7390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56350,
        Z                   = 80,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 58970,
        Z                   = 1000,
        Y                   = 52150,
        Direction           = 180,
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
        X                   = 54460,
        Z                   = 0,
        Y                   = 50690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 60540,
        Z                   = 1000,
        Y                   = 52350,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 59120,
        Z                   = 0,
        Y                   = 47050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57540,
        Z                   = 0,
        Y                   = 47300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = 47260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 61430,
        Z                   = 0,
        Y                   = 47360,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -10050,
        Z                   = 0,
        Y                   = 3740,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -12730,
        Z                   = 0,
        Y                   = 4160,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -9930,
        Z                   = 0,
        Y                   = 7470,
        Direction           = 280,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -13330,
        Z                   = 600,
        Y                   = 6230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -11600,
        Z                   = 250,
        Y                   = 1950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 59140,
        Z                   = 0,
        Y                   = 46600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 52250,
        Z                   = 5000,
        Y                   = 51330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56350,
        Z                   = -600,
        Y                   = 44730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 59140,
        TriggerZ            = 1000,
        TriggerY            = 50250,
        TriggerRange        = 400,
        ActorX              = 58970,
        ActorZ              = 2700,
        ActorY              = 52150,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_580",          # 01, 1
        "Function_2_591",          # 02, 2
        "Function_3_70E",          # 03, 3
        "Function_4_9D1",          # 04, 4
        "Function_5_BD2",          # 05, 5
        "Function_6_1095",         # 06, 6
        "Function_7_12D0",         # 07, 7
        "Function_8_14E1",         # 08, 8
        "Function_9_1892",         # 09, 9
        "Function_10_1D2C",        # 0A, 10
        "Function_11_1EC6",        # 0B, 11
        "Function_12_1F5F",        # 0C, 12
        "Function_13_1FE4",        # 0D, 13
        "Function_14_20CB",        # 0E, 14
        "Function_15_21F9",        # 0F, 15
        "Function_16_2C7F",        # 10, 16
        "Function_17_2D1C",        # 11, 17
        "Function_18_2FEB",        # 12, 18
        "Function_19_30C7",        # 13, 19
        "Function_20_32CA",        # 14, 20
        "Function_21_7005",        # 15, 21
        "Function_22_701F",        # 16, 22
        "Function_23_7034",        # 17, 23
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_45C")
    SetChrFlags(0x18, 0x10)

    label("loc_45C")

    Jump("loc_4D7")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49E")
    Jump("loc_4D7")

    label("loc_49E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4C1")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, 53390, 0, 52130, 180)
    Jump("loc_4D7")

    label("loc_4C1")

    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, -16840, 0, 42910, 270)

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5")
    OP_A2(0xD)

    label("loc_4F5")

    Jump("loc_502")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_502")
    OP_A2(0xD)

    label("loc_502")

    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_515")
    Jump("loc_521")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xA, 0x10)

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_52D")
    SetChrFlags(0xA, 0x80)

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556")
    ClearChrFlags(0xE, 0x80)
    TurnDirection(0xC, 0xE, 0)
    TurnDirection(0xE, 0xC, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_556")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_562"),
        (SWITCH_DEFAULT, "loc_57F"),
    )


    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_57C")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_57C")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_57C")

    Jump("loc_57F")

    label("loc_57F")

    Return()

    # Function_0_426 end

    def Function_1_580(): pass

    label("Function_1_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")
    OP_64(0x0, 0x1)

    label("loc_590")

    Return()

    # Function_1_580 end

    def Function_2_591(): pass

    label("Function_2_591")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_6F8")

    label("loc_5B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_6F8")

    label("loc_5CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_6F8")

    label("loc_5E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_601")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_6F8")

    label("loc_601")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_6F8")

    label("loc_61A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_6F8")

    label("loc_633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_6F8")

    label("loc_64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_6F8")

    label("loc_665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_6F8")

    label("loc_67E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_6F8")

    label("loc_697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_6F8")

    label("loc_6B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_6F8")

    label("loc_6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_6F8")

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_6F8")

    label("loc_70D")

    Return()

    # Function_2_591 end

    def Function_3_70E(): pass

    label("Function_3_70E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_78C")

    ChrTalk(    #0
        0xFE,
        (
            "That Belden... He said he's helping\x01",
            "out with the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I wonder if Rocco and the others are angry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CD")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_8A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_7F7")

    ChrTalk(    #2
        0xFE,
        "*sigh* Things were nice when I was a kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I wish I could go back to those days.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A5")

    label("loc_7F7")

    OP_A2(0xC)

    ChrTalk(    #4
        0xFE,
        "Today's the day for Sunday School, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I was pretty good at studying despite how\x01",
            "I look. The sister complimented me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "*sigh* Those days were so good.\x02",
    )

    CloseMessageWindow()

    label("loc_8A5")

    Jump("loc_9CD")

    label("loc_8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(    #7
        0xFE,
        "The entire city's crazy about the election.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "It's not like I don't have the time, I guess.\x01",
            "Maybe I should go sneak my vote in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CD")

    label("loc_93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(    #9
        0xFE,
        (
            "*pheeew* First time in a long time\x01",
            "I've been in such a tense situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "A-Anyway, I'm just glad I didn't\x01",
            "get dragged into it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CD")

    TalkEnd(0xFE)
    Return()

    # Function_3_70E end

    def Function_4_9D1(): pass

    label("Function_4_9D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_A5B")

    ChrTalk(    #11
        0xFE,
        (
            "I ain't doin' some pain in\x01",
            "the butt election stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Though, if you were gonna gimme\x01",
            "some mira, I'd think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCE")

    label("loc_A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(    #13
        0xFE,
        "The casino's interestin', but it's a bit far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "The bridge is such a pain.\x01",
            "I can't stand crossing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCE")

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #15
        0xFE,
        (
            "Wasn't nothin' good about goin' to\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "That's why I said I ain't doin'\x01",
            "anything that's a pain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCE")

    label("loc_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(    #17
        0xFE,
        "Everyone's always out pickin' fights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Even though they know they're\x01",
            "gonna get beat down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCE")

    TalkEnd(0xFE)
    Return()

    # Function_4_9D1 end

    def Function_5_BD2(): pass

    label("Function_5_BD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #19
        0xFE,
        (
            "Apparently Rocco plans on turnin' the\x01",
            "Ravens into some kinda neighborhood\x01",
            "watch group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Well, if it gets annoying,\x01",
            "I'll be checking out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_D0B")

    label("loc_C7C")


    ChrTalk(    #21
        0xFE,
        (
            "Apparently Rocco plans on turnin' the\x01",
            "Ravens into some kinda neighborhood\x01",
            "watch group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "Well, it's got nothin' to do with me, though.\x02",
    )

    CloseMessageWindow()

    label("loc_D0B")

    Jump("loc_1091")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDE")

    ChrTalk(    #23
        0xFE,
        "Hmm? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Our members are all out right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Didn't you see them all yelling,\x01",
            "'the dock is over here'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Seriously, that Rocco. What\x01",
            "a boring thing he thought up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_E45")

    label("loc_DDE")


    ChrTalk(    #27
        0xFE,
        "Our members are all out right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Seriously, that Rocco. What\x01",
            "a boring thing he thought up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E45")

    Jump("loc_1091")

    label("loc_E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_EAE")

    ChrTalk(    #29
        0xFE,
        "Lately Rocco's been actin' real weird.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Might be time to get out if this keeps up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1091")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_EFD")

    ChrTalk(    #31
        0xFE,
        (
            "The only types who get wrapped\x01",
            "up in a fight are idiots.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9D")

    label("loc_EFD")

    OP_A2(0xB)

    ChrTalk(    #32
        0xFE,
        (
            "The only types who get wrapped\x01",
            "up in a fight are idiots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "On that point, I never let my guard down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Check out before things get bad,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9D")

    Jump("loc_1091")

    label("loc_FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_100C")

    ChrTalk(    #35
        0xFE,
        (
            "The sun set while we were talkin'\x01",
            "over what to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "Seriously, what a waste of life.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1091")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1091")

    ChrTalk(    #37
        0xFE,
        (
            "*pheeew* Glad I didn't get wrapped\x01",
            "up this time, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Annoyin' things can skip me right on by.\x01",
            "Gotta live smart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1091")

    TalkEnd(0xFE)
    Return()

    # Function_5_BD2 end

    def Function_6_1095(): pass

    label("Function_6_1095")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1129")

    ChrTalk(    #39
        0xFE,
        (
            "Heh heh, O'Neil gave me some\x01",
            "extra change. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Of course, I just stayed quiet and took it.\x01",
            "Really, I'm such a bad guy. Heh heh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CC")

    label("loc_1129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_117C")

    ChrTalk(    #41
        0xFE,
        "I'm outta chocolate cigs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "I can never calm down without those.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12CC")

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(    #43
        0xFE,
        "I traded in some chips I picked up at the casino.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "H-Heh heh... A free 100 mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Th-The staff probably didn't notice,\x01",
            "right? R-Right...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CC")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_12CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_127F")

    ChrTalk(    #46
        0xFE,
        "Everyone's gotten stronger, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Can't match up to bracers, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_12CC")

    label("loc_127F")


    ChrTalk(    #48
        0xFE,
        "Everyone's gotten stronger, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Can't match up to bracers, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_12CC")

    TalkEnd(0xFE)
    Return()

    # Function_6_1095 end

    def Function_7_12D0(): pass

    label("Function_7_12D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(    #50
        0xFE,
        (
            "Belden's been turning up at his\x01",
            "dad's office lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Stranger things have happened,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_13C7")

    ChrTalk(    #52
        0xFE,
        "A fight in the middle of the city, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Those guys doin' that election must\x01",
            "have a lot of free time, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_13C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_146F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_13F8")

    ChrTalk(    #54
        0xFE,
        "*yaaaaawn* So bored...\x02",
    )

    CloseMessageWindow()
    Jump("loc_146C")

    label("loc_13F8")

    OP_A2(0xA)

    ChrTalk(    #55
        0xFE,
        "*yaaaaawn* So bored...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I'd like to go to the casino, but without\x01",
            "any mira it's, well, kinda pointless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146C")

    Jump("loc_14DD")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_14DD")

    ChrTalk(    #57
        0xFE,
        (
            "That guy Belden gets along real bad\x01",
            "with his dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "So, that's why he started showing up here.\x02",
    )

    CloseMessageWindow()

    label("loc_14DD")

    TalkEnd(0xFE)
    Return()

    # Function_7_12D0 end

    def Function_8_14E1(): pass

    label("Function_8_14E1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1560")

    ChrTalk(    #59
        0xFE,
        (
            "#1742FI wonder what the heck Rocco's doing.\x02\x03",

            "He said he was gonna go 'move around'\x01",
            "and hasn't come back yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188E")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_15F8")

    ChrTalk(    #60
        0xFE,
        (
            "#1740FWhy don't we just let whoever wants\x01",
            "to be the mayor be the mayor?\x02\x03",

            "Can't be worse than Dalmore,\x01",
            "whoever it turns out to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657")

    label("loc_15F8")

    OP_A2(0x7)

    ChrTalk(    #61
        0xFE,
        (
            "#1744FOh, yeah, there's an election goin' on.\x02\x03",

            "#1740FOf course, I'm not gonna go vote.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657")

    Jump("loc_188E")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1735")

    ChrTalk(    #62
        0xFE,
        (
            "#1742FWe've become a bunch stronger,\x01",
            "too, I'm sure, but...\x02\x03",

            "Lately, the monsters have also\x01",
            "become stronger.\x02\x03",

            "#1744FBecause of that, it's hard to get a sense of\x01",
            "exactly HOW MUCH stronger we've gotten.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188E")

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_188E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_17AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1777")

    ChrTalk(    #63
        0xFE,
        (
            "#1740FHey, good work.\x02\x03",

            "How's Belden?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AB")

    label("loc_1777")


    ChrTalk(    #64
        0xFE,
        (
            "#1740FAh, good work.\x02\x03",

            "Did Belden say anything?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AB")

    Jump("loc_188E")

    label("loc_17AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1823")

    ChrTalk(    #65
        0xFE,
        (
            "#1740FBelden's house is to the right\x01",
            "of the mayoral mansion.\x02\x03",

            "He's the oldest son of that\x01",
            "Norman guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188E")

    label("loc_1823")


    ChrTalk(    #66
        0xFE,
        (
            "#1740FBelden's house is to the right\x01",
            "of the mayoral mansion.\x02\x03",

            "He's the oldest son of that\x01",
            "Norman guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188E")

    TalkEnd(0x8)
    Return()

    # Function_8_14E1 end

    def Function_9_1892(): pass

    label("Function_9_1892")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_19E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_191F")

    ChrTalk(    #67
        0xFE,
        (
            "#1754FWhen I went out a bit ago, Rocco\x01",
            "was behind the warehouse.\x02\x03",

            "He was all quiet, swinging his\x01",
            "weapon at the air.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_191F")

    OP_A2(0x8)

    ChrTalk(    #68
        0xFE,
        (
            "#1752FWhen I went out a bit ago, Rocco\x01",
            "was behind the warehouse.\x02\x03",

            "He was all quiet, swinging his\x01",
            "weapon at the air.\x02\x03",

            "#1754FWhen Rocco starts doin' trainin' like\x01",
            "that, nothin' good's coming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E5")

    Jump("loc_1D28")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1AA9")

    ChrTalk(    #69
        0xFE,
        (
            "#1756FHeh heh, apparently there was a\x01",
            "fight among all those election idiots.\x02\x03",

            "Pull back the curtains off those guys who act\x01",
            "all high-class and that's who they really are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8D")

    label("loc_1AA9")

    OP_A2(0x8)

    ChrTalk(    #70
        0xFE,
        (
            "#1756FHeh heh, apparently there was a\x01",
            "fight among all those election idiots.\x02\x03",

            "Pull back the curtains off those guys who act\x01",
            "all high-class and that's who they really are.\x02\x03",

            "#1750FThat Dalmore guy was a good example.\x01",
            "Heh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8D")

    Jump("loc_1D28")

    label("loc_1B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1BEB")

    ChrTalk(    #71
        0xFE,
        (
            "#1754FFor a while now, Rocco's been doin'\x01",
            "some serious thinking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C68")

    label("loc_1BEB")

    OP_A2(0x8)

    ChrTalk(    #72
        0xFE,
        (
            "#1755FLately Rocco's been doin' some serious thinking.\x02\x03",

            "#1754FWhen he gets like that, it's\x01",
            "best not to get near him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C68")

    Jump("loc_1D28")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1D28")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB5")

    ChrTalk(    #73
        0xFE,
        "#1751FHeh heh, Esteeeelle. Come on back again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEE")

    ChrTalk(    #74
        0xFE,
        "#1750FG-Good work. We'll be waitin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D28")

    ChrTalk(    #75
        0xFE,
        "#1751FCome back again, okay, Esteeeelle.\x02",
    )

    CloseMessageWindow()

    label("loc_1D28")

    TalkEnd(0x9)
    Return()

    # Function_9_1892 end

    def Function_10_1D2C(): pass

    label("Function_10_1D2C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1D71")

    ChrTalk(    #76
        0xFE,
        (
            "#1765FMayoral election...\x02\x03",

            "#1763FHmph, how stupid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC2")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1DA1")

    ChrTalk(    #77
        0xFE,
        (
            "#1764F...\x02\x03",

            "Damn it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEA")

    label("loc_1DA1")

    OP_A2(0x9)

    ChrTalk(    #78
        0xFE,
        (
            "#1764FDammit...\x02\x03",

            "Even we know things can't keep going like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEA")

    Jump("loc_1EC2")

    label("loc_1DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E17")

    ChrTalk(    #79
        0xFE,
        (
            "#1764F...\x02\x03",

            "...Damn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC2")

    label("loc_1E17")


    ChrTalk(    #80
        0xFE,
        (
            "#1765FEver since he saw that shadow, Belden's\x01",
            "locked himself in his house.\x02\x03",

            "Of course, he's always been a cream puff from\x01",
            "a nice family, so he's never had much guts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC2")

    TalkEnd(0xA)
    Return()

    # Function_10_1D2C end

    def Function_11_1EC6(): pass

    label("Function_11_1EC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F30")

    ChrTalk(    #81
        0xFE,
        "Bracers sure are cool, aren't they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Maybe I should try and be one, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5B")

    label("loc_1F30")


    ChrTalk(    #83
        0xFE,
        "The lessons at the church are so fun!\x02",
    )

    CloseMessageWindow()

    label("loc_1F5B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1EC6 end

    def Function_12_1F5F(): pass

    label("Function_12_1F5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FBE")

    ChrTalk(    #84
        0xFE,
        "So bracers even teach at Sunday School?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "That was a surprise.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE0")

    label("loc_1FBE")


    ChrTalk(    #86
        0xFE,
        "I'm studying with Eletta. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_1FE0")

    TalkEnd(0xFE)
    Return()

    # Function_12_1F5F end

    def Function_13_1FE4(): pass

    label("Function_13_1FE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #87
        0xFE,
        "I-I wonder if classes are ending soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I gotta hurry or the next airliner will arrive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20C7")

    label("loc_205D")


    ChrTalk(    #89
        0xFE,
        "I see a lot of bracers at the landing port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "They always seem so busy,\x01",
            "so it must be a hard job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1FE4 end

    def Function_14_20CB(): pass

    label("Function_14_20CB")

    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    ChrTalk(    #91
        0xC,
        "Hey, good work. How were the orphanage kids?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#1060FThey were plenty energetic.\x02\x03",

            "Seems like they're all in good spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        (
            "They do say the younger the\x01",
            "sprout, the stronger it grows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xC,
        (
            "It seems we've got something\x01",
            "to learn from them ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        "#1060FOh, absolutely.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    OP_4B(0xE, 255)
    Return()

    # Function_14_20CB end

    def Function_15_21F9(): pass

    label("Function_15_21F9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E4")

    ChrTalk(    #96
        0xC,
        (
            "Those young people calling themselves the\x01",
            "'Ravens' have been quite helpful, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "The more rebellious, the harder they work once\x01",
            "they reform, they say, and this sure feels like\x01",
            "an example of that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_233F")

    label("loc_22E4")


    ChrTalk(    #98
        0xC,
        (
            "Those young people calling themselves the\x01",
            "'Ravens' have been quite helpful, it seems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233F")

    Jump("loc_2C7B")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245F")

    ChrTalk(    #99
        0xC,
        (
            "When this phenomenon took hold,\x01",
            "the entire city was in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "Somehow things calmed down after a bit,\x01",
            "but I was pretty worried for a moment, there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        (
            "How much we rely on orbal devices\x01",
            "day to day... Recent events have certainly\x01",
            "shown us just that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_24F6")

    label("loc_245F")


    ChrTalk(    #102
        0xC,
        (
            "At first when the phenomenon occurred,\x01",
            "the city was a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        (
            "Well, guess that just means that's how\x01",
            "much we've been relying on orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F6")

    Jump("loc_2C7B")

    label("loc_24F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_257D")

    ChrTalk(    #104
        0xC,
        "Whoever wins, I hope they settle things soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "Once this election ends, the citizens\x01",
            "of Ruan will come together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7B")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2949")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26C5")

    ChrTalk(    #106
        0xC,
        (
            "It's special qualities like these that allow\x01",
            "the guild to be an organization that goes\x01",
            "beyond national borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        (
            "There are a number of agreements between\x01",
            "the guild and nations aside from that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        (
            "The most notable promise is their non-\x01",
            "interference with national privilege.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_26C5")

    OP_A2(0x2)

    ChrTalk(    #109
        0xC,
        (
            "...And the organization that appeared in\x01",
            "that situation is the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "As everyone knows, the Bracer Guild is a\x01",
            "massive organization that manages bracers\x01",
            "all over the continent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "Their biggest notable quality is that they\x01",
            "are a non-governmental organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xC,
        (
            "Ah, a non-governmental organization, uh,\x01",
            "basically means that they don't interfere\x01",
            "with countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284E")

    Jump("loc_2946")

    label("loc_2851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28D2")

    ChrTalk(    #113
        0xC,
        (
            "So, for the end of class let's\x01",
            "go over what we did today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "First, about the foundation of the\x01",
            "Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2946")

    label("loc_28D2")

    OP_A2(0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #115
        0xC,
        "Oh, you guys. Good work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        "I'm still in the middle of class, so pardon me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 0)

    label("loc_2946")

    Jump("loc_2C7B")

    label("loc_2949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_29CB")

    ChrTalk(    #117
        0xC,
        "Hey, what's all the excitement about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        (
            "The traveling priest fellow's already\x01",
            "headed off to his next territory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7B")

    label("loc_29CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A77")
    OP_4A(0xE, 255)

    ChrTalk(    #119
        0xC,
        (
            "Incidentally, Father Kevin. Are you going\x01",
            "to head to your next region soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        (
            "Since you've got the time, you\x01",
            "should enjoy Ruan a bit more.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    Jump("loc_2A7E")

    label("loc_2A77")

    OP_A2(0x4)
    Call(0, 14)

    label("loc_2A7E")

    Jump("loc_2C7B")

    label("loc_2A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE9")

    ChrTalk(    #121
        0xC,
        "Hey, today's Sunday School.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "Put yourself into it and\x01",
            "give these kids a lecture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7B")

    label("loc_2AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2C7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B9F")

    ChrTalk(    #123
        0xC,
        (
            "It's fine to get excited about an election,\x01",
            "but I wish they'd stop makin' so much noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "Ruan, as you can see, is a place\x01",
            "with some very excitable people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7B")

    label("loc_2B9F")

    OP_A2(0x2)

    ChrTalk(    #125
        0xC,
        (
            "It's fine to get excited about an election,\x01",
            "but I wish they'd stop makin' so much noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "Ruan, as you can see, is a city built\x01",
            "by men of the sea, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xC,
        "It's a land with some very excitable people.\x02",
    )

    CloseMessageWindow()

    label("loc_2C7B")

    TalkEnd(0xC)
    Return()

    # Function_15_21F9 end

    def Function_16_2C7F(): pass

    label("Function_16_2C7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D11")
    OP_4A(0xC, 255)

    ChrTalk(    #128
        0xE,
        (
            "#1060FOnce I get a bit of relax time in,\x01",
            "I plan on headin' out immediately.\x02\x03",

            "I got a lot I need t'look into, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    Jump("loc_2D18")

    label("loc_2D11")

    OP_A2(0x4)
    Call(0, 14)

    label("loc_2D18")

    TalkEnd(0xFE)
    Return()

    # Function_16_2C7F end

    def Function_17_2D1C(): pass

    label("Function_17_2D1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2D29")
    Jump("loc_2FE7")

    label("loc_2D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2FE7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DAA")

    ChrTalk(    #129
        0xFE,
        (
            "Year 1187, huh?\x01",
            "All right, this time I've got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "Judis was 1187, huh. 1187, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E46")

    label("loc_2DAA")

    OP_A2(0x1)

    ChrTalk(    #131
        0xFE,
        (
            "Let's see... Alicia the Second\x01",
            "was crowned in 1162.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Er, after that, Crown Prince\x01",
            "Judis passed away in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "...Ahh, I forgot again.\x02",
    )

    CloseMessageWindow()

    label("loc_2E46")

    Jump("loc_2FE7")

    label("loc_2E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F0F")

    ChrTalk(    #135
        0xFE,
        (
            "Ah, it wasn't called the central factory at\x01",
            "the time. It was the 'engineering factory.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Little details like these seem to get picked for\x01",
            "entrance exams, so I gotta be careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE7")

    label("loc_2F0F")

    OP_A2(0x1)

    ChrTalk(    #137
        0xFE,
        "Er... The central factory was established in 1157.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "The test flight of the Calatrava was in 1168,\x01",
            "and the scheduled liners were commissioned\x01",
            "in 1175... Right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "...All right, I've learned up to there.\x02",
    )

    CloseMessageWindow()

    label("loc_2FE7")

    TalkEnd(0xFE)
    Return()

    # Function_17_2D1C end

    def Function_18_2FEB(): pass

    label("Function_18_2FEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2FF8")
    Jump("loc_30C3")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_30C3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3051")

    ChrTalk(    #140
        0xFE,
        "Ah, the bracer teacher.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "Will you come teach again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C3")

    label("loc_3051")


    ChrTalk(    #142
        0xFE,
        "Ahem! I'm already attending Sunday School.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I'm gonna study lots and go to\x01",
            "the same school as Gerome. ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C3")

    TalkEnd(0xFE)
    Return()

    # Function_18_2FEB end

    def Function_19_30C7(): pass

    label("Function_19_30C7")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313D")

    ChrTalk(    #144
        0xFE,
        "Aidios... Please forgive us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I am sure those who have lost\x01",
            "their faith will repent.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_315F")

    label("loc_313D")


    ChrTalk(    #146
        0xFE,
        "Aidios... Please forgive us.\x02",
    )

    CloseMessageWindow()

    label("loc_315F")

    Jump("loc_32C6")

    label("loc_3162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_32C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3258")

    ChrTalk(    #147
        0xFE,
        (
            "I came to meet an acquaintance\x01",
            "here in Ruan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Unfortunately, with this all going on\x01",
            "I couldn't even go home if I wanted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Phew! Anyway, all we can do now is cling\x01",
            "to the Goddess and pray for Her mercy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_32C6")

    label("loc_3258")


    ChrTalk(    #150
        0xFE,
        "Here, you pray to Her, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "When something like this happens, all\x01",
            "we can do is pray to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C6")

    TalkEnd(0x18)
    Return()

    # Function_19_30C7 end

    def Function_20_32CA(): pass

    label("Function_20_32CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32DB")
    Call(0, 23)

    label("loc_32DB")

    EventBegin(0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x101, 110, 0, 450, 348)
    SetChrPos(0xF7, -790, 0, -230, 347)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_8C(0x8, 135, 0)
    OP_8C(0x9, 270, 0)
    OP_6D(-3640, 0, 9320, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #152
        0x8,
        (
            "#1749F#6PHaaaaaaa...\x01",
            "Man, I've been feeling worn out lately.\x02\x03",

            "#6PWe've been working like dogs at training,\x01",
            "but it still doesn't feel like we're any stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "#1764F#3PTch...\x02\x03",

            "I don't get why we're having trouble with\x01",
            "random fuggin' monsters on the roads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "#1753F#2PAh, it isn't just us, though. Everyone's\x01",
            "been sayin' the monsters are gettin'\x01",
            "really dangerous lately.\x02\x03",

            "#1750F#2PLike, everything's gotten a couple times more\x01",
            "powerful than it used to be. It's freaky...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #155
        0xA,
        (
            "#1765F#3PNow that you mention it...yeah...\x02\x03",

            "#1763F#3P...Ah, whatever. How about we have a night\x01",
            "on the town? First one we've had in a while!\x02\x03",

            "#1761F#3PWe can hit up the Lavantar in the\x01",
            "north block! How's that sound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        (
            "#1756F#2POh, that place with the remodeled\x01",
            "second floor that's a casino now?!\x02\x03",

            "#1751FAww yeah, that sounds great, especially\x01",
            "since I hear the dealers are hot chicks!\x02\x03",

            "Maybe I can show them my strength\x01",
            "at poker, if you know what I mean!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #157
        0x8,
        (
            "#1743F#6PNow that's a plan!\x02\x03",

            "#1741F#6PCarna's out of town, so if we wanna\x01",
            "cut loose a bit, now's the time!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_515D")

    NpcTalk(    #158
        0x106,
        "Man's Voice",
        (
            "#2PDo you seriously think you\x01",
            "can get away with that?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 410, 0, -450, 348)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_387A():
        OP_6D(-2500, 0, 4470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_387A)

    def lambda_3892():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3892)

    def lambda_38AA():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38AA)

    def lambda_38BA():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_38BA)

    def lambda_38CA():

        label("loc_38CA")

        TurnDirection(0x8, 0x106, 400)
        OP_48()
        Jump("loc_38CA")

    QueueWorkItem2(0x8, 1, lambda_38CA)

    def lambda_38DB():

        label("loc_38DB")

        TurnDirection(0x9, 0x106, 400)
        OP_48()
        Jump("loc_38DB")

    QueueWorkItem2(0x9, 1, lambda_38DB)

    def lambda_38EC():

        label("loc_38EC")

        TurnDirection(0xA, 0x106, 400)
        OP_48()
        Jump("loc_38EC")

    QueueWorkItem2(0xA, 1, lambda_38EC)
    TurnDirection(0x13, 0x106, 800)
    TurnDirection(0x14, 0x106, 800)
    TurnDirection(0x15, 0x106, 800)
    Sleep(300)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #159
        0x8,
        "#1743F#4PA-Agate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        "#1762F#4PTch...\x02",
    )

    CloseMessageWindow()

    def lambda_3953():

        label("loc_3953")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_3953")

    QueueWorkItem2(0x106, 1, lambda_3953)

    def lambda_3964():

        label("loc_3964")

        TurnDirection(0x106, 0xA, 0)
        OP_48()
        Jump("loc_3964")

    QueueWorkItem2(0x106, 2, lambda_3964)

    def lambda_3975():

        label("loc_3975")

        TurnDirection(0x13, 0x106, 0)
        OP_48()
        Jump("loc_3975")

    QueueWorkItem2(0x13, 0, lambda_3975)

    def lambda_3986():

        label("loc_3986")

        TurnDirection(0x14, 0x106, 0)
        OP_48()
        Jump("loc_3986")

    QueueWorkItem2(0x14, 0, lambda_3986)

    def lambda_3997():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0x12B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3997)
    Sleep(300)

    def lambda_39B7():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39B7)
    Sleep(500)

    def lambda_39D7():
        OP_6D(-3350, 0, 7460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39D7)

    def lambda_39EF():
        OP_67(0, 8350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39EF)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x106, 0x0)
    OP_44(0x106, 0x1)
    OP_44(0x106, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)

    ChrTalk(    #161
        0x106,
        (
            "#057FWhat the hell is this?\x02\x03",

            "I hear all about how you've 'improved,'\x01",
            "and when I show up you guys are\x01",
            "acting like THIS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#1749F#4PAh-hahaha! It was just a joke, man!\x01",
            "Totally a joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #163
        0x8,
        "#1743F#4PHey, wait, isn't that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #164
        0x9,
        "#1753F#2PThat's that newbie bracer chick, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#5P#1006FHey guys, been a while! We last\x01",
            "met at the tournament, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        "#1760F#4PYeah, sounds right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "#1756F#2POh, man! We watched you from the stands\x01",
            "after our fight, all the way to the finals!\x02\x03",

            "#1751FYou were incredible!\x01",
            "I've fallen for you all over again! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#5P#1016FAhaha... Umm, thanks?\x02\x03",

            "#1002FAnyway, we're here for a reason.\x01",
            "Guild business.\x02\x03",

            "Is the guy who saw a 'white shadow'\x01",
            "here today?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #169
        0x8,
        "#1742F#4PWhite shadow? You mean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #170
        0x9,
        "#1752F#4PYeah, they must mean that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#5P#1011FYou know what I'm talking about, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x106,
        (
            "#053FSo spit it out already.\x02\x03",

            "Stop wasting our time, it's valuable.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #173
        0xA,
        (
            "#1763F#4P...Wait just one damn minute.\x02\x03",

            "#1765FWhere do you get off, making\x01",
            "demands like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x106,
        "#052FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "#1764F#4PYou're pissin' me off.\x02\x03",

            "You abandon us, leave us in the dust,\x01",
            "to become a BRACER, of all things.\x01",
            "A fuggin' law-whore!\x02\x03",

            "#1760FAnd then you come back to us,\x01",
            "only when it's convenient for you,\x01",
            "and expect us to tell you whatever?\x02\x03",

            "Well, you can just piss right off!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #176
        0x8,
        "#1743F#6PYyyyyieee, Rocco...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x106,
        (
            "#051FHeh. You're a prideful son of a gun,\x01",
            "Rocco...same as ever.\x02\x03",

            "What d'you want me to do, then, huh?\x02\x03",

            "Get down on the ground and beg?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        "#1765F#4P...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #179
        0xA,
        (
            "#1760F#4PYou... You gotta fight us.\x01",
            "Here and now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #180
        0x8,
        "#1742F#6PWH-WH-WH-WHAT?! WHY?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #181
        0x9,
        "#1753F#4PDude, dude! Calm down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        (
            "#1767F#4PShut it! We need to settle this!\x02\x03",

            "#1763FYou win, we'll tell you what\x01",
            "you want to know.\x02\x03",

            "#1760FIf WE win...you don't get to act like\x01",
            "the puffed-up king fish no more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x106,
        "#051FHah, suits me just fine.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 18)
    SetChrSubChip(0x106, 0)
    Sleep(500)

    ChrTalk(    #184
        0x106,
        (
            "#053FLet's see just how tough you\x01",
            "guys have gotten...\x02\x03",

            "#054FAll right, you three, COME GET SOME!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)

    def lambda_4341():
        OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x1E46, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4341)
    WaitChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_4366():
        TurnDirection(0x8, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4366)

    def lambda_4374():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4374)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #185
        0x8,
        (
            "#1749F#6POh, man, oh, man, why'd things\x01",
            "turn out like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#1751F#2PBut hey, we get to fight Estelle again! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#5P#1016FI, uh, dunno if that's really the point here...\x02\x03",

            "#1018FOkay, then! Don't expect me to hold back!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Battle(0x79A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_44D3"),
        (SWITCH_DEFAULT, "loc_44D8"),
    )


    label("loc_44D3")

    OP_B4(0x0)
    Jump("loc_44D8")

    label("loc_44D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -1240, 0, 3520, 357)
    SetChrPos(0x106, -2620, 0, 3570, 359)
    SetChrPos(0xA, -2360, 0, 6360, 182)
    SetChrPos(0x9, -1110, 0, 7050, 195)
    SetChrPos(0x8, -3870, 0, 6790, 123)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 21)
    SetChrSubChip(0xA, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    OP_6D(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #188
        0x8,
        "#1748F#6PGuah, you guys ARE strong...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#1755F#4PI give, I give! If I had a white flag,\x01",
            "I'd be waving it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        "#1767F#4PDAMN it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x106,
        (
            "#051FHeh. Guess it wasn't TOTAL BS that\x01",
            "you guys were in the tournament.\x02\x03",

            "You still aren't putting enough into it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1006F#5PEven so, you guys are really good for\x01",
            "civilians. Like, really, really good!\x02\x03",

            "Why not stop wasting your time\x01",
            "here and become bracers?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #193
        0xA,
        "#1762F#4PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_99(0x8, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #194
        0x8,
        "#1743FB-Bracers? Us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#1753F#4PN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1011F#5PHey, the guild doesn't discriminate.\x01",
            "Agate became a bracer, and so did I,\x01",
            "and I started out as a clueless kid!\x02\x03",

            "You guys should be able to\x01",
            "do it, no problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #197
        0x106,
        (
            "#050F#5PDon't make promises you can't keep.\x02\x03",

            "A bracer's more than just hired muscle.\x01",
            "There's a lot of jobs that need more than\x01",
            "just mindless fighting.\x02\x03",

            "You should know that well\x01",
            "enough yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #198
        0x101,
        "#1015F#2PWell...yeah, but even so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        (
            "#1742FY-Yeah, that's right.\x02\x03",

            "#1749FFighting's just about the\x01",
            "only thing we're good at...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "#1754F#4PShoulda known nothin' would\x01",
            "be that simple...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "#1764F#4P...\x02\x03",

            "#1763FAnyway...a deal's a deal.\x02\x03",

            "#1760FI'll tell you what you want to know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xA, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #202
        0x106,
        "#051FAll right, let's hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#1002F#5PLike we said, we're looking for the\x01",
            "guy who saw a 'white shadow.'\x02\x03",

            "We heard that one of you saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "#1761F#4PYeah, someone did.\x02\x03",

            "He ain't here today, but you're\x01",
            "lookin' for Belden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x8,
        (
            "#1740FHe joined about a year ago--\x01",
            "long after Agate left.\x02\x03",

            "You might've seen him before,\x01",
            "though, Agate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x106,
        (
            "#552FOh, yeah, think I did.\x02\x03",

            "We talked a bit when I came\x01",
            "by on that last case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#1752F#4PBelden hasn't been by since seeing\x01",
            "that thing, actually.\x02\x03",

            "#1754FI heard a few people say he's stuck\x01",
            "in bed from the shock of seeing\x01",
            "a ghost.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #208
        0x101,
        (
            "#1020F#5PWHAT?!\x02\x03",

            "D-D-Do you mean he was cursed,\x01",
            "doomed to die, suffer forev--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "#1764F#4PUh. Dunno about THAT...but I do\x01",
            "know he was damn scared.\x02\x03",

            "#1760FHe's always been sort of a\x01",
            "spineless rich kid, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x106,
        (
            "#053FTch. So what's he doin' pretending to\x01",
            "be a punk if he's got a nice family?\x02\x03",

            "#050FAh, whatever. We'll hit him up for\x01",
            "details. Where's this kid live?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        (
            "#1740FIt's the big place to the right\x01",
            "of the mayor's mansion.\x02\x03",

            "Some old fart named Norman owns\x01",
            "the joint. Belden's his oldest son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1011F#5PTo the right of the mayor's mansion,\x01",
            "got it.\x02\x03",

            "#1001FThanks for your help, guys!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #213
        0x101,
        (
            "#1006F#2POkay, now we know where to go!\x01",
            "Let's go meet this 'Belden' dude.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #214
        0x106,
        "#051F#5PSounds good.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #215
        0x106,
        (
            "#051FSee you, guys. Don't get into any\x01",
            "crap just 'cause you're bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        "#1760F#4PAh, shaddup.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "#1741FYou guys keep it up! And stop\x01",
            "by again sometime! Hopefully\x01",
            "without beating us up next time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x9,
        "#1751F#4PKeep up the good work, Estelle! ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EDF")

    label("loc_515D")


    ChrTalk(    #219
        0x101,
        (
            "#2P*sigh* And here I was, just possibly\x01",
            "thinking better of you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_520B():
        OP_6D(-2500, 0, 4470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_520B)

    def lambda_5223():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5223)

    def lambda_523B():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_523B)

    def lambda_524B():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_524B)

    def lambda_525B():

        label("loc_525B")

        TurnDirection(0x8, 0x103, 400)
        OP_48()
        Jump("loc_525B")

    QueueWorkItem2(0x8, 1, lambda_525B)

    def lambda_526C():

        label("loc_526C")

        TurnDirection(0x9, 0x101, 400)
        OP_48()
        Jump("loc_526C")

    QueueWorkItem2(0x9, 1, lambda_526C)

    def lambda_527D():

        label("loc_527D")

        TurnDirection(0xA, 0x103, 400)
        OP_48()
        Jump("loc_527D")

    QueueWorkItem2(0xA, 1, lambda_527D)
    TurnDirection(0x13, 0x103, 800)
    TurnDirection(0x14, 0x103, 800)
    TurnDirection(0x15, 0x103, 800)
    Sleep(300)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #220
        0x8,
        "#1743FHuh? You're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#1753F#4PIt is!\x02\x03",

            "#1751FThat's that newbie bracer chick, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5317():

        label("loc_5317")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_5317")

    QueueWorkItem2(0x103, 1, lambda_5317)

    def lambda_5328():

        label("loc_5328")

        TurnDirection(0x103, 0xA, 0)
        OP_48()
        Jump("loc_5328")

    QueueWorkItem2(0x103, 2, lambda_5328)

    def lambda_5339():

        label("loc_5339")

        TurnDirection(0x13, 0x103, 0)
        OP_48()
        Jump("loc_5339")

    QueueWorkItem2(0x13, 0, lambda_5339)

    def lambda_534A():

        label("loc_534A")

        TurnDirection(0x14, 0x103, 0)
        OP_48()
        Jump("loc_534A")

    QueueWorkItem2(0x14, 0, lambda_534A)

    def lambda_535B():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_535B)
    Sleep(300)

    def lambda_537B():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0x12B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_537B)
    Sleep(500)

    def lambda_539B():
        OP_6D(-3350, 0, 7460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_539B)

    def lambda_53B3():
        OP_67(0, 8350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53B3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x103, 0x0)
    OP_44(0x103, 0x1)
    OP_44(0x103, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)

    ChrTalk(    #222
        0x101,
        (
            "#5P#1006FHey, guys, been a while!\x01",
            "We last met at the tournament, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xA,
        "#1760F#4PYeah, sounds right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x9,
        (
            "#1756F#2POh, man! We watched you from the stands\x01",
            "after our fight, all the way to the finals!\x02\x03",

            "#1751FYou were incredible!\x01",
            "I've fallen for you all over again! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#5P#1008FAhaha... Umm, thanks?\x02\x03",

            "#1007FMore importantly...what was that\x01",
            "I heard about 'Carna's gone, let's cut\x01",
            "loose'? And something about 'poker'?\x02\x03",

            "#1019FDo you realize what Agate would\x01",
            "do to you guys if he heard that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        (
            "#1749F#4PDaaaaah! It was just a joke, really!\x02\x03",

            "#1742FPlease don't tell him! Please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xA,
        "#1765F#4PPfft. I ain't scared of him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x9,
        (
            "#1753F#2PUh, anyway!\x02\x03",

            "#1750FWho's the lovely lady with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        (
            "#5P#1011FThis is Schera. She's a bracer,\x01",
            "like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x103,
        (
            "#021FHello. I'm Scherazard Harvey.\x02\x03",

            "I'm a friend of Agate's, by the by.\x02\x03",

            "#027FNice to meet you, bad boys. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #231
        0x8,
        "#1743F#4P*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        "#1762F#4PUh, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        "#1753F#2PShe's kinda hot...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #234
        0x101,
        (
            "#2P#1019FUh, Schera, please don't flirt with\x01",
            "the criminal element.\x02\x03",

            "They don't need to be hit over\x01",
            "the head with how, er, bad their \x01",
            "lady situation is, for starters.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #235
        0x103,
        (
            "#021F#5POh, don't worry.\x01",
            "I'm just breaking the ice a little.\x02\x03",

            "#027FNow, then, I believe we have a\x01",
            "question for these fine young men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#1004F#2PAh, right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(    #237
        0x101,
        (
            "#1002F#5PAnyway, yeah, we're here today\x01",
            "on guild business.\x02\x03",

            "Is the guy who saw a 'white shadow'\x01",
            "here today?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #238
        0x8,
        "#1742F#4PWhite shadow? You mean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #239
        0x9,
        "#1752F#4PYeah, they must mean that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1011F#5PYou know what I'm talking about, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x103,
        (
            "#020FCould you tell us, if it isn't\x01",
            "too much trouble?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)
    TurnDirection(0x9, 0xA, 400)
    OP_8C(0xA, 0, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #242
        0x8,
        "#1741F#6PWhat do you think, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xA,
        "#1761F#6PHell yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        "#1751F#4PThis is gonna be SWEET!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #245
        0x101,
        "#1015F#5P(What're they mumbling about?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0xA, 0x103, 400)
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #246
        0x8,
        "#1740F#4PSure, we'll tell you, but on one condition.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        "#1756F#2PIf you're OK with that, we'll talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#1019F#5PAnd what, precisely, would that condition be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x103,
        (
            "#025F(Whoops! I may have gone\x01",
            "a tad overboard...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "#1761F#4PHeh, as if you can't figure it out.\x02\x03",

            "Isn't it obvious?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)

    def lambda_5D29():
        OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x1E46, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_5D29)
    WaitChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_5D4E():
        TurnDirection(0x8, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D4E)

    def lambda_5D5C():
        TurnDirection(0x9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D5C)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #251
        0x8,
        (
            "#1741F#6PWe want you to fight us!\x02\x03",

            "We're gonna get some revenge\x01",
            "for our loss at the tournament!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x103,
        "#1P#023FPARDON?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "#1751F#2PJust so you know, we've gotten\x01",
            "a lot stronger since then!\x02\x03",

            "#1756FAnd this time it's three on two--\x01",
            "we're not gonna lose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#5P#1006FOh, that's all?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #255
        0x101,
        (
            "#1018F#5PWell, I'll never turn down an offer\x01",
            "to spar! You up for it, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x103,
        (
            "#023FNo, I don't mind...\x01",
            "It's just not quite what I expected...\x02\x03",

            "#027FBut, then...no need to hold back,\x01",
            "in that case.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 17)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x103, 23)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_5FE0():
        OP_99(0x103, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5FE0)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6007():
        OP_96(0xA, 0xFFFFF466, 0x0, 0x1D4C, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6007)
    WaitChrThread(0x103, 0x0)

    def lambda_602A():
        OP_99(0x103, 0x7, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_602A)
    WaitChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 17)
    SetChrSubChip(0x103, 0)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #257
        0x8,
        "#1743F#1P#1KWHOOOOOA!\x02",
    )


    ChrTalk(    #258
        0xA,
        "#1762F#2P#1KA WHIP?!\x02",
    )


    ChrTalk(    #259
        0x9,
        "#1753F#4P#1KGotta be KIDDING me...!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #260
        0x103,
        (
            "#021FWell, come on, boys.\x02\x03",

            "Big Sis will show you how\x01",
            "the adults play.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #261
        0x8,
        "#1749F#6PEr, you see yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xA,
        (
            "#1762F#4PWell, wait a minute...\x01",
            "Picking a fight with a pair of girls...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "#1755F#2PWe'd be, uh, unmanly bullies\x01",
            "if we did that! Right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x103,
        (
            "#021FOh, come on, boys!\x02\x03",

            "#027FIt'll only be your spines!\x01",
            "I'm sure they'll grow back. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0xA, 0xFF)
    Battle(0x79A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_627B"),
        (SWITCH_DEFAULT, "loc_6280"),
    )


    label("loc_627B")

    OP_B4(0x0)
    Jump("loc_6280")

    label("loc_6280")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -1240, 0, 3520, 357)
    SetChrPos(0x103, -2620, 0, 3570, 359)
    SetChrPos(0xA, -2360, 0, 6360, 182)
    SetChrPos(0x9, -1110, 0, 7050, 195)
    SetChrPos(0x8, -3870, 0, 6790, 123)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0xA, 21)
    SetChrSubChip(0xA, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    OP_6D(-2650, 0, 5850, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #265
        0x8,
        "#1749F#6PMy spiiiiiine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        "#1755F#4PAll my OTHER bones!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xA,
        "#1764F#4PHow could we lose like that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x103,
        (
            "#023FAww, we done already?\x02\x03",

            "#021FKids these days get tired so easily.\x01",
            "You could've given me all you've got,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1007F#5PSchera, NOBODY has enough energy\x01",
            "to keep up with you.\x02\x03",

            "#1006FEven so, seems like you guys have\x01",
            "kept up with your training since the\x01",
            "tournament, yeah?\x02\x03",

            "Why not stop wasting your time\x01",
            "here and become bracers?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #270
        0xA,
        "#1762F#4PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_99(0x8, 0x3, 0x1, 0x3E8)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #271
        0x8,
        "#1743FB-Bracers? Us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x9,
        "#1753F#4PN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        (
            "#1011F#5PHey, the guild doesn't discriminate.\x01",
            "Agate became a bracer, and so did I,\x01",
            "and I started out as a clueless kid!\x02\x03",

            "You guys should be able\x01",
            "to do it, no problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #274
        0x103,
        (
            "#020F#5PMmm. In a straight fight, they could\x01",
            "match a junior bracer, certainly.\x02\x03",

            "Being a bracer involves far more than\x01",
            "just violence, though, Estelle.\x02\x03",

            "I wouldn't make promises like\x01",
            "that quite so quickly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #275
        0x101,
        "#1015F#2PYou think so? But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "#1742FY-Yeah, that's right.\x02\x03",

            "#1749FFighting's just about the\x01",
            "only thing we're good at...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x9,
        "#1754F#4PShoulda known nothin' would be that simple...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xA,
        (
            "#1764F#4P...\x02\x03",

            "#1763FAnyway...a deal's a deal.\x02\x03",

            "#1760FWe'll tell you what you want to know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #279
        0x103,
        "#021FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1002F#5PLike we said, we're looking for the\x01",
            "guy who saw a 'white shadow.'\x02\x03",

            "We heard that one of you saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xA,
        (
            "#1761F#4PYeah, someone did.\x02\x03",

            "He ain't here today, but you're\x01",
            "lookin' for Belden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        (
            "#1740FHe's our newest member, joined a year ago.\x02\x03",

            "I think you might've seen him before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1015F#5PUh, I wasn't quite paying that\x01",
            "much attention to you guys.\x02\x03",

            "I do kinda remember another guy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x9,
        (
            "#1752F#4PBelden hasn't been by since\x01",
            "seeing that thing, actually.\x02\x03",

            "#1754FI heard a few people say he's\x01",
            "stuck in bed from the shock\x01",
            "of seeing a ghost.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #285
        0x101,
        (
            "#1020F#5PWHAT?!\x02\x03",

            "D-D-Do you mean he was cursed,\x01",
            "doomed to die, suffer forev--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xA,
        (
            "#1764F#4PUh. Dunno about THAT...\x01",
            "but I do know he was damn scared.\x02\x03",

            "#1760FHe's always been sort of a\x01",
            "spineless rich kid, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x103,
        (
            "#026FAn odd fit for the life of a thug, then.\x02\x03",

            "#020FWe can get the details from\x01",
            "him. Where does he live?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#1740FIt's the big place to the right\x01",
            "of the mayor's mansion.\x02\x03",

            "Some old fart named Norman owns\x01",
            "the joint. Belden's his oldest son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1011F#5PTo the right of the mayor's mansion,\x01",
            "got it.\x02\x03",

            "#1001FThanks for your help, guys!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #290
        0x101,
        (
            "#1006F#2POkay, now we know where to go!\x01",
            "Let's go meet this 'Belden' dude.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #291
        0x103,
        "#020F#5PLet's.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #292
        0x103,
        (
            "#021FThanks again, little bad boys.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        "#1760F#4PUh, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#1741FYou guys keep it up!\x01",
            "And stop by again sometime!\x01",
            "Hopefully without beating us up next time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x9,
        "#1751F#4PKeep up the good work, Estelle! ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_6EDF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -4150, 0, 9070, 90)
    SetChrPos(0x9, -1590, 0, 7520, 322)
    SetChrPos(0xA, -2970, 0, 7390, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_8C(0x13, 280, 0)
    OP_8C(0x14, 80, 0)
    OP_8C(0x15, 303, 0)
    OP_8C(0x16, 90, 0)
    OP_8C(0x17, 0, 0)
    OP_6D(-3460, 0, 3720, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -3460, 0, 3720, 0)
    SetChrPos(0xF7, -3460, 0, 3720, 0)
    OP_6A(0x0)
    OP_A2(0x120E)
    OP_28(0x82, 0x2, 0x10)
    OP_28(0x82, 0x1, 0x20)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_20_32CA end

    def Function_21_7005(): pass

    label("Function_21_7005")

    ClearChrFlags(0xFE, 0x8)
    OP_8E(0xFE, 0xFFFFE656, 0x0, 0xED8, 0x1770, 0x0)
    Return()

    # Function_21_7005 end

    def Function_22_701F(): pass

    label("Function_22_701F")

    OP_8E(0xFE, 0xFFFFE110, 0x0, 0xB22, 0x1770, 0x0)
    Return()

    # Function_22_701F end

    def Function_23_7034(): pass

    label("Function_23_7034")

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
        (0, "loc_70AD"),
        (1, "loc_70B3"),
        (SWITCH_DEFAULT, "loc_70B9"),
    )


    label("loc_70AD")

    OP_A2(0x1200)
    Jump("loc_70B9")

    label("loc_70B3")

    OP_A2(0x1201)
    Jump("loc_70B9")

    label("loc_70B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_70C7")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_70CB")

    label("loc_70C7")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_70CB")

    Return()

    # Function_23_7034 end

    SaveToFile()

Try(main)
