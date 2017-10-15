from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60010",
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
        'Passenger',                            # 9
        'Passenger',                            # 10
        'Passenger',                            # 11
        'Passenger',                            # 12
        'Passenger',                            # 13
        'Passenger',                            # 14
        'Passenger',                            # 15
        'Passenger',                            # 16
        'Passenger',                            # 17
        'Passenger',                            # 18
        'Passenger',                            # 19
        'Passenger',                            # 20
        'Alan',                                 # 21
        'Father Kevin',                         # 22
        'Airliner, Cecilia',                    # 23
        'セシリア号影',                         # 24
        'Airliner, Cecilia',                    # 25
        'Bridge',                               # 26
        'Skip',                                 # 27
        'Fabree',                               # 28
        'Tico',                                 # 29
        'Morie',                                # 30
        'Passenger',                            # 31
        'Passenger',                            # 32
        'Passenger',                            # 33
        'Warrant Officer Dyne',                 # 34
        'Captain Grandt',                       # 35
        'Crew Mem. Clare',                      # 36
        'Crew Mem. Timon',                      # 37
        'Anton',                                # 38
        'Ricky',                                # 39
        'Linde Passenger',                      # 40
        'Linde Passenger',                      # 41
        'Rolent',                               # 42
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
        'ED6_DT07/CH01200 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01290 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT07/CH01300 ._CH',             # 0C
        'ED6_DT07/CH01440 ._CH',             # 0D
        'ED6_DT07/CH01540 ._CH',             # 0E
        'ED6_DT07/CH01460 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01200P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01290P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT07/CH01300P._CP',             # 0C
        'ED6_DT07/CH01440P._CP',             # 0D
        'ED6_DT07/CH01540P._CP',             # 0E
        'ED6_DT07/CH01460P._CP',             # 0F
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 36100,
        Z                   = 0,
        Y                   = 35620,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44350,
        Z                   = 4000,
        Y                   = 39550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 31840,
        Z                   = 0,
        Y                   = 51530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 39680,
        Z                   = 4000,
        Y                   = 35470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39680,
        Z                   = 4000,
        Y                   = 36730,
        Direction           = 180,
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
        X                   = 36520,
        Z                   = 0,
        Y                   = 33790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 37790,
        Z                   = 0,
        Y                   = 32820,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35870,
        Z                   = 0,
        Y                   = 32330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 43580,
        Z                   = 4000,
        Y                   = 30220,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 44340,
        Z                   = 4000,
        Y                   = 35280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 42290,
        Z                   = 4000,
        Y                   = 31720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 45360,
        Z                   = 4000,
        Y                   = 54040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 45360,
        Z                   = 4000,
        Y                   = 55190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 36820,
        Z                   = 0,
        Y                   = 27490,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 33120,
        Z                   = 0,
        Y                   = 30640,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
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


    DeclActor(
        TriggerX            = 36142,
        TriggerZ            = 0,
        TriggerY            = 34342,
        TriggerRange        = 1000,
        ActorX              = 36095,
        ActorZ              = 1500,
        ActorY              = 35619,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5FA",          # 00, 0
        "Function_1_6F8",          # 01, 1
        "Function_2_7FA",          # 02, 2
        "Function_3_977",          # 03, 3
        "Function_4_99B",          # 04, 4
        "Function_5_9A0",          # 05, 5
        "Function_6_24B5",         # 06, 6
        "Function_7_29CE",         # 07, 7
        "Function_8_3157",         # 08, 8
        "Function_9_327B",         # 09, 9
        "Function_10_340A",        # 0A, 10
        "Function_11_349C",        # 0B, 11
        "Function_12_362D",        # 0C, 12
        "Function_13_366F",        # 0D, 13
        "Function_14_37CE",        # 0E, 14
        "Function_15_3858",        # 0F, 15
        "Function_16_3A04",        # 10, 16
        "Function_17_3E6E",        # 11, 17
        "Function_18_40B7",        # 12, 18
        "Function_19_43AC",        # 13, 19
        "Function_20_4565",        # 14, 20
        "Function_21_4743",        # 15, 21
        "Function_22_5041",        # 16, 22
        "Function_23_50A0",        # 17, 23
        "Function_24_50F3",        # 18, 24
        "Function_25_57AC",        # 19, 25
        "Function_26_580F",        # 1A, 26
        "Function_27_5872",        # 1B, 27
        "Function_28_58D5",        # 1C, 28
        "Function_29_5931",        # 1D, 29
        "Function_30_5994",        # 1E, 30
        "Function_31_59F7",        # 1F, 31
        "Function_32_5A5A",        # 20, 32
        "Function_33_6825",        # 21, 33
        "Function_34_686C",        # 22, 34
        "Function_35_68C7",        # 23, 35
        "Function_36_6936",        # 24, 36
        "Function_37_6AA4",        # 25, 37
        "Function_38_6B75",        # 26, 38
        "Function_39_6C30",        # 27, 39
        "Function_40_6CBE",        # 28, 40
    )


    def Function_0_5FA(): pass

    label("Function_0_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_618")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_6C7")

    label("loc_618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_622")
    Jump("loc_6C7")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_66B")
    SetChrPos(0x1B, 42670, 4000, 39780, 90)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    SetChrPos(0x14, 43140, 4000, 38650, 45)
    SetChrPos(0x1A, 44350, 4000, 39550, 270)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_6C7")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_69F")
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 36940, 0, 31150, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_6C7")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_6C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B3")
    SetChrFlags(0x14, 0x10)

    label("loc_6B3")

    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6E6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_6F7")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_6F7")

    Return()

    # Function_0_5FA end

    def Function_1_6F8(): pass

    label("Function_1_6F8")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x230007)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74C")
    OP_B5(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_737")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_74C")

    label("loc_737")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_74C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77B")
    OP_A1(0x18, 0xB)
    SetChrPos(0x18, 56000, -3075, 35200, 0)
    OP_72(0xB, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_7E4")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_794")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_7E4")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_7E4")
    OP_71(0xB, 0x4)
    OP_72(0xF, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 56000, -3075, 35200, 0)
    OP_72(0xC, 0x4)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7EE")
    Jump("loc_7F9")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7F9")
    OP_64(0x0, 0x1)

    label("loc_7F9")

    Return()

    # Function_1_6F8 end

    def Function_2_7FA(): pass

    label("Function_2_7FA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_961")

    label("loc_81F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_961")

    label("loc_838")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_961")

    label("loc_851")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_961")

    label("loc_86A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_883")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_961")

    label("loc_883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_961")

    label("loc_89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_961")

    label("loc_8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_961")

    label("loc_8CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_961")

    label("loc_8E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_961")

    label("loc_900")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_961")

    label("loc_919")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_961")

    label("loc_932")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_961")

    label("loc_94B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_961")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_976")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_961")

    label("loc_976")

    Return()

    # Function_2_7FA end

    def Function_3_977(): pass

    label("Function_3_977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99A")
    OP_8D(0xFE, 29021, 54795, 33637, 48557, 2000)
    Jump("Function_3_977")

    label("loc_99A")

    Return()

    # Function_3_977 end

    def Function_4_99B(): pass

    label("Function_4_99B")

    Call(0, 5)
    Return()

    # Function_4_99B end

    def Function_5_9A0(): pass

    label("Function_5_9A0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_117D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE3")

    ChrTalk(    #0
        0x14,
        "Yo, Estelle, J.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        "Back again, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000FYup.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1040FIt IS somehow comforting to see you\x01",
            "in the same place as always, Alan.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 400)

    ChrTalk(    #4
        0x14,
        (
            "Yeah, well. I'd LIKE to say it's business\x01",
            "as usual and I just spend my days\x01",
            "tallyin' the score...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14,
        (
            "But with the airships the way they are,\x01",
            "I'm exhausted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1007FYeah, I'll bet...\x02\x03",

            "Gotta explain to a lot of angry customers\x01",
            "why they can't go anywhere now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1035FThat sort of thing is always a bed\x01",
            "of thorns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14,
        (
            "Well, yeah, that parks sucks a lot,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14,
        (
            "More importantly, no airships means\x01",
            "I can't keep score! Girls are scarce\x01",
            "enough around here! I need tourists!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x14,
        (
            "And that's the only part of this job I\x01",
            "even enjoy! Aidios, have mercy...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x102,
        (
            "#1048FYou really HAVEN'T changed at all,\x01",
            "have you, Alan?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20A7)
    Jump("loc_117A")

    label("loc_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DA9")

    ChrTalk(    #12
        0x14,
        (
            "Sure, dealing with the customers\x01",
            "is hard, but the real problem is there\x01",
            "aren't any girls!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x14,
        (
            "The girls are the only reason I like this\x01",
            "job! Aidios, have mercy! Send me some\x01",
            "honeys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117A")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1F")

    ChrTalk(    #14
        0x14,
        (
            "The engineers are going over the ship,\x01",
            "but they haven't found anything out of\x01",
            "the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "At times like this, all you can do is sit\x01",
            "back and watch the pretty ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1019F(Alan's perverseness: one of the dark\x01",
            "constants of the universe.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        "Oh, that girl over there's kinda cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14,
        (
            "Mmm... Still, 78 points. She's got a\x01",
            "ways to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_F99")

    label("loc_F1F")


    ChrTalk(    #19
        0x14,
        "Oh, that girl over there's kinda cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "Mmm, still, 78 points. Not cute enough\x01",
            "to rate all that high in my book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F99")

    Jump("loc_117A")

    label("loc_F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9")

    ChrTalk(    #21
        0x14,
        (
            "The airship currently docked is the\x01",
            "usually-southbound Linde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x14,
        (
            "The orbments stopped working moments\x01",
            "before it was going to take off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14,
        (
            "It was pretty crazy, securing lodging and\x01",
            "everything for our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        (
            "I know the company is hurting from all\x01",
            "the trouble we've been having lately...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_117A")

    label("loc_10D9")


    ChrTalk(    #25
        0x14,
        (
            "The airship currently docked is the\x01",
            "usually-southbound Linde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x14,
        (
            "Thanks to what's happening, it can't\x01",
            "leave the dock, so it's on a layover with\x01",
            "its crew.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_24B1")

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1190")
    Call(0, 32)
    Jump("loc_24B1")

    label("loc_1190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_12C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1205")

    ChrTalk(    #27
        0x14,
        (
            "The staff is getting ready to pack it in\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14,
        "Can't really do anything in this fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C6")

    label("loc_1205")


    ChrTalk(    #29
        0x14,
        (
            "We had customers who came this\x01",
            "morning, trying to go home. We had\x01",
            "to turn them away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14,
        (
            "The staff is getting ready to pack it in\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x14,
        "Can't really do anything in this fog.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_12C6")

    Jump("loc_24B1")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1355")

    ChrTalk(    #32
        0x14,
        (
            "We do not have a date for when service\x01",
            "will resume!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        (
            "W-We're very sorry, and we thank you\x01",
            "for your understanding!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1424")

    label("loc_1355")


    ChrTalk(    #34
        0x14,
        (
            "W-We're very sorry, but airship service\x01",
            "has not yet resumed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14,
        "We thank you for your continued patience!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14,
        (
            "As a representative of the Liberl Orbalship\x01",
            "Company, I offer our sincerest apologies!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1424")

    Jump("loc_24B1")

    label("loc_1427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 2)), scpexpr(EXPR_END)), "loc_156F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14B8")

    ChrTalk(    #37
        0x14,
        (
            "The Jenis uniform is cute no matter how\x01",
            "many times I see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "Ahhhh! It was worth wadin' through the\x01",
            "fog today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156C")

    label("loc_14B8")


    ChrTalk(    #39
        0x14,
        (
            "If our scheduled airships are out of\x01",
            "service, that means I won't be seeing\x01",
            "any girls for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        (
            "...\x01",
            "...This is the greatest damned crisis\x01",
            "Rolent has faced in a decade!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156C")

    Jump("loc_2215")

    label("loc_156F")


    ChrTalk(    #41
        0x14,
        "72, 80, 75... Eh, today's okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1813")
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x14, 0x105, 400)
    Sleep(1000)

    ChrTalk(    #42
        0x14,
        "Oh... OH... Blue socks worn high...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x14,
        "...and...a tidy, trim, elegant white skirt?\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x14,
        (
            "AM I DREAMING?! Th-Th-This is the\x01",
            "Jenis Royal Academy uniform!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x14,
        (
            "And you've got the perfect air of\x01",
            "refinement to match!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "Milady! You're incredible! A perfect 100!\x01",
            "No question!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #47
        0x105,
        "#542FUm... Thank you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007FFor the love of Aidios, leave Kloe alone,\x01",
            "you maniac. You have no idea what\x01",
            "you're even doing.\x02\x03",

            "#1019FYou're never going to change your spots,\x01",
            "are you? Maybe I'LL change something...\x01",
            "Like your face. With my staff.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1F4D")

    label("loc_1813")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_182C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1845")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_1845")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_185E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1877")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_1877")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1890")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_1890")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A9")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_18A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_18C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18F1")

    label("loc_18DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (2, "loc_1906"),
        (6, "loc_1B73"),
        (0, "loc_1DB2"),
        (SWITCH_DEFAULT, "loc_1F4D"),
    )


    label("loc_1906")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x103, 400)
    Sleep(1000)

    ChrTalk(    #49
        0x14,
        (
            "Boy, that dress of yours doesn't leave a lot\x01",
            "to the imagination, does it? That opening in\x01",
            "the chest... Mmmm... Delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14,
        (
            "Don't know how you managed it, but you're\x01",
            "totally walking that thin line between classy\x01",
            "and super-sexy. Bravo, Schera... Bravo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x14,
        (
            "As always, a 97 for you! You haven't lost\x01",
            "your touch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#526FOh, still not a perfect hundred? I feel\x01",
            "both hurt and secure at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x14,
        (
            "Heh, I don't give THAT one out to just\x01",
            "anyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1019FYou're never going to change your spots,\x01",
            "are you? Maybe I'LL change something...\x01",
            "Like your face. With my staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4D")

    label("loc_1B73")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x107, 400)
    Sleep(1000)

    ChrTalk(    #55
        0x14,
        (
            "Honey-blond hair, eyes like the summer\x01",
            "sea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        (
            "Obviously still a bit too young to really rank,\x01",
            "but you can tell she'll be a beauty once she\x01",
            "really blooms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x14,
        (
            "So let's go with a provisional 80 points in\x01",
            "the Junior League! Though smart money's\x01",
            "on that going higher in the majors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#065FWh-Wh-Whaaaaa...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1007FTita, don't worry. That is not a sport you\x01",
            "want to play. Ever. Under any circumstances.\x02\x03",

            "#1019FYou're never going to change your spots,\x01",
            "are you? Maybe I'LL change something...\x01",
            "Like your face. With my staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4D")

    label("loc_1DB2")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #60
        0x14,
        (
            "Heeey... Tight thigh-highs, giving off a sort\x01",
            "of clean, virtuous vibe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14,
        (
            "Still not quite bursting with sex appeal,\x01",
            "but overflowing with a young, healthy\x01",
            "beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x14,
        "Yeah, you're a solid 90! Great work!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #63
        0x101,
        (
            "#1019F90, huh? You're never going to change\x01",
            "your spots, are you? Maybe I'LL change\x01",
            "something... Like your face. With my staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4D")

    label("loc_1F4D")

    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #64
        0x14,
        (
            "Oh, hey, Estelle. Welcome back. You're\x01",
            "getting more and more beautiful every\x01",
            "time I lay eyes on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "Seriously, you're really coming into your\x01",
            "own. And I know you ain't done growing\x01",
            "yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007FSetting aside the fact that people have\x01",
            "killed for less...do you really have the\x01",
            "time for your shenanigans?\x02\x03",

            "The airships aren't running and you\x01",
            "seem kinda busy, all told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        (
            "Ha-ha-ha! Aww, come on, Estelle,\x01",
            "don't cramp my style now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x14,
        (
            "This is the secret to enjoying this job\x01",
            "as long as I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x14,
        "Still, though, this fog is insane, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x14,
        (
            "I wonder how many girls I've missed\x01",
            "in this mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1019FWell, with a one-track mind like yours,\x01",
            "at least there isn't much to waste.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x189A)
    ClearChrFlags(0x14, 0x10)

    label("loc_2215")

    Jump("loc_24B1")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_24B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 7)), scpexpr(EXPR_END)), "loc_22A6")

    ChrTalk(    #72
        0x14,
        (
            "All the traffic from the queen's birthday\x01",
            "celebrations has finally settled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        "Rolent is back to its usual self.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B1")

    label("loc_22A6")


    ChrTalk(    #74
        0x14,
        (
            "90 points, 70, 84... Heheh.\x01",
            "Today's been sweet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x101, 400)
    Sleep(600)

    ChrTalk(    #75
        0x14,
        (
            "Ooh! Chestnut hair in twintails, brown\x01",
            "eyes that are almost red like flame...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14,
        (
            "Healthy proportions, but...lacking in a\x01",
            "certain feminine charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x14,
        "I'll have to give that one 82 points!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#509F...Please explain to me, in detail,\x01",
            "exactly how I am 82 points. I want\x01",
            "justification for the beatings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14,
        "...Well, now that I look, it's you, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x14,
        "Hey, been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#007FUgh... You're the same as always, Alan.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1027)

    label("loc_24B1")

    TalkEnd(0x14)
    Return()

    # Function_5_9A0 end

    def Function_6_24B5(): pass

    label("Function_6_24B5")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_253E")

    ChrTalk(    #82
        0xFE,
        (
            "I've gone over it again and again,\x01",
            "but I can't find anything wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "It's got to be this wider...whatever this is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_253E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25C3")

    ChrTalk(    #84
        0xFE,
        "The engine isn't activating...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I don't see anything wrong with its mechanics,\x01",
            "either. What the hell is going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_25C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_264B")

    ChrTalk(    #86
        0xFE,
        "Finished checking in?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "If you intend to ride one of our regularly-\x01",
            "scheduled ships, check in with Alan at\x01",
            "reception.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_264B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_26C5")

    ChrTalk(    #88
        0xFE,
        (
            "I came out hoping the fog would've cleared\x01",
            "up by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Looks like we're not getting much done\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_26C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_277D")

    ChrTalk(    #90
        0xFE,
        (
            "We're having the Linde fly an alternate\x01",
            "route through the other four cities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Haven't modified a flight plan like this\x01",
            "since the sky bandits were a serious\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CA")

    label("loc_277D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(    #92
        0xFE,
        (
            "So I don't mind admitting that I just\x01",
            "about lost my mind during that landing\x01",
            "attempt. That was harrowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Captain Petrov is a hero for succeeding\x01",
            "at landing in these conditions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2952")

    label("loc_284A")


    ChrTalk(    #94
        0xFE,
        (
            "Ohhhh, Aidios. That landing just about\x01",
            "made me die of a heart attack, I tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "We managed it, even though visibility\x01",
            "was practically nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Captain Petrov is a hero for succeeding\x01",
            "at landing in these conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "He's got guts of steel!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2952")

    Jump("loc_29CA")

    label("loc_2955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_29CA")

    ChrTalk(    #98
        0xFE,
        "The capital-bound Linde's arriving next.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I need to keep things maintained so\x01",
            "there're no accidents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CA")

    TalkEnd(0x1A)
    Return()

    # Function_6_24B5 end

    def Function_7_29CE(): pass

    label("Function_7_29CE")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2B8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADC")

    ChrTalk(    #100
        0xFE,
        (
            "According to rumors, an army patrol ship\x01",
            "made an emergency landing near town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Looks like it's true that this orbment-\x01",
            "stopping thing is affecting the entire\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "That's terrifying... Guess us engineers\x01",
            "might be out of a job...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2B8C")

    label("loc_2ADC")


    ChrTalk(    #103
        0xFE,
        (
            "According to rumors, an army patrol ship\x01",
            "made an emergency landing near town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Looks like it's true that this orbment-\x01",
            "stopping thing is affecting the entire\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    Jump("loc_3153")

    label("loc_2B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C21")

    ChrTalk(    #105
        0xFE,
        "Damn it... What's causing this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "The Linde's engine is totally fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "So why won't this piece of junk start?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2C6F")

    label("loc_2C21")


    ChrTalk(    #108
        0xFE,
        "Damn it... What's causing this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Why won't the Linde's engine start?\x02",
    )

    CloseMessageWindow()

    label("loc_2C6F")

    Jump("loc_3153")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D10")

    ChrTalk(    #110
        0xFE,
        (
            "The Cecilia herself must be pretty fed up\x01",
            "with waiting around, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Heheh, hope she doesn't haul TOO\x01",
            "hard and burn out her engine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF3")

    label("loc_2D10")


    ChrTalk(    #112
        0xFE,
        (
            "Heheh, finally back in business!\x01",
            "Going to be busy around here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "The Cecilia herself must be pretty fed\x01",
            "up with waiting around, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Hope it flies hard and strong out there\x01",
            "today to make up for lost time!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2DF3")

    Jump("loc_3153")

    label("loc_2DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2E8A")

    ChrTalk(    #115
        0xFE,
        "The Cecilia's in perfect shape now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I came in after the fog got real bad,\x01",
            "so now I'm planning on hanging up my\x01",
            "hat for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3153")

    label("loc_2E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2F2A")

    ChrTalk(    #117
        0xFE,
        (
            "Alan's got a real hard time of it for\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "He's going to have to spend most of\x01",
            "the day dealing with passengers instead\x01",
            "of hitting on them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3153")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_30C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FCB")

    ChrTalk(    #119
        0xFE,
        (
            "The control tower folk, us engineers,\x01",
            "and the ship crew...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "These three groups coordinating together\x01",
            "is the key to making a port work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C3")

    label("loc_2FCB")


    ChrTalk(    #121
        0xFE,
        (
            "Landing an airship's a contest of\x01",
            "teamwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "The control tower folk, us engineers,\x01",
            "and the ship crew...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "All three of us need to do our jobs\x01",
            "perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "If we're not perfectly in sync, there's no\x01",
            "way an airship can land safely.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_30C3")

    Jump("loc_3153")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_3153")

    ChrTalk(    #125
        0xFE,
        (
            "I want to see the royal family's Arseille\x01",
            "I've been hearing so much about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Well, doubt I'll ever see it come out to\x01",
            "Rolent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3153")

    TalkEnd(0x1B)
    Return()

    # Function_7_29CE end

    def Function_8_3157(): pass

    label("Function_8_3157")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_31DF")

    ChrTalk(    #127
        0xFE,
        "No passenger ships today, either...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I shouldn't be surprised. The fog is\x01",
            "even worse today than it was yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3277")

    label("loc_31DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3277")

    ChrTalk(    #129
        0xFE,
        (
            "Man, oh, man... I have no idea what to\x01",
            "do, stopping in Rolent like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "*sigh* Guess I've got to delay my trip\x01",
            "to see the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3277")

    TalkEnd(0x1C)
    Return()

    # Function_8_3157 end

    def Function_9_327B(): pass

    label("Function_9_327B")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3313")

    ChrTalk(    #131
        0xFE,
        (
            "There's stuff I'd like to see in Rolent,\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "But what the heck kind of pictures am\x01",
            "I supposed to take in fog like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3406")

    label("loc_3313")


    ChrTalk(    #133
        0xFE,
        (
            "There's stuff I'd like to see in Rolent,\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "But what the heck kind of pictures am\x01",
            "I supposed to take in fog like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "But just hanging around the Hotel Rolent\x01",
            "would get boring really quickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Mmm, this is baaad...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3406")

    TalkEnd(0x1D)
    Return()

    # Function_9_327B end

    def Function_10_340A(): pass

    label("Function_10_340A")

    OP_EA(0x1, 0x9, 0x0, 0x0)
    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3498")

    ChrTalk(    #137
        0xFE,
        (
            "I put all my hopes, my dreams, my money\x01",
            "into this Bose trip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Even NATURE ITSELF conspires against\x01",
            "my quest! NATURE!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3498")

    TalkEnd(0x25)
    Return()

    # Function_10_340A end

    def Function_11_349C(): pass

    label("Function_11_349C")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3547")

    ChrTalk(    #139
        0xFE,
        (
            "Anton, spitting at the heavens isn't\x01",
            "gonna get us anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Let's go to the bracer guildhouse for\x01",
            "now and talk about where we go from\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3629")

    label("loc_3547")


    ChrTalk(    #141
        0xFE,
        (
            "Anton, spitting at the heavens isn't\x01",
            "gonna get us anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Let's go to the bracer guildhouse for\x01",
            "now and talk about where we go from\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "We might be able to secure a ground\x01",
            "route to Bose, if we're lucky.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3629")

    TalkEnd(0x26)
    Return()

    # Function_11_349C end

    def Function_12_362D(): pass

    label("Function_12_362D")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_366B")

    ChrTalk(    #144
        0xFE,
        (
            "Oh, no! The ships haven't resumed\x01",
            "service yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366B")

    TalkEnd(0x1E)
    Return()

    # Function_12_362D end

    def Function_13_366F(): pass

    label("Function_13_366F")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_37CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_36F9")

    ChrTalk(    #145
        0xFE,
        (
            "Apparently the airships still aren't in\x01",
            "service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Nothing for it... I'll have to go back\x01",
            "to the hotel again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CA")

    label("loc_36F9")


    ChrTalk(    #147
        0xFE,
        (
            "Apparently the airships still aren't in\x01",
            "service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Nothing for it... I'll have to go back\x01",
            "to the hotel again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I should have a look around town first,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Maybe I can find a nice shop?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_37CA")

    TalkEnd(0x1F)
    Return()

    # Function_13_366F end

    def Function_14_37CE(): pass

    label("Function_14_37CE")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3800")

    ChrTalk(    #151
        0xFE,
        "Nooo! Not today, either?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3854")

    label("loc_3800")


    ChrTalk(    #152
        0xFE,
        "Nooo! Not today, either?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "*sigh* Guess I need to contact\x01",
            "my wife again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3854")

    TalkEnd(0x20)
    Return()

    # Function_14_37CE end

    def Function_15_3858(): pass

    label("Function_15_3858")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3900")

    ChrTalk(    #154
        0xFE,
        (
            "Looks like the airship passengers\x01",
            "have all left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I understand how they feel,\x01",
            "I really do. But I hope they'll\x01",
            "remain at the hotel for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A00")

    label("loc_3900")


    ChrTalk(    #156
        0xFE,
        (
            "Looks like the airship passengers\x01",
            "have all left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I understand how they feel,\x01",
            "I really do. But I hope they'll\x01",
            "remain at the hotel for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Having so many citizens walking about\x01",
            "is only going to make things harder for\x01",
            "my men out on patrol.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3A00")

    TalkEnd(0x21)
    Return()

    # Function_15_3858 end

    def Function_16_3A04(): pass

    label("Function_16_3A04")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B69")

    ChrTalk(    #159
        0xFE,
        (
            "The check of the engine didn't find\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "This phenomenon occurring across the\x01",
            "kingdom can be the only cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Without orbal power...forget flight.\x01",
            "The only way we have to get around is\x01",
            "our own two feet or a horse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "At some point, we began relying on\x01",
            "orbments completely. You do have to\x01",
            "wonder how wise it was.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3C48")

    label("loc_3B69")


    ChrTalk(    #163
        0xFE,
        (
            "We're powerless when orbal energy's\x01",
            "taken from us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "Never mind flying. The only way we\x01",
            "have to get around is our own two\x01",
            "feet or a horse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Our reliance on orbal power came to\x01",
            "define us as a people, in a way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C48")

    Jump("loc_3E6A")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD5")

    ChrTalk(    #166
        0xFE,
        (
            "We're still trying to figure out why the\x01",
            "engines have stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I sent the crew who have family waiting\x01",
            "back to Grancel, but who knows when\x01",
            "we'll need them again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I've never heard of orbments across an\x01",
            "entire nation simply ceasing to function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Combined with some of the other recent\x01",
            "goings-on, I suspect we still have some\x01",
            "struggles ahead of us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3E6A")

    label("loc_3DD5")


    ChrTalk(    #170
        0xFE,
        (
            "We're still trying to figure out why the\x01",
            "engines have stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Even once we locate the cause,\x01",
            "resuming flight will take some time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6A")

    TalkEnd(0x22)
    Return()

    # Function_16_3A04 end

    def Function_17_3E6E(): pass

    label("Function_17_3E6E")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3F19")

    ChrTalk(    #172
        0xFE,
        (
            "Right now, we have no idea when\x01",
            "service will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "It's unfortunate, but what can we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "We're not even sure why the engines\x01",
            "aren't working!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B3")

    label("loc_3F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_40B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401C")

    ChrTalk(    #175
        0xFE,
        (
            "Missing flights due to machine trouble\x01",
            "is a hassle for our customers, I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "But personally? I'm just glad no one\x01",
            "was hurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Just thinking what would've happened\x01",
            "if the engine power cut out when we\x01",
            "were in flight... Brrrr!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_40B3")

    label("loc_401C")


    ChrTalk(    #178
        0xFE,
        (
            "Personally, I'm just glad no one was\x01",
            "hurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Just thinking what would've happened\x01",
            "if the engine power cut out when we\x01",
            "were in flight... Brrrr!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B3")

    TalkEnd(0x23)
    Return()

    # Function_17_3E6E end

    def Function_18_40B7(): pass

    label("Function_18_40B7")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_4160")

    ChrTalk(    #180
        0xFE,
        (
            "I just can't find anything wrong with\x01",
            "the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I feel so bad for the ground crew.\x01",
            "Everyone's just been beating themselves\x01",
            "up over this non-stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A8")

    label("loc_4160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_43A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42CE")

    ChrTalk(    #182
        0xFE,
        (
            "So strange... I've never seen a problem\x01",
            "like this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Normally there's some kind of sign\x01",
            "before a ship has mechanical trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "The engine block overheats, a rattle in\x01",
            "the hull, that sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "But this time there was absolutely\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "It was so sudden, like some just began\x01",
            "turning off our engines mid-flight.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_43A8")

    label("loc_42CE")


    ChrTalk(    #187
        0xFE,
        (
            "There was no sign of this trouble at all\x01",
            "in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I was even looking at the instruments\x01",
            "as it happened, which made it even more\x01",
            "unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Without a sound, the output gauge\x01",
            "just slid down to zero.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A8")

    TalkEnd(0x24)
    Return()

    # Function_18_40B7 end

    def Function_19_43AC(): pass

    label("Function_19_43AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_4506")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445C")

    ChrTalk(    #190
        0xFE,
        "*siiigh* I can't stay in Rolent forever!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "I need to start considering options\x01",
            "for ground transport...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "*sigh* This is really depressing...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_4503")

    label("loc_445C")


    ChrTalk(    #193
        0xFE,
        (
            "Oooh, but I really don't want to go\x01",
            "home on the roads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I, well, those monsters...\x01",
            "I can't stand them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "That's why I use airships to travel\x01",
            "everywhere!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4503")

    Jump("loc_4561")

    label("loc_4506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4561")

    ChrTalk(    #196
        0xFE,
        "No airships today either, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Not like I expected much different,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4561")

    TalkEnd(0xFE)
    Return()

    # Function_19_43AC end

    def Function_20_4565(): pass

    label("Function_20_4565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_464B")

    ChrTalk(    #198
        0xFE,
        (
            "We don't know when service will resume.\x01",
            "We don't know the cause of the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Even I could say that!\x01",
            "Tell us something USEFUL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Really, that guy at the reception desk.\x01",
            "Does he even want to do his job?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_473F")

    label("loc_464B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_473F")

    ChrTalk(    #201
        0xFE,
        (
            "'We have no idea when service will resume.'\x01",
            "I mean, is that really an answer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I mean, even if it's a bit of a lie,\x01",
            "I'd like to hear an answer that gives\x01",
            "me some hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Right? You understand, right?\x01",
            "You get what I'm saying!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473F")

    TalkEnd(0xFE)
    Return()

    # Function_20_4565 end

    def Function_21_4743(): pass

    label("Function_21_4743")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    OP_11(0xA4, 0xB7, 0xFF, 0xA7F8, 0x493E0, 0x0)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_72(0xF, 0x4)
    OP_72(0xC, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55700, -300, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, -1000, 35000, 0)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x17, 0x4)
    ClearMapFlags(0x2000000)
    OP_6D(47960, 26950, 30490, 0)
    OP_67(0, 27020, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x1, 0xBB8)
    OP_DE("Rolent")
    FadeToBright(3000, 0)
    OP_6F(0xD, 200)
    OP_70(0xD, 0xC8)
    StopSound(0xA7F8, 0x3D090, 0x2710)

    def lambda_483C():
        OP_6D(53380, 4050, 31110, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_483C)

    def lambda_4854():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4854)

    def lambda_486C():
        OP_6B(3300, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_486C)

    def lambda_487C():
        OP_6C(65000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_487C)

    def lambda_488C():
        OP_91(0xFE, 0x0, 0xFFFFF441, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_488C)

    def lambda_48A7():
        OP_91(0xFE, 0x0, 0xFFFFF829, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_48A7)
    OP_6F(0xF, 130)
    WaitChrThread(0x18, 0x0)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 130)
    OP_70(0xF, 0x1)
    Sleep(900)
    OP_22(0x76, 0x0, 0x46)
    OP_73(0xF)
    Sleep(400)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 200)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xF, 411)
    OP_70(0xF, 0x1C2)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0xF)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x16)
    OP_43(0x9, 0x1, 0x0, 0x17)
    Sleep(1000)
    OP_43(0xA, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0x16)
    OP_43(0xC, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0xD, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(500)
    Sleep(1000)
    OP_43(0xF, 0x1, 0x0, 0x16)
    Sleep(3000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x15, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x15, 0x20)
    OP_48()
    OP_89(0x101, 55990, 4230, 34970, 6)
    OP_89(0x15, 55990, 4230, 34970, 6)

    def lambda_49F5():
        OP_8E(0x101, 0xD8E0, 0x1022, 0x7CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_49F5)
    Sleep(1000)

    def lambda_4A15():
        OP_8E(0x15, 0xD9B2, 0x1022, 0x8106, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4A15)
    WaitChrThread(0x101, 0x0)

    def lambda_4A35():
        OP_8E(0x101, 0xCD28, 0x1022, 0x78E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A35)
    WaitChrThread(0x15, 0x0)

    def lambda_4A55():
        OP_8E(0x15, 0xCD28, 0x1022, 0x78E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4A55)
    WaitChrThread(0x101, 0x0)

    def lambda_4A75():
        OP_8E(0x101, 0xA456, 0xFA0, 0x7A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A75)
    WaitChrThread(0x15, 0x0)

    def lambda_4A95():
        OP_8E(0x15, 0xA9A6, 0xFA0, 0x78FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4A95)
    ClearChrFlags(0x101, 0x4)
    Sleep(1000)
    ClearChrFlags(0x15, 0x4)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(42990, 4000, 31290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(57000, 0)
    OP_6E(200, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x15, 0x0)
    OP_0D()
    Sleep(500)
    OP_8C(0x15, 225, 500)
    Sleep(500)

    ChrTalk(    #204
        0x15,
        (
            "#1061FAhhhh, smell that fresh air!\x01",
            "So this is Rolent, huh?\x02\x03",

            "Gotta admit, though...it feels a bit\x01",
            "like a backwater farming village with\x01",
            "an airship dock dropped on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 120, 500)

    ChrTalk(    #205
        0x101,
        (
            "#007F#3PWell, excuse the heck out of\x01",
            "us for living in the boonies.\x02\x03",

            "#509FAt least we're big enough to have\x01",
            "our own church,\x01",
            "Mr. Totally-Pretending-To-Be-A-Holy-Man.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 500)

    ChrTalk(    #206
        0x15,
        (
            "#1062FOh! I'd better go pay my respects\x01",
            "over there once we're done.\x02\x03",

            "So, Estelle! Which one of these\x01",
            "fine boonie-shacks is yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#505F#3PUh, setting the 'boonie-shacks' bit\x01",
            "aside...you really don't need to escort\x01",
            "me home, you know.\x02\x03",

            "It's just outside town, and crying fits\x01",
            "aside, I really AM a bracer. I can take\x01",
            "care of myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x15,
        (
            "#1061FHah, nah, don't worry about it.\x01",
            "It's a duty of us real, manly men to\x01",
            "make sure a lady gets home safely.\x02\x03",

            "#1060F 'Sides! I'm lookin' forward to\x01",
            "meeting this boyfriend of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#503F#3PB-B-Boyfriend isn't the term I...\x01",
            "think I'd use...maybe...\x02\x03",

            "#008FBut, fair enough, I guess! I'll fix\x01",
            "you some tea or something when\x01",
            "we get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x15,
        (
            "#1061FAnd I get free tea out of the deal!\x01",
            "Victory again! Well, lead the way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_72(0xA, 0x4)
    OP_6D(42190, 4000, 31180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x41, 0xFF, 0xFF)
    SetChrPos(0x101, 42190, 4000, 31180, 0)
    SetChrPos(0x142, 42190, 4000, 31180, 0)
    OP_A2(0x1003)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x15, 0x80)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_21_4743 end

    def Function_22_5041(): pass

    label("Function_22_5041")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 55680, 3890, 35740, 0)
    OP_8E(0xFE, 0xD9C6, 0x105E, 0x795E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xAA0A, 0xF5A, 0x7670, 0x7D0, 0x0)
    Sleep(2000)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_5041 end

    def Function_23_50A0(): pass

    label("Function_23_50A0")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 52970, 4293, 42260, 357)
    OP_8E(0xFE, 0xCEFE, 0x1022, 0x7B02, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA820, 0xFA0, 0x7A76, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_50A0 end

    def Function_24_50F3(): pass

    label("Function_24_50F3")

    EventBegin(0x0)
    OP_DB()
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_6D(51650, -3070, 39040, 0)
    OP_67(0, 16810, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(135000, 0)
    OP_6E(540, 0)
    SetChrFlags(0x0, 0x80)
    OP_72(0xF, 0x20)
    OP_72(0xC, 0x4)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x3C)
    OP_6F(0xE, 0)
    OP_6F(0xD, 200)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x17, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55800, 15000, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, 10000, 35000, 0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)
    AddParty(0x3, 0xFA, 0xFF)
    AddParty(0x4, 0xFB, 0xFF)
    AddParty(0x7, 0xFC, 0xFF)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_71(0x4, 0x20)
    OP_71(0x5, 0x20)
    OP_71(0x7, 0x20)
    OP_71(0x8, 0x20)
    OP_71(0x9, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2D0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x2D0)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x2D0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x2D0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x2D0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x2D0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x2D0)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x2D0)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x2D0)

    def lambda_5277():
        OP_6D(51760, -3070, 40830, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5277)

    def lambda_528F():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_528F)

    def lambda_529F():
        OP_8F(0xFE, 0xD9F8, 0xFFFFF448, 0x88B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_529F)

    def lambda_52BA():
        OP_8F(0xFE, 0xD9F8, 0x0, 0x88B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_52BA)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x1, 0x3E8)
    OP_DE("City of Rolent")
    FadeToBright(1000, 0)
    OP_22(0xE2, 0x0, 0x64)
    WaitChrThread(0x18, 0x1)

    def lambda_530D():
        OP_8F(0xFE, 0xD9F8, 0xFFFFFC18, 0x88B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_530D)
    WaitChrThread(0x18, 0x1)

    def lambda_532D():
        OP_8F(0xFE, 0xD9F8, 0xFFFFF448, 0x88B8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_532D)
    WaitChrThread(0x18, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_22(0x76, 0x0, 0x46)
    OP_B0(0xF, 0x3C)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x1)
    OP_73(0xF)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 200)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    Sleep(1000)
    OP_23(0x79)
    Fade(1000)
    OP_6D(55840, 4200, 32009, 0)
    OP_67(0, 7250, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(29000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xF, 411)
    OP_70(0xF, 0x1C2)
    OP_73(0xF)
    OP_43(0x101, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0x107, 0x0, 0x0, 0x1C)
    Sleep(300)
    OP_43(0x106, 0x0, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x103, 0x0, 0x0, 0x1A)
    Sleep(500)
    OP_43(0x104, 0x0, 0x0, 0x1D)
    Sleep(500)
    OP_43(0x105, 0x0, 0x0, 0x1E)
    Sleep(500)
    OP_43(0x108, 0x0, 0x0, 0x1F)
    Sleep(500)
    WaitChrThread(0x108, 0x0)
    OP_DC()

    ChrTalk(    #211
        0x101,
        "#1020FHoly... It's completely white.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x107,
        "#065F#5PYeah! You can't see anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x105,
        (
            "#043F#3PIt looks like the port authority is grounding\x01",
            "all flights until the fog clears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x103,
        "#026F#6PHmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(500)

    ChrTalk(    #215
        0x103,
        (
            "#020F#6PI think we'll want to visit the\x01",
            "guildhouse here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5574():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5574)
    Sleep(50)

    def lambda_5587():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5587)
    Sleep(50)

    def lambda_559A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_559A)
    Sleep(400)

    ChrTalk(    #216
        0x106,
        "#051F#2PThought so too, huh?\x02",
    )

    CloseMessageWindow()

    def lambda_55CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_55CF)
    Sleep(50)

    def lambda_55E2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_55E2)
    Sleep(50)

    def lambda_55F5():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_55F5)
    Sleep(400)

    ChrTalk(    #217
        0x101,
        "#1004FHuh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x108,
        (
            "#074F#4PThis fog is deep and strange enough that\x01",
            "even you and Scherazard comment on it,\x01",
            "Estelle.\x02\x03",

            "#072FIt's possible the society is behind this.\x01",
            "Somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1026FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x104,
        (
            "#035F#4PHm. Only Rolent and Bose remain unmolested\x01",
            "by their hands.\x02\x03",

            "#030FIt is possible their next 'experiment'\x01",
            "shall be here, then, and not in Bose.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400A7, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_24_50F3 end

    def Function_25_57AC(): pass

    label("Function_25_57AC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_57D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57D3)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD0E8, 0x1022, 0x7A58, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_57AC end

    def Function_26_580F(): pass

    label("Function_26_580F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_5836():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5836)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD93A, 0x1022, 0x7BF2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_26_580F end

    def Function_27_5872(): pass

    label("Function_27_5872")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_5899():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5899)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD9E4, 0x1022, 0x7620, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_27_5872 end

    def Function_28_58D5(): pass

    label("Function_28_58D5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_58FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58FC)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD3AE, 0x1022, 0x756C, 0x7D0, 0x0)
    Return()

    # Function_28_58D5 end

    def Function_29_5931(): pass

    label("Function_29_5931")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_5958():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5958)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDE76, 0x1022, 0x7878, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_29_5931 end

    def Function_30_5994(): pass

    label("Function_30_5994")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_59BB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59BB)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD548, 0x1068, 0x7E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_30_5994 end

    def Function_31_59F7(): pass

    label("Function_31_59F7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_5A1E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A1E)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDE80, 0x1022, 0x802A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_59F7 end

    def Function_32_5A5A(): pass

    label("Function_32_5A5A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A7B")
    Call(0, 37)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_5A7B")

    Fade(1000)
    OP_6D(36120, 0, 34420, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 36570, 0, 33800, 0)
    SetChrPos(0x103, 35550, 0, 33750, 0)
    SetChrPos(0xF8, 35590, 0, 32350, 0)
    SetChrPos(0xF9, 36650, 0, 32439, 0)
    TurnDirection(0x14, 0x101, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D8A")
    OP_A2(0x1A01)

    ChrTalk(    #221
        0x14,
        "#6PHey, Estelle. Heading out already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x14,
        (
            "#6PYou just came home. Sure you can't\x01",
            "stay around for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1016F#4PYeah, sorry...\x01",
            "There's kind of a lot going on.\x02\x03",

            "#1006FOnce our current job's done, I totally\x01",
            "intend to come back and take a load\x01",
            "off for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x14,
        "#6PYou really should. We'll be waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x14,
        (
            "#6PAnyway, your tickets've already\x01",
            "been paid for by Aina.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x14,
        "#6PReady to check in?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)

    ChrTalk(    #227
        0x103,
        (
            "#020F#6PAs always, we should wait for the ship\x01",
            "once we check in.\x02\x03",

            "Do you have any other business in Rolent\x01",
            "before we go?\x02",
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
            "Still Have Things To Do\x01",      # 0
            "Let's Fly\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_5E11")

    label("loc_5D8A")


    ChrTalk(    #228
        0x14,
        "#6PHey! Want to check in for your flight?\x02",
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
            "Still Have Things To Do\x01",      # 0
            "Let's Fly\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E5C")

    ChrTalk(    #229
        0x14,
        (
            "#6PNo worries.\x01",
            "Just let me know when you're ready.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_5E5C")


    ChrTalk(    #230
        0x14,
        "#6PAll right, then!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #231
        0x14,
        (
            "#6PI'll give the guildhouse a ring and call\x01",
            "the other members of your team.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #232
        (
            "\x07\x05Estelle's team checked in for their flight and\x01",
            "waited for the airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 36)
    OP_6D(44610, 4000, 35220, 0)
    OP_67(0, 8220, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(50000, 0)
    OP_6E(331, 0)
    SetChrPos(0x101, 40690, 4000, 36460, 180)
    SetChrPos(0x103, 41780, 4000, 37050, 180)
    SetChrPos(0xF8, 39750, 4000, 37200, 180)
    SetChrPos(0xF9, 40930, 4000, 38420, 180)
    SetChrPos(0xFA, 39260, 4000, 38230, 180)
    SetChrPos(0xFB, 40230, 4000, 39230, 180)
    SetChrPos(0xFC, 39020, 4000, 39620, 180)
    SetChrPos(0x8, 42970, 4000, 31060, 90)
    SetChrPos(0x9, 42660, 4000, 31950, 180)
    SetChrPos(0xA, 42690, 4000, 33090, 180)
    SetChrPos(0xB, 42120, 4000, 34240, 114)
    SetChrPos(0xC, 41690, 4000, 35590, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_71(0xA, 0x4)
    OP_71(0xA, 0x2)
    OP_72(0xF, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_6F(0xF, 450)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    SetChrFlags(0x1A, 0x80)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55000, -3040, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55000, -3040, 35000, 0)
    OP_48()
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_43(0x8, 0x1, 0x0, 0x21)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x22)
    Sleep(580)
    OP_43(0xA, 0x1, 0x0, 0x22)
    Sleep(550)
    OP_43(0xB, 0x1, 0x0, 0x22)
    Sleep(680)
    OP_43(0xC, 0x1, 0x0, 0x22)
    Sleep(650)
    OP_43(0x101, 0x1, 0x0, 0x23)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0x23)
    Sleep(480)
    OP_43(0xF8, 0x1, 0x0, 0x23)
    Sleep(470)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    Sleep(490)
    OP_43(0xFA, 0x1, 0x0, 0x23)
    Sleep(500)
    OP_43(0xFB, 0x1, 0x0, 0x23)
    Sleep(480)
    OP_43(0xFC, 0x1, 0x0, 0x23)
    Sleep(4800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_6D(48470, 3930, 38060, 0)
    OP_67(0, 40540, -45000, 0)
    OP_6B(740, 0)
    OP_6C(159000, 0)
    OP_6E(510, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    OP_6F(0xF, 1)
    FadeToBright(1000, 0)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)

    def lambda_62D6():
        OP_6D(59300, 3930, 70000, 18000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62D6)

    def lambda_62EE():
        OP_6C(215000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62EE)

    def lambda_62FE():
        OP_6B(850, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_62FE)

    def lambda_630E():
        OP_6E(580, 20000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_630E)
    LoadEffect(0x0, "map\\\\mp028_00.eff")
    Play3DEffect(0x0, 0x0, 0xB, "Frame1_E0000_ground_Layer1", 0xFFFFE7C8, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Play3DEffect(0x0, 0x1, 0xB, "Frame1_E0000_ground_Layer1", 0x1838, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)

    def lambda_63B4():
        OP_8E(0xFE, 0xD6D8, 0xFFFFF808, 0x88B8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_63B4)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0xF, 0x20)
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x18, 0x0)

    def lambda_63FD():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_63FD)

    def lambda_6418():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6418)
    Sleep(200)

    def lambda_6438():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6438)

    def lambda_6453():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6453)
    Sleep(200)

    def lambda_6473():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6473)

    def lambda_648E():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_648E)
    Sleep(200)

    def lambda_64AE():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_64AE)

    def lambda_64C9():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_64C9)
    Sleep(200)

    def lambda_64E9():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_64E9)

    def lambda_6504():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6504)
    Sleep(200)

    def lambda_6524():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6524)

    def lambda_653F():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_653F)
    Sleep(200)

    def lambda_655F():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_655F)

    def lambda_657A():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_657A)
    Sleep(200)

    def lambda_659A():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_659A)

    def lambda_65B5():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_65B5)
    Sleep(200)

    def lambda_65D5():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_65D5)

    def lambda_65F0():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_65F0)
    Sleep(200)

    def lambda_6610():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6610)

    def lambda_662B():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_662B)
    Sleep(200)

    def lambda_664B():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_664B)

    def lambda_6666():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6666)
    Sleep(200)

    def lambda_6686():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6686)

    def lambda_66A1():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_66A1)
    Sleep(200)

    def lambda_66C1():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_66C1)

    def lambda_66DC():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_66DC)
    Sleep(200)

    def lambda_66FC():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_66FC)

    def lambda_6717():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6717)
    Sleep(200)

    def lambda_6737():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6737)

    def lambda_6752():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6752)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x10F3)
    OP_A2(0x1A02)
    OP_28(0x72, 0x4, 0x40)
    OP_28(0x73, 0x4, 0x40)
    OP_28(0x74, 0x4, 0x40)
    OP_28(0x75, 0x4, 0x40)
    OP_28(0x76, 0x4, 0x40)
    OP_28(0x77, 0x4, 0x40)
    OP_28(0xAD, 0x4, 0x40)
    OP_28(0xAE, 0x4, 0x40)
    OP_28(0xAF, 0x4, 0x40)
    OP_28(0xB0, 0x4, 0x40)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3133   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_32_5A5A end

    def Function_33_6825(): pass

    label("Function_33_6825")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_6825 end

    def Function_34_686C(): pass

    label("Function_34_686C")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xA6CC, 0xFA0, 0x78BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xF5A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_686C end

    def Function_35_68C7(): pass

    label("Function_35_68C7")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xA32A, 0xFA0, 0x8818, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA6CC, 0xFA0, 0x78BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_68C7 end

    def Function_36_6936(): pass

    label("Function_36_6936")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_696F")
    AddParty(0x5, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_696F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69A4")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_69BC")

    label("loc_69A4")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_69BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A31")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69F1")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6A31")

    label("loc_69F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A19")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6A31")

    label("loc_6A19")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A7E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A66")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6A7E")

    label("loc_6A66")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6AA3")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_6AA3")

    Return()

    # Function_36_6936 end

    def Function_37_6AA4(): pass

    label("Function_37_6AA4")

    FadeToDark(0, 0, -1)
    OP_6D(90, 0, 24870, 0)
    Sleep(100)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0, "loc_6B2D"),
        (1, "loc_6B33"),
        (SWITCH_DEFAULT, "loc_6B39"),
    )


    label("loc_6B2D")

    OP_A2(0x1200)
    Jump("loc_6B39")

    label("loc_6B33")

    OP_A2(0x1201)
    Jump("loc_6B39")

    label("loc_6B39")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_37_6AA4 end

    def Function_38_6B75(): pass

    label("Function_38_6B75")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #233
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Grancel\x01",
            "⇒ To Bose\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #234
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_6B75 end

    def Function_39_6C30(): pass

    label("Function_39_6C30")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #235
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_6C30 end

    def Function_40_6CBE(): pass

    label("Function_40_6CBE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #236
        "\x07\x05※Employees Only 《Liberl Orbalship Co.》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_6CBE end

    SaveToFile()

Try(main)
