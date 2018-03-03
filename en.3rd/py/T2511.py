from ED63RDScenarioHelper import *

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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Leo',                                  # 11
        'Lucy',                                 # 12
        'Monika',                               # 13
        'Clara',                                # 14
        'Lechter',                              # 15
        'Deborah',                              # 16
        'Ms. Wiola',                            # 17
        'Fauna',                                # 18
        'Janitor Parkes',                       # 19
        'Roy',                                  # 20
        'Patrick',                              # 21
        'Freyja',                               # 22
        'Rigel',                                # 23
        'Rhody',                                # 24
        'Board',                                # 25
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
        'ED6_DT07/CH01130 ._CH',             # 00
        'ED6_DT07/CH01080 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01093 ._CH',             # 07
        'ED6_DT07/CH02680 ._CH',             # 08
        'ED6_DT07/CH02690 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01090 ._CH',             # 0B
        'ED6_DT07/CH02670 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01093 ._CH',             # 10
        'ED6_DT07/CH01373 ._CH',             # 11
        'ED6_DT07/CH01590 ._CH',             # 12
        'ED6_DT07/CH02910 ._CH',             # 13
        'ED6_DT26/CH20777 ._CH',             # 14
        'ED6_DT07/CH02393 ._CH',             # 15
        'ED6_DT07/CH02553 ._CH',             # 16
        'ED6_DT07/CH00043 ._CH',             # 17
        'ED6_DT26/CH20779 ._CH',             # 18
        'ED6_DT26/CH20780 ._CH',             # 19
        'ED6_DT26/CH20778 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH01130P._CP',             # 00
        'ED6_DT07/CH01080P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01093P._CP',             # 07
        'ED6_DT07/CH02680P._CP',             # 08
        'ED6_DT07/CH02690P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01090P._CP',             # 0B
        'ED6_DT07/CH02670P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01093P._CP',             # 10
        'ED6_DT07/CH01373P._CP',             # 11
        'ED6_DT07/CH01590P._CP',             # 12
        'ED6_DT07/CH02910P._CP',             # 13
        'ED6_DT26/CH20777P._CP',             # 14
        'ED6_DT07/CH02393P._CP',             # 15
        'ED6_DT07/CH02553P._CP',             # 16
        'ED6_DT07/CH00043P._CP',             # 17
        'ED6_DT26/CH20779P._CP',             # 18
        'ED6_DT26/CH20780P._CP',             # 19
        'ED6_DT26/CH20778P._CP',             # 1A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 28640,
        Z                   = 0,
        Y                   = 57160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 31500,
        Z                   = 0,
        Y                   = 58600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 3940,
        Z                   = 100,
        Y                   = -4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 3330,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -4660,
        Z                   = 0,
        Y                   = 2600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -30680,
        Z                   = 0,
        Y                   = 28760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 31500,
        Z                   = 0,
        Y                   = 53100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 2940,
        Z                   = 0,
        Y                   = 2450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -28600,
        Z                   = 0,
        Y                   = 27930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -31820,
        Z                   = 0,
        Y                   = 26670,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE8,
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


    DeclActor(
        TriggerX            = 30990,
        TriggerZ            = 0,
        TriggerY            = 55250,
        TriggerRange        = 1000,
        ActorX              = 30990,
        ActorZ              = 1100,
        ActorY              = 55250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29620,
        TriggerZ            = 0,
        TriggerY            = 60000,
        TriggerRange        = 1000,
        ActorX              = 29620,
        ActorZ              = 1500,
        ActorY              = 60000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2020,
        TriggerZ            = 0,
        TriggerY            = 42880,
        TriggerRange        = 400,
        ActorX              = 2020,
        ActorZ              = 800,
        ActorY              = 42880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3020,
        TriggerZ            = 0,
        TriggerY            = 42000,
        TriggerRange        = 400,
        ActorX              = 3020,
        ActorZ              = 800,
        ActorY              = 42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
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
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_476",          # 00, 0
        "Function_1_6E5",          # 01, 1
        "Function_2_7C5",          # 02, 2
        "Function_3_942",          # 03, 3
        "Function_4_966",          # 04, 4
        "Function_5_98A",          # 05, 5
        "Function_6_98F",          # 06, 6
        "Function_7_1081",         # 07, 7
        "Function_8_1230",         # 08, 8
        "Function_9_1568",         # 09, 9
        "Function_10_18AF",        # 0A, 10
        "Function_11_1F81",        # 0B, 11
        "Function_12_283D",        # 0C, 12
        "Function_13_29A9",        # 0D, 13
        "Function_14_2A71",        # 0E, 14
        "Function_15_2C2B",        # 0F, 15
        "Function_16_2D99",        # 10, 16
        "Function_17_2F01",        # 11, 17
        "Function_18_302D",        # 12, 18
        "Function_19_3237",        # 13, 19
        "Function_20_3639",        # 14, 20
        "Function_21_45BC",        # 15, 21
        "Function_22_4F67",        # 16, 22
        "Function_23_557B",        # 17, 23
        "Function_24_55DC",        # 18, 24
        "Function_25_5EC8",        # 19, 25
        "Function_26_5F7C",        # 1A, 26
        "Function_27_6A13",        # 1B, 27
        "Function_28_6A6D",        # 1C, 28
        "Function_29_6AC7",        # 1D, 29
        "Function_30_6B26",        # 1E, 30
        "Function_31_6B7E",        # 1F, 31
        "Function_32_6BD6",        # 20, 32
        "Function_33_6C6E",        # 21, 33
        "Function_34_72EB",        # 22, 34
        "Function_35_7351",        # 23, 35
        "Function_36_73BB",        # 24, 36
        "Function_37_7421",        # 25, 37
        "Function_38_747A",        # 26, 38
        "Function_39_7555",        # 27, 39
        "Function_40_75E7",        # 28, 40
    )


    def Function_0_476(): pass

    label("Function_0_476")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4FA")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2200, 0, 42000, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -150, 0, 42850, 90)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -31600, 0, 58830, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -28790, 0, 53110, 90)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_65E")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_509")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_65E")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_57D")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2940, 0, 1420, 180)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 2940, 0, 490, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30690, 0, 27510, 0)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_65E")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_604")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6140, 100, -540, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x15, 0x4)
    OP_4A(0x15, 255)
    SetChrChipByIndex(0x15, 16)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6100, 100, -2320, 0)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x4)
    OP_4A(0x14, 255)
    SetChrChipByIndex(0x14, 17)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x12, 0x80)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_65E")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 31370, 0, 53040, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x14, 31040, 0, 26400, 90)
    ClearChrFlags(0x1A, 0x80)

    label("loc_65E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_68D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_68D")

    Jump("loc_6E4")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_6CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_6B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_6C9")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6C9")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_6C9")

    Jump("loc_6E4")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_6E4")

    Return()

    # Function_0_476 end

    def Function_1_6E5(): pass

    label("Function_1_6E5")

    OP_B1("T2511_n")
    OP_82(0x82, 0x0)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x4, 0x4)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C4")
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_A1(0x20, 0x4)
    SetChrPos(0x20, 2040, 0, 42880, 0)
    OP_D1(32, 0, 90000, 0, 0)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x4, 0x4)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_786")
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3")
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x4, 0x4)
    ExitThread()
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_7C4")
    OP_64(0x4, 0x1)
    OP_72(0x1001, 0x0)
    ExitThread()

    label("loc_7C4")

    Return()

    # Function_1_6E5 end

    def Function_2_7C5(): pass

    label("Function_2_7C5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_92C")

    label("loc_7EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_803")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_92C")

    label("loc_803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_92C")

    label("loc_81C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_835")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_92C")

    label("loc_835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_92C")

    label("loc_84E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_867")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_92C")

    label("loc_867")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_92C")

    label("loc_880")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_92C")

    label("loc_899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_92C")

    label("loc_8B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_92C")

    label("loc_8CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_92C")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_92C")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_92C")

    label("loc_916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_92C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_92C")

    label("loc_941")

    Return()

    # Function_2_7C5 end

    def Function_3_942(): pass

    label("Function_3_942")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_965")
    OP_8D(0xFE, -3430, 3160, -5050, 1500, 2000)
    Jump("Function_3_942")

    label("loc_965")

    Return()

    # Function_3_942 end

    def Function_4_966(): pass

    label("Function_4_966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_8D(0xFE, 510, 43490, -1140, 41320, 2000)
    Jump("Function_4_966")

    label("loc_989")

    Return()

    # Function_4_966 end

    def Function_5_98A(): pass

    label("Function_5_98A")

    Call(0, 6)
    Return()

    # Function_5_98A end

    def Function_6_98F(): pass

    label("Function_6_98F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A47")

    ChrTalk(    #0
        0x17,
        (
            "Seeing you students so energetic always\x01",
            "brings a smile to my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x17,
        (
            "We're still open if you haven't had anything\x01",
            "to eat yet, by the way. Just hop in line.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC1")

    label("loc_A47")


    ChrTalk(    #2
        0x17,
        "Whew... The lunchtime rush is finally over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x17,
        (
            "I never cease to be amazed by how much\x01",
            "energy you students have.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_AC1")

    Jump("loc_107D")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B7C")

    ChrTalk(    #4
        0x17,
        "Maybe it's just me, but you're looking blue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x17,
        (
            "We're open until late if you're feeling hungry.\x01",
            "Sometimes a good meal's all you need to perk\x01",
            "yourself right up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4C")

    label("loc_B7C")


    ChrTalk(    #6
        0x17,
        (
            "One of the girls in the Student Council has\x01",
            "been working awfully late today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x17,
        (
            "We're open until late, of course, so hopefully\x01",
            "she'll come down here if she's feeling hungry.\x01",
            "That goes for you, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C4C")

    Jump("loc_107D")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_D4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C96")

    ChrTalk(    #8
        0x17,
        "All right, kids! Make sure to form a clear line.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_C96")


    ChrTalk(    #9
        0x17,
        "So much to do, so much to do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x17,
        (
            "The second the exams finish, this place is\x01",
            "teeming with students.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x17,
        (
            "I'm kind of used to it at this point, though.\x01",
            "It always happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D49")

    Jump("loc_107D")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DB6")

    ChrTalk(    #12
        0x17,
        (
            "I'm 100% sure I haven't seen Lechter here\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x17,
        "Maybe Parkes knows something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F3D")

    label("loc_DB6")


    ChrTalk(    #14
        0x13B,
        (
            "#640FExcuse me, ma'am... You haven't spotted our\x01",
            "president anywhere, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x17,
        "You're looking for him again, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x152,
        "#734FHaha... Sad as it is to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x17,
        "Well, I wish I could say I have, but I haven't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        (
            "He's always sure to say hi whenever he passes\x01",
            "by me, too, so I'd definitely noticed if he'd been\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#044FH-He does?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x13B,
        "#647F(That's oddly...sweet of him?)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F3D")

    Jump("loc_107D")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_107D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FDA")

    ChrTalk(    #21
        0x17,
        "Kids your age always have ravenous appetites.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x17,
        (
            "So if you want something to eat, don't feel bad\x01",
            "about it! Come right along here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107D")

    label("loc_FDA")


    ChrTalk(    #23
        0x17,
        (
            "Oh, I don't think I've seen you here before.\x01",
            "Are you a first year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x17,
        (
            "This is the school cafeteria. When you want\x01",
            "something to eat, you come right here!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_107D")

    TalkEnd(0x17)
    Return()

    # Function_6_98F end

    def Function_7_1081(): pass

    label("Function_7_1081")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_108E")
    Jump("loc_122C")

    label("loc_108E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1098")
    Jump("loc_122C")

    label("loc_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_10A2")
    Jump("loc_122C")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_10AC")
    Jump("loc_122C")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_122C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1151")

    ChrTalk(    #25
        0xFE,
        (
            "There was a girl who came to talk to me not\x01",
            "long ago because she'd lost something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "She might still be upstairs if you're looking\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122C")

    label("loc_1151")


    ChrTalk(    #27
        0xFE,
        "Hey there. You looking for someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Actually, there was a girl who came to talk to\x01",
            "me not long ago because she'd lost something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "You're not looking for her, are you? She went\x01",
            "up the stairs if you are.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_122C")

    TalkEnd(0xFE)
    Return()

    # Function_7_1081 end

    def Function_8_1230(): pass

    label("Function_8_1230")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12F7")

    ChrTalk(    #30
        0xFE,
        (
            "Looks like I've gone and lost the key to this\x01",
            "room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Oh, well. It'll probably turn up at some point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Guess we'll just have to do some training by\x01",
            "ourselves today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135F")

    label("loc_12F7")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #33
        0xFE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Where did I put the key to get in here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "We're stuck outside without that!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_135F")

    Jump("loc_1554")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_136C")
    Jump("loc_1554")

    label("loc_136C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_14A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13E1")

    ChrTalk(    #36
        0xFE,
        "Being a third year is really tough, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "How am I supposed to get through to you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_13E1")


    ChrTalk(    #38
        0xFE,
        (
            "Everything changes when you become a third year.\x01",
            "Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "If you think that attitude's going to get you\x01",
            "through to graduation, you're going to be in\x01",
            "for a very rude awakening.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_149F")

    Jump("loc_1554")

    label("loc_14A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_154D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14FE")

    ChrTalk(    #40
        0xFE,
        "Oh, give me something for my broccoli, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "I think that's fair.\x02",
    )

    CloseMessageWindow()
    Jump("loc_154A")

    label("loc_14FE")


    ChrTalk(    #42
        0xFE,
        "Give me your eggs, Monika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "I'll give you my carrots if you do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_154A")

    Jump("loc_1554")

    label("loc_154D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1554")

    label("loc_1554")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1567")
    OP_4A(0xFE, 255)

    label("loc_1567")

    Return()

    # Function_8_1230 end

    def Function_9_1568(): pass

    label("Function_9_1568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_16CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(    #44
        0xFE,
        (
            "I'm trying to help her find it because I don't\x01",
            "really have any choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I just hope it doesn't turn out to have been\x01",
            "somewhere stupid obvious the whole time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_1625")


    ChrTalk(    #46
        0xFE,
        "Clara's gone and lost the key to this room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "She gave me a real earful when I lost it,\x01",
            "and then she goes and does the exact\x01",
            "same thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Typical, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_16CC")

    Jump("loc_189B")

    label("loc_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_16D9")
    Jump("loc_189B")

    label("loc_16D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_173F")

    ChrTalk(    #49
        0xFE,
        "Yeah, I'm not buying that. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I mean, look at you! You never studied at all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D2")

    label("loc_173F")


    ChrTalk(    #51
        0xFE,
        (
            "I'm managing to score in line with the average!\x01",
            "I'm doing fine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "As long as I keep studying, I'll be able to keep\x01",
            "up. I'm sure I will.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_17D2")

    Jump("loc_189B")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1854")

    ChrTalk(    #53
        0xFE,
        (
            "You might be older than me, but that doesn't\x01",
            "mean you can steal my food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "That's abuse of seniority!\x02",
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1854")


    ChrTalk(    #55
        0xFE,
        "But that's not fair!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I don't want to trade!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_188D")

    Jump("loc_189B")

    label("loc_1890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_189B")
    Call(0, 21)

    label("loc_189B")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18AE")
    OP_4A(0xFE, 255)

    label("loc_18AE")

    Return()

    # Function_9_1568 end

    def Function_10_18AF(): pass

    label("Function_10_18AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_19A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_18F5")

    ChrTalk(    #57
        0x12,
        "#1782F...Find him before the end of the day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19A2")

    label("loc_18F5")


    ChrTalk(    #58
        0x12,
        (
            "#1782FTomorrow is the general meeting of the\x01",
            "Student Council.\x02\x03",

            "You must find him before then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x105,
        (
            "#042FR-Right!\x02\x03",

            "#045F(He never says more than he has to, does he?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_19A2")

    Jump("loc_1F7D")

    label("loc_19A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_19AF")
    Jump("loc_1F7D")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 0)), scpexpr(EXPR_END)), "loc_1A3E")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #60
        0x12,
        (
            "#1782FWell, it's the end of the month.\x02\x03",

            "It's about time for Lechter to make his move.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_1C51")

    label("loc_1A3E")


    ChrTalk(    #61
        0x12,
        (
            "#1780FWhy do you have that envelope...?\x02\x03",

            "#1782F...It was forced on you by Lechter, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#045FAha... Haha...\x02\x03",

            "#040FIt's fine, of course. I'll make sure it's delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#1780F...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x05Received \x07\x02200 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    AddMira(200)

    ChrTalk(    #65
        0x12,
        (
            "#1782FHead south on the highway to reach Ruan.\x01",
            "The mayor's mansion is on the east side of\x01",
            "the town's southern block.\x02\x03",

            "Don't get lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#045FI-I won't. Thank you.\x02\x03",

            "(I wonder if this is supposed to be payment for\x01",
            "doing this errand or something?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F78)

    label("loc_1C51")

    Jump("loc_1F7D")

    label("loc_1C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1CE9")
    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #67
        0x12,
        (
            "#1780FI'll take care of as much of our work as possible\x01",
            "without him for now.\x02\x03",

            "But you must find him.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1EA0")

    label("loc_1CE9")

    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #68
        0x12,
        "#1780F...Do you have business with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x13B,
        (
            "#645FO-Oh, no...\x02\x03",

            "We still haven't found Lechter, though,\x01",
            "I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x152,
        (
            "#734FWe've been looking for him for three days now.\x01",
            "I think it's about time we threw in the towel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "#1782FWe always knew that finding that slacker would\x01",
            "be a herculean task.\x02\x03",

            "But he is in the academy grounds, so it can be\x01",
            "done.\x02\x03",

            "#1783FNo excuses. Catch him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x152,
        "#733FY-Yes, sir!\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A2(0x5)

    label("loc_1EA0")

    Jump("loc_1F7D")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(    #73
        0x12,
        (
            "#1782FThat fool is highly dangerous. If you sight him,\x01",
            "don't attempt to approach him. Inform us at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7D")

    label("loc_1F22")


    ChrTalk(    #74
        0x12,
        (
            "#1780FIf you happen to encounter the Student Council\x01",
            "president, inform us at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F7D")

    TalkEnd(0xFE)
    Return()

    # Function_10_18AF end

    def Function_11_1F81(): pass

    label("Function_11_1F81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1F8E")
    Jump("loc_2839")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_227F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 2)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(    #75
        0x13,
        (
            "#1790FYou should probably be heading back to your room\x01",
            "soon if you've got no reason to be out.\x02\x03",

            "It's past curfew, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227C")

    label("loc_2021")


    ChrTalk(    #76
        0x105,
        (
            "#043FOh, I didn't know you were here, Lucy.\x02\x03",

            "Are you busy working still? It's awfully late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "#1791FI was, yes. It took me a little longer than\x01",
            "I was expecting to finish everything.\x02\x03",

            "I've just finished, though, so it's about time \x01",
            "I started heading back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#049FO-Oh, sure...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x13,
        (
            "#1792FIs something wrong, Kloe?\x02\x03",

            "You seem kind of down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x105,
        "#047FNo... It's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x13,
        (
            "#1790FWell, if you say so...\x02\x03",

            "It's past curfew, though. You should probably\x01",
            "be heading back to your room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        (
            "#042FI suppose...\x02\x03",

            "#049F(That's the last place I want to be right now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7A)

    label("loc_227C")

    Jump("loc_2839")

    label("loc_227F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_22FE")

    ChrTalk(    #83
        0x13,
        (
            "#1793FEvery time I see his face, I just feel like\x01",
            "punching him.\x02\x03",

            "Is that how I really feel about him...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2380")

    label("loc_22FE")


    ChrTalk(    #84
        0x13,
        (
            "#1793FI ended up hitting him again.\x02\x03",

            "...Why did I do it?\x02\x03",

            "#1795FEvery time I see his face, I just feel like\x01",
            "punching him.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2380")

    Jump("loc_2839")

    label("loc_2383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_238D")
    Jump("loc_2839")

    label("loc_238D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2839")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 1)), scpexpr(EXPR_END)), "loc_253F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2427")

    ChrTalk(    #85
        0x13,
        (
            "#1790FIf the Student Council's president causes you\x01",
            "any grief, come and let me know right away.\x02\x03",

            "#1794FI'll...deal with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253C")

    label("loc_2427")


    ChrTalk(    #86
        0x13,
        (
            "#1790FI can't solve all the problems you'll encounter\x01",
            "during your time here as a student...\x02\x03",

            "...but if the Student Council's president causes\x01",
            "you any trouble, that's another story. Come and\x01",
            "let me know right away.\x02\x03",

            "#1794FI'll...deal with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x105,
        "#044FTh-Thank you...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_253C")

    Jump("loc_2839")

    label("loc_253F")


    ChrTalk(    #88
        0x13,
        (
            "#1790FOh...\x02\x03",

            "Are you the new transfer student?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x105,
        (
            "#044FY-Yes, that's right.\x02\x03",

            "Umm... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x13,
        (
            "#1790FI take it this is your first time coming to this\x01",
            "room? There's no need to be so nervous.\x02\x03",

            "#1794FI'm the Student Council's vice president, Lucy\x01",
            "Seiland.\x02\x03",

            "He's our secretary and accountant, Leo.\x02\x03",

            "#1791FIt's a pleasure to meet you. You're very welcome\x01",
            "to come here whenever you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x105,
        (
            "#044F...\x02\x03",

            "#540F(She's so pretty...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #92
        0x105,
        (
            "#542FUmm... My name is Kloe Rinz.\x02\x03",

            "#045FIt's nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x13,
        (
            "#1794FThe pleasure is all mine.\x02\x03",

            "#1790FYour academic life here probably isn't going\x01",
            "to be all smooth sailing, but I'm sure you'll be\x01",
            "fine.\x02\x03",

            "Just try and enjoy yourself. I believe in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x105,
        "#542FTh-Thank you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F79)

    label("loc_2839")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F81 end

    def Function_12_283D(): pass

    label("Function_12_283D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_29A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_28FE")

    ChrTalk(    #95
        0xFE,
        (
            "I'm going to have to start grading all those\x01",
            "papers when I get back to the faculty lounge...\x01",
            "Ugh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Do I have to? Right now, all I want to do is\x01",
            "take the day off...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A5")

    label("loc_28FE")


    ChrTalk(    #97
        0xFE,
        "Whew... I'm so glad the exams are finally over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "The exam period is tough on us teachers, too,\x01",
            "I'll have you know! It's not like we enjoy giving\x01",
            "you them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_29A5")

    TalkEnd(0xFE)
    Return()

    # Function_12_283D end

    def Function_13_29A9(): pass

    label("Function_13_29A9")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2A3E")

    ChrTalk(    #99
        0x19,
        "Hi there, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x19,
        (
            "Heehee. Surprised to see me here? I don't spend\x01",
            "the entire day behind the receptionist desk, you\x01",
            "know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_2A3E")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #101
        0x19,
        "I'll go with one A-set, please.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2A6D")

    TalkEnd(0x19)
    Return()

    # Function_13_29A9 end

    def Function_14_2A71(): pass

    label("Function_14_2A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2C27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2B10")
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #102
        0xFE,
        (
            "Oh, I can deliver that form to him myself\x01",
            "if that would be easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I imagine he's quite familiar with how to fill\x01",
            "it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C27")

    label("loc_2B10")


    ChrTalk(    #104
        0xFE,
        "Oh, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "There's no practice today, as you might be aware.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x105,
        (
            "#040FYes, I am.\x02\x03",

            "We're starting again tomorrow, though, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "That's right. We've got a big tournament coming\x01",
            "up, after all. We really need to get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "Let's put our backs into it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2C27")

    TalkEnd(0xFE)
    Return()

    # Function_14_2A71 end

    def Function_15_2C2B(): pass

    label("Function_15_2C2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2D95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C9E")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #109
        0x11,
        (
            "#730FYep. I've come regarding the club's budget.\x02\x03",

            "Is Rigel still in the classroom?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D95")

    label("loc_2C9E")


    ChrTalk(    #110
        0x11,
        (
            "#733FOh, yeah. Kloe? I probably should've mentioned\x01",
            "this earlier on...\x02\x03",

            "#730F...but you do know you need permission to leave\x01",
            "the grounds, right?\x02\x03",

            "I'm sure the dean won't hesitate to give it to\x01",
            "you if you ask, but permission is permission.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2D95")

    TalkEnd(0xFE)
    Return()

    # Function_15_2C2B end

    def Function_16_2D99(): pass

    label("Function_16_2D99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2E2E")

    ChrTalk(    #111
        0xFE,
        (
            "Still, I'm amazed just how much work he usually\x01",
            "takes care of all on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "I've really got a lot to learn from him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2E2E")


    ChrTalk(    #113
        0xFE,
        "I'm busy helping out Leo with his work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Unfortunately, all I can really do is get things\x01",
            "together for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "...but he does so much for me all the time,\x01",
            "I like to help however I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2EFD")

    TalkEnd(0xFE)
    Return()

    # Function_16_2D99 end

    def Function_17_2F01(): pass

    label("Function_17_2F01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3029")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2FA2")

    ChrTalk(    #116
        0xFE,
        "Logic's the first victim on my list.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I'll have to see if I can find some third years\x01",
            "who look like they've got nothing to do, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3029")

    label("loc_2FA2")


    ChrTalk(    #118
        0xFE,
        "Whew. The exams are finally OVER!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I'm gonna grab something to eat and then get\x01",
            "right to hunting for more club members! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3029")

    TalkEnd(0xFE)
    Return()

    # Function_17_2F01 end

    def Function_18_302D(): pass

    label("Function_18_302D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3091")

    ChrTalk(    #120
        0x1E,
        "Drop by at practice if you ever get the chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1E,
        "We'll always be here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3233")

    label("loc_3091")


    ChrTalk(    #122
        0x1E,
        (
            "Oh, hello, Kloe. How come you haven't been\x01",
            "showing up for practice much lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x105,
        (
            "#044FSorry about that, Rigel...\x02\x03",

            "#043FI've just...had a lot going on lately, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x1E,
        "Oh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x1E,
        (
            "Still, it's you we're talking about, here,\x01",
            "so I always knew there had to be some\x01",
            "kind of legitimate reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1E,
        (
            "Drop by if you get the chance, though.\x01",
            "We'll always be waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x105,
        "#040FI will. Thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3233")

    TalkEnd(0xFE)
    Return()

    # Function_18_302D end

    def Function_19_3237(): pass

    label("Function_19_3237")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3635")
    TurnDirection(0xFE, 0x152, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 0)), scpexpr(EXPR_END)), "loc_32B3")

    ChrTalk(    #128
        0xFE,
        (
            "Lucy is mine, and I'm not letting anyone else\x01",
            "have her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Know when you're beaten, Hans!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3635")

    label("loc_32B3")


    ChrTalk(    #130
        0xFE,
        "Oh, if isn't Hans!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "You're gonna join our club, right? I mean, you rock\x01",
            "at sports stuff. You'd be a perfect fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x152,
        (
            "#735FNot happening, my man.\x02\x03",

            "#730FI've only got time for Lucy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x13B,
        (
            "#659FSo THAT'S why you decided to join the council.\x01",
            "Should've known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x152,
        (
            "#733FWait...\x02\x03",

            "#735FN-No! That wasn't the reason, I just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x13B,
        (
            "#649FI knew something seemed fishy when you\x01",
            "put your name forward. You just weren't\x01",
            "the type.\x02\x03",

            "Is all our work just a game to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Yeah! You should be ashamed of yourself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I won't let you get close to Lucy using such\x01",
            "underhanded trickery!\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x20)
    Sleep(100)

    ChrTalk(    #138
        0xFE,
        (
            "#3SStep back, Hans! She's mine, and I'm not letting\x01",
            "you have her!#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #139
        0x152,
        (
            "#735FHow dare you? Lucy and I are destined to be\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #140
        0x152,
        "#732F#3SYOU step back!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x20)

    ChrTalk(    #141
        0x13B,
        "#645FHere they go again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x105,
        (
            "#045FHaha... Haha...\x02\x03",

            "(Lucy certainly is popular...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F80)

    label("loc_3635")

    TalkEnd(0xFE)
    Return()

    # Function_19_3237 end

    def Function_20_3639(): pass

    label("Function_20_3639")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(1200, 0, 900, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    SetChrPos(0x12, 540, 0, 540, 180)
    SetChrPos(0x13, -500, 0, 700, 180)
    SetChrPos(0x11, 1140, 0, -840, 0)
    SetChrPos(0x10, -60, 0, -1000, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3719"),
        (101, "loc_3738"),
        (SWITCH_DEFAULT, "loc_3757"),
    )


    label("loc_3719")

    SetChrPos(0x105, 100, -500, -9200, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_3757")

    label("loc_3738")

    SetChrPos(0x105, -9240, -250, -3100, 90)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_3757")

    label("loc_3757")


    def lambda_375D():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_375D)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #143
        0x10,
        (
            "#645F#12P*pant*...*pant*...\x02\x03",

            "#646FAidios, help us. Where IS that loser?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        "#734F#12PI would've thought we'd have found him by now...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x13, 400)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #145
        0x11,
        (
            "#737FLucyyy! I'm not sure I can stand much more of\x01",
            "this!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #146
        0x10,
        (
            "#1891F#6PStop your whining, you!\x02\x03",

            "#646FI bet you've secretly been slacking off with your\x01",
            "search the whole time, haven't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #147
        0x11,
        (
            "#732F#11PI have not!\x02\x03",

            "I just don't get it! We're swimming in eyewitness\x01",
            "reports of him, but US running into him? It's not\x01",
            "happening. Why?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(200)
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #148
        0x13,
        (
            "#1794F#1PI don't think our odds of capturing him\x01",
            "today are especially high, Leo.\x02\x03",

            "#1792FWhat should we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x12,
        (
            "#1782F#5PI suppose we'll just have to do what we can\x01",
            "without him for now.\x02\x03",

            "#1780FThe two of us can handle the majority of the \x01",
            "Student Council's work.\x02\x03",

            "But we ARE going to need his approval in the end,\x01",
            "so you two need to keep up your search. Find him \x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B2C():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3B2C)

    def lambda_3B3A():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3B3A)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x10, 0x2)

    ChrTalk(    #150
        0x10,
        "#642F#3PR-Right!\x02",
    )


    ChrTalk(    #151
        0x11,
        "#732FR-Right!\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_8C(0x12, 0, 500)

    def lambda_3B83():
        OP_8E(0xFE, 0x21C, 0xDAC, 0x1D38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3B83)
    Sleep(1000)
    OP_8C(0x13, 180, 400)

    ChrTalk(    #152
        0x13,
        "#1791F#5PI'll see you two later.\x02",
    )

    CloseMessageWindow()

    def lambda_3BD0():

        label("loc_3BD0")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_3BD0")

    QueueWorkItem2(0x11, 2, lambda_3BD0)

    ChrTalk(    #153
        0x11,
        "#738FRight-o. ㈱\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)

    def lambda_3BFE():
        OP_8E(0xFE, 0xC8, 0xDAC, 0x1D38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3BFE)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(500)

    def lambda_3C28():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C28)
    Sleep(100)

    def lambda_3C3B():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3C3B)
    Sleep(300)

    ChrTalk(    #154
        0x10,
        "#645F#6PWell, I guess we'd better get back to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x11,
        "#734F#11P*sigh* If we must...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3CB9"),
        (101, "loc_3D06"),
        (SWITCH_DEFAULT, "loc_3D5A"),
    )


    label("loc_3CB9")


    def lambda_3CBF():
        OP_6D(1200, 0, -800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3CBF)

    def lambda_3CD7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3CD7)

    def lambda_3CE9():
        OP_8E(0xFE, 0x64, 0xFFFFFE0C, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CE9)
    WaitChrThread(0x105, 0x1)
    Jump("loc_3D5A")

    label("loc_3D06")


    def lambda_3D0C():
        OP_6D(400, 0, -1000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3D0C)

    def lambda_3D24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3D24)

    def lambda_3D36():
        OP_8E(0xFE, 0xFFFFF9E8, 0xFFFFFF06, 0xFFFFF3E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3D36)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 45, 400)
    Jump("loc_3D5A")

    label("loc_3D5A")

    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3D98"),
        (101, "loc_3DC1"),
        (SWITCH_DEFAULT, "loc_3DEA"),
    )


    label("loc_3D98")


    def lambda_3D9E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3D9E)
    Sleep(100)

    def lambda_3DB1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3DB1)
    Sleep(300)
    Jump("loc_3DEA")

    label("loc_3DC1")


    def lambda_3DC7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3DC7)
    Sleep(100)

    def lambda_3DDA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3DDA)
    Sleep(300)
    Jump("loc_3DEA")

    label("loc_3DEA")


    ChrTalk(    #156
        0x10,
        (
            "#643F#5PHuh? Kloe?\x02\x03",

            "What brings you here with a pile of printouts\x01",
            "in hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x105,
        (
            "#044FOh...\x02\x03",

            "#045FUmm... Well...\x02\x03",

            "#542FI'm just helping Ms. Wiola with some of her work,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        (
            "#733FBy going around after classes giving\x01",
            "out printouts?\x02\x03",

            "#735FYou're one model student. I would've turned\x01",
            "her down if I was in your position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10,
        (
            "#640F#5PUmm... Well, how about this?\x02\x03",

            "#648FWhy don't we give you a hand with it?\x02\x03",

            "The two of us are gonna be walking around the\x01",
            "school for a while because of some other work,\x01",
            "anyway, so it'd be no skin off our backs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x105,
        (
            "#543FOh, I don't want to trouble you. I was the one who\x01",
            "accepted this task, so it's my duty to see it through\x01",
            "to the end.\x02\x03",

            "#048FWell, if you'll excuse me. I should probably be getting\x01",
            "back to it. Good luck with your own work.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4101():

        label("loc_4101")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_4101")

    QueueWorkItem2(0x10, 2, lambda_4101)

    def lambda_4112():
        OP_8F(0xFE, 0x44C, 0x0, 0xFFFFFF10, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4112)

    def lambda_412D():

        label("loc_412D")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_412D")

    QueueWorkItem2(0x11, 2, lambda_412D)

    def lambda_413E():
        OP_8F(0xFE, 0x7BC, 0x0, 0xFFFFFCB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_413E)
    Sleep(200)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4168"),
        (101, "loc_418B"),
        (SWITCH_DEFAULT, "loc_41CE"),
    )


    label("loc_4168")


    def lambda_416E():
        OP_8E(0xFE, 0x64, 0xDAC, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_416E)
    WaitChrThread(0x105, 0x1)
    Jump("loc_41CE")

    label("loc_418B")


    def lambda_4191():
        OP_8E(0xFE, 0x64, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4191)
    WaitChrThread(0x105, 0x1)

    def lambda_41B1():
        OP_8E(0xFE, 0x64, 0xDAC, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41B1)
    WaitChrThread(0x105, 0x1)
    Jump("loc_41CE")

    label("loc_41CE")


    def lambda_41D4():
        OP_6D(2540, 0, 460, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_41D4)
    WaitChrThread(0x21, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #161
        0x10,
        (
            "#645F#5PSo, like...\x02\x03",

            "#1890F...guess who's sharing a room with her?\x01",
            "Me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        (
            "#733F#12PHuh... Really?\x02\x03",

            "#730FShe's supposed to be a real genius from all\x01",
            "I've heard about her.\x02\x03",

            "#731FSounds like one convenient room arrangement\x01",
            "if you ever find yourself stuck on homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        (
            "#1892F#5PWell, I guess you could see it that way...\x01",
            "But it's like, I dunno...\x02\x03",

            "She's really pleasant and polite and all,\x01",
            "but it's sorta...\x02\x03",

            "#645FIt's like she doesn't want to be super close\x01",
            "to anybody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#735F#12PYeah. I get what you mean.\x02\x03",

            "#730FBut if you're sharing a room with her,\x01",
            "you can't be TOTAL strangers, right?\x01",
            "Don't you talk sometimes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        (
            "#1892F#5PNot really...\x02\x03",

            "'Hi' and 'Good night' is about the most\x01",
            "we do, to be honest.\x02\x03",

            "#1890F(I wish I could talk to her normally...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4523():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4523)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x21, 0xFF)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 0, 51650, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 0, 0, 51650, 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x1A, 0x80)
    OP_A2(0x2F6A)
    EventEnd(0x0)
    Return()

    # Function_20_3639 end

    def Function_21_45BC(): pass

    label("Function_21_45BC")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(31620, 0, 27480, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 29660, 0, 26400, 90)
    SetChrSubChip(0x14, 0)
    Sleep(1000)

    ChrTalk(    #166
        0x14,
        "#5PWhere could it have gone...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x14,
        "#5POh, there it is! Phew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        "#043F#6PUmm... Excuse me...\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x14, 0x105, 400)
    Sleep(300)

    ChrTalk(    #169
        0x14,
        "#11PHey! You're the transfer student, right? Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x14,
        "#11PDo you need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#047F#6PYes, actually. \x02\x03",

            "#542FYou see, Ms. Wiola asked me to deliver these...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #172
        "\x07\x05Kloe handed Monika a printout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #173
        0x14,
        "#11POh, it's our credit list.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x14,
        (
            "#11PUgh... There're so many classes here... Being a \x01",
            "second year seems like it's gonna be rough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x14,
        (
            "#11PI'm surprised you went out your way to deliver\x01",
            "these. Not like there was any rush.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0x105,
        (
            "#044F#6PUmm...\x02\x03",

            "You really think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x14,
        (
            "#11PYeah. She forgot to hand them out last\x01",
            "year, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x14,
        (
            "#11PWe got them eventually, but it was, like,\x01",
            "foreeever after we should have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x14,
        (
            "#11PShe might be pretty, but she's kind of...\x01",
            "not all there, if you know what I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x14,
        "#11PYou might want to watch your back, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x14,
        (
            "#11PLike, you're obviously a nice girl,\x01",
            "so if you don't, she might end up\x01",
            "taking advantage of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x105,
        "#049F#6P...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    OP_4A(0x15, 255)
    SetChrPos(0x15, 25000, 0, 26000, 90)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4A9D():
        OP_8E(0xFE, 0x64C8, 0x0, 0x6590, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4A9D)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #183
        0x15,
        "#5PTHERE you are, Monika!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x15,
        "#5PYou do realize we can't start without you, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x14,
        "#11PWhoops! Sorry! I'm coming now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "#11PWell, see you later, Kloe. Thanks for delivering\x01",
            "that printout to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        "#045F#6POh... Not at all.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 400)

    def lambda_4BC3():
        OP_8E(0xFE, 0x61A8, 0x0, 0x6590, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4BC3)

    def lambda_4BDE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4BDE)

    def lambda_4BF0():
        OP_8E(0xFE, 0x75E4, 0x0, 0x639C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4BF0)
    WaitChrThread(0x14, 0x1)

    def lambda_4C10():
        OP_8E(0xFE, 0x61A8, 0x0, 0x639C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4C10)
    Sleep(1100)

    def lambda_4C30():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4C30)
    WaitChrThread(0x14, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #188
        0x105,
        (
            "#047F#5PBut...\x02\x03",

            "#042FBut I need to keep doing what I can!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_4CAF():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4CAF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #189
        (
            "\x18\x07\x0CMaybe I was desperate to cling on to something to\x01",
            "keep from losing sight of myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #190
        (
            "\x18\x07\x0CThe world made it seem like you could only broaden\x01",
            "your horizons by interacting with others, but there\x01",
            "I was, stubbornly refusing to come out of my shell.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #191
        (
            "\x18\x07\x0COr was it really stubbornness? In some weird way\x01",
            "I can't explain, it was more like obsessing over the\x01",
            "idea that I could grow as long as I pushed myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #192
        (
            "\x18\x07\x0CIt's not like I wanted to be left behind...\x01",
            "It's not like I wanted to be alone...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #193
        (
            "\x18\x07\x0CAs long as I tried hard enough, maybe I'd one day\x01",
            "stop feeling like I was always running in place...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_45BC end

    def Function_22_4F67(): pass

    label("Function_22_4F67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(3840, 0, 50680, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(58000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 2920, 0, 49940, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 4500, 0, 50100, 270)
    SetChrPos(0x11, 4500, 0, 50100, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)

    def lambda_5020():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5020)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    OP_C4(0x1, 0x800)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #194
        (
            "\x07\x05              [The Student Council]\x01",
            "An autonomous body run by students, for students,\x01",
            "responsible for maintaining order and overseeing \x01",
            "student activities.#11550W #20W \x01\x01",
            "And their most important duty of all...#4100W #20W \x01\x01",
            "#3S...is searching for their president!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)

    NpcTalk(    #195
        0x105,
        "Voice",
        "#3S#6PHe's not here, either!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x1E)

    def lambda_51BB():
        OP_6D(3460, 0, 51800, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_51BB)

    def lambda_51D3():
        OP_67(0, 4780, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_51D3)

    def lambda_51EB():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_51EB)

    def lambda_51FB():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_51FB)

    def lambda_520B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_520B)

    def lambda_521D():
        OP_8E(0xFE, 0x898, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_521D)
    WaitChrThread(0x10, 0x1)

    def lambda_523D():
        OP_8E(0xFE, 0x898, 0x0, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_523D)

    def lambda_5258():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5258)

    def lambda_526A():
        OP_8E(0xFE, 0x898, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_526A)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x10,
        (
            "#646F#5PWhere IS that ruffian?!\x02\x03",

            "#1891FI was sure he'd think he got us and come back\x01",
            "to the council room this time. SURE of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "#734F#12PI swear, every time we do manage to find him,\x01",
            "he gets a thousand times more capable of hiding\x01",
            "from us...\x02\x03",

            "#735FWhere could he be? We've searched the school\x01",
            "buildings, we've searched the dorms...\x02\x03",

            "#732FWhere's left? The shrubs on the grounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10,
        "#646F#5PUgh... He's just taunting us now!\x02",
    )

    CloseMessageWindow()

    def lambda_5478():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5478)
    Sleep(200)
    TurnDirection(0x11, 0x10, 500)
    Sleep(500)

    ChrTalk(    #199
        0x10,
        (
            "#1891F#5PGet it together, Hans!\x02\x03",

            "We're going to find him, and we are going\x01",
            "to force-feed him EVERY SINGLE PIECE OF\x01",
            "PAPERWORK he's got piling up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x11,
        "#732F#12PRight on!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 600)
    OP_43(0x10, 0x3, 0x0, 0x17)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0x17)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4F67 end

    def Function_23_557B(): pass

    label("Function_23_557B")


    def lambda_5581():
        OP_8E(0xFE, 0x898, 0x0, 0xC9F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5581)
    WaitChrThread(0xFE, 0x1)

    def lambda_55A1():
        OP_8E(0xFE, 0xC8, 0x0, 0xC9F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55A1)
    WaitChrThread(0xFE, 0x1)

    def lambda_55C1():
        OP_8E(0xFE, 0xC8, 0xFFFFF830, 0xB98C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55C1)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_23_557B end

    def Function_24_55DC(): pass

    label("Function_24_55DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #201
        (
            "\x07\x00#40WAfter that, Kloe decided to join the Fencing Club\x01",
            "so that the skills Julia taught her didn't grow rusty\x01",
            "during her time at the academy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #202
        (
            "\x07\x00#40WShe also found herself being roped into helping\x01",
            "Jill and Hans search for the nefarious Lechter\x01",
            "quite often, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #203
        "\x07\x00#40WThen, roughly a month after this all began...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #204
        (
            "\x07\x00#40W...everyone's favorite time of the academic year\x01",
            "finally arrived!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(31040, 0, 57300, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_4A(0x11, 255)
    OP_4A(0x16, 255)
    OP_4A(0x13, 255)
    SetChrFlags(0x12, 0x80)
    OP_63(0x12)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 28740, 250, 54300, 90)
    SetChrPos(0x16, 25000, 0, 56000, 90)
    SetChrPos(0x13, 25000, 0, 56000, 90)
    OP_1D(0x4B)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #205
        0x11,
        (
            "#732F#5PRight, so here I need to use this formula...\x02\x03",

            "#733FWait! This isn't right. What am I doing wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)

    def lambda_5917():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5917)

    def lambda_5929():
        OP_8E(0xFE, 0x6C5C, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5929)
    WaitChrThread(0x16, 0x1)
    OP_22(0x7, 0x0, 0x64)
    TurnDirection(0x16, 0x11, 400)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1800)

    ChrTalk(    #206
        0x16,
        (
            "#1776F#5PExam season, huh?\x02\x03",

            "#1771FStudents sure have it rough.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x4)

    def lambda_59BF():
        OP_8E(0xFE, 0x6C5C, 0x0, 0xE380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_59BF)
    WaitChrThread(0x16, 0x1)

    def lambda_59DF():
        OP_8E(0xFE, 0x7148, 0x0, 0xE380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_59DF)
    WaitChrThread(0x16, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrPos(0x16, 29840, 250, 58240, 180)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    OP_0D()
    SetChrSubChip(0x11, 1)
    OP_62(0x11, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0x11,
        (
            "#735F#12PYou're technically one, too, you know.\x01",
            "Technically.\x02\x03",

            "#732FYou ARE going to study, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x16,
        (
            "#1776F#5PWell...\x02\x03",

            "#1775FWeeeeeell...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0x11,
        "#734F#12P(I'll take that as a no.)\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)

    def lambda_5B2F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5B2F)

    def lambda_5B41():
        OP_8E(0xFE, 0x69A0, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5B41)
    Sleep(500)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x16, 400)
    Sleep(300)

    ChrTalk(    #210
        0x13,
        "#1792F#6POh, HERE you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x11,
        "#738F#11P(An angel shines her majesty upon us!)\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    SetChrFlags(0x13, 0x4)

    def lambda_5BE3():
        OP_8E(0xFE, 0x6D88, 0x0, 0xE36C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5BE3)
    WaitChrThread(0x13, 0x1)

    def lambda_5C03():
        OP_8E(0xFE, 0x7044, 0x0, 0xE36C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5C03)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #212
        0x13,
        (
            "#1794F#6PCome on, Lechter. It's time for you to hit those\x01",
            "books!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x16,
        (
            "#1772F#5PB-But I've studied for a whole half-second today\x01",
            "already! I really don't think...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CC9():
        OP_8F(0xFE, 0x729C, 0x0, 0xE36C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5CC9)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_5CEE():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_5CEE)
    OP_62(0x16, 0xAA, 1650, 0x28, 0x2B, 0x82, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x16, 0x20)
    OP_0D()
    OP_8C(0x13, 270, 400)
    OP_43(0x16, 0x3, 0x0, 0x19)

    def lambda_5D38():
        OP_8E(0xFE, 0x6C34, 0x0, 0xE36C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5D38)
    WaitChrThread(0x13, 0x1)

    def lambda_5D58():
        OP_8E(0xFE, 0x6C34, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5D58)
    WaitChrThread(0x13, 0x1)

    def lambda_5D78():
        OP_8E(0xFE, 0x61A8, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5D78)
    Sleep(1000)

    def lambda_5D98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5D98)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x16, 0x3)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x11, 0x2)
    Sleep(1000)

    ChrTalk(    #214
        0x11,
        (
            "#735F#11POh, Lucy...\x02\x03",

            "#737FWhy can't I get you to do that to me? ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #215
        0x11,
        (
            "#733F#5PWait, no! This is no time for fantasizing!\x02\x03",

            "#735FI need to study!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E97():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5E97)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearChrFlags(0x105, 0x8)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_55DC end

    def Function_25_5EC8(): pass

    label("Function_25_5EC8")


    def lambda_5ECE():
        OP_8F(0xFE, 0x6C34, 0x0, 0xE36C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5ECE)
    Sleep(300)
    Fade(250)
    OP_8C(0x16, 270, 0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x16, 26)
    SetChrSubChip(0x16, 0)
    WaitChrThread(0x16, 0x1)

    def lambda_5F0E():
        OP_8C(0xFE, 180, 1000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5F0E)

    def lambda_5F1C():
        OP_8F(0xFE, 0x6C34, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5F1C)
    WaitChrThread(0x16, 0x1)

    def lambda_5F3C():
        OP_8C(0xFE, 270, 1000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5F3C)

    def lambda_5F4A():
        OP_8F(0xFE, 0x61A8, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5F4A)
    Sleep(1000)

    def lambda_5F6A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5F6A)
    WaitChrThread(0x16, 0x1)
    Return()

    # Function_25_5EC8 end

    def Function_26_5F7C(): pass

    label("Function_26_5F7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(31040, 0, 57300, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, 29840, 250, 58240, 180)
    SetChrChipByIndex(0x12, 24)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 28740, 250, 56300, 90)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 30860, 250, 56080, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 25000, 0, 56000, 90)
    SetChrPos(0x11, 25000, 0, 56000, 90)
    SetChrPos(0x105, 25000, 0, 56000, 90)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x16, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_63(0x12)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x105, 0x3, 0x0, 0x1D)
    WaitChrThread(0x105, 0x3)

    ChrTalk(    #216
        0x10,
        (
            "#641F#6PYo, guys.\x02\x03",

            "#643FWhoa. Lechter's HERE? What's the occasion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x16,
        (
            "#1772F#5PHey! You say that as if I'm never here!\x02\x03",

            "I'm always here doing nothing, aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x105,
        "#045F#6P(At least he's being honest about it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x11,
        "#738F#6PLucy! I'm so happy to see you again! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x13,
        (
            "#1791F#11PYou're looking well, Hans.\x02\x03",

            "How did your exams go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x11,
        (
            "#738F#6PAhaha... Well...\x02\x03",

            "#737FI'd appreciate if we avoided that fine subject. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10,
        (
            "#649F#5PMuch like how you avoided all the subjects\x01",
            "you were supposed to study, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x12,
        (
            "#1782F#5PCan you stop wasting time and take your seats?\x01",
            "We have work to do.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("First Years")

    AnonymousTalk(    #224
        "\x07\x00#3SS-Sorry!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x105, 0x3, 0x0, 0x20)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x1F)
    Sleep(200)
    OP_43(0x10, 0x3, 0x0, 0x1E)
    WaitChrThread(0x105, 0x3)
    Sleep(500)

    ChrTalk(    #225
        0x12,
        (
            "#1780F#6PWell, we're all here, so let's get started.\x02\x03",

            "#1782FAll right. Our first order of the day is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x16,
        (
            "#1777F#5P...talking about everyone's dreams for the future!\x02\x03",

            "#1771FYou three can go first! Speak of your highest\x01",
            "aspirations so that we all might hear!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 30860, 0, 56800, 270)
    OP_0D()
    OP_8C(0x13, 0, 500)

    def lambda_6509():
        OP_8E(0xFE, 0x788C, 0x0, 0xE2F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6509)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    def lambda_6535():
        OP_8F(0xFE, 0x76E8, 0x0, 0xE2F4, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6535)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_62(0x16, 0xAA, 1650, 0x28, 0x2B, 0x82, 0x2)

    def lambda_656C():
        OP_9E(0xFE, 0xF, 0xF, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_656C)

    def lambda_6586():
        OP_8F(0xFE, 0x788C, 0x0, 0xE2F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6586)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x13, 180, 500)

    def lambda_6606():
        OP_8E(0xFE, 0x788C, 0x0, 0xDDE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6606)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 30860, 250, 56080, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #227
        0x13,
        "#1794F#11PPlease continue, Leo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x12,
        (
            "#1782F#6PFirst, I will go over the Student Council's main\x01",
            "orders of business for the year.\x02\x03",

            "#1780FAfter that, I will discuss our future activities\x01",
            "in more detail, and then we can start to work\x01",
            "on allocating the budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x16,
        (
            "#1778F#5PJill! You spill first!\x02\x03",

            "#1778FTell us what desires burn within that pure,\x01",
            "sisterly heart of yours!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 1)
    Sleep(300)

    ChrTalk(    #230
        0x10,
        "#1891F#6P#3SThe desire to topple your presidency!#2S\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #231
        0x16,
        "#1773F#5P#3S*dramatic gasp*!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #232
        0x12,
        (
            "#1782F#6PAs you can see, this fool will be of no use at all to\x01",
            "the proceedings. Expect diddly squat from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x105,
        "#045F#11P(Oh, Lechter...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x11,
        (
            "#734F#6P(When he's not here, he causes trouble...\x01",
            "and when he's here, he causes...trouble.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #235
        0x12,
        (
            "#1780F#6PSo, moving along. If we go by our usual pattern\x01",
            "for the year, next month will be...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69E1():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_69E1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_26_5F7C end

    def Function_27_6A13(): pass

    label("Function_27_6A13")


    def lambda_6A19():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6A19)

    def lambda_6A2B():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6A2B)
    WaitChrThread(0x10, 0x1)

    def lambda_6A4B():
        OP_8E(0xFE, 0x6B44, 0x0, 0xDC8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6A4B)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Return()

    # Function_27_6A13 end

    def Function_28_6A6D(): pass

    label("Function_28_6A6D")


    def lambda_6A73():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6A73)

    def lambda_6A85():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A85)
    WaitChrThread(0x11, 0x1)

    def lambda_6AA5():
        OP_8E(0xFE, 0x6B94, 0x0, 0xD8A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6AA5)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 90, 400)
    Return()

    # Function_28_6A6D end

    def Function_29_6AC7(): pass

    label("Function_29_6AC7")


    def lambda_6ACD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6ACD)

    def lambda_6ADF():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6ADF)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)

    def lambda_6B04():
        OP_8E(0xFE, 0x6978, 0x0, 0xD2C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B04)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 45, 400)
    Return()

    # Function_29_6AC7 end

    def Function_30_6B26(): pass

    label("Function_30_6B26")

    SetChrFlags(0x10, 0x4)

    def lambda_6B31():
        OP_8E(0xFE, 0x6CFC, 0x0, 0xD7A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B31)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 21)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 28740, 250, 55300, 90)
    OP_0D()
    Return()

    # Function_30_6B26 end

    def Function_31_6B7E(): pass

    label("Function_31_6B7E")

    SetChrFlags(0x11, 0x4)

    def lambda_6B89():
        OP_8E(0xFE, 0x6CFC, 0x0, 0xD354, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B89)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 28740, 250, 54300, 90)
    OP_0D()
    Return()

    # Function_31_6B7E end

    def Function_32_6BD6(): pass

    label("Function_32_6BD6")

    SetChrFlags(0x105, 0x4)

    def lambda_6BE1():
        OP_8E(0xFE, 0x6E00, 0x0, 0xCF1C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6BE1)
    WaitChrThread(0x105, 0x1)

    def lambda_6C01():
        OP_8E(0xFE, 0x788C, 0x0, 0xCF1C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C01)
    WaitChrThread(0x105, 0x1)

    def lambda_6C21():
        OP_8E(0xFE, 0x788C, 0x0, 0xD2B4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C21)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x105, 23)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x105, 30860, 250, 54700, 270)
    OP_0D()
    Return()

    # Function_32_6BD6 end

    def Function_33_6C6E(): pass

    label("Function_33_6C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_6DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_6D08")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Climb Up\x01",         # 0
            "Don't Climb\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D05")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CEE")
    OP_A2(0x2505)
    Jump("loc_6CF9")

    label("loc_6CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF9")
    OP_A2(0x2506)

    label("loc_6CF9")

    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_6D05")

    label("loc_6D05")

    Jump("loc_6DCD")

    label("loc_6D08")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #236
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x105,
        (
            "#044FHmm? What's this?\x02\x03",

            "Are you supposed to climb up using this?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_6DCD")

    Jump("loc_72E7")

    label("loc_6DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_6EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_6DF5")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2800   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_6EA1")

    label("loc_6DF5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #238
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #239
        0x105,
        (
            "#047F...\x02\x03",

            "#040FLooks like I can use this to climb up onto the\x01",
            "roof.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_6EA1")

    Jump("loc_72E7")

    label("loc_6EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_7001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_6F22")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Climb Up\x01",         # 0
            "Don't Climb\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1F")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_6F1F")

    label("loc_6F1F")

    Jump("loc_6FFE")

    label("loc_6F22")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #240
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #241
        0x105,
        (
            "#044FHmm? What's this?\x02\x03",

            "#042FIs it meant to be some way to climb up on top of\x01",
            "the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_6FFE")

    Jump("loc_72E7")

    label("loc_7001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_71CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_707F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Climb Up\x01",         # 0
            "Don't Climb\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_707C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_707C")

    label("loc_707C")

    Jump("loc_71CA")

    label("loc_707F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #242
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #243
        0x105,
        (
            "#044FHmm? A rope?\x02\x03",

            "I wonder what it's here for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x152,
        "#734FOh, this is Lechter's handiwork.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x13B,
        (
            "#645FHe loves to use it to climb up onto the roof.\x02\x03",

            "Aidios knows how he first conjured that idea up...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_71CA")

    Jump("loc_72E7")

    label("loc_71CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_72E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_723E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #246
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_72E7")

    label("loc_723E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #247
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #248
        0x105,
        "#044F(I wonder what this is for...?)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_72E7")

    TalkEnd(0xFF)
    Return()

    # Function_33_6C6E end

    def Function_34_72EB(): pass

    label("Function_34_72EB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25010, 0, 55900, 90)

    def lambda_7312():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7312)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x6C66, 0x0, 0xDA84, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_34_72EB end

    def Function_35_7351(): pass

    label("Function_35_7351")

    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0x6892, 0x0, 0xDA52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6892, 0x0, 0xDA52, 0x7D0, 0x0)

    def lambda_738B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_738B)
    OP_8E(0xFE, 0x61A8, 0x0, 0xDB06, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_35_7351 end

    def Function_36_73BB(): pass

    label("Function_36_73BB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25010, 0, 55900, 90)

    def lambda_73E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73E2)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x6C66, 0x0, 0xDA84, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_36_73BB end

    def Function_37_7421(): pass

    label("Function_37_7421")

    OP_82(0x82, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #249
        "\x07\x05Found \x1F\x5A\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x8, 0x1)
    OP_3E(0x35A, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_37_7421 end

    def Function_38_747A(): pass

    label("Function_38_747A")

    EventBegin(0x2)
    OP_8C(0x105, 90, 500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #250
        0x105,
        (
            "#047F(It looks like someone's getting changed.)\x02\x03",

            "#040F(I should come back later.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrPos(0x105, 1200, 0, 42000, 270)
    OP_6D(1200, 0, 42000, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    EventEnd(0x4)
    Return()

    # Function_38_747A end

    def Function_39_7555(): pass

    label("Function_39_7555")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #251
        "\x07\x05Currently changing\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #252
        0x105,
        (
            "#047F(I can't go inside right now.)\x02\x03",

            "#040F(I should come back later.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_39_7555 end

    def Function_40_75E7(): pass

    label("Function_40_75E7")

    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #253
        0x105,
        (
            "#047F(It looks like someone's getting changed.)\x02\x03",

            "#040F(I should come back later.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    TalkEnd(0xFF)
    Return()

    # Function_40_75E7 end

    SaveToFile()

Try(main)
