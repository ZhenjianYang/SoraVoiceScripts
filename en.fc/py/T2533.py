from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2533   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2533.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Mr. Ratio',                            # 11
        'Ms. Wiola',                            # 12
        'Ms. Millia',                           # 13
        'Mr. Effort',                           # 14
        'Rhody',                                # 15
        'Mickey',                               # 16
        'Mickey',                               # 17
        'Alice',                                # 18
        'Purity',                               # 19
        'Taylor',                               # 20
        'Logic',                                # 21
        'Argyle',                               # 22
        'Roy',                                  # 23
        'Monika',                               # 24
        'Thelma',                               # 25
        'Richelle',                             # 26
        'Patrick',                              # 27
        'Gerome',                               # 28
        'Dennis',                               # 29
        'Nikita',                               # 30
        'Felicity',                             # 31
        'Reina',                                # 32
        'Janitor Parkes',                       # 33
        'Maid Rainey',                          # 34
        'Maid Laurel',                          # 35
        'Duke Radmont',                         # 36
        'Chairman Claude',                      # 37
        'Archbishop',                           # 38
        'Assassin',                             # 39
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
        'ED6_DT07/CH01660 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01430 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01080 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01090 ._CH',             # 0A
        'ED6_DT07/CH01370 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH02260 ._CH',             # 0E
        'ED6_DT07/CH02270 ._CH',             # 0F
        'ED6_DT07/CH02280 ._CH',             # 10
        'ED6_DT07/CH01350 ._CH',             # 11
        'ED6_DT07/CH02540 ._CH',             # 12
        'ED6_DT07/CH01220 ._CH',             # 13
        'ED6_DT07/CH01570 ._CH',             # 14
        'ED6_DT07/CH01670 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT06/CH20069 ._CH',             # 17
        'ED6_DT06/CH20071 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01660P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01430P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01080P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01090P._CP',             # 0A
        'ED6_DT07/CH01370P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH02260P._CP',             # 0E
        'ED6_DT07/CH02270P._CP',             # 0F
        'ED6_DT07/CH02280P._CP',             # 10
        'ED6_DT07/CH01350P._CP',             # 11
        'ED6_DT07/CH02540P._CP',             # 12
        'ED6_DT07/CH01220P._CP',             # 13
        'ED6_DT07/CH01570P._CP',             # 14
        'ED6_DT07/CH01670P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT06/CH20069P._CP',             # 17
        'ED6_DT06/CH20071P._CP',             # 18
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 66040,
        Z                   = 1000,
        Y                   = 16210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 9300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -6300,
        Z                   = 0,
        Y                   = 300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5900,
        Z                   = 0,
        Y                   = 3800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4100,
        Z                   = 0,
        Y                   = -4200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -6300,
        Z                   = 0,
        Y                   = 6900,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4600,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 5900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -5700,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 7200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 6700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -5400,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 0,
        Y                   = 2700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 3400,
        Z                   = 0,
        Y                   = 3800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = 200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 1900,
        Z                   = 0,
        Y                   = 200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 0,
        Y                   = -1860,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 61850,
        Z                   = 1000,
        Y                   = 17310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63320,
        Z                   = 1000,
        Y                   = 15250,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57740,
        Z                   = 1000,
        Y                   = 16980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58590,
        Z                   = 1000,
        Y                   = 17010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59600,
        Z                   = 1000,
        Y                   = 16379,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56830,
        Z                   = 1000,
        Y                   = 16500,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_552",          # 00, 0
        "Function_1_678",          # 01, 1
        "Function_2_6A3",          # 02, 2
        "Function_3_820",          # 03, 3
        "Function_4_8C1",          # 04, 4
        "Function_5_9C8",          # 05, 5
        "Function_6_A21",          # 06, 6
        "Function_7_ABC",          # 07, 7
        "Function_8_B47",          # 08, 8
        "Function_9_BC5",          # 09, 9
        "Function_10_C50",         # 0A, 10
        "Function_11_C7D",         # 0B, 11
        "Function_12_D08",         # 0C, 12
        "Function_13_D75",         # 0D, 13
        "Function_14_DE0",         # 0E, 14
        "Function_15_E3A",         # 0F, 15
        "Function_16_ECF",         # 10, 16
        "Function_17_FEB",         # 11, 17
        "Function_18_1073",        # 12, 18
        "Function_19_10C9",        # 13, 19
        "Function_20_1133",        # 14, 20
        "Function_21_117E",        # 15, 21
        "Function_22_11FB",        # 16, 22
        "Function_23_1236",        # 17, 23
        "Function_24_13FC",        # 18, 24
        "Function_25_1571",        # 19, 25
        "Function_26_1669",        # 1A, 26
        "Function_27_1714",        # 1B, 27
        "Function_28_17A1",        # 1C, 28
        "Function_29_20B8",        # 1D, 29
    )


    def Function_0_552(): pass

    label("Function_0_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_55C")
    Jump("loc_652")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_600")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 320, 0, 4890, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1040, 0, 4970, 0)
    Jump("loc_652")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_60A")
    Jump("loc_652")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_652")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_61E")
    Jump("loc_652")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_62D")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_652")

    label("loc_62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_637")
    Jump("loc_652")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_652")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_652")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_652")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_660")
    OP_A3(0x3FA)
    Event(0, 28)

    label("loc_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_677")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 29)

    label("loc_677")

    Return()

    # Function_0_552 end

    def Function_1_678(): pass

    label("Function_1_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_699")
    OP_B1("t2533_y")
    Jump("loc_6A2")

    label("loc_699")

    OP_B1("t2533_n")

    label("loc_6A2")

    Return()

    # Function_1_678 end

    def Function_2_6A3(): pass

    label("Function_2_6A3")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_80A")

    label("loc_6C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_80A")

    label("loc_6E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_80A")

    label("loc_6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_80A")

    label("loc_713")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_80A")

    label("loc_72C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_745")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_80A")

    label("loc_745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_80A")

    label("loc_75E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_80A")

    label("loc_777")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_790")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_80A")

    label("loc_790")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_80A")

    label("loc_7A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_80A")

    label("loc_7C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_80A")

    label("loc_7DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_80A")

    label("loc_7F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_80A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_80A")

    label("loc_81F")

    Return()

    # Function_2_6A3 end

    def Function_3_820(): pass

    label("Function_3_820")

    TalkBegin(0xA)

    ChrTalk(    #0
        0xFE,
        (
            "A lot of the teachers and students\x01",
            "are really grateful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "This year's festival was truly\x01",
            "something that the royal\x01",
            "academy can boast about.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_3_820 end

    def Function_4_8C1(): pass

    label("Function_4_8C1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B")
    OP_A2(0x1)

    ChrTalk(    #2
        0xFE,
        "Ha ha...thank you...all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd love to kick back with a good, stiff\x01",
            "drink. Aidios knows I need it after seeing\x01",
            "Mr. Effort try on that princess costume...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C4")

    label("loc_97B")


    ChrTalk(    #4
        0xFE,
        (
            "When we're done here, I think I\x01",
            "might hit the town with Ms. Millia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C4")

    TalkEnd(0xB)
    Return()

    # Function_4_8C1 end

    def Function_5_9C8(): pass

    label("Function_5_9C8")

    TalkBegin(0xC)

    ChrTalk(    #5
        0xFE,
        "My, but you did a fantastic job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Good enough for me to give\x01",
            "you an 'A'.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_5_9C8 end

    def Function_6_A21(): pass

    label("Function_6_A21")

    TalkBegin(0xD)

    ChrTalk(    #7
        0xFE,
        (
            "I'm just glad that everything\x01",
            "concluded without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Tomorrow, the kids are going to\x01",
            "have to work harder than ever at\x01",
            "their lessons.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_6_A21 end

    def Function_7_ABC(): pass

    label("Function_7_ABC")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")
    OP_A2(0x4)

    ChrTalk(    #9
        0xFE,
        "And that's a launch, folks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Time to party like it's 1499!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B43")

    label("loc_B11")


    ChrTalk(    #11
        0xFE,
        "Classes start up again tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_B43")

    TalkEnd(0xE)
    Return()

    # Function_7_ABC end

    def Function_8_B47(): pass

    label("Function_8_B47")

    TalkBegin(0xF)

    ChrTalk(    #13
        0xFE,
        "The festival's over, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "So, why's everyone making\x01",
            "so much noise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "I just want to go home, already...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_8_B47 end

    def Function_9_BC5(): pass

    label("Function_9_BC5")

    TalkBegin(0x10)

    ChrTalk(    #16
        0xFE,
        (
            "I feel like we've really accomplished\x01",
            "something today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "To be honest, though, I had\x01",
            "the most fun while we were\x01",
            "setting up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_9_BC5 end

    def Function_10_C50(): pass

    label("Function_10_C50")

    TalkBegin(0x11)

    ChrTalk(    #18
        0xFE,
        "Hee hee...I love launch parties!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_10_C50 end

    def Function_11_C7D(): pass

    label("Function_11_C7D")

    TalkBegin(0x12)

    ChrTalk(    #19
        0xFE,
        (
            "We really didn't have much time,\x01",
            "but we just barely squeaked by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "All the guests seemed to enjoy\x01",
            "it, though, so I had fun.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_11_C7D end

    def Function_12_D08(): pass

    label("Function_12_D08")

    TalkBegin(0x13)

    ChrTalk(    #21
        0xFE,
        (
            "I've been SO busy lately, but I've\x01",
            "managed to pull it all off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "I feel pretty good about it.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_12_D08 end

    def Function_13_D75(): pass

    label("Function_13_D75")

    TalkBegin(0x14)

    ChrTalk(    #23
        0xFE,
        (
            "I look forward to going back\x01",
            "home to Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "...but days like today make\x01",
            "the wait easier.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_13_D75 end

    def Function_14_DE0(): pass

    label("Function_14_DE0")

    TalkBegin(0x15)

    ChrTalk(    #25
        0xFE,
        (
            "Everything turned out okay...darn.\x01",
            "I was really hoping for a tragic\x01",
            "ending...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_14_DE0 end

    def Function_15_E3A(): pass

    label("Function_15_E3A")

    TalkBegin(0x16)

    ChrTalk(    #26
        0xFE,
        (
            "The Fencing Club's ice cream shop\x01",
            "was super popular. People just\x01",
            "loved those Pom-shaped scoops!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "I'm glad those little kids had fun.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_15_E3A end

    def Function_16_ECF(): pass

    label("Function_16_ECF")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCD")
    OP_A2(0xD)

    ChrTalk(    #28
        0xFE,
        "Ahh, that was the best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I think the festival is enjoyable because\x01",
            "it only happens once a year and everyone\x01",
            "puts so much work into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "If we tried to keep up that pace\x01",
            "throughout the year, we'd all\x01",
            "get seriously burnt out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE7")

    label("loc_FCD")


    ChrTalk(    #31
        0xFE,
        "Ahh, that was great!\x02",
    )

    CloseMessageWindow()

    label("loc_FE7")

    TalkEnd(0x17)
    Return()

    # Function_16_ECF end

    def Function_17_FEB(): pass

    label("Function_17_FEB")

    TalkBegin(0x18)

    ChrTalk(    #32
        0xFE,
        (
            "Ha ha...there's nothing quite like\x01",
            "participating in a big event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "The important thing is to be\x01",
            "there for everyone else.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_17_FEB end

    def Function_18_1073(): pass

    label("Function_18_1073")

    TalkBegin(0x19)

    ChrTalk(    #34
        0xFE,
        "Oh, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "The play and the ice cream shop\x01",
            "were big hits. I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_18_1073 end

    def Function_19_10C9(): pass

    label("Function_19_10C9")

    TalkBegin(0x1A)

    ChrTalk(    #36
        0xFE,
        "Ha ha...and that makes me happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "The play was great. Thanks to all\x01",
            "of you for your help.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_19_10C9 end

    def Function_20_1133(): pass

    label("Function_20_1133")

    TalkBegin(0x1B)

    ChrTalk(    #38
        0xFE,
        "*sigh* Man, I'm beat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I can't wait to get home and sleep.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_20_1133 end

    def Function_21_117E(): pass

    label("Function_21_117E")

    TalkBegin(0x1C)

    ChrTalk(    #40
        0xFE,
        (
            "I wonder if it's okay to take a\x01",
            "break from studying for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "It just has a tendency to pile\x01",
            "up on me...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_21_117E end

    def Function_22_11FB(): pass

    label("Function_22_11FB")

    TalkBegin(0x1D)

    ChrTalk(    #42
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Gerome is goofing off again...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_22_11FB end

    def Function_23_1236(): pass

    label("Function_23_1236")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(    #44
        0x1E,
        (
            "It's because of you that I practically\x01",
            "worked myself to death!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x1E,
        (
            "I should send you off to the old\x01",
            "man, or someone equally scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1F,
        (
            "Ha ha...I'm honored by your\x01",
            "kind words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1F,
        (
            "You know I only pushed you because I knew\x01",
            "you could handle it, right? And that it\x01",
            "would make you a better person!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_13F8")

    label("loc_137C")


    ChrTalk(    #48
        0x1E,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x1F,
        (
            "What's with the sigh? If you need\x01",
            "someone to talk to, you know I'm\x01",
            "here for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1E,
        "Someone, shoot me...\x02",
    )

    CloseMessageWindow()

    label("loc_13F8")

    TalkEnd(0x1E)
    Return()

    # Function_23_1236 end

    def Function_24_13FC(): pass

    label("Function_24_13FC")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1542")
    OP_A2(0x14)
    OP_A2(0x15)

    ChrTalk(    #51
        0x1E,
        (
            "It's because of you that I practically\x01",
            "worked myself to death!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1E,
        (
            "I should send you off to the old man,\x01",
            "or someone equally scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1F,
        (
            "Ha ha...I'm honored by your\x01",
            "kind words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x1F,
        (
            "You know I only pushed you because I knew\x01",
            "you could handle it, right? And that it\x01",
            "would make you a better person!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    Jump("loc_156D")

    label("loc_1542")


    ChrTalk(    #55
        0xFE,
        (
            "Ha ha ha...\x01",
            "(I love torturing her...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156D")

    TalkEnd(0x1F)
    Return()

    # Function_24_13FC end

    def Function_25_1571(): pass

    label("Function_25_1571")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1608")
    OP_A2(0x16)

    ChrTalk(    #56
        0xFE,
        (
            "#640FOh...I didn't know you were\x01",
            "still here.\x02\x03",

            "Don't you have to go back\x01",
            "to Ruan?\x02\x03",

            "You're more than welcome to\x01",
            "join in, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1665")

    label("loc_1608")


    ChrTalk(    #57
        0xFE,
        (
            "#640FDon't you have to go back\x01",
            "to Ruan?\x02\x03",

            "You're more than welcome to\x01",
            "join in, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1665")

    TalkEnd(0x8)
    Return()

    # Function_25_1571 end

    def Function_26_1669(): pass

    label("Function_26_1669")

    TalkBegin(0x9)

    ChrTalk(    #58
        0xFE,
        (
            "#730FOh...are you planning to participate\x01",
            "in the launch?\x02\x03",

            "The teachers are paying for all\x01",
            "of it, so you might as well pinch\x01",
            "'em for what they're worth! Heh...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_26_1669 end

    def Function_27_1714(): pass

    label("Function_27_1714")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_179D")

    ChrTalk(    #59
        0xFE,
        (
            "We'd better make the best of\x01",
            "this afternoon, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Dean Collins said he'd be doing\x01",
            "safety inspections right about now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")

    TalkEnd(0x20)
    Return()

    # Function_27_1714 end

    def Function_28_17A1(): pass

    label("Function_28_17A1")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_6D(-410, 4000, -4600, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 850, 1000, 14010, 270)
    SetChrPos(0x105, -960, 1000, 14000, 90)
    SetChrPos(0x8, -80, 1000, 13250, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrChipByIndex(0x102, 16)
    FadeToBright(1000, 0)
    SetPlaceName(0x5F)
    OP_6D(910, 2000, 12490, 4000)
    Fade(500)
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x101, 61000, 1000, 14250, 225)
    SetChrPos(0x105, 59080, 1000, 14210, 135)
    SetChrPos(0x8, 60000, 1000, 13140, 45)
    SetChrPos(0x102, 67180, 1000, 16860, 270)
    SetChrPos(0x9, 67180, 1000, 16860, 270)
    OP_0D()

    ChrTalk(    #61
        0x101,
        (
            "#340F#2PSo...these are our costumes?\x02\x03",

            "I figured that if we're playing\x01",
            "knights, we'd be all armored up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#644F#3PWell, armor and a helmet won't\x01",
            "work so well if we want people\x01",
            "to see you ACT.\x02\x03",

            "That's why I decided to arrange\x01",
            "things so you'd be dressed more\x01",
            "like the Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#340F#2POhhh, I got it.\x02\x03",

            "#341FIt's perfect for Kloe.\x01",
            "She's petite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#351F#1PHa ha. Thank you so much.\x02\x03",

            "I think it suits you, also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#348F#2PHa ha... Really?\x02\x03",

            "Say, why are we dressed\x01",
            "in different colors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#350F#1PBecause I'm playing the\x01",
            "Azure Knight, Oscar.\x02\x03",

            "You're playing the Ruby\x01",
            "Knight, Julius.\x02\x03",

            "It makes the play more colorful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#340F#2PAhh, okay then...\x02\x03",

            "So what about Joshua...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#3PThe object of your affection\x01",
            "is the fair Princess Cecilia.\x02\x03",

            "Come on, Princess. This way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#3PW-Wait...\x01",
            "I'm not in the moment yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x0)

    def lambda_1C3D():
        OP_6D(61500, 2310, 14620, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C3D)

    def lambda_1C55():
        OP_6B(850, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C55)

    def lambda_1C65():

        label("loc_1C65")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C65")

    QueueWorkItem2(0x101, 1, lambda_1C65)

    def lambda_1C76():

        label("loc_1C76")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C76")

    QueueWorkItem2(0x105, 1, lambda_1C76)

    def lambda_1C87():

        label("loc_1C87")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C87")

    QueueWorkItem2(0x8, 1, lambda_1C87)

    def lambda_1C98():

        label("loc_1C98")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1C98")

    QueueWorkItem2(0x9, 1, lambda_1C98)

    def lambda_1CA9():
        OP_8F(0xFE, 0xF582, 0x3E8, 0x3B10, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1CA9)
    Sleep(800)

    def lambda_1CC9():
        OP_8F(0xFE, 0xF71C, 0x3E8, 0x3DFE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CC9)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 0)
    WaitChrThread(0x9, 0x2)
    Sleep(200)
    OP_8F(0x9, 0xF85C, 0x3E8, 0x378C, 0x7D0, 0x0)
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 315, 0)

    ChrTalk(    #70
        0x102,
        "#363F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#344F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        "#354F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "#643F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#367F#2PIf you're going to say\x01",
            "something, say it...\x02\x03",

            "Don't leave me in suspense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#340FWell, how should I put it...?\x02\x03",

            "#341FI think it looks perfect. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#351FI'm shocked.\x02\x03",

            "#358FYou look beautiful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "#731FIndeed. Such poise.\x02\x03",

            "Why, if I didn't know what's really\x01",
            "going on under there, I'd be smitten\x01",
            "at the very sight of you. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #78
        0x102,
        (
            "#368F#2PWell, thank you for being so\x01",
            "honest about it, at least.\x01",
            "I'M not so thrilled, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#659FHeh heh...\x01",
            "This is just as I'd hoped...\x02\x03",

            "I think everyone will be pretty\x01",
            "pleased with the casting.\x02\x03",

            "#641FCome on, everyone! Let's make\x01",
            "this play one to remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#341F#1P#1KYeeeeaah!\x02",
    )


    ChrTalk(    #81
        0x105,
        "#351F#1KAll right!\x02",
    )


    ChrTalk(    #82
        0x9,
        "#731F#1KMm-hmm...\x02",
    )

    Sleep(500)
    OP_56(0x1)

    ChrTalk(    #83
        0x102,
        "#367F#2PBoo hoo... *sniffle*\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    AnonymousTalk(    #84
        (
            "\x07\x05Afterward, Estelle and Joshua each slept\x01",
            "in their respective dormitories.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_66(0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2512   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_28_17A1 end

    def Function_29_20B8(): pass

    label("Function_29_20B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)

    AnonymousTalk(    #85
        "\x07\x05And the day before the festival...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_6D(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 610, 0, -360, 0)
    SetChrPos(0x102, -400, 0, 430, 0)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x101, 62000, 1000, 14000, 270)
    SetChrPos(0x105, 58000, 1000, 14000, 90)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_1D(0x61)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #86
        0x101,
        "Ruby Knight Julius",
        (
            "#424F#2PMy friend...I fear that\x01",
            "this was inevitable.\x02\x03",

            "Perhaps fate always intended\x01",
            "for us to meet in so base a\x01",
            "fashion.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x101, 23)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(    #87
        0x101,
        "Ruby Knight Julius",
        (
            "#421F#2PSpeak, that we may\x01",
            "both be unburdened!\x02\x03",

            "If nothing else, for\x01",
            "our beloved princess!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #88
        0x105,
        "Azure Knight Oscar",
        (
            "#359F#1PWe would cleave a path through\x01",
            "fate with our own hands...\x02\x03",

            "But at this moment, my words\x01",
            "and her smile seem lost...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #89
        0x101,
        "Ruby Knight Julius",
        (
            "#422F#2PHas fear clutched your heart,\x01",
            "Oscar?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #90
        0x105,
        "Azure Knight Oscar",
        (
            "#357F#1PBut what is this passion that\x01",
            "pierces me to the quick?\x02\x03",

            "Though I have no wish to fight\x01",
            "you again, it would seem that\x01",
            "I am left with little choice.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(    #91
        0x105,
        "Azure Knight Oscar",
        (
            "#352F#1PBefore this storm, by the\x01",
            "name of revolution, should\x01",
            "claim us both...\x02\x03",

            "Take up your sword, and\x01",
            "we shall let fate decide!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #92
        0x101,
        "Ruby Knight Julius",
        (
            "#420F#2PYes! And may the Goddess\x01",
            "above see our spirits as they\x01",
            "truly are!\x02\x03",

            "Come, then!\x01",
            "Let it be done!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #93
        0x105,
        "Azure Knight Oscar",
        "#356F#1PIndeed!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)
    OP_21()

    ChrTalk(    #94
        0x101,
        "#347F#2PWhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        "#357F#1PWhew...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x105, 15)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_1D(0xE)
    Sleep(500)

    ChrTalk(    #96
        0x101,
        (
            "#341F#2PWoohoo! ㈱\x02\x03",

            "I finally got through the\x01",
            "scene with no mistakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x105,
        (
            "#351F#1PHa ha. And a convincing\x01",
            "performance it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#346F#2PHa ha ha. I've got nothing\x01",
            "on you, though.\x02\x03",

            "I don't think you've\x01",
            "flubbed a single line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        (
            "#350F#1PWell, I've been familiar with\x01",
            "this script for a long time.\x02\x03",

            "I think I learned it at about\x01",
            "the same rate you're going.\x02\x03",

            "#351FI really appreciate you taking\x01",
            "the trouble to rehearse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#340F#2PIt's no big deal. You've kinda\x01",
            "been my guide through it all.\x02\x03",

            "I think you would make a great\x01",
            "bracer, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x105,
        "#355F#1PHa ha... You flatter me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)
    Sleep(500)

    def lambda_28C6():
        OP_6D(58730, 2850, 2760, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28C6)

    def lambda_28DE():
        OP_6C(18000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_28DE)

    def lambda_28EE():
        OP_67(0, 2930, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_28EE)
    Sleep(1000)

    def lambda_290B():
        OP_8E(0xFE, 0xE7D6, 0x3E8, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_290B)
    Sleep(500)
    OP_8C(0x101, 225, 400)

    def lambda_2932():
        OP_8E(0xFE, 0xECA4, 0x3E8, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2932)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #102
        0x105,
        (
            "#350FWe finally do this for real\x01",
            "tomorrow.\x02\x03",

            "I hope Matron Theresa and the\x01",
            "children will enjoy it...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(    #103
        0x101,
        (
            "#340F#4PHa ha... They really mean\x01",
            "a lot to you, don't they?\x02\x03",

            "#341FThey're like your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x105,
        "#353F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#344F#4PI'm sorry. Did I say\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(    #106
        0x105,
        (
            "#355FNo... You're exactly right.\x02\x03",

            "They're the ones who taught me\x01",
            "the real value of family...\x02\x03",

            "#350FBoth of my parents died\x01",
            "shortly after I was born.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#344F#4PWha...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(    #108
        0x105,
        (
            "#357F#1PI was left in the care of an\x01",
            "affluent relative. I never\x01",
            "wanted for anything...\x02\x03",

            "But I really had no idea what\x01",
            "having a family was like.\x02\x03",

            "#358FIt was ten years ago that\x01",
            "I met the matron...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#344F#2PTen years ago...\x02\x03",

            "#342FWas that during the Hundred\x01",
            "Days War?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        (
            "#359F#1PYes... That was when I came\x01",
            "to Ruan.\x02\x03",

            "Everyone I knew had scattered\x01",
            "trying to escape the Imperial\x01",
            "forces...\x02\x03",

            "Matron Theresa and her\x01",
            "husband, Joseph, took me in\x01",
            "and cared for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#343F#2PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x105,
        (
            "#358F#1PAfter the war ended, we\x01",
            "waited several months for\x01",
            "word to come of my relatives...\x02\x03",

            "She and Joseph were so kind\x01",
            "to me...\x02\x03",

            "#357FThat was when I first\x01",
            "understood...\x02\x03",

            "...what it must be like to\x01",
            "have a mother and father.\x02\x03",

            "And how it must be to have\x01",
            "a family to be with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#340F#2PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x105,
        (
            "#355F#1PI-I'm sorry...\x02\x03",

            "I've been rambling... You\x01",
            "must be bored to tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#346F#2PNo...not at all.\x02\x03",

            "#341FLet's really show everyone\x01",
            "tomorrow how it's done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x105,
        "#358F#1PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#346F#2PI was worried before, but\x01",
            "I'm really excited now.\x02\x03",

            "Jill and Hans sure have worked\x01",
            "hard on this, haven't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x105,
        (
            "#350F#1PHa ha... Yes, indeed.\x02\x03",

            "But I think Joshua has really\x01",
            "been the biggest help.\x02\x03",

            "I never expected him to\x01",
            "be such a good actor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#340F#2PY-Yeah...\x02\x03",

            "He acted all uninterested, but\x01",
            "he sure plays the role of the\x01",
            "spoiled princess well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x105,
        (
            "#350F#1PHe definitely nailed the mannerisms.\x01",
            "I've seen professionals turn in\x01",
            "worse performances.\x02\x03",

            "Does he have any experience\x01",
            "in theater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#343F#2PHmm...\x02\x03",

            "I don't really know much about\x01",
            "his life before I met him...\x02\x03",

            "Whatever went on back then,\x01",
            "he's never wanted to talk\x01",
            "about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x105,
        (
            "#353F#1POh...\x02\x03",

            "I'm sorry... I don't mean to pry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#340F#2PHa ha ha...\x01",
            "Don't sweat it.\x02\x03",

            "#346FHe's always been the type\x01",
            "to be good at whatever\x01",
            "he does.\x02\x03",

            "He's always so calm and collected.\x02\x03",

            "Sometimes he gets flustered,\x01",
            "though, and that's when he's\x01",
            "really cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x105,
        (
            "#355F#1P*giggle*\x02\x03",

            "#357F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#340F#2PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#359F#1PPerhaps our roles should\x01",
            "have been reversed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#344F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x105,
        (
            "#353F#1PJulius and Oscar.\x02\x03",

            "Somehow I think you would have\x01",
            "preferred to play Oscar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#340F#2PUh, how come?\x02\x03",

            "Well, maybe. I mean, Julius is\x01",
            "the son of a noble, and I sure\x01",
            "don't know anything about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x105,
        (
            "#353F#1PThat's not what I mean.\x02\x03",

            "#355FIt's more about...umm,\x01",
            "you know...the ending...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#344F#2POh...\x01",
            "You mean how Oscar gets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#355F#1PR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#348F#2PW-Well, it's just Joshua...\x02\x03",

            "And hey, do you mean you\x01",
            "wouldn't like kissing Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x105,
        (
            "#354F#1PD-Don't be ridiculous!\x02\x03",

            "#359FStill, it does seem rather risque...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#348F#2PC-Come on. You're starting\x01",
            "to sound like Jill.\x02\x03",

            "#343FAnd besides, Joshua just sees\x01",
            "me like a little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x105,
        "#353F#1PDoes he...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#347F#2PHe's always treated me like a\x01",
            "little kid, especially with my\x01",
            "dad around.\x02\x03",

            "It drives me nuts...\x02\x03",

            "#346FAnyway, there's absolutely\x01",
            "nothing like that going on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x105,
        "#354F#1PO-Okay...\x02",
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    SetChrPos(0x9, 65530, 0, 570, 0)
    SetChrPos(0x102, 64700, 0, 520, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x102, 0x80)

    ChrTalk(    #139
        0x102,
        "#1P...Ah, here you are.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_375B():

        label("loc_375B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_375B")

    QueueWorkItem2(0x101, 1, lambda_375B)

    def lambda_376C():

        label("loc_376C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_376C")

    QueueWorkItem2(0x105, 1, lambda_376C)

    def lambda_377D():
        OP_6D(62650, 1000, 10120, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_377D)

    def lambda_3795():
        OP_67(0, 4550, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3795)

    def lambda_37AD():
        OP_8E(0xFE, 0x10036, 0x0, 0x1C98, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37AD)
    Sleep(500)

    def lambda_37CD():
        OP_8E(0xFE, 0xFCB2, 0x0, 0x191E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37CD)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 315, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 315, 400)
    OP_44(0x105, 0xFF)
    OP_44(0x101, 0xFF)

    ChrTalk(    #140
        0x101,
        "#344FJ-Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x105,
        "#354FHans...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x9,
        (
            "#730FRehearsal's over, and you're\x01",
            "still practicing.\x02\x03",

            "That's some dedication you\x01",
            "two have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        "#010FReady for the big duel scene?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#346FJ-Just leave it to us!\x01",
            "It'll be flawless!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#019FReally...? I look forward to\x01",
            "seeing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x105,
        (
            "#350FAnyway...what are you two\x01",
            "doing here?\x02\x03",

            "Were you looking for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x9,
        (
            "#730FYeah...today's the last day\x01",
            "that you two will be staying\x01",
            "with us in the dorms, right?\x02\x03",

            "I was thinking we could\x01",
            "have a big dinner to pump \x01",
            "ourselves up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#340FHmm... Maybe...\x02\x03",

            "#341FYeah, let's do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x105,
        (
            "#351FI think it sounds like\x01",
            "a great idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        "#010FBy the way...wasn't Jill with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x105,
        (
            "#350FShe was called away by the\x01",
            "dean some time ago...\x02\x03",

            "I'll go check on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#340FI'll come with you!\x02\x03",

            "You guys can go on ahead\x01",
            "to the cafeteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        "#019FOkay.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #154
        0x102,
        "#010F#5PLet's go to the cafeteria.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #155
        0x9,
        "#731F#2PAs you wish, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        "#018F#5PDon't call me that...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)

    def lambda_3BC3():
        OP_8E(0xFE, 0xFCBC, 0x0, 0x208, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BC3)
    Sleep(200)
    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0xFFFA, 0x0, 0x23A, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x102, 0x80)
    Fade(1000)
    OP_6D(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(    #157
        0x101,
        (
            "#346F#5PHa ha... Looks like they've\x01",
            "really hit it off.\x02\x03",

            "Sometimes it worries me that\x01",
            "he doesn't really let people\x01",
            "get close...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(    #158
        0x105,
        "#358F#1P*chuckle*\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(    #159
        0x101,
        "#344F#2PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x105,
        "#351F#1POh, it's nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#340F#2POkay, then.\x01",
            "Let's go get changed.\x02\x03",

            "It'd be kind of embarrassing\x01",
            "to walk around like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        "#358F#1PI have to agree.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-34830, 1000, 10350, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    RemoveParty(0x1, 0xFF)
    SetChrPos(0x105, -36520, 1000, 8430, 90)
    SetChrPos(0x101, -35180, 1000, 8580, 270)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x101, 65535)
    Sleep(300)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #163
        0x101,
        (
            "#006F#2PThat should do it...\x02\x03",

            "Want to go meet up with Jill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x105,
        (
            "#040F#1PAll right. Let's go to the\x01",
            "dean's office.\x02",
        )
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

    def lambda_3ED8():
        OP_69(0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3ED8)
    EventEnd(0x2)
    SetMapFlags(0x80)
    WaitChrThread(0x0, 0x1)
    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    Return()

    # Function_29_20B8 end

    SaveToFile()

Try(main)
