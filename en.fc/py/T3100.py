from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3100.x',
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
        'Sotiria',                              # 9
        'Elise',                                # 10
        'Muriel',                               # 11
        'Vince',                                # 12
        'Gary',                                 # 13
        'Knowles',                              # 14
        'Didi',                                 # 15
        'Lane',                                 # 16
        'Cosimo',                               # 17
        'Monika',                               # 18
        'Bruno',                                # 19
        'Igor',                                 # 20
        'Radmira',                              # 21
        'Charles',                              # 22
        ' ',                                    # 23
        'Zeiss - Factory Block',                # 24
        'Tratt Plains Road',                    # 25
        'Ritter Roadway',                       # 26
    )

    DeclEntryPoint(
        Unknown_00              = 67000,
        Unknown_04              = 0,
        Unknown_08              = 53000,
        Unknown_0C              = 4,
        Unknown_0E              = 315,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 270,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01200 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01060 ._CH',             # 0A
        'ED6_DT07/CH01160 ._CH',             # 0B
        'ED6_DT07/CH01450 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH01530 ._CH',             # 0F
        'ED6_DT07/CH01250 ._CH',             # 10
        'ED6_DT07/CH01690 ._CH',             # 11
        'ED6_DT07/CH02640 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01200P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01060P._CP',             # 0A
        'ED6_DT07/CH01160P._CP',             # 0B
        'ED6_DT07/CH01450P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH01530P._CP',             # 0F
        'ED6_DT07/CH01250P._CP',             # 10
        'ED6_DT07/CH01690P._CP',             # 11
        'ED6_DT07/CH02640P._CP',             # 12
    )

    DeclNpc(
        X                   = 17600,
        Z                   = 3500,
        Y                   = 53760,
        Direction           = 283,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 18000,
        Z                   = 3500,
        Y                   = 52580,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23890,
        Z                   = 3500,
        Y                   = 53440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17220,
        Z                   = 8000,
        Y                   = 59000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81330,
        Z                   = 0,
        Y                   = 53110,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 42990,
        Z                   = 0,
        Y                   = 104270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 39600,
        Y                   = -1000,
        Z                   = 90600,
        Range               = 46400,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x16828,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 69400,
        Y                   = -1000,
        Z                   = 56700,
        Range               = 71000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB734,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 7780,
        Y                   = -1000,
        Z                   = 63930,
        Range               = 6420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xEA1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 6420,
        Y                   = -1000,
        Z                   = 58250,
        Range               = 7860,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xD5D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 43700,
        Y                   = 0,
        Z                   = 63080,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 40200,
        Y                   = 0,
        Z                   = 66870,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 52230,
        Y                   = 0,
        Z                   = 54590,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 51500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 48500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 59950,
        Y                   = 0,
        Z                   = 25220,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 36000,
        Y                   = 0,
        Z                   = 54740,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 27020,
        Y                   = 0,
        Z                   = 63460,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 23130,
        Y                   = 0,
        Z                   = 82450,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = 64030,
        Y                   = 0,
        Z                   = 69550,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 500,
        TriggerY            = 85510,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1500,
        ActorY              = 85510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_566",          # 00, 0
        "Function_1_B57",          # 01, 1
        "Function_2_BD2",          # 02, 2
        "Function_3_C08",          # 03, 3
        "Function_4_D85",          # 04, 4
        "Function_5_DA9",          # 05, 5
        "Function_6_DCD",          # 06, 6
        "Function_7_E32",          # 07, 7
        "Function_8_1182",         # 08, 8
        "Function_9_1522",         # 09, 9
        "Function_10_1632",        # 0A, 10
        "Function_11_1E15",        # 0B, 11
        "Function_12_2577",        # 0C, 12
        "Function_13_2AD8",        # 0D, 13
        "Function_14_30C8",        # 0E, 14
        "Function_15_30F6",        # 0F, 15
        "Function_16_338C",        # 10, 16
        "Function_17_343F",        # 11, 17
        "Function_18_38D9",        # 12, 18
        "Function_19_3AA2",        # 13, 19
        "Function_20_43E7",        # 14, 20
        "Function_21_44FB",        # 15, 21
        "Function_22_4FA8",        # 16, 22
        "Function_23_5CC2",        # 17, 23
        "Function_24_5CDE",        # 18, 24
        "Function_25_5CFA",        # 19, 25
        "Function_26_5D83",        # 1A, 26
        "Function_27_5F78",        # 1B, 27
        "Function_28_61BF",        # 1C, 28
        "Function_29_6481",        # 1D, 29
        "Function_30_650F",        # 1E, 30
        "Function_31_6513",        # 1F, 31
        "Function_32_6517",        # 20, 32
        "Function_33_651B",        # 21, 33
        "Function_34_651F",        # 22, 34
        "Function_35_6523",        # 23, 35
        "Function_36_6527",        # 24, 36
    )


    def Function_0_566(): pass

    label("Function_0_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_574")
    OP_A3(0x3FA)
    Event(0, 25)

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_582")
    OP_A3(0x3FB)
    Event(0, 26)

    label("loc_582")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_58E"),
        (SWITCH_DEFAULT, "loc_5AD"),
    )


    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    OP_A2(0x52B)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 27)

    label("loc_5AA")

    Jump("loc_5AD")

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_625")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 38910, 0, 68560, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 38910, 0, 69580, 90)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    Jump("loc_B56")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_76B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16250, 3500, 71750, 39)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 45110, 0, 62220, 90)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 46310, 0, 62180, 0)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 32970, 500, 85010, 175)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 38670, 0, 68820, 90)
    Jump("loc_B56")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_775")
    Jump("loc_B56")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_7AB")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 22230, 0, 80520, 215)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_806")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 20340, 0, 80730, 227)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 14670, 0, 60890, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8BB")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8690, 0, 54740, 180)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 45910, 0, 57120, 270)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 44430, 0, 57110, 90)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_95F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_B56")

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_A2F")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 16780, 3500, 73480, 97)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 17830, 3500, 72380, 8)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41900, 0, 61970, 17)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41890, 0, 52020, 267)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 46850, 0, 87800, 238)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 9770, 0, 59280, 277)
    Jump("loc_B56")

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_AC4")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 10650, 0, 59050, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35280, 0, 69150, 90)
    OP_43(0xD, 0x0, 0x0, 0x6)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)
    Jump("loc_B56")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B56")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 10650, 0, 59050, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 35280, 0, 69150, 90)
    OP_43(0xD, 0x0, 0x0, 0x6)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 41020, 0, 53780, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 39400, 0, 46910, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 32930, 0, 83370, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45470, 0, 62220, 1)

    label("loc_B56")

    Return()

    # Function_0_566 end

    def Function_1_B57(): pass

    label("Function_1_B57")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x30051)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_B81")
    Jump("loc_BAE")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B90")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B9F")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_BAE")
    OP_71(0x11, 0x4)
    Jump("loc_BAE")

    label("loc_BAE")

    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Return()

    # Function_1_B57 end

    def Function_2_BD2(): pass

    label("Function_2_BD2")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C07")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_BDC")

    label("loc_C07")

    Return()

    # Function_2_BD2 end

    def Function_3_C08(): pass

    label("Function_3_C08")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D6F")

    label("loc_C2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C46")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D6F")

    label("loc_C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D6F")

    label("loc_C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C78")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D6F")

    label("loc_C78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C91")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D6F")

    label("loc_C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D6F")

    label("loc_CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D6F")

    label("loc_CC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D6F")

    label("loc_CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D6F")

    label("loc_CF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D6F")

    label("loc_D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D6F")

    label("loc_D27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D40")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D6F")

    label("loc_D40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D59")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D6F")

    label("loc_D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D84")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D6F")

    label("loc_D84")

    Return()

    # Function_3_C08 end

    def Function_4_D85(): pass

    label("Function_4_D85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA8")
    OP_8D(0xFE, 17510, 71160, 14830, 73220, 3000)
    Jump("Function_4_D85")

    label("loc_DA8")

    Return()

    # Function_4_D85 end

    def Function_5_DA9(): pass

    label("Function_5_DA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DCC")
    OP_8D(0xFE, 11460, 51180, 8590, 67130, 3000)
    Jump("Function_5_DA9")

    label("loc_DCC")

    Return()

    # Function_5_DA9 end

    def Function_6_DCD(): pass

    label("Function_6_DCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E31")
    OP_8E(0xFE, 0x9808, 0x0, 0x10E1E, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_63(0xD)
    OP_8E(0xFE, 0x89D0, 0x0, 0x10E1E, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xD)
    Jump("Function_6_DCD")

    label("loc_E31")

    Return()

    # Function_6_DCD end

    def Function_7_E32(): pass

    label("Function_7_E32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_105D")
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_E87")

    ChrTalk(    #0
        0xFE,
        "Very well, let's get this started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "Yes, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1052")

    label("loc_E87")

    OP_A2(0xB)
    OP_A2(0x8)

    ChrTalk(    #2
        0x10,
        (
            "Thank you for making the time\x01",
            "to help us, Igor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Why, it's no trouble at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "An old, obsolete engineer like\x01",
            "me has plenty of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "Ha! 'Obsolete,' he says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "He helps build the Arseille,\x01",
            "the greatest machine to ever\x01",
            "fly, and he's 'obsolete.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Okay, okay. Then just 'old'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x13,
        (
            "My small part in the Arseille's\x01",
            "construction wore me out. I\x01",
            "couldn't keep up with Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "But I've got to serve as best\x01",
            "I can, even at my age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1052")

    OP_4B(0x13, 255)
    OP_4B(0x10, 255)
    Jump("loc_117E")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_117E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_10DE")

    ChrTalk(    #10
        0xFE,
        (
            "By the way, I'm pleased to hear\x01",
            "Randall's working so hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "But when did he start working\x01",
            "in a BAR?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117E")

    label("loc_10DE")

    OP_A2(0xB)

    ChrTalk(    #12
        0xFE,
        (
            "Would you look at that...\x01",
            "the main clock IS slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Guess that blackout's\x01",
            "responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Well, I'll be sure t' take\x01",
            "a look at it in a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117E")

    TalkEnd(0xFE)
    Return()

    # Function_7_E32 end

    def Function_8_1182(): pass

    label("Function_8_1182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_151E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149D")
    OP_A2(0x583)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #15
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Hey. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#014F...?\x02\x03",

            "#010FAh, hey.\x01",
            "It HAS been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#501FWho's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FYou remember that kid who was\x01",
            "looking for the quartz shard in\x01",
            "Rolent, don't you?\x02\x03",

            "Remember? We took a request\x01",
            "to find it a while back.\x02\x03",

            "Are you headed back to\x01",
            "the Republic?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #20
        0xFE,
        (
            "Nah, the central factory. We\x01",
            "made some cash in Grancel and\x01",
            "have some shopping to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Mom said we're gonna take this\x01",
            "mira and stock up on orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "They say the eyes are the first\x01",
            "to go, but she can still spot a\x01",
            "good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#506FI can see you're still an\x01",
            "obnoxious brat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #24
        0xFE,
        (
            "What? I'm only saying what\x01",
            "everybody else is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "But yeah...did you check out\x01",
            "these crazy moving stairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "I'll never get tired of them!\x02",
    )

    CloseMessageWindow()
    Jump("loc_151E")

    label("loc_149D")


    ChrTalk(    #27
        0xFE,
        "These moving stairs are cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "It's true that walking up and\x01",
            "down stairs is a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "So make the stairs move.\x01",
            "Nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1182 end

    def Function_9_1522(): pass

    label("Function_9_1522")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1584")

    ChrTalk(    #30
        0xFE,
        "Now, where is Charles?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "That stupid boy is always\x01",
            "wandering off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162E")

    label("loc_1584")

    OP_A2(0xC)

    ChrTalk(    #32
        0xFE,
        "Whew, Zeiss at last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I probably should go to the\x01",
            "central factory and see the\x01",
            "orbment selection...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "But first, a break. Let's find a\x01",
            "nice place to sit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1522 end

    def Function_10_1632(): pass

    label("Function_10_1632")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_17BA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(    #35
        0xFE,
        (
            "Now we just remove the broken\x01",
            "quartz and we're finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "*sigh* I just can't seem to get\x01",
            "into this like usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Maybe I should go to the chapel\x01",
            "again for prayer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B7")

    label("loc_16F8")

    OP_A2(0x7)

    ChrTalk(    #38
        0xFE,
        (
            "Okay, all the size 8 screws together\x01",
            "in one case, along with two orbal\x01",
            "pressure indicators...CHECK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Feels like the same thing every\x01",
            "single week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "Parts inventory is SO dull.\x02",
    )

    CloseMessageWindow()

    label("loc_17B7")

    Jump("loc_1E11")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1875")

    ChrTalk(    #41
        0xFE,
        (
            "It...took a lot less time\x01",
            "than I expected to find the\x01",
            "box I was looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm going to pretend I'm still\x01",
            "searching when the boss comes\x01",
            "by. Have a little 'me' time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E11")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1906")

    ChrTalk(    #43
        0xFE,
        (
            "All right! Starting today I will\x01",
            "be positive! POSITIVE, CURSE YOU\x01",
            "ALL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Today I'm finishing the order\x01",
            "for Elkan's weapon box.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E11")

    label("loc_1906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(    #45
        0xFE,
        "All the factory workers are...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "They've all been evacuated?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E11")

    label("loc_1958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1A8D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_19FB")

    ChrTalk(    #47
        0xFE,
        (
            "I wanna just tell Elkan to finish\x01",
            "his own boxes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "But...*sigh* I can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "And ratting him out to old man\x01",
            "Stain'd look bad, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_19FB")

    OP_A2(0x7)

    ChrTalk(    #50
        0xFE,
        (
            "Dang it, now the box with the\x01",
            "parts I need is gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I wanna just tell Elkan to finish\x01",
            "his own boxes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "But...*sigh* I can't.\x02",
    )

    CloseMessageWindow()

    label("loc_1A8A")

    Jump("loc_1E11")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C0C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1B2E")

    ChrTalk(    #53
        0xFE,
        (
            "Man...these boxes are\x01",
            "just a MESS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "It's going to take FOREVER to\x01",
            "find what I need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Progress demands sacrifice, \x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C09")

    label("loc_1B2E")

    OP_A2(0x7)

    ChrTalk(    #56
        0xFE,
        "But still, what a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I was in total shock when the\x01",
            "lights went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "But I bet those guys up in the\x01",
            "engine room were even more\x01",
            "surprised, am I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Progress demands sacrifice, \x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C09")

    Jump("loc_1E11")

    label("loc_1C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1CA1")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #60
        0xFE,
        (
            "Hey, Tita. Thanks again for\x01",
            "helping clean up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Tell your grandfather to place\x01",
            "his orders early when he starts\x01",
            "running low.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E11")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E11")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(    #62
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "All that's left now is collecting\x01",
            "the broken quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E11")

    label("loc_1CFA")

    OP_A2(0x7)

    ChrTalk(    #64
        0xFE,
        (
            "Okay, all the size 8 screws together\x01",
            "in one case, along with two orbal\x01",
            "pressure indicators...CHECK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "Parts inventory isn't easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "That's because all the research\x01",
            "labs submit massive orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I'm pretty lucky that I've got the\x01",
            "Professor's grandkid to help me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E11")

    TalkEnd(0xFE)
    Return()

    # Function_10_1632 end

    def Function_11_1E15(): pass

    label("Function_11_1E15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(    #68
        0xFE,
        (
            "Looks like the clock decided\x01",
            "to work properly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Gotta check it every day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1F25")

    ChrTalk(    #70
        0xFE,
        "At last, it's keeping time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "As long as this old clock's tickin',\x01",
            "I reckon I will too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I mean, if I ain't around to\x01",
            "watch the old girl, who will?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_1F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_214D")
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1F77")

    ChrTalk(    #73
        0x13,
        "Very well, let's get this started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Yes, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2142")

    label("loc_1F77")

    OP_A2(0xB)
    OP_A2(0x8)

    ChrTalk(    #75
        0xFE,
        (
            "Thank you for making the time\x01",
            "to help us, Igor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x13,
        "Why, it's no trouble at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "An old, obsolete engineer like\x01",
            "me has plenty of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Ha! 'Obsolete,' he says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "He helps build the Arseille,\x01",
            "the greatest machine to ever\x01",
            "fly, and he's 'obsolete.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x13,
        "Okay, okay. Then just 'old'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x13,
        (
            "My small part in the Arseille's\x01",
            "construction wore me out. I\x01",
            "couldn't keep up with Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x13,
        (
            "But I've got to serve as best\x01",
            "I can, even at my age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2142")

    OP_4B(0x13, 255)
    OP_4B(0x10, 255)
    Jump("loc_2573")

    label("loc_214D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2182")

    ChrTalk(    #83
        0xFE,
        "Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "What's that smoke, I wonder?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_2182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_22B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2217")

    ChrTalk(    #85
        0xFE,
        (
            "Sorry, but I don't trust Randall\x01",
            "to work the machinery any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Call on the experts to get the\x01",
            "job done right, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B5")

    label("loc_2217")

    OP_A2(0x8)

    ChrTalk(    #87
        0xFE,
        (
            "Good ol' Igor. Full of spit and\x01",
            "vinegar, like usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Wonder if I could trouble you\x01",
            "to look at the clock. It's been\x01",
            "runnin' slow since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B5")

    Jump("loc_2573")

    label("loc_22B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2351")

    ChrTalk(    #89
        0xFE,
        (
            "I guess it's true... ALL the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Well, let's get this reset.\x01",
            "I suppose I should call\x01",
            "ol' Igor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BA")

    label("loc_2351")

    OP_A2(0x8)

    ChrTalk(    #91
        0xFE,
        "Look at that. The clock's slow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I guess it's true... ALL the\x01",
            "orbments shut down last night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23BA")

    Jump("loc_2573")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_246F")

    ChrTalk(    #93
        0xFE,
        (
            "Orbments all started with the\x01",
            "technology we invented for\x01",
            "clocks, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "And now orbments are being\x01",
            "used to power clocks. Ain't\x01",
            "science grand?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_246F")

    OP_A2(0x8)

    ChrTalk(    #95
        0xFE,
        "Ah, the memories.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "I helped Professor Russell build\x01",
            "this orbal clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Orbments drive it, you know.\x01",
            "Long as the orbal power don't\x01",
            "stop, the clock'll keep running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Not many remember the old days\x01",
            "anymore, when Zeiss was 'that\x01",
            "clock town'...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2573")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E15 end

    def Function_12_2577(): pass

    label("Function_12_2577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2689")

    ChrTalk(    #99
        0xFE,
        (
            "*giggle* I've discovered a way\x01",
            "to shop without getting bogged\x01",
            "down by decisions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Whenever I don't know what\x01",
            "to buy, I just choose the one\x01",
            "furthest to the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "That way, I don't have to worry\x01",
            "about silly details and can get\x01",
            "on with my shopping!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_27A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2714")

    ChrTalk(    #102
        0xFE,
        (
            "That said, doesn't this lack of\x01",
            "information bother you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "We consumers demand all kinds\x01",
            "of important information!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A6")

    label("loc_2714")

    OP_A2(0x9)

    ChrTalk(    #104
        0xFE,
        (
            "I came shopping for canned\x01",
            "goods today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "It's so much easier than bread.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I mean, what's in the can is\x01",
            "right on the label, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A6")

    Jump("loc_2AD4")

    label("loc_27A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_280A")

    ChrTalk(    #107
        0xFE,
        (
            "Oh, thank goodness things\x01",
            "have finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "Now I can shop properly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_280A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2889")

    ChrTalk(    #109
        0xFE,
        (
            "The owner of the item shop's\x01",
            "run off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Maybe to the factory to see all\x01",
            "the commotion for himself?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_295B")

    ChrTalk(    #111
        0xFE,
        (
            "My father's an orbal engineer.\x01",
            "I'm used to buying parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "*sigh* Parts' vital statistics are\x01",
            "clearly labeled. It's so easy to\x01",
            "make a choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Why isn't this bread like that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_295B")

    OP_A2(0x9)

    ChrTalk(    #114
        0xFE,
        "Wheat, white, rye, sourdough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "What kind of bread is 'good\x01",
            "bread,' anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "Labels would be SO much easier.\x02",
    )

    CloseMessageWindow()

    label("loc_29D9")

    Jump("loc_2AD4")

    label("loc_29DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2A5B")

    ChrTalk(    #117
        0xFE,
        (
            "This is my first time shopping\x01",
            "for food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "All this bread looks the same. \x01",
            "Which one do I choose?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD4")

    label("loc_2A5B")

    OP_A2(0x9)

    ChrTalk(    #119
        0xFE,
        "What do I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Father told me to go buy bread...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "All this bread looks the same. \x01",
            "Which one do I choose?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD4")

    TalkEnd(0xFE)
    Return()

    # Function_12_2577 end

    def Function_13_2AD8(): pass

    label("Function_13_2AD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2B5E")

    ChrTalk(    #122
        0xFE,
        (
            "I'm tired, but being a bracer\x01",
            "has gotta be tough, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Wouldn't call it 'work' otherwise\x01",
            "though, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDB")

    label("loc_2B5E")

    OP_A2(0xA)

    ChrTalk(    #124
        0xFE,
        (
            "*sigh* I'm off to the Wolf Fort\x01",
            "this afternoon. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "How many orbments do those \x01",
            "Republican guys need anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDB")

    Jump("loc_30C4")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C5A")

    ChrTalk(    #126
        0xFE,
        "Oh well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Probably a bit early, but I'd\x01",
            "better go place a request for\x01",
            "guards at the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDB")

    label("loc_2C5A")

    OP_A2(0xA)

    ChrTalk(    #128
        0xFE,
        "Feels like I just got home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "And now I'm off to the\x01",
            "Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I can't even catch my breath\x01",
            "enough to complain!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDB")

    Jump("loc_30C4")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2E7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2DCC")

    ChrTalk(    #131
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Everybody's all blah-blah-blah\x01",
            "about yesterday, instead of \x01",
            "getting some real work done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "And here I am trying to get\x01",
            "ready to leave for the Wolf\x01",
            "Fort!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "We working guys have got it\x01",
            "the worst.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7C")

    label("loc_2DCC")

    OP_A2(0xA)

    ChrTalk(    #135
        0xFE,
        (
            "Looks like all the packing's in\x01",
            "order. Almost ready to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Time for one final check.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Oh, hey, gotta remember to go request\x01",
            "a bracer escort. Time's a-wastin'!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7C")

    Jump("loc_30C4")

    label("loc_2E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2F16")

    ChrTalk(    #138
        0xFE,
        (
            "I swear, I get paranoid about this\x01",
            "thing. Never satisfied that it'll\x01",
            "get me where I'm goin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "I worry that it'll break down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FB9")

    label("loc_2F16")

    OP_A2(0xA)

    ChrTalk(    #140
        0xFE,
        (
            "And I need to be absolutely certain\x01",
            "it won't before I take it even one\x01",
            "selge out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I'd hate to break down in the\x01",
            "middle of a nest of monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB9")

    Jump("loc_30C4")

    label("loc_2FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3037")

    ChrTalk(    #142
        0xFE,
        (
            "Shame they don't use airships\x01",
            "for transporting goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Only royalty gets to fly to\x01",
            "the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C4")

    label("loc_3037")

    OP_A2(0xA)

    ChrTalk(    #144
        0xFE,
        (
            "Just about time to check\x01",
            "our inventory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Once the order's assembled,\x01",
            "we'll take all the goods to the\x01",
            "Republic via the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C4")

    TalkEnd(0xFE)
    Return()

    # Function_13_2AD8 end

    def Function_14_30C8(): pass

    label("Function_14_30C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_30F2")

    ChrTalk(    #146
        0xFE,
        "What's causing that smoke?\x02",
    )

    CloseMessageWindow()

    label("loc_30F2")

    TalkEnd(0xFE)
    Return()

    # Function_14_30C8 end

    def Function_15_30F6(): pass

    label("Function_15_30F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_31CE")

    ChrTalk(    #147
        0xFE,
        (
            "I heard the ones who attacked\x01",
            "the central factory were\x01",
            "members of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "My Vince said he saw soldiers\x01",
            "in blue uniforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I couldn't believe it, but Vince\x01",
            "isn't one to tell lies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_31F6")

    ChrTalk(    #150
        0xFE,
        "It's not a fire, is it?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_31F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_32B0")

    ChrTalk(    #151
        0xFE,
        (
            "My son's got a point... There's faaaar\x01",
            "too much planter space up here, and not\x01",
            "enough flowers to fill it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "I wonder if Sotiria would part\x01",
            "with a few flowers for me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_32B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3328")
    TurnDirection(0x9, 0xB, 0)

    ChrTalk(    #153
        0xFE,
        "Vince, dear, what do you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Isn't the color balance for this\x01",
            "flower bed nice?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_3328")

    OP_A2(0x1)

    ChrTalk(    #155
        0xFE,
        (
            "My husband said all the orbments\x01",
            "stopped running yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "Is that even possible?\x02",
    )

    CloseMessageWindow()

    label("loc_3388")

    TalkEnd(0xFE)
    Return()

    # Function_15_30F6 end

    def Function_16_338C(): pass

    label("Function_16_338C")

    TalkBegin(0xFE)

    ChrTalk(    #157
        0xFE,
        "I think my mom might be wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I wanna be a receptionist in\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I should be able to get a position\x01",
            "easily enough. That Hazel's\x01",
            "getting old.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_338C end

    def Function_17_343F(): pass

    label("Function_17_343F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_35B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_34E0")

    ChrTalk(    #160
        0xFE,
        (
            "I wonder if the central factory\x01",
            "will tighten security after this\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I don't know if I'd like it if\x01",
            "things get too strict...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B6")

    label("loc_34E0")

    OP_A2(0x3)

    ChrTalk(    #162
        0xFE,
        (
            "A group of soldiers wearing\x01",
            "blue uniforms ran past me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Judging from the time of the\x01",
            "attack on the central factory,\x01",
            "I'm sure they were involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "It's too bad I didn't have an\x01",
            "orbal camera with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B6")

    Jump("loc_38D5")

    label("loc_35B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_363B")

    ChrTalk(    #165
        0xFE,
        (
            "What is that smoke? It doesn't\x01",
            "look like it's from a fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Maybe some experimental device\x01",
            "is releasing gas?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D5")

    label("loc_363B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_37E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3733")

    ChrTalk(    #167
        0xFE,
        (
            "If I had the chance, I'd love to\x01",
            "study the phenomenon using\x01",
            "the archives room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Of course, Constance from\x01",
            "Archives would need to finish\x01",
            "reorganizing everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "It's going to take so long to\x01",
            "figure out the cause...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_3733")

    OP_A2(0x3)

    ChrTalk(    #170
        0xFE,
        "Total orbal shutdown...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I've never even seen any records\x01",
            "of such an event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "If some experiment was the cause,\x01",
            "I wonder exactly what kind of\x01",
            "experiment it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E3")

    Jump("loc_38D5")

    label("loc_37E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3841")
    TurnDirection(0xFE, 0x9, 0)

    ChrTalk(    #173
        0xFE,
        "By the way, Mother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "Did you change the flower bed?\x02",
    )

    CloseMessageWindow()
    Jump("loc_38D5")

    label("loc_3841")

    OP_A2(0x3)

    ChrTalk(    #175
        0xFE,
        "An orbal blackout...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Something like that wasn't in\x01",
            "the first edition theses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "I suppose I need to find more\x01",
            "specialized documents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D5")

    TalkEnd(0xFE)
    Return()

    # Function_17_343F end

    def Function_18_38D9(): pass

    label("Function_18_38D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3A17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3983")

    ChrTalk(    #178
        0xFE,
        (
            "They have everything at that\x01",
            "Eastern-style hot spring resort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "I actually love everything\x01",
            "related to the Far East!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "Ooh, I'm so excited!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A14")

    label("loc_3983")

    OP_A2(0x4)

    ChrTalk(    #181
        0xFE,
        (
            "I hear there's a hot spring\x01",
            "resort near here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "I wanna go see it! But I guess\x01",
            "I'll wait until we check this\x01",
            "place out a little more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A14")

    Jump("loc_3A9E")

    label("loc_3A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A66")

    ChrTalk(    #183
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Can somebody get me on\x01",
            "this crazy thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9E")

    label("loc_3A66")

    OP_A2(0x4)

    ChrTalk(    #185
        0xFE,
        "That's incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "A staircase that moves.\x02",
    )

    CloseMessageWindow()

    label("loc_3A9E")

    TalkEnd(0xFE)
    Return()

    # Function_18_38D9 end

    def Function_19_3AA2(): pass

    label("Function_19_3AA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3B58")

    ChrTalk(    #187
        0xFE,
        "Okay, let's arrange cans today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "First move all the unsold cans\x01",
            "to the front right. There.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Make the goods you want to\x01",
            "sell easy to get at. Get it? \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C27")

    label("loc_3B58")

    OP_A2(0x5)

    ChrTalk(    #190
        0xFE,
        (
            "I thought it might be time to\x01",
            "teach my brother Didi about\x01",
            "item display...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "...but I guess it's too early.\x01",
            "He just gets bored and quits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "*sigh* I guess I'll have to do\x01",
            "it myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)

    label("loc_3C27")

    Jump("loc_43E3")

    label("loc_3C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3CA0")

    ChrTalk(    #193
        0xFE,
        "Didi, you're moving it too far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "If you set it like that you'll\x01",
            "destroy the entire balance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D27")

    label("loc_3CA0")

    OP_A2(0x5)

    ChrTalk(    #195
        0xFE,
        (
            "I think it'd look better if\x01",
            "you moved those cans over\x01",
            "there, a little to the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Didi! Set it up the way I told\x01",
            "you to!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D27")

    Jump("loc_43E3")

    label("loc_3D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3DB9")

    ChrTalk(    #197
        0xFE,
        (
            "I'm thinking it's time to get\x01",
            "my brother working in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "I want to teach him about all\x01",
            "the facets of item display!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E2F")

    label("loc_3DB9")

    OP_A2(0x5)

    ChrTalk(    #199
        0xFE,
        "Listen up, Didi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "You have to put merchandise\x01",
            "the customers have moved\x01",
            "back to their original place.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_3E2F")

    Jump("loc_43E3")

    label("loc_3E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_406C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3EAE")

    ChrTalk(    #201
        0xFE,
        (
            "I'd forgotten how dark it\x01",
            "actually gets at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "It was kind of scary looking\x01",
            "out the window...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4069")

    label("loc_3EAE")

    OP_A2(0x5)
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(    #203
        0xFE,
        "Oh, Tita. It's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Yesterday sure was something\x01",
            "else, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Did the orbments at your house \x01",
            "all suddenly stop, too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0xD, 400)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #206
        0x107,
        (
            "#061FUhh, uh...\x02\x03",

            "Y-Yeah, they did. We were all\x01",
            "...surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Yeah, they stopped all over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "It was scary, looking out and\x01",
            "seeing the whole town dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I'd forgotten how dark it got \x01",
            "at night without orbal lights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x107,
        "#067FY-You know it.\x02",
    )

    CloseMessageWindow()

    label("loc_4069")

    Jump("loc_43E3")

    label("loc_406C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_40D7")

    ChrTalk(    #211
        0xFE,
        "Oh, that's just awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "Let's move all those cans to\x01",
            "the left a little bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4317")

    label("loc_40D7")

    OP_A2(0x5)
    OP_63(0xD)

    ChrTalk(    #213
        0xFE,
        "Proper item display is ESSENTIAL.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "The balance is still all off...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(    #215
        0xFE,
        "Huh? Oh, Tita, it's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "Got work at the central factory\x01",
            "again today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x107,
        (
            "#560FUh, yeah.\x02\x03",

            "You're helping out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "Yeah, I'm in charge of merchandise\x01",
            "display.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "My dad doesn't have a lick of\x01",
            "sense about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x107,
        (
            "#560FOh, so you're the one who keeps\x01",
            "everything lined up so nice and\x01",
            "straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "Heheh.\x01",
            "Yep! That's all me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "Okay, next is the fruit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "See you at school on Sunday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x107,
        (
            "#061FOkay. See you then.\x02\x03",

            "Don't forget to finish your\x01",
            "homework this time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4317")

    Jump("loc_43E3")

    label("loc_431A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4381")

    ChrTalk(    #225
        0xFE,
        "What a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "We'll have to restack the cans\x01",
            "again, starting on the right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E3")

    label("loc_4381")

    OP_A2(0x5)

    ChrTalk(    #227
        0xFE,
        "The balance is all off again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "Maybe if I moved that can on\x01",
            "the left a little more...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E3")

    TalkEnd(0xFE)
    Return()

    # Function_19_3AA2 end

    def Function_20_43E7(): pass

    label("Function_20_43E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4448")

    ChrTalk(    #229
        0xFE,
        "This is so BORING!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "I can't believe my brother\x01",
            "actually enjoys doing this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F7")

    label("loc_4448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_44F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_44BF")
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #231
        0xFE,
        (
            "Activate Orbal Engines! \x01",
            "Commence Apple Shrinkage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "Beeep, bweeeeep...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "Ka-chink!\x02",
    )

    CloseMessageWindow()
    Jump("loc_44F7")

    label("loc_44BF")

    OP_A2(0x6)

    ChrTalk(    #234
        0xFE,
        "Okay, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "Message received, Dr. Knowles.\x02",
    )

    CloseMessageWindow()

    label("loc_44F7")

    TalkEnd(0xFE)
    Return()

    # Function_20_43E7 end

    def Function_21_44FB(): pass

    label("Function_21_44FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4572")
    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #236
        0x102,
        (
            "#010FFirst, we need to cancel\x01",
            "at the departure gate.\x02\x03",

            "I think we can leave from here.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4789")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465F")
    OP_A2(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #237
        0x101,
        (
            "#006FThe highway...\x02\x03",

            "#502FWoohoo! No walking this time! ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #238
        0x102,
        (
            "#010FYeah, it's kind of odd...\x02\x03",

            "But no time to muse on that\x01",
            "right now--we've got a flight\x01",
            "to catch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#001FYeah, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4782")

    label("loc_465F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A5")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #240
        0x102,
        (
            "#010FWe've got a flight to catch,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4782")

    label("loc_46A5")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #241
        0x102,
        (
            "#010FThe highway is this way.\x02\x03",

            "I could keep going, but it's\x01",
            "probably best to wait.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #242
        0x101,
        (
            "#007FYeah, I have to agree.\x02\x03",

            "Since we went to all this trouble\x01",
            "to take this trip, I really don't\x01",
            "want to be late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4782")

    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4959")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_487C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482C")
    OP_A2(0xE)

    ChrTalk(    #243
        0x101,
        (
            "#000FAh... Yeah, it's about time we\x01",
            "report in at the guild.\x02\x03",

            "We could learn something new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        "#010FRight. Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4879")

    label("loc_482C")


    ChrTalk(    #245
        0x101,
        (
            "#000FFor now, we should go\x01",
            "to the guild.\x02\x03",

            "We could learn something new.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4879")

    Jump("loc_4952")

    label("loc_487C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48FB")
    OP_A2(0xE)

    ChrTalk(    #246
        0x102,
        (
            "#010FFor now, we should head to\x01",
            "the guild.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        "#000FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4952")

    label("loc_48FB")


    ChrTalk(    #248
        0x102,
        (
            "#010FFor now, we should head to\x01",
            "the guild.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4952")

    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC4")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4C")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49DD")

    ChrTalk(    #249
        0x106,
        (
            "#050FBah... Chasing them turned\x01",
            "up nothing useful.\x02\x03",

            "We'd better get back to\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A49")

    label("loc_49DD")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #250
        0x106,
        (
            "#050FHey, where do you think\x01",
            "you're going?\x02\x03",

            "Let's get to the guild, and\x01",
            "don't spare the horses.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A49")

    Jump("loc_4ABD")

    label("loc_4A4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A62")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_4A69")

    label("loc_4A62")

    TurnDirection(0x106, 0x0, 400)

    label("loc_4A69")


    ChrTalk(    #251
        0x106,
        (
            "#050FChasing them turned up nothing\x01",
            "useful. We'd better get back\x01",
            "to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ABD")

    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BF6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B30")

    ChrTalk(    #252
        0x101,
        (
            "#002FOh, the highway is this way...\x01",
            "We need to go to the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BEF")

    label("loc_4B30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B8B")

    ChrTalk(    #253
        0x102,
        (
            "#012FSomething's up at the central\x01",
            "factory... We'd better hurry\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BEF")

    label("loc_4B8B")


    ChrTalk(    #254
        0x107,
        (
            "#062FSomething strange is going on\x01",
            "at the central factory. We'd\x01",
            "better hurry and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BEF")

    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D64")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD5")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(    #255
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "You DID make a note of what it\x01",
            "is we're delivering, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #256
        0x101,
        (
            "#009FD-Don't be a jerk!\x02\x03",

            "Of course I wrote it down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5D")

    label("loc_4CD5")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #257
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "For now, we need to focus on\x01",
            "getting that thing up and running.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D5D")

    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D88")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_4D8F")

    label("loc_4D88")

    TurnDirection(0x107, 0x0, 400)

    label("loc_4D8F")


    ChrTalk(    #258
        0x107,
        (
            "#060FUmm, the highway is this way.\x02\x03",

            "The central factory is on\x01",
            "the north side of town.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E76")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E15")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_4E1C")

    label("loc_4E15")

    TurnDirection(0x107, 0x0, 400)

    label("loc_4E1C")


    ChrTalk(    #259
        0x107,
        (
            "#060FThis leads out to the highway\x01",
            "to Grancel.\x02\x03",

            "My house is to the southwest.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 23)
    Jump("loc_4FA7")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2F")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(    #260
        0x102,
        (
            "#010FBefore we leave, we should\x01",
            "check in at the guild.\x02\x03",

            "There's a lot that I want\x01",
            "to discuss with them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #261
        0x101,
        "#000FThat sounds fine to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FA3")

    label("loc_4F2F")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #262
        0x102,
        (
            "#010FBefore we leave, we should\x01",
            "check in at the guild.\x02\x03",

            "There's a lot that I want\x01",
            "to discuss with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA3")

    Call(0, 23)

    label("loc_4FA7")

    Return()

    # Function_21_44FB end

    def Function_22_4FA8(): pass

    label("Function_22_4FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_501F")
    EventBegin(0x2)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #263
        0x102,
        (
            "#010FFirst, we need to cancel\x01",
            "at the departure gate.\x02\x03",

            "I think we can leave from here.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_501F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5224")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5119")
    OP_A2(0xE)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #264
        0x101,
        (
            "#006FSo this is the highway...\x02\x03",

            "#502FWoohoo!♪  And we don't even\x01",
            "have to walk, this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #265
        0x102,
        (
            "#010FYeah, it does feel a\x01",
            "little strange here.\x02\x03",

            "Okay, let's go over to the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#001FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_521D")

    label("loc_5119")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5158")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #267
        0x102,
        (
            "#010FLet's go to the gate,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_521D")

    label("loc_5158")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #268
        0x102,
        (
            "#010FThe plains road is this way.\x02\x03",

            "I could keep going, but it's\x01",
            "probably best to wait.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #269
        0x101,
        (
            "#007FFirst, we need to cancel\x01",
            "at the departure gate.\x02\x03",

            "I think we can leave from here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_521D")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546A")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F6")
    OP_A2(0xE)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #270
        0x102,
        (
            "#017FYou're going the wrong\x01",
            "way, Estelle.\x02\x03",

            "To reach Leiston Fortress, we have\x01",
            "to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #271
        0x101,
        "#004FOh... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        "#018FI swear...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5376")

    label("loc_52F6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #273
        0x102,
        (
            "#017FTo reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02\x03",

            "Didn't you just write this\x01",
            "down in your notes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5376")

    Jump("loc_5463")

    label("loc_5379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F4")
    OP_A2(0xE)

    ChrTalk(    #274
        0x102,
        (
            "#012FThis way is the Tratt Plains Road.\x02\x03",

            "To reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5463")

    label("loc_53F4")


    ChrTalk(    #275
        0x102,
        (
            "#012FThis way is the Tratt Plains Road...\x02\x03",

            "To reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5463")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_546A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5678")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5519")
    OP_A2(0xE)

    ChrTalk(    #276
        0x101,
        (
            "#000FAh... Yeah, it's about time we\x01",
            "report in at the guild.\x02\x03",

            "We don't have any new \x01",
            "intel to report...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x102,
        "#010FRight. Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5572")

    label("loc_5519")


    ChrTalk(    #278
        0x101,
        (
            "#000FFor now, we should go to\x01",
            "the guild.\x02\x03",

            "We don't have any new \x01",
            "intel to report...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5572")

    Jump("loc_5671")

    label("loc_5575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5607")
    OP_A2(0xE)

    ChrTalk(    #279
        0x102,
        (
            "#010FWe should go to the guild and\x01",
            "see what they have to say.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        "#000FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5671")

    label("loc_5607")


    ChrTalk(    #281
        0x102,
        (
            "#010FWe should go to the guild and\x01",
            "see what they have to say.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5671")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57E3")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576B")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56FC")

    ChrTalk(    #282
        0x106,
        (
            "#050FBah... Chasing them turned\x01",
            "up nothing useful.\x02\x03",

            "We'd better get back to\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5768")

    label("loc_56FC")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #283
        0x106,
        (
            "#050FHey, where do you think\x01",
            "you're going?\x02\x03",

            "Let's get to the guild, and\x01",
            "don't spare the horses.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5768")

    Jump("loc_57DC")

    label("loc_576B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5781")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5788")

    label("loc_5781")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5788")


    ChrTalk(    #284
        0x106,
        (
            "#050FChasing them turned up nothing\x01",
            "useful. We'd better get back\x01",
            "to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DC")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_57E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5915")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_584F")

    ChrTalk(    #285
        0x101,
        (
            "#002FOh, the highway is this way...\x01",
            "We need to go to the central\x01",
            "factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_590E")

    label("loc_584F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58AA")

    ChrTalk(    #286
        0x102,
        (
            "#012FSomething's up at the central\x01",
            "factory... We'd better hurry\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_590E")

    label("loc_58AA")


    ChrTalk(    #287
        0x107,
        (
            "#062FSomething strange is going on\x01",
            "at the central factory. We'd\x01",
            "better hurry and check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590E")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A83")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59F4")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(    #288
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "You DID make a note of what it\x01",
            "is we're delivering, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #289
        0x101,
        (
            "#009FD-Don't be a jerk!\x02\x03",

            "Of course I wrote it down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A7C")

    label("loc_59F4")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #290
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "For now, we need to focus on\x01",
            "getting that thing up and running.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7C")

    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B11")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA7")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_5AAE")

    label("loc_5AA7")

    TurnDirection(0x107, 0x0, 400)

    label("loc_5AAE")


    ChrTalk(    #291
        0x107,
        (
            "#060FOh, the highway is this way...\x02\x03",

            "The central factory is on\x01",
            "the north side of town.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B90")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B35")
    TurnDirection(0x107, 0x1, 400)
    Jump("loc_5B3C")

    label("loc_5B35")

    TurnDirection(0x107, 0x0, 400)

    label("loc_5B3C")


    ChrTalk(    #292
        0x107,
        (
            "#060FThis way goes to the plains road...\x02\x03",

            "My house is to the southwest.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jump("loc_5CC1")

    label("loc_5B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C49")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0xE)

    ChrTalk(    #293
        0x102,
        (
            "#010FBefore we leave, we should\x01",
            "check in at the guild.\x02\x03",

            "There's a lot that I want\x01",
            "to discuss with them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #294
        0x101,
        "#000FThat sounds fine to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CBD")

    label("loc_5C49")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #295
        0x102,
        (
            "#010FBefore we leave, we should\x01",
            "check in at the guild.\x02\x03",

            "There's a lot that I want\x01",
            "to discuss with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CBD")

    Call(0, 24)

    label("loc_5CC1")

    Return()

    # Function_22_4FA8 end

    def Function_23_5CC2(): pass

    label("Function_23_5CC2")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_23_5CC2 end

    def Function_24_5CDE(): pass

    label("Function_24_5CDE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_24_5CDE end

    def Function_25_5CFA(): pass

    label("Function_25_5CFA")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_67(0, 5600, -10000, 0)
    OP_6D(58400, 3900, 51600, 0)
    OP_6B(4700, 0)
    OP_6C(276000, 0)

    def lambda_5D3B():
        OP_6D(57400, 3900, 23700, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3B)
    OP_6C(204000, 6000)

    def lambda_5D5C():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D5C)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_5CFA end

    def Function_26_5D83(): pass

    label("Function_26_5D83")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(60080, 0, 26320, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 60090, 0, 27140, 180)
    SetChrPos(0x102, 60590, 0, 25950, 315)
    SetChrPos(0x107, 59500, 0, 26070, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #296
        0x101,
        (
            "#001FAaaand now that we've\x01",
            "had a good breakfast...\x02\x03",

            "Off to the central factory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        (
            "#010FBefore we do that, I'd like\x01",
            "to check in at the guild.\x02\x03",

            "I think it might be best to report\x01",
            "on what happened yesterday, just\x01",
            "to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        (
            "#006FWell, okay...\x02\x03",

            "Hey, Tita... Would you mind if\x01",
            "we stopped by there on our way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x107,
        "#061F#4PSure, go ahead.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_26_5D83 end

    def Function_27_5F78(): pass

    label("Function_27_5F78")

    EventBegin(0x0)
    OP_6D(66850, 0, 53050, 0)
    OP_6C(270000, 0)
    SetChrPos(0x101, 66140, 0, 53000, 270)
    SetChrPos(0x107, 66790, 0, 52290, 270)
    SetChrPos(0x102, 66830, 0, 53720, 270)
    SetChrPos(0x110, 67900, 0, 52960, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #300
        0x101,
        "#004FHuh...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #301
        0x107,
        "#064FWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        (
            "#505FMaybe I'm just losing it, but\x01",
            "I thought I heard something...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #303
        0x102,
        (
            "#012FYou're not losing it. At least, not\x01",
            "because of that. I heard something\x01",
            "too, but far off.\x02\x03",

            "From the direction of the factory.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_612A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_612A)

    def lambda_6138():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6138)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #304
        0x107,
        "#065FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x110,
        (
            "#154FOh, no...\x01",
            "What do you mean?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        (
            "#002FI don't know... We'll just\x01",
            "have to go and see.\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0xD)
    EventEnd(0x0)
    Return()

    # Function_27_5F78 end

    def Function_28_61BF(): pass

    label("Function_28_61BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6480")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6389")
    OP_A2(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6295")
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(    #307
        0x102,
        (
            "#010FHold on a second, Tita.\x02\x03",

            "I know it's not part of the \x01",
            "original plan, but I want to\x01",
            "stop by the guild on our way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #308
        0x107,
        "#060FOh...uh, sure. No problem.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6386")

    label("loc_6295")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #309
        0x102,
        (
            "#010FI know it's not part of the \x01",
            "original plan, but I want to\x01",
            "stop by the guild on our way.\x02\x03",

            "I think it might be best to report\x01",
            "on what happened yesterday, just\x01",
            "to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #310
        0x101,
        "#000FYeah, you might be right.\x02",
    )

    CloseMessageWindow()

    label("loc_6386")

    Jump("loc_6465")

    label("loc_6389")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_639F")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_63A6")

    label("loc_639F")

    TurnDirection(0x102, 0x0, 400)

    label("loc_63A6")


    ChrTalk(    #311
        0x102,
        (
            "#010FI know it's not part of the \x01",
            "original plan, but I want to\x01",
            "stop by the guild on our way.\x02\x03",

            "I think it might be best to report\x01",
            "on what happened yesterday, just\x01",
            "to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6465")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6480")

    Return()

    # Function_28_61BF end

    def Function_29_6481(): pass

    label("Function_29_6481")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #312
        (
            "\x07\x05'First Orbally-Powered Clock'\x01",
            "Made in year 1162 of the Septian Calendar,\x01",
            "by Zeissian manufacturers.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_29_6481 end

    def Function_30_650F(): pass

    label("Function_30_650F")

    SetPlaceName(0x7D)
    Return()

    # Function_30_650F end

    def Function_31_6513(): pass

    label("Function_31_6513")

    SetPlaceName(0x7F)
    Return()

    # Function_31_6513 end

    def Function_32_6517(): pass

    label("Function_32_6517")

    SetPlaceName(0x82)
    Return()

    # Function_32_6517 end

    def Function_33_651B(): pass

    label("Function_33_651B")

    SetPlaceName(0x7C)
    Return()

    # Function_33_651B end

    def Function_34_651F(): pass

    label("Function_34_651F")

    SetPlaceName(0x7A)
    Return()

    # Function_34_651F end

    def Function_35_6523(): pass

    label("Function_35_6523")

    SetPlaceName(0x7B)
    Return()

    # Function_35_6523 end

    def Function_36_6527(): pass

    label("Function_36_6527")

    SetPlaceName(0x80)
    Return()

    # Function_36_6527 end

    SaveToFile()

Try(main)
