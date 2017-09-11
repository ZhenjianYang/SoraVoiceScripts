from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3115   ._SN',
            'ED6_DT01/T3115_1 ._SN',
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
        'Factory Chief Murdock',                # 9
        'Captain Amalthea',                     # 10
        'Officer',                              # 11
        'Soldier',                              # 12
        'Louise',                               # 13
        'Karl',                                 # 14
        'Hugo',                                 # 15
        'Maintenance Chief Gustav',             # 16
        'Constance',                            # 17
        'Antoine',                              # 18
        'Igor',                                 # 19
        'Prometheus',                           # 20
        'Wilmont',                              # 21
        'Orbment',                              # 22
        'Ashtray',                              # 23
        'Cigarettes',                           # 24
        'Book',                                 # 25
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
        'ED6_DT07/CH01190 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH02440 ._CH',             # 06
        'ED6_DT07/CH01230 ._CH',             # 07
        'ED6_DT07/CH01700 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01100 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01640 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
        'ED6_DT07/CH02623 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01190P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH02440P._CP',             # 06
        'ED6_DT07/CH01230P._CP',             # 07
        'ED6_DT07/CH01700P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01100P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01640P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
        'ED6_DT07/CH02623P._CP',             # 0E
    )

    DeclNpc(
        X                   = 2400,
        Z                   = 0,
        Y                   = 5300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917517,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 520,
        Z                   = 775,
        Y                   = 100690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572877,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1100,
        Z                   = 800,
        Y                   = 100800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638413,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -105970,
        Z                   = 800,
        Y                   = 105440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703949,
        ChipIndex           = 0xD,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -101920,
        TriggerZ            = 0,
        TriggerY            = 93750,
        TriggerRange        = 1200,
        ActorX              = -101920,
        ActorZ              = 0,
        ActorY              = 93750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2950,
        TriggerZ            = 0,
        TriggerY            = 8029,
        TriggerRange        = 800,
        ActorX              = -2950,
        ActorZ              = 1000,
        ActorY              = 8029,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4150,
        TriggerZ            = 0,
        TriggerY            = 6850,
        TriggerRange        = 800,
        ActorX              = 4070,
        ActorZ              = 1000,
        ActorY              = 7610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4700,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 800,
        ActorX              = 5490,
        ActorZ              = 1000,
        ActorY              = 2270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1600,
        TriggerZ            = 0,
        TriggerY            = 3910,
        TriggerRange        = 800,
        ActorX              = 1600,
        ActorZ              = 1200,
        ActorY              = 3910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4430,
        TriggerZ            = 0,
        TriggerY            = 3760,
        TriggerRange        = 800,
        ActorX              = -5500,
        ActorZ              = 1200,
        ActorY              = 3500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 190,
        TriggerZ            = 0,
        TriggerY            = 101690,
        TriggerRange        = 1200,
        ActorX              = 720,
        ActorZ              = 800,
        ActorY              = 100680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -105970,
        TriggerZ            = 0,
        TriggerY            = 105440,
        TriggerRange        = 1500,
        ActorX              = -105970,
        ActorZ              = 800,
        ActorY              = 105440,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -3070,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -3070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100460,
        TriggerZ            = 0,
        TriggerY            = -6860,
        TriggerRange        = 800,
        ActorX              = -100460,
        ActorZ              = 1200,
        ActorY              = -6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -103830,
        TriggerZ            = 0,
        TriggerY            = 5890,
        TriggerRange        = 800,
        ActorX              = -103830,
        ActorZ              = 1200,
        ActorY              = 5890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -104800,
        TriggerZ            = 0,
        TriggerY            = 9210,
        TriggerRange        = 800,
        ActorX              = -104800,
        ActorZ              = 1200,
        ActorY              = 9210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -101680,
        TriggerZ            = 0,
        TriggerY            = 9240,
        TriggerRange        = 800,
        ActorX              = -101680,
        ActorZ              = 1200,
        ActorY              = 9240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -100410,
        TriggerZ            = 0,
        TriggerY            = 8100,
        TriggerRange        = 800,
        ActorX              = -100410,
        ActorZ              = 1200,
        ActorY              = 8100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_55E",          # 00, 0
        "Function_1_BB5",          # 01, 1
        "Function_2_E95",          # 02, 2
        "Function_3_EAB",          # 03, 3
        "Function_4_ECF",          # 04, 4
        "Function_5_EF3",          # 05, 5
        "Function_6_1098",         # 06, 6
        "Function_7_118A",         # 07, 7
        "Function_8_1A3C",         # 08, 8
        "Function_9_265B",         # 09, 9
        "Function_10_267A",        # 0A, 10
        "Function_11_41EF",        # 0B, 11
        "Function_12_5BED",        # 0C, 12
        "Function_13_642F",        # 0D, 13
        "Function_14_6963",        # 0E, 14
        "Function_15_76A0",        # 0F, 15
        "Function_16_92FA",        # 10, 16
        "Function_17_98A1",        # 11, 17
        "Function_18_A962",        # 12, 18
        "Function_19_A9AC",        # 13, 19
        "Function_20_AA00",        # 14, 20
        "Function_21_AA4A",        # 15, 21
        "Function_22_AC0C",        # 16, 22
        "Function_23_ACB5",        # 17, 23
        "Function_24_AD6C",        # 18, 24
        "Function_25_AE28",        # 19, 25
        "Function_26_AEB7",        # 1A, 26
        "Function_27_B351",        # 1B, 27
        "Function_28_B415",        # 1C, 28
        "Function_29_B4DA",        # 1D, 29
        "Function_30_B59F",        # 1E, 30
        "Function_31_B662",        # 1F, 31
        "Function_32_B729",        # 20, 32
        "Function_33_B7ED",        # 21, 33
    )


    def Function_0_55E(): pass

    label("Function_0_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_56C")
    OP_A3(0x3FA)
    Event(0, 17)

    label("loc_56C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_578"),
        (SWITCH_DEFAULT, "loc_58E"),
    )


    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B")
    OP_A2(0x50E)
    Event(0, 15)

    label("loc_58B")

    Jump("loc_58E")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_62F")
    SetChrPos(0xF, 2240, 0, 3050, 6)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108280, 0, 100340, 215)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6B5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108280, 0, 100340, 215)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_723")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, -104580, 0, 101850, 186)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    Jump("loc_B99")

    label("loc_723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_7AE")
    SetChrPos(0xC, -102800, 0, 96960, 277)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -102800, 0, 97960, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101470, 0, 105910, 180)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_808")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_84C")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101430, 0, 102440, 267)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_85B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B99")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86F")
    SetChrFlags(0x8, 0x80)

    label("loc_86F")

    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    SetChrPos(0xC, -103490, 0, 98980, 184)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xD, -102800, 0, 97960, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -102960, 0, 8850, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -101660, 0, 107300, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    Jump("loc_B99")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_9B4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -102800, 0, 97440, 277)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2180, 0, 3050, 352)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -106230, 0, 107410, 325)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_A5F")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -106270, 0, 103210, 195)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -106210, 0, 102010, 343)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -101150, 0, -4440, 100)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_B07")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102890, 0, 97500, 280)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -104980, 0, 101930, 319)
    OP_43(0x11, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -108240, 0, 100430, 225)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)
    Jump("loc_B99")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B99")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -101150, 0, 4900, 9)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -102780, 0, 97390, 350)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -102830, 0, 98700, 178)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -103290, 0, 108340, 355)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 2510, 250, 5400, 180)

    label("loc_B99")

    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB4")
    ClearChrFlags(0x18, 0x80)

    label("loc_BB4")

    Return()

    # Function_0_55E end

    def Function_1_BB5(): pass

    label("Function_1_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA")

    label("loc_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA")

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BFA")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C88")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_C88")

    Jump("loc_D27")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D23")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -101920, 0, 93750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_D27")

    label("loc_D23")

    OP_64(0x0, 0x1)

    label("loc_D27")

    Jump("loc_D2E")

    label("loc_D2A")

    OP_64(0x0, 0x1)

    label("loc_D2E")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D72")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)

    label("loc_D72")

    OP_64(0x6, 0x1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA9")
    OP_65(0x6, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC4")
    OP_71(0x0, 0x10)
    OP_64(0x1, 0x1)

    label("loc_DC4")

    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE4")
    OP_65(0x7, 0x1)

    label("loc_DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF4")
    OP_64(0xD, 0x1)

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E04")
    OP_64(0x9, 0x1)

    label("loc_E04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E14")
    OP_64(0xE, 0x1)

    label("loc_E14")

    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    OP_64(0xC, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E35")
    OP_65(0xA, 0x1)

    label("loc_E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4A")
    OP_65(0xB, 0x1)

    label("loc_E4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5F")
    OP_65(0xC, 0x1)

    label("loc_E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7A")
    OP_65(0xA, 0x1)

    label("loc_E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E87")
    OP_65(0xB, 0x1)

    label("loc_E87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E94")
    OP_65(0xC, 0x1)

    label("loc_E94")

    Return()

    # Function_1_BB5 end

    def Function_2_E95(): pass

    label("Function_2_E95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_E95")

    label("loc_EAA")

    Return()

    # Function_2_E95 end

    def Function_3_EAB(): pass

    label("Function_3_EAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECE")
    OP_8D(0xFE, -105470, 104540, -101970, 99920, 3000)
    Jump("Function_3_EAB")

    label("loc_ECE")

    Return()

    # Function_3_EAB end

    def Function_4_ECF(): pass

    label("Function_4_ECF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EF2")
    OP_8D(0xFE, -106870, 104010, -102300, 99050, 3000)
    Jump("Function_4_ECF")

    label("loc_EF2")

    Return()

    # Function_4_ECF end

    def Function_5_EF3(): pass

    label("Function_5_EF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_F58")

    ChrTalk(    #0
        0xF,
        (
            "#690FThe Royal Army was indeed fast\x01",
            "in its reaction time.\x02\x03",

            "They must be desperate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1094")

    label("loc_F58")

    OP_A2(0xB)

    ChrTalk(    #1
        0xF,
        (
            "#690FThe Leibnitz is underground,\x01",
            "receiving an overhaul.\x02\x03",

            "We've made it through the most\x01",
            "dangerous parts, so we should\x01",
            "be fine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#803FThat's a relief, at least.\x02\x03",

            "#800FStill though...I was surprised myself\x01",
            "by how fast the Royal Army moved.\x02\x03",

            "They'd have had us if we'd been\x01",
            "the tiniest bit slower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1094")

    TalkEnd(0xFE)
    Return()

    # Function_5_EF3 end

    def Function_6_1098(): pass

    label("Function_6_1098")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1186")

    ChrTalk(    #3
        0xFE,
        (
            "I believe the Capel's\x01",
            "effectiveness was directly\x01",
            "related to the orbal shutdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I believe that when the orbments\x01",
            "shut down, it was able to do\x01",
            "a complete reset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "We could use that, as a new\x01",
            "maintenance technique...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1186")

    TalkEnd(0xFE)
    Return()

    # Function_6_1098 end

    def Function_7_118A(): pass

    label("Function_7_118A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1244")
    TalkBegin(0x13)

    ChrTalk(    #6
        0xFE,
        "Come to think of it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I've heard of a new photo exhibit\x01",
            "in the Museum of History about\x01",
            "the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If I could make the time I would\x01",
            "love to see it myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_1244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_12DA")
    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        (
            "I can't seem to find that\x01",
            "paperwork anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I truly believe we need to rethink\x01",
            "the filing system we use here in\x01",
            "the factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1417")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_137F")

    ChrTalk(    #11
        0xFE,
        (
            "I'm sure the Arseille is aching\x01",
            "to feel the wind beneath its\x01",
            "wings again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I hope we can keep the project\x01",
            "moving ahead at a brisk pace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1414")

    label("loc_137F")

    OP_A2(0x9)

    ChrTalk(    #13
        0xFE,
        (
            "So that young lady there is the\x01",
            "new member of the Orbal Engine\x01",
            "Project team?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "She looks like she'll be able to\x01",
            "hold her own well enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    Jump("loc_1A38")

    label("loc_1417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_149B")
    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        (
            "Thank goodness! The room \x01",
            "appears to be left intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "We should be able to resume\x01",
            "our work without a problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1758")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x346)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D7")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_154C")

    ChrTalk(    #17
        0xFE,
        (
            "This whole incident has reminded\x01",
            "me of one thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "...and that is just how much we\x01",
            "still do not understand about\x01",
            "orbal technology.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D4")

    label("loc_154C")

    OP_A2(0x9)

    ChrTalk(    #19
        0xFE,
        "Hmm...according to this data...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I've no doubts that during the\x01",
            "blackout all orbments suddenly\x01",
            "and utterly ceased activity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D4")

    Jump("loc_1755")

    label("loc_15D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F2")
    Call(1, 3)
    Jump("loc_1755")

    label("loc_15F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(    #21
        0xFE,
        (
            "This whole incident has reminded\x01",
            "me of one thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "...and that is just how much\x01",
            "we still do not understand\x01",
            "about orbal technology.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171D")

    label("loc_1695")

    OP_A2(0x9)

    ChrTalk(    #23
        0xFE,
        "Hmm...according to this data...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I've no doubts that during the\x01",
            "blackout all orbments suddenly\x01",
            "and utterly ceased activity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    Jump("loc_1755")

    label("loc_1720")


    ChrTalk(    #25
        0xFE,
        (
            "Hello! Is there anything I might\x01",
            "help you with?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1755")

    Jump("loc_1A38")

    label("loc_1758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1846")
    TalkBegin(0xFE)

    ChrTalk(    #26
        0xFE,
        (
            "Yesterday's event was quite\x01",
            "the surprising phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "As far as I know, this event is inexplicable\x01",
            "within the limits of our current knowledge\x01",
            "of orbal technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Okay, now where did I put\x01",
            "those documents...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_1846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_18DF")
    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "I can't find that blasted\x01",
            "paperwork anywhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "It might be faster to just pull out\x01",
            "all the blueprints and start over\x01",
            "from scratch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_18DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A38")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1987")

    ChrTalk(    #31
        0xFE,
        (
            "When I was returning from the\x01",
            "royal academy I got caught\x01",
            "up in that sky bandit affair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Thinking back on it gives me\x01",
            "chills, even today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A38")

    label("loc_1987")

    OP_A2(0x9)

    ChrTalk(    #33
        0xFE,
        (
            "Now where are those papers\x01",
            "I set aside before I left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Of course, by 'before,' I mean prior to\x01",
            "my trip to the royal academy...and that\x01",
            "was quite a while ago...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_1A38")

    TalkEnd(0xFE)
    Return()

    # Function_7_118A end

    def Function_8_1A3C(): pass

    label("Function_8_1A3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1AEA")

    ChrTalk(    #35
        0xFE,
        (
            "Y'know, I've got nothing but respect\x01",
            "for you bracers. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "You all jumped right into the Royal\x01",
            "Army's frying pan, just to rescue\x01",
            "Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8F")

    label("loc_1AEA")

    OP_A2(0x8)

    ChrTalk(    #37
        0xFE,
        "Hey there, you all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Thanks again for savin' ol' Russell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "What? He's fine, I tell ya!\x01",
            "Made o' solid stone, that guy.\x01",
            "He got out of there just fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8F")

    Jump("loc_2657")

    label("loc_1B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1C85")

    ChrTalk(    #40
        0xFE,
        (
            "Now, I don't see that\x01",
            "paperwork anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "How many times do I have to tell\x01",
            "that girl?! Constance, keep this\x01",
            "place in order, will ya?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "And she's already trotted herself\x01",
            "on home for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "This is a fix...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DE5")

    label("loc_1C85")

    OP_A2(0x8)

    ChrTalk(    #44
        0xFE,
        (
            "Thanks to the orbal shutdown,\x01",
            "the main clock's lost time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "To readjust it I need t' find the\x01",
            "records from when it was built,\x01",
            "but no luck finding 'em here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "How many times do I have to tell\x01",
            "that girl?! Constance, keep this\x01",
            "place in order, will ya?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "If we can't use this place when\x01",
            "we really need it, there ain't no\x01",
            "point havin' it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE5")

    Jump("loc_2657")

    label("loc_1DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1EBA")

    ChrTalk(    #48
        0xFE,
        (
            "Can't seem to find that book\x01",
            "I was needin' to read either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Been so busy worryin' about filling\x01",
            "my head I forgot to fill my stomach. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Better go get me some lunch\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB7")

    label("loc_1EBA")

    OP_A2(0x8)

    ChrTalk(    #51
        0xFE,
        (
            "Can't seem to find that book\x01",
            "I was needin' to read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "On the other hand, I did find\x01",
            "some other pretty fascinatin'\x01",
            "stuff to fill my time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Ooh, I'll have t' read this one\x01",
            "sometime, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "...and dang it if the book I need\x01",
            "ain't here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB7")

    Jump("loc_2657")

    label("loc_1FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_212F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_205A")
    TurnDirection(0x12, 0x10, 400)

    ChrTalk(    #55
        0xFE,
        "Constance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Think I could trouble ya to do\x01",
            "a little actual work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I mean, look at this place!\x01",
            "Books lyin' around all over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212C")

    label("loc_205A")

    OP_A2(0x8)

    ChrTalk(    #58
        0xFE,
        (
            "I came up here t' look up some stuff\x01",
            "about what happened yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "And look around!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "All this mess?! It's b'cause she\x01",
            "ain't doin' her job!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "And t' think she's gettin' paid\x01",
            "to do this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212C")

    Jump("loc_2657")

    label("loc_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_245F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_21F0")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #62
        0xFE,
        "Oh, hi there, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "You're lucky you had a couple\x01",
            "of bracers with you on that\x01",
            "last assignment, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "When I was younger, I got into\x01",
            "all kinds o' scrapes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_245C")

    label("loc_21F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 6)), scpexpr(EXPR_END)), "loc_228D")

    ChrTalk(    #65
        0xFE,
        (
            "Well, I've got some free time,\x01",
            "so I should get some researchin'\x01",
            "under m' belt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "It's gonna take a while wadin' \x01",
            "through all them theses. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_245C")

    label("loc_228D")

    OP_A2(0x8)
    OP_A2(0x586)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #67
        0xFE,
        "Hey, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "How'd it go changin' those lights\x01",
            "in the Kaldia Tunnel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        (
            "#065FWell, it...\x02\x03",

            "#067F...went okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "'Went okay'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "You did change the lights though,\x01",
            "didn't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x107,
        "#061FOh yes. I changed them all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Okay, then. Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "You're lucky you had a couple\x01",
            "of bracers with you on that\x01",
            "last assignment, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "When I was younger, I got into\x01",
            "all kinds o' scrapes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x107,
        (
            "#067FYes, I can imagine.\x02\x03",

            "#562FI'll be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245C")

    Jump("loc_2657")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2579")

    ChrTalk(    #77
        0xFE,
        (
            "Truth be told, Russell was s'posed\x01",
            "to head the new engine project to\x01",
            "the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "But for some reason, he went and started \x01",
            "up somethin' else after he finished \x01",
            "calibratin' the central power orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "As a result, the project ground\x01",
            "to a complete halt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2657")

    label("loc_2579")

    OP_A2(0x8)

    ChrTalk(    #80
        0xFE,
        (
            "That one fella quittin' ain't much\x01",
            "of a help either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Right now, the Arseille ain't much\x01",
            "more'n a gussied-up transport ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "We don't do somethin' about\x01",
            "finishin' it and all that time an'\x01",
            "work's wasted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2657")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A3C end

    def Function_9_265B(): pass

    label("Function_9_265B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2676")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #83
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()

    label("loc_2676")

    TalkEnd(0xFE)
    Return()

    # Function_9_265B end

    def Function_10_267A(): pass

    label("Function_10_267A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_26CF")

    ChrTalk(    #84
        0xFE,
        "Hello! \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "If I need your help again I'll\x01",
            "be giving you a call!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_26CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F67")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26FB")
    Call(1, 6)
    TalkEnd(0xFE)
    Return()

    label("loc_26FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_2716")
    Call(1, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_2716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2731")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_2731")
    Call(1, 10)
    TalkEnd(0xFE)
    Return()

    label("loc_2731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_274C")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_274C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_28DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(    #86
        0xFE,
        "Oh my, look at the time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "It's a little early, but I think\x01",
            "I'll take some brunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "The shops always get so\x01",
            "crowded right at lunchtime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DC")

    label("loc_27F4")

    OP_A2(0x4)

    ChrTalk(    #89
        0xFE,
        (
            "It finally looks like the factory\x01",
            "has calmed back down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "It was so crazy around here\x01",
            "I couldn't get any work done...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "...but I still managed to find a\x01",
            "way to get this place all cleaned\x01",
            "up under budget!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "*giggle*\x02",
    )

    CloseMessageWindow()

    label("loc_28DC")

    Jump("loc_2F64")

    label("loc_28DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_299F")

    ChrTalk(    #93
        0xFE,
        "Oh my, look at the time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "It's a little early, but I think\x01",
            "I'll take some brunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I skipped breakfast this morning\x01",
            "and that's really not very healthy\x01",
            "of me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A75")

    label("loc_299F")

    OP_A2(0x4)

    ChrTalk(    #96
        0xFE,
        (
            "It finally looks like the factory\x01",
            "has calmed back down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It was so crazy around here\x01",
            "I couldn't get any work done...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "...but at least I managed to get\x01",
            "some of this cleaned up and\x01",
            "stay under budget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A75")

    Jump("loc_2F64")

    label("loc_2A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2B56")

    ChrTalk(    #99
        0xFE,
        (
            "I'm sorry, but I've withdrawn\x01",
            "the contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "The Zeiss Guild branch will clean\x01",
            "up the rest later. Don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I'll be sure to call you if I need\x01",
            "any other help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "See you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E09")

    label("loc_2B56")

    OP_28(0x2D, 0x1, 0x8000)

    ChrTalk(    #103
        0xFE,
        "Oh, it's you! Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Oh, I've already withdrawn\x01",
            "the contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#004FHuh? How come?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I received a call from the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "You're being transferred to\x01",
            "another section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Before you move, they said to\x01",
            "finalize all work orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#014FI see...\x02\x03",

            "I apologize that we weren't able\x01",
            "to finish everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#003FWe're really sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "No, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "I'm sure there are more important\x01",
            "things than this for you to focus on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I'll just get the Zeiss Guild branch\x01",
            "to clean up the rest of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        "#010FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Well, take care!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I'll be sure to call you if I need\x01",
            "any other help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#000FOK, great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()

    label("loc_2E09")

    Jump("loc_2F64")

    label("loc_2E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2EC1")

    ChrTalk(    #119
        0xFE,
        "Oh my, look at the time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "It's a little early, but I think\x01",
            "I'll take some brunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I skipped breakfast this morning\x01",
            "and that's really not very healthy\x01",
            "of me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F64")

    label("loc_2EC1")

    OP_A2(0x4)

    ChrTalk(    #122
        0xFE,
        (
            "It finally looks like the factory\x01",
            "has calmed back down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "It was so crazy around here\x01",
            "I couldn't get any work done..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Let's start here in Archives!\x02",
    )

    CloseMessageWindow()

    label("loc_2F64")

    Jump("loc_41EB")

    label("loc_2F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3168")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F93")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F93")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_2F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_2FAE")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_2FAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_2FC9")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_2FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_2FE4")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_2FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30A2")

    ChrTalk(    #125
        0xFE,
        (
            "Hmm...it feels like something big\x01",
            "is going to happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Chief Murdock's left for somewhere,\x01",
            "all the repair crews are running\x01",
            "around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "It's so...busy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3165")

    label("loc_30A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30BB")
    Call(1, 4)
    Jump("loc_3165")

    label("loc_30BB")


    ChrTalk(    #128
        0xFE,
        (
            "Hmm...it feels like something big\x01",
            "is going to happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Chief Murdock's left for somewhere,\x01",
            "all the repair crews are running\x01",
            "around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "It's so...busy!\x02",
    )

    CloseMessageWindow()

    label("loc_3165")

    Jump("loc_41EB")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_331C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3194")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3194")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3194")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_31AF")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_31AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_31CA")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_31CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_31E5")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_31E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_323B")

    ChrTalk(    #131
        0xFE,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Here's hoping for at least one\x01",
            "quiet day, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3319")

    label("loc_323B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_32B7")

    ChrTalk(    #133
        0xFE,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Here's hoping for at least one\x01",
            "quiet day, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "I hope you can find that book...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3319")

    label("loc_32B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D0")
    Call(1, 4)
    Jump("loc_3319")

    label("loc_32D0")


    ChrTalk(    #136
        0xFE,
        "Good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Here's hoping for at least one\x01",
            "quiet day, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3319")

    Jump("loc_41EB")

    label("loc_331C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_35E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_33A5")

    ChrTalk(    #138
        0xFE,
        (
            "Ugh...the entire building still\x01",
            "smells like smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I'm finished for today. I don't care.\x01",
            "I'm just going home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DF")

    label("loc_33A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_342D")

    ChrTalk(    #140
        0xFE,
        (
            "Ugh...the entire building still\x01",
            "smells like smoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I'm finished for today. I don't care.\x01",
            "I'm just going home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_35DF")

    label("loc_342D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_34CA")

    ChrTalk(    #142
        0xFE,
        (
            "Ugh...the entire building smells\x01",
            "like smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "So, I'm just going home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Sorry. Can you bring me that\x01",
            "book tomorrow instead?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_35DF")

    label("loc_34CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3568")

    ChrTalk(    #145
        0xFE,
        (
            "Ugh...the entire building smells\x01",
            "like smoke now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "So, I'm just going home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "If you want to talk about that\x01",
            "job, ask me tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_35DF")

    label("loc_3568")


    ChrTalk(    #148
        0xFE,
        (
            "Thanks to all that running all\x01",
            "my muscles are sore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I'm finished for today. I don't care.\x01",
            "I'm going home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_35DF")

    Jump("loc_41EB")

    label("loc_35E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_384B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_360E")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_360E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3629")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3629")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3644")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_365F")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_365F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3751")

    ChrTalk(    #150
        0xFE,
        (
            "Oh, so that's the infamous\x01",
            "'Wilmont from Operations.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I've never even seen him before...\x01",
            "He doesn't look like much, does he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "You know, he looks like the kind\x01",
            "of guy who's always washing his\x01",
            "hands and stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3848")

    label("loc_3751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_376A")
    Call(1, 4)
    Jump("loc_3848")

    label("loc_376A")


    ChrTalk(    #153
        0xFE,
        (
            "Oh, so that's the infamous\x01",
            "'Wilmont from Operations.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I've never even seen him before...\x01",
            "He doesn't look like much, does he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "You know, he looks like the kind\x01",
            "of guy who's always washing his\x01",
            "hands and stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3848")

    Jump("loc_41EB")

    label("loc_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3877")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3877")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3877")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3892")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3892")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3892")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_38AD")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_38AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_38C8")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_38C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3939")

    ChrTalk(    #156
        0xFE,
        "Can't Igor just read quietly?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Doesn't he know anything about\x01",
            "how libraries work?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AF")

    label("loc_3939")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3952")
    Call(1, 4)
    Jump("loc_39AF")

    label("loc_3952")


    ChrTalk(    #158
        0xFE,
        "Can't Igor just read quietly?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Doesn't he know anything about\x01",
            "how libraries work?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AF")

    Jump("loc_41EB")

    label("loc_39B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3B51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39DE")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_39DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_39F9")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_39F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3A14")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3A2F")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ABC")

    ChrTalk(    #160
        0xFE,
        (
            "That's Igor over there. He's such\x01",
            "a pain in the butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I can totally see why he's lived\x01",
            "his entire life single.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B4E")

    label("loc_3ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD5")
    Call(1, 4)
    Jump("loc_3B4E")

    label("loc_3AD5")


    ChrTalk(    #162
        0xFE,
        (
            "That's Igor over there. He's such\x01",
            "a pain in the butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "I can totally see why he's lived\x01",
            "his entire life single.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4E")

    Jump("loc_41EB")

    label("loc_3B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3F1E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B7D")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3B98")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3B98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3BB3")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3BCE")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C87")

    ChrTalk(    #164
        0xFE,
        (
            "Well, if it isn't Tita and those two\x01",
            "bracers from before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Thank you SO much for collecting\x01",
            "those books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Thanks to you my to-do box is\x01",
            "nice and empty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1B")

    label("loc_3C87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3CF3")

    ChrTalk(    #167
        0xFE,
        (
            "If you find any of the books,\x01",
            "just please bring them back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "I'm counting on you guys!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1B")

    label("loc_3CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D0C")
    Call(1, 4)
    Jump("loc_3F1B")

    label("loc_3D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3D87")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #169
        0xFE,
        "You help out, too, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I get the feeling that I can't keep\x01",
            "this place in order all by myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1B")

    label("loc_3D87")

    OP_A2(0x4)

    ChrTalk(    #171
        0xFE,
        "Welcome to Archives!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DCA")

    ChrTalk(    #172
        0xFE,
        "Why, hello, Tita!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DEB")

    label("loc_3DCA")

    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #173
        0xFE,
        "Hey, it's you, Tita!\x02",
    )

    CloseMessageWindow()

    label("loc_3DEB")


    ChrTalk(    #174
        0x107,
        (
            "#060FHi, Constance. It's been such\x01",
            "a long time! How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "It has been a while, hasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "You should come help me\x01",
            "arrange books sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "I get the feeling that I can't keep\x01",
            "this place in order all by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x107,
        "#060FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "You're so nice and helpful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "See you soon!\x02",
    )

    CloseMessageWindow()

    label("loc_3F1B")

    Jump("loc_41EB")

    label("loc_3F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x340)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x341)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x342)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F43")
    Call(1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_3F43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x343)"), scpexpr(EXPR_END)), "loc_3F5E")
    Call(1, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_3F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x344)"), scpexpr(EXPR_END)), "loc_3F79")
    Call(1, 9)
    TalkEnd(0xFE)
    Return()

    label("loc_3F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x345)"), scpexpr(EXPR_END)), "loc_3F94")
    Call(1, 11)
    TalkEnd(0xFE)
    Return()

    label("loc_3F94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_403E")

    ChrTalk(    #181
        0xFE,
        "Well, if it isn't the bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "Thank you SO much for collecting\x01",
            "those books for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Go ahead and look through any\x01",
            "book that catches your eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41EB")

    label("loc_403E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_40C7")

    ChrTalk(    #184
        0xFE,
        (
            "Feel free to look through anything\x01",
            "of ours you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "If you find any of the books,\x01",
            "just please bring them back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41EB")

    label("loc_40C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40E0")
    Call(1, 4)
    Jump("loc_41EB")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4163")

    ChrTalk(    #186
        0xFE,
        (
            "Go ahead and look through any\x01",
            "book that catches your eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "And when you're finished, \x01",
            "put it back on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41EB")

    label("loc_4163")

    OP_A2(0x4)

    ChrTalk(    #188
        0xFE,
        "Ooh, a new face!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Welcome to Archives!\x01",
            "My name is Constance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "Go ahead and look through any\x01",
            "book that catches your eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EB")

    TalkEnd(0xFE)
    Return()

    # Function_10_267A end

    def Function_11_41EF(): pass

    label("Function_11_41EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_43AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_426D")

    ChrTalk(    #191
        0x8,
        (
            "#800FStill though...I was surprised myself\x01",
            "by how fast the Royal Army moved.\x02\x03",

            "They're really driven.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A5")

    label("loc_426D")

    OP_A2(0x3)
    OP_4A(0xF, 255)

    ChrTalk(    #192
        0xF,
        (
            "#690FThe Leibnitz is underground, \x01",
            "receiving an overhaul.\x02\x03",

            "We've handled the most dangerous\x01",
            "parts, so we should be fine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        (
            "#803FThat's a relief, at least.\x02\x03",

            "Still though...I was surprised myself\x01",
            "by how fast the Royal Army moved.\x02\x03",

            "They'd have had us if we'd been\x01",
            "the tiniest bit slower.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)

    label("loc_43A5")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_43AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4598")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43D6")
    SetChrSubChip(0xFE, 1)
    Jump("loc_43F1")

    label("loc_43D6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43EC")
    SetChrSubChip(0xFE, 0)
    Jump("loc_43F1")

    label("loc_43EC")

    SetChrSubChip(0xFE, 2)

    label("loc_43F1")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(    #194
        0x8,
        (
            "#803FAt any rate, we need to make\x01",
            "sure the Capel is hidden...\x02\x03",

            "And the only problem we'll have\x01",
            "left is the Leibnitz.\x02\x03",

            "#800FBut I'd bet money that Gustav's\x01",
            "got something up his sleeve for\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4590")

    label("loc_44CF")

    OP_A2(0x3)

    ChrTalk(    #195
        0x8,
        (
            "#802FEstelle, Joshua. I didn't know\x01",
            "you two were still here.\x02\x03",

            "#801FDon't worry about us. Even if\x01",
            "someone got in, they'd have\x01",
            "quite the welcome waiting.\x02\x03",

            "You need to get to the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4590")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_4598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_4A75")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45C1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_45DC")

    label("loc_45C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45D7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_45DC")

    label("loc_45D7")

    SetChrSubChip(0xFE, 2)

    label("loc_45DC")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_465D")

    ChrTalk(    #196
        0x8,
        (
            "#800FPlease bring back Professor\x01",
            "Russell safely, for Tita's sake.\x02\x03",

            "We'll be waiting for news.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4833")

    label("loc_465D")

    OP_A2(0x3)

    ChrTalk(    #197
        0x8,
        (
            "#800FGood morning.\x02\x03",

            "Got anything yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#002FNot yet. We're off to the guild to\x01",
            "see what kind of information we\x01",
            "can gather now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        "#802FTita's not with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x102,
        (
            "#015FShe went to the clinic to check\x01",
            "up on Agate.\x02\x03",

            "She's very worried about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "#803FI see...\x02\x03",

            "Please bring back Professor\x01",
            "Russell safely, for Tita's sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        "#002FWe will, I promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        (
            "#010FWe'll do our absolute best.\x02\x03",

            "Now if you'll excuse us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x8,
        "#800FWe'll be waiting for news.\x02",
    )

    CloseMessageWindow()

    label("loc_4833")

    Jump("loc_4A6D")

    label("loc_4836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48AA")

    ChrTalk(    #205
        0x8,
        (
            "#800FSome useful clues, huh...\x02\x03",

            "Well, we're counting on you.\x01",
            "Please bring back the\x01",
            "professor safely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6D")

    label("loc_48AA")

    OP_A2(0x3)

    ChrTalk(    #206
        0x8,
        "#800FHi. Find any clues yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        "#505FWell, we've got some leads...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#015FI'm sorry, Mr. Murdock.\x02\x03",

            "We're still investigating the\x01",
            "situation, so we shouldn't\x01",
            "discuss anything just yet.\x02\x03",

            "#012FWe do, however, have quite a\x01",
            "useful clue that may lead us\x01",
            "to the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "#802FIs that right, now?!\x02\x03",

            "#801FThen we can expect some big\x01",
            "things from you, I guess.\x02\x03",

            "We'll be waiting for news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#000FYou bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        "#010FNow if you'll excuse us...\x02",
    )

    CloseMessageWindow()

    label("loc_4A6D")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_4E9E")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A9E")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4AB9")

    label("loc_4A9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AB4")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4AB9")

    label("loc_4AB4")

    SetChrSubChip(0xFE, 2)

    label("loc_4AB9")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B17")

    ChrTalk(    #212
        0x8,
        (
            "#800FCan you two afford to be standing\x01",
            "around talking?\x02\x03",

            "Get going!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E96")

    label("loc_4B17")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_4BAA")

    ChrTalk(    #213
        0x8,
        (
            "#800FYour injured bracer friend was\x01",
            "taken to the clinic.\x02\x03",

            "I don't think you can afford to stand\x01",
            "around here talking.\x02\x03",

            "Get going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E96")

    label("loc_4BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_4D50")

    ChrTalk(    #214
        0x8,
        (
            "#800FHello there.\x02\x03",

            "That other injured bracer is upstairs\x01",
            "in the clinic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        (
            "#012FYes, we've heard that he's been\x01",
            "poisoned. Something rare and\x01",
            "very dangerous...\x02\x03",

            "We just talked to Father Vixen\x01",
            "about an anti-poison treatment.\x02\x03",

            "We need to go to the Limestone\x01",
            "Cave and collect some of the\x01",
            "ingredients he needs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "#800FI see. Then you shouldn't be\x01",
            "standing around talking.\x02\x03",

            "Get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x102,
        "#012FVery well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E96")

    label("loc_4D50")


    ChrTalk(    #218
        0x8,
        (
            "#800FHello there.\x02\x03",

            "That other injured bracer is\x01",
            "upstairs in the clinic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        (
            "#012FYes, we've heard that he's been\x01",
            "poisoned. Something rare and\x01",
            "very dangerous...\x02\x03",

            "We're on our way to talk to\x01",
            "Father Vixen about treatment\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x8,
        (
            "#800FI see. Then you shouldn't be\x01",
            "standing around talking.\x02\x03",

            "Get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        "#012FVery well.\x02",
    )

    CloseMessageWindow()

    label("loc_4E96")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_4E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_4FA2")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EC7")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4EE2")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EDD")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4EE2")

    label("loc_4EDD")

    SetChrSubChip(0xFE, 2)

    label("loc_4EE2")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #222
        0x8,
        (
            "#800FI decided we should keep the news\x01",
            "about Professor Russell secret for\x01",
            "the time being.\x02\x03",

            "It should make it easier for you to\x01",
            "do what you need to.\x02\x03",

            "Please, find him.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_4FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_522E")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FCB")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4FE6")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FE1")
    SetChrSubChip(0xFE, 0)
    Jump("loc_4FE6")

    label("loc_4FE1")

    SetChrSubChip(0xFE, 2)

    label("loc_4FE6")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50AD")

    ChrTalk(    #223
        0x8,
        (
            "#803FI decided we should keep the news\x01",
            "about Professor Russell secret for\x01",
            "the time being.\x02\x03",

            "#800FIt should make it easier for you\x01",
            "to do what you need to.\x02\x03",

            "Please, find him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5226")

    label("loc_50AD")

    OP_A2(0x3)

    ChrTalk(    #224
        0x8,
        (
            "#803F...\x02\x03",

            "...I've decided to keep the news\x01",
            "about Professor Russell secret\x01",
            "for the time being.\x02\x03",

            "It should make it easier for you\x01",
            "to do what you need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x102,
        "#015FThat was a wise decision.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        (
            "#003FYeah, we wouldn't want to\x01",
            "start a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x8,
        (
            "#800FPlease find Professor Russell.\x02\x03",

            "And Tita, keep your chin up.\x02\x03",

            "I'm sure the professor's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x107,
        (
            "#063FYes, sir...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5226")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_522E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5291")

    ChrTalk(    #229
        0x8,
        (
            "#800FPlease take care of Tita while\x01",
            "she's out there.\x02\x03",

            "Tita, you be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5466")

    label("loc_5291")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52B3")
    SetChrSubChip(0xFE, 1)
    Jump("loc_52CE")

    label("loc_52B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52C9")
    SetChrSubChip(0xFE, 0)
    Jump("loc_52CE")

    label("loc_52C9")

    SetChrSubChip(0xFE, 2)

    label("loc_52CE")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_53A0")

    ChrTalk(    #230
        0x8,
        (
            "#805FHello. Sorry about before.\x02\x03",

            "I plan to take a long rest after\x01",
            "this and kick this smoking habit\x01",
            "of mine.\x02\x03",

            "#800FI'm counting on you two to watch\x01",
            "out for Tita on the way to Elmo.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5461")

    label("loc_53A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_53CF")

    ChrTalk(    #231
        0x8,
        "#805FDid you find anything?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5461")

    label("loc_53CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F1")
    SetChrSubChip(0xFE, 0)
    Call(1, 2)
    Jump("loc_5461")

    label("loc_53F1")


    ChrTalk(    #232
        0x8,
        (
            "#800FAnything the matter?\x02\x03",

            "You can get to the Elmo Hot\x01",
            "Springs by using the gate at\x01",
            "the south end of town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5461")

    SetChrSubChip(0xFE, 0)

    label("loc_5466")

    Jump("loc_5BE9")

    label("loc_5469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_556A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_54E8")

    ChrTalk(    #233
        0x8,
        (
            "#800FI heard that Clive from Ruan\x01",
            "turned us down.\x02\x03",

            "Finding a replacement for him\x01",
            "isn't going to be easy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5567")

    label("loc_54E8")

    OP_A2(0x3)

    ChrTalk(    #234
        0x8,
        (
            "#800FHello, Hugo!\x02\x03",

            "I heard that Clive from Ruan\x01",
            "turned us down.\x02\x03",

            "Finding a replacement for him\x01",
            "isn't going to be easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5567")

    Jump("loc_5BE9")

    label("loc_556A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5AC7")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5593")
    SetChrSubChip(0xFE, 1)
    Jump("loc_55AE")

    label("loc_5593")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55A9")
    SetChrSubChip(0xFE, 0)
    Jump("loc_55AE")

    label("loc_55A9")

    SetChrSubChip(0xFE, 2)

    label("loc_55AE")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 4)), scpexpr(EXPR_END)), "loc_5677")

    ChrTalk(    #235
        0x8,
        (
            "#800FThe professor should be in his\x01",
            "workshop, up on 3.\x02\x03",

            "#805FDon't get him all worked up.\x02\x03",

            "#806FIf we have a repeat of yesterday\x01",
            "we won't be able to do anything\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABF")

    label("loc_5677")

    OP_A2(0x584)
    OP_28(0x3F, 0x1, 0x40)

    ChrTalk(    #236
        0x8,
        "#800FGood morning, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        "#001FGood morning, Mr. Murdock!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x107,
        "#560FGood morning, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x8,
        (
            "#805FWhat a day yesterday was.\x02\x03",

            "We've been getting complaints\x01",
            "from the citizens all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#506FWow, that's rough.\x02\x03",

            "It's not like it was your fault\x01",
            "or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#017FWe're very sorry, sir.\x02\x03",

            "We didn't mean to cause...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        (
            "#802FNo, no, no. Don't apologize.\x02\x03",

            "These kinds of things happen\x01",
            "when you're doing science.\x02\x03",

            "#803FIt happens a little bit more\x01",
            "often around Professor\x01",
            "Russell's science, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        (
            "#501FSpeaking of the professor,\x01",
            "has he come in already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x8,
        (
            "#800FOh yes. He came in very early\x01",
            "this morning, all fired up about\x01",
            "something.\x02\x03",

            "He probably needs some assistance,\x01",
            "so go on up to his workshop and see\x01",
            "him.\x02\x03",

            "It's on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x102,
        (
            "#010FThe third floor...\x02\x03",

            "Let's go, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#000FI've got a bad feeling about this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x8,
        "#800FBy the way, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x107,
        "#064FSir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        (
            "#805FPlease don't get the professor\x01",
            "too excited.\x02\x03",

            "#806FIf we have a repeat of yesterday\x01",
            "we won't be able to do anything\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x107,
        (
            "#065FI understand, sir.\x02\x03",

            "#060FI'll be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABF")

    SetChrSubChip(0xFE, 0)
    Jump("loc_5BE9")

    label("loc_5AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5BE9")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AF0")
    SetChrSubChip(0xFE, 1)
    Jump("loc_5B0B")

    label("loc_5AF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B06")
    SetChrSubChip(0xFE, 0)
    Jump("loc_5B0B")

    label("loc_5B06")

    SetChrSubChip(0xFE, 2)

    label("loc_5B0B")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #251
        0x8,
        (
            "#802FAnything the matter?\x02\x03",

            "The professor's private facility is\x01",
            "on the southwest corner of town.\x02\x03",

            "#801FIf you learn anything please\x01",
            "let me know.\x02\x03",

            "I have to admit part of this is\x01",
            "intensely fascinating.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_5BE9")

    TalkEnd(0xFE)
    Return()

    # Function_11_41EF end

    def Function_12_5BED(): pass

    label("Function_12_5BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_5D8B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C95")
    OP_A2(0x0)

    ChrTalk(    #252
        0xFE,
        (
            "I just finished a meeting about\x01",
            "the new orbal engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "I guess I was overdoing it a bit\x01",
            "with that anxiety attack about\x01",
            "my idea block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D85")

    label("loc_5C95")


    ChrTalk(    #254
        0xFE,
        (
            "Well, I've heard that inspiration\x01",
            "can come on a full stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "And what do you know, but while\x01",
            "I was having some soup yesterday\x01",
            "I had a flash!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "So I guess I'll be calling Ursus\x01",
            "to make me soup every time I'm\x01",
            "stuck for an idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D85")

    TalkEnd(0xFE)
    Jump("loc_642E")

    label("loc_5D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6176")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_44(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601C")
    OP_A2(0x2)

    ChrTalk(    #257
        0xC,
        (
            "Upgrading the orbment mechanism or the wing\x01",
            "cross-section isn't going to result in a further\x01",
            "increase to the ship's propulsion coefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xC,
        (
            "Therefore, I believe we should shift\x01",
            "our design focus from performance\x01",
            "to accessibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xC,
        (
            "I propose we reposition the essential mechanics\x01",
            "along the current lines of the ship's fairing,\x01",
            "according to their respective maintenance needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xE,
        (
            "I see...maximize the potential of the\x01",
            "Arseille's current aerodynamics while\x01",
            "facilitating usability. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xE,
        (
            "An interesting perspective. High efficiency\x01",
            "within a predetermined performance range\x01",
            "is something we haven't been examining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_616D")

    label("loc_601C")


    ChrTalk(    #262
        0xFE,
        (
            "We've proven this engine's technical\x01",
            "prowess already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "Once we incorporate the professor's newest\x01",
            "central drive orbment, I'm sure it will exceed\x01",
            "any of our performance estimates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "Therefore, I think working to streamline those\x01",
            "limits to work within current design parameters\x01",
            "will yield the highest net performance benefits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616D")

    OP_85(0xE)
    TalkEnd(0xFE)
    Jump("loc_642E")

    label("loc_6176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_642E")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635E")
    OP_A2(0x1)

    ChrTalk(    #265
        0xD,
        (
            "Hmm...I think we should compact\x01",
            "the barrel more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xD,
        (
            "We're not taking full advantage of\x01",
            "the high orbal pressure threshold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xC,
        "Yes, sir, that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xC,
        (
            "But won't doing so make the\x01",
            "overall unit too top-heavy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xC,
        (
            "I believe this configuration is\x01",
            "better given its current housing\x01",
            "and balance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xD,
        (
            "That may be true, but it's not \x01",
            "part of my design philosophy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xD,
        (
            "I'm trying to maximize output\x01",
            "within our technical limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xC,
        "Y-Yes, sir...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6427")

    label("loc_635E")


    ChrTalk(    #273
        0xC,
        "It's just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xC,
        (
            "Shouldn't we also factor usability\x01",
            "into our design?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xD,
        "That lowers efficiency.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xD,
        (
            "Louise, we need you to start\x01",
            "pushing limits more like a\x01",
            "proper engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xC,
        "Y-Yes, sir...\x02",
    )

    CloseMessageWindow()

    label("loc_6427")

    OP_4B(0xD, 255)
    TalkEnd(0xFE)

    label("loc_642E")

    Return()

    # Function_12_5BED end

    def Function_13_642F(): pass

    label("Function_13_642F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6701")
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6612")
    OP_A2(0x1)

    ChrTalk(    #278
        0xD,
        (
            "Hmm...I think we should compact\x01",
            "the barrel more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xD,
        (
            "We're not taking full advantage of\x01",
            "the high orbal pressure threshold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xC,
        "Yes, sir, that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xC,
        (
            "But won't doing so make the\x01",
            "overall unit too top-heavy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "I believe this configuration is\x01",
            "better given its current housing\x01",
            "and balance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xD,
        (
            "That may be true, but it's not \x01",
            "part of my design philosophy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xD,
        (
            "I'm trying to maximize output\x01",
            "within our technical limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xC,
        "Y-Yes, sir...\x02",
    )

    CloseMessageWindow()
    Jump("loc_66FA")

    label("loc_6612")


    ChrTalk(    #286
        0xC,
        "It's just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xC,
        (
            "Shouldn't we also factor usability\x01",
            "into our design?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xD,
        "That lowers efficiency.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xD,
        (
            "Louise, we need you to start\x01",
            "pushing limits more like a\x01",
            "proper engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xD,
        (
            "(This is your last chance,\x01",
            "get it together!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66FA")

    OP_4B(0xC, 255)
    Jump("loc_695A")

    label("loc_6701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_67E7")

    ChrTalk(    #291
        0xFE,
        "So...she's to be transferred.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "I hear she'll be working on\x01",
            "airships, like she's always\x01",
            "wanted. Good for her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "I shouldn't think of this as\x01",
            "a setback.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "I've got to get this new orbal\x01",
            "gun into production!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_695A")

    label("loc_67E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_695A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6892")

    ChrTalk(    #295
        0xFE,
        (
            "Oh, she's a dedicated and highly\x01",
            "experienced researcher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "Putting her on a project she really\x01",
            "wants to work on can only be good\x01",
            "for the factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_695A")

    label("loc_6892")

    OP_A2(0x5)

    ChrTalk(    #297
        0xFE,
        (
            "Louise...? She's an exemplary\x01",
            "researcher and scientist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "But...she's losing her drive\x01",
            "working on orbal weapons \x01",
            "research and design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "I agree with her transfer.\x01",
            "It'll be good for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_695A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_13_642F end

    def Function_14_6963(): pass

    label("Function_14_6963")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_6AFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6A0F")

    ChrTalk(    #300
        0xFE,
        (
            "Karl is quite an accomplished\x01",
            "scientist himself, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "He should be able to continue\x01",
            "his work on orbal weaponry\x01",
            "without too much trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AFC")

    label("loc_6A0F")

    OP_A2(0x6)

    ChrTalk(    #302
        0xFE,
        (
            "At first I had my doubts, but\x01",
            "the Orbal Engine Project is\x01",
            "progressing fantastically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "The new transfer, Louise, is doing\x01",
            "a marvelous job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "I feel bad for Karl losing such a\x01",
            "talented assistant, but she is\x01",
            "invaluable here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AFC")

    Jump("loc_769C")

    label("loc_6AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_6B98")

    ChrTalk(    #305
        0xFE,
        (
            "I daresay this has been the first\x01",
            "meeting that's ended well in a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "Or at least, ended with a feeling\x01",
            "of some real progress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_769C")

    label("loc_6B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_6EE9")
    OP_44(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E1F")
    OP_A2(0x2)

    ChrTalk(    #307
        0xC,
        (
            "Upgrading the orbment mechanism or the wing\x01",
            "cross-section isn't going to result in further\x01",
            "increase to the ship's propulsion coefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xC,
        (
            "Therefore, I believe we should shift\x01",
            "our design focus from performance\x01",
            "to accessibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xC,
        (
            "I propose we reposition the essential mechanics\x01",
            "along the current lines of the ship's fairing,\x01",
            "according to their respective maintenance needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xE,
        (
            "I see...maximize the potential of the\x01",
            "Arseille's current aerodynamics while\x01",
            "facilitating usability. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xE,
        (
            "An interesting perspective. High efficiency\x01",
            "within a predetermined performance range\x01",
            "is something we haven't been examining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EE3")

    label("loc_6E1F")


    ChrTalk(    #312
        0xFE,
        (
            "It's obviously still in the concept\x01",
            "stages, but a fascinating design\x01",
            "direction nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "Honestly, we've never thought about\x01",
            "reconfiguring our internal design to\x01",
            "favor accessibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EE3")

    OP_85(0xC)
    Jump("loc_769C")

    label("loc_6EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_700D")

    ChrTalk(    #314
        0xFE,
        (
            "I've decided to bring young Louise\x01",
            "aboard the Orbal Engine Project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "It will no doubt be a challenge,\x01",
            "both for her and for all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "I understand we need to bring\x01",
            "some of our younger minds\x01",
            "into our research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "...but it makes me nervous.\x01",
            "Hmm...oh, my stomach...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_769C")

    label("loc_700D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_708E")

    ChrTalk(    #318
        0xFE,
        "Thank you for your time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "I'd like to talk about the new\x01",
            "Orbal Engine Project we're\x01",
            "running for the Arseille.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_769C")

    label("loc_708E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_7261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7119")

    ChrTalk(    #320
        0xFE,
        (
            "I think it's time we gave the\x01",
            "opportunity to Louise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "If you agree, I'll take our proposal\x01",
            "to Murdock right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725E")

    label("loc_7119")

    OP_A2(0x6)

    ChrTalk(    #322
        0xFE,
        (
            "I know you're probably busy due\x01",
            "to last night, Karl, but I wonder if\x01",
            "I could have a word?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "I want to discuss Louise. Her\x01",
            "original application stated a\x01",
            "desire to work on airships...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "If possible, I'd like to move her\x01",
            "to work on the Arseille's Orbal \x01",
            "Engine Project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "What do you think,\x01",
            "as her supervisor?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_725E")

    Jump("loc_769C")

    label("loc_7261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_74C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7376")

    ChrTalk(    #326
        0xFE,
        (
            "The Arseille was designed to be the\x01",
            "prototype for a new model of engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "The engine it's running now isn't\x01",
            "even close to showing her\x01",
            "projected performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "I think we may need a fresh\x01",
            "point of view on it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x11, 400)

    ChrTalk(    #329
        0xFE,
        "What do you think, Antoine?\x02",
    )

    CloseMessageWindow()
    Jump("loc_74BE")

    label("loc_7376")

    OP_A2(0x6)

    ChrTalk(    #330
        0xFE,
        (
            "We need a researcher who can\x01",
            "help work on the Arseille's new\x01",
            "experimental engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "It's the center of the ship's design,\x01",
            "so we can't have just anyone\x01",
            "working in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "It won't be easy to find such a\x01",
            "person, but we can't leave the\x01",
            "Arseille's engine as is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "I think we may need a fresh\x01",
            "point of view on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74BE")

    Jump("loc_769C")

    label("loc_74C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_769C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7599")

    ChrTalk(    #334
        0xFE,
        (
            "Clive has announced his wish to\x01",
            "stay in Ruan, to take care of his\x01",
            "younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "I believe his actual wishes were to\x01",
            "come here and work with us, but I\x01",
            "certainly can't fault his decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_769C")

    label("loc_7599")

    OP_A2(0x6)

    ChrTalk(    #336
        0xFE,
        (
            "*sigh* This new engine for the\x01",
            "Arseille is turning into quite a\x01",
            "formidable problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "We were waiting for Clive in Ruan\x01",
            "to join in collaborative research,\x01",
            "but he declined our offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        (
            "And as things currently stand,\x01",
            "we're unable to move forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_769C")

    TalkEnd(0xFE)
    Return()

    # Function_14_6963 end

    def Function_15_76A0(): pass

    label("Function_15_76A0")

    EventBegin(0x0)
    OP_6D(1050, 0, 2760, 0)
    AddParty(0x6, 0xFF)
    SetChrPos(0x101, -200, 0, 1000, 0)
    SetChrPos(0x102, -1600, 0, 900, 0)
    SetChrSubChip(0x8, 2)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x107, -1100, 0, -1600, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #339
        0x8,
        (
            "#801F#3PHey, I've been waiting for you\x01",
            "two. Estelle and Joshua, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#000FUh, yes!\x01",
            "It's nice to meet you, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        (
            "#010FWe're sorry to bother\x01",
            "you at work like this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77C8():
        OP_6D(2680, 0, 4730, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77C8)

    def lambda_77E0():
        OP_8E(0xFE, 0xA32, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77E0)
    Sleep(500)

    def lambda_7800():
        OP_8E(0xFE, 0x6A4, 0x0, 0xBEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7800)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x8, 0)

    def lambda_7825():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7825)
    WaitChrThread(0x102, 0x1)

    def lambda_7838():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7838)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #342
        0x8,
        (
            "#800FNo, don't worry yourselves\x01",
            "about that.\x02\x03",

            "The Bracer Guild...and Cassius\x01",
            "in particular...have done a\x01",
            "great deal for me in the past.\x02\x03",

            "It would be rude of me not\x01",
            "to welcome his children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        (
            "#004FHuh?!\x02\x03",

            "You know Dad?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x8,
        (
            "#803FI guess you might say that.\x01",
            "He was my benefactor.\x02\x03",

            "#800FIt's no exaggeration to say that\x01",
            "the central factory produces the\x01",
            "finest orbments in the land.\x02\x03",

            "Naturally, the confrontations\x01",
            "over our craft have never\x01",
            "really stopped.\x02\x03",

            "Whenever we had a problem, we'd\x01",
            "always contact the Rolent branch\x01",
            "and have him come over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        "#501FI... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x102,
        (
            "#019FHeh. That explains all the\x01",
            "'business trips' then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x8,
        (
            "#801FAnd now, my benefactor's kids\x01",
            "come to visit me themselves.\x02\x03",

            "So what can I do for you?\x01",
            "I'm happy to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x101,
        "#008FHee hee... Thanks, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x102,
        "#012FIt's kind of a long story...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #350
        (
            "\x07\x05Joshua and Estelle explained to Murdock about the events surrounding the\x01",
            "mysterious Black Orbment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #351
        0x8,
        (
            "#800FI see... Well, then...\x02\x03",

            "Would you mind if I had\x01",
            "a look at this orbment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        "#006FSure, no problem.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #353
        "\x07\x05Estelle produced the Black Orbment and handed it to the factory chief.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0x15, 2290, 800, 4650, 0)
    ClearChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(    #354
        0x8,
        (
            "#802FHmm... Now, this certainly\x01",
            "is an oddity.\x02\x03",

            "It's obviously made from modern\x01",
            "materials, but the caliber isn't\x01",
            "inscribed anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        "#505F...Caliber?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        (
            "#014FYou mean the numbers that are\x01",
            "carved into the orbment's frame?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x8,
        (
            "#800FExactly.\x02\x03",

            "It's almost unheard of for an\x01",
            "orbment to be produced without\x01",
            "them.\x02\x03",

            "That's not just in Liberl, either.\x01",
            "Most other nations on the continent\x01",
            "are the same way.\x02\x03",

            "It's been a tradition dating\x01",
            "back to when the orbments were\x01",
            "first invented, fifty years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#501FHuh... You don't say.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #359
        "\x07\x05Estelle took out her combat orbment and eyeballed it suspiciously.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #360
        0x101,
        (
            "#004F...You're right.\x02\x03",

            "There are numbers, right there.\x01",
            "Crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x102,
        (
            "#017F*sigh*... You mean to say that\x01",
            "you've NEVER noticed, in all\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x101,
        (
            "#509FOh, you hush!\x02\x03",

            "#501FBut seriously, is it really that\x01",
            "strange for one to have no\x01",
            "caliber on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x8,
        (
            "#803FIt's pretty much a part of the\x01",
            "production process, and that\x01",
            "goes for any orbal factory.\x02\x03",

            "It's as if this one were a\x01",
            "prototype or something...\x02\x03",

            "#800FIf so, I'd imagine it wasn't made\x01",
            "to entertain at birthday parties,\x01",
            "if you take my meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        (
            "#002FSo...less with the sweet\x01",
            "and awesome, more with\x01",
            "the stabby-hurty. Got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x8,
        (
            "#800FOf course, I can't say for certain\x01",
            "without looking inside.\x02\x03",

            "#802F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x102,
        "#010FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x8,
        (
            "#805FBah... I can't find the \x01",
            "maintenance cover.\x02\x03",

            "And now that I really look at it,\x01",
            "it has no seams to it at all. How\x01",
            "the hell was this thing made?\x02\x03",

            "Hmm... I don't see any way to\x01",
            "check out the inside of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        (
            "#007FAw, man...\x02\x03",

            "#501FWould it be possible to cut\x01",
            "it open?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x8,
        (
            "#805FThat might work, yes...\x02\x03",

            "...but I'd hate to just break\x01",
            "something belonging to Cassius\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        "#003FOh... Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x102,
        (
            "#013F...\x02\x03",

            "#015FMaybe we should let that\x01",
            "professor handle it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #372
        0x101,
        (
            "#004FOh, right...the one mentioned\x01",
            "in the note...\x02\x03",

            "#006FYeah, he should be able\x01",
            "to tell us something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x8,
        "#802F...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #374
        0x101,
        (
            "#002FThere was a note that was\x01",
            "included with the orbment.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #375
        "\x07\x05Estelle showed Murdock the note that was in the package for Cassius.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #376
        0x8,
        (
            "#802F'Please ask Professor R to\x01",
            "do an analysis...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x102,
        (
            "#012FYou wouldn't happen to know\x01",
            "who this 'Professor R' is,\x01",
            "would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x8,
        (
            "#802FWell, let me think...\x02\x03",

            "From the letter R, and the people\x01",
            "that Cassius knew... It must be\x01",
            "Professor Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x102,
        "#015FI thought so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #380
        0x101,
        (
            "#004FWho's Professor Russell?\x02\x03",

            "And wait a second...\x01",
            "How do YOU know this guy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)
    CloseMessageWindow()

    ChrTalk(    #381
        0x102,
        (
            "#010F#5PI don't, but I know OF him.\x02\x03",

            "He's known as the person who brought orbal\x01",
            "technology to Liberl in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x8,
        "#800FHey, you know your stuff.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #383
        0x8,
        (
            "#803FAs I'm sure you know, orbments were invented by\x01",
            "Professor Epstein.\x02\x03",

            "And Professor Russell was one of his disciples.\x02\x03",

            "Forty years ago, he brought the orbments and\x01",
            "his knowledge back, and that's why Liberl is\x01",
            "a technologically advanced nation.\x02\x03",

            "#800FYou might say that he was the\x01",
            "father of the Orbal Revolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#004FWow... Now, that IS impressive.\x02\x03",

            "#007FMan, I had no idea that Dad\x01",
            "knew anyone like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x8,
        (
            "#803FEven so, it worries me a little\x01",
            "that you'll be letting the old\x01",
            "prof...uh, handle this orbment.\x02\x03",

            "We have no idea what\x01",
            "it is, really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x8,
        (
            "#805FWell, how to put this...\x01",
            "For good or ill, he's a certified genius.\x02\x03",

            "When he gets an idea for a new invention in his\x01",
            "head, there's just no telling what he'll do.\x02\x03",

            "#806FMuch like the time when he was developing the\x01",
            "first orbal airship.\x02\x03",

            "#806F*sigh*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        "#506F(Uh, what's with the far-off look...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x102,
        "#015F(I guess that a lot's happened...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#803FAhem! Sorry.\x02\x03",

            "#800FI'm sure that he'll be able\x01",
            "to figure this thing out.\x02\x03",

            "Go find him and ask him\x01",
            "about it. It can't hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        "#006FThanks, Chief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        "#010FWhere should we go to find him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x8,
        (
            "#800FHmmm...\x01",
            "Hold on a moment.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x8, 1720, 0, 5540, 270)
    OP_0D()
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0x550, 0x0, 0x1C52, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #394
        "\x07\x05Murdock flipped the switch on the intercom.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #395
        0x8,
        (
            "#800FTesting, testing...\x01",
            "Ah, good.\x02\x03",

            "Actually, I've been looking for you.\x02\x03",

            "Sorry to bother you, but\x01",
            "can you come here?\x02\x03",

            "#801FAll right. I'll be waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        (
            "#000FWhat, did you just call the\x01",
            "professor, or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x6B8, 0x0, 0x15A4, 0x7D0, 0x0)

    ChrTalk(    #397
        0x8,
        (
            "#800FOh, no, no.\x02\x03",

            "He actually has a private\x01",
            "workshop in town.\x02\x03",

            "He has all the latest technology at\x01",
            "his disposal, so I know he can figure\x01",
            "out something about that thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x101,
        (
            "#501FWow...\x01",
            "He really must be a genius.\x02\x03",

            "#505F...Wait. Then who did you call?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x8,
        (
            "#801FHis granddaughter. She works\x01",
            "here at the factory.\x02\x03",

            "I'm sure the child will be happy\x01",
            "to show you the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x101,
        "#004FThe 'child'?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #401
        0x107,
        "Girl's Voice",
        "#1PUm, excuse me...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)

    def lambda_8F30():
        OP_6D(1170, 0, 3070, 2000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_8F30)

    def lambda_8F48():

        label("loc_8F48")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_8F48")

    QueueWorkItem2(0x101, 1, lambda_8F48)

    def lambda_8F59():

        label("loc_8F59")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_8F59")

    QueueWorkItem2(0x102, 1, lambda_8F59)
    ClearChrFlags(0x107, 0x80)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8F7A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_8F7A)
    OP_8E(0x107, 0xFFFFFCE0, 0x0, 0x4B0, 0xBB8, 0x0)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #402
        0x101,
        "#004F#4PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x102,
        "#014F#4PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x107,
        "#064FOh... Estelle and Joshua?\x02",
    )

    CloseMessageWindow()

    def lambda_8FF4():
        OP_6D(2680, 0, 4730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FF4)

    def lambda_900C():
        OP_8E(0xFE, 0x190, 0x0, 0xC62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_900C)
    WaitChrThread(0x107, 0x2)
    TurnDirection(0x107, 0x101, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #405
        0x8,
        (
            "#802FYou mean that you know\x01",
            "each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        (
            "#006F#2PYeah... We only just met a\x01",
            "little while ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x102,
        (
            "#010F#2PSo then, I guess that she's\x01",
            "the professor's granddaughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x8,
        "#800FExactly.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)
    Sleep(400)

    ChrTalk(    #409
        0x8,
        (
            "#800FTita.\x02\x03",

            "I've been talking with Estelle\x01",
            "and Joshua here...\x02\x03",

            "#800FI'd like for you to show them\x01",
            "the way to your house.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #410
        0x107,
        (
            "#560FTo see Grandpa...\x01",
            "Okay, I will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x8,
        "#801FI appreciate it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x107, 0x101, 400)
    Sleep(400)

    ChrTalk(    #412
        0x8,
        (
            "#800FAh, yes. If you learn anything \x01",
            "new, I'd love it if you came\x01",
            "back and told me.\x02\x03",

            "As an engineer, I'm extremely \x01",
            "curious to know more about this.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #413
        0x101,
        "#001FHa ha ha. Sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x102,
        "#010FIf you'll excuse us, then...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x3F, 0x1, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3114   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_76A0 end

    def Function_16_92FA(): pass

    label("Function_16_92FA")

    EventBegin(0x0)
    OP_A2(0x54A)
    OP_64(0x0, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(-101920, 0, 93750, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9765")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93AB")

    ChrTalk(    #415
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, that's...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_951F")

    label("loc_93AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943B")

    ChrTalk(    #417
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, look at this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x102,
        (
            "#012FYeah. Looks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_951F")

    label("loc_943B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C5")

    ChrTalk(    #419
        0x107,
        (
            "#065FHey...\x01",
            "Joshua! What's this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_951F")

    label("loc_94C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951F")

    ChrTalk(    #421
        0x106,
        "#057FThis is...a smoke canister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x102,
        "#012FAgate, let me see that a sec.\x02",
    )

    CloseMessageWindow()

    label("loc_951F")

    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #423
        "\x07\x05Joshua quickly dismantled the smoke canister.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -102470, 0, 94470, 135)
    SetChrPos(0x101, -102530, 0, 95560, 135)
    SetChrPos(0x107, -103610, 0, 94520, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_95AA")
    SetChrPos(0x106, -101550, 0, 95550, 225)

    label("loc_95AA")

    FadeToBright(600, 0)
    OP_82(0x1, 0x2)
    OP_82(0x0, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_968B")

    ChrTalk(    #424
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        (
            "#012FThere are probably more canisters\x01",
            "like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9762")

    label("loc_968B")

    OP_A2(0x53E)

    ChrTalk(    #428
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9762")

    Jump("loc_989E")

    label("loc_9765")

    FadeToDark(600, 0, -1)

    AnonymousTalk(    #432
        "\x07\x05Joshua quickly dismantled the smoke canister.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -102470, 0, 94470, 135)
    SetChrPos(0x101, -102530, 0, 95560, 135)
    SetChrPos(0x107, -103610, 0, 94520, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_97F8")
    SetChrPos(0x106, -101550, 0, 95550, 225)

    label("loc_97F8")

    OP_82(0x1, 0x2)
    OP_82(0x0, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_989E")
    OP_A2(0x53E)

    ChrTalk(    #433
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_989E")

    EventEnd(0x0)
    Return()

    # Function_16_92FA end

    def Function_17_98A1(): pass

    label("Function_17_98A1")

    AddParty(0xF, 0xFF)
    EventBegin(0x0)
    OP_6D(2860, 0, 5340, 0)
    OP_6B(3200, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 2360, 0, 2680, 0)
    SetChrPos(0x110, 4670, 0, 3000, 270)
    SetChrPos(0xA, 250, 0, 2990, 90)
    SetChrPos(0xB, 250, 0, 2040, 90)
    SetChrPos(0x102, -820, 0, 5490, 135)
    SetChrPos(0x101, -540, 0, 4290, 90)
    SetChrPos(0x106, 230, 0, 5620, 180)
    SetChrPos(0x107, -1830, 0, 4760, 90)

    def lambda_995D():

        label("loc_995D")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_995D")

    QueueWorkItem2(0x101, 1, lambda_995D)

    def lambda_996E():

        label("loc_996E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_996E")

    QueueWorkItem2(0x102, 1, lambda_996E)

    def lambda_997F():

        label("loc_997F")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_997F")

    QueueWorkItem2(0x107, 1, lambda_997F)
    OP_A2(0x533)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #435
        0x9,
        (
            "#182FI understand the particulars.\x02\x03",

            "Nevertheless...this is major.\x02\x03",

            "This would appear to be a\x01",
            "clear-cut case of terrorism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x8,
        "#805F#3PIn Aidios' name... Terrorism...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x9,
        (
            "#181FUsing smoke canisters to create a diversion\x01",
            "while abducting the kingdom's greatest mind...\x02\x03",

            "To say nothing of the theft of the orbal\x01",
            "calculator, which contains some of our\x01",
            "country's most cutting edge technology...\x02\x03",

            "This deed will not go unpunished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x106,
        (
            "#050F#1PSo, what kind of plan does the\x01",
            "military have up its sleeve?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x9,
        (
            "#182FWe already have Air-Letten, the Wolf\x01",
            "Fort, Soldat Army Road and Sanktheim\x01",
            "Gate performing inspections.\x02\x03",

            "There's no way that the culprits\x01",
            "are getting out of the Zeiss\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x101,
        (
            "#004FWow...\x01",
            "You really mean business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x9,
        (
            "#181FHa ha... Well, Intel's job is to help\x01",
            "us mobilize as quickly and efficiently\x01",
            "as possible, in times of emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x102,
        (
            "#012FI do have one question...\x02\x03",

            "What do you think about the\x01",
            "terrorists having masqueraded\x01",
            "as Royal Guardsmen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x9,
        "#182FYes... It's very unsettling.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x110, 400)

    ChrTalk(    #445
        0x9,
        (
            "#181F#1PHaving said that...\x01",
            "Miss Dorothy Hyatt?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9DE9():

        label("loc_9DE9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_9DE9")

    QueueWorkItem2(0x110, 1, lambda_9DE9)

    ChrTalk(    #446
        0x110,
        (
            "#153F#4PWha...?\x02\x03",

            "Who...me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x9,
        (
            "#182F#1PYou took photos of the criminals\x01",
            "making their escape, did you not?\x02\x03",

            "We would greatly appreciate it if\x01",
            "you'd give us that photo-quartz\x01",
            "to be processed as evidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x110,
        (
            "#152F#4PWhat?!\x02\x03",

            "But... But...it's my big scoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x9,
        (
            "#182F#1PThe Royal Guardsmen are the pride of Liberl's\x01",
            "military. A photo of their involvement in such an\x01",
            "incident is a very serious, and sensitive, matter.\x02\x03",

            "I also must ask that you not post any news about\x01",
            "this until we know more. This is in order to\x01",
            "protect the honor of Her Majesty the Queen.\x02\x03",

            "#181FThis isn't a formal request, but the entirety of\x01",
            "the Royal Armed Forces would greatly appreciate\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x110,
        (
            "#154F#4P*siiiigh*...\x01",
            "Fine, I guess...\x02\x03",

            "Once you figure out what\x01",
            "you need to know, you'll\x01",
            "give it back, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x110, 0xBA4, 0x0, 0xA6E, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #451
        (
            "\x07\x05Dorothy reluctantly handed over the photo-quartz exposure to Captain\x01",
            "Amalthea.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x110, 0xDF2, 0x0, 0xB18, 0x7D0, 0x0)

    ChrTalk(    #452
        0x9,
        "#182F#1PThank you for cooperating.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #453
        0x9,
        (
            "#182FI hate to ask this, but it would \x01",
            "also be appreciated if the bracers\x01",
            "would cease their inves--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x106,
        (
            "#057F#1PAin't happening.\x02\x03",

            "I've been chasing those guys in\x01",
            "black since way before any of\x01",
            "this started.\x02\x03",

            "Military honor or not, I got no\x01",
            "reason to stop now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0x9,
        (
            "#181F...\x02\x03",

            "#182F*sigh*... You leave me no choice.\x01",
            "Please, proceed with your investigation.\x02\x03",

            "That said, this is with the condition\x01",
            "that you report your findings back to\x01",
            "Intelligence at Fort Leiston.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x106,
        (
            "#051F#1PFine with me.\x02\x03",

            "And if you learn anything\x01",
            "new, you report it to the\x01",
            "Zeiss branch, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x9,
        (
            "#182FVery well.\x02\x03",

            "#181FAnd with that,\x01",
            "I must take my leave.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x9, 225, 400)

    def lambda_A455():

        label("loc_A455")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_A455")

    QueueWorkItem2(0xA, 1, lambda_A455)

    def lambda_A466():

        label("loc_A466")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_A466")

    QueueWorkItem2(0xB, 1, lambda_A466)

    def lambda_A477():
        OP_6D(640, 0, 1650, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A477)
    OP_8E(0x9, 0xFFFFFC2C, 0x0, 0x1EA, 0x7D0, 0x0)
    OP_43(0x9, 0x1, 0x0, 0x12)
    OP_43(0xA, 0x1, 0x0, 0x13)
    OP_43(0xB, 0x1, 0x0, 0x14)
    WaitChrThread(0xA, 0x1)
    OP_44(0x110, 0xFF)
    OP_44(0x106, 0xFF)
    OP_6D(190, 0, 5120, 1500)

    ChrTalk(    #458
        0x101,
        (
            "#505FWhew...\x01",
            "That was a little intense.\x02\x03",

            "She's Colonel Richard's right-\x01",
            "hand man...err, woman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x102,
        (
            "#010F#3PYes... It looks like she came here as\x01",
            "the colonel's direct representative\x01",
            "in the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x106,
        (
            "#552FHeh... Well, I'm just fine\x01",
            "with not rubbing elbows with\x01",
            "the military.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #461
        0x106,
        (
            "#050FAnyway, it looks like the culprits\x01",
            "are hiding out somewhere in Zeiss.\x02\x03",

            "The sooner we report in at the\x01",
            "guild, the sooner we can start\x01",
            "searching outside of town.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A6A8():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6A8)

    def lambda_A6B6():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6B6)

    def lambda_A6C4():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A6C4)

    def lambda_A6D2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_A6D2)

    ChrTalk(    #462
        0x101,
        (
            "#004FYeah...\x02\x03",

            "#009FWait a second. How come\x01",
            "you're not telling us not\x01",
            "to follow you this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x106,
        (
            "#051FBecause I can use you.\x02\x03",

            "Why else would I want you along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x101,
        (
            "#509FYou're a real peach,\x01",
            "you know that?\x02\x03",

            "#007FNo big deal, though. It's\x01",
            "just more training for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x102,
        "#010FThanks for having us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x106,
        (
            "#053FYeah, yeah...\x01",
            "Just stay alert.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #467
        0x106,
        "#050FWe're gonna go now, Chief.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #468
        0x8,
        (
            "#800FAll right... Take care.\x02\x03",

            "#803FDo what you have to in order\x01",
            "to save the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -1150, 0, 2880, 180)
    SetChrPos(0x102, -1150, 0, 2880, 180)
    SetChrPos(0x107, -1150, 0, 2880, 180)
    SetChrPos(0x106, -1150, 0, 2880, 180)
    SetChrPos(0x110, -1150, 0, 2880, 180)
    OP_6D(-1150, 0, 2880, 0)
    OP_6B(3000, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_98A1 end

    def Function_18_A962(): pass

    label("Function_18_A962")

    OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0x12C, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_A981():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A981)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_A962 end

    def Function_19_A9AC(): pass

    label("Function_19_A9AC")

    Sleep(300)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFFFEFC, 0x7D0, 0x0)

    def lambda_A9D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A9D0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x6D, 0x0, 0x64)
    Return()

    # Function_19_A9AC end

    def Function_20_AA00(): pass

    label("Function_20_AA00")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFFBD2, 0x0, 0xFFFFFEFC, 0x7D0, 0x0)

    def lambda_AA1F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AA1F)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0xFFFFF650, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_AA00 end

    def Function_21_AA4A(): pass

    label("Function_21_AA4A")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #470
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x356)"), scpexpr(EXPR_END)), "loc_AB01")
    FadeToDark(300, 0, 100)
    OP_22(0x73, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #471
        "\x07\x00Used \x07\x02Back Room Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_71(0x0, 0x10)
    OP_64(0x1, 0x1)
    OP_3F(0x356, 1)
    OP_28(0x2C, 0x1, 0x8000)
    OP_65(0x6, 0x1)
    Jump("loc_AC08")

    label("loc_AB01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x100)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC08")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #472
        0x13C,
        "Nyaa～go.\x02",
    )

    CloseMessageWindow()

    def lambda_AB3A():
        TurnDirection(0x102, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB3A)

    def lambda_AB48():
        TurnDirection(0x107, 0x13C, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AB48)
    TurnDirection(0x101, 0x13C, 400)

    ChrTalk(    #473
        0x101,
        "#002F...In there?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13C, 0x101, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #474
        0x13C,
        "Nya～o.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #475
        0x102,
        (
            "#012FLet's try to find the key.\x02\x03",

            "It's gotta be in here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #476
        0x101,
        "#002FSure thing.\x02",
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_28(0x2C, 0x1, 0x400)

    label("loc_AC08")

    TalkEnd(0xFF)
    Return()

    # Function_21_AA4A end

    def Function_22_AC0C(): pass

    label("Function_22_AC0C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #477
        "\x07\x05Examined the bookshelf.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #478
        (
            "\x07\x05There's nothing of interest. Apparently no one was\x01",
            "considerate enough to hide some money here. Alas.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_AC0C end

    def Function_23_ACB5(): pass

    label("Function_23_ACB5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #479
        "\x07\x05Examined the documents.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #480
        (
            "\x07\x05There's nothing of interest. Sadly no one seems\x01",
            "to have left any exciting or incriminating papers\x01",
            "for you to find.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_ACB5 end

    def Function_24_AD6C(): pass

    label("Function_24_AD6C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #481
        "\x07\x05Examined the pen stand.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #482
        (
            "\x07\x05There's nothing of interest...except you notice\x01",
            "that someone has chewed rather industriously on\x01",
            "the ends of these pens.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_AD6C end

    def Function_25_AE28(): pass

    label("Function_25_AE28")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #483
        "\x07\x05Examined the book on the desk.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #484
        "\x07\x00Found \x07\x02Back Room Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2C, 0x1, 0x800)
    OP_3E(0x356, 1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_25_AE28 end

    def Function_26_AEB7(): pass

    label("Function_26_AEB7")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(710, 0, 100700, 0)
    SetChrPos(0x101, 60, 0, 101680, 189)
    SetChrPos(0x102, 780, 0, 102660, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF10")
    SetChrPos(0x107, -600, 0, 102530, 168)

    label("loc_AF10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF2F")
    SetChrPos(0x106, 120, 0, 102990, 182)

    label("loc_AF2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF4E")
    SetChrPos(0x13C, -1020, 0, 101070, 101)

    label("loc_AF4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF68")

    def lambda_AF60():
        TurnDirection(0x0, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AF60)

    label("loc_AF68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF82")

    def lambda_AF7A():
        TurnDirection(0x1, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AF7A)

    label("loc_AF82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF9C")

    def lambda_AF94():
        TurnDirection(0x2, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AF94)

    label("loc_AF9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFB6")

    def lambda_AFAE():
        TurnDirection(0x3, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AFAE)

    label("loc_AFB6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFD0")

    def lambda_AFC8():
        TurnDirection(0x4, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_AFC8)

    label("loc_AFD0")

    OP_0D()
    Sleep(400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #485
        "\x07\x00Found \x07\x02Cigarettes\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #486
        0x101,
        "#001FHa ha... Found them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x102,
        "#010FWhich would likely mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x107,
        (
            "#561FNo...\x01",
            "Mr. Murdock couldn't have...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #489
        0x101,
        (
            "#003F#4PWell, it's a shock,\x01",
            "that's for sure.\x02\x03",

            "I wouldn't have suspected...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x10)

    def lambda_B122():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B122)
    SetChrPos(0x8, -3380, 0, 98500, 0)

    ChrTalk(    #490
        0x8,
        "N-No! You've got it all wrong!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B180():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B180)
    OP_8E(0x8, 0xFFFFF7B8, 0x0, 0x18D80, 0xFA0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1BA")

    def lambda_B1B2():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B1B2)

    label("loc_B1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1D4")

    def lambda_B1CC():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B1CC)

    label("loc_B1D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1EE")

    def lambda_B1E6():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B1E6)

    label("loc_B1EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B208")

    def lambda_B200():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B200)

    label("loc_B208")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B222")

    def lambda_B21A():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_B21A)

    label("loc_B222")

    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #491
        0x8,
        (
            "#805FThis is all just one \x01",
            "big misunderstanding!\x02\x03",

            "I was just going to take one quick puff,\x01",
            "then put the rest of them right back in\x01",
            "the clinic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x102,
        (
            "#015F#4PChief Murdock...\x02\x03",

            "I think you ought to come and\x01",
            "explain this to Dr. Miriam.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x2C, 0x1, 0x1000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3118   ._SN", 100, 0, 0)
    IdleLoop()
    OP_64(0x6, 0x1)
    EventEnd(0x0)
    Return()

    # Function_26_AEB7 end

    def Function_27_B351(): pass

    label("Function_27_B351")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #493
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'Hertz's Adventure I.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B411")
    OP_B9(0x374, 0x0)

    label("loc_B411")

    TalkEnd(0xFF)
    Return()

    # Function_27_B351 end

    def Function_28_B415(): pass

    label("Function_28_B415")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #494
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'Hertz's Adventure II.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4D6")
    OP_B9(0x344, 0x0)

    label("loc_B4D6")

    TalkEnd(0xFF)
    Return()

    # Function_28_B415 end

    def Function_29_B4DA(): pass

    label("Function_29_B4DA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #495
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'Septium Optic Annals.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B59B")
    OP_B9(0x342, 0x0)

    label("loc_B59B")

    TalkEnd(0xFF)
    Return()

    # Function_29_B4DA end

    def Function_30_B59F(): pass

    label("Function_30_B59F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #496
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'Tomorrow's Cooking.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B65E")
    OP_B9(0x341, 0x0)

    label("loc_B65E")

    TalkEnd(0xFF)
    Return()

    # Function_30_B59F end

    def Function_31_B662(): pass

    label("Function_31_B662")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #497
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'Kitty-Talk for Dummies.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B725")
    OP_B9(0x340, 0x0)

    label("loc_B725")

    TalkEnd(0xFF)
    Return()

    # Function_31_B662 end

    def Function_32_B729(): pass

    label("Function_32_B729")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #498
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'The Erbe Woodpecker.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7E9")
    OP_B9(0x343, 0x0)

    label("loc_B7E9")

    TalkEnd(0xFF)
    Return()

    # Function_32_B729 end

    def Function_33_B7ED(): pass

    label("Function_33_B7ED")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #499
        (
            "\x07\x05The shelf holds a book entitled,\x01",
            "'31 Cypress Trees.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read it]\x01",      # 0
            "[Cancel]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8AA")
    OP_B9(0x345, 0x0)

    label("loc_B8AA")

    TalkEnd(0xFF)
    Return()

    # Function_33_B7ED end

    SaveToFile()

Try(main)
