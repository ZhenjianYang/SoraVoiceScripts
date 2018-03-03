from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2500   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2500.x',
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
        'Lechter',                              # 9
        'Jill',                                 # 10
        'Hans',                                 # 11
        'Sieg',                                 # 12
        'Mr. Effort',                           # 13
        'Janitor Parkes',                       # 14
        'Ricky',                                # 15
        'Roy',                                  # 16
        'Logic',                                # 17
        'Felicity',                             # 18
        'Reina',                                # 19
        'Dennis',                               # 20
        'Freyja',                               # 21
        'Kaden',                                # 22
        'Alice',                                # 23
        'Rhody',                                # 24
        'Mickey',                               # 25
        'Target Camera',                        # 26
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
        'ED6_DT07/CH01590 ._CH',             # 00
        'ED6_DT07/CH01090 ._CH',             # 01
        'ED6_DT07/CH01370 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01080 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01580 ._CH',             # 06
        'ED6_DT07/CH01093 ._CH',             # 07
        'ED6_DT07/CH02670 ._CH',             # 08
        'ED6_DT07/CH02390 ._CH',             # 09
        'ED6_DT07/CH02550 ._CH',             # 0A
        'ED6_DT07/CH02320 ._CH',             # 0B
        'ED6_DT07/CH02323 ._CH',             # 0C
        'ED6_DT06/CH20051 ._CH',             # 0D
        'ED6_DT07/CH00043 ._CH',             # 0E
        'ED6_DT26/CH20254 ._CH',             # 0F
        'ED6_DT07/CH01460 ._CH',             # 10
        'ED6_DT26/CH20783 ._CH',             # 11
        'ED6_DT07/CH01583 ._CH',             # 12
        'ED6_DT26/CH20776 ._CH',             # 13
        'ED6_DT26/CH20777 ._CH',             # 14
        'ED6_DT26/CH20778 ._CH',             # 15
        'ED6_DT07/CH00044 ._CH',             # 16
        'ED6_DT26/CH20786 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01590P._CP',             # 00
        'ED6_DT07/CH01090P._CP',             # 01
        'ED6_DT07/CH01370P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01080P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01580P._CP',             # 06
        'ED6_DT07/CH01093P._CP',             # 07
        'ED6_DT07/CH02670P._CP',             # 08
        'ED6_DT07/CH02390P._CP',             # 09
        'ED6_DT07/CH02550P._CP',             # 0A
        'ED6_DT07/CH02320P._CP',             # 0B
        'ED6_DT07/CH02323P._CP',             # 0C
        'ED6_DT06/CH20051P._CP',             # 0D
        'ED6_DT07/CH00043P._CP',             # 0E
        'ED6_DT26/CH20254P._CP',             # 0F
        'ED6_DT07/CH01460P._CP',             # 10
        'ED6_DT26/CH20783P._CP',             # 11
        'ED6_DT07/CH01583P._CP',             # 12
        'ED6_DT26/CH20776P._CP',             # 13
        'ED6_DT26/CH20777P._CP',             # 14
        'ED6_DT26/CH20778P._CP',             # 15
        'ED6_DT07/CH00044P._CP',             # 16
        'ED6_DT26/CH20786P._CP',             # 17
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        X                   = 29230,
        Z                   = -2000,
        Y                   = 35060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 35340,
        Z                   = 0,
        Y                   = 75590,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 28510,
        Z                   = -1750,
        Y                   = 59190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 44890,
        Z                   = 0,
        Y                   = 53100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 37100,
        Z                   = 0,
        Y                   = 77390,
        Direction           = 180,
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
        X                   = 25960,
        Z                   = 0,
        Y                   = 65180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24550,
        Z                   = 0,
        Y                   = 65180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 41920,
        Z                   = 0,
        Y                   = 25060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 35560,
        Z                   = 0,
        Y                   = 77450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 30160,
        Z                   = -2000,
        Y                   = 45970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 45040,
        Z                   = 0,
        Y                   = 54220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 62660,
        Z                   = 0,
        Y                   = 75310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 41480,
        Z                   = 0,
        Y                   = 77530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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


    DeclActor(
        TriggerX            = 13590,
        TriggerZ            = 0,
        TriggerY            = 45970,
        TriggerRange        = 800,
        ActorX              = 13590,
        ActorZ              = 1100,
        ActorY              = 45970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59440,
        TriggerZ            = 9000,
        TriggerY            = 17860,
        TriggerRange        = 1000,
        ActorX              = 59440,
        ActorZ              = 9500,
        ActorY              = 17860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 50,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33510,
        TriggerZ            = 0,
        TriggerY            = 79330,
        TriggerRange        = 800,
        ActorX              = 33510,
        ActorZ              = 500,
        ActorY              = 79330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 51,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13590,
        TriggerZ            = 0,
        TriggerY            = 45970,
        TriggerRange        = 800,
        ActorX              = 13590,
        ActorZ              = 1100,
        ActorY              = 45970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43A",          # 00, 0
        "Function_1_73C",          # 01, 1
        "Function_2_928",          # 02, 2
        "Function_3_AA5",          # 03, 3
        "Function_4_B02",          # 04, 4
        "Function_5_B26",          # 05, 5
        "Function_6_B4A",          # 06, 6
        "Function_7_B6E",          # 07, 7
        "Function_8_BCB",          # 08, 8
        "Function_9_BF4",          # 09, 9
        "Function_10_C18",         # 0A, 10
        "Function_11_C3C",         # 0B, 11
        "Function_12_C60",         # 0C, 12
        "Function_13_F87",         # 0D, 13
        "Function_14_1482",        # 0E, 14
        "Function_15_16C7",        # 0F, 15
        "Function_16_1AD4",        # 10, 16
        "Function_17_1C38",        # 11, 17
        "Function_18_2043",        # 12, 18
        "Function_19_23EC",        # 13, 19
        "Function_20_2657",        # 14, 20
        "Function_21_2865",        # 15, 21
        "Function_22_2A78",        # 16, 22
        "Function_23_2C31",        # 17, 23
        "Function_24_2DAE",        # 18, 24
        "Function_25_3067",        # 19, 25
        "Function_26_329D",        # 1A, 26
        "Function_27_3387",        # 1B, 27
        "Function_28_3935",        # 1C, 28
        "Function_29_3A06",        # 1D, 29
        "Function_30_3CED",        # 1E, 30
        "Function_31_4E0D",        # 1F, 31
        "Function_32_5FE2",        # 20, 32
        "Function_33_66C7",        # 21, 33
        "Function_34_7783",        # 22, 34
        "Function_35_77A3",        # 23, 35
        "Function_36_77C8",        # 24, 36
        "Function_37_7809",        # 25, 37
        "Function_38_8949",        # 26, 38
        "Function_39_8B30",        # 27, 39
        "Function_40_9305",        # 28, 40
        "Function_41_93B7",        # 29, 41
        "Function_42_94B4",        # 2A, 42
        "Function_43_A782",        # 2B, 43
        "Function_44_A882",        # 2C, 44
        "Function_45_A97D",        # 2D, 45
        "Function_46_A9F5",        # 2E, 46
        "Function_47_AAE7",        # 2F, 47
        "Function_48_AB91",        # 30, 48
        "Function_49_ABDF",        # 31, 49
        "Function_50_B00E",        # 32, 50
        "Function_51_B026",        # 33, 51
    )


    def Function_0_43A(): pass

    label("Function_0_43A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (130, "loc_452"),
        (SWITCH_DEFAULT, "loc_459"),
    )


    label("loc_452")

    Event(0, 44)
    Jump("loc_459")

    label("loc_459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 23000, 0, 35340, 0)
    OP_43(0x15, 0x0, 0x0, 0x7)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0x18, 0x10)

    label("loc_49B")

    OP_43(0x18, 0x0, 0x0, 0x8)
    ClearChrFlags(0x1C, 0x80)
    OP_43(0x1C, 0x0, 0x0, 0x8)
    ClearChrFlags(0x1F, 0x80)
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_507")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, 49120, 9000, 20740, 0)
    OP_62(0x10, 0x0, 1800, 0x8, 0x9, 0xC8, 0x0)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 0)

    label("loc_507")

    Jump("loc_646")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_514")
    Jump("loc_646")

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 28130, -2000, 44180, 180)
    OP_43(0x15, 0x0, 0x0, 0x6)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 35370, 0, 17310, 90)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 60700, 0, 50820, 0)
    OP_43(0x1E, 0x0, 0x0, 0xA)
    Jump("loc_646")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5D5")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 20890, 0, 29430, 0)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x5)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 35370, 0, 17310, 90)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_646")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_646")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    ClearChrFlags(0x14, 0x80)
    OP_43(0x14, 0x0, 0x0, 0x3)

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 2)), scpexpr(EXPR_END)), "loc_646")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 61450, 0, 36510, 270)
    OP_43(0x12, 0x0, 0x0, 0x9)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39400, 0, 18670, 270)
    OP_43(0x11, 0x0, 0x0, 0xB)

    label("loc_646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_6A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_66F")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_6A1")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_685")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 42)
    Jump("loc_6A1")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6A1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 39)

    label("loc_6A1")

    Jump("loc_73B")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_6C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6BE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_6BE")

    Jump("loc_73B")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_6DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6DB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_6DB")

    Jump("loc_73B")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_707")
    OP_A3(0x2505)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 30)
    Jump("loc_726")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_726")
    OP_A3(0x2504)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 29)

    label("loc_726")

    Jump("loc_73B")

    label("loc_729")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_73B")

    Return()

    # Function_0_43A end

    def Function_1_73C(): pass

    label("Function_1_73C")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_76D")
    OP_B1("t2500_y")
    Jump("loc_776")

    label("loc_76D")

    OP_B1("t2500_n")

    label("loc_776")

    OP_A3(0x0)
    Jump("loc_785")

    label("loc_77C")

    OP_B1("t2500_n")

    label("loc_785")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_797")
    OP_72(0x1021, 0x0)
    ExitThread()

    label("loc_797")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x83), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3")
    OP_11(0xA4, 0xFF, 0xDC, 0x9470, 0x1ADB0, 0x0)

    label("loc_7B3")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83E")
    OP_72(0x1021, 0x0)
    ExitThread()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_813")
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_813")
    OP_62(0x10, 0x0, 1800, 0x8, 0x9, 0xC8, 0x0)

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_827")
    OP_64(0x0, 0x1)
    OP_65(0x3, 0x1)

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 3)), scpexpr(EXPR_END)), "loc_83E")
    OP_65(0x2, 0x1)

    label("loc_83E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")
    OP_1B(0x1E, 0x0, 0x2D)
    Jump("loc_85B")

    label("loc_852")

    OP_71(0x42E, 0x0)
    ExitThread()
    OP_10(0x1E, 0x0)

    label("loc_85B")

    OP_71(0x409, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    OP_71(0x40E, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_71(0x410, 0x0)
    ExitThread()
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_71(0x427, 0x0)
    ExitThread()
    OP_71(0x428, 0x0)
    ExitThread()
    OP_71(0x429, 0x0)
    ExitThread()
    OP_71(0x42A, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()
    OP_71(0x42C, 0x0)
    ExitThread()
    Return()

    # Function_1_73C end

    def Function_2_928(): pass

    label("Function_2_928")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A8F")

    label("loc_94D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_966")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A8F")

    label("loc_966")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A8F")

    label("loc_97F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_998")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A8F")

    label("loc_998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A8F")

    label("loc_9B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A8F")

    label("loc_9CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A8F")

    label("loc_9E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A8F")

    label("loc_9FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A8F")

    label("loc_A15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A8F")

    label("loc_A2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A47")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A8F")

    label("loc_A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A8F")

    label("loc_A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A79")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A8F")

    label("loc_A79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A8F")

    label("loc_AA4")

    Return()

    # Function_2_928 end

    def Function_3_AA5(): pass

    label("Function_3_AA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B01")
    OP_8E(0xFE, 0x7238, 0xFFFFF830, 0x88F4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7238, 0xFFFFF830, 0xDDB8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97F4, 0xFFFFF830, 0xDDB8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97F4, 0xFFFFF830, 0x88F4, 0x7D0, 0x0)
    Jump("Function_3_AA5")

    label("loc_B01")

    Return()

    # Function_3_AA5 end

    def Function_4_B02(): pass

    label("Function_4_B02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B25")
    OP_8D(0xFE, 23400, 28220, 20230, 31360, 2000)
    Jump("Function_4_B02")

    label("loc_B25")

    Return()

    # Function_4_B02 end

    def Function_5_B26(): pass

    label("Function_5_B26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B49")
    OP_8D(0xFE, 36420, 76870, 33680, 73630, 2000)
    Jump("Function_5_B26")

    label("loc_B49")

    Return()

    # Function_5_B26 end

    def Function_6_B4A(): pass

    label("Function_6_B4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6D")
    OP_8D(0xFE, 29400, 42790, 27350, 46370, 2000)
    Jump("Function_6_B4A")

    label("loc_B6D")

    Return()

    # Function_6_B4A end

    def Function_7_B6E(): pass

    label("Function_7_B6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BCA")
    OP_8E(0xFE, 0x59D8, 0x0, 0xF6AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB0CC, 0x0, 0xF6AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB0CC, 0x0, 0x709E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0x709E, 0x7D0, 0x0)
    Jump("Function_7_B6E")

    label("loc_BCA")

    Return()

    # Function_7_B6E end

    def Function_8_BCB(): pass

    label("Function_8_BCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF3")
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Jump("Function_8_BCB")

    label("loc_BF3")

    Return()

    # Function_8_BCB end

    def Function_9_BF4(): pass

    label("Function_9_BF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C17")
    OP_8D(0xFE, 59880, 38950, 64269, 33940, 2000)
    Jump("Function_9_BF4")

    label("loc_C17")

    Return()

    # Function_9_BF4 end

    def Function_10_C18(): pass

    label("Function_10_C18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3B")
    OP_8D(0xFE, 60140, 50160, 62310, 53370, 2000)
    Jump("Function_10_C18")

    label("loc_C3B")

    Return()

    # Function_10_C18 end

    def Function_11_C3C(): pass

    label("Function_11_C3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5F")
    OP_8D(0xFE, 40550, 17520, 37680, 20650, 2000)
    Jump("Function_11_C3C")

    label("loc_C5F")

    Return()

    # Function_11_C3C end

    def Function_12_C60(): pass

    label("Function_12_C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_C6D")
    Jump("loc_F83")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_C77")
    Jump("loc_F83")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_C81")
    Jump("loc_F83")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(    #0
        0xFE,
        (
            "I could've sworn I saw him not long ago,\x01",
            "but I can't find hide nor hair of him now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Ugh... Why does he have to be so good at\x01",
            "running away?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA1")

    label("loc_D28")


    ChrTalk(    #2
        0xFE,
        "Oh, are you guys searching for that devil, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Same here. He's in real trouble when I get my\x01",
            "hands on him!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_DA1")

    Jump("loc_F83")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E68")

    ChrTalk(    #4
        0xFE,
        (
            "Speaking of people slacking off, sounds like\x01",
            "my favorite dummy has been causing all sorts\x01",
            "of trouble again, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'm really gonna have to do something about\x01",
            "that guy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F83")

    label("loc_E68")


    ChrTalk(    #6
        0xFE,
        (
            "It's about this time of year that the new first-\x01",
            "year students start getting used to life at the\x01",
            "academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Which meeeans that a lot of them start\x01",
            "slacking off 'cause they think they've got\x01",
            "it all figured out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "And I'm not gonna let that happen this year!\x01",
            "No, sirree!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F83")

    TalkEnd(0xFE)
    Return()

    # Function_12_C60 end

    def Function_13_F87(): pass

    label("Function_13_F87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_F94")
    Jump("loc_147E")

    label("loc_F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_F9E")
    Jump("loc_147E")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1031")

    ChrTalk(    #9
        0xFE,
        "He's been coming over to me a lot lately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "*sigh* I wish he wouldn't. All he's doing is\x01",
            "getting in the way of my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1123")

    label("loc_1031")


    ChrTalk(    #11
        0xFE,
        (
            "The Student Council president came up\x01",
            "and talked to me again not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The exams are finally over, so I thought I could\x01",
            "take it easy for a while, but nooo! Now he wants\x01",
            "me to DRAW him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "He wants it colored, too! Uuugh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1123")

    Jump("loc_147E")

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_12C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_11A9")

    ChrTalk(    #14
        0xFE,
        (
            "Craaap... I can't get that weird song out\x01",
            "of my head now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Is brain bleach a thing? I need some, stat!\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C6")

    label("loc_11A9")


    ChrTalk(    #16
        0xFE,
        (
            "The Student Council president came over not\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "...He started singing some weird song into my\x01",
            "ear out of nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Something about lunar threads and a knight\x01",
            "with a mustache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I can't get the damn thing out of my head now,\x01",
            "so I can't concentrate on drawing!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_12C6")

    Jump("loc_147E")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_147E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_135C")

    ChrTalk(    #20
        0xFE,
        (
            "There used to be a fountain here, you know.\x01",
            "But they got rid of it last year for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I really liked it, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_147E")

    label("loc_135C")


    ChrTalk(    #22
        0xFE,
        (
            "There used to be a fountain here, you know.\x01",
            "But they got rid of it last year for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I mean, it was from the Middle Ages, so it was\x01",
            "pretty beat up. I can't blame them for getting\x01",
            "rid of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I just wish I'd drawn it before they did so.\x01",
            "That's my biggest regret.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_147E")

    TalkEnd(0xFE)
    Return()

    # Function_13_F87 end

    def Function_14_1482(): pass

    label("Function_14_1482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_148F")
    Jump("loc_16C3")

    label("loc_148F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1499")
    Jump("loc_16C3")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_14A3")
    Jump("loc_16C3")

    label("loc_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_14AD")
    Jump("loc_16C3")

    label("loc_14AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_16C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(    #25
        0x11,
        (
            "#643FCome to think of it...\x02\x03",

            "#640F...I think that one student who usually hangs\x01",
            "around near the old schoolhouse is on the social\x01",
            "studies course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C3")

    label("loc_1554")


    ChrTalk(    #26
        0x11,
        (
            "#643FOh! Hey, Kloe.\x02\x03",

            "#1890FYou're sure you don't need any help with\x01",
            "that? Really, really sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#543FI'm sure.\x02\x03",

            "#542FI promise all of these will be delivered no\x01",
            "problem, so don't you worry about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#645FWell, if you're sure...\x02\x03",

            "#648FIf you change your mind, though,\x01",
            "just come and let me know.\x02\x03",

            "It'd be no sweat on my end.\x02\x03",

            "So you just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_16C3")

    TalkEnd(0xFE)
    Return()

    # Function_14_1482 end

    def Function_15_16C7(): pass

    label("Function_15_16C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_178F")

    ChrTalk(    #29
        0xFE,
        (
            "You might think Lechter doesn't look like\x01",
            "the type to help out school staff like me,\x01",
            "but he helps me with menial tasks a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "...Almost always during class time, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1895")

    label("loc_178F")


    ChrTalk(    #31
        0xFE,
        (
            "You might think Lechter doesn't look like\x01",
            "the type to help out school staff like me,\x01",
            "but he helps me with menial tasks a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "He gets a lot of hate, but he's a good guy\x01",
            "in my book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "...He has been known to steal stuff from\x01",
            "time to time, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1895")

    Jump("loc_1AD0")

    label("loc_1898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_18A2")
    Jump("loc_1AD0")

    label("loc_18A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_19DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(    #34
        0xFE,
        (
            "You don't generally find any especially dangerous\x01",
            "monsters in this region, but any monster can be a\x01",
            "threat if you're not careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "So watch yourself while you're outside, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19DB")

    label("loc_196D")


    ChrTalk(    #36
        0xFE,
        (
            "Oh, are you planning on heading outside the\x01",
            "academy grounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Keep an eye out for monsters, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_19DB")

    Jump("loc_1AD0")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1A1E")

    ChrTalk(    #38
        0xFE,
        "I can't imagine Lechter's gone too far...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AC1")

    label("loc_1A1E")


    ChrTalk(    #39
        0xFE,
        "Hmm? You're looking for Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "He was on that bench reading a book till\x01",
            "not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Then he just up and disappeared. I wonder\x01",
            "where he went?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD0")
    OP_A2(0x2F83)
    OP_65(0x2, 0x1)

    label("loc_1AD0")

    TalkEnd(0xFE)
    Return()

    # Function_15_16C7 end

    def Function_16_1AD4(): pass

    label("Function_16_1AD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1B73")

    ChrTalk(    #42
        0xFE,
        (
            "I saw Ms. Millia running past here not long ago,\x01",
            "too, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "She looked like she was in a real hurry...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C34")

    label("loc_1B73")


    ChrTalk(    #44
        0xFE,
        (
            "After the exams, the cafeteria's always full\x01",
            "of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "So I'm just wasting time here until it empties\x01",
            "out some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Ahhh... It's so nice to be able to just sit and\x01",
            "take it easy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1C34")

    TalkEnd(0xFE)
    Return()

    # Function_16_1AD4 end

    def Function_17_1C38(): pass

    label("Function_17_1C38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_203F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 6)), scpexpr(EXPR_END)), "loc_1D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1CEA")

    ChrTalk(    #47
        0xFE,
        "We're on cleaning duty this week.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Thanks to how huge the campus is, it's a\x01",
            "ton of work, too... We won't have time for\x01",
            "clubs any time soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1CEA")


    ChrTalk(    #49
        0xFE,
        "Alice and I're on cleaning duty this week.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Which kind of makes it hard for us to join\x01",
            "any clubs right away... We'll get around to\x01",
            "it at some point.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1D8B")

    Jump("loc_203F")

    label("loc_1D8E")


    ChrTalk(    #51
        0xFE,
        (
            "Well, hey! Did you decide to join the\x01",
            "Student Council, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#044FOh, it's not that...\x02\x03",

            "#045FI'm just helping them with something\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "Aww. I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "You just seemed a little different from\x01",
            "how you usually are, so I thought joining\x01",
            "the council was the reason for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        "#044F...Different?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "It's nothing. Don't mind me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Anyway, can I help you out with anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#044FActually, you can.\x02\x03",

            "#040FYou haven't seen Lechter around anywhere,\x01",
            "have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Lechter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "No, I'm pretty sure he hasn't passed by here.\x01",
            "The only other person I can remember seeing\x01",
            "is the janitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#047FI see.\x02\x03",

            "#040FThanks for your help, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "No problemo.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F76)

    label("loc_203F")

    TalkEnd(0xFE)
    Return()

    # Function_17_1C38 end

    def Function_18_2043(): pass

    label("Function_18_2043")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_23E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 7)), scpexpr(EXPR_END)), "loc_21F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2126")

    ChrTalk(    #63
        0xFE,
        (
            "Now that I've decided to join this club,\x01",
            "I intend to devote myself fully to it and\x01",
            "all of its club activities!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "...I'm not sure what purpose this particular\x01",
            "practice activity serves, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F5")

    label("loc_2126")


    ChrTalk(    #65
        0xFE,
        (
            "Apparently, Freyja is an exchange student\x01",
            "from Leman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "They say she's crazy smart. Like, exceedingly\x01",
            "intelligent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Th-That's not why I decided to join the Music Club,\x01",
            "though! Absolutely not!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_21F5")

    Jump("loc_23E3")

    label("loc_21F8")

    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #68
        0xFE,
        "O-Oh... Hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#044FHello, Logic.\x02\x03",

            "Umm... Might I ask what you're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "O-Oh, not much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "It's just that I joined the academy's\x01",
            "Music Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Today's our first practice session.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        (
            "#040FDid you?\x02\x03",

            "#041FHave fun, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "I-I'll try...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Incidentally, Kloe...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0xFE,
        "Erm, I was just going to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "L-Let's give our best to our next set\x01",
            "of examinations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#040FHeehee. But of course.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F77)

    label("loc_23E3")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Return()

    # Function_18_2043 end

    def Function_19_23EC(): pass

    label("Function_19_23EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_248A")

    ChrTalk(    #79
        0xFE,
        (
            "I'm so pissed off, I think I'm just gonna take\x01",
            "the plunge and do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I'll show everyone I'll be a GREAT club head!\x01",
            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2653")

    label("loc_248A")


    ChrTalk(    #81
        0xFE,
        (
            "I kept saying I didn't want to be head of the\x01",
            "club, but no matter how many times I did it,\x01",
            "Reina just kept bringing it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "...And as if that wasn't annoying enough, some\x01",
            "boy walked past earlier yawning and telling me\x01",
            "I wasn't good enough to be head!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "What does he know?! I've never even TALKED\x01",
            "to him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I'm so pissed off, I think I'm just gonna take\x01",
            "the plunge and do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I'll show everyone I'll be a GREAT club head!\x01",
            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2653")

    TalkEnd(0xFE)
    Return()

    # Function_19_23EC end

    def Function_20_2657(): pass

    label("Function_20_2657")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_26E7")

    ChrTalk(    #86
        0xFE,
        (
            "Oh, well. All's well that ends well, I suppose.\x01",
            "I got what I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "I'll leave the word for next time I need it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2861")

    label("loc_26E7")


    ChrTalk(    #88
        0xFE,
        (
            "Felicity finally seems to have decided that she\x01",
            "wants to be the leader of our club!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I thought I might have to use a certain word\x01",
            "that is rather effective on her if she didn't\x01",
            "show any signs of relenting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "...but thanks to that boy who came past just\x01",
            "before, I didn't need it after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "...I rather wanted to be the one to deliver the\x01",
            "final push, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2861")

    TalkEnd(0xFE)
    Return()

    # Function_20_2657 end

    def Function_21_2865(): pass

    label("Function_21_2865")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_294F")

    ChrTalk(    #92
        0xFE,
        (
            "Around this time every year, Zeiss Central Factory\x01",
            "holds a series of lectures that are open to the\x01",
            "public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "You can hear all about their latest research and\x01",
            "stuff, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "Haha. I can hardly wait to go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_294F")


    ChrTalk(    #95
        0xFE,
        (
            "Starting next week, there's going to be a series\x01",
            "of lectures over at Zeiss Central Factory that\x01",
            "are open to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Fortunately the exams are over now, so I should\x01",
            "be able to go and take a look during a free day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It's going to be a real eye-opening experience,\x01",
            "I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_2A74")

    TalkEnd(0xFE)
    Return()

    # Function_21_2865 end

    def Function_22_2A78(): pass

    label("Function_22_2A78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2ADA")

    ChrTalk(    #98
        0x12,
        (
            "#735FHe's SUCH a nightmare...\x02\x03",

            "#734FThe guy just loooves toying with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2D")

    label("loc_2ADA")


    ChrTalk(    #99
        0x12,
        (
            "#733FO-Oh! It's you, Kloe.\x02\x03",

            "#732FYou haven't seen a really slovenly-looking guy\x01",
            "around here, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        "#044FA slovenly-looking guy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x12,
        (
            "#734FThat's a no, then. Trust me--if you'd seen the\x01",
            "guy I'm looking for, you wouldn't need to ask\x01",
            "for clarification.\x02\x03",

            "#736FWhere could he be? If he's not around here,\x01",
            "then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#042F???\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2C2D")

    TalkEnd(0xFE)
    Return()

    # Function_22_2A78 end

    def Function_23_2C31(): pass

    label("Function_23_2C31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2D75")

    ChrTalk(    #103
        0xFE,
        (
            "Radio calisthenics are a big thing over in\x01",
            "Remiferia, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "People always gather around a big orbal\x01",
            "radio and do them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Wait... Do you know what an orbal radio is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "It's a device that you can use to listen to music\x01",
            "and stuff that gets broadcast by something called\x01",
            "a radio station!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAA")

    label("loc_2D75")


    ChrTalk(    #107
        0xFE,
        "Radio calisthenics!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "One! Two! One! Two!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_2DAA")

    TalkEnd(0xFE)
    Return()

    # Function_23_2C31 end

    def Function_24_2DAE(): pass

    label("Function_24_2DAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2E3C")

    ChrTalk(    #109
        0xFE,
        (
            "I saw Lechter playing around with a white bird\x01",
            "a while ago. Can you believe that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "It was during an exam, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F33")

    label("loc_2E3C")


    ChrTalk(    #111
        0xFE,
        (
            "I saw Lechter playing around with a white bird\x01",
            "a while ago. Can you believe that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I saw him doing it from out the window, so as soon\x01",
            "as the exam was over, I came to look, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Looks like he's gone, and so has the bird. Bummer.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_2F33")

    Jump("loc_3063")

    label("loc_2F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2FD8")

    ChrTalk(    #114
        0xFE,
        (
            "*sigh* No matter what she does, Lucy is always\x01",
            "so beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I wonder how she does it. What kind of secrets\x01",
            "do you think she's hiding?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2FD8")


    ChrTalk(    #116
        0xFE,
        "I saw Lucy wander into the main building earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "She looked so exhausted...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "...but she was just as charming as ever. ㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_3063")

    TalkEnd(0xFE)
    Return()

    # Function_24_2DAE end

    def Function_25_3067(): pass

    label("Function_25_3067")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_319A")
    OP_63(0xFE)

    ChrTalk(    #119
        0xFE,
        (
            "I think Lucy has her heart set on someone\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "B-But WHO? I have to know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "...I probably shouldn't tell Hans that, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I wouldn't want to deny him the suffering\x01",
            "and misery of rejection when he takes a\x01",
            "shot at confessing to her like I did.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3299")

    label("loc_319A")

    OP_63(0xFE)

    ChrTalk(    #123
        0xFE,
        "I tried my luck confessing to Lucy a while back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "...All she said was, 'I'm sorry.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Her expression says she's got someone\x01",
            "else on her mind already to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I don't think she'd look at another guy\x01",
            "even if we tried.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A2(0x11)

    label("loc_3299")

    TalkEnd(0xFE)
    Return()

    # Function_25_3067 end

    def Function_26_329D(): pass

    label("Function_26_329D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3320")

    ChrTalk(    #127
        0xFE,
        "I'm bored, so I'm just taking it easy for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "What do you want? I'm not really in the mood\x01",
            "to talk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3383")

    label("loc_3320")


    ChrTalk(    #129
        0xFE,
        "You're that new student, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "What do you want? I'm not really in the mood\x01",
            "to talk.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_3383")

    TalkEnd(0xFE)
    Return()

    # Function_26_329D end

    def Function_27_3387(): pass

    label("Function_27_3387")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        "\x07\x00#40WSpring came.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #132
        (
            "\x07\x00#40WBut it took far more time doing so than the average\x01",
            "year.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_6D(58000, 0, 46000, 0)
    OP_67(0, 7820, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(540, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    SetChrPos(0x105, 11400, 0, 46000, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 49420, 8700, 20980, 90)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 4)
    OP_1D(0xE)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x7D0)

    def lambda_34DB():
        OP_6D(19660, 0, 44000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_34DB)

    def lambda_34F3():
        OP_67(0, 6260, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_34F3)

    def lambda_350B():
        OP_6C(125000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_350B)
    WaitChrThread(0x21, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #133
        (
            "\x07\x00#40WOne by one, the magnolia flowers began to show\x01",
            "their faces to the world as if reluctant to let their\x01",
            "long slumber end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #134
        (
            "\x07\x00#40WAnd with the changing of the seasons, a brand-new\x01",
            "student of the infamous Jenis Royal Academy set\x01",
            "foot into its grounds...slightly later than her peers.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    WaitChrThread(0x21, 0x0)
    OP_6D(18000, 0, 46000, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #135
        0x105,
        "Transfer Student",
        "#542FWell, here I am...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    NpcTalk(    #136
        0x105,
        "Transfer Student",
        "#047F*deep breath*\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #137
        0x105,
        "Transfer Student",
        "#042FOkay! I can do this!\x02",
    )

    CloseMessageWindow()

    def lambda_377E():
        OP_8E(0xFE, 0x319C, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_377E)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_70(0x21, 0x3C)
    OP_73(0x21)
    StopSound(0x9470, 0x2D2A8, 0x4650)
    OP_43(0x105, 0x3, 0x0, 0x1C)
    Sleep(2000)
    Fade(1500)
    OP_6D(21500, 0, 46720, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(305000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_3809():
        OP_6D(30960, -2000, 37400, 8000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3809)

    def lambda_3821():
        OP_6B(3860, 8000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3821)

    def lambda_3831():
        OP_6E(454, 8000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_3831)
    WaitChrThread(0x21, 0x0)
    Sleep(1000)

    NpcTalk(    #138
        0x10,
        "Mysterious Boy",
        (
            "#1770F#5POho...\x02\x03",

            "So that's our famous transfer student, huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    OP_22(0x196, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x8C, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x26, 0x27, 0xC8, 0x1)
    Sleep(1500)
    SetChrSubChip(0x10, 3)
    Sleep(150)
    SetChrSubChip(0x10, 2)
    Sleep(300)

    NpcTalk(    #139
        0x10,
        "Mysterious Boy",
        (
            "#1776FA hawk?\x02\x03",

            "#1775F...Nah. Seems more like a falcon.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_3387 end

    def Function_28_3935(): pass

    label("Function_28_3935")


    def lambda_393B():
        OP_8E(0xFE, 0x7030, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_393B)
    WaitChrThread(0x105, 0x1)

    def lambda_395B():
        OP_8E(0xFE, 0x7030, 0xFFFFF830, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_395B)
    WaitChrThread(0x105, 0x1)

    def lambda_397B():
        OP_8E(0xFE, 0x9740, 0xFFFFF830, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_397B)
    WaitChrThread(0x105, 0x1)

    def lambda_399B():
        OP_8E(0xFE, 0x9740, 0xFFFFF830, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_399B)
    WaitChrThread(0x105, 0x1)

    def lambda_39BB():
        OP_8E(0xFE, 0xBC5C, 0x190, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39BB)
    WaitChrThread(0x105, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_39EB():
        OP_8E(0xFE, 0xC544, 0x1F4, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39EB)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_28_3935 end

    def Function_29_3A06(): pass

    label("Function_29_3A06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(33900, 0, 44000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    SetChrPos(0x105, 49500, 500, 19240, 270)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x14, 0x80)

    def lambda_3A85():
        OP_6D(44500, 0, 20400, 8000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3A85)

    def lambda_3A9D():
        OP_67(0, 6600, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3A9D)

    def lambda_3AB5():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_3AB5)

    def lambda_3AC5():
        OP_6E(300, 8000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_3AC5)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_70(0x8, 0x3C)
    OP_73(0x8)

    def lambda_3AF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3AF4)

    def lambda_3B06():
        OP_8E(0xFE, 0xA2A8, 0x0, 0x4B28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B06)
    Sleep(1000)
    OP_72(0x8, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #140
        0x105,
        (
            "#044F#11PH-Hold on a minute...\x02\x03",

            "#043FI don't have a printout left for me...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 181, 500)
    Sleep(800)
    OP_8C(0x105, 0, 500)
    Sleep(800)

    ChrTalk(    #141
        0x105,
        (
            "#049F#11P(I wonder if I left mine in the classroom.)\x02\x03",

            "#042F(I must have... I'd better go back and get\x01",
            "it!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 500)

    def lambda_3C57():
        OP_8E(0xFE, 0x9A4C, 0x0, 0x5384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C57)
    WaitChrThread(0x105, 0x1)

    def lambda_3C77():
        OP_8E(0xFE, 0x9A4C, 0x0, 0x67E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C77)
    WaitChrThread(0x105, 0x1)

    def lambda_3C97():
        OP_8E(0xFE, 0xB5A4, 0x0, 0x7148, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C97)
    WaitChrThread(0x105, 0x1)

    def lambda_3CB7():
        OP_8E(0xFE, 0xB5A4, 0x0, 0xA7F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CB7)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x105, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3A06 end

    def Function_30_3CED(): pass

    label("Function_30_3CED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(53700, 170, 44000, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    SetChrPos(0x105, 50500, 500, 46000, 270)
    SetChrFlags(0x14, 0x80)

    def lambda_3D57():
        OP_6D(48700, 0, 45000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3D57)
    FadeToBright(2000, 0)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_3D8D():
        OP_8E(0xFE, 0xBA54, 0xFA, 0xB3B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3D8D)
    WaitChrThread(0x105, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #142
        0x105,
        (
            "#047F#5P*sigh*\x02\x03",

            "...\x02\x03",

            "#049FI'm feeling kind of tired.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E24():
        OP_6D(45720, 0, 44680, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3E24)

    def lambda_3E3C():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3E3C)

    def lambda_3E54():
        OP_6C(125000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_3E54)

    def lambda_3E64():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_3E64)

    def lambda_3E74():
        OP_8E(0xFE, 0xAB2C, 0xFFFFFF06, 0xAE24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E74)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 43820, -300, 44580, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 14)
    Sleep(500)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #143
        0x105,
        "#049F#5P*sigh*\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 45640, 0, 35640, 0)

    def lambda_3F1E():
        OP_8E(0xFE, 0xB248, 0x0, 0xA6B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F1E)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Sleep(300)

    NpcTalk(    #144
        0x10,
        "Mysterious Boy",
        "#1770F#11PHey there, pretty lady!\x02",
    )

    CloseMessageWindow()
    OP_63(0x105)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x105, 1)
    Sleep(300)

    ChrTalk(    #145
        0x105,
        (
            "#044F#6P...!\x02\x03",

            "#043FYou're the Student Council president,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146 op#A
        0x10,
        "#1775F#5P#10ABingo! Name's Lechter.\x02",
    )


    def lambda_4016():
        OP_8E(0xFE, 0xB248, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4016)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x105, 0)

    def lambda_403B():
        OP_8E(0xFE, 0xAC94, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_403B)
    WaitChrThread(0x10, 0x1)
    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        "#1773F#5PSure is a gorgeous sunset today, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x105,
        "#044F#5POh... Y-Yes, it is...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x10, 43820, -300, 46000, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #149
        0x10,
        "#1770F#6PSo, what're your impressions of the academy?\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    Fade(300)
    SetChrSubChip(0x105, 2)
    Sleep(500)

    ChrTalk(    #150
        0x105,
        (
            "#044F#11PWell...\x02\x03",

            "#543FUmm...\x02\x03",

            "I think it's a wonderful place. It's well equipped\x01",
            "in terms of facilities, for one thing.\x02\x03",

            "#542FIt has everything needed to really cultivate a \x01",
            "good environment for learning, and I'm happy\x01",
            "to have chosen it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #151
        0x10,
        (
            "#1777F#6PHaha...\x02\x03",

            "#1771F#3SHahaha!#2S\x01",
            "Ahh, my hunch was right on the money.\x01",
            "I knew you'd take it that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x105,
        (
            "#044F#11PAs opposed to...?\x02\x03",

            "#043FI-I'm sorry. Did I misunderstand you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        (
            "#1775F#6PWell, I was more asking about your life at\x01",
            "the academy outside of all the book junk.\x02\x03",

            "#1779FMaybe it's just me, but you don't really seem\x01",
            "to be letting loose or having fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #154
        0x105,
        (
            "#049F#5PU-Umm...\x02\x03",

            "#047FW-Well, I do still feel as though I'm still \x01",
            "adjusting to life here, s-so there's a lot\x01",
            "that I have yet to learn...\x02\x03",

            "#042F...but I'll keep working as hard as I can on\x01",
            "doing so. I promise!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0xAA, 1650, 0x18, 0x1B, 0x12C, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #155
        0x10,
        (
            "#1774F#6PHmm...\x02\x03",

            "#1773FWas that really what you came here to do, \x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_59()
    Fade(200)
    SetChrSubChip(0x105, 2)
    Sleep(400)

    ChrTalk(    #156
        0x105,
        "#044F#11PPardon me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        "#1775F#6PHeh.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #158
        0x10,
        (
            "#1778F#6PMan, you're too serious.\x02\x03",

            "#1771FHave you ever tried playing hooky,\x01",
            "like, ever? At least once?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #159
        0x105,
        "#043F#11PI... Umm... I... I...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 44120, -300, 46000, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #160
        0x10,
        (
            "#1770F#6PI might not look the part, but I AM the Student \x01",
            "Council president, y'know.\x02\x03",

            "#1775FOur work's pretty damn easy, too. What do you\x01",
            "think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        "#044F#11PAre you inviting me to join?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        (
            "#1772F#6POnly if you have a thing for long nights\x01",
            "filled with exciting paperwork and super-\x01",
            "duper enthralling schedules! (Monotone)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x105,
        "#042F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        "#1771F#6PAww. I was hoping for some kinda reaction.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #165
        0x105,
        (
            "#049F#5P(If he's the president, there must be something\x01",
            "respectable about him, but I'm not seeing it...)\x02\x03",

            "(How do I put this...?)\x02\x03",

            "#043F(I feel like I couldn't trust him with so much as\x01",
            "a ten mira coin...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #166
        0x10,
        (
            "#1776F#6POh, whoops. After Millia was bugging me about \x01",
            "showing up to lessons once in a while, I should\x01",
            "probably cough up some new excuse to ditch.\x02\x03",

            "#1775FI mean, I COULD go, but where's the fun in that?\x02\x03",

            "Pissing her off's like watching a pot boil over,\x01",
            "though, so whatever crap I make up better be\x01",
            "REALLY convincing.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #167
        0x105,
        (
            "#047F#5P(...Yep. I think my instincts were dead on.)\x02\x03",

            "#043FUmm... I... I should really be heading back to\x01",
            "the dormitory now.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 44180, 0, 44580, 270)
    ClearChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)
    Sleep(200)

    ChrTalk(    #168
        0x10,
        (
            "#1774F#6PYou might want to watch how you stand when\x01",
            "I'm kickin' it down here...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(200)
    SetChrSubChip(0x10, 3)
    Sleep(400)

    ChrTalk(    #169
        0x10,
        "#1772F#6P#3SMy view's awesome, if you catch my drift!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x105, 350, 600)
    SetChrFlags(0x105, 0x1000)

    def lambda_4BC7():
        OP_8F(0xFE, 0xAC94, 0x0, 0xA924, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4BC7)
    WaitChrThread(0x105, 0x1)
    ClearChrFlags(0x105, 0x1000)
    Sleep(500)

    ChrTalk(    #170
        0x105,
        "#046F#11P#3SExcuse me!#2S\x02",
    )

    OP_7C(0x0, 0x50, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_4C21():
        OP_6D(43820, -2000, 41200, 1000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4C21)

    def lambda_4C39():
        OP_6B(2940, 1000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4C39)

    def lambda_4C49():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0xA924, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C49)
    WaitChrThread(0x105, 0x1)
    SetChrSubChip(0x10, 2)

    def lambda_4C6E():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0x9984, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C6E)

    ChrTalk(    #171 op#A
        0x10,
        "#1775F#5P#15AThat way's the boys' dorm.\x02",
    )

    Sleep(1000)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #172
        0x105,
        "#047F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 340, 400)
    Sleep(300)

    def lambda_4CF8():
        OP_6D(43820, -2000, 48200, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4CF8)

    def lambda_4D10():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0xDF20, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D10)
    WaitChrThread(0x105, 0x1)

    def lambda_4D30():
        OP_8E(0xFE, 0x8430, 0xFFFFF830, 0xDF20, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D30)
    Sleep(1000)
    Fade(100)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #173
        0x10,
        (
            "#1775F#12POh, boy...\x02\x03",

            "#1770FThis one's gonna be like pulling teeth.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #174
        "\x07\x00Several days later, after classes...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    OP_A2(0x2F6B)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_3CED end

    def Function_31_4E0D(): pass

    label("Function_31_4E0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(40060, -2000, 32479, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    SetChrChipByIndex(0x105, 14)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 39560, -1750, 32980, 0)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, 34760, 0, 24860, 0)
    SetChrPos(0x12, 33640, 0, 24860, 0)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)

    def lambda_4EC7():
        OP_67(0, 5700, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4EC7)
    FadeToBright(2000, 0)

    def lambda_4EE8():
        OP_8E(0xFE, 0x87C8, 0xFFFFF830, 0x84D0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4EE8)
    Sleep(150)

    def lambda_4F08():
        OP_8E(0xFE, 0x8368, 0xFFFFF830, 0x823C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F08)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_4F2D():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4F2D)
    Sleep(100)
    TurnDirection(0x12, 0x105, 400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4F75():
        OP_8E(0xFE, 0x9240, 0xFFFFF830, 0x84D0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F75)
    Sleep(100)

    def lambda_4F95():
        OP_8E(0xFE, 0x8F20, 0xFFFFF830, 0x823C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F95)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #175
        0x11,
        (
            "#643F#6PHuh? Kloe?\x02\x03",

            "What are you doing sitting here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105)
    Sleep(500)
    SetChrSubChip(0x105, 1)
    Sleep(300)

    ChrTalk(    #176
        0x105,
        (
            "#044F#5POh... Hello.\x02\x03",

            "#542FI just had a little free time, so I thought\x01",
            "I would try and use it productively.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0x12,
        "#733F#12PIs that lesson prep work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x11,
        (
            "#643F#6PMan... You're so dedicated.\x02\x03",

            "#648FI think I can see how you were able to pass the\x01",
            "legendary transfer student entrance exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        (
            "#043F#5PE-Erm...\x02\x03",

            "It's really just something to pass the time.\x01",
            "It's not like I'm working every waking hour\x01",
            "of the day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        (
            "#644F#6POh, yeah. Guess it wouldn't hurt to ask...\x02\x03",

            "You haven't seen Lechter around, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#044F#5PLechter?\x02\x03",

            "#042F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #182
        0x11,
        (
            "#647F#6PI-I'm almost scared to ask, but...\x02\x03",

            "#1892F...he didn't try anything funny on you,\x01",
            "did he?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #183
        0x105,
        (
            "#047F...No.\x02\x03",

            "#047FSort of.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5310():
        OP_6D(40830, -2000, 32580, 600)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5310)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_534C():

        label("loc_534C")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_534C")

    QueueWorkItem2(0x11, 2, lambda_534C)

    def lambda_535D():

        label("loc_535D")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_535D")

    QueueWorkItem2(0x12, 2, lambda_535D)

    def lambda_536E():
        OP_8F(0xFE, 0x9BB4, 0xFFFFF830, 0x8A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_536E)

    def lambda_5389():
        OP_8F(0xFE, 0x97CC, 0xFFFFF830, 0x8A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5389)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #184
        0x11,
        (
            "#1893F#6PI-I'm so, so sorry!\x02\x03",

            "This is all our fault for not keeping that nutjob on\x01",
            "a leash!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x12,
        (
            "#734F#6PI don't know how we can begin to apologize to you.\x02\x03",

            "Whatever he did, we'll be absolutely sure it never\x01",
            "happens again--or anything else for that matter--\x01",
            "so please, forgive us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x11,
        "#645F#6PWe're begging you!\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    OP_96(0x105, 0x9A88, 0xFFFFF830, 0x83A4, 0x64, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #187
        0x105,
        (
            "#043F#11PU-Umm... It's okay, honestly.\x02\x03",

            "#045FHe really didn't do anything major to me.\x01",
            "Honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x11,
        "#643F#6PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x105,
        (
            "#542F#11PY-Yes.\x02\x03",

            "He just tried to tease me a little.\x01",
            "It was harmless fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x11,
        (
            "#645F#6PWhew... You nearly gave me a heart attack,\x01",
            "Kloe...\x02\x03",

            "I thought I was gonna faint or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x12,
        (
            "#734F#6PSeriously... It's getting to the point where\x01",
            "I feel like I need to apologize every time \x01",
            "I hear his name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x11,
        "#645F#1PThanks Aidios...\x02",
    )


    ChrTalk(    #193
        0x12,
        "#734FThanks Aidios...\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #194
        0x105,
        "#045F#11PH-Haha...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #195
        0x105,
        (
            "#049F#11PUmm...\x02\x03",

            "#043FIs he really that much of a troublemaker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x11,
        (
            "#640F#6POh, 'troublemaker'? That's cute.\x02\x03",

            "#645FHonestly, with a personality like that, he's a\x01",
            "walking nightmare straight from Gehenna.\x02\x03",

            "We've lost count of how many times he's ran\x01",
            "away from doing his council work in the past\x01",
            "couple weeks alone.\x02\x03",

            "#646FWhich would be bad enough if it weren't for\x01",
            "the fact that he's usually out raising hell for\x01",
            "people instead.\x02\x03",

            "So instead of doing our own work, we're either\x01",
            "out searching for him or apologizing for things\x01",
            "he's done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x12,
        (
            "#734F#6PThat's why the council's most important policy \x01",
            "is: 'If he's not in our sights, the sooner we find\x01",
            "him, the better.'\x02\x03",

            "If you're thinking we can't be a very effective\x01",
            "Student Council like that...well, you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x105,
        "#049F#11PI-I see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x11,
        "#643F#6PSomething wrong, Kloe?\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #200
        0x105,
        (
            "#045F#11PO-Oh, no. Nothing, really.\x02\x03",

            "#044FBut speaking of Lechter...\x02\x03",

            "He was sleeping on top of the clubhouse\x01",
            "roof not long ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #201
        0x11,
        "#642F#6PHe was?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x12,
        (
            "#733F#6PWell, that explains why we couldn't find him...\x01",
            "We didn't checked there.\x02\x03",

            "#731FYou're the best, Kloe! Thanks a ton!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x105,
        (
            "#045F#11PN-Not at all...\x02\x03",

            "#540F(It was actually Sieg who noticed him there,\x01",
            "but I suppose I shouldn't tell them that...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CBD():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5CBD)
    Sleep(200)
    TurnDirection(0x12, 0x11, 500)
    Sleep(300)

    ChrTalk(    #204
        0x11,
        "#1891F#5PC'mon, Hans! We've got some trash to bring in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x12,
        "#732F#12PDamn straight!\x02",
    )

    CloseMessageWindow()

    def lambda_5D36():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5D36)
    Sleep(200)
    OP_8C(0x12, 180, 500)
    Sleep(300)

    ChrTalk(    #206
        0x11,
        "#641F#6PSeriously! Thanks, Kloe. We owe you big time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x12,
        "#730F#6PSee ya later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x105,
        "#542F#11POh, s-sure.\x02",
    )

    CloseMessageWindow()

    def lambda_5DC5():

        label("loc_5DC5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_5DC5")

    QueueWorkItem2(0x105, 2, lambda_5DC5)

    def lambda_5DD6():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x8A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5DD6)
    Sleep(100)

    def lambda_5DF6():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x8A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5DF6)
    WaitChrThread(0x12, 0x1)

    def lambda_5E16():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x5F50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E16)
    WaitChrThread(0x11, 0x1)

    def lambda_5E36():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x5F50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5E36)
    Sleep(2000)
    OP_44(0x105, 0x2)
    OP_8C(0x105, 180, 400)
    Sleep(1500)

    def lambda_5E66():
        OP_6D(40800, -2000, 32500, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5E66)
    WaitChrThread(0x21, 0x0)
    Sleep(500)

    ChrTalk(    #209
        0x105,
        (
            "#047F#6PSo that's what he's usually like...\x02\x03",

            "#049FMy instincts about him being irresponsible\x01",
            "were right, I see...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #210
        0x105,
        (
            "#047F#6P(Still...)\x02\x03",

            "(...that question he asked me...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F5E():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5F5E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x21, 0xFF)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #211
        (
            "\x07\x0C\x18Was that really what you came here to do, \x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    Call(0, 32)
    Return()

    # Function_31_4E0D end

    def Function_32_5FE2(): pass

    label("Function_32_5FE2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(164)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, 31900, 0, 19000, 90)
    SetChrPos(0x12, 31900, 0, 19000, 90)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 48740, 8700, 20900, 270)
    OP_62(0x10, 0xFFFFFEA2, 1800, 0x8, 0x9, 0xC8, 0x0)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 0)
    OP_6D(49100, 500, 19000, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(350, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_60C8():
        OP_6D(47600, 9000, 22000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_60C8)

    def lambda_60E0():
        OP_67(0, 8840, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_60E0)

    def lambda_60F8():
        OP_6C(135000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_60F8)

    def lambda_6108():
        OP_6E(250, 4000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_6108)
    WaitChrThread(0x21, 0x0)
    Sleep(1000)

    def lambda_6122():
        OP_6D(56500, 9000, 18360, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_6122)

    def lambda_613A():
        OP_67(0, 7220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_613A)

    def lambda_6152():
        OP_6C(110000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_6152)

    def lambda_6162():
        OP_6E(264, 3000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_6162)
    WaitChrThread(0x21, 0x0)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x11, 60500, 6800, 16860, 290)
    SetChrPos(0x12, 60500, 6800, 16860, 290)
    OP_63(0x10)
    SetChrFlags(0x10, 0x8)
    OP_96(0x11, 0xEC54, 0x1E78, 0x41DC, 0x3E8, 0xFA0)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x11,
        "#1891F(There he is!)\x02",
    )

    CloseMessageWindow()
    OP_96(0x11, 0xEC54, 0x1A90, 0x41DC, 0xA, 0xFA0)
    Sleep(500)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0xE6DC, 0x2328, 0x4498, 0xBB8, 0x1194)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_6255():
        OP_6D(51700, 9000, 20600, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_6255)

    def lambda_626D():
        OP_6C(65000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_626D)

    def lambda_627D():
        OP_8E(0xFE, 0xC92C, 0x2328, 0x5078, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_627D)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x12, 0xE6DC, 0x2328, 0x4498, 0xBB8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_62B9():
        OP_8E(0xFE, 0xC8F0, 0x2328, 0x4BDC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_62B9)
    WaitChrThread(0x11, 0x1)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #213
        0x11,
        "#643FWhat?!\x02",
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x22)
    OP_43(0x12, 0x3, 0x0, 0x23)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #214
        0x12,
        "#733FWh-Where is he...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        "#642FHe was there a second ago! I saw him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        "#732FThen why isn't he there now?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x11,
        "#1891FCRAP! Where'd he go?!\x02",
    )

    CloseMessageWindow()

    def lambda_63E8():
        OP_8E(0xFE, 0xC350, 0x2328, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63E8)
    Sleep(100)
    OP_43(0x12, 0x3, 0x0, 0x23)
    WaitChrThread(0x11, 0x1)
    OP_43(0x11, 0x3, 0x0, 0x22)
    WaitChrThread(0x11, 0x3)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x11,
        "#643F#5POh...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x105, 33380, -2000, 35840, 180)
    OP_43(0x105, 0x3, 0x0, 0x24)

    def lambda_6467():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6467)

    def lambda_6475():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6475)

    def lambda_6483():
        OP_6D(46060, 9000, 21580, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_6483)

    def lambda_649B():
        OP_6C(324000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_649B)
    Sleep(3000)

    def lambda_64B0():
        OP_8F(0xFE, 0xC350, 0x2328, 0x4DE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_64B0)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #219
        0x11,
        "#640FLooks like Kloe's heading off somewhere else.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #220
        0x11,
        (
            "#641FMaybe we should ask her again if she saw\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x12,
        (
            "#733F#6PHuh? Oh, sure. I guess.\x02\x03",

            "#730FCan't hurt.\x02\x03",

            "I mean, she was the one who led us up here in\x01",
            "the first place.\x02\x03",

            "She'd probably be a useful asset in our search\x01",
            "in general if we could convince her to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x11,
        "#644FYeah! Let's go down and talk to her!\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)

    def lambda_6671():
        OP_8E(0xFE, 0xE038, 0x2328, 0x526C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6671)
    Sleep(400)

    def lambda_6691():
        OP_8E(0xFE, 0xE038, 0x2328, 0x4DE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6691)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Call(0, 33)
    Return()

    # Function_32_5FE2 end

    def Function_33_66C7(): pass

    label("Function_33_66C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_6D(53100, 0, 27240, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(306, 0)
    SetChrPos(0x105, 43360, 0, 28060, 90)
    SetChrPos(0x12, 52820, 500, 22500, 350)
    SetChrPos(0x11, 53020, 500, 22500, 350)

    def lambda_6775():
        OP_8E(0xFE, 0xC4B8, 0x0, 0x6D9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6775)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)

    def lambda_67AF():
        OP_8E(0xFE, 0xCE54, 0x0, 0x6EB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_67AF)
    Sleep(400)

    def lambda_67CF():
        OP_8E(0xFE, 0xCF1C, 0x0, 0x6A40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_67CF)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_23(0x6)
    WaitChrThread(0x12, 0x1)

    def lambda_680A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_680A)
    WaitChrThread(0x11, 0x1)

    def lambda_681D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_681D)

    ChrTalk(    #223
        0x12,
        "#731F#5P...Kloe! Our favorite person!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #224
        0x105,
        (
            "#044F#12POh... Hello again.\x02\x03",

            "Was he not on the roof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x11,
        (
            "#647F#5PN-No, he was... He just managed to disappear\x01",
            "before we could wring our hands around his\x01",
            "stupid neck.\x02\x03",

            "#646FCan't believe he managed to escape again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x12,
        (
            "#734F#5PThat doesn't make any sense to us, though.\x02\x03",

            "It's not like there was anywhere to hide up there,\x01",
            "and he was way too far up to be able to just jump\x01",
            "down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x105,
        "#043F#12PThat does seem strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x11,
        (
            "#640F#5PSooo...you knooow...\x02\x03",

            "We were wondering if you might have some\x01",
            "idea where he might've gone next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12,
        (
            "#732F#5PIt doesn't even need to be a specific location\x01",
            "like last time. Anything useful you might have\x01",
            "on him to share, share away!\x02\x03",

            "Please! Anything will do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x105,
        (
            "#044F#12PW-Well...\x02\x03",

            "#047F(They really do seem to need some help...)\x02\x03",

            "#542FI might have some kind of idea...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #231
        0x11,
        "#643F#5PWait. You DO know something?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x105,
        (
            "#045F#12PI don't...but I know someone who might.\x02\x03",

            "Let me ask him for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 345, 400)
    Sleep(500)

    ChrTalk(    #233
        0x105,
        "#042F#11PSieg!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 40440, 6000, 40960, 180)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_8E(0x13, 0xC030, 0x514, 0x6A7C, 0x2328, 0x0)
    OP_97(0x13, 0xC4B8, 0x6D9C, 0xFFFD8F00, 0x157C, 0x1)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 225, 400)
    OP_8F(0x13, 0xC56C, 0xC8, 0x6EC8, 0x3E8, 0x0)
    Fade(500)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 13)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x11,
        "#643FWh-Whoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x12,
        (
            "#733F#5PYou have a falcon?!\x02\x03",

            "Is he your pet or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x105,
        (
            "#045F#12POh, no...\x02\x03",

            "#542FHe's more like a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x13,
        "#311F#5PScree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x11,
        "#641F#5PHa...haha... Got'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x105,
        (
            "#042F#12PSieg, you haven't seen Lechter, have you?\x02\x03",

            "He was that slovenly boy who was sleeping\x01",
            "on the clubhouse roof not long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x13,
        (
            "#310F#5PScree?\x02\x03",

            "Screescree... Scree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#044F#12PSo you lost sight of him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x13,
        "#310F#5PScree... Screeeee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x105,
        (
            "#045F#12PNo, it's all right. Don't worry about it.\x02\x03",

            "#542FSorry for calling you, then. Thanks for\x01",
            "trying to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x13,
        "#311F#5PScree...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()

    def lambda_6FCD():

        label("loc_6FCD")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_6FCD")

    QueueWorkItem2(0x11, 2, lambda_6FCD)

    def lambda_6FDE():

        label("loc_6FDE")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_6FDE")

    QueueWorkItem2(0x12, 2, lambda_6FDE)
    OP_22(0x8C, 0x0, 0x64)
    OP_8F(0x13, 0xC65C, 0x514, 0x7058, 0x3E8, 0x0)
    SetChrChipByIndex(0x13, 11)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 300, 400)
    OP_8E(0x13, 0x9F4C, 0x1770, 0xAA64, 0x2328, 0x0)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    SetChrFlags(0x13, 0x80)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #245
        0x105,
        (
            "#047F#12PWow...\x02\x03",

            "#042FHe really must be fast if Sieg can't keep up\x01",
            "with him!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70AB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_70AB)
    Sleep(200)
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #246
        0x12,
        (
            "#735F#5PUhhh... I think we're a bit too busy having our\x01",
            "minds blown by you talking to a falcon to feel\x01",
            "impressed by Lechter right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x11,
        (
            "#645F#5PY-You're telling me...\x02\x03",

            "#649FYou're a true enigma...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 75, 400)
    Sleep(300)

    ChrTalk(    #248
        0x105,
        "#043F#12PD-Did I do something strange...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x11,
        (
            "#643F#5POh, don't get me wrong. I don't mean that\x01",
            "in a bad way.\x02\x03",

            "#648FI'm just genuinely amazed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x12,
        (
            "#730F#5PThat makes two of us.\x02\x03",

            "#734FShame that superpower of yours didn't get\x01",
            "us any closer to finding Lechter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x105,
        (
            "#049F#12PIndeed...\x02\x03",

            "#047FStill, if Sieg couldn't find him, it could mean\x01",
            "he's inside one of the buildings.\x02\x03",

            "#040FProbably in one that's relatively quiet at this\x01",
            "time of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x11,
        (
            "#642F#5PActually, that helps narrow things down a lot.\x02\x03",

            "#647FIt just leaves empty classrooms, the dorms,\x01",
            "the auditorium, the old schoolhouse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x12,
        "#734F#5PThat still leaves plenty of places if you ask me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x105,
        (
            "#045F#12PU-Umm...\x02\x03",

            "#542FWould... Would you like me to help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x11,
        (
            "#643F#5PReally? You're sure you wouldn't mind?\x02\x03",

            "I thought you had something else you\x01",
            "needed to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x105,
        (
            "#543F#12PI was just going to go and have a look around\x01",
            "some of the clubs, but I can do that any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x12,
        (
            "#735F#5PWell, I do feel kinda bad about asking you\x01",
            "to put yourself out for us...\x02\x03",

            "#730F...but you really would be a serious help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x11,
        (
            "#644F#5PI don't think we could wish for better, even.\x02\x03",

            "You're totally sure, though? We wouldn't want\x01",
            "to force you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x105,
        "#041F#12POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        (
            "#641FGreat! Let's get to work, then!\x02\x03",

            "#1891FHe's not gonna know what hit him!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    AddParty(0x3A, 0xFF, 0xFF)
    SetChrFlags(0x12, 0x80)
    AddParty(0x51, 0xFF, 0xFF)
    OP_6D(50660, 0, 28060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 50660, 0, 28060, 270)
    SetChrPos(0x13B, 50360, 0, 28060, 90)
    SetChrPos(0x152, 50360, 0, 28060, 90)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x13B, 65535)
    SetChrChipByIndex(0x152, 65535)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x13B, 0)
    SetChrSubChip(0x152, 0)
    OP_69(0x0, 0x0)
    OP_71(0x1007, 0x0)
    ExitThread()
    OP_71(0x1008, 0x0)
    ExitThread()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_33_66C7 end

    def Function_34_7783(): pass

    label("Function_34_7783")

    OP_8C(0x11, 335, 500)
    Sleep(600)
    OP_8C(0x11, 245, 500)
    Sleep(600)
    OP_8C(0x11, 290, 500)
    Return()

    # Function_34_7783 end

    def Function_35_77A3(): pass

    label("Function_35_77A3")

    Sleep(300)
    OP_8C(0x12, 245, 500)
    Sleep(600)
    OP_8C(0x12, 335, 500)
    Sleep(600)
    OP_8C(0x12, 290, 500)
    Return()

    # Function_35_77A3 end

    def Function_36_77C8(): pass

    label("Function_36_77C8")


    def lambda_77CE():
        OP_8E(0xFE, 0x8264, 0x0, 0x7120, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_77CE)
    WaitChrThread(0x105, 0x1)

    def lambda_77EE():
        OP_8E(0xFE, 0xCEE0, 0x0, 0x7120, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_77EE)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_36_77C8 end

    def Function_37_7809(): pass

    label("Function_37_7809")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 52640, 500, 22500, 350)
    SetChrPos(0x11, 52840, 500, 22500, 350)
    SetChrPos(0x105, 53320, 500, 22500, 350)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_6D(54100, 0, 27240, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(306, 0)
    OP_6F(0x1, 60)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)

    def lambda_78CD():
        OP_8E(0xFE, 0xCE68, 0x0, 0x724C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_78CD)
    Sleep(500)

    def lambda_78ED():
        OP_8E(0xFE, 0xCDA0, 0x0, 0x6810, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_78ED)
    Sleep(1000)

    def lambda_790D():
        OP_8E(0xFE, 0xD048, 0x0, 0x69C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_790D)
    WaitChrThread(0x12, 0x1)
    OP_72(0x7, 0x8)
    ExitThread()
    OP_6F(0x7, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)

    def lambda_7946():
        OP_8E(0xFE, 0xCB34, 0x0, 0x6FE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7946)
    WaitChrThread(0x11, 0x1)

    def lambda_7966():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7966)
    WaitChrThread(0x12, 0x1)

    def lambda_7979():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7979)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #261
        0x11,
        "#645F#6PUrgh... I'm exhausted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x12,
        (
            "#735F#6PTrying to find Lechter is exhausting but somehow\x01",
            "not having to do it ends up being just as tiring.\x02\x03",

            "#738FBut at least I was finally reunited with my beloved\x01",
            "Lucy!\x02\x03",

            "I was dying of loneliness from not getting to see\x01",
            "her during the exam period. ㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #263
        0x11,
        (
            "#649F#5P...You liar. You went and met her this morning,\x01",
            "didn't you? Something about seeing her before \x01",
            "your exams making you do better in them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x12, 400)
    Sleep(300)

    ChrTalk(    #264
        0x105,
        "#041F#11PHeehee. You're right. I saw you, too.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_71(0x7, 0x8)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 53060, 500, 22500, 350)
    OP_4A(0x10, 255)

    def lambda_7BC3():
        OP_8E(0xFE, 0xCF44, 0x1F4, 0x5E74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7BC3)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #265
        0x10,
        (
            "#1773F#11POh, hey. \x02\x03",

            "#1771FJust what I needed. A few people who look like\x01",
            "they've got nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C52():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7C52)
    Sleep(100)

    def lambda_7C65():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C65)
    Sleep(100)
    TurnDirection(0x12, 0x10, 400)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #266
        0x11,
        (
            "#646F#6PWe're a hell of lot busier than YOU are!\x02\x03",

            "WE need to go around and meet with the heads\x01",
            "of all the academy's clubs and start drafting up\x01",
            "a budget!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x10,
        "#1775F#11POh. 'Kay. I guess it's up to you, Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x105,
        "#044F#6P...Me?\x02",
    )

    CloseMessageWindow()

    def lambda_7D8A():
        OP_8E(0xFE, 0xD00C, 0x0, 0x6554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7D8A)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #269
        "\x07\x05Lechter handed an envelope to Kloe.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #270
        0x105,
        "#045F#6PUmm... What is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x10,
        (
            "#1774F#11PIt's something that needs to be delivered to\x01",
            "the mayor of Ruan.\x02\x03",

            "#1779FLeo's not gonna take no for an answer, either. \x01",
            "So there you go. Enjoy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x11,
        "#647F#6PThat sounds very much like it's YOUR job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x10,
        (
            "#1771F#11PMine? You sure you're not mistaking me for\x01",
            "someone else?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #274
        0x10,
        (
            "#1773F#11POh, and Kloe?\x02\x03",

            "You've got a feather on your head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x105,
        "#044F#6PI do?!\x02",
    )

    CloseMessageWindow()

    def lambda_7FAE():
        OP_8E(0xFE, 0xD00C, 0x0, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7FAE)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #276
        "\x07\x05Lechter brushed his hand across Kloe's head.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_8026():
        OP_8F(0xFE, 0xD00C, 0x0, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8026)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #277
        0x10,
        (
            "#1775F#11PI guess that must've been Sieg's.\x02\x03",

            "#1776FHe did say it was almost time for him\x01",
            "to start molting, come to think of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x105,
        (
            "#540F#6P(H-How long has that been there...?)\x02\x03",

            "(I hope it wasn't there during the exams...\x01",
            "That would be so embarrassing!)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #279
        0x105,
        (
            "#044F#6PYou know about Sieg?\x02\x03",

            "A-And did you actually TALK to him?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    Sleep(300)

    ChrTalk(    #280
        0x10,
        "#1775F#5POkay! Good luck delivering that envelope!\x02",
    )

    CloseMessageWindow()

    def lambda_81FC():
        OP_8E(0xFE, 0xCF44, 0x1F4, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_81FC)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    OP_72(0x7, 0x8)
    ExitThread()
    OP_6F(0x7, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)
    Sleep(1300)

    ChrTalk(    #281
        0x105,
        "#042F#5P(Talk about an enigma...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #282
        0x11,
        (
            "#645F#6PUmm... Kloe?\x02\x03",

            "You are aware you've just had Lechter's work\x01",
            "unceremoniously dumped on you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x12,
        (
            "#734F#6PAlso, while I hate to be the one to break\x01",
            "it to you...\x02\x03",

            "...there wasn't a feather on your head.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 350, 600)
    Sleep(300)

    ChrTalk(    #284
        0x105,
        (
            "#044F#11P#3S...!!#2S\x02\x03",

            "#540FHe did it again...\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #285
        0x11,
        (
            "#646F#6PCome on! You can't let him get away with this!\x01",
            "You've got to go after him and force him to take\x01",
            "it back!\x02\x03",

            "You shouldn't have to do his work for him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x12,
        (
            "#735F#6PI don't disagree, but I'm not sure she's gonna\x01",
            "find him if she goes after him now.\x02\x03",

            "#736FHe's got enough of a head start that we're\x01",
            "probably talking, like--what?--five hours to\x01",
            "find him? Six?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x105,
        (
            "#045F#11PI...\x02\x03",

            "I think it would be faster for me to just go and\x01",
            "do the job myself, wouldn't it?\x02\x03",

            "#542FAll I have to do is deliver it to the mayor of\x01",
            "Ruan, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x11,
        (
            "#645F#6PAww... We were kinda hoping you could help\x01",
            "us with our work, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x105,
        "#045F#11PI'm sorry, Jill.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x11,
        (
            "#648F#6PAww, don't worry about it. No big deal.\x02\x03",

            "#640FDo you know the way to the mayor's place?\x01",
            "If you don't, I can help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x105,
        (
            "#542F#11PThanks, but I know the way. I've been to visit\x01",
            "him once before, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x11,
        "#643F#6PHuh? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x12,
        (
            "#731F#6PSounds like you should be fine, then.\x02\x03",

            "#730FWell, take care of monsters on the way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x105,
        "#040F#11PThank you. I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x11,
        (
            "#644F#6PWell, this is goodbye for now, I guess.\x02\x03",

            "#648FLater!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x12,
        "#730F#6PDon't be out too late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x105,
        "#041F#11PI won't.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 345, 400)

    def lambda_8850():
        OP_8E(0xFE, 0xCE68, 0x1F4, 0x86C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8850)
    Sleep(400)
    OP_8C(0x12, 345, 500)

    def lambda_8877():
        OP_8E(0xFE, 0xCEE0, 0x0, 0x75BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8877)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)

    def lambda_889C():
        OP_8E(0xFE, 0xCEE0, 0x1F4, 0x86C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_889C)
    WaitChrThread(0x12, 0x1)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1007, 0x0)
    ExitThread()
    OP_71(0x7, 0x8)
    ExitThread()
    OP_6F(0x1, 0)
    OP_6D(52800, 0, 27220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 52800, 0, 27220, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_37_7809 end

    def Function_38_8949(): pass

    label("Function_38_8949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_89FA")
    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(12760, 0, 44640, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 15300, 0, 46000, 270)
    OP_0D()
    OP_72(0x1021, 0x0)
    ExitThread()
    OP_70(0x21, 0x3C)
    OP_73(0x21)

    def lambda_89C2():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_89C2)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x105, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_8B2C")

    label("loc_89FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8A8D")

    ChrTalk(    #298
        0x105,
        (
            "#040FHmm... I'm going to need permission to go out\x01",
            "of the academy grounds, aren't I?\x02\x03",

            "I should go let the dean know what I'm doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B2C")

    label("loc_8A8D")


    ChrTalk(    #299
        0x105,
        (
            "#044FOh, right...\x02\x03",

            "Hmm... I'm going to need permission to go out\x01",
            "of the academy grounds, aren't I?\x02\x03",

            "#040FI should go let the dean know what I'm doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8B2C")

    TalkEnd(0xFF)
    Return()

    # Function_38_8949 end

    def Function_39_8B30(): pass

    label("Function_39_8B30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #300
        "\x07\x00#3SLechteeeeeeeeer!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 45960, 0, 61200, 180)
    SetChrPos(0x11, 45960, 0, 61200, 180)
    SetChrPos(0x105, 61540, 0, 22500, 0)
    SetChrChipByIndex(0x105, 22)
    SetChrSubChip(0x105, 0)
    SetChrFlags(0x105, 0x8)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_6D(45900, 0, 47400, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(356, 0)
    OP_1D(0xE)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_43(0x10, 0x3, 0x0, 0x28)
    Sleep(2000)
    OP_43(0x11, 0x3, 0x0, 0x29)
    Sleep(1000)

    def lambda_8C3A():
        OP_6D(45900, 0, 33400, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8C3A)
    Sleep(400)

    ChrTalk(    #301 op#A op#5
        0x11,
        (
            "#1891F#30A#6PGET BACK HERE!\x05\x02\x03",

            "#18AToday's the day you're finally going to do \x01",
            "some work!\x02",
        )
    )

    WaitChrThread(0x21, 0x0)

    def lambda_8CB9():
        OP_6D(62500, 0, 23800, 3300)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8CB9)

    def lambda_8CD1():
        OP_67(0, 6820, -10000, 3300)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8CD1)

    def lambda_8CE9():
        OP_6C(120000, 3300)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8CE9)

    def lambda_8CF9():
        OP_6B(2580, 3300)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_8CF9)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x11, 0x3)
    OP_22(0x7D, 0x0, 0x64)

    NpcTalk(    #302
        0x105,
        "Voice",
        "#3S#2PEeek!\x02",
    )


    ChrTalk(    #303
        0x11,
        "#3S#1PAaah!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_8D4F():
        OP_96(0xFE, 0xF064, 0x0, 0x63D8, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D4F)
    OP_56(0x1)
    OP_59()
    WaitChrThread(0x11, 0x1)

    def lambda_8D75():
        OP_6D(60880, 0, 22420, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8D75)

    def lambda_8D8D():
        OP_67(0, 6600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8D8D)

    def lambda_8DA5():
        OP_6C(220000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8DA5)

    def lambda_8DB5():
        OP_6B(2260, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_8DB5)
    Sleep(700)
    ClearChrFlags(0x105, 0x8)
    Sleep(150)
    SetChrFlags(0x105, 0x800)
    WaitChrThread(0x21, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8DF0():
        OP_8E(0xFE, 0xF064, 0x0, 0x5FF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DF0)

    ChrTalk(    #304
        0x11,
        "#643FK-Kloe?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #305
        0x11,
        "#642FI'm so sorry. Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x105,
        "#045F#5P...Y-Yes, I'm fine.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(700)
    ClearChrFlags(0x105, 0x800)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x105, 61540, 0, 22500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #307
        0x105,
        "#042F#5POur pincer attack didn't work all that well...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #308
        0x10,
        "Voice",
        (
            "#6PHahaha. You'll have to do better than that\x01",
            "if you want to catch the almighty Lechter!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8F5F():
        OP_6D(58540, 6300, 20240, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8F5F)

    def lambda_8F77():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8F77)

    def lambda_8F8F():
        OP_6B(2160, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_8F8F)

    def lambda_8F9F():
        OP_8C(0xFE, 220, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8F9F)
    Sleep(100)

    def lambda_8FB2():
        OP_8C(0xFE, 220, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8FB2)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #309
        0x11,
        "#1891F#5PHow'd he get up there so fast?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x105,
        "#042F#5PHis agility is amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x10,
        (
            "#1778FHAH! You've got no one to blame but yourselves\x01",
            "for letting me get away. So long, suckers!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 220, 500)

    def lambda_908B():
        OP_8E(0xFE, 0xD7DC, 0x2328, 0x404C, 0xED8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_908B)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x11, 61540, 0, 24560, 220)
    Fade(1000)
    OP_6D(60880, 0, 22420, 0)
    OP_67(0, 6600, -10000, 0)
    OP_6C(220000, 0)
    OP_6B(2260, 0)
    Sleep(1000)

    ChrTalk(    #312
        0x11,
        (
            "#646F#6PGET. BACK. HEEEREEE!\x02\x03",

            "#1891F#3SWe'll see who's a sucker when you're chained\x01",
            "to a chair under a mountain of paperwork!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 315, 500)

    def lambda_918C():
        OP_8E(0xFE, 0xE3D0, 0x0, 0x6A7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_918C)
    WaitChrThread(0x11, 0x1)

    def lambda_91AC():
        OP_8E(0xFE, 0xB504, 0x0, 0x6A7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_91AC)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    OP_8C(0x105, 40, 400)
    Sleep(500)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)

    ChrTalk(    #313
        0x105,
        (
            "#047F#5P...After all the times I've chased him around,\x01",
            "I know there's got to be more to this than it\x01",
            "seems.\x02\x03",

            "He's not making it look like he's up there--\x01",
            "he's making it look like he isn't... But is that\x01",
            "all there is to it?\x02\x03",

            "#040FLet's go and have a look, anyway.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_39_8B30 end

    def Function_40_9305(): pass

    label("Function_40_9305")


    def lambda_930B():
        OP_8E(0xFE, 0xB388, 0x0, 0x733C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_930B)
    WaitChrThread(0x10, 0x1)

    def lambda_932B():
        OP_8E(0xFE, 0xB964, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_932B)
    WaitChrThread(0x10, 0x1)

    def lambda_934B():
        OP_8E(0xFE, 0xEA74, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_934B)
    WaitChrThread(0x10, 0x1)

    def lambda_936B():
        OP_8E(0xFE, 0xF244, 0x0, 0x6590, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_936B)
    WaitChrThread(0x10, 0x1)

    def lambda_938B():
        OP_8E(0xFE, 0xF244, 0x0, 0x4C2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_938B)
    WaitChrThread(0x10, 0x1)
    SetChrPos(0x10, 59480, 9000, 21480, 40)
    Return()

    # Function_40_9305 end

    def Function_41_93B7(): pass

    label("Function_41_93B7")


    def lambda_93BD():
        OP_8E(0xFE, 0xB388, 0x0, 0x733C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_93BD)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)

    def lambda_9422():
        OP_8E(0xFE, 0xB964, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9422)
    WaitChrThread(0x11, 0x1)

    def lambda_9442():
        OP_8E(0xFE, 0xEA74, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9442)
    Sleep(1500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)

    def lambda_9479():
        OP_8E(0xFE, 0xF244, 0x0, 0x6590, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9479)
    WaitChrThread(0x11, 0x1)

    def lambda_9499():
        OP_8E(0xFE, 0xF244, 0x0, 0x571C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9499)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_41_93B7 end

    def Function_42_94B4(): pass

    label("Function_42_94B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_63(0x10)
    OP_C4(0x0, 0x20000000)
    OP_6D(48450, 9000, 25150, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(300000, 0)
    OP_6E(304, 0)
    OP_11(0xF5, 0xF5, 0xFF, 0x9470, 0x2BF20, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 50000, 9000, 20820, 90)
    SetChrPos(0x105, 56900, 9000, 19020, 270)
    OP_4A(0x10, 255)
    SetChrFlags(0x15, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #314
        0x105,
        "Voice",
        "...I knew I'd find you here.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0xBB8)

    def lambda_9589():
        OP_6D(49430, 9000, 23670, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9589)

    def lambda_95A1():
        OP_8F(0xFE, 0xCE40, 0x2328, 0x4E84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_95A1)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 400)
    WaitChrThread(0x105, 0x2)
    Sleep(500)

    ChrTalk(    #315
        0x10,
        (
            "#1770F#5POh! Look who we've got here.\x02\x03",

            "#1775FGreat weather, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x105,
        (
            "#047F#6PPerhaps so, but you can't honestly believe I came\x01",
            "to talk to you about the weather.\x02\x03",

            "#042FIf you have enough free time to laze around on the\x01",
            "roof, come and do some work. Everyone could use\x01",
            "your help, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x10,
        (
            "#1774F#5PHey, they need me a lot less than you'd think.\x02\x03",

            "#1772FAnd predicting the weather ten years in the\x01",
            "future takes a lot of brainpower, you know.\x01",
            "I need to concentrate right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x105,
        "#045F#6P(How does he think up these things...?)\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #319
        0x105,
        (
            "#542F#6P(Still, going by my experience with him...)\x02\x03",

            "(...when he acts like this, he's usually\x01",
            "willing to listen to me.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_988A():
        OP_6D(48730, 9000, 23940, 1600)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_988A)

    def lambda_98A2():
        OP_8E(0xFE, 0xC8F0, 0x2328, 0x5208, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_98A2)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    Sleep(500)
    OP_1D(0x75)
    WaitChrThread(0x105, 0x2)
    Sleep(500)

    ChrTalk(    #320
        0x105,
        (
            "#543F#6PUmm... Hey, Lechter?\x02\x03",

            "#048FI just wanted to say thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x0, 0x1, 0xC8, 0x2)
    Sleep(800)
    SetChrSubChip(0x10, 1)
    Sleep(100)
    SetChrSubChip(0x10, 2)
    Sleep(300)

    ChrTalk(    #321
        0x10,
        "#1773F#5P...Thanks? For what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x105,
        (
            "#543F#6PA lot of things, really.\x02\x03",

            "You've done an awful lot to help me ever since\x01",
            "I enrolled here.\x02\x03",

            "#542FBut because you're always trying to act like you\x01",
            "aren't or you're running away from me, I've never\x01",
            "been able to say thanks for any of it.\x02\x03",

            "I feel like I owe it to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x10, 3)
    Sleep(500)

    ChrTalk(    #323
        0x10,
        (
            "#1775F#5P...Yeah, I'm lost. I got no clue what you're\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x105,
        "#048F#6PHeehee...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 51640, 9000, 20870, 0)
    SetChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 23)
    SetChrSubChip(0x105, 0)
    OP_0D()

    def lambda_9B28():
        OP_6B(2650, 25000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_9B28)
    Sleep(500)

    ChrTalk(    #325
        0x105,
        (
            "#542F#6PYou asked me a long time ago what it was that\x01",
            "I came here to do, didn't you?\x02\x03",

            "#047F...I hated the life I had before enrolling here.\x02\x03",

            "I always felt like I was being pushed around by\x01",
            "everyone and everything around me instead of\x01",
            "really achieving anything for myself.\x02\x03",

            "And it was that I hated most of all. I felt empty.\x01",
            "Worthless. \x02\x03",

            "#049FThat was part of why I didn't want to try to answer\x01",
            "your question...or even think about it.\x02\x03",

            "It was like if I accepted how weak I was inside,\x01",
            "I'd never be able to get any stronger.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #326
        0x105,
        (
            "#045F#6PBut that's not how I feel now. I'm not empty at\x01",
            "all anymore.\x02\x03",

            "#542FThanks to coming here and meeting you and all of\x01",
            "my friends, I've learned so many new things.\x02\x03",

            "I was able to do things for myself, too, instead of\x01",
            "just relying on others for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x10,
        "#1775F#5PYeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x105,
        "#543F#6PSo that's why I wanted to thank you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #329
        0x10,
        (
            "#1773F#5P...Man.\x02\x03",

            "#1771FI told you before you were too serious, right?\x02\x03",

            "You've been thinking about that one offhand\x01",
            "thing all this time? I never saw that coming! ☆\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x8, 0x9, 0xC8, 0x2)
    Sleep(1000)

    ChrTalk(    #330
        0x105,
        (
            "#045F#6PYou're trying to make fun of me again,\x01",
            "aren't you...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 1)
    Sleep(500)

    ChrTalk(    #331
        0x105,
        (
            "#542F#6PWhat about you, though?\x02\x03",

            "Why did you choose to come here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10,
        (
            "#1773F#5PMe?\x02\x03",

            "#1776FHmm...\x02\x03",

            "#1775FI had nothing better to do, I guess?\x01",
            "Seemed like a good way to kill time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x105,
        (
            "#543F#6PHeh. Really?\x02\x03",

            "#040FWell, as long as you're here, you may as\x01",
            "well do some work.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrPos(0x105, 51440, 9000, 21000, 0)
    SetChrSubChip(0x105, 0)
    ClearChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_8C(0x105, 270, 500)

    def lambda_A164():
        OP_6D(49000, 9000, 25440, 1500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_A164)

    def lambda_A17C():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A17C)

    def lambda_A18C():
        OP_8F(0xFE, 0xC670, 0x2328, 0x51E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A18C)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 21)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x105, 50700, 9000, 20960, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #334
        0x10,
        "#1773F#5PWait...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x105,
        (
            "#042F#12PTomorrow is the Student Council's general meeting.\x01",
            "Which means you have a lot to do. AND you need to\x01",
            "do it all by the end of the day.\x02\x03",

            "There's a mountain of it just waiting for you to get\x01",
            "started on!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #336 op#A
        0x10,
        "#1773F#5P#12AH-Hold up a second!\x02",
    )


    def lambda_A310():
        OP_8F(0xFE, 0xC9F4, 0x2328, 0x51E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A310)

    def lambda_A32B():
        OP_8F(0xFE, 0xC738, 0x2328, 0x5154, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A32B)
    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #337
        0x10,
        (
            "#1772F#5PDon't do this, Kloe!\x02\x03",

            "I can explain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x105,
        "#041F#5PI'm not going to listen!\x02",
    )

    CloseMessageWindow()

    def lambda_A3AA():
        OP_8F(0xFE, 0xEB28, 0x2328, 0x51E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3AA)

    def lambda_A3C5():
        OP_8F(0xFE, 0xE86C, 0x2328, 0x5154, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A3C5)
    Sleep(1000)

    ChrTalk(    #339 op#A
        0x10,
        "#1P#22ASpare me! Pleeeeeease!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    Sleep(300)

    def lambda_A412():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_A412)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #340
        (
            "\x18\x07\x0C#40WThis was the first and last chance I ever had to thank\x01",
            "Lechter for all he did for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #341
        (
            "\x18\x07\x0C#40WThe day after that year's academy festival, he suddenly\x01",
            "registered his intent to withdraw from school...and was\x01",
            "never seen there again.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #342
        (
            "\x18\x07\x0C#40W(He was himself to the very end, though, making a\x01",
            "#5W#40Wsudden appearance in the Student Council-organized\x01",
            "#5W#40Wplay's final scene, ruining it for his amusement.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #343
        "\x18\x07\x0C#40WThen, two years later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #344
        (
            "\x18\x07\x0C#40W...I ended up meeting him once more, in a place and\x01",
            "way I never would have expected...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x20000000)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0xA, 0x3, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #345
        "\x07\x00Side Story [Descended Wings] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A775")
    Sleep(1000)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x20)
    OP_3E(0x2CD, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #346
        "\x07\x05Received \x1F\xCD\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(6000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #347
        "\x07\x05Received \x07\x026,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_A775")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_94B4 end

    def Function_43_A782(): pass

    label("Function_43_A782")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x105, 57990, 9000, 18750, 270)
    OP_6D(58320, 9000, 18760, 0)
    OP_67(0, 7390, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(314000, 0)
    OP_6E(297, 0)
    Sleep(1000)

    def lambda_A7E7():
        OP_6D(54100, 9000, 19210, 2500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_A7E7)

    def lambda_A7FF():
        OP_6B(2550, 2500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A7FF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    Sleep(500)

    ChrTalk(    #348
        0x105,
        (
            "#543F#12P(...I knew I wouldn't find him here.)\x02\x03",

            "#040F(Let's try somewhere else for now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x2FA7)
    EventEnd(0x0)
    Return()

    # Function_43_A782 end

    def Function_44_A882(): pass

    label("Function_44_A882")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(17840, 0, 45920, 0)
    SetChrPos(0x3, 17230, 0, 46030, 90)
    SetChrPos(0x2, 17890, 0, 46670, 90)
    SetChrPos(0x1, 17890, 0, 45370, 90)
    SetChrPos(0x0, 18510, 0, 46030, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 46)
    Call(0, 47)
    Fade(500)
    OP_6D(20220, 0, 46020, 0)
    SetChrPos(0x0, 20220, 0, 46020, 90)
    SetChrPos(0x1, 20220, 0, 46020, 90)
    SetChrPos(0x2, 20220, 0, 46020, 90)
    SetChrPos(0x3, 20220, 0, 46020, 90)
    EventEnd(0x0)
    Return()

    # Function_44_A882 end

    def Function_45_A97D(): pass

    label("Function_45_A97D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(17840, 0, 45920, 0)
    SetChrPos(0x0, 17230, 0, 46030, 270)
    SetChrPos(0x1, 17890, 0, 46670, 270)
    SetChrPos(0x2, 17890, 0, 45370, 270)
    SetChrPos(0x3, 18510, 0, 46030, 270)
    OP_0D()
    Call(0, 46)
    Call(0, 48)
    NewScene("ED6_DT21/C4102   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_45_A97D end

    def Function_46_A9F5(): pass

    label("Function_46_A9F5")

    LoadEffect(0x0, "map\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_46_A9F5 end

    def Function_47_AAE7(): pass

    label("Function_47_AAE7")


    def lambda_AAED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AAED)

    def lambda_AAFF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AAFF)

    def lambda_AB11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AB11)

    def lambda_AB23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AB23)
    Sleep(2500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB4B")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_AB4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB62")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_AB62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB79")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_AB79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB90")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_AB90")

    Return()

    # Function_47_AAE7 end

    def Function_48_AB91(): pass

    label("Function_48_AB91")


    def lambda_AB97():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AB97)

    def lambda_ABA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_ABA9)

    def lambda_ABBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_ABBB)

    def lambda_ABCD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_ABCD)
    Sleep(2000)
    Return()

    # Function_48_AB91 end

    def Function_49_ABDF(): pass

    label("Function_49_ABDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_AD5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_AC85")

    ChrTalk(    #349
        0x105,
        (
            "#047FHe's hiding, but he wants us to find him,\x01",
            "so he's not going to have left the school\x01",
            "grounds.\x02\x03",

            "#042FHe's somewhere in them. I'm sure of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD58")

    label("loc_AC85")


    ChrTalk(    #350
        0x105,
        (
            "#047FI'm sure he hasn't left the school grounds\x01",
            "this time.\x02\x03",

            "#049FEven if he often does wander into Ruan to play\x01",
            "around and gamble...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)

    ChrTalk(    #351
        0x105,
        "#047F*sigh* He really is unbelievable.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AD58")

    Jump("loc_B00A")

    label("loc_AD5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_AF23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_ADD7")

    ChrTalk(    #352
        0x105,
        (
            "#040FI don't think Lechter's gone outside the academy\x01",
            "grounds. \x02\x03",

            "I should keep looking around inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF20")

    label("loc_ADD7")


    ChrTalk(    #353
        0x105,
        (
            "#047FI don't think Lechter's gone outside the academy \x01",
            "grounds. \x02\x03",

            "#040FIf he had, Sieg would have noticed him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x152,
        (
            "#733FTh-That's some amazing vision that bird\x01",
            "of yours has...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x13B,
        (
            "#640FBut you're probably right. He would've needed\x01",
            "permission to leave, too, just like we do.\x02\x03",

            "We should stick to looking indoors for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_AF20")

    Jump("loc_B00A")

    label("loc_AF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_B00A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_AF7B")

    ChrTalk(    #356
        0x105,
        (
            "#047FI've got no reason to be going out of the grounds\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00A")

    label("loc_AF7B")


    ChrTalk(    #357
        0x105,
        (
            "#047FI've got no reason to be going out of the grounds\x01",
            "right now.\x02\x03",

            "#040FI can't imagine any of the students I'm looking\x01",
            "for have left.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_B00A")

    TalkEnd(0xFF)
    Return()

    # Function_49_ABDF end

    def Function_50_B00E(): pass

    label("Function_50_B00E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2511   ._SN", 112, 0, 0)
    IdleLoop()
    TalkEnd(0xFF)
    Return()

    # Function_50_B00E end

    def Function_51_B026(): pass

    label("Function_51_B026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B070")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #358
        "\x07\x05It's still quite warm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_B18F")

    label("loc_B070")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #359
        "\x07\x05It's still quite warm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #360
        0x13B,
        (
            "#647FHe should still be somewhere near here.\x02\x03",

            "#649FHeh. We've finally got you cornered now,\x01",
            "Lechter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x152,
        (
            "#735FRight.\x02\x03",

            "#732FHe'll regret all the trouble he's caused when\x01",
            "we're through with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x105,
        "#045FA-Ahaha...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_B18F")

    TalkEnd(0xFF)
    Return()

    # Function_51_B026 end

    SaveToFile()

Try(main)
