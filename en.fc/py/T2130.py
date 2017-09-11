from ED6ScenarioHelper import *

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
            'ED6_DT01/T2130   ._SN',
            'ED6_DT01/T2130_1 ._SN',
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
        'Bargo',                                # 12
        'Terence',                              # 13
        'Jabu',                                 # 14
        'Clem',                                 # 15
        'Matron Theresa',                       # 16
        'Agate',                                # 17
        'Jimmy',                                # 18
        'Camera',                               # 19
        'Father Theodore',                      # 20
        'Sister Frieda',                        # 21
        'Rutherford',                           # 22
        'Randall',                              # 23
        'Muriel',                               # 24
        'Seagaro',                              # 25
        'Edel',                                 # 26
        'Belden',                               # 27
        'Burt',                                 # 28
        'Bargo',                                # 29
        'Terence',                              # 30
        'Jabu',                                 # 31
        'Picaro',                               # 32
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
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02570 ._CH',             # 02
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00370 ._CH',             # 04
        'ED6_DT07/CH00371 ._CH',             # 05
        'ED6_DT07/CH00373 ._CH',             # 06
        'ED6_DT07/CH00374 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00110 ._CH',             # 09
        'ED6_DT07/CH00140 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00111 ._CH',             # 0C
        'ED6_DT07/CH01040 ._CH',             # 0D
        'ED6_DT07/CH01670 ._CH',             # 0E
        'ED6_DT07/CH01410 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01003 ._CH',             # 11
        'ED6_DT07/CH01053 ._CH',             # 12
        'ED6_DT07/CH01043 ._CH',             # 13
        'ED6_DT07/CH01213 ._CH',             # 14
        'ED6_DT07/CH02510 ._CH',             # 15
        'ED6_DT07/CH02520 ._CH',             # 16
        'ED6_DT07/CH02530 ._CH',             # 17
        'ED6_DT07/CH00450 ._CH',             # 18
        'ED6_DT07/CH00451 ._CH',             # 19
        'ED6_DT07/CH00453 ._CH',             # 1A
        'ED6_DT07/CH00454 ._CH',             # 1B
        'ED6_DT07/CH00460 ._CH',             # 1C
        'ED6_DT07/CH00461 ._CH',             # 1D
        'ED6_DT07/CH00463 ._CH',             # 1E
        'ED6_DT07/CH00464 ._CH',             # 1F
        'ED6_DT07/CH00470 ._CH',             # 20
        'ED6_DT07/CH00471 ._CH',             # 21
        'ED6_DT07/CH00473 ._CH',             # 22
        'ED6_DT07/CH00474 ._CH',             # 23
        'ED6_DT06/CH20058 ._CH',             # 24
        'ED6_DT07/CH00051 ._CH',             # 25
        'ED6_DT07/CH01393 ._CH',             # 26
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02570P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00370P._CP',             # 04
        'ED6_DT07/CH00371P._CP',             # 05
        'ED6_DT07/CH00373P._CP',             # 06
        'ED6_DT07/CH00374P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00110P._CP',             # 09
        'ED6_DT07/CH00140P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00111P._CP',             # 0C
        'ED6_DT07/CH01040P._CP',             # 0D
        'ED6_DT07/CH01670P._CP',             # 0E
        'ED6_DT07/CH01410P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01003P._CP',             # 11
        'ED6_DT07/CH01053P._CP',             # 12
        'ED6_DT07/CH01043P._CP',             # 13
        'ED6_DT07/CH01213P._CP',             # 14
        'ED6_DT07/CH02510P._CP',             # 15
        'ED6_DT07/CH02520P._CP',             # 16
        'ED6_DT07/CH02530P._CP',             # 17
        'ED6_DT07/CH00450P._CP',             # 18
        'ED6_DT07/CH00451P._CP',             # 19
        'ED6_DT07/CH00453P._CP',             # 1A
        'ED6_DT07/CH00454P._CP',             # 1B
        'ED6_DT07/CH00460P._CP',             # 1C
        'ED6_DT07/CH00461P._CP',             # 1D
        'ED6_DT07/CH00463P._CP',             # 1E
        'ED6_DT07/CH00464P._CP',             # 1F
        'ED6_DT07/CH00470P._CP',             # 20
        'ED6_DT07/CH00471P._CP',             # 21
        'ED6_DT07/CH00473P._CP',             # 22
        'ED6_DT07/CH00474P._CP',             # 23
        'ED6_DT06/CH20058P._CP',             # 24
        'ED6_DT07/CH00051P._CP',             # 25
        'ED6_DT07/CH01393P._CP',             # 26
    )

    DeclNpc(
        X                   = -4150,
        Z                   = 0,
        Y                   = 9070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -4950,
        Z                   = 0,
        Y                   = 4460,
        Direction           = 120,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 7390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
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
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
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
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
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
        X                   = -6030,
        Z                   = 0,
        Y                   = 4040,
        Direction           = 270,
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
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
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
        X                   = 53000,
        Z                   = 0,
        Y                   = 48100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 53000,
        Z                   = 0,
        Y                   = 33500,
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
        X                   = 58900,
        Z                   = 1000,
        Y                   = 52200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 54400,
        Z                   = 0,
        Y                   = 50000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 56580,
        Z                   = 0,
        Y                   = 42980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55130,
        Z                   = 0,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 56110,
        Z                   = 0,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 61600,
        Z                   = 0,
        Y                   = 45930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 62560,
        Z                   = 0,
        Y                   = 45930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -11800,
        Z                   = 250,
        Y                   = 4070,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -11600,
        Z                   = 250,
        Y                   = 1950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 350,
        Z                   = 0,
        Y                   = 1410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -13330,
        Z                   = 600,
        Y                   = 6230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -7720,
        Z                   = 0,
        Y                   = 10340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )


    DeclActor(
        TriggerX            = 58980,
        TriggerZ            = 1000,
        TriggerY            = 50440,
        TriggerRange        = 400,
        ActorX              = 58900,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_506",          # 00, 0
        "Function_1_6DA",          # 01, 1
        "Function_2_705",          # 02, 2
        "Function_3_71B",          # 03, 3
        "Function_4_73F",          # 04, 4
        "Function_5_10F3",         # 05, 5
        "Function_6_15C8",         # 06, 6
        "Function_7_15FA",         # 07, 7
        "Function_8_1626",         # 08, 8
        "Function_9_167F",         # 09, 9
        "Function_10_16F5",        # 0A, 10
        "Function_11_177F",        # 0B, 11
        "Function_12_1989",        # 0C, 12
        "Function_13_1B92",        # 0D, 13
        "Function_14_1DA5",        # 0E, 14
        "Function_15_208C",        # 0F, 15
        "Function_16_223F",        # 10, 16
        "Function_17_2501",        # 11, 17
        "Function_18_2817",        # 12, 18
        "Function_19_2A14",        # 13, 19
        "Function_20_2C34",        # 14, 20
    )


    def Function_0_506(): pass

    label("Function_0_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_521")
    SetChrPos(0x14, 62350, 0, 48350, 180)
    Jump("loc_67F")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_569")
    SetChrPos(0x14, 62350, 0, 48350, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    Jump("loc_67F")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_584")
    SetChrPos(0x14, -17370, 0, 42870, 270)
    Jump("loc_67F")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_END)), "loc_59F")
    SetChrPos(0x14, 14600, 0, 44890, 270)
    Jump("loc_67F")

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5E7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrPos(0x14, 14600, 0, 44890, 270)
    Jump("loc_67F")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_67F")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_67F")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_61E")
    Jump("loc_67F")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_67F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8)

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A1")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_6B7")

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B7")
    ClearChrFlags(0x11, 0x80)

    label("loc_6B7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_6C3"),
        (SWITCH_DEFAULT, "loc_6D9"),
    )


    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
    OP_A2(0x42C)
    Event(0, 20)

    label("loc_6D6")

    Jump("loc_6D9")

    label("loc_6D9")

    Return()

    # Function_0_506 end

    def Function_1_6DA(): pass

    label("Function_1_6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FB")
    OP_B1("t2130_y")
    Jump("loc_704")

    label("loc_6FB")

    OP_B1("t2130_n")

    label("loc_704")

    Return()

    # Function_1_6DA end

    def Function_2_705(): pass

    label("Function_2_705")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_705")

    label("loc_71A")

    Return()

    # Function_2_705 end

    def Function_3_71B(): pass

    label("Function_3_71B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73E")
    OP_8D(0xFE, -8060, 7500, -1360, 2009, 1500)
    Jump("Function_3_71B")

    label("loc_73E")

    Return()

    # Function_3_71B end

    def Function_4_73F(): pass

    label("Function_4_73F")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")
    OP_A2(0x1)

    ChrTalk(    #0
        0x13,
        (
            "So the love of money claimed\x01",
            "the mayor, as it has done with\x01",
            "so many others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x13,
        (
            "Care must be taken to ensure\x01",
            "that the region does not fall\x01",
            "into chaos and disorder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "Almighty Aidios...please, grant\x01",
            "us your guidance and wisdom...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F3")

    label("loc_847")


    ChrTalk(    #3
        0x13,
        (
            "So the love of money claimed\x01",
            "the mayor, as it has done with\x01",
            "so many others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x13,
        (
            "Care must be taken to ensure\x01",
            "that the region does not fall\x01",
            "into chaos and disorder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F3")

    Jump("loc_10EF")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_952")

    ChrTalk(    #5
        0x13,
        (
            "The mayor has been so busy\x01",
            "that he hasn't even had time\x01",
            "to appear at church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EF")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    OP_A2(0x1)

    ChrTalk(    #6
        0x13,
        (
            "I pray that all will receive the\x01",
            "blessing of Aidios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "Whew. The day's finally over.\x01",
            "And as usual, the congregation\x01",
            "was packed full with tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x13,
        (
            "The mayor seems quite happy,\x01",
            "but I can't shake the feeling\x01",
            "that something isn't right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B03")

    label("loc_A62")


    ChrTalk(    #9
        0x13,
        (
            "As usual, today's congregation\x01",
            "was packed full with tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x13,
        (
            "The mayor seems quite happy,\x01",
            "but I can't shake the feeling\x01",
            "that something isn't right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B03")

    Jump("loc_10EF")

    label("loc_B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_CE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83")
    OP_A2(0x1)

    ChrTalk(    #11
        0x13,
        (
            "Orbments have made the modern\x01",
            "world a more convenient place\x01",
            "in which to live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x13,
        (
            "The invention of the airship,\x01",
            "however, has all but negated\x01",
            "the usefulness of Ruan's harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x13,
        (
            "The world seems to be leaving\x01",
            "the Septian church behind in\x01",
            "similar fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "I should hope that the people \x01",
            "of Ruan, at least, would not\x01",
            "forget their faith in Aidios...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4")

    label("loc_C83")


    ChrTalk(    #15
        0x13,
        (
            "I should hope that the people \x01",
            "of Ruan, at least, would not\x01",
            "forget their faith in Aidios...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE4")

    Jump("loc_10EF")

    label("loc_CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDC")
    OP_A2(0x1)

    ChrTalk(    #16
        0x13,
        (
            "I tend to see more tourists than\x01",
            "local folk in my congregation\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x13,
        (
            "Some of them have the most\x01",
            "atrocious manners. Even during\x01",
            "Mass, they will not keep quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13,
        (
            "They can be quite trying on\x01",
            "one's patience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_DDC")


    ChrTalk(    #19
        0x13,
        (
            "I tend to see more tourists than\x01",
            "local folk in my congregation\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x13,
        (
            "Some of them have the most \x01",
            "atrocious manners. They can be\x01",
            "quite trying on one's patience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8C")

    Jump("loc_10EF")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(    #21
        0x13,
        (
            "Ahhh... I hope that today's\x01",
            "Mass will be a relatively\x01",
            "peaceful affair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EF")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_F32")

    ChrTalk(    #22
        0x13,
        (
            "Ideally, they will all follow the\x01",
            "prayer as they're meant to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EF")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_10EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1027")
    OP_A2(0x1)

    ChrTalk(    #23
        0x13,
        (
            "Long ago, this area was populated\x01",
            "mainly by men waiting to go off\x01",
            "to sea. True louts, all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        (
            "A magazine article described our\x01",
            "'seaside church' as being nothing\x01",
            "more than a tourist attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        "So very strange...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10EF")

    label("loc_1027")


    ChrTalk(    #26
        0x13,
        (
            "Long ago, this area was populated\x01",
            "mainly by men waiting to go off\x01",
            "to sea. True louts, all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x13,
        (
            "A magazine article described our\x01",
            "'seaside church' as being nothing\x01",
            "more than a tourist attraction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EF")

    TalkEnd(0x13)
    Return()

    # Function_4_73F end

    def Function_5_10F3(): pass

    label("Function_5_10F3")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CC")
    OP_A2(0x2)

    ChrTalk(    #28
        0xFE,
        (
            "It's heartbreaking that children\x01",
            "should be drawn into such\x01",
            "terrible events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "The head of our church is\x01",
            "planning to visit the children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I intend to go with him,\x01",
            "if he'll allow me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123C")

    label("loc_11CC")


    ChrTalk(    #31
        0xFE,
        (
            "The head of our church is\x01",
            "planning to visit the children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I intend to go with him,\x01",
            "if he'll allow me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123C")

    Jump("loc_15C4")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_12C2")

    ChrTalk(    #33
        0xFE,
        (
            "The people living in Ruan seem\x01",
            "to be quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I think that may be the sole\x01",
            "reason that Ruan still survives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_132F")

    ChrTalk(    #35
        0xFE,
        (
            "Today's evening Mass was\x01",
            "a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "The head of the church seems\x01",
            "to be a little tired...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1383")

    ChrTalk(    #37
        0xFE,
        (
            "He can seem a little on the\x01",
            "crass side, but he is rich\x01",
            "in his faith.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1405")

    ChrTalk(    #38
        0xFE,
        "Ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I don't think that Father Theodore\x01",
            "cares much for the church being\x01",
            "turned into a tourist attraction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_1405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1461")

    ChrTalk(    #40
        0xFE,
        "Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "The morning Mass starts soon. \x01",
            "Will you be participating?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_1461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_14EB")

    ChrTalk(    #42
        0xFE,
        "Evening Mass is currently in progress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Around now is when tourists\x01",
            "come to see the sunset light\x01",
            "up the stained glass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_14EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(    #44
        0xFE,
        (
            "When the sun sets in the evening, the light\x01",
            "comes in from over the water and through\x01",
            "the stained glass. It's quite beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "And since the building itself is so\x01",
            "pretty, it's very popular with women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C4")

    TalkEnd(0x14)
    Return()

    # Function_5_10F3 end

    def Function_6_15C8(): pass

    label("Function_6_15C8")

    TalkBegin(0x15)

    ChrTalk(    #46
        0xFE,
        "Ha ha...well, would you look at that?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_6_15C8 end

    def Function_7_15FA(): pass

    label("Function_7_15FA")

    TalkBegin(0x16)

    ChrTalk(    #47
        0xFE,
        "Well, now...that is impressive.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_7_15FA end

    def Function_8_1626(): pass

    label("Function_8_1626")

    TalkBegin(0x17)

    ChrTalk(    #48
        0xFE,
        "Wow! Lookie, lookie, Grampa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "It's so pretty...just like the\x01",
            "guide said!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_8_1626 end

    def Function_9_167F(): pass

    label("Function_9_167F")

    TalkBegin(0x18)

    ChrTalk(    #50
        0xFE,
        "And the pilgrimage ends safely...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "My wife and I managed to\x01",
            "agree on what sights we\x01",
            "wanted to go see.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_9_167F end

    def Function_10_16F5(): pass

    label("Function_10_16F5")

    TalkBegin(0x19)

    ChrTalk(    #52
        0xFE,
        (
            "You can see all the sunlight \x01",
            "reflecting off the water and in\x01",
            "through the stained glass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "It's unbelievably stunning...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_10_16F5 end

    def Function_11_177F(): pass

    label("Function_11_177F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_183C")

    ChrTalk(    #54
        0xFE,
        (
            "I can't believe we got controlled by the\x01",
            "mayor like that. All those things he made\x01",
            "us do... Like friggin' puppets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "And by HIM, of all people...\x01",
            "How pathetic is that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1985")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_18A5")

    ChrTalk(    #56
        0xFE,
        "Agate's back in Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Well, crap. I have to be on my\x01",
            "best behavior when he's around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1985")

    label("loc_18A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(    #58
        0xFE,
        "Owwww...just as strong as ever...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Agate's back in Ruan?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1985")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(    #60
        0xFE,
        (
            "Damn...I think I drank too much\x01",
            "last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "My head's pounding, fit to burst.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1985")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1985")

    ChrTalk(    #62
        0xFE,
        (
            "Wha...? What are you guys\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1985")

    TalkEnd(0x8)
    Return()

    # Function_11_177F end

    def Function_12_1989(): pass

    label("Function_12_1989")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A42")

    ChrTalk(    #63
        0xFE,
        (
            "Heh...no need to get all pissy\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "It's not like that soldier chick\x01",
            "isn't already riding my ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I guess it's my famous luck\x01",
            "with women at work again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1AF1")

    ChrTalk(    #66
        0xFE,
        (
            "Owww...why'd he have\x01",
            "to hit me like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I think he got stronger when he\x01",
            "became a bracer, or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I guess I'd better just\x01",
            "lie low for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1B14")

    ChrTalk(    #69
        0xFE,
        "Oh, what's the use?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1B60")

    ChrTalk(    #70
        0x9,
        (
            "HAAAAAA ha ha ha!\x01",
            "I ain't drinkin' that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "*hic*...oof...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1B8E")

    ChrTalk(    #72
        0xFE,
        "...Whaddyoo think yer lookin' at?\x02",
    )

    CloseMessageWindow()

    label("loc_1B8E")

    TalkEnd(0x9)
    Return()

    # Function_12_1989 end

    def Function_13_1B92(): pass

    label("Function_13_1B92")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C1F")

    ChrTalk(    #73
        0xFE,
        (
            "If they spot you, you'll get\x01",
            "locked up in a naval airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "This girl in a blue and white\x01",
            "uniform told me so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA1")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1CA5")

    ChrTalk(    #76
        0xFE,
        (
            "Oh...oh, crap...\x01",
            "Don't tell me he's back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I seriously thought he was\x01",
            "gonna kill me. That is one\x01",
            "intense dude...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA1")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1CFC")

    ChrTalk(    #78
        0xFE,
        (
            "Whoa, whoa, whoa, don't\x01",
            "tell me he's back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "I didn't hear anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA1")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1D4C")

    ChrTalk(    #80
        0xFE,
        (
            "What's with you? You change\x01",
            "your mind about hanging out\x01",
            "with us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA1")

    label("loc_1D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_1DA1")

    ChrTalk(    #81
        0xFE,
        (
            "Bah. And what would a high-\x01",
            "and-mighty bracer want in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA1")

    TalkEnd(0xA)
    Return()

    # Function_13_1B92 end

    def Function_14_1DA5(): pass

    label("Function_14_1DA5")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DF3")

    ChrTalk(    #82
        0xFE,
        "Ouchiewawa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "See this cut?\x01",
            "That's from Agate's sword.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2088")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1EE8")

    ChrTalk(    #84
        0xFE,
        (
            "I'd heard stories, but that was\x01",
            "the first time I'd ever actually\x01",
            "met Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "He's just got a hell of a temper.\x01",
            "Maybe that bandanna o' his is a\x01",
            "little too tight, ya know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "He sure scared the crap\x01",
            "outta Deen and the others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2088")

    label("loc_1EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(    #87
        0xFE,
        (
            "I'd heard stories, but that was\x01",
            "the first time I'd ever actually\x01",
            "met Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2088")

    label("loc_1F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2037")
    OP_A2(0x9)

    ChrTalk(    #88
        0xFE,
        "I don't wanna go home...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "My folks are gonna be waiting\x01",
            "for me, and you know their\x01",
            "favorite hobby? Giving me crap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "In fact, scratch that...I ain't\x01",
            "got a soul waiting for me. They've\x01",
            "given up by now, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205E")

    label("loc_2037")


    ChrTalk(    #91
        0xFE,
        (
            "I'm comfortable right where\x01",
            "I am.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205E")

    Jump("loc_2088")

    label("loc_2061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2088")

    ChrTalk(    #92
        0xFE,
        "Adults are so damn boring.\x02",
    )

    CloseMessageWindow()

    label("loc_2088")

    TalkEnd(0x1A)
    Return()

    # Function_14_1DA5 end

    def Function_15_208C(): pass

    label("Function_15_208C")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20FD")

    ChrTalk(    #93
        0xFE,
        (
            "Gilbert was taken away in a different airship\x01",
            "from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "I wonder where they're taking him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_223B")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_219E")

    ChrTalk(    #95
        0xFE,
        "He's just as scary as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Agate's always been a real\x01",
            "hard-ass, but we respect him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "The Ravens just ain't been\x01",
            "the same since he left.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223B")

    label("loc_219E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_21C9")

    ChrTalk(    #98
        0xFE,
        "He's just as scary as ever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_223B")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_21F8")

    ChrTalk(    #99
        0xFE,
        "Yo...find anything interesting?\x02",
    )

    CloseMessageWindow()
    Jump("loc_223B")

    label("loc_21F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_223B")

    ChrTalk(    #100
        0xFE,
        (
            "Man, this is so dull. I've had\x01",
            "more fun wiping my ass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223B")

    TalkEnd(0x1B)
    Return()

    # Function_15_208C end

    def Function_16_223F(): pass

    label("Function_16_223F")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_233C")

    ChrTalk(    #101
        0xFE,
        (
            "Rais challenged this chick with\x01",
            "a military haircut to a duel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "But you shoulda seen it. She\x01",
            "beat him down so fast, he\x01",
            "barely knew what hit him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "We've seen a lot of cute chicks\x01",
            "lately, but do they all have to\x01",
            "be such badasses?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_233C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_23C6")

    ChrTalk(    #104
        0xFE,
        (
            "You ever eat chocolate cigarettes?\x01",
            "They're my favorite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I like to think I'm pretty tough,\x01",
            "but I got nothing on Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_23C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2411")

    ChrTalk(    #106
        0xFE,
        (
            "I like to think I'm pretty tough,\x01",
            "but I got nothing on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_2411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2492")

    ChrTalk(    #107
        0xFE,
        (
            "Yesterday, I managed to snag a\x01",
            "salmon from a fishing boat.\x01",
            "Easy pickings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Yeah, you know I'm a\x01",
            "total badass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FD")

    label("loc_2492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_24FD")

    ChrTalk(    #109
        0xFE,
        (
            "I found a mira on the side of\x01",
            "the road today, so I took it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Heh heh...I'm so slick. Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_24FD")

    TalkEnd(0x1C)
    Return()

    # Function_16_223F end

    def Function_17_2501(): pass

    label("Function_17_2501")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2580")

    ChrTalk(    #111
        0xFE,
        (
            "I could've sworn that Gilbert\x01",
            "was coming here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "We can't remember a damn\x01",
            "thing about this whole to-do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2813")

    label("loc_2580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2679")

    ChrTalk(    #113
        0xFE,
        (
            "If Agate comes and we find out\x01",
            "about it, we're getting the hell\x01",
            "out of the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "He kinda stands out in a\x01",
            "crowd, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "With that huge sword and the\x01",
            "red hair, we'll hear about it\x01",
            "if he shows up around town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2813")

    label("loc_2679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_271E")

    ChrTalk(    #116
        0xFE,
        (
            "If Agate comes and we find out\x01",
            "about it, we're getting the hell\x01",
            "out of the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "In this world, you've gotta be\x01",
            "prepared to fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2813")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_27A7")

    ChrTalk(    #118
        0xFE,
        (
            "If you've got no ambition, this is\x01",
            "where you'll be sent, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "We've really screwed up\x01",
            "our lives, haven't we...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2813")

    label("loc_27A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2813")

    ChrTalk(    #120
        0xFE,
        "I hate manual labor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I swear, if they try to make me do\x01",
            "any real work, I am SO outta here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2813")

    TalkEnd(0x1D)
    Return()

    # Function_17_2501 end

    def Function_18_2817(): pass

    label("Function_18_2817")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_285A")

    ChrTalk(    #122
        0xFE,
        (
            "Looks like the mayor was\x01",
            "nastier than any of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_285A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_28C9")

    ChrTalk(    #123
        0xFE,
        (
            "So that's Agate, huh? He \x01",
            "scared the hell out of me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "He really is the genuine article...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2929")

    ChrTalk(    #125
        0xFE,
        "Whoa...so that's Agate, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "He's pretty slick.\x01",
            "Bet he gets all the ladies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2995")

    ChrTalk(    #127
        0xFE,
        (
            "Man...there's no place fun\x01",
            "around here to get some mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "I mean, the casino's closed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A10")

    label("loc_2995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2A10")

    ChrTalk(    #129
        0xFE,
        "*siiiigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "Honest work ain't for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I was driven out of my home...\x01",
            "and before I knew it, here I was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A10")

    TalkEnd(0x1E)
    Return()

    # Function_18_2817 end

    def Function_19_2A14(): pass

    label("Function_19_2A14")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2AA9")

    ChrTalk(    #132
        0xFE,
        "Brrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "If Agate finds out about this, he's gonna\x01",
            "start hitting us again. I don't think my\x01",
            "head can take any more trauma...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(    #134
        0xFE,
        "Brrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I can never relax when I know\x01",
            "that Agate's around...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2B68")

    ChrTalk(    #136
        0xFE,
        "Brrrrr...*chatter chatter*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Whenever I get scared, my legs\x01",
            "kinda don't wanna hold me up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_2BBA")

    ChrTalk(    #138
        0xFE,
        (
            "*sigh* If I said I wanted to\x01",
            "quit the Ravens, he'd be\x01",
            "so pissed...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C30")

    label("loc_2BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_2C30")

    ChrTalk(    #139
        0xFE,
        (
            "*sigh* What am I even\x01",
            "doin' here?\x02\x03",

            "It's not like you get the\x01",
            "option of refusing if you\x01",
            "get asked to join.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C30")

    TalkEnd(0x1F)
    Return()

    # Function_19_2A14 end

    def Function_20_2C34(): pass

    label("Function_20_2C34")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    RemoveParty(0x35, 0xFF)
    AddParty(0x4, 0xFF)
    OP_31(0x4, 0x0, 0x11)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x79)
    OP_41(0x4, 0xF4)
    OP_41(0x4, 0x112)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x262, 0x5)
    OP_41(0x4, 0x2C8, 0x4)
    OP_41(0x4, 0x265, 0x3)
    OP_41(0x4, 0x25B, 0x2)
    OP_41(0x4, 0x2D4, 0x1)
    OP_35(0x4, 0xBE)
    OP_36(0x4, 0xFA)
    FadeToDark(0, 0, -1)
    OP_20(0x9C4)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x56)
    SetChrPos(0x8, -10880, 0, 6920, 135)
    SetChrPos(0x9, -9460, 0, 7150, 270)
    SetChrPos(0xA, -10770, 0, 5350, 0)
    SetChrPos(0xB, -11290, 0, 4290, 90)
    SetChrPos(0xC, -10500, 0, 1550, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    def lambda_2D4B():

        label("loc_2D4B")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2D4B")

    QueueWorkItem2(0x8, 1, lambda_2D4B)

    def lambda_2D5C():

        label("loc_2D5C")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2D5C")

    QueueWorkItem2(0x9, 1, lambda_2D5C)

    def lambda_2D6D():

        label("loc_2D6D")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2D6D")

    QueueWorkItem2(0xA, 1, lambda_2D6D)

    def lambda_2D7E():

        label("loc_2D7E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2D7E")

    QueueWorkItem2(0xB, 1, lambda_2D7E)

    def lambda_2D8F():

        label("loc_2D8F")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2D8F")

    QueueWorkItem2(0xC, 1, lambda_2D8F)

    def lambda_2DA0():

        label("loc_2DA0")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_2DA0")

    QueueWorkItem2(0xD, 1, lambda_2DA0)
    OP_6D(-9740, 0, 5080, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #140
        0xE,
        (
            "#776FDon't try to play dumb! I know\x01",
            "it was you guys that did it!\x02\x03",

            "I'm not gonna let you get\x01",
            "away with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xA,
        (
            "What's this little punk talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#6PHey, this is no place for little\x01",
            "kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "#6PYou oughta go home and get\x01",
            "back to sucking on your mama's\x01",
            "tit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        "#4PHA HA HA! Nice one, man!\x02",
    )

    CloseMessageWindow()
    OP_92(0xE, 0x9, 0xED8, 0x7D0, 0x0)

    ChrTalk(    #145
        0xE,
        "#776FGrrrrr...\x02",
    )

    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #146
        0xE,
        "#778F#3SWAAAAAAHHHHH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_2FE3():
        OP_6D(-12160, 0, 5450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE3)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xE, 0x10E, 0x64, 0xBB8, 0x0)
    CloseMessageWindow()
    OP_92(0xE, 0x9, 0x1F4, 0x1770, 0x0)

    def lambda_30BE():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30BE)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0x9, 0xB4, 0x320, 0x1770, 0x0)
    Sleep(200)
    OP_92(0xE, 0xA, 0x320, 0x1770, 0x0)

    def lambda_30FB():
        OP_94(0x1, 0xFE, 0xB4, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30FB)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x258, 0x1770, 0x0)

    ChrTalk(    #147
        0x8,
        "#2PWhat the...?\x02",
    )

    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_3147():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3147)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)
    CloseMessageWindow()

    ChrTalk(    #148
        0x9,
        (
            "What's the brat so pissed off\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "#778F#4PI don't have a mom, you jerks!\x02\x03",

            "I have the matron!\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_31EA():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31EA)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)

    ChrTalk(    #150
        0xE,
        "#776F#4PYou don't get to make fun of her!\x02",
    )

    CloseMessageWindow()
    OP_92(0xE, 0xA, 0x258, 0x1770, 0x0)

    def lambda_3251():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3251)
    OP_22(0x7D, 0x0, 0x64)
    OP_94(0x1, 0xA, 0xB4, 0x12C, 0x1770, 0x0)

    ChrTalk(    #151
        0xA,
        "#1PHeh...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x40)
    OP_94(0x1, 0xE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_92(0xE, 0xA, 0x320, 0x1770, 0x0)

    def lambda_32B1():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_32B1)
    OP_92(0xE, 0xA, 0x1F4, 0x1770, 0x0)
    OP_22(0x209, 0x0, 0x64)
    OP_96(0xE, 0xFFFFD594, 0x0, 0x145A, 0x1F4, 0x1388)
    OP_96(0xE, 0xFFFFD88C, 0x0, 0x1450, 0xC8, 0x1388)

    ChrTalk(    #152
        0xE,
        "#778F#4PUng...\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0xE, 0x2BC, 0x7D0, 0x0)
    OP_63(0xE)
    TurnDirection(0xE, 0x8, 400)
    Sleep(500)

    def lambda_3339():
        OP_94(0x1, 0xFE, 0x10E, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3339)
    SetChrFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x400)
    OP_44(0x8, 0xFF)

    def lambda_335D():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_335D)

    def lambda_336D():
        OP_94(0x1, 0xFE, 0x0, 0x64, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_336D)
    OP_94(0x1, 0xE, 0xB4, 0x64, 0x3E8, 0x0)
    OP_94(0x1, 0xE, 0x0, 0x64, 0x3E8, 0x0)

    def lambda_33A1():
        OP_91(0xFE, 0x0, 0x190, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_33A1)
    OP_9E(0xE, 0xF, 0x0, 0x12C, 0xBB8)

    ChrTalk(    #153
        0x8,
        "#5PYou've got a lot of attitude, punk.\x02",
    )

    CloseMessageWindow()
    OP_92(0xA, 0xE, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #154
        0xA,
        "#1PMaybe you need some discipline.\x02",
    )

    CloseMessageWindow()
    OP_92(0x9, 0xE, 0x5DC, 0x7D0, 0x0)

    ChrTalk(    #155
        0x9,
        (
            "#2PHow about a hundred whacks\x01",
            "on the ass? Ha ha ha!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -1130, 0, 4490, 0)
    SetChrPos(0x105, -1130, 0, 4490, 0)
    SetChrPos(0x102, -1130, 0, 4490, 0)

    ChrTalk(    #156
        0x105,
        "#1PStop this!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3558():

        label("loc_3558")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3558")

    QueueWorkItem2(0x9, 1, lambda_3558)

    def lambda_3569():

        label("loc_3569")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_3569")

    QueueWorkItem2(0xA, 1, lambda_3569)

    def lambda_357A():

        label("loc_357A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_357A")

    QueueWorkItem2(0xB, 1, lambda_357A)

    def lambda_358B():

        label("loc_358B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_358B")

    QueueWorkItem2(0xC, 1, lambda_358B)

    def lambda_359C():

        label("loc_359C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_359C")

    QueueWorkItem2(0xD, 1, lambda_359C)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 11)
    SetChrChipByIndex(0x102, 12)

    def lambda_35C1():
        OP_6D(-10300, 0, 5530, 1000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_35C1)

    def lambda_35D9():
        OP_8E(0xFE, 0xFFFFE2FA, 0x0, 0x1338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35D9)
    Sleep(500)

    def lambda_35F9():
        OP_8E(0xFE, 0xFFFFE606, 0x0, 0x16F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35F9)
    Sleep(300)

    def lambda_3619():
        OP_8E(0xFE, 0xFFFFE868, 0x0, 0xFC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3619)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 6)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 6)

    ChrTalk(    #157
        0x8,
        "#5PIt's you...\x02",
    )

    CloseMessageWindow()
    OP_22(0x1FC, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    Sleep(100)
    SetChrChipByIndex(0xA, 32)
    Sleep(100)
    SetChrChipByIndex(0xB, 4)
    Sleep(100)
    SetChrChipByIndex(0xC, 4)
    Sleep(100)
    SetChrChipByIndex(0xD, 4)
    Sleep(100)
    SetChrFlags(0xE, 0x40)

    def lambda_36A2():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_36A2)
    OP_96(0xE, 0xFFFFD544, 0x0, 0x17E8, 0x1F4, 0x1388)
    ClearChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x400)
    OP_96(0xE, 0xFFFFD1D4, 0x0, 0x19AA, 0xC8, 0x1388)
    ClearChrFlags(0xE, 0x4)
    SetChrChipByIndex(0x8, 24)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #158
        0xE,
        "#778F*cough* *cough*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x105, 250)

    ChrTalk(    #159
        0xE,
        "#775FMiss...Miss Kloe?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #160
        0x105,
        (
            "#049FHow can you be so cruel to a child\x01",
            "like this...?\x02\x03",

            "It's disgusting... You should be\x01",
            "ashamed of yourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        "#3POh, hell no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        "#3PHey, missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "#3PWho are you to look down on us,\x01",
            "just because of your looks?\x01",
            "Rich snob...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "How many bracers you think\x01",
            "it'll take to beat us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#005FStand aside, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#012FWe'll buy you some time. Get the kid\x01",
            "as far away from here as you can!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(200)

    ChrTalk(    #167
        0x105,
        (
            "#042F#1PNo...\x02\x03",

            "Let me fight, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x105,
        (
            "#047F#1PI really don't enjoy it...\x02\x03",

            "...but I was taught how to use a\x01",
            "sword, if it's to protect others.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F8, 0x0, 0x64)
    SetChrChipByIndex(0x105, 10)
    SetChrSubChip(0x105, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(    #170
        0x105,
        "#042F#1PI think now is the right time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#004FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        "#014FA self-defense...rapier?!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x105, 0x20)

    def lambda_3A02():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A02)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    ClearChrFlags(0x105, 0x20)

    ChrTalk(    #173
        0x105,
        (
            "#046FLet the child go, please.\x02\x03",

            "Otherwise...I will force you to\x01",
            "do so!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xC,
        "That's so hot...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #176
        0x8,
        (
            "#3S#3PGet your minds out of the gutter\x01",
            "and focus!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #177
        0x9,
        (
            "#3PYou expect us to let this brat get\x01",
            "away with mouthing off to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "#3PWe're the Ravens, and you need\x01",
            "to learn not to mess with us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        "#2P#1KYeah!\x02",
    )


    ChrTalk(    #180
        0xC,
        "#1P#1KAll right!\x02",
    )


    ChrTalk(    #181
        0xD,
        "#4P#1KCome on!\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 29)
    SetChrChipByIndex(0xA, 33)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 5)
    SetChrChipByIndex(0xD, 5)

    def lambda_3BE1():
        OP_92(0xFE, 0x105, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3BE1)

    def lambda_3BF6():
        OP_92(0xFE, 0x102, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3BF6)

    def lambda_3C0B():
        OP_92(0xFE, 0x105, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C0B)

    def lambda_3C20():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3C20)

    def lambda_3C35():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3C35)

    def lambda_3C4A():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3C4A)
    Sleep(300)
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3C77"),
        (SWITCH_DEFAULT, "loc_3C7A"),
    )


    label("loc_3C77")

    OP_B4(0x0)
    Return()

    label("loc_3C7A")

    EventBegin(0x0)
    SetChrPos(0xE, -11720, 0, 5630, 90)
    SetChrPos(0x105, -7070, 0, 5350, 270)
    SetChrPos(0x101, -6160, 0, 4019, 270)
    SetChrPos(0x102, -6120, 0, 5950, 270)
    SetChrChipByIndex(0x8, 24)
    SetChrChipByIndex(0x9, 28)
    SetChrChipByIndex(0xA, 32)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 7)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, -11300, 0, 10000, 135)
    SetChrPos(0xC, -14730, 0, 3670, 90)
    SetChrPos(0xD, -10480, 0, -290, 0)
    SetChrPos(0x8, -11270, 0, 6060, 90)
    SetChrPos(0x9, -9150, 0, 3860, 90)
    SetChrPos(0xA, -8760, 0, 7620, 90)
    TurnDirection(0x9, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)
    OP_6D(-10660, 0, 5990, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #182
        0x8,
        (
            "#3PY-You guys are some kind of\x01",
            "monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        (
            "Even if she is a bracer, there's\x01",
            "something weird about this chick...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xE,
        "#774FThat was awesome, Miss Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#001FPhew! Nice going, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x102,
        (
            "#010FYou must have learned the art\x01",
            "of the sword from someone very\x01",
            "skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        "#045FNo, I'm still just a novice.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 65535)
    OP_0D()
    Sleep(500)
    OP_94(0x1, 0x105, 0x0, 0x3E8, 0x3E8, 0x0)

    ChrTalk(    #188
        0x105,
        (
            "#043FFighting any longer would serve\x01",
            "no purpose.\x02\x03",

            "Please...release the boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "#2PY-You bitch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x8,
        (
            "#3PWe ain't just gonna let you make\x01",
            "fools of us and get away with it!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, -990, 0, 1560, 315)
    SetChrPos(0xF, -2200, 0, 1380, 0)

    NpcTalk(    #191
        0x10,
        "Young Man's Voice",
        "#1P...Enough.\x02",
    )

    CloseMessageWindow()

    def lambda_4068():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4068)

    def lambda_4076():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4076)

    def lambda_4084():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4084)

    def lambda_4092():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4092)

    def lambda_40A0():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40A0)

    def lambda_40AE():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40AE)

    ChrTalk(    #192
        0x8,
        (
            "#3PWha...\x01",
            "Who's there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        "#2PReinforcements?!\x02",
    )

    CloseMessageWindow()

    def lambda_40F2():

        label("loc_40F2")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_40F2")

    QueueWorkItem2(0x8, 1, lambda_40F2)

    def lambda_4103():

        label("loc_4103")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_4103")

    QueueWorkItem2(0x9, 1, lambda_4103)

    def lambda_4114():

        label("loc_4114")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_4114")

    QueueWorkItem2(0xA, 1, lambda_4114)

    def lambda_4125():

        label("loc_4125")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_4125")

    QueueWorkItem2(0x101, 1, lambda_4125)

    def lambda_4136():

        label("loc_4136")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_4136")

    QueueWorkItem2(0x102, 1, lambda_4136)

    def lambda_4147():

        label("loc_4147")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_4147")

    QueueWorkItem2(0x105, 1, lambda_4147)

    def lambda_4158():
        OP_6D(-9840, 0, 5810, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4158)
    ClearChrFlags(0x10, 0x80)
    OP_8E(0x10, 0xFFFFF042, 0x0, 0x114E, 0xBB8, 0x0)
    OP_8C(0x10, 270, 400)

    ChrTalk(    #194
        0x10,
        (
            "#053F#2PHas it been so long that you've\x01",
            "forgotten my voice?\x02",
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
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #195
        0x8,
        "A-Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x9,
        "You're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10,
        "#050F#2P...\x02",
    )

    CloseMessageWindow()

    def lambda_4284():
        OP_6D(-10660, 0, 5990, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4284)

    def lambda_429C():
        OP_8E(0xFE, 0xFFFFDE36, 0x0, 0x14E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_429C)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    Sleep(600)
    OP_44(0x105, 0xFF)
    OP_8C(0x105, 45, 400)
    OP_90(0x105, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0x105, 180, 400)

    def lambda_42EC():

        label("loc_42EC")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_42EC")

    QueueWorkItem2(0x105, 1, lambda_42EC)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 400)

    ChrTalk(    #198
        0x101,
        (
            "#004FWhat are you doing here...?\x02\x03",

            "And you know these guys?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x10,
        "#053FRais...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        "Y-Yeah...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x9, 400)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_92(0x10, 0x9, 0x190, 0x1F40, 0x0)
    SetChrSubChip(0x10, 1)
    OP_22(0x1FB, 0x0, 0x64)

    def lambda_43A9():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_43A9)
    SetChrChipByIndex(0x9, 30)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_94(0x1, 0x9, 0xB4, 0x1F4, 0x1F40, 0x0)
    OP_22(0x209, 0x0, 0x64)

    def lambda_43E8():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_43E8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 31)
    OP_99(0x9, 0x0, 0x3, 0x7D0)

    ChrTalk(    #201
        0x9,
        "Urgh!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(80)
    SetChrChipByIndex(0x10, 3)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)
    TurnDirection(0x10, 0xA, 400)
    OP_92(0x10, 0x9, 0xBB8, 0x1F40, 0x0)

    ChrTalk(    #202
        0x10,
        (
            "#057FWhat are you fools doing?\x02\x03",

            "Fighting with girls and beating up\x01",
            "a little kid...\x02\x03",

            "Is that what it's come to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        "#2PY-You shut up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "#2PYou left us, so who are you to\x01",
            "give us orders anymore...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4516():
        OP_6D(-10660, 0, 7680, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4516)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0x10, 37)
    OP_92(0x10, 0xA, 0x3E8, 0x2710, 0x0)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_92(0x10, 0xA, 0x190, 0x2710, 0x0)
    SetChrSubChip(0x10, 1)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)

    def lambda_457C():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_457C)
    SetChrChipByIndex(0xA, 34)
    SetChrFlags(0xA, 0x20)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_94(0x1, 0xA, 0xB4, 0x1F4, 0x1F40, 0x0)

    def lambda_45B6():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_45B6)
    WaitChrThread(0xA, 0x1)
    SetChrSubChip(0x10, 2)
    OP_8F(0xA, 0xFFFFDDAA, 0x7D0, 0x2CEC, 0x3A98, 0x0)
    PlayEffect(0x12, 0xFF, 0xA, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #205 op#5
        0xA,
        "Oof!\x05\x02",
    )

    OP_22(0x8E, 0x0, 0x64)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0xA, 0xFFFFDDAA, 0x0, 0x2CEC, 0x7D0, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xA, 35)
    OP_99(0xA, 0x1, 0x3, 0x3E8)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x20)
    Sleep(500)

    ChrTalk(    #206
        0x10,
        "#050F...You were saying?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #207
        0x8,
        "Hey, A-Agate...take it easy!\x02",
    )

    CloseMessageWindow()

    def lambda_46D2():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_46D2)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 21)
    OP_8E(0x8, 0xFFFFD1DE, 0x0, 0x18CE, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFD01C, 0x0, 0x15E0, 0xBB8, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #208
        0x8,
        (
            "If it's about the kid, we'll let\x01",
            "him go, see?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_474C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_474C)

    def lambda_475A():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_475A)

    def lambda_4768():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4768)

    ChrTalk(    #209
        0xE,
        "#775F#3PMiss Kloe!\x02",
    )

    CloseMessageWindow()

    def lambda_478E():
        OP_6D(-9010, 0, 6820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_478E)

    def lambda_47A6():
        OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x1496, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_47A6)
    Sleep(300)
    OP_8E(0x105, 0xFFFFE03E, 0x0, 0x152C, 0x7D0, 0x0)
    OP_8C(0x105, 270, 400)

    ChrTalk(    #210
        0x105,
        (
            "#048F#4PThank goodness...\x01",
            "You're all right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x10,
        (
            "#053FHmph... You should've just done\x01",
            "that from the start.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #212
        0x101,
        (
            "#007FWhat a bunch of mean jerks...\x02\x03",

            "#009FHey, how did you know exactly\x01",
            "when to show up?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #213
        0x10,
        (
            "#050FI just talked to Jean, is all.\x02\x03",

            "He said the newbies were somewhere,\x01",
            "investigating the arson case.\x02\x03",

            "#053FSo...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)
    Sleep(500)

    ChrTalk(    #214
        0x10,
        "#050F#4PHey, kid.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(    #215
        0xE,
        "#775FWh-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x10,
        (
            "#051F#4PYou've got some guts to come\x01",
            "up here all by your lonesome.\x02\x03",

            "But you're really pushing your\x01",
            "luck.\x02\x03",

            "You shouldn't worry your mama\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xE,
        "#774F...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #218
        0xF,
        "Woman's Voice",
        "Clem...\x02",
    )

    CloseMessageWindow()

    def lambda_4A39():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4A39)

    def lambda_4A47():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A47)

    def lambda_4A55():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A55)

    def lambda_4A63():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A63)

    def lambda_4A71():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4A71)
    TurnDirection(0xE, 0xF, 400)
    Sleep(500)

    def lambda_4A8B():

        label("loc_4A8B")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_4A8B")

    QueueWorkItem2(0x101, 1, lambda_4A8B)

    def lambda_4A9C():

        label("loc_4A9C")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_4A9C")

    QueueWorkItem2(0x102, 1, lambda_4A9C)

    def lambda_4AAD():

        label("loc_4AAD")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_4AAD")

    QueueWorkItem2(0x105, 1, lambda_4AAD)
    ClearChrFlags(0xF, 0x80)

    def lambda_4AC3():
        OP_6D(-9140, 0, 5560, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4AC3)
    OP_8E(0xF, 0xFFFFE642, 0x0, 0xAFA, 0x7D0, 0x0)
    TurnDirection(0xF, 0xE, 0)
    TurnDirection(0xE, 0xF, 0)

    ChrTalk(    #219
        0xE,
        "#774F#3PM-Matron?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x105,
        "#044F#4PWhy have you come here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xF,
        (
            "#754FI inquired at the guild as to\x01",
            "what was going on, and I was\x01",
            "led here.\x02\x03",

            "#752FClem, really... You know better...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xE,
        (
            "#772F#3PI-I'm not apologizing this time!\x02\x03",

            "I'm gonna get those jerks who\x01",
            "started the fire, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xF,
        "#755F#3SClem!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(200)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4C54():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x1770)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4C54)
    CloseMessageWindow()

    ChrTalk(    #224
        0x105,
        (
            "#043F#4PMatron Theresa...please don't\x01",
            "scold him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xF,
        (
            "#754FThat wasn't my intent.\x02\x03",

            "#757FI understand how you feel, Clem...\x01",
            "Believe me, I do.\x02\x03",

            "The house was important to everyone\x01",
            "who lived there with you...to all of\x01",
            "us...\x02\x03",

            "However...\x02\x03",

            "#756FGetting yourself killed will not\x01",
            "bring it back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xE,
        "#775F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xF,
        (
            "#750FAll that I want is for everyone\x01",
            "to be safe.\x02\x03",

            "Nothing else matters...\x02\x03",

            "#758FSo, please...don't put yourself\x01",
            "in danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xE,
        (
            "#775F#3PM-Matron...\x02\x03",

            "#777FI... *sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #229
        0xE,
        "#778F#3P#5SWAAAAHHHH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_92(0xE, 0xF, 0x258, 0x1388, 0x0)
    SetChrFlags(0xF, 0x20)
    OP_94(0x1, 0xF, 0xB4, 0x64, 0x5DC, 0x0)
    OP_94(0x1, 0xF, 0x0, 0x64, 0x5DC, 0x0)
    ClearChrFlags(0xF, 0x20)
    Sleep(500)

    ChrTalk(    #230
        0x101,
        (
            "#003F#2P*sniffle* I'm such a sucker\x01",
            "for this stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x105,
        (
            "#049F#4PClem...\x02\x03",

            "#049FI'm really glad he's okay...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_4F66():
        OP_6D(-9840, 0, 6260, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4F66)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #232
        0x10,
        (
            "#551FGeez... Women and kids, always\x01",
            "the same.\x02\x03",

            "#552FHey, bracer-kid.\x02\x03",

            "You should get the matron\x01",
            "and brat out of here.\x02\x03",

            "This really is no place for them.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 270, 400)

    ChrTalk(    #233
        0x102,
        (
            "#014FI don't mind...but what will you\x01",
            "do, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x10,
        "#057FI've made up my mind...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)

    def lambda_508B():
        OP_6D(-10420, 0, 6530, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_508B)
    OP_8E(0x10, 0xFFFFD58A, 0x0, 0x15E0, 0xBB8, 0x0)
    OP_8C(0x8, 90, 0)
    TurnDirection(0x10, 0x8, 400)

    ChrTalk(    #235
        0x10,
        (
            "#054F#4PI'm going to remind these idiots\x01",
            "who runs things and why.\x02\x03",

            "I might need to crack a few\x01",
            "skulls.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x8, 0x32, 0x0, 0x12C, 0x1770)
    Sleep(500)
    OP_44(0x8, 0xFF)

    ChrTalk(    #236
        0x8,
        (
            "Nooooo...please, take it easy\x01",
            "on us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x102,
        (
            "#010FI see...\x02\x03",

            "#019FI guess you'd prefer not being\x01",
            "interrupted, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_28(0x3C, 0x1, 0x20)
    OP_A2(0x3FE)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_2C34 end

    SaveToFile()

Try(main)
