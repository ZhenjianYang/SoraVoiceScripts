from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0312   ._SN',
        MapName             = 'Event',
        Location            = 'E0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0312   ._SN',
            'ED6_DT21/E0312_1 ._SN',
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
        'Professor Russell',                    # 9
        'Scherazard',                           # 10
        'Agate',                                # 11
        'Tita',                                 # 12
        'Zin',                                  # 13
        'Father Kevin',                         # 14
        'Josette',                              # 15
        'Hugo',                                 # 16
        'Louise',                               # 17
        'Royal Guardsman',                      # 18
        'Royal Guardsman',                      # 19
        'Ray',                                  # 20
        'Clive',                                # 21
        'Mechanic Payton',                      # 22
        'Faye',                                 # 23
        'Antoine',                              # 24
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT07/CH01320 ._CH',             # 09
        'ED6_DT07/CH01220 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01550 ._CH',             # 0C
        'ED6_DT07/CH01700 ._CH',             # 0D
        'ED6_DT07/CH00170 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT07/CH01320P._CP',             # 09
        'ED6_DT07/CH01220P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01550P._CP',             # 0C
        'ED6_DT07/CH01700P._CP',             # 0D
        'ED6_DT07/CH00170P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 360,
        Z                   = 0,
        Y                   = 63980,
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
        X                   = -5140,
        Z                   = 0,
        Y                   = 65400,
        Direction           = 0,
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
        X                   = -2670,
        Z                   = 0,
        Y                   = 5340,
        Direction           = 180,
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
        X                   = -2680,
        Z                   = 0,
        Y                   = 5370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -5340,
        Z                   = 0,
        Y                   = 60180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -5340,
        Z                   = 0,
        Y                   = 58780,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -30,
        Z                   = 0,
        Y                   = 60960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 400,
        Z                   = 0,
        Y                   = 63980,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -6120,
        Z                   = 0,
        Y                   = 62560,
        Direction           = 233,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclEvent(
        X                   = -2680,
        Y                   = -1000,
        Z                   = 5370,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 42,
    )


    DeclActor(
        TriggerX            = -5110,
        TriggerZ            = 0,
        TriggerY            = 65500,
        TriggerRange        = 400,
        ActorX              = -5410,
        ActorZ              = 1500,
        ActorY              = 65800,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2980,
        TriggerZ            = 0,
        TriggerY            = 66830,
        TriggerRange        = 800,
        ActorX              = -2980,
        ActorZ              = 1000,
        ActorY              = 66830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = 0,
        TriggerY            = -36460,
        TriggerRange        = 1200,
        ActorX              = 60000,
        ActorZ              = 2080,
        ActorY              = -36230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2370,
        TriggerZ            = 0,
        TriggerY            = 60960,
        TriggerRange        = 800,
        ActorX              = -30,
        ActorZ              = 1500,
        ActorY              = 60960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 62910,
        TriggerZ            = 0,
        TriggerY            = 4740,
        TriggerRange        = 1200,
        ActorX              = 62910,
        ActorZ              = 800,
        ActorY              = 4740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F6",          # 00, 0
        "Function_1_897",          # 01, 1
        "Function_2_A7E",          # 02, 2
        "Function_3_BFB",          # 03, 3
        "Function_4_C1F",          # 04, 4
        "Function_5_2E8C",         # 05, 5
        "Function_6_31C3",         # 06, 6
        "Function_7_3505",         # 07, 7
        "Function_8_5600",         # 08, 8
        "Function_9_5D3F",         # 09, 9
        "Function_10_7602",        # 0A, 10
        "Function_11_7A8A",        # 0B, 11
        "Function_12_7D31",        # 0C, 12
        "Function_13_7E77",        # 0D, 13
        "Function_14_801E",        # 0E, 14
        "Function_15_818E",        # 0F, 15
        "Function_16_8FEC",        # 10, 16
        "Function_17_94B2",        # 11, 17
        "Function_18_98C8",        # 12, 18
        "Function_19_A7C0",        # 13, 19
        "Function_20_A885",        # 14, 20
        "Function_21_AB8E",        # 15, 21
        "Function_22_AEF9",        # 16, 22
        "Function_23_B29D",        # 17, 23
        "Function_24_B3CC",        # 18, 24
        "Function_25_B45C",        # 19, 25
        "Function_26_B4E9",        # 1A, 26
        "Function_27_BD07",        # 1B, 27
        "Function_28_BD34",        # 1C, 28
        "Function_29_BD73",        # 1D, 29
        "Function_30_BDB2",        # 1E, 30
        "Function_31_BDF1",        # 1F, 31
        "Function_32_BE30",        # 20, 32
        "Function_33_BE5E",        # 21, 33
        "Function_34_BE7A",        # 22, 34
        "Function_35_BE96",        # 23, 35
        "Function_36_BEB2",        # 24, 36
        "Function_37_C7AE",        # 25, 37
        "Function_38_CD79",        # 26, 38
        "Function_39_D46A",        # 27, 39
        "Function_40_D4B9",        # 28, 40
        "Function_41_D55B",        # 29, 41
        "Function_42_D560",        # 2A, 42
    )


    def Function_0_3F6(): pass

    label("Function_0_3F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_89(0x0, 2980, 1200, 4200, 180)

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43D")
    SetChrPos(0xB, -2830, 0, 65940, 90)
    ClearChrFlags(0xB, 0x80)

    label("loc_43D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_460")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_460")

    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A6")
    SetChrPos(0x9, -5340, 0, 59510, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_4A6")

    Jump("loc_5B6")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5B6")

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_547")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50B")
    SetChrPos(0xB, -3510, 0, 5330, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_52E")

    SetChrPos(0x12, 63010, 0, -39310, 270)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5B6")

    label("loc_547")

    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56F")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_56F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A0")
    OP_44(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 15)
    SetChrPos(0xA, 61300, 250, -40950, 0)

    label("loc_5A0")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_5B6")

    Jump("loc_877")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_5FC")

    label("loc_5E6")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_5FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61F")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_61F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_642")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_642")

    SetChrPos(0x13, -6370, 0, 61080, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -5350, 0, 59530, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_877")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AD")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_6C3")

    label("loc_6AD")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_6C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E6")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_6E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_709")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_709")

    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_877")

    label("loc_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_7A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_759")

    label("loc_743")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_759")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77C")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_77C")

    SetChrPos(0x14, -6310, 0, 61050, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_877")

    label("loc_7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_823")
    SetChrPos(0x8, -6370, 0, 61080, 180)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E4")
    SetChrPos(0xB, -4420, 0, 62290, 225)
    ClearChrFlags(0xB, 0x80)

    label("loc_7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_807")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_807")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_877")

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_83C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_877")

    label("loc_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_877")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    SetChrPos(0xC, 62250, 0, -39280, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)

    label("loc_877")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_883"),
        (SWITCH_DEFAULT, "loc_896"),
    )


    label("loc_883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_893")
    Event(0, 26)

    label("loc_893")

    Jump("loc_896")

    label("loc_896")

    Return()

    # Function_0_3F6 end

    def Function_1_897(): pass

    label("Function_1_897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_8D9")
    OP_B1("E0312_1")
    Jump("loc_8E2")

    label("loc_8D9")

    OP_B1("E0312_2")

    label("loc_8E2")

    Jump("loc_906")

    label("loc_8E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_B1("E0312_2")
    Jump("loc_906")

    label("loc_8FD")

    OP_B1("E0312_1")

    label("loc_906")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92F")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93C")

    label("loc_92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93C")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_93C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_967")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_967")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_988")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_997")
    OP_72(0x5, 0x4)
    Jump("loc_9D5")

    label("loc_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AF")
    OP_64(0x0, 0x1)
    OP_72(0x5, 0x4)
    Jump("loc_9D5")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_9C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BE")

    label("loc_9BE")

    OP_72(0x5, 0x4)
    Jump("loc_9D5")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_9D5")
    OP_64(0x0, 0x1)
    OP_64(0x3, 0x1)

    label("loc_9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E7")
    Jump("loc_A19")

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F2")
    Jump("loc_A19")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_A19")

    label("loc_9FD")

    OP_D2(0x70053, 0x7005B, 0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A19")
    SetChrChipByIndex(0xA, 15)

    label("loc_A19")

    Jump("loc_A7D")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_A30")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A7D")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_A44")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A7D")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_A58")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A7D")

    label("loc_A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_A6C")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A7D")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_A76")
    Jump("loc_A7D")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_A7D")

    label("loc_A7D")

    Return()

    # Function_1_897 end

    def Function_2_A7E(): pass

    label("Function_2_A7E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BE5")

    label("loc_AA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BE5")

    label("loc_ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BE5")

    label("loc_AD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BE5")

    label("loc_AEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B07")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BE5")

    label("loc_B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BE5")

    label("loc_B20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B39")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BE5")

    label("loc_B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B52")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BE5")

    label("loc_B52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BE5")

    label("loc_B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BE5")

    label("loc_B84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BE5")

    label("loc_B9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BE5")

    label("loc_BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BE5")

    label("loc_BCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BE5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BE5")

    label("loc_BFA")

    Return()

    # Function_2_A7E end

    def Function_3_BFB(): pass

    label("Function_3_BFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1E")
    OP_8D(0xFE, -7430, 62910, -5150, 62070, 1000)
    Jump("Function_3_BFB")

    label("loc_C1E")

    Return()

    # Function_3_BFB end

    def Function_4_C1F(): pass

    label("Function_4_C1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")
    Call(0, 36)
    TalkEnd(0xFE)
    Return()

    label("loc_C48")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",               # 0
            "Make a Weapon\x01",      # 1
            "Do Nothing\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E96")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "#100FMaking a weapon?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(    #1
        "\x06\x18\x07\x05Which weapon do you wish to make?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        330,
        50,
        0,
        (
            "Qilin Horn - Staff\x01",                # 0
            "Phoenix Blades - Dual blades\x01",      # 1
            "Sirius Whip - Whip\x01",                # 2
            "Eternity - Pistol\x01",                 # 3
            "Moon Singer - Rapier\x01",              # 4
            "Demon Eater - Greatsword\x01",          # 5
            "Kowloon - Cannon\x01",                  # 6
            "Avalokiteshvara - Gauntlets\x01",       # 7
            "Glittering Stars - Crossbow\x01",       # 8
            "Quit\x01",                              # 9
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    label("loc_E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA7")
    TalkEnd(0xFE)
    Return()

    label("loc_EA7")

    FadeToBright(300, 0)

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(    #2
        0x8,
        (
            "#100FHeh heh! Thanks for giving this old\x01",
            "man a chance to horse around like\x01",
            "this.\x02\x03",

            "How many men can claim to have\x01",
            "worked with ancient Zemurian metals?\x02\x03",

            "I'll keep these notes in mind for more\x01",
            "research later!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E88")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA0")
    Call(0, 22)
    Jump("loc_2E88")

    label("loc_FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_END)), "loc_2B0D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3FE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x400, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x401, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x402, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x403, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x404, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x405, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x406, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x407, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1041")
    Call(0, 23)
    Jump("loc_2B0A")

    label("loc_1041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D0")

    ChrTalk(    #3
        0x8,
        (
            "#100FWe're about to begin the final tests of\x01",
            "the flight engine.\x02\x03",

            "If the engine passes, we'll have basic\x01",
            "flight capability.\x02\x03",

            "#104FOf course, if we can recover the\x01",
            "left outrigger, that would be best...\x02\x03",

            "#100F...but I want to proceed on the\x01",
            "assumption we'll have to make do\x01",
            "without.\x02\x03",

            "I'll have us ready to be airborne by the\x01",
            "time you return from the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1225")

    ChrTalk(    #4
        0x10F,
        (
            "#179FWe'll be counting on you,\x01",
            "Professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#100FHo ho! You just leave it to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12CA")

    label("loc_1225")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126F")

    ChrTalk(    #6
        0x8,
        (
            "#100FYou just take care of Tita, and\x01",
            "return safely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CA")

    label("loc_126F")


    ChrTalk(    #7
        0x8,
        (
            "#100FTake care of yourselves, you hear?\x01",
            "We've come too far for tragedy to\x01",
            "strike now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CA")

    OP_A2(0x3)
    Jump("loc_1380")

    label("loc_12D0")


    ChrTalk(    #8
        0xFE,
        (
            "#100FI'll have us ready to fly by the time\x01",
            "you get back from the Axis Pillar.\x02\x03",

            "So you kids return safe and sound,\x01",
            "all right? We've come too far for\x01",
            "tragedy to strike now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1380")

    Jump("loc_2B0A")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AD")

    ChrTalk(    #9
        0x8,
        (
            "#104FIt's quite possible the outrigger is\x01",
            "unsalvageable.\x02\x03",

            "#100FIf that ends up being the case, we'll\x01",
            "simply take the flight engine from it\x01",
            "and mount it inside the Arseille.\x02\x03",

            "It won't be optimal, but the flight field\x01",
            "should be balanced enough to get us\x01",
            "airborne, at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1520")

    label("loc_14AD")


    ChrTalk(    #10
        0x8,
        (
            "#100FIt's quite possible the outrigger\x01",
            "is unsalvageable.\x02\x03",

            "I'm working on some alternative\x01",
            "plans just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1520")

    Jump("loc_2B0A")

    label("loc_1523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_196E")

    ChrTalk(    #11
        0x8,
        (
            "#100FHello, everyone!\x02\x03",

            "How goes it? Did you find\x01",
            "anything interesting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015FI'm not so sure about 'interesting'...\x02\x03",

            "We found something pretty weird,\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #13
        0x8,
        "#103FOh? What did you find?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1035FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Estelle explained about finding a Gospel-issuing terminal,\x01",
            "and that it was asking for a citizen's name.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #16
        0x8,
        (
            "#104FI see, I see...\x02\x03",

            "#100FSo you need a citizen's name on\x01",
            "record to be issued a Gospel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1003FYeah, that's about the size of it.\x02\x03",

            "#1007FLong shot, but you wouldn't happen to\x01",
            "know the names of a bunch of folks\x01",
            "from an ancient civilization, would you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #18
        0x8,
        (
            "#104FOf course not! Contrary to popular\x01",
            "belief, I'm not THAT old.\x02\x03",

            "#102FHowever, those data crystals have\x01",
            "records on them, among other things.\x02\x03",

            "If you check the data Capel has\x01",
            "decrypted, you may be able to fish\x01",
            "out a name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1044FThat's true. The data on those\x01",
            "crystals WERE presumably written\x01",
            "by a citizen of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1015FThe data crystals, huh?\x02\x03",

            "Well, not like we have any other clues.\x01",
            "Let's go take a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_A2(0x22D2)
    Jump("loc_2B0A")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_2045")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_1ACE")

    ChrTalk(    #21
        0x8,
        (
            "#100FThe data crystals have records on\x01",
            "them, among other things.\x02\x03",

            "If you check the data Capel has\x01",
            "decrypted, you may be able to fish\x01",
            "out a name.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x14)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x10B, 400)
    Sleep(400)

    ChrTalk(    #22
        0x8,
        (
            "#103FWhy, if it isn't...\x02\x03",

            "#101FThe bandit lass! It's been some time!\x02\x03",

            "Ever since we met beneath\x01",
            "Leiston Fortress, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B3D")

    label("loc_1ACE")

    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #23
        0x8,
        (
            "#101FThe bandit lass! It's been some time!\x02\x03",

            "Ever since we met beneath\x01",
            "Leiston Fortress, I believe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1BC5")

    ChrTalk(    #24
        0x10B,
        (
            "#214FB-Bandit lass?! Enough with the weird\x01",
            "nicknames, you old coot!\x02\x03",

            "#413FLike granddaughter, like grandfather,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0E")

    label("loc_1BC5")


    ChrTalk(    #25
        0x10B,
        (
            "#214FB-Bandit lass?! Enough with the weird\x01",
            "nicknames, you old coot!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0E")


    ChrTalk(    #26
        0x8,
        (
            "#100FOh, let me indulge a little.\x02\x03",

            "More to the point, I understand your\x01",
            "vessel's crashed here as well?\x02\x03",

            "I'm not completely familiar with Reinford's\x01",
            "orbal engines, but I believe I can offer\x01",
            "you some advice on repairs, if you'd like.\x02\x03",

            "Don't be shy about asking if you or your\x01",
            "brothers hit any trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10B,
        "#213FUm, thanks. We'll do that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22C2)
    Jump("loc_1E1F")

    label("loc_1D6A")

    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #28
        0x8,
        (
            "#100FI understand your vessel's crashed here\x01",
            "as well?\x02\x03",

            "Don't be shy about asking if you or your\x01",
            "brothers hit any trouble. I can offer some\x01",
            "advice on repairs, I believe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1F")

    Jump("loc_2042")

    label("loc_1E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_1EC2")

    ChrTalk(    #29
        0x8,
        (
            "#100FThe data crystals have records on them,\x01",
            "among other things.\x02\x03",

            "If you check the data Capel has decrypted,\x01",
            "you may be able to fish out a name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2042")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F96")

    ChrTalk(    #30
        0x8,
        (
            "#100FAh, everyone! I heard you saved that\x01",
            "bandit lass.\x02\x03",

            "I wouldn't mind getting my hands dirty\x01",
            "with that Reinford-built Imperial airship.\x02\x03",

            "#104FI'll have to make time to talk to\x01",
            "her in person.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2042")

    label("loc_1F96")


    ChrTalk(    #31
        0x8,
        (
            "#100FThere's quite a few things I don't know\x01",
            "about the airships Erebonia's Reinford\x01",
            "Company makes.\x02\x03",

            "I'll have to find the time to ask that\x01",
            "bandit lass some questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2042")

    Jump("loc_2B0A")

    label("loc_2045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_233F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A5")

    ChrTalk(    #32
        0x8,
        (
            "#100FThe main engine's orbments are repaired,\x01",
            "but for safety's sake it's still on low output.\x02\x03",

            "Once we make sure it won't throw any\x01",
            "more fits, we'll fire it up to full output.\x02\x03",

            "I'm afraid we'll be running on emergency\x01",
            "lights for a bit longer. Try to put up with it\x01",
            "and keep working, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1040FUnderstood. We'll do the best we can,\x01",
            "Professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1015FYeah, gotta do our best.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_223C")

    ChrTalk(    #35
        0x8,
        (
            "#100FBe off, then, and take care.\x02\x03",

            "And keep an eye on Tita, would you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_229F")

    label("loc_223C")


    ChrTalk(    #36
        0x8,
        (
            "#100FBe off, then, and take care.\x02\x03",

            "If you find anything interesting,\x01",
            "let me know immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229F")

    OP_A2(0x22C1)
    Jump("loc_233C")

    label("loc_22A5")


    ChrTalk(    #37
        0x8,
        (
            "#100FWe're still keeping an eye on the\x01",
            "main engine.\x02\x03",

            "If there's no problem, we'll start increasing\x01",
            "the output--beginning with the blasted\x01",
            "lights!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233C")

    Jump("loc_2B0A")

    label("loc_233F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_25F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2355")
    Call(0, 5)
    Jump("loc_25ED")

    label("loc_2355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_243E")

    ChrTalk(    #38
        0x8,
        (
            "#100FI'll be continuing work on this equipment\x01",
            "for a while yet.\x02\x03",

            "If you need weapons or quartz refining,\x01",
            "speak with Payton over there.\x02\x03",

            "He brought the run of the finest\x01",
            "orbal-tuning equipment from the central\x01",
            "factory!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25ED")

    label("loc_243E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254D")

    ChrTalk(    #39
        0x8,
        (
            "#100FI'm just a step away from finishing a test\x01",
            "version of that equipment I mentioned.\x02\x03",

            "I'll have it ready in some fashion once you\x01",
            "return from the tower.\x02\x03",

            "#101FAnd let me tell you, I'm glad I slid under this\x01",
            "wire! It looks like we'll make it in time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_25ED")

    label("loc_254D")


    ChrTalk(    #40
        0x8,
        (
            "#100FI'm just a step away from finishing a test\x01",
            "version of that equipment I mentioned.\x02\x03",

            "I'll have it ready in some fashion once you\x01",
            "return from the tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25ED")

    Jump("loc_2B0A")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_28A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2606")
    Call(0, 5)
    Jump("loc_28A6")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2788")

    ChrTalk(    #41
        0x8,
        (
            "#100FI'm afraid we still know very little about\x01",
            "that barrier engulfing the tops of the\x01",
            "towers.\x02\x03",

            "If we could make some progress deciphering\x01",
            "that data crystal, we might get a clue...\x02\x03",

            "For now, I'm going to focus on getting some\x01",
            "practical use out of that idea of mine.\x02\x03",

            "Let me say, between the 'shadow' towers and\x01",
            "these barriers, I'm not lacking for things\x01",
            "to research!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_28A6")

    label("loc_2788")


    ChrTalk(    #42
        0x8,
        (
            "#100FLet me say, between the 'shadow' towers\x01",
            "and these barriers, I'm not lacking for\x01",
            "things to research!\x02\x03",

            "#104FTo be honest, I've half a mind to go out\x01",
            "there myself and have a good look at these\x01",
            "phenomena in person, but these days...\x02\x03",

            "#102FTch! If I was ten years younger, even...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A6")

    Jump("loc_2B0A")

    label("loc_28A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_2B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BF")
    Call(0, 5)
    Jump("loc_2B0A")

    label("loc_28BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29B4")

    ChrTalk(    #43
        0x8,
        (
            "#100FI'll be continuing work on this equipment\x01",
            "for a while yet.\x02\x03",

            "If you need weapons or quartz refining,\x01",
            "speak with Payton over there.\x02\x03",

            "I think you'll find having third-level\x01",
            "slots prepared for your orbments\x01",
            "well worth your time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B0A")

    label("loc_29B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A68")

    ChrTalk(    #44
        0x8,
        (
            "#100FI'll be leaving the deciphering of the\x01",
            "data crystal to Capel.\x02\x03",

            "Not only are there four towers to examine,\x01",
            "but I've got a little something extra to work on.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B0A")

    label("loc_2A68")


    ChrTalk(    #45
        0x8,
        (
            "#100FIf you find any other data crystals,\x01",
            "bring them to me.\x02\x03",

            "I'll set them into Capel and put the automatic\x01",
            "deciphering program to work on them immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0A")

    Jump("loc_2E88")

    label("loc_2B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA8")

    ChrTalk(    #46
        0x8,
        (
            "#100FAh, everyone.\x02\x03",

            "Looking to have your orbments tuned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1011FYeah, we are, but...\x02\x03",

            "Why's everyone gathered here, Professor?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #48
        0x8,
        (
            "#100FAh, I was getting an opinion or two.\x02\x03",

            "To be honest, I found a base for...\x01",
            "a certain piece of equipment I'm\x01",
            "developing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C60")

    ChrTalk(    #49
        0x107,
        "#064FA 'certain piece of equipment'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C88")

    label("loc_2C60")


    ChrTalk(    #50
        0x102,
        "#1044FA 'certain piece' of... Hmm.\x02",
    )

    CloseMessageWindow()

    label("loc_2C88")


    ChrTalk(    #51
        0x101,
        (
            "#1015FWell, when you put it like THAT,\x01",
            "I've gotta know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#104FI'm sorry, but I can't speak more of it\x01",
            "just yet.\x02\x03",

            "It's quite possible nothing will come\x01",
            "of it and I'm just a stubborn old fool.\x02\x03",

            "#101FFor now, look forward to getting something\x01",
            "new soon...and wish me luck, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E29)
    Jump("loc_2E88")

    label("loc_2DA8")


    ChrTalk(    #53
        0x8,
        (
            "#100FI'll be continuing work on this equipment\x01",
            "for a while yet.\x02\x03",

            "If you need weapons or quartz refining,\x01",
            "speak with Payton over there.\x02\x03",

            "He brought the run of the finest orbal-\x01",
            "tuning equipment from the central\x01",
            "factory!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E88")

    TalkEnd(0xFE)
    Return()

    # Function_4_C1F end

    def Function_5_2E8C(): pass

    label("Function_5_2E8C")


    ChrTalk(    #54
        0x8,
        (
            "#100FMm? Something wrong?\x02\x03",

            "Still have some questions about\x01",
            "the data crystal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1011FNo, I think I get it, but, um...\x02\x03",

            "#1015FWell, what're you going to do while\x01",
            "it's deciphering?\x02\x03",

            "You seem pretty busy, given that you're\x01",
            "leaving it all to Capel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #56
        0x8,
        (
            "#100FAh, good eye. I'm putting together a little\x01",
            "something based on a theory of mine...\x02\x03",

            "To be honest, I found a base for...\x01",
            "a certain piece of equipment I'm\x01",
            "developing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_307A")

    ChrTalk(    #57
        0x107,
        "#064FA 'certain piece of equipment'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A2")

    label("loc_307A")


    ChrTalk(    #58
        0x102,
        "#1044FA 'certain piece' of... Hmm.\x02",
    )

    CloseMessageWindow()

    label("loc_30A2")


    ChrTalk(    #59
        0x101,
        (
            "#1015FWell, when you put it like THAT,\x01",
            "I've gotta know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#104FI'm sorry, but I can't speak more of it\x01",
            "just yet.\x02\x03",

            "It's quite possible nothing will come\x01",
            "of it and I'm just a stubborn old fool.\x02\x03",

            "#101FFor now, look forward to getting something\x01",
            "new soon...and wish me luck, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1E2A)
    Return()

    # Function_5_2E8C end

    def Function_6_31C3(): pass

    label("Function_6_31C3")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3253")
    Jump("loc_3295")

    label("loc_3253")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_326F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3295")

    label("loc_326F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_328B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3295")

    label("loc_328B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3295")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_331D"),
        (1, "loc_34B8"),
        (2, "loc_34F9"),
        (SWITCH_DEFAULT, "loc_34FC"),
    )


    label("loc_331D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3411")

    ChrTalk(    #61
        0xA,
        (
            "#053FRepairs are pretty close to done, so I\x01",
            "popped in here for a quick breather.\x02\x03",

            "#050FLooks like the society's just gonna bite\x01",
            "back even harder now that we're exploring\x01",
            "that Axis whatever.\x02\x03",

            "Gotta get some rest while we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_34B5")

    label("loc_3411")


    ChrTalk(    #62
        0xA,
        (
            "#050FRepairs are pretty close to done, so I\x01",
            "popped in here for a quick breather.\x02\x03",

            "The society's just gonna bite back harder.\x01",
            "Gotta get some rest while we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B5")

    Jump("loc_34FC")

    label("loc_34B8")


    ChrTalk(    #63
        0xA,
        (
            "#050FNeed to change team members?\x01",
            "I'm all set to go.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_34FC")

    label("loc_34F9")

    Jump("loc_34FC")

    label("loc_34FC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_31C3 end

    def Function_7_3505(): pass

    label("Function_7_3505")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_356B"),
        (1, "loc_55CF"),
        (2, "loc_55F9"),
        (SWITCH_DEFAULT, "loc_55FC"),
    )


    label("loc_356B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_365B")

    ChrTalk(    #64
        0x107,
        (
            "#060FGrandpa's not sure what the Zemurian Ore\x01",
            "is made of, exactly.\x02\x03",

            "We've got a lot of data, though, so we can\x01",
            "look it all over later when we get home!\x02\x03",

            "Heehee! I think we're gonna be busy once\x01",
            "we win. We will win, right...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55CC")

    label("loc_365B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 2)), scpexpr(EXPR_END)), "loc_3DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9A")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #65
        0xB,
        (
            "#064FEstelle! Joshua!\x02\x03",

            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1025FUm... yeah. There's something\x01",
            "I want to talk to you about, Tita.\x02\x03",

            "#1003FRenne...chose to fight us.\x01",
            "In her capacity as an Enforcer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0xB,
        "#065FHuh?! Oh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1040FShe did. But you needn't worry.\x01",
            "She's safe.\x02\x03",

            "After we defeated her, she retreated\x01",
            "and went...somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "#064FOh, o-okay.\x02\x03",

            "#561FI-I'm...really glad she's not hurt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1015FI'm not really sure if we got through\x01",
            "to her...\x02\x03",

            "...but I think, I hope, she's started to\x01",
            "think about things for herself, rather\x01",
            "than just doing what Ouroboros says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1040FPersonally, I'm hopeful about her.\x02\x03",

            "Renne's a smart girl--smarter than I was,\x01",
            "anyway. She'll come to understand it all\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #72
        0xB,
        (
            "#560FYeah! Yeah, I bet she will.\x02\x03",

            "#066FI hope... I hope she and I can\x01",
            "play again someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1017FYou'll meet her again, Tita. I know you will.\x01",
            "Just keep believing, you know?\x02\x03",

            "After all, it took a while, but I met\x01",
            "Joshua again, in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        "#1049FHaha. True enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        "#560FAh... yeah!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A3)
    Jump("loc_3B1A")

    label("loc_3A9A")


    ChrTalk(    #76
        0xB,
        (
            "#060FBeing in the society is a mistake...\x02\x03",

            "I'm sure Renne will understand that,\x01",
            "someday.\x02\x03",

            "I hope we can go shopping again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1A")

    Jump("loc_3DF9")

    label("loc_3B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D51")

    ChrTalk(    #77
        0xB,
        (
            "#063FRenne's gone away somewhere, but...\x02\x03",

            "She'll understand what we said to her\x01",
            "someday, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1040FPersonally, I'm hopeful about her.\x02\x03",

            "Renne's a smart girl--smarter than I was,\x01",
            "anyway. She'll come to understand it all\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #79
        0xB,
        (
            "#560FYeah! Yeah, I bet she will.\x02\x03",

            "#066FI hope... I hope she and I can\x01",
            "play again someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1017FYou'll meet her again, Tita. I know you will.\x01",
            "Just keep believing, you know?\x02\x03",

            "After all, it took a while, but I met\x01",
            "Joshua again, in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1049FHaha. True enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xB,
        "#560FAh... yeah!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A3)
    Jump("loc_3DF9")

    label("loc_3D51")


    ChrTalk(    #83
        0xB,
        (
            "#560FRenne will figure things out on her own,\x01",
            "right?\x02\x03",

            "I'll believe in Renne like you believed in\x01",
            "Joshua, Estelle!\x02\x03",

            "#067FI hope we can go shopping again someday...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF9")

    Jump("loc_55CC")

    label("loc_3DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_3EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7C")

    ChrTalk(    #84
        0xB,
        (
            "#060FI wonder if the flight engine test\x01",
            "will go okay?\x02\x03",

            "#067FMy heart's racing just thinking about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3EF1")

    label("loc_3E7C")


    ChrTalk(    #85
        0xB,
        (
            "#060FI wonder if the flight engine test\x01",
            "will go okay?\x02\x03",

            "#067FHeeee, I can't stay still.\x01",
            "My heart's all fluttery!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF1")

    Jump("loc_55CC")

    label("loc_3EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4108")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #86
        0xB,
        (
            "#064FOh, um, you're the bandit lady!\x02\x03",

            "#560FUm, I'm, um, Tita!\x02\x03",

            "N-Nice to meet you!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 2)), scpexpr(EXPR_END)), "loc_401B")

    ChrTalk(    #87
        0x10B,
        (
            "#413FUh, 'scuse me, kid.\x01",
            "I've got a name and it's Josette.\x02\x03",

            "Could you please not be like your granddad\x01",
            "in calling me weird nicknames?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_406F")

    label("loc_401B")


    ChrTalk(    #88
        0x10B,
        (
            "#213FB-Bandit lady? Argh...\x02\x03",

            "#215FYou know I have a name, right?\x01",
            "It's Josette.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406F")

    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #89
        0xB,
        (
            "#065FOh! Umm, I'm sorry, band--\x02\x03",

            "#067FEr, I mean, Josette! Haha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10B,
        "#216F(Is she...doing that on purpose now?!)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x22A2)
    Jump("loc_461E")

    label("loc_4108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_416B")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #91
        0xB,
        (
            "#560FUm, nice to meet you, Josette.\x02\x03",

            "I hope we can all get along!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461E")

    label("loc_416B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_44CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4430")

    ChrTalk(    #92
        0xB,
        "#560FWelcome back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006FThanks! You look like you're working\x01",
            "pretty hard, Tita.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #94
        0xB,
        (
            "#060FUh-huh! I'm checking the lights!\x02\x03",

            "We've gone back to normal lighting, but\x01",
            "it'd be bad if a short somewhere strains\x01",
            "the engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1040FI see. How are the repairs going,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #96
        0xB,
        (
            "#060FGrandpa's started tuning the flight\x01",
            "engine.\x02\x03",

            "Once he's done, we'll do a simulated\x01",
            "lift-off test.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4378")

    ChrTalk(    #97
        0x10B,
        (
            "#213FHoly crap, you guys are practically done\x01",
            "already. After crashing like that, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4378")


    ChrTalk(    #98
        0x102,
        (
            "#1040FJust what I'd expect from Professor Russell.\x01",
            "He works fast when he focuses on something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43DC")


    ChrTalk(    #99
        0xB,
        (
            "#067FHeehee! It won't be long now.\x02\x03",

            "I'm going to do my best to help out!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CD)
    Jump("loc_44C9")

    label("loc_4430")


    ChrTalk(    #100
        0xB,
        (
            "#060FGrandpa's starting tuning the flight\x01",
            "engine.\x02\x03",

            "Once he's done, we'll do a simulated\x01",
            "lift-off test.\x02\x03",

            "Just a little bit more work and we can\x01",
            "fly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C9")

    Jump("loc_461E")

    label("loc_44CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")

    ChrTalk(    #101
        0xB,
        (
            "#060FWe'll be turning the lights back on\x01",
            "soon.\x02\x03",

            "Right now we're inspecting the power\x01",
            "transmission systems involved.\x02\x03",

            "Once that's done, all we need to do is\x01",
            "connect the quartz.\x02\x03",

            "#067FWe'll be able to see again!\x01",
            "I can't wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_461E")

    label("loc_45BF")


    ChrTalk(    #102
        0xB,
        (
            "#060FWe'll be turning the lights\x01",
            "back on soon.\x02\x03",

            "We'll be able to see again!\x01",
            "I can't wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_461E")

    Jump("loc_55CC")

    label("loc_4621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E0")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #103
        0xB,
        (
            "#060FOh, hi, Estelle!\x02\x03",

            "Like Grandpa said, there doesn't seem to\x01",
            "be any big problem with the orbal engine.\x02\x03",

            "We still need to look close at the engine\x01",
            "before we know for sure...\x02\x03",

            "...but we'll probably be able to fly\x01",
            "sooner than we thought!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1006FThat's good to hear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1040FIt does make things seem a bit\x01",
            "less grim, yes.\x02\x03",

            "Keep up the good work, Tita.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #106
        0xB,
        (
            "#560FI will!\x02\x03",

            "#067FAhhhhh, I get to touch the Arseille's\x01",
            "XG-02 engine...\x02\x03",

            "Ehe, ehehehe... I can't waaaaaait. ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(60)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_487D")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_48BB")

    label("loc_487D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A4")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_48BB")

    label("loc_48A4")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_48BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E2")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4920")

    label("loc_48E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4909")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4920")

    label("loc_4909")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_4920")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4988")

    ChrTalk(    #107
        0x106,
        "#551FAaaaand she's not on the same planet anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1016FHahaha...ha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_49DA")

    label("loc_4988")


    ChrTalk(    #109
        0x101,
        (
            "#1016FHahaha...ha...\x02\x03",

            "Sooooomeone's just died and gone\x01",
            "to heaven, I think...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DA")

    OP_A2(0x22C0)
    Jump("loc_4A37")

    label("loc_49E0")


    ChrTalk(    #110
        0xB,
        (
            "#067F*siiiigh* The Arseille's engine, and quartz,\x01",
            "and...\x02\x03",

            "Ooooh, I can't wait. ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A37")

    Jump("loc_55CC")

    label("loc_4A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B79")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #111
        0xB,
        "#063FOh... Estelle... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1010FIt's okay. I know what you want to say.\x02\x03",

            "#1000FWe'll take care of Renne. Don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        (
            "#1040FI don't think any of us can say for sure\x01",
            "how it will go...\x02\x03",

            "But we'll do everything we can to bring\x01",
            "her back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #114
        0xB,
        "#063FO-Okay...please...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E41)
    Jump("loc_4BB0")

    label("loc_4B79")

    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #115
        0xB,
        "#063FEstelle, Joshua...please! Save Renne!\x02",
    )

    CloseMessageWindow()

    label("loc_4BB0")

    Jump("loc_55CC")

    label("loc_4BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F1E")

    ChrTalk(    #116
        0xB,
        "#060FOh, hi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1001FHey, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        "#020FHow's the professor's research going?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #119
        0xB,
        (
            "#063FOh, um.\x02\x03",

            "#561FEven Grandpa's having a hard time with\x01",
            "those barriers.\x02\x03",

            "He keeps saying he just doesn't understand\x01",
            "the principle behind them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1015FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1043FThe barriers most likely have something to\x01",
            "do with the mission the Enforcers have\x01",
            "been given.\x02\x03",

            "I doubt a solution to breaching them will\x01",
            "be straightforward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        (
            "#020FWell, there's little point in sitting\x01",
            "here, moping around about it.\x02\x03",

            "We can leave studying it to the professor\x01",
            "while we enter the towers the old-fashioned\x01",
            "way.\x02\x03",

            "What we find in the towers might lead to\x01",
            "some hints to help his research.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #123
        0x101,
        "#1011FYeah, and there's the data crystals, too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #124
        0x102,
        (
            "#1040FYou're right. Let's focus on investigating\x01",
            "the towers for now...the old-fashioned way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E2B)
    Jump("loc_4F94")

    label("loc_4F1E")


    ChrTalk(    #125
        0xB,
        (
            "#063FEven Grandpa doesn't know what to do\x01",
            "about those barriers.\x02\x03",

            "I hope you can find some hints in the\x01",
            "towers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F94")

    Jump("loc_55CC")

    label("loc_4F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4FA1")
    Jump("loc_55CC")

    label("loc_4FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_55CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505E")

    ChrTalk(    #126
        0xB,
        "#060FAh! Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x106,
        (
            "#051FHey, shortstuff.\x02\x03",

            "Already botherin' your Grandpa, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "#063FI-I'm not a bother!\x02\x03",

            "I'm, um, just peeking in on his research!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50F4")

    label("loc_505E")


    ChrTalk(    #129
        0xB,
        "#060FOh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1001FHaha, straight to the professor, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "#560FUm, yeah!\x02\x03",

            "I thought I'd peek in and see how the\x01",
            "research is going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 1)), scpexpr(EXPR_END)), "loc_51A6")

    ChrTalk(    #132
        0x102,
        (
            "#1043FAnalyzing the phenomena surrounding the\x01",
            "towers, and that 'equipment' he's working on...\x02\x03",

            "Even Russell must be having trouble\x01",
            "managing both at the same time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_532F")

    label("loc_51A6")


    ChrTalk(    #133
        0x102,
        (
            "#1040FSo he's already begun looking at that\x01",
            "strange barrier around the towers?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #134
        0xB,
        (
            "#060FUh-huh, he's looking into that too.\x02\x03",

            "#561FBut there's something else he's\x01",
            "researching...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1004FSomething else? On TOP of all the\x01",
            "stuff going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1044FHe's shouldering another project on top\x01",
            "of looking into the towers?\x02\x03",

            "Even for Russell, managing both at once\x01",
            "would be...difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_532F")

    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #137
        0xB,
        (
            "#060FYeah...\x02\x03",

            "That's why I want to help with whatever I can.\x02\x03",

            "Oh, um, but if you need me, I'll be glad\x01",
            "to help you, too, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1006FIt's okay.\x01",
            "You stay here for now.\x02\x03",

            "If we really need help,\x01",
            "we'll come and ask, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x102,
        (
            "#1049FYes. I imagine Russell needs a good\x01",
            "assistant right about now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553E")

    ChrTalk(    #140
        0x106,
        (
            "#552FYeah, you leave the old man alone and\x01",
            "two research projects could turn into\x01",
            "three...or three hundred.\x02\x03",

            "Keep an eye on him, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "#560FHeehee... I know.\x02\x03",

            "Agate...please, take care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5574")

    label("loc_553E")


    ChrTalk(    #142
        0xB,
        (
            "#560FYeah! I'll do my best.\x02\x03",

            "Take care, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5574")

    OP_A2(0x1E2C)
    Jump("loc_55CC")

    label("loc_557A")


    ChrTalk(    #143
        0xB,
        (
            "#060FI'm going to stay here and\x01",
            "help out Grandpa.\x02\x03",

            "If you need me, just ask!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55CC")

    Jump("loc_55FC")

    label("loc_55CF")


    ChrTalk(    #144
        0xB,
        "#060FOh, do you need my help?\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_55FC")

    label("loc_55F9")

    Jump("loc_55FC")

    label("loc_55FC")

    TalkEnd(0xFE)
    Return()

    # Function_7_3505 end

    def Function_8_5600(): pass

    label("Function_8_5600")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_562A")

    ChrTalk(    #145
        0xFE,
        "#070F◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_5D3B")

    label("loc_562A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA6")

    def lambda_563F():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_563F)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #146
        0xC,
        (
            "#070FEstelle! Good to see you.\x02\x03",

            "What brings you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#1000FI could ask the same thing of you, Zin.\x02\x03",

            "#1018FAh, I know! Trying to catch a nap\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xC,
        (
            "#071FHaha! Probably wouldn't be a bad idea,\x01",
            "but no. I thought I'd get a little practice in.\x02\x03",

            "I cannot seem to stay calm, sitting in a\x01",
            "confined space like this ship.\x02\x03",

            "#070FYou're in the middle of one of your walks,\x01",
            "I'd guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1007FYeah, I can never manage to\x01",
            "sit still myself...\x02\x03",

            "#1015FBut, practice, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #150
        0x101,
        "#1015FIsn't this a little...cramped for practice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xC,
        (
            "#070FPractice isn't all about movement,\x01",
            "remember.\x02\x03",

            "There's plenty you can do even in a small\x01",
            "space such as this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #152
        0x101,
        "#1000FHuh? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xC,
        (
            "#074FBreathing exercises and meditation, for\x01",
            "one, but practicing your forms is an\x01",
            "important part of training as well.\x02\x03",

            "Especially for bracers like us, who tend to\x01",
            "get a little sloppy and let our styles fall\x01",
            "apart from so much 'live' combat.\x02\x03",

            "#070FIt's important, from time to time, to find\x01",
            "a chance to return to the basics and\x01",
            "correct yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1013FThat's, um, a good point.\x01",
            "I haven't actually done any disciplined\x01",
            "practice for a while now.\x02\x03",

            "Hearing you put it that way makes me worry\x01",
            "I'm, like, an awful mess in a fight now.\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xC,
        (
            "#070FHaha, it's nothing to worry about.\x01",
            "I was speaking generally.\x02\x03",

            "Still, if it resonated with you, then\x01",
            "there's nothing lost by finding a chance\x01",
            "to re-center yourself.\x02\x03",

            "My offer still stands to be a practice\x01",
            "partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1001FHaha! Well, thanks, Zin.\x01",
            "I may just take you up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xC,
        "#070FI'll be looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1A22)
    Jump("loc_5D3B")

    label("loc_5CA6")


    def lambda_5CAC():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5CAC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #158
        0xC,
        (
            "#070FI'm going to continue my kata for a\x01",
            "while.\x02\x03",

            "I want to be warmed up when that dragon\x01",
            "appears.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)

    label("loc_5D3B")

    TalkEnd(0xFE)
    Return()

    # Function_8_5600 end

    def Function_9_5D3F(): pass

    label("Function_9_5D3F")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5DA5"),
        (1, "loc_75A7"),
        (2, "loc_75FB"),
        (SWITCH_DEFAULT, "loc_75FE"),
    )


    label("loc_5DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_5FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F0C")

    ChrTalk(    #159
        0xD,
        (
            "#1060FOnly place left to poke our noses into is\x01",
            "that big central tower. Looks like we've\x01",
            "hit the end of the road.\x02\x03",

            "Those society guys'll be bringin'\x01",
            "everything they've got.\x01",
            "It ain't gonna be easy.\x02\x03",

            "But hey, it'd be weird to get this far\x01",
            "without a grand finale, right?\x02\x03",

            "Let's find the Aureole and get back\x01",
            "to the Goddess' good earth.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5FB2")

    label("loc_5F0C")


    ChrTalk(    #160
        0xD,
        (
            "#1060FOnly place left to poke our noses into is\x01",
            "that big central tower. Looks like we've\x01",
            "hit the end of the road.\x02\x03",

            "If you want, I'll help you in any way \x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FB2")

    Jump("loc_75A4")

    label("loc_5FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_61AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60ED")

    ChrTalk(    #161
        0xD,
        (
            "#1060FSounds like we've hooked up with those\x01",
            "sky bandits, eh?\x02\x03",

            "I'm on board with that. No harm in having\x01",
            "as many friends as we can up here.\x02\x03",

            "I'll see if I can think of any way I can\x01",
            "help out with that.\x02\x03",

            "I suppose for now I can throw together\x01",
            "some medical supplies for them and\x01",
            "whatnot.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_61A7")

    label("loc_60ED")


    ChrTalk(    #162
        0xD,
        (
            "#1060FI'll think of something I can do to help\x01",
            "out the sky bandits, let 'em know\x01",
            "we're friendly.\x02\x03",

            "I suppose for now I can throw together\x01",
            "some medical supplies for them and\x01",
            "whatnot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61A7")

    Jump("loc_75A4")

    label("loc_61AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_662C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6346")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #163
        0xD,
        (
            "#1060FJosette, right?\x02\x03",

            "I'm Kevin Graham, priest of the Septian\x01",
            "Church.\x02\x03",

            "#1061FI've always got time for cute girls,\x01",
            "so nice to meet'cha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10B,
        (
            "#215FUh... yeah, nice to meet you, too...\x02\x03",

            "#212F...but are you really a priest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xD,
        (
            "#1060FYou bet I am! One hundred percent pure\x01",
            "holy man, right here.\x02\x03",

            "#1064F...Hey, what's with the blatant look\x01",
            "of disbelief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10B,
        "#212F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x22A4)
    Jump("loc_6629")

    label("loc_6346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_642B")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #167
        0xD,
        (
            "#1064FI'm SERIOUS! I'm really a priest!\x01",
            "Look, medallion, Testaments, everything!\x02\x03",

            "#1068FOh, man, bein' doubted by a cutie!\x01",
            "It's heartbreaking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10B,
        "#413F(It's just... This guy? A priest? No way.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6629")

    label("loc_642B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6558")

    ChrTalk(    #169
        0xD,
        (
            "#1063FI dunno if it's because everyone's\x01",
            "workin' themselves to the bone,\x01",
            "but we've got a lot of injuries.\x02\x03",

            "They ain't much more than scratches,\x01",
            "thankfully. Still, you guys be careful\x01",
            "out there too, yeah?\x02\x03",

            "I dunno how long we'll be here, so I\x01",
            "need to make our supplies last a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_6629")

    label("loc_6558")


    ChrTalk(    #170
        0xD,
        (
            "#1063FI dunno if it's because everyone's\x01",
            "workin' themselves to the bone,\x01",
            "but we've got a lot of injuries.\x02\x03",

            "They ain't much more than scratches,\x01",
            "thankfully. Still, you guys be careful\x01",
            "out there too, yeah?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6629")

    Jump("loc_75A4")

    label("loc_662C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_67A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6722")

    ChrTalk(    #171
        0xD,
        (
            "#1062FYo, Estelle, everyone!\x02\x03",

            "I just finished cleaning up sickbay, here.\x02\x03",

            "#1066FThe cabinets kinda, uh, spilled\x01",
            "everything out when we made\x01",
            "that crash landing.\x02\x03",

            "Anyway, you start feelin' like dirt,\x01",
            "just c'mon down here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_67A4")

    label("loc_6722")


    ChrTalk(    #172
        0xD,
        (
            "#1060FAnyway, you start feelin' like dirt,\x01",
            "just c'mon down here.\x02\x03",

            "My trade's in helpin' the soul AND body.\x01",
            "I can fix you up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A4")

    Jump("loc_75A4")

    label("loc_67A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_6D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C82")

    ChrTalk(    #173
        0xD,
        (
            "#1067FOh, boy...\x01",
            "Last Enforcer's that girl, huh?\x02\x03",

            "I was kinda hopin' she wouldn't turn up,\x01",
            "but...\x02\x03",

            "#1068FWell, figures Ouroboros would throw\x01",
            "a child in our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1003FYeah... That's how I thought at first, too...\x02\x03",

            "#1002FI think this might be what we need,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #175
        0xD,
        (
            "#1064FHow in the heck is havin' to fight a\x01",
            "murderous pre-teen somethin' we NEED?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1015FWell, I want to rescue her from the society.\x01",
            "And I've got a lot I want to say to her.\x02\x03",

            "When you've got something to say from\x01",
            "the heart, it's best to say it face to face,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xD,
        (
            "#1066FHaha! That's one way of lookin' at it,\x01",
            "I suppose!\x02\x03",

            "#1071FYeah, that's more like it, Estelle.\x01",
            "You're shinin' like the sun again!\x02\x03",

            "You keep that up and I mi--\x02\x03",

            "#1063F*cough* Sorry.\x01",
            "I almost did my usual thing there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x101,
        "#1011FYour... Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xD,
        "#1068FUhhh, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x102,
        "#1048FMy apologies for existing, Kevin.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #181
        0xD,
        (
            "#1066FHahaaaa, noooo, no.\x01",
            "My bad, really.\x02\x03",

            "Just, uh, gimme a pass on that one,\x01",
            "yeah? I'll be better next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1019FAre you guys, like, having some kinda\x01",
            "male bonding moment or something?\x01",
            "It's creeping me out.\x02\x03",

            "I'm right here and I've got a long stick\x01",
            "with your names on it, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x1E2E)
    Jump("loc_6D8C")

    label("loc_6C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_6D17")

    ChrTalk(    #183
        0xD,
        (
            "#1060FAnyway, seriously, keep up the positive\x01",
            "thinkin', Estelle. It's a good thing to have.\x02\x03",

            "I really am a sucker for cheery girls...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8C")

    label("loc_6D17")


    ChrTalk(    #184
        0xD,
        (
            "#1060FLike you said, Estelle, let's keep it\x01",
            "positive.\x02\x03",

            "Gettin' all grim and morose ain't gonna\x01",
            "get us anywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8C")

    Jump("loc_75A4")

    label("loc_6D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6F63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA9")

    ChrTalk(    #185
        0xD,
        (
            "#1064FMan, climbin' that 'shadow' tower like\x01",
            "it's nothin' at all...\x02\x03",

            "Aidios! I dunno if what I'm feelin' is\x01",
            "fear or a crush!\x02\x03",

            "#1064FWell, it helps keep us guys on our toes,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #186
        0xD,
        "#1061FRight, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        "#1048FLeave me out of this, please.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_6F60")

    label("loc_6EA9")


    ChrTalk(    #188
        0xD,
        (
            "#1060FI never woulda figured someone'd be able\x01",
            "to climb that 'shadow' tower on their own.\x02\x03",

            "Sometimes I think women can make even\x01",
            "the most determined guys look like\x01",
            "lightweights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F60")

    Jump("loc_75A4")

    label("loc_6F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_711C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7088")

    ChrTalk(    #189
        0xD,
        (
            "#1063F'Shadow' tower interiors and beta Gospels\x01",
            "on the roofs...\x02\x03",

            "We STILL don't know what the society's\x01",
            "tryin' to do, but something stinks.\x02\x03",

            "#1062FWell, at times like this the best we\x01",
            "can do is help each other out!\x02\x03",

            "I'll be on standby.\x01",
            "If you need me, just come ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_7119")

    label("loc_7088")


    ChrTalk(    #190
        0xD,
        (
            "#1063F'Shadow' tower interiors and beta Gospels\x01",
            "on the roofs...\x02\x03",

            "We STILL don't know what the society's\x01",
            "tryin' to do, but something stinks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7119")

    Jump("loc_75A4")

    label("loc_711C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_75A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7544")

    ChrTalk(    #191
        0xD,
        "#1062FHey, Estelle. Heading into the tower?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1006FYeah, once we're ready.\x02\x03",

            "How about you, Kevin?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #193
        0xD,
        (
            "#1060FI'm just givin' the sickbay a once-over,\x01",
            "familiarizing myself with it a bit.\x02\x03",

            "You know, just in case I ever need to\x01",
            "make use of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        (
            "#1049FKnowledge of modern medicine?\x01",
            "Pretty uncommon for a Gralsritter.\x01",
            "Impressive, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #195
        0xD,
        (
            "#1066FHaha, yeah, well, it's somethin' I picked\x01",
            "up because I kinda had to.\x02\x03",

            "'Sides, I'd be even happier if I had no\x01",
            "reason to use this place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_734C")

    ChrTalk(    #196
        0x105,
        "#047FAs would I...\x02",
    )

    CloseMessageWindow()
    Jump("loc_73D0")

    label("loc_734C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_736F")

    ChrTalk(    #197
        0x108,
        "#070FAgreed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73D0")

    label("loc_736F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73A8")

    ChrTalk(    #198
        0x103,
        "#026FI certainly can't disagree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_73D0")

    label("loc_73A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73D0")

    ChrTalk(    #199
        0x106,
        "#050FGot that right.\x02",
    )

    CloseMessageWindow()

    label("loc_73D0")


    ChrTalk(    #200
        0x101,
        (
            "#1002FLet's be careful exploring, then,\x01",
            "so we don't need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x102,
        (
            "#1042FYes, we must proceed cautiously.\x02\x03",

            "We have no idea what dangers may be\x01",
            "lurking within the towers themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xD,
        (
            "#1060FGot that right. Caution, more than anything,\x01",
            "will make sure this place stays useless.\x02\x03",

            "Anyway, don't get too reckless, and make\x01",
            "sure I've got no use for a sickbay,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E2D)
    Jump("loc_75A4")

    label("loc_7544")


    ChrTalk(    #203
        0xD,
        (
            "#1060FI'd love it if we had no reason to\x01",
            "use this place.\x02\x03",

            "Estelle, gang, be careful, yeah?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75A4")

    Jump("loc_75FE")

    label("loc_75A7")


    ChrTalk(    #204
        0xD,
        (
            "#1060FYou need a handsome, charmin' priest in\x01",
            "your party? I'm your man!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_75FE")

    label("loc_75FB")

    Jump("loc_75FE")

    label("loc_75FE")

    TalkEnd(0xFE)
    Return()

    # Function_9_5D3F end

    def Function_10_7602(): pass

    label("Function_10_7602")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7668"),
        (1, "loc_7A27"),
        (2, "loc_7A83"),
        (SWITCH_DEFAULT, "loc_7A86"),
    )


    label("loc_7668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_780C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776E")

    ChrTalk(    #205
        0xE,
        (
            "#210FSounds like the Bobcat's repairs are\x01",
            "going pretty well!\x02\x03",

            "Apparently they fixed the problem in the\x01",
            "flight controls with Professor Russell's\x01",
            "help.\x02\x03",

            "Kyle was really impressed with that old coo-,\x01",
            "er, with Liberl's number one engineer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_7809")

    label("loc_776E")


    ChrTalk(    #206
        0xE,
        (
            "#210FSounds like the Bobcat's repairs are\x01",
            "going pretty well!\x02\x03",

            "Apparently they fixed the problem in the\x01",
            "flight controls with Professor Russell's\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7809")

    Jump("loc_7A24")

    label("loc_780C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_7A24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79A1")

    ChrTalk(    #207
        0xE,
        (
            "#210FHi, guys.\x02\x03",

            "I'm just a liaison, but I'm doing what\x01",
            "I can to help!\x02\x03",

            "I mean, you saved my brothers.\x01",
            "I don't want to owe you even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1007F*sigh* I dunno whether to say you hate\x01",
            "losing or just call you stubborn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        (
            "#1040FIt still helps.\x02\x03",

            "Not all of us can remain here to\x01",
            "help repair the ship, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #210
        0xE,
        (
            "#414FOh... U-Umm...\x02\x03",

            "#415FY-Yeah! Leave it to me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CE)
    Jump("loc_7A24")

    label("loc_79A1")


    ChrTalk(    #211
        0xE,
        (
            "#210FI'm just a liaison, but I'm doing what\x01",
            "I can to help!\x02\x03",

            "I mean, you saved my brothers.\x01",
            "I don't want to owe you even more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A24")

    Jump("loc_7A86")

    label("loc_7A27")


    ChrTalk(    #212
        0xE,
        (
            "#210FHeheh! Yeah, figured you wouldn't be able\x01",
            "to get anything done without me!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_7A86")

    label("loc_7A83")

    Jump("loc_7A86")

    label("loc_7A86")

    TalkEnd(0xFE)
    Return()

    # Function_10_7602 end

    def Function_11_7A8A(): pass

    label("Function_11_7A8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_7D2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C9F")

    ChrTalk(    #213
        0xFE,
        (
            "We've done test after test to wring as\x01",
            "much performance as we can from the\x01",
            "engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "No matter how many experiments we do,\x01",
            "though, in live combat things will be\x01",
            "different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "As one of the development staff,\x01",
            "I'm half eager and half terrified to\x01",
            "see how the engine performs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "If it can get us through this mission,\x01",
            "I'd say all the hard work will have been\x01",
            "worth it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "This'll be the first flight out of the\x01",
            "nest for this little bird. I'll be seeing\x01",
            "how she does and collecting the final data.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7D2D")

    label("loc_7C9F")


    ChrTalk(    #218
        0xFE,
        (
            "We've done test after test,\x01",
            "but live combat is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "We development guys are half eager\x01",
            "and half terrified to see how it does!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D2D")

    TalkEnd(0xFE)
    Return()

    # Function_11_7A8A end

    def Function_12_7D31(): pass

    label("Function_12_7D31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_7E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E15")

    ChrTalk(    #220
        0xFE,
        "Ooooo...kay! Instruments check out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "It isn't too often that you get to measure\x01",
            "an engine's output in action!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I am TOTALLY writing all this down for all\x01",
            "the engines we design in the future!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_7E73")

    label("loc_7E15")


    ChrTalk(    #223
        0xFE,
        "Oooooo...kay. Instruments check out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "Now we just wait for Mister Dragon to\x01",
            "show up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E73")

    TalkEnd(0xFE)
    Return()

    # Function_12_7D31 end

    def Function_13_7E77(): pass

    label("Function_13_7E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800A")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #225
        0xFE,
        "Nya-go.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x101,
        "#1004FAntoine?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F14")

    ChrTalk(    #227
        0x107,
        (
            "#067FHeehee! Are you surprised?\x02\x03",

            "Ray brought her aboard!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F56")

    label("loc_7F14")


    ChrTalk(    #228
        0x102,
        (
            "#1044FDid someone from the central factory bring\x01",
            "her aboard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F56")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #229
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#1016FWhy is it that we always meet you\x01",
            "when our lives are on the line, Antoine?\x02\x03",

            "Wellllll...it's always good to see my\x01",
            "favorite kitty.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #231
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)
    Jump("loc_801A")

    label("loc_800A")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #232
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    label("loc_801A")

    TalkEnd(0xFE)
    Return()

    # Function_13_7E77 end

    def Function_14_801E(): pass

    label("Function_14_801E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_818A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811A")

    ChrTalk(    #233
        0xFE,
        "Ah, you're the bracers I heard about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "I never thought General Morgan would\x01",
            "allow bracers aboard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "The Royal Army's really changing,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "I guess it's proof General Bright's\x01",
            "reorganization is coming along.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_818A")

    label("loc_811A")


    ChrTalk(    #237
        0xFE,
        (
            "I never thought General Morgan would\x01",
            "allow bracers aboard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "The Royal Army's really changing,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_818A")

    TalkEnd(0xFE)
    Return()

    # Function_14_801E end

    def Function_15_818E(): pass

    label("Function_15_818E")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_8252")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8223")

    ChrTalk(    #239
        0xFE,
        "*yawn* Already time for my shift, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "Didn't get near enough sleep, buuuut I'd\x01",
            "better get to my post...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_824F")

    label("loc_8223")


    ChrTalk(    #241
        0xFE,
        "*yawn* Already time for my shift, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_824F")

    Jump("loc_8FE8")

    label("loc_8252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_8532")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_835C")

    ChrTalk(    #242
        0xFE,
        (
            "Er, Your Highness!\x01",
            "Thank you for your efforts so far!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "At the rate we're going, we'll succeed at\x01",
            "the mission Her Majesty entrusted to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Put everything you've got into this last\x01",
            "tower! We're behind you, Your Highness!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_83EE")

    label("loc_835C")


    ChrTalk(    #245
        0xFE,
        (
            "At the rate we're going, we'll succeed at\x01",
            "the mission Her Majesty entrusted to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "Put everything you've got into the last\x01",
            "tower, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83EE")

    Jump("loc_852F")

    label("loc_83F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F5")

    ChrTalk(    #247
        0xFE,
        (
            "Man, oh, man. The end is FINALLY in sight\x01",
            "for this friggin' mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "Give this last one your all so we can put\x01",
            "it to bed, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Like, you know, the ends justify the--\x01",
            "well, maybe not that ruthless, but...\x01",
            "Aww, just try hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_852F")

    label("loc_84F5")


    ChrTalk(    #250
        0xFE,
        (
            "Give this last one your all so we can go\x01",
            "home, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_852F")

    Jump("loc_8FE8")

    label("loc_8532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_884B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_862F")

    ChrTalk(    #251
        0xFE,
        (
            "So, after Zeiss, the society's paid thugs\x01",
            "are in Ruan, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "Sounds like we've got snakes all across\x01",
            "the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Your Highness, please, be careful.\x01",
            "There could be, you know, a viper in the\x01",
            "grass anywhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_86CA")

    label("loc_862F")


    ChrTalk(    #254
        0xFE,
        (
            "Sounds like we've got snakes all across\x01",
            "the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "Your Highness, please, be careful.\x01",
            "There could be, you know, a viper in the\x01",
            "grass anywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86CA")

    Jump("loc_8848")

    label("loc_86CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C1")

    ChrTalk(    #256
        0xFE,
        (
            "Almost feels like the hand of the society\x01",
            "can reach across the whole kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "Reminds me of how things felt during\x01",
            "the coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "What is up with groups plotting awful stuff\x01",
            "like this springin' up like weeds these\x01",
            "days?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_8848")

    label("loc_87C1")


    ChrTalk(    #259
        0xFE,
        (
            "Almost feels like the hand of the society\x01",
            "can reach across the whole kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "Reminds me of how things felt during\x01",
            "the coup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8848")

    Jump("loc_8FE8")

    label("loc_884B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_8C8E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_88E6")

    ChrTalk(    #261
        0xFE,
        "Putting ancient quartz into an orbment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "What kind of madman does it take to\x01",
            "do that? The old man sure is gutsy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A2D")

    label("loc_88E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89BE")

    ChrTalk(    #263
        0xFE,
        (
            "Your Highness! Do you have some\x01",
            "business in the workshop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Professor Russell is analyzing the black\x01",
            "machine inside, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "It's a bit cluttered inside, so please,\x01",
            "watch your step.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_8A2D")

    label("loc_89BE")


    ChrTalk(    #266
        0xFE,
        (
            "Professor Russell's having a look at that\x01",
            "black machine in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "It's a bit cluttered, so watch out.\x02",
    )

    CloseMessageWindow()

    label("loc_8A2D")

    Jump("loc_8C8B")

    label("loc_8A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_8AB8")

    ChrTalk(    #268
        0xFE,
        "Putting ancient quartz into an orbment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "What kind of madman does it take to\x01",
            "do that? The old man sure is gutsy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C8B")

    label("loc_8AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE7")

    ChrTalk(    #270
        0xFE,
        (
            "The professor just brought out some\x01",
            "strange black thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "Is that what you found at the top of\x01",
            "the tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "What's the society trying to do with\x01",
            "those things, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "Hopefully the professor's research goes\x01",
            "quickly and we can get some answers\x01",
            "about the enemy's goals!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_8C8B")

    label("loc_8BE7")


    ChrTalk(    #274
        0xFE,
        (
            "What's the society trying to do with those\x01",
            "black machines, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "Not knowing what the enemy's goal is...\x01",
            "It's one of the worst feelings in the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8B")

    Jump("loc_8FE8")

    label("loc_8C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_8FE8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E21")

    ChrTalk(    #276
        0xFE,
        "Er, Your Highness! Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Shall you be departing with the bracers\x01",
            "to the tower, Your Highness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x105,
        (
            "#040FYes, that is my intention.\x02\x03",

            "This isn't the time to be observing from\x01",
            "on high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "Y-Your Highness... Such resolve!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "In that case, please use this workshop\x01",
            "room to prepare yourself to the fullest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "Mr. Payton seemed to have some\x01",
            "supplies ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_8ED3")

    label("loc_8E21")


    ChrTalk(    #282
        0xFE,
        (
            "If you're assaulting the tower, use the\x01",
            "workshop room to get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "Resolve and will is good and all...\x01",
            "but to really win a fight, you need good\x01",
            "steel and quartz, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED3")

    Jump("loc_8FE8")

    label("loc_8ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F6B")

    ChrTalk(    #284
        0xFE,
        "Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "This is the workshop room.\x01",
            "The storeroom's the other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "If you're looking for the lift,\x01",
            "it's near the storeroom.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_8FE8")

    label("loc_8F6B")


    ChrTalk(    #287
        0xFE,
        (
            "This is the workshop room.\x01",
            "The storeroom's the other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "If you're looking for the lift,\x01",
            "it's near the storeroom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FE8")

    TalkEnd(0xFE)
    Return()

    # Function_15_818E end

    def Function_16_8FEC(): pass

    label("Function_16_8FEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_9294")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91BD")

    ChrTalk(    #289
        0xFE,
        (
            "We've finished working out the theory,\x01",
            "so now we're actually putting the\x01",
            "'equipment' together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "Well...we SAY the theory's done,\x01",
            "but it's just the math, in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "The funny thing is, I couldn't even follow\x01",
            "what the math actually means!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "I mean, we proved it's true, but, uh...\x01",
            "I think the old man's the only one who\x01",
            "understands what we proved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "Ironic? Yeah, but this is kinda common\x01",
            "when working with the old man...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_9291")

    label("loc_91BD")


    ChrTalk(    #294
        0xFE,
        (
            "We've finished working out the theory,\x01",
            "so now we're actually putting the\x01",
            "'equipment' together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "It was a hard bit of research, but I've\x01",
            "got to admit it was satisfying.\x01",
            "Even if I don't understand it all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9291")

    Jump("loc_94AE")

    label("loc_9294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_94AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9404")

    ChrTalk(    #296
        0xFE,
        (
            "I've finally got some new crops growing\x01",
            "in the laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "I heard the old man was up to something\x01",
            "in here, though, so I had to come over\x01",
            "and see what was what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "From what the old man's saying,\x01",
            "I made the right choice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "So we're going to take on the problem\x01",
            "head-first, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "Heheheh!\x01",
            "This is going to be an exciting project!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_94AE")

    label("loc_9404")


    ChrTalk(    #301
        0xFE,
        (
            "So we're going to take on the problem\x01",
            "head-first, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "Just what I'd expect from the old man.\x01",
            "He's got a different sort of mind than\x01",
            "your average sepith-basher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94AE")

    TalkEnd(0xFE)
    Return()

    # Function_16_8FEC end

    def Function_17_94B2(): pass

    label("Function_17_94B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_9576")

    ChrTalk(    #303
        0xFE,
        (
            "Our research is finally nearing\x01",
            "completion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "We're going to need a bunch of prototype\x01",
            "models soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "The next step is going to be getting those\x01",
            "put together...in a hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98C4")

    label("loc_9576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_9760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A1")

    ChrTalk(    #306
        0xFE,
        (
            "I'm working on the quartz-circuit\x01",
            "prototypes while Ray and the professor\x01",
            "finish hashing out the theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "It isn't just theory that'll make this\x01",
            "work, it'll take engineering skill too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "That's why I was called up. I have a lot\x01",
            "of experience as an orbal electrician.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_975D")

    label("loc_96A1")


    ChrTalk(    #309
        0xFE,
        (
            "I'm working on the quartz-circuit\x01",
            "prototypes while Ray and the professor\x01",
            "finish hashing out the theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "This is going to need a good engineer\x01",
            "behind it, as well as solid theory!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_975D")

    Jump("loc_98C4")

    label("loc_9760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_98C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9838")

    ChrTalk(    #311
        0xFE,
        (
            "It's a great honor to be part of the\x01",
            "professor's research staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "I'll do my best to not be the slow gear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "I want this to be a good story for my\x01",
            "little brother, Todd, back in Ruan.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_98C4")

    label("loc_9838")


    ChrTalk(    #314
        0xFE,
        (
            "I hope this ends up a good story for\x01",
            "my brother, Todd, in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "He'll turn green with envy when I tell\x01",
            "him I was on the Arseille!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98C4")

    TalkEnd(0xFE)
    Return()

    # Function_17_94B2 end

    def Function_18_98C8(): pass

    label("Function_18_98C8")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_99A9")

    ChrTalk(    #316
        0x15,
        (
            "So did the professor tell you about the\x01",
            "level 3 upgrades?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x15,
        "I'm ready to do them whenever you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x15,
        (
            "It'll massively increase the EP charge\x01",
            "your orbments can hold, too, so I really\x01",
            "recommend doing it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x12)

    label("loc_99A9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Upgrade/Exchange\x01",      # 1
            "Shop\x01",                  # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_9A17")
    OP_A9(0x2E)
    Jump("loc_9A19")

    label("loc_9A17")

    OP_A9(0x28)

    label("loc_9A19")

    TalkEnd(0x15)
    Return()

    label("loc_9A20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_9A39")
    OP_A9(0x2D)
    Jump("loc_9A3B")

    label("loc_9A39")

    OP_A9(0x29)

    label("loc_9A3B")

    TalkEnd(0x15)
    Return()

    label("loc_9A42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A5C")
    FadeToBright(300, 0)
    TalkEnd(0x15)
    Return()

    label("loc_9A5C")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_9BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B3A")

    ChrTalk(    #319
        0x15,
        "Good work so far, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x15,
        (
            "Please, look over your equipment before\x01",
            "you head to the central tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x15,
        (
            "Once you're in battle, it will be too late,\x01",
            "no matter how hard you regret it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_9BF1")

    label("loc_9B3A")


    ChrTalk(    #322
        0x15,
        (
            "Please, look over your equipment before\x01",
            "you head to the central tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x15,
        (
            "You might find it effective to change your\x01",
            "gear depending on the kind of orbal enemy\x01",
            "you're fighting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF1")

    Jump("loc_A7BC")

    label("loc_9BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_9DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D20")

    ChrTalk(    #324
        0x15,
        "Ahhhhh, they finally got the lights working!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x15,
        (
            "It's easy to get depressed when you're\x01",
            "surrounded by the dark all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x15,
        (
            "Well! Now that we've got some lights,\x01",
            "time to shake off the sad and get to\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x15,
        (
            "If anything happens and you need help,\x01",
            "stop by any time!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_9DA8")

    label("loc_9D20")


    ChrTalk(    #328
        0x15,
        "Ahhhhh, they finally got the lights working!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x15,
        (
            "Well! Now that we've got some lights,\x01",
            "time to shake off the sad and get to\x01",
            "work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DA8")

    Jump("loc_A7BC")

    label("loc_9DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_A100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EDE")
    TurnDirection(0x15, 0x10B, 0)

    ChrTalk(    #330
        0x15,
        "Ah... Josette, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x15,
        (
            "I think I've got some armor that'd be\x01",
            "just right for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x15,
        (
            "Be sure and check your equipment before\x01",
            "you head back to your ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x10B,
        (
            "#211FHaha! Thanks! That's nice of you!\x02\x03",

            "All right, then, man, make with the selling!\x01",
            "Come at me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22C5)
    Jump("loc_9FE2")

    label("loc_9EDE")


    ChrTalk(    #334
        0x15,
        (
            "You're looking for that bandit lady's\x01",
            "brothers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x15,
        (
            "Be sure to look over her gear if you're\x01",
            "going to take her along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x15,
        (
            "Be sure and check her armor,\x01",
            "specifically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x15,
        (
            "Gun users have a bad habit of not wearing\x01",
            "much in the way of defensive gear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FE2")

    OP_A2(0x9)
    Jump("loc_A0FD")

    label("loc_9FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A056")
    TurnDirection(0x15, 0x10B, 0)

    ChrTalk(    #338
        0x15,
        (
            "I'm sure I've got something that'd suit\x01",
            "her perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x15,
        "Please, take a look!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0FD")

    label("loc_A056")


    ChrTalk(    #340
        0x15,
        (
            "Be sure to look over that bandit lady's\x01",
            "gear if you're going to take her along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x15,
        (
            "Gun users have a bad habit of not wearing\x01",
            "much in the way of defensive gear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0FD")

    Jump("loc_A7BC")

    label("loc_A100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_A20C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1A3")

    ChrTalk(    #342
        0x15,
        (
            "Ahhhh, it's wonderful to have my tools\x01",
            "working again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x15,
        "I can finally grind some quartz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x15,
        "Right! You need anything, just tell me!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_A209")

    label("loc_A1A3")


    ChrTalk(    #345
        0x15,
        (
            "It's been a while since I've been able\x01",
            "to work with quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x15,
        "If you need anything, just ask.\x02",
    )

    CloseMessageWindow()

    label("loc_A209")

    Jump("loc_A7BC")

    label("loc_A20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_A38C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E2")

    ChrTalk(    #347
        0x15,
        (
            "One tower left... The mission will be in\x01",
            "the bag after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x15,
        (
            "They've probably got one hell of a\x01",
            "fight left for the finale, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x15,
        (
            "Make sure you give your equipment\x01",
            "a once-over.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_A389")

    label("loc_A2E2")


    ChrTalk(    #350
        0x15,
        (
            "One tower left... The mission will be in\x01",
            "the bag after this. They've probably got\x01",
            "a surprise waiting, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x15,
        (
            "Make sure you give your equipment\x01",
            "a once-over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A389")

    Jump("loc_A7BC")

    label("loc_A38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_A56D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4F6")

    ChrTalk(    #352
        0x15,
        "Hello, everyone, good work so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x15,
        (
            "It seems the professor's research is\x01",
            "stuck on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x15,
        (
            "The researchers just went out for a\x01",
            "quick break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x15,
        (
            "You can't really make progress at\x01",
            "anything if you just keep flogging away\x01",
            "at something when you're stuck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x15,
        (
            "Maybe you guys could use a little time\x01",
            "in the break room, as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_A56A")

    label("loc_A4F6")


    ChrTalk(    #357
        0x15,
        (
            "It seems the professor's research is\x01",
            "stuck on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x15,
        (
            "The researchers just went out for a\x01",
            "quick break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A56A")

    Jump("loc_A7BC")

    label("loc_A56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_A71C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A66E")

    ChrTalk(    #359
        0x15,
        (
            "The professor seems busy with his\x01",
            "research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x15,
        (
            "I took a look at the blueprints for what\x01",
            "the professor is working on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x15,
        (
            "Unfortunately, I couldn't understand any\x01",
            "of it. Cutting-edge research really is\x01",
            "mind-blowing, sometimes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_A719")

    label("loc_A66E")


    ChrTalk(    #362
        0x15,
        (
            "The equipment the professor's researching\x01",
            "seems incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x15,
        (
            "Unfortunately, I couldn't figure out what\x01",
            "it's supposed to DO, even after looking\x01",
            "at the blueprints!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A719")

    Jump("loc_A7BC")

    label("loc_A71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_A7BC")

    ChrTalk(    #364
        0x15,
        (
            "If you need to tune your orbment or\x01",
            "fabricate quartz, come see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x15,
        (
            "I've also got weapons and armor,\x01",
            "so I should have most everything you\x01",
            "need!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7BC")

    TalkEnd(0x15)
    Return()

    # Function_18_98C8 end

    def Function_19_A7C0(): pass

    label("Function_19_A7C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_A881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A841")

    ChrTalk(    #366
        0xFE,
        "Setting orbal engine output to 50%.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "Orbal voltage steady...\x01",
            "We can start the test at any time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_A881")

    label("loc_A841")


    ChrTalk(    #368
        0xFE,
        (
            "Output to 50%...\x01",
            "Orbal voltage steady, no problems at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A881")

    TalkEnd(0xFE)
    Return()

    # Function_19_A7C0 end

    def Function_20_A885(): pass

    label("Function_20_A885")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A8EB"),
        (1, "loc_AB4B"),
        (2, "loc_AB84"),
        (SWITCH_DEFAULT, "loc_AB87"),
    )


    label("loc_A8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAF8")

    ChrTalk(    #369
        0x9,
        (
            "#023FAh, Estelle, everyone.\x01",
            "You haven't left yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        "#1015FNope, we're still getting ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x102,
        "#1040FDeigning to clean up the room, Schera?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #372
        0x9,
        (
            "#020FFor now, yes. Alas, fie and all that.\x02\x03",

            "Unfortunately, I'm hardly able to help\x01",
            "with fine engine repair, so all I can do\x01",
            "is stand on the sidelines.\x02\x03",

            "#525FHey, THERE'S an idea, though.\x01",
            "I DO have a whip, perhaps I should get\x01",
            "out there and...be motivational?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x101,
        "#1001FHahaha! I think that's a great idea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x102,
        "#1048FP-Please be gentle, at least...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22C3)
    Jump("loc_AB48")

    label("loc_AAF8")


    ChrTalk(    #375
        0x9,
        (
            "#020FNow, then...what to do.\x02\x03",

            "I do wish there was some way\x01",
            "I could help...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB48")

    Jump("loc_AB8A")

    label("loc_AB4B")


    ChrTalk(    #376
        0x9,
        "#020FShall I join the traveling party, then?\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_AB8A")

    label("loc_AB84")

    Jump("loc_AB8A")

    label("loc_AB87")

    Jump("loc_AB8A")

    label("loc_AB8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_A885 end

    def Function_21_AB8E(): pass

    label("Function_21_AB8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_AC05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_END)), "loc_ABC0")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    Jump("loc_AC02")

    label("loc_ABC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_ABE7")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_AC02")

    label("loc_ABE7")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_AC02")

    Jump("loc_AC83")

    label("loc_AC05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_AC28")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_AC83")

    label("loc_AC28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_AC49")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_AC83")

    label("loc_AC49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_AC6A")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_AC83")

    label("loc_AC6A")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_AC83")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_ADDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACD9")
    SetChrPos(0xB, -2830, 0, 65940, 90)
    ClearChrFlags(0xB, 0x80)

    label("loc_ACD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACFC")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_ACFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD27")
    SetChrPos(0x9, -5340, 0, 59510, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_AD27")

    Jump("loc_ADDA")

    label("loc_AD2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD35")
    Jump("loc_ADDA")

    label("loc_AD35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD60")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_AD60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD83")
    SetChrPos(0xB, -3510, 0, 5330, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_AD83")

    Jump("loc_ADDA")

    label("loc_AD86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ADA9")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_ADA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ADDA")
    OP_44(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 15)
    SetChrPos(0xA, 61300, 250, -40950, 0)

    label("loc_ADDA")

    Jump("loc_AEF7")

    label("loc_ADDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_AE2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE07")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_AE07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE2A")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_AE2A")

    Jump("loc_AEF7")

    label("loc_AE2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_AE7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE57")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_AE57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE7A")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_AE7A")

    Jump("loc_AEF7")

    label("loc_AE7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_AEAA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AEA7")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_AEA7")

    Jump("loc_AEF7")

    label("loc_AEAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_AEF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AED4")
    SetChrPos(0xB, -4420, 0, 62290, 225)
    ClearChrFlags(0xB, 0x80)

    label("loc_AED4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AEF7")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_AEF7")

    OP_0D()
    Return()

    # Function_21_AB8E end

    def Function_22_AEF9(): pass

    label("Function_22_AEF9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF1E")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_AF1E")

    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    OP_4A(0x8, 255)

    def lambda_AFAE():

        label("loc_AFAE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AFAE")

    QueueWorkItem2(0x101, 1, lambda_AFAE)

    def lambda_AFBF():

        label("loc_AFBF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AFBF")

    QueueWorkItem2(0x102, 1, lambda_AFBF)

    def lambda_AFD0():

        label("loc_AFD0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AFD0")

    QueueWorkItem2(0xF8, 1, lambda_AFD0)

    def lambda_AFE1():

        label("loc_AFE1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AFE1")

    QueueWorkItem2(0xF9, 1, lambda_AFE1)
    OP_0D()
    TurnDirection(0x8, 0x101, 400)
    Sleep(700)

    ChrTalk(    #377
        0x8,
        (
            "#101FAh! Good timing!\x02\x03",

            "I just got all those data crystals you\x01",
            "brought me into Capel.\x02\x03",

            "Now we just need to wait for Capel to\x01",
            "finish analyzing them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x101,
        "#1011F#4PCool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x102,
        "#1040FDo you know how long it will take?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        (
            "#100FMmmmm... it will depend greatly on the\x01",
            "damage to each crystal. I'd really be\x01",
            "guessing.\x02\x03",

            "In the worst case, it could be a several-\x01",
            "day wait, so for now, try to be patient,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x102,
        "#1040FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x101,
        (
            "#1015F#4PNo point in worrying about it,\x01",
            "then, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x8,
        (
            "#100FIf you find any more crystals,\x01",
            "bring them to me.\x02\x03",

            "I'll get them set into Capel and begin\x01",
            "analyzing them immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFC4A, 0x0, 0xFF6E, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    OP_4B(0x8, 255)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    ClearChrFlags(0x8, 0x10)
    OP_65(0x0, 0x1)
    OP_A2(0x1E0B)
    EventEnd(0x0)
    Return()

    # Function_22_AEF9 end

    def Function_23_B29D(): pass

    label("Function_23_B29D")


    ChrTalk(    #384
        0x8,
        (
            "#101FAh, you found a new data crystal,\x01",
            "did you?\x02\x03",

            "Let's get it set into Capel and start\x01",
            "the auto-analysis program!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x101,
        "#1006FThanks!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #386
        "\x07\x05Estelle handed over all the data crystals they found.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x3FE, 1)
    OP_3F(0x3FF, 1)
    OP_3F(0x400, 1)
    OP_3F(0x401, 1)
    OP_3F(0x402, 1)
    OP_3F(0x403, 1)
    OP_3F(0x404, 1)
    OP_3F(0x405, 1)
    OP_3F(0x406, 1)
    OP_3F(0x407, 1)
    OP_3F(0x408, 1)
    OP_3F(0x409, 1)
    OP_3F(0x412, 1)
    OP_3F(0x413, 1)
    OP_3F(0x414, 1)
    Return()

    # Function_23_B29D end

    def Function_24_B3CC(): pass

    label("Function_24_B3CC")

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
            "Chose Schera as your partner\x01",      # 0
            "Chose Agate as your partner\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B44F"),
        (1, "loc_B455"),
        (SWITCH_DEFAULT, "loc_B45B"),
    )


    label("loc_B44F")

    OP_A2(0x1200)
    Jump("loc_B45B")

    label("loc_B455")

    OP_A2(0x1201)
    Jump("loc_B45B")

    label("loc_B45B")

    Return()

    # Function_24_B3CC end

    def Function_25_B45C(): pass

    label("Function_25_B45C")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_25_B45C end

    def Function_26_B4E9(): pass

    label("Function_26_B4E9")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(3300, 2800, 6000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B547")
    Call(0, 24)
    Call(0, 25)

    label("loc_B547")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x8, -1060, 150, 7570, 0)
    OP_4A(0x8, 255)

    def lambda_B576():
        OP_6D(1600, 0, 1900, 4500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B576)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x1, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x1F)
    OP_0D()
    OP_43(0x8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_4A(0x12, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_B5EF():

        label("loc_B5EF")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_B5EF")

    QueueWorkItem2(0x8, 1, lambda_B5EF)
    Sleep(1000)

    ChrTalk(    #387
        0x8,
        "#103FAh, everyone. Good timing!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_B63C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B63C)
    Sleep(120)

    def lambda_B64F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B64F)

    def lambda_B65D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B65D)
    Sleep(120)

    def lambda_B670():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B670)

    ChrTalk(    #388
        0x101,
        "#1011F#4PHi, Professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x102,
        "#1044F#4PDid you want us for something?\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x20)

    def lambda_B6CF():
        OP_6D(-260, 0, 4050, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B6CF)

    def lambda_B6E7():
        OP_67(0, 7140, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B6E7)

    def lambda_B6FF():
        OP_6B(2680, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B6FF)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x21)
    Sleep(400)
    OP_43(0xF8, 0x1, 0x0, 0x22)
    Sleep(600)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #390
        0x8,
        (
            "#100FYes, actually.\x02\x03",

            "We found something quite interesting in\x01",
            "our analysis of the data crystal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        "#1015F#6PReally? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x8,
        (
            "#104FWell, we've verified that ancient orbments used\x01",
            "quartz, or something similar enough, at any rate.\x02\x03",

            "#100FAnd with the data from the crystal,\x01",
            "we've found a way to put those ancient\x01",
            "quartz into modern orbments!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8E3")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #393
        0x107,
        "#064F#4PR-Really, Grandpa?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B923")

    label("loc_B8E3")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #394
        0x101,
        "#1004F#6PSeriously? Holy crap!\x02",
    )

    CloseMessageWindow()

    label("loc_B923")


    ChrTalk(    #395
        0x8,
        (
            "#101FHeh heh! Remember who you're speaking to!\x02\x03",

            "#100F...There's one problem, though.\x01",
            "The slots on your orbments, as designed,\x01",
            "won't be able to take the quartz.\x02\x03",

            "You'll need to modify the slots further...\x01",
            "A 'level 3' upgrade, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x102,
        (
            "#1044F#4PSo what you're saying is...\x02\x03",

            "We can now upgrade our orbments even further?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x8,
        (
            "#100FExactly so!\x02\x03",

            "I've told Payton what kind of modifications\x01",
            "need to be made, so talk to him when\x01",
            "you're ready.\x02\x03",

            "And if you find any quartz like that in\x01",
            "'the wild,' give it a try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x101,
        "#1006F#6PYeah, you bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x102,
        "#1040F#4PWe'll definitely make use of that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBD9")

    ChrTalk(    #400
        0x8,
        (
            "#100FI'm going to keep puttering around here.\x02\x03",

            "Take care of Tita, you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC31")

    label("loc_BBD9")


    ChrTalk(    #401
        0x8,
        (
            "#100FI'm going to keep puttering around here.\x02\x03",

            "Good luck investigating that tower!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC31")

    OP_8E(0x8, 0xFFFFFBDC, 0x96, 0x1D92, 0x7D0, 0x0)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(500)
    SetChrPos(0x8, -950, 0, 65390, 0)
    OP_4B(0x8, 255)
    OP_A2(0x12)
    OP_A2(0x1E4D)
    Fade(500)
    OP_6D(-1060, 0, 2880, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1060, 0, 2880, 180)
    SetChrPos(0x1, -1060, 0, 2880, 180)
    SetChrPos(0x2, -1060, 0, 2880, 180)
    SetChrPos(0x3, -1060, 0, 2880, 180)
    OP_43(0x12, 0x1, 0x0, 0x2A)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_26_B4E9 end

    def Function_27_BD07(): pass

    label("Function_27_BD07")

    Sleep(500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFBDC, 0x0, 0x11C6, 0x7D0, 0x0)
    Return()

    # Function_27_BD07 end

    def Function_28_BD34(): pass

    label("Function_28_BD34")

    SetChrPos(0xFE, 2700, 800, 4000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_28_BD34 end

    def Function_29_BD73(): pass

    label("Function_29_BD73")

    SetChrPos(0xFE, 2700, 1800, 5000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_29_BD73 end

    def Function_30_BDB2(): pass

    label("Function_30_BDB2")

    SetChrPos(0xFE, 3400, 1800, 4500, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF254, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_30_BDB2 end

    def Function_31_BDF1(): pass

    label("Function_31_BDF1")

    SetChrPos(0xFE, 3400, 2800, 5500, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF254, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_31_BDF1 end

    def Function_32_BE30(): pass

    label("Function_32_BE30")

    OP_44(0x8, 0x1)

    def lambda_BE3A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BE3A)
    OP_8E(0xFE, 0xFFFFF9C0, 0x0, 0xD52, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_32_BE30 end

    def Function_33_BE5E(): pass

    label("Function_33_BE5E")

    OP_8E(0xFE, 0xFFFFFDC6, 0x0, 0xD52, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_33_BE5E end

    def Function_34_BE7A(): pass

    label("Function_34_BE7A")

    OP_8E(0xFE, 0xFFFFF8EE, 0x0, 0x96A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_BE7A end

    def Function_35_BE96(): pass

    label("Function_35_BE96")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x96A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_35_BE96 end

    def Function_36_BEB2(): pass

    label("Function_36_BEB2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #402
        0x8,
        (
            "#100FHm? You look like a woman with a purpose,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x101,
        (
            "#1011FYeah, I am, sorta. There's something we'd\x01",
            "like for you to look at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x102,
        "#1040FIt's this, specifically.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #405
        "\x07\x00You handed over #1048i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x418, 1)

    ChrTalk(    #406
        0x8,
        (
            "#100FAh, a data crystal!\x02\x03",

            "Hmmmmm. I don't actually see any\x01",
            "damage to it...\x02\x03",

            "#101FGive me a moment.\x01",
            "Analyzing this shouldn't take long!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    SetChrPos(0x8, -5200, 0, 65530, 0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(2000)
    OP_63(0x8)

    ChrTalk(    #407
        0x8,
        "#103FI see! Incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x101,
        "#1004FUh, what does it say?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #409
        0x8,
        (
            "#100FIt contains schematics for advanced personal\x01",
            "weaponry for the Ark residents.\x02\x03",

            "They seem to require a specific 'Zemurian Ore'\x01",
            "in their construction...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C340")

    ChrTalk(    #410
        0x101,
        (
            "#1015FZemurian Ore...\x01",
            "Wait, I've heard of that before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x102,
        (
            "#6P#1042FThat's right! Remember?\x02\x03",

            "#1040FThe owner of the cafe in Grancel claimed the\x01",
            "strange metal he gave us was 'Zemurian Ore.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        (
            "#1004FOh, right!\x02\x03",

            "#1001FThis weirdo hunk of metal, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3B1")

    label("loc_C340")


    ChrTalk(    #413
        0x101,
        (
            "#1015FZemurian Ore...\x01",
            "We might actually have some of that.\x02\x03",

            "#1001FIs it this weirdo hunk of metal we found?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3B1")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #414
        "\x07\x00You gave Russell the #1047i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #415
        0x8,
        (
            "#103FHow fortuitous! Yes, indeed, I believe\x01",
            "this is what we need!\x02\x03",

            "#101FWell! This makes things easy, then!\x02\x03",

            "#100FI should be able to make something\x01",
            "right away with our equipment, now\x01",
            "that I have the plans.\x02\x03",

            "You do have a choice to make first,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x101,
        "#1015FA choice? On what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x8,
        (
            "#100FWe have schematics for nine separate\x01",
            "weapons here, you see...\x02\x03",

            "But the designs require so much metal\x01",
            "that I think we can build only one weapon\x01",
            "per piece of ore you find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        (
            "#1004FReally?\x02\x03",

            "#1007FOooooh, that's a hard choice, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x8,
        (
            "#100FI'll leave the choice in your hands.\x02\x03",

            "#101FNow! What would you like to make first?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(30, 10, -1, -1)

    AnonymousTalk(    #420
        "\x06\x18\x07\x05Which weapon do you wish to make?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        330,
        50,
        0,
        (
            "Qilin Horn - Staff\x01",                    # 0
            "Phoenix Blades - Dual-blades\x01",          # 1
            "Sirius Whip - Whip\x01",                    # 2
            "Eternity - Pistol\x01",                     # 3
            "Moon Singer - Rapier\x01",                  # 4
            "Demon Eater - Greatsword\x01",              # 5
            "Kowloon - Cannon\x01",                      # 6
            "Thousand-Hands Kanon - Gauntlets\x01",      # 7
            "Glittering Stars - Crossbow\x01",           # 8
            "Quit\x01",                                  # 9
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Call(0, 37)
    OP_A2(0x22B1)
    Return()

    # Function_36_BEB2 end

    def Function_37_C7AE(): pass

    label("Function_37_C7AE")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C7E8"),
        (1, "loc_C7E8"),
        (2, "loc_C7E8"),
        (3, "loc_C7E8"),
        (4, "loc_C7E8"),
        (5, "loc_C7E8"),
        (6, "loc_C7E8"),
        (7, "loc_C7E8"),
        (8, "loc_C7E8"),
        (9, "loc_CC61"),
        (SWITCH_DEFAULT, "loc_CD76"),
    )


    label("loc_C7E8")


    ChrTalk(    #421
        0x8,
        "#100FRight, then! I'll get right on it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(2000)
    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    SetChrPos(0x8, -950, 0, 65390, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #422
        0x8,
        "#101FAll right! It's done!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C912")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #423
        "\x07\x00Received #027i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1B, 1)
    Jump("loc_CBD2")

    label("loc_C912")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #424
        "\x07\x00Received #049i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x31, 1)
    Jump("loc_CBD2")

    label("loc_C96A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9C2")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #425
        "\x07\x00Received #079i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4F, 1)
    Jump("loc_CBD2")

    label("loc_C9C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA1A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #426
        "\x07\x00Received #104i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x68, 1)
    Jump("loc_CBD2")

    label("loc_CA1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA72")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #427
        "\x07\x00Received #133i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x85, 1)
    Jump("loc_CBD2")

    label("loc_CA72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CACA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #428
        "\x07\x00Received #169i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0xA9, 1)
    Jump("loc_CBD2")

    label("loc_CACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB22")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #429
        "\x07\x00Received #192i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0xC0, 1)
    Jump("loc_CBD2")

    label("loc_CB22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB7A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #430
        "\x07\x00Received #221i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0xDD, 1)
    Jump("loc_CBD2")

    label("loc_CB7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD2")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #431
        "\x07\x00Received #231i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0xE7, 1)
    Jump("loc_CBD2")

    label("loc_CBD2")

    OP_3F(0x417, 1)

    ChrTalk(    #432
        0x101,
        "#1001FThanks, Professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x102,
        "#1040FWe'll definitely make good use of this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x8,
        (
            "#100FYes, well, be careful out there,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD76")

    label("loc_CC61")


    ChrTalk(    #435
        0x101,
        (
            "#1016FUm... This is kind of a hard choice.\x01",
            "Do you mind waiting a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x8,
        (
            "#100FNot at all. You should think hard about this.\x01",
            "Think it over and come back to me.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_6D(-2960, 0, 62700, 0)
    SetChrPos(0x8, -950, 0, 65390, 0)
    SetChrPos(0x101, -2960, 0, 62700, 0)
    SetChrPos(0x102, -2960, 0, 62700, 0)
    SetChrPos(0xF8, -2960, 0, 62700, 0)
    SetChrPos(0xF9, -2960, 0, 62700, 0)
    OP_0D()
    Jump("loc_CD76")

    label("loc_CD76")

    EventEnd(0x0)
    Return()

    # Function_37_C7AE end

    def Function_38_CD79(): pass

    label("Function_38_CD79")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #437
        0x8,
        (
            "#100FHm? You look like a woman with a purpose,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#1011FYeah, I am, sorta. There's something\x01",
            "we'd like for you to look at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x102,
        "#1040FIt's this, specifically.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #440
        "\x07\x00You handed over #1048i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x418, 1)

    ChrTalk(    #441
        0x8,
        (
            "#100FAh, a data crystal!\x02\x03",

            "Hmmmmm. I don't actually see any\x01",
            "damage to it...\x02\x03",

            "#101FGive me a moment.\x01",
            "Analyzing this shouldn't take long!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    SetChrPos(0x8, -5200, 0, 65530, 0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #442
        0x8,
        "#103FI see! Incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x101,
        "#1004FUh, what does it say?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #444
        0x8,
        (
            "#100FIt contains schematics for advanced personal\x01",
            "weaponry for the Ark residents.\x02\x03",

            "They seem to require a specific 'Zemurian Ore'\x01",
            "in their construction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1015FZemurian Ore...\x01",
            "Wait, I've heard of that before.\x02\x03",

            "#1001FIs it this weirdo hunk of metal we found?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #446
        "\x07\x00You gave Russell the #1047i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x417, 2)

    ChrTalk(    #447
        0x8,
        (
            "#103FHow fortuitous! Yes, indeed, I believe\x01",
            "this is what we need!\x02\x03",

            "#101FWell! This makes things easy, then!\x02\x03",

            "#100FI should be able to make something\x01",
            "quickly with the equipment we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x101,
        "#1001FReally?! Then don't let us stop you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x8,
        "#100FRight, just a moment, now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22B1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(2000)
    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    SetChrPos(0x8, -950, 0, 65390, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #450
        0x8,
        "#101FAll right! It's done!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #451
        "\x07\x00Received #027i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #452
        "\x07\x00Received #049i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x31, 1)
    OP_3E(0x1B, 1)

    ChrTalk(    #453
        0x101,
        "#1001FThanks, Professor Russell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x102,
        (
            "#1040FWe'll definitely make good use\x01",
            "of these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0x8,
        (
            "#100FYes, well, be careful out there,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    EventEnd(0x0)
    Return()

    # Function_38_CD79 end

    def Function_39_D46A(): pass

    label("Function_39_D46A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #456
        "\x07\x05Engine Room ※No Trespassing\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_D46A end

    def Function_40_D4B9(): pass

    label("Function_40_D4B9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53F")
    SoundLoad(13)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_D53F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D559")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_D559")

    Return()

    # Function_40_D4B9 end

    def Function_41_D55B(): pass

    label("Function_41_D55B")

    Call(0, 18)
    Return()

    # Function_41_D55B end

    def Function_42_D560(): pass

    label("Function_42_D560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D569")
    Return()

    label("loc_D569")

    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_4A(0x12, 0)
    Sleep(2000)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    OP_4B(0x12, 0)
    Return()

    # Function_42_D560 end

    SaveToFile()

Try(main)
