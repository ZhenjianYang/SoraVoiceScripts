from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0311   ._SN',
        MapName             = 'Event',
        Location            = 'E0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0311_1 ._SN',
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
        'Scherazard',                           # 9
        'Olivier',                              # 10
        'Kloe',                                 # 11
        'Zin',                                  # 12
        'Julia',                                # 13
        'General Morgan',                       # 14
        'Nial',                                 # 15
        'Dorothy',                              # 16
        'Agate',                                # 17
        'Tita',                                 # 18
        'Kevin',                                # 19
        'Professor Russell',                    # 20
        'Gospel',                               # 21
        'Zero Field Generator',                 # 22
        'Estelle',                              # 23
        'Joshua',                               # 24
        'Major Vander',                         # 25
        'Fancy Booze Glass',                    # 26
        'Bottle',                               # 27
        'Bottle',                               # 28
        "Ship's Cook Casey",                    # 29
        'Royal Guardsman',                      # 30
        'Ray',                                  # 31
        'Royal Guardsman',                      # 32
        'Royal Guardsman',                      # 33
        'Fancy Booze Glass',                    # 34
        'Glass',                                # 35
        'Glass',                                # 36
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT07/CH00070 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT07/CH02080 ._CH',             # 05
        'ED6_DT07/CH02060 ._CH',             # 06
        'ED6_DT07/CH02070 ._CH',             # 07
        'ED6_DT07/CH00050 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT26/CH20352 ._CH',             # 0A
        'ED6_DT07/CH00150 ._CH',             # 0B
        'ED6_DT27/CH03080 ._CH',             # 0C
        'ED6_DT07/CH02020 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
        'ED6_DT06/CH20020 ._CH',             # 0F
        'ED6_DT27/CH03000 ._CH',             # 10
        'ED6_DT27/CH03010 ._CH',             # 11
        'ED6_DT27/CH03570 ._CH',             # 12
        'ED6_DT27/CH03003 ._CH',             # 13
        'ED6_DT07/CH00023 ._CH',             # 14
        'ED6_DT07/CH00033 ._CH',             # 15
        'ED6_DT07/CH00043 ._CH',             # 16
        'ED6_DT07/CH00073 ._CH',             # 17
        'ED6_DT07/CH02093 ._CH',             # 18
        'ED6_DT07/CH02083 ._CH',             # 19
        'ED6_DT27/CH03013 ._CH',             # 1A
        'ED6_DT07/CH00053 ._CH',             # 1B
        'ED6_DT07/CH00063 ._CH',             # 1C
        'ED6_DT27/CH03083 ._CH',             # 1D
        'ED6_DT07/CH02023 ._CH',             # 1E
        'ED6_DT07/CH01520 ._CH',             # 1F
        'ED6_DT07/CH01320 ._CH',             # 20
        'ED6_DT07/CH01220 ._CH',             # 21
        'ED6_DT06/CH20045 ._CH',             # 22
        'ED6_DT07/CH01323 ._CH',             # 23
        'ED6_DT27/CH03210 ._CH',             # 24
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00070P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT07/CH02080P._CP',             # 05
        'ED6_DT07/CH02060P._CP',             # 06
        'ED6_DT07/CH02070P._CP',             # 07
        'ED6_DT07/CH00050P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT26/CH20352P._CP',             # 0A
        'ED6_DT07/CH00150P._CP',             # 0B
        'ED6_DT27/CH03080P._CP',             # 0C
        'ED6_DT07/CH02020P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
        'ED6_DT06/CH20020P._CP',             # 0F
        'ED6_DT27/CH03000P._CP',             # 10
        'ED6_DT27/CH03010P._CP',             # 11
        'ED6_DT27/CH03570P._CP',             # 12
        'ED6_DT27/CH03003P._CP',             # 13
        'ED6_DT07/CH00023P._CP',             # 14
        'ED6_DT07/CH00033P._CP',             # 15
        'ED6_DT07/CH00043P._CP',             # 16
        'ED6_DT07/CH00073P._CP',             # 17
        'ED6_DT07/CH02093P._CP',             # 18
        'ED6_DT07/CH02083P._CP',             # 19
        'ED6_DT27/CH03013P._CP',             # 1A
        'ED6_DT07/CH00053P._CP',             # 1B
        'ED6_DT07/CH00063P._CP',             # 1C
        'ED6_DT27/CH03083P._CP',             # 1D
        'ED6_DT07/CH02023P._CP',             # 1E
        'ED6_DT07/CH01520P._CP',             # 1F
        'ED6_DT07/CH01320P._CP',             # 20
        'ED6_DT07/CH01220P._CP',             # 21
        'ED6_DT06/CH20045P._CP',             # 22
        'ED6_DT07/CH01323P._CP',             # 23
        'ED6_DT27/CH03210P._CP',             # 24
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 458766,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 458766,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2370,
        Z                   = 500,
        Y                   = -40540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 500,
        Y                   = -44670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835023,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 500,
        Y                   = -44770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966095,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3760,
        Z                   = 0,
        Y                   = -38100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1420,
        Z                   = 0,
        Y                   = -41460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1410,
        Z                   = 0,
        Y                   = -41580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2370,
        Z                   = 200,
        Y                   = -46010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2370,
        Z                   = 200,
        Y                   = -39890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -650,
        Z                   = 600,
        Y                   = -48810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -650,
        Z                   = 650,
        Y                   = -49330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2340,
        Z                   = 650,
        Y                   = -48700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 1410,
        TriggerZ            = 0,
        TriggerY            = -38950,
        TriggerRange        = 800,
        ActorX              = 3330,
        ActorZ              = 1500,
        ActorY              = -38950,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_576",          # 00, 0
        "Function_1_ABD",          # 01, 1
        "Function_2_C34",          # 02, 2
        "Function_3_DB1",          # 03, 3
        "Function_4_E84",          # 04, 4
        "Function_5_E89",          # 05, 5
        "Function_6_134C",         # 06, 6
        "Function_7_2A62",         # 07, 7
        "Function_8_2B90",         # 08, 8
        "Function_9_450F",         # 09, 9
        "Function_10_455E",        # 0A, 10
        "Function_11_45B2",        # 0B, 11
        "Function_12_45E2",        # 0C, 12
        "Function_13_4617",        # 0D, 13
        "Function_14_5104",        # 0E, 14
        "Function_15_59AF",        # 0F, 15
        "Function_16_6DEF",        # 10, 16
        "Function_17_9C08",        # 11, 17
        "Function_18_9C6B",        # 12, 18
        "Function_19_9CEE",        # 13, 19
        "Function_20_9D20",        # 14, 20
        "Function_21_9D66",        # 15, 21
        "Function_22_9DAC",        # 16, 22
        "Function_23_9DD7",        # 17, 23
        "Function_24_9E02",        # 18, 24
        "Function_25_9E51",        # 19, 25
        "Function_26_9E96",        # 1A, 26
        "Function_27_9ECC",        # 1B, 27
        "Function_28_9F12",        # 1C, 28
        "Function_29_9F58",        # 1D, 29
        "Function_30_9FDE",        # 1E, 30
        "Function_31_A06D",        # 1F, 31
        "Function_32_A0FA",        # 20, 32
        "Function_33_A18B",        # 21, 33
        "Function_34_A1A5",        # 22, 34
    )


    def Function_0_576(): pass

    label("Function_0_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 0)), scpexpr(EXPR_END)), "loc_70D")
    SetChrPos(0x1C, 3330, 0, -38950, 270)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_70A")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AE")
    ClearChrFlags(0x20, 0x80)
    Jump("loc_70A")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5EA")
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2020, 0, -43620, 270)
    SetChrChipByIndex(0x9, 34)
    OP_43(0x9, 0x0, 0x0, 0x3)

    label("loc_5EA")

    ClearChrFlags(0x1F, 0x80)
    Jump("loc_70A")

    label("loc_5F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0x1A, -180, 750, -48810, 180)
    SetChrPos(0x1B, -200, 750, -49380, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -420, 200, -48050, 180)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    ClearChrFlags(0x21, 0x80)

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BD")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -420, 200, -50170, 0)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x22, 0x80)

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2370, 200, -48050, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x23, 0x80)

    label("loc_70A")

    Jump("loc_9F3")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_7CF")
    SetChrPos(0x1C, 3330, 0, -38950, 270)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_765")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_765")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CC")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 50, -42000, 0)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    SetChrPos(0x1A, -2070, 750, -41180, 180)
    SetChrPos(0x1B, -2500, 750, -41080, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_7CC")

    Jump("loc_9F3")

    label("loc_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_88A")
    SetChrPos(0x1C, 3330, 0, -38950, 270)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1E, 4990, 0, -39510, 45)
    SetChrFlags(0x1E, 0x10)
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_842")
    SetChrPos(0x10, -2370, 200, -46010, 0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 0)
    OP_44(0x10, 0x0)

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_887")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_887")

    Jump("loc_9F3")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_91E")
    SetChrPos(0x1C, 3330, 0, -38950, 270)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E0")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2370, 200, -41880, 0)
    SetChrPos(0x10, 4600, 0, -47630, 270)

    label("loc_8E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91B")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_91B")

    Jump("loc_9F3")

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_97E")
    SetChrPos(0x1C, 3330, 0, -38950, 270)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97B")
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_97B")

    Jump("loc_9F3")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_992")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_9F3")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F3")
    SetChrPos(0xD, 1730, 0, 53900, 0)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x0, 0x2)
    SetChrPos(0x9, -2370, 200, -39890, 180)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A12")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_ABC")

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_A31")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_ABC")

    label("loc_A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_A47")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_ABC")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_A5D")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_ABC")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_A7C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_ABC")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_A9B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_ABC")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_ABC")

    Return()

    # Function_0_576 end

    def Function_1_ABD(): pass

    label("Function_1_ABD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADB")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_AFA")
    OP_B1("E0311_1")
    Jump("loc_B03")

    label("loc_AFA")

    OP_B1("E0311_2")

    label("loc_B03")

    Jump("loc_B27")

    label("loc_B06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1E")
    OP_B1("E0311_2")
    Jump("loc_B27")

    label("loc_B1E")

    OP_B1("E0311_1")

    label("loc_B27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B50")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5D")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5D")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_B5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B88")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_B88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_BB6")
    SetMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_BAD")
    OP_A3(0xF)
    Jump("loc_BB6")

    label("loc_BAD")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDF")
    Call(0, 33)
    Jump("loc_BFB")

    label("loc_BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Call(0, 34)

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_C05")
    Jump("loc_C24")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_C0F")
    Jump("loc_C24")

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C24")
    OP_74(0xFF, 0x10, 0x1)

    label("loc_C24")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_C33")
    OP_65(0x0, 0x1)

    label("loc_C33")

    Return()

    # Function_1_ABD end

    def Function_2_C34(): pass

    label("Function_2_C34")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C59")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D9B")

    label("loc_C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C72")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D9B")

    label("loc_C72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D9B")

    label("loc_C8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D9B")

    label("loc_CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D9B")

    label("loc_CBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D9B")

    label("loc_CD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D9B")

    label("loc_CEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D08")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D9B")

    label("loc_D08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D21")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D9B")

    label("loc_D21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D9B")

    label("loc_D3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D9B")

    label("loc_D53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D9B")

    label("loc_D6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D85")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D9B")

    label("loc_D85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D9B")

    label("loc_DB0")

    Return()

    # Function_2_C34 end

    def Function_3_DB1(): pass

    label("Function_3_DB1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E83")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_DE7")
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Jump("loc_E00")

    label("loc_DE7")

    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)

    label("loc_E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_E0D")
    OP_A3(0xE)
    Jump("loc_E49")

    label("loc_E0D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_E49")
    Sleep(80)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    OP_A2(0xE)

    label("loc_E49")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_E6C")
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_E80")

    label("loc_E6C")

    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)

    label("loc_E80")

    Jump("Function_3_DB1")

    label("loc_E83")

    Return()

    # Function_3_DB1 end

    def Function_4_E84(): pass

    label("Function_4_E84")

    Call(1, 6)
    Return()

    # Function_4_E84 end

    def Function_5_E89(): pass

    label("Function_5_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 6)), scpexpr(EXPR_END)), "loc_EBB")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xE, 0xF, 0xFFFF)
    Jump("loc_EFD")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_EE2")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_EFD")

    label("loc_EE2")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_EFD")

    Jump("loc_F7E")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_F23")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_F7E")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_F44")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_F7E")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_F65")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_F7E")

    label("loc_F65")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_F7E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_114F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDF")
    Jump("loc_114C")

    label("loc_FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEA")
    Jump("loc_114C")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1034")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_102D")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2020, 0, -43620, 270)
    SetChrChipByIndex(0x9, 34)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102A")
    Call(0, 33)

    label("loc_102A")

    Jump("loc_1031")

    label("loc_102D")

    Call(0, 34)

    label("loc_1031")

    Jump("loc_114C")

    label("loc_1034")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1077")
    SetChrPos(0x1A, -180, 750, -48810, 180)
    SetChrPos(0x1B, -200, 750, -49380, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_1077")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10B2")
    SetChrPos(0x9, -420, 200, -48050, 180)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    ClearChrFlags(0x21, 0x80)

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10FF")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -420, 200, -50170, 0)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x22, 0x80)

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_114C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2370, 200, -48050, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x23, 0x80)

    label("loc_114C")

    Jump("loc_134A")

    label("loc_114F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_1200")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1196")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_1196")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FD")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 50, -42000, 0)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    SetChrPos(0x1A, -2070, 750, -41180, 180)
    SetChrPos(0x1B, -2500, 750, -41080, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_11FD")

    Jump("loc_134A")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_128A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1242")
    SetChrPos(0x10, -2370, 200, -46010, 0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 0)
    OP_44(0x10, 0x0)

    label("loc_1242")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1287")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_1287")

    Jump("loc_134A")

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_1308")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12C5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2370, 200, -41880, 0)
    SetChrPos(0x10, 4600, 0, -47630, 270)

    label("loc_12C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1305")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_1305")

    Jump("loc_134A")

    label("loc_1308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_134A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_134A")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0x8, 0x0)

    label("loc_134A")

    OP_0D()
    Return()

    # Function_5_E89 end

    def Function_6_134C(): pass

    label("Function_6_134C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0xD, 1070, 200, 53790, 180)
    SetChrPos(0xC, 2370, 0, 54390, 180)
    SetChrPos(0x101, -1140, 100, 52380, 90)
    SetChrPos(0x8, -1140, 100, 51220, 90)
    SetChrPos(0xB, -1140, 100, 49960, 90)
    SetChrPos(0xA, 2880, 200, 52400, 270)
    SetChrPos(0x9, 2880, 200, 51200, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 2)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 2)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 1)
    SetChrChipByIndex(0xD, 25)
    SetChrSubChip(0xD, 0)
    OP_6D(1690, 0, 46880, 0)
    OP_67(0, 7340, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #0
        (
            "\x07\x00Well, then. Allow me to explain Operation Dragon\x01",
            "Capture.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_14FE():
        OP_6D(2029, 100, 52820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14FE)

    def lambda_1516():
        OP_67(0, 6340, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1516)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #1
        0xD,
        (
            "#163F#6PThis operation will be conducted primarily\x01",
            "by the airship force.\x02\x03",

            "Our ground divisions will focus solely on\x01",
            "keeping order in all regions during the\x01",
            "operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1015FWait, all the regions?\x01",
            "So we're going beyond Bose for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xD,
        (
            "#160F#6PPossibly not by our choice.\x01",
            "Last night's events showed that the dragon's\x01",
            "capacity for flight is...significant.\x02\x03",

            "It is very possible that it will move to another\x01",
            "region at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1003FYeah, good point...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xD,
        (
            "#160F#6PThe plan shall involve twelve airships in total,\x01",
            "including the Arseille.\x02\x03",

            "Which is to say, it involves two-fifths of our\x01",
            "entire fleet. The rest will be held in reserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#023F#5PTwo-fifths of the entire fleet...\x01",
            "That's enough power to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#030F#4PEnough power to give our friend\x01",
            "quite a reception, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        "#163F#6PJulia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xC,
        "#178F#6PSir!\x02",
    )

    CloseMessageWindow()

    def lambda_1886():
        OP_6D(2029, 100, 53820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1886)
    OP_8C(0xC, 270, 400)
    OP_8C(0xC, 0, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xFF, 0x10, 0x1)
    OP_0D()
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS136._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS210._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS211._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS212._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS213._CH")
    OP_C5(0x5, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS214._CH")
    OP_C5(0x6, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS215._CH")
    OP_C5(0x7, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS216._CH")
    OP_C5(0x8, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS217._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #10
        "\x07\x00#1004FWhoa!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #11
        "\x07\x00#073FThis is a map of the mission plan?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #12
        (
            "\x07\x00#163FYes, precisely.\x02\x03",

            "#160FThe Arseille is currently cruising in Bose\x01",
            "airspace.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #13
        (
            "\x07\x00#160FWe shall be using the Arseille as the flagship\x01",
            "and command vessel for this operation.\x02\x03",

            "The actual 'dragon patrol' shall be carried\x01",
            "out by...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #14
        (
            "\x07\x00#163F...eight patrol ships equipped with wide-area\x01",
            "radar.\x02\x03",

            "If the dragon so much as raises its head above\x01",
            "the tree line, they will be able to find it.\x02\x03",

            "#160FThen, once the dragon is found...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #15
        (
            "\x07\x00#160FShips will give chase at high speed and\x01",
            "use their rapid fire artillery to check the\x01",
            "the dragon and guide it over Lake Valleria.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x5, 0x4, 0, 0, 0)
    OP_C6(0x5, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #16
        (
            "\x07\x00#163FAt the same time, several patrol vessels armed\x01",
            "with tranquilizer rounds will be scrambled from\x01",
            "Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x6, 0x4, 0, 0, 0)
    OP_C6(0x6, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x7, 0x4, 0, 0, 0)
    OP_C6(0x7, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("General Morgan")

    AnonymousTalk(    #17
        (
            "\x07\x00#163FOnce the dragon is pinned, they will intercept it.\x02\x03",

            "They will fire every tranquilizer round they have\x01",
            "and sink the creature.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x8, 0x4, 0, 0, 0)
    OP_C6(0x8, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_1FF9():
        OP_6D(2029, 100, 52820, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FF9)
    OP_8C(0xC, 180, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    OP_C6(0x5, 0x3, 16777215, 0, 0)
    OP_C6(0x6, 0x3, 16777215, 0, 0)
    OP_C6(0x7, 0x3, 16777215, 0, 0)
    OP_C6(0x8, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)

    ChrTalk(    #18
        0xD,
        "#160F#6PThat is the plan in full.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1004FUm...wow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#025F#5PWell, this is...certainly a bit larger-scale\x01",
            "than most guild operations.\x02\x03",

            "#022FIf the tranquilizers don't work, I'm guessing\x01",
            "you'll switch to live ammunition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xD,
        (
            "#163F#6PYes...\x02\x03",

            "In that case, we'll have to destroy the dragon\x01",
            "with concentrated fire from all ships.\x02\x03",

            "Her Majesty has asked us to prioritize capture\x01",
            "over destruction...but we are ready for\x01",
            "every contingency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1015FHuh? Why would Queen Alicia want\x01",
            "the dragon alive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "#160F#6PDragons are creatures of myth,\x01",
            "oldest legends.\x02\x03",

            "She said she could not bear to\x01",
            "have it slain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "#043F#4PI can understand that...\x02\x03",

            "Especially since the dragon\x01",
            "is under the society's control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1007FYeah, good point.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x101,
        (
            "#1020FW-Wait, that's right!\x02\x03",

            "That Lorence, er, Leonhardt, er,\x01",
            "whoever-he-is guy!\x01",
            "He had a Gospel! That'd mean--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xD,
        (
            "#163F#6PYes... The Orbal Shutdown Phenomenon.\x02\x03",

            "#160FAccording to Professor Russell, the\x01",
            "maximum range of the effect is roughly\x01",
            "five arge.\x02\x03",

            "All ships have orders to get no closer\x01",
            "than ten arge to the dragon.\x02\x03",

            "As long as we do that, there should not\x01",
            "be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1025FThat should work, hopefully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#031F#4PMost impressive, General.\x01",
            "You do seem prepared for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "#163FHmph. We learned quite a bit from the\x01",
            "Hundred Days War.\x02\x03",

            "#160FAnd should this plan somehow fail entirely,\x01",
            "we will be left wanting for options.\x02\x03",

            "Should that come to pass, we will be\x01",
            "relying on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1007FIt's nice of you to say that, but, uh...\x02\x03",

            "#1019FWhy do I get the impression you think\x01",
            "this plan is foolproof and invincible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        (
            "#163FHeh. Of course.\x02\x03",

            "If this plan has a problem, it's that we\x01",
            "have to wait for the dragon to show its\x01",
            "face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015FWell, that's a question... What do we do\x01",
            "if the dragon doesn't show up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "#074F#2PGiven how Ouroboros has behaved up to this point,\x01",
            "I find it unlikely they'll keep it hidden.\x02\x03",

            "#072FThey'll want to use that dragon to do\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1002FThey probably will, won't they...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)
    Sleep(500)

    ChrTalk(    #36
        0xC,
        (
            "#170F#6PWell then, bracers.\x02\x03",

            "Once we've found the dragon, we will\x01",
            "announce it over the comm.\x02\x03",

            "Until then, please, make yourselves\x01",
            "at home.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(870, 0, 3010, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, 870, 0, 3010, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_69(0x0, 0x0)
    OP_A2(0x1A1E)
    OP_28(0x95, 0x1, 0x2)
    OP_28(0x95, 0x1, 0x4)
    OP_28(0x95, 0x1, 0x8)
    OP_28(0x95, 0x1, 0x10)
    Sleep(1000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_134C end

    def Function_7_2A62(): pass

    label("Function_7_2A62")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Julia's Voice")

    AnonymousTalk(    #37
        (
            "\x07\x05Signal from the Melder!\x02\x03",

            "Dragon in flight in airspace above the\x01",
            "Malga Mine!\x02\x03",

            "All crew to battle stations!\x01",
            "All crew to battle stations!\x02\x03",

            "Guild observers, report to the bridge!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #38
        0x101,
        "#1005FHere we go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2A62 end

    def Function_8_2B90(): pass

    label("Function_8_2B90")

    EventBegin(0x0)
    OP_6D(940, 950, 48420, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1010, 100, 48750, 90)
    SetChrPos(0x103, -1060, 100, 47520, 90)
    SetChrPos(0x104, -1040, 100, 46300, 90)
    SetChrPos(0x108, -1140, 100, 49960, 90)
    SetChrPos(0xD, 2900, 250, 48750, 270)
    SetChrPos(0xC, 2950, 230, 47470, 270)
    SetChrPos(0x105, 2900, 200, 49900, 270)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0x103, 255)
    OP_4A(0x104, 255)
    OP_4A(0x108, 255)
    OP_4A(0x105, 255)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 20)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x104, 21)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x105, 22)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x108, 23)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0xC, 24)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xD, 25)
    SetChrSubChip(0xD, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0xC,
        (
            "#176F#4PThe dragon has fled to the northwestern\x01",
            "corner of Nebel Valley.\x02\x03",

            "#178FIt's the part of the valley that's hardest\x01",
            "to traverse, and it's covered in deep fog,\x01",
            "being further in than the bandit base was.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 1)
    Sleep(400)

    ChrTalk(    #40
        0x105,
        (
            "#042F#6PIn other words, scouting by airship\x01",
            "will be difficult?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #41
        0xC,
        (
            "#176F#4PHm. 'Difficult' at best...\x02\x03",

            "#175FThere's really no option but to\x01",
            "dispatch an expedition on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1020F#5PBut wait a second!\x02\x03",

            "If you send in a whole army the dragon\x01",
            "will just run away!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #43
        0x103,
        (
            "#026F#5PShe has a point.\x02\x03",

            "#020FI think it would be better to try and strike\x01",
            "at him with a smaller group while he's\x01",
            "still vulnerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        "#160F#4PMeaning you'd like for us to leave it to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x108,
        (
            "#074F#3PWell, we are more used to investigating something\x01",
            "on difficult terrain than most of your troops.\x02\x03",

            "#070FI would say we're the right people for the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "#163F#4PHmm...\x02\x03",

            "#160FDo you have any idea of HOW you\x01",
            "would 'investigate' this?\x02\x03",

            "As I recall, there is no real road into that\x01",
            "section of the valley.\x02\x03",

            "Simply wandering over and praying to Aidios\x01",
            "that you'll find something could take days...\x01",
            "at a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1015F#5PEr, well...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x10, 1000, 0, 40690, 0)

    NpcTalk(    #48
        0x10,
        "Man's Voice",
        "#1PLeave that to me.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x1)
    Sleep(500)

    def lambda_328E():
        OP_6D(2800, 100, 48400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_328E)

    def lambda_32A6():
        OP_67(0, 4370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_32A6)

    def lambda_32BE():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_32BE)

    def lambda_32CE():
        OP_6C(52000, 4000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_32CE)

    def lambda_32DE():
        OP_6B(2840, 4000)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_32DE)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x103, 2)
    Sleep(50)
    SetChrSubChip(0x104, 2)
    SetChrSubChip(0x105, 1)
    Sleep(50)
    SetChrSubChip(0x108, 2)
    SetChrSubChip(0xC, 1)
    Sleep(50)
    SetChrSubChip(0xD, 1)
    Sleep(800)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_43(0x10, 0x1, 0x0, 0x9)
    OP_43(0x11, 0x1, 0x0, 0xA)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #49
        0xD,
        "#161F#6POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1004F#5PAgate! Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#051FYo! Sorry to butt in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        "#560F#2PUm, pardon us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1008F#5PWhat're you doing here...\x02\x03",

            "#1020FA-And more importantly!\x01",
            "Are you sure you should be up and about?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#053FLike I told Tita, this is nothin'.\x01",
            "Just a bunch of scratches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1019F#5PTita. Is he serious?\x01",
            "Estelle Stare, Tita. Estelle Stare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "#066F#2PUm, y-yeah...\x02\x03",

            "I don't think Agate's really pushing himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1006F#5PI see... Well, okay then, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "#163F#6PHmph. You have plenty of energy,\x01",
            "if nothing else.\x02\x03",

            "#160FYou said 'leave it to me,' but do you even\x01",
            "know what we're talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#050FYeah, Lugran filled me in on the details.\x02\x03",

            "That overgrown lizard's disappeared into the\x01",
            "northwest of Nebel Valley, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1015F#5PYeah, but what can you--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "#053FI know a man who knows\x01",
            "a lot about the area.\x02\x03",

            "If we ask him, we should be able to find\x01",
            "a way to get into that corner of the valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        "#161F#6POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1004F#5PWho is this guy, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#051FA tough old-timer by the name of Whemler.\x01",
            "He lives on the eastern side of the valley.\x02\x03",

            "He bragged to me once that he got across\x01",
            "the ravine that divides that part of the\x01",
            "valley from the rest.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A1")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Whemler in previous game\x01",              # 0
            "Set as didn't meet Whemler in previous game\x01",      # 1
            "No change\x01",                                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3895"),
        (1, "loc_389B"),
        (SWITCH_DEFAULT, "loc_38A1"),
    )


    label("loc_3895")

    OP_A2(0x1A80)
    Jump("loc_38A1")

    label("loc_389B")

    OP_A3(0x1A80)
    Jump("loc_38A1")

    label("loc_38A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_38F0")

    ChrTalk(    #65
        0x101,
        (
            "#1011F#5POh, right, right! That old man living in\x01",
            "that little hut!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F0")


    ChrTalk(    #66
        0x104,
        (
            "#031F#5PHeh, impressive.\x02\x03",

            "Your constant hunt for information\x01",
            "has borne fruit, you might say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        (
            "#163F#6P...\x02\x03",

            "#160FEven if you find the dragon...\x01",
            "what do you intend to do?\x02\x03",

            "It is not what I would call a trivial foe.\x01",
            "Do you intend to slay it yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "#050FThere's a Gospel on the thing's head,\x01",
            "right?\x02\x03",

            "Job one is to deal with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        "#161F#6PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#022F#5PIt does follow that the reason the dragon has\x01",
            "grown violent is due to that Gospel.\x02\x03",

            "The Gospels have been responsible for all\x01",
            "sorts of bizarre phenomena before now,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x108,
        (
            "#074F#6PAnd if we nullify the Gospel, perhaps we can\x01",
            "put an end to the dragon's rampage.\x02\x03",

            "#070FSounds like a good plan to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xC,
        (
            "#176F#6PWhen you say you'll 'break the Gospel,'\x01",
            "you remind me of what Father Graham did.\x02\x03",

            "#175FHe hit the Gospel with an artifact and\x01",
            "shorted it out, but we do not exactly have\x01",
            "a surfeit of artifacts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#051FYeah, we don't have time to fiddle with\x01",
            "stuff like that.\x02\x03",

            "We're just going to smash that thing to\x01",
            "bits, frame and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xC,
        "#173F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1004F#5PWhoa, hang on a sec!\x02\x03",

            "Can we really break a Gospel that easily?\x02\x03",

            "Whenever I handled one, it always seemed\x01",
            "like it was really sturdy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#053FLet's just say we've got a solution to\x01",
            "that little problem.\x02\x03",

            "#050FTake a look.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 10)
    SetChrSubChip(0x10, 16)
    OP_0D()
    Sleep(1000)
    OP_AD(0x240098, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #77
        "\x07\x00#1004FYour sword!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #78
        (
            "\x07\x00#020FThere's something fitted into the...\x01",
            "Oh, now I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #79
        0x10,
        (
            "#053FRussell tossed me a new gizmo of his\x01",
            "in the mail.\x02\x03",

            "#051FIt's a little something for breakin' Gospels.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #80
        0x101,
        "#1004F#1P#3SFor real?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x104,
        "#033F#5PHmmmm... How is it meant to work, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x11,
        (
            "#061F#2POoh, I'll explain!\x02\x03",

            "#560FThe unit on the hilt applies high-frequency\x01",
            "vibrations to the blade that will help it\x01",
            "break a Gospel's frame.\x02\x03",

            "Because of the vibration, the motor will\x01",
            "break after a few hits...\x02\x03",

            "#067FBut Grandpa is sure that if you hit a\x01",
            "Gospel cleanly with a vibrating blade,\x01",
            "the Gospel will break!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1008F#5PI, uh, don't think I quite get it all,\x01",
            "but it sounds incredible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#035F#5PHeh. Liberl's greatest living genius\x01",
            "comes through once again.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #85
        0x10,
        (
            "#053FI got Tita to attach it when it arrived,\x01",
            "and it seems like it works.\x02\x03",

            "All that's left now is to find the dragon\x01",
            "and give him a good one on the forehead.\x02\x03",

            "#051FSo, Mister General, how's that sound for\x01",
            "a plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xD,
        (
            "#163F#6P...\x02\x03",

            "#160FIf Russell's given you a fighting chance,\x01",
            "I suppose I have no choice but to agree.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    SetChrSubChip(0x103, 0)
    Sleep(50)
    SetChrSubChip(0x104, 0)
    Sleep(50)
    SetChrSubChip(0x108, 0)
    Sleep(50)
    SetChrSubChip(0xC, 2)
    Sleep(200)

    ChrTalk(    #87
        0x101,
        "#1006F#5PSo, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        "#050FYou'll let us take a crack at it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xD,
        (
            "#163F#6PYes... Do everything you can.\x02\x03",

            "#160FHowever, I will have airships around the\x01",
            "valley, on standby.\x02\x03",

            "They will be able to respond if...or when...\x01",
            "the dragon slips past you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "#051FHeh, sounds like a challenge.\x02\x03",

            "You just tell them they won't need much ammo.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2B90 end

    def Function_9_450F(): pass

    label("Function_9_450F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 1000, 0, 40690, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4536():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4536)
    OP_8E(0xFE, 0x654, 0x0, 0xADDE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_9_450F end

    def Function_10_455E(): pass

    label("Function_10_455E")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 1000, 0, 40690, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_458A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_458A)
    OP_8F(0xFE, 0xFFFFFFA6, 0x0, 0xAD7A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_10_455E end

    def Function_11_45B2(): pass

    label("Function_11_45B2")

    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xA8DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xB84C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_11_45B2 end

    def Function_12_45E2(): pass

    label("Function_12_45E2")

    Sleep(500)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xA8DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xB518, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_12_45E2 end

    def Function_13_4617(): pass

    label("Function_13_4617")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_462E")
    Call(0, 29)
    Call(0, 30)

    label("loc_462E")

    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x13, 1060, 150, 53910, 180)
    SetChrPos(0xC, 2250, 0, 54450, 180)
    SetChrPos(0x101, -1140, 100, 52380, 90)
    SetChrPos(0x102, -1140, 100, 51220, 90)
    SetChrPos(0x8, -1140, 100, 49960, 90)
    SetChrPos(0xB, -1190, 100, 48660, 90)
    SetChrPos(0xA, 2950, 200, 52400, 270)
    SetChrPos(0x11, 2950, 200, 51200, 270)
    SetChrPos(0x10, 2950, 200, 49840, 270)
    SetChrPos(0x12, 2950, 200, 48620, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x13, 0x4)
    OP_4A(0x10, 255)
    OP_4A(0x8, 255)
    OP_4A(0x11, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0x12, 255)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 2)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 1)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 1)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 2)
    SetChrChipByIndex(0x11, 28)
    SetChrSubChip(0x11, 2)
    SetChrChipByIndex(0x12, 29)
    SetChrSubChip(0x12, 2)
    SetChrChipByIndex(0x13, 30)
    SetChrSubChip(0x13, 0)
    OP_72(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #91
        0x13,
        (
            "#104F#6PI see, I see.\x01",
            "Sounds as if quite a lot happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1002F#5PAnyway, Professor, we thought\x01",
            "you should have the beta.\x02\x03",

            "#1004FOh, also!\x01",
            "We found this in the tower.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #93
        "\x07\x05Estelle handed over the crystal she found.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x3FD, 1)
    OP_3F(0x3FE, 1)
    OP_3F(0x3FF, 1)
    OP_3F(0x400, 1)
    Sleep(100)
    SetChrSubChip(0x13, 2)
    Sleep(300)

    ChrTalk(    #94
        0x13,
        (
            "#103F#6POhhh... This is a memory crystal!\x01",
            "The ancient orbal cultures used\x01",
            "these to store information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1042F#5PThe information inside it seemed...damaged,\x01",
            "somehow. Is there a way to restore it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x13,
        (
            "#104F#6PDamaged? Hmm.\x02\x03",

            "#100FThe crystal itself seems to be circuit-imprinted\x01",
            "septium, just like a 'normal' quartz crystal.\x02\x03",

            "It may take a while, but I'm reasonably\x01",
            "sure I can make the Capel read it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1006F#5PCould you do that, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        "#101F#6POf course! Leave it to me.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 0)
    Sleep(300)

    ChrTalk(    #99
        0x13,
        (
            "#102F#6PSo. Beyond that...whatever-it-is in\x01",
            "front of the tower doors is something\x01",
            "you're calling the 'shadow tower.'\x02\x03",

            "#104FHmmmmmmmmm... I should have gone myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        "#067FUmm, Grandpaaaa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#1043F#5PWe've been calling it 'shadow,'\x01",
            "but I think it might be the actual\x01",
            "form of the towers.\x02\x03",

            "#1042FThat is, as the components of\x01",
            "the second seal on the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x12,
        (
            "#1067FI kinda want to be relieved that it's\x01",
            "all back to 'normal,' but...yeah.\x02\x03",

            "#1068FWhat's got me really worried is that\x01",
            "they got the machines at the top\x01",
            "workin', and now they're stopped again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x13,
        "#104F#6PMmmm. True.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1002F#5POne way or another, we can't leave\x01",
            "the society to do what it wants.\x02\x03",

            "#1005FWe have to get to the next\x01",
            "tower as soon as we can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "#042FJulia. Do we have ANY information\x01",
            "on the other towers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xC,
        (
            "#176F#6PWe did just get an update from the scout\x01",
            "squad sent toward Carnelia Tower.\x02\x03",

            "#178FThey reported a man wearing a black suit\x01",
            "and sunglasses entering the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1026F#5PHim...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F92")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as chose Agate in Ch. 1\x01",           # 0
            "Set as chose Scherazard in Ch. 1\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F86"),
        (1, "loc_4F8C"),
        (SWITCH_DEFAULT, "loc_4F92"),
    )


    label("loc_4F86")

    OP_A2(0x1201)
    Jump("loc_4F92")

    label("loc_4F8C")

    OP_A3(0x1200)
    Jump("loc_4F92")

    label("loc_4F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4FC1")

    ChrTalk(    #108
        0x10,
        "#057FThat 'Direwolf' guy. Damn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FF0")

    label("loc_4FC1")


    ChrTalk(    #109
        0x8,
        "#022F#2PThat must be Walter the Direwolf.\x02",
    )

    CloseMessageWindow()

    label("loc_4FF0")


    ChrTalk(    #110
        0xB,
        (
            "#070F#2PWalter? Mmm...\x02\x03",

            "#074FFinally. A chance to meet\x01",
            "him head on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x102, 2)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    SetChrSubChip(0xA, 1)
    Sleep(100)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 1)
    Sleep(100)
    SetChrSubChip(0x12, 0)
    Sleep(100)

    ChrTalk(    #111
        0x101,
        "#1026F#5PZin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xB,
        (
            "#070F#2PEstelle, Joshua.\x02\x03",

            "I'm sorry to impose, but I'm coming\x01",
            "with you into Carnelia Tower.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_4617 end

    def Function_14_5104(): pass

    label("Function_14_5104")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_511B")
    Call(0, 29)
    Call(0, 31)

    label("loc_511B")

    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x13, 1060, 150, 53910, 180)
    SetChrPos(0xC, 2250, 0, 54450, 180)
    SetChrPos(0x101, -1140, 100, 52380, 90)
    SetChrPos(0x102, -1140, 100, 51220, 90)
    SetChrPos(0x8, -1140, 100, 49960, 90)
    SetChrPos(0x108, -1190, 100, 48660, 90)
    SetChrPos(0xA, 2950, 200, 52400, 270)
    SetChrPos(0x11, 2950, 200, 51200, 270)
    SetChrPos(0x10, 2950, 200, 49840, 270)
    SetChrPos(0x12, 2950, 200, 48620, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x13, 0x4)
    OP_4A(0x10, 255)
    OP_4A(0x8, 255)
    OP_4A(0x11, 255)
    OP_4A(0xA, 255)
    OP_4A(0x108, 255)
    OP_4A(0x12, 255)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 2)
    SetChrChipByIndex(0x108, 23)
    SetChrSubChip(0x108, 1)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 1)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 2)
    SetChrChipByIndex(0x11, 28)
    SetChrSubChip(0x11, 2)
    SetChrChipByIndex(0x12, 29)
    SetChrSubChip(0x12, 2)
    SetChrChipByIndex(0x13, 30)
    SetChrSubChip(0x13, 0)
    OP_72(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #113
        0x13,
        (
            "#103F#6PWhat in blazes? She climbed\x01",
            "the whole thing on her own?\x02\x03",

            "#101FHah! Shouldn't actually surprise me.\x01",
            "Kilika's always been quietly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "#171F#6PI had always heard that Kilika Rouran of the Zeiss\x01",
            "guildhouse was a tremendously capable woman.\x02\x03",

            "I hope I have the chance to\x01",
            "meet her in person one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1008F#5P(Erm. Kilika and Julia together...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1040F#2P(Those two could probably juggle\x01",
            "mountains, working together.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x108,
        (
            "#074F#2PAnyway...\x02\x03",

            "#072FIt's just like last time. The tower\x01",
            "has returned to normal, but the\x01",
            "machinery atop it no longer functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "#047FYes... It's worrying.\x02\x03",

            "#043FWe also still don't understand\x01",
            "the nature of those...barriers\x01",
            "that appear over the roofs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x11,
        (
            "#063FUm, I guess the question is 'why are\x01",
            "they covered up in the first place,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10,
        (
            "#053FPersonally, I think we can sweat that later.\x02\x03",

            "#050FRight now we need to get a\x01",
            "move on to the next tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1015F#5PYeah, good idea.\x02\x03",

            "#1002FJulia, don't suppose we have any\x01",
            "updates from the other towers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "#176F#6POne came in not long ago\x01",
            "from the Sapphirl Tower.\x02\x03",

            "#178FThis time it was a woman dressed\x01",
            "in black, wielding a bell, of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1020F#5PA bell? It's her...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(50)
    SetChrSubChip(0x11, 1)
    Sleep(50)
    SetChrSubChip(0xA, 1)
    Sleep(50)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    SetChrSubChip(0x102, 2)
    Sleep(400)

    ChrTalk(    #124
        0x102,
        (
            "#1043F#5PLuciola the Bewitching Bell.\x02\x03",

            "#1042F#5PShe was once an...acquaintance\x01",
            "of yours, wasn't she, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#026F#2PYes, she's an old friend.\x02\x03",

            "#524FThis means it's my turn\x01",
            "to tag along, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1026F#5PSchera...if you don't want to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#021F#2PC'mon, you. Don't make that face.\x02\x03",

            "#020FLuci is herself, and I'm me.\x01",
            "We can settle our differences\x01",
            "if we have time.\x02\x03",

            "Our first priority must be to\x01",
            "complete the mission we've\x01",
            "been given as bracers.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R2200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_5104 end

    def Function_15_59AF(): pass

    label("Function_15_59AF")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(950, 0, 51430, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(67000, 0)
    OP_6E(291, 0)
    OP_77(0xCC, 0x84, 0x55, 0x0, 0x0)
    OP_6D(2220, 100, 52500, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0x13, 1060, 150, 53910, 180)
    SetChrPos(0xC, 2250, 0, 54450, 180)
    SetChrPos(0x16, -1140, 100, 52380, 90)
    SetChrPos(0x17, -1140, 100, 51220, 90)
    SetChrPos(0x8, -1140, 100, 49960, 90)
    SetChrPos(0xB, -1190, 100, 48660, 90)
    SetChrPos(0xA, 2950, 200, 52400, 270)
    SetChrPos(0x11, 2950, 200, 51200, 270)
    SetChrPos(0x10, 2950, 200, 49840, 270)
    SetChrPos(0x12, 2950, 200, 48620, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x13, 0x4)
    OP_4A(0x10, 255)
    OP_4A(0x8, 255)
    OP_4A(0x11, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0x12, 255)
    SetChrChipByIndex(0x16, 19)
    SetChrSubChip(0x16, 1)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 1)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 2)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 1)
    SetChrChipByIndex(0x17, 26)
    SetChrSubChip(0x17, 1)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 2)
    SetChrChipByIndex(0x11, 28)
    SetChrSubChip(0x11, 2)
    SetChrChipByIndex(0x12, 29)
    SetChrSubChip(0x12, 2)
    SetChrChipByIndex(0x13, 30)
    SetChrSubChip(0x13, 0)
    OP_72(0xB, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #128
        0x13,
        (
            "#100F#6PThis, everyone, is my latest invention,\x01",
            "the Zero Field Generator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x16,
        "#1004F#5PZero...Field... What now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x13,
        (
            "#104F#6PPut simply: you are aware of the special\x01",
            "warp-field the Gospels produce, yes?\x02\x03",

            "#100FThis is a circuit which produces a field\x01",
            "to nullify that warp via a resonance wa--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x16,
        (
            "#1019F#5PThat does not qualify as 'simple'\x01",
            "under any definition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        (
            "#1044F#5PIf I understand correctly,\x01",
            "then, Professor...\x02\x03",

            "This can actually reverse the\x01",
            "Orbal Shutdown Phenomenon?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xC, 0x13, 400)

    ChrTalk(    #133
        0x16,
        "#1004F#5PWhoa, what?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        "#173F#4PIs that true, Professor?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x13,
        (
            "#104F#6PPrevent it, more specifically,\x01",
            "but just so.\x02\x03",

            "#102FUltimately, the 'shutdown phenomenon'\x01",
            "is just orbal energy being absorbed by\x01",
            "the Gospels.\x02\x03",

            "WHERE the energy went was a mystery,\x01",
            "but having come this far I think we finally\x01",
            "have an answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xA,
        (
            "#043F#4PTo the floating city...\x01",
            "To the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x13,
        (
            "#100F#6PIt is the only answer which makes sense.\x02\x03",

            "#104FThe Aureole uses the little holes between\x01",
            "dimensions generated by devices which we\x01",
            "call 'Gospels' to cause the phenomenon.\x02\x03",

            "Gospels are, all things considered,\x01",
            "small holes, so the area affected\x01",
            "was thankfully minor.\x02\x03",

            "With the Aureole made manifest once again,\x01",
            "however, that area has grown immensely.\x02\x03",

            "#102FEnough to engulf the entirety of Liberl and\x01",
            "even beyond our borders, I'd imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        "#1026F#5PAll of Liberl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x17,
        "#1042F#5PSo that's what's causing all this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x13,
        (
            "#104F#6PYes, I find it likely that every orbment\x01",
            "in the country, without exception, has\x01",
            "stopped working.\x02\x03",

            "#100FHowever, this Zero Field Generator\x01",
            "can stop the interference of the Aureole.\x02\x03",

            "#101FWhich is to say, put it next to\x01",
            "an orbment and that orbment\x01",
            "will work just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        "#560F#4PWooow...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x16,
        "#1008F#5PProfessor, that's amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10,
        (
            "#051F#4PSo we fire that thing up and\x01",
            "everything's cool, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x13,
        (
            "#102F#6PErm... Not quite, I'm afraid.\x02\x03",

            "#104FThe area this prototype can\x01",
            "protect is limited.\x02\x03",

            "It can shield, at most, an orbment\x01",
            "you could carry in two hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x11,
        "#065F#4PThat small? Aww...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10,
        (
            "#555F#4PWell, hell, that kinda limits\x01",
            "what we can do, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x13,
        (
            "#102F#6PThe other problem is...I only\x01",
            "have so many of them.\x02\x03",

            "Even as a favor for Cassius, I could\x01",
            "only put sixteen of them together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x16,
        (
            "#1015F#5PSixteen... That's actually a lot,\x01",
            "if anything.\x02\x03",

            "#1004FWait, Dad asked you for these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x13,
        (
            "#100F#6PYes, he requested that I work\x01",
            "on these a while back, actually.\x02\x03",

            "#104FI scarcely even imagined a crisis\x01",
            "on this scale at the time, but it\x01",
            "seems he did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x16,
        "#1016F#5PI, uh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "#070F#5PJust as I'd expect from Cassius. Always\x01",
            "seeing further than any other man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x12,
        (
            "#1065FThat bein' the case, though.\x02\x03",

            "#1060FPretty clear how we should\x01",
            "use these things, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x13,
        "#103F#6PAh, you're a sharp one, Father!\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x16, 0)
    Sleep(75)
    SetChrSubChip(0x16, 2)
    Sleep(300)

    ChrTalk(    #154
        0x16,
        "#1004F#5PUh, I don't quite follow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x12,
        (
            "#1063F#2PSo in a crisis like this, the thing you need\x01",
            "more than ANYTHING else is fast, accurate\x01",
            "communication.\x02\x03",

            "Whether it's about the society throwing bears\x01",
            "at people, or where goods need to be taken,\x01",
            "if you can't communicate, you're up a creek.\x02\x03",

            "#1062FMeaning...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x17, 0)
    Sleep(75)
    SetChrSubChip(0x17, 2)
    Sleep(300)

    ChrTalk(    #156
        0x17,
        (
            "#1035F#5PThey should be used to restore\x01",
            "communication devices all over\x01",
            "Liberl.\x02\x03",

            "#1040FIs that about the size of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x12,
        "#1061F#2PBingo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x16,
        "#1006F#5PThat IS a good idea!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    Sleep(500)

    ChrTalk(    #159
        0xC,
        (
            "#176F#6PMmm. For the military, not being able\x01",
            "to use our guns or airships is dire.\x02\x03",

            "#178FNot having communications between\x01",
            "headquarters and our forces is even more\x01",
            "serious, however.\x02\x03",

            "We should restore communications\x01",
            "between Grancel Castle, the Haken Gate,\x01",
            "and Leiston Fortress a.s.a.p.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x16, 0)
    Sleep(75)
    SetChrSubChip(0x16, 1)
    Sleep(50)
    SetChrSubChip(0x17, 0)
    Sleep(75)
    SetChrSubChip(0x17, 1)
    Sleep(300)

    ChrTalk(    #160
        0x8,
        (
            "#026F#5PThe guild's in the same boat, in a way.\x02\x03",

            "#020FIf the branches can't get in touch,\x01",
            "it'll be hard to mount any response\x01",
            "to anything that might happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x13,
        (
            "#104F#6PSounds as if we're all\x01",
            "in agreement, then.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(300)

    ChrTalk(    #162
        0x13,
        (
            "#100F#6PWell, then, Captain Schwarz.\x02\x03",

            "I'll provide ten Zero Field Generators\x01",
            "to the Royal Army.\x02\x03",

            "#101FThat should give you enough to cover\x01",
            "the Arseille, the capital, the gate,\x01",
            "Leiston, and all regional posts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 400)
    Sleep(500)

    ChrTalk(    #163
        0xC,
        (
            "#171F#4PYou have my thanks, Professor.\x02\x03",

            "I'll order my men to distribute\x01",
            "them immediately.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x13, 0)
    Sleep(75)
    SetChrSubChip(0x13, 2)
    Sleep(300)

    ChrTalk(    #164
        0x13,
        (
            "#100F#6PAnd the remaining six go\x01",
            "to the Bracer Guild.\x02\x03",

            "That should be enough to restore\x01",
            "the phone in each guild branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x16,
        "#1006F#5PWe'll get right on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x17,
        "#1040F#5PWe'll see them safely there.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_59AF end

    def Function_16_6DEF(): pass

    label("Function_16_6DEF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_D2(0x270003, 0x270007, 0x13)
    OP_D2(0x270013, 0x270017, 0x14)
    OP_D2(0x70023, 0x7002B, 0x15)
    OP_D2(0x70033, 0x7003B, 0x16)
    OP_D2(0x27039B, 0x27039F, 0x17)
    OP_D2(0x70053, 0x7005B, 0x18)
    OP_D2(0x70063, 0x7006B, 0x19)
    OP_D2(0x70073, 0x7007B, 0x1A)
    OP_D2(0x270083, 0x270087, 0x1B)
    OP_D2(0x7046C, 0x70470, 0x1C)
    OP_D2(0x2703E0, 0x2703E5, 0x1D)
    OP_D2(0x7047B, 0x7047F, 0x1E)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x102, 20)
    SetChrChipByIndex(0x8, 21)
    SetChrChipByIndex(0x9, 22)
    SetChrChipByIndex(0xA, 23)
    SetChrChipByIndex(0x10, 24)
    SetChrChipByIndex(0x11, 25)
    SetChrChipByIndex(0xB, 26)
    SetChrChipByIndex(0x12, 27)
    SetChrChipByIndex(0x13, 28)
    SetChrChipByIndex(0x18, 29)
    SetChrChipByIndex(0xC, 30)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x18, 0x4)
    OP_6D(2570, 100, 51210, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    SetChrPos(0xC, 1060, 200, 53910, 180)
    SetChrPos(0xA, 2950, 200, 52420, 270)
    SetChrPos(0x9, 2950, 200, 51220, 270)
    SetChrPos(0x18, 2950, 300, 49990, 270)
    SetChrPos(0x13, 2950, 200, 48730, 270)
    SetChrPos(0x11, 2950, 200, 47540, 270)
    SetChrPos(0x12, 2950, 200, 46360, 270)
    SetChrPos(0x101, -1100, 100, 52380, 90)
    SetChrPos(0x102, -1100, 100, 51220, 90)
    SetChrPos(0x8, -1100, 100, 49960, 90)
    SetChrPos(0x10, -1100, 100, 48660, 90)
    SetChrPos(0xB, -1100, 100, 47570, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_4A(0x10, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x11, 255)
    OP_4A(0xA, 255)
    OP_4A(0x12, 255)
    OP_4A(0xB, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #167
        0x13,
        (
            "#104F#4PThe damage to the Arseille looks\x01",
            "worse than it actually is.\x02\x03",

            "The engines themselves are virtually untouched,\x01",
            "and the flight field generator mostly just needs to\x01",
            "be beaten furiously with a wrench.\x02\x03",

            "#102FThe problem lies in a lot of our finer\x01",
            "systems--our stabilizers, for starters.\x02\x03",

            "Ironically, we can plow forward just fine,\x01",
            "but hovering steadily would be an issue\x01",
            "as things stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xC,
        "#178F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x18,
        (
            "#272F#7POur first order of business needs to be\x01",
            "organizing everyone we can for repairs,\x01",
            "then.\x02\x03",

            "#277FI may be an outsider here, but I'll\x01",
            "help in any way you require.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xC,
        "#176F#6PThank you, Vander.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x9,
        (
            "#035F#4PThat will solve the problem with the\x01",
            "Arseille, but our real struggle will be\x01",
            "locating the Aureole in this massive city.\x02\x03",

            "#030FEspecially since it seems likely our friends\x01",
            "in the society are already here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 1)
    Sleep(200)

    ChrTalk(    #172
        0xA,
        (
            "#1163F#6PYes...\x02\x03",

            "If they claim the Aureole, who\x01",
            "knows what they may do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#025F#5PGiven everything they've done until now,\x01",
            "you have to imagine it would be nothing\x01",
            "good for anyone else.\x02\x03",

            "#022FWe need to get out there and\x01",
            "find a way to stop them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        (
            "#555F#5PNo complaints to that idea here.\x02\x03",

            "We should get moving right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "#074F#5PTrying to run off in multiple small\x01",
            "groups would just be chaos, though.\x02\x03",

            "#070FI think it would be wisest to use\x01",
            "a single exploration team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1015F#5PYeah, I agree.\x02\x03",

            "#1007FAnd the first thing we gotta find is some kinda\x01",
            "powered means of getting around the city.\x01",
            "Trying to walk would take forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x102,
        "#1043F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #178
        0x101,
        "#1004F#5PWhat is it, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#1035F#5PIt's nothing, really.\x02\x03",

            "#1042FAnyway. The exploration team is\x01",
            "going to need backup.\x02\x03",

            "Ideally, we should have people ready\x01",
            "to swap in and out as soon as the\x01",
            "team returns to the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xC,
        (
            "#176F#6PA good idea.\x02\x03",

            "I'd like to join in myself, but right now\x01",
            "I need to oversee the Arseille's repairs.\x02\x03",

            "#178FLet's go ahead and decide\x01",
            "who's leaving, first.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_31(0x4, 0xFE, 0x0)
    OP_41(0x4, 0x87, 0xFF)
    OP_41(0x4, 0x107, 0xFF)
    OP_41(0x4, 0x128, 0xFF)
    OP_37(0x4, 0x80, 0x2)
    OP_41(0x4, 0x294, 0x0)
    OP_41(0x4, 0x266, 0x1)
    OP_41(0x4, 0x25D, 0x2)
    OP_41(0x4, 0x2CA, 0x4)
    OP_41(0x4, 0x269, 0x5)
    OP_31(0x3, 0xFE, 0x0)
    OP_41(0x3, 0x6E, 0xFF)
    OP_41(0x3, 0x105, 0xFF)
    OP_41(0x3, 0x126, 0xFF)
    OP_37(0x3, 0x80, 0x2)
    OP_41(0x3, 0x296, 0x0)
    OP_41(0x3, 0x26C, 0x1)
    OP_41(0x3, 0x263, 0x2)
    OP_41(0x3, 0x260, 0x3)
    OP_41(0x3, 0x26F, 0x4)
    OP_41(0x3, 0x272, 0x5)
    OP_31(0x8, 0xFE, 0x0)
    OP_41(0x8, 0xED, 0xFF)
    OP_41(0x8, 0x105, 0xFF)
    OP_41(0x8, 0x126, 0xFF)
    OP_37(0x8, 0x80, 0x2)
    OP_37(0x8, 0x81, 0x2)
    OP_37(0x8, 0x82, 0x2)
    OP_37(0x8, 0x83, 0x2)
    OP_41(0x8, 0x275, 0x0)
    OP_41(0x8, 0x25D, 0x1)
    OP_41(0x8, 0x294, 0x2)
    OP_41(0x8, 0x29C, 0x3)
    OP_41(0x8, 0x263, 0x4)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_790D")
    Call(0, 29)

    label("loc_790D")

    SetChrName("")

    AnonymousTalk(    #181
        (
            "\x07\x05Please form your party. You may choose one other\x01",
            "member aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xC, 2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, -1100, 100, 52380, 90)
    SetChrPos(0x102, -1100, 100, 51220, 90)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x102, 20)
    OP_6D(2570, 100, 51210, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #182
        0xC,
        (
            "#170F#6PAll right, Estelle.\x01",
            "Your group of four will explore the city.\x02\x03",

            "Do remember that we have no idea\x01",
            "what's out there, society or otherwise.\x01",
            "Don't do anything too foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1006F#5PDon't worry, we'll be fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        (
            "#1040F#5PWe'll be looking for a way around\x01",
            "the city ahead of anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xC,
        "#176F#6PGood luck to you, then!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #186
        0xC,
        (
            "#178F#6PEveryone else will remain behind on\x01",
            "standby and help repair the Arseille.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C45")

    ChrTalk(    #187
        0x11,
        "#560F#2POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C9E")

    label("loc_7C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C6E")

    ChrTalk(    #188
        0x10,
        "#051F#5PNo problem.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C9E")

    label("loc_7C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C9E")

    ChrTalk(    #189
        0xB,
        "#070F#5PWe'll do what we can!\x02",
    )

    CloseMessageWindow()

    label("loc_7C9E")


    ChrTalk(    #190
        0x13,
        (
            "#103F#4POh, by the way, that reminds me.\x01",
            "One other small mercy...\x02\x03",

            "#100FThe shutdown phenomenon doesn't seem\x01",
            "to be happening here on the island.\x02\x03",

            "Your tactical orbments should work just\x01",
            "fine away from the Arseille, even without\x01",
            "handheld Zero Field Generators.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x101, 2)
    Sleep(50)
    SetChrSubChip(0x102, 2)
    SetChrSubChip(0x18, 1)
    Sleep(50)
    SetChrSubChip(0x9, 1)
    Sleep(50)
    SetChrSubChip(0x12, 2)
    Sleep(50)
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #191
        0x101,
        "#1004F#5PReally? Well, hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x11,
        "#064F#2PGrandpa, how can you tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x13,
        (
            "#104F#4PWell, truth be told, the biggest casualty\x01",
            "of the crash was the Arseille's ZFG.\x02\x03",

            "#102FBut even with it in pieces, all our other\x01",
            "orbal systems are operating just fine.\x02\x03",

            "Father Graham's theory seems to\x01",
            "have been right on the mark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x12,
        (
            "#1065F#2PRight, the Aureole neutralizes 'foreign'\x01",
            "orbal elements...\x02\x03",

            "#1060F...but if we can get onto the island,\x01",
            "we surely can't be 'foreign,' right, guys?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(300)

    ChrTalk(    #195
        0x13,
        (
            "#101F#6PYes, I'm willing to guess it can't\x01",
            "tell the difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1007F#5PWhew, yeah, talk about small mercies.\x02\x03",

            "#1008FGoing out there without any arts or\x01",
            "anything would be kinda...harsh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#1040F#5PI take it that means the orbal workshop\x01",
            "tools are also functional?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 0)
    Sleep(200)

    ChrTalk(    #198
        0x13,
        (
            "#100F#4POh, yes, everything survived the\x01",
            "crash just fine.\x02\x03",

            "#101FIf you need your orbments tuned\x01",
            "up, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1006F#5PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x102,
        "#1040F#5PI suspect we'll be stopping by a lot.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x8, 0xFE, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_BB(0x4, 0x1, 0x1D)
    OP_BD()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 36)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0x12, 12)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0xC, 4)
    OP_6D(1490, 0, 2300, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x7, 0x10)
    OP_6F(0x7, 0)
    OP_70(0x7, 0xF)
    OP_73(0x7)
    OP_43(0x13, 0x1, 0x0, 0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_844E")
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x11)

    label("loc_844E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8467")
    Sleep(800)
    OP_43(0x10, 0x1, 0x0, 0x11)

    label("loc_8467")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8480")
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x11)

    label("loc_8480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8499")
    Sleep(800)
    OP_43(0xB, 0x1, 0x0, 0x11)

    label("loc_8499")

    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84BE")
    Sleep(800)
    OP_43(0xA, 0x1, 0x0, 0x12)

    label("loc_84BE")

    Sleep(800)
    OP_43(0x18, 0x1, 0x0, 0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84E3")
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x12)

    label("loc_84E3")

    Sleep(2000)

    def lambda_84EE():
        OP_6D(1700, 0, 810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_84EE)

    def lambda_8506():
        OP_6B(2690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8506)
    OP_43(0x101, 0x1, 0x0, 0x13)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8574")
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x16)
    Sleep(1500)
    OP_71(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    Jump("loc_85B4")

    label("loc_8574")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85B4")
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x16)
    Sleep(1500)
    OP_71(0x6, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)

    label("loc_85B4")

    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #201
        0x101,
        (
            "#1015FOkay, then...\x02\x03",

            "Is everyone ready to take a look\x01",
            "around outside the ship?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8649")

    ChrTalk(    #202
        0x105,
        "#1382F#6PYes, let's be off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8728")

    label("loc_8649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8675")

    ChrTalk(    #203
        0x103,
        "#020F#6PAll set here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8728")

    label("loc_8675")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_869E")

    ChrTalk(    #204
        0x104,
        "#035F#6PAfter you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8728")

    label("loc_869E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86CE")

    ChrTalk(    #205
        0x106,
        "#051F#6PReady for action.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8728")

    label("loc_86CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86F9")

    ChrTalk(    #206
        0x107,
        "#560F#6PI'm all set!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8728")

    label("loc_86F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8728")

    ChrTalk(    #207
        0x108,
        "#070F#6PReady when you are!\x02",
    )

    CloseMessageWindow()

    label("loc_8728")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #208
        0x102,
        (
            "#1035F#6P...Sorry, Estelle.\x02\x03",

            "#1040FI actually need to...prepare something\x01",
            "from the ship's storeroom. Something to\x01",
            "help if I need to sneak around again.\x02\x03",

            "Could I ask you to wait a bit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #209
        0x101,
        "#1004F#5POh, uh, sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x109,
        (
            "#1062F#1POooh, hey, I...should probably tune\x01",
            "up my crossbow, come to think of it!\x01",
            "Lemme join you.\x02\x03",

            "#1061FEstelle, why don't you and the gang\x01",
            "hang out in the lounge for a bit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(300)

    ChrTalk(    #211
        0x101,
        "#1006FWell, okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8924")

    ChrTalk(    #212
        0x105,
        "#1168F#6PWe will be waiting, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A40")

    label("loc_8924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_895F")

    ChrTalk(    #213
        0x103,
        "#021F#6PWait in the lounge? Happily.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A40")

    label("loc_895F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89A4")

    ChrTalk(    #214
        0x104,
        "#035F#6PHeh... Do not tarry overlong, friends.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A40")

    label("loc_89A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89DD")

    ChrTalk(    #215
        0x106,
        "#051F#6PDon't take too long, guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A40")

    label("loc_89DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A13")

    ChrTalk(    #216
        0x107,
        "#061F#6POkay, we'll be waiting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A40")

    label("loc_8A13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A40")

    ChrTalk(    #217
        0x108,
        "#071F#6PWe'll be waiting!\x02",
    )

    CloseMessageWindow()

    label("loc_8A40")

    OP_43(0x101, 0x1, 0x0, 0x18)

    def lambda_8A4D():

        label("loc_8A4D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8A4D")

    QueueWorkItem2(0x102, 1, lambda_8A4D)
    Sleep(100)

    def lambda_8A63():

        label("loc_8A63")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8A63")

    QueueWorkItem2(0x109, 1, lambda_8A63)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A8F")
    OP_43(0xF9, 0x1, 0x0, 0x1A)
    WaitChrThread(0xF9, 0x1)
    Jump("loc_8AA8")

    label("loc_8A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AA8")
    OP_43(0xF8, 0x1, 0x0, 0x1A)
    WaitChrThread(0xF8, 0x1)

    label("loc_8AA8")

    Sleep(1500)
    OP_44(0x102, 0x1)
    OP_44(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #218
        0x109,
        (
            "#1067F#5PMy man, you are a dude of many\x01",
            "talents, but lying ain't one of 'em.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 400)
    Sleep(300)

    ChrTalk(    #219
        0x102,
        "#1043FI'm sorry... Lying to her isn't...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 400)
    Sleep(300)

    ChrTalk(    #220
        0x109,
        (
            "#1065F#1PI think the one you should apologize\x01",
            "to eventually is Estelle.\x02\x03",

            "#1063FAnyway. You're...sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        (
            "#1035FYes. I've made my decision.\x02\x03",

            "#1040FKevin... Father Kevin...please.\x01",
            "You're the only one who can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x109,
        (
            "#1068F#1PAll right, all right.\x01",
            "Don't need to lay it on THAT thick.\x02\x03",

            "#1060FC'mon, that little lie ain't gonna buy us\x01",
            "much time. Let's get to the medical bay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9499")

    label("loc_8CD2")

    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x15)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x16)
    Sleep(1500)
    OP_71(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #223
        0x101,
        (
            "#1015FOkay, then...\x02\x03",

            "Is everyone ready to take a look\x01",
            "around outside the ship?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D97")

    ChrTalk(    #224
        0x105,
        "#1382FYes, let's be off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E67")

    label("loc_8D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DC0")

    ChrTalk(    #225
        0x103,
        "#020FAll set here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E67")

    label("loc_8DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DE6")

    ChrTalk(    #226
        0x104,
        "#035FAfter you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E67")

    label("loc_8DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E13")

    ChrTalk(    #227
        0x106,
        "#051FReady for action.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E67")

    label("loc_8E13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E3B")

    ChrTalk(    #228
        0x107,
        "#560FI'm all set!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E67")

    label("loc_8E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E67")

    ChrTalk(    #229
        0x108,
        "#070FReady when you are!\x02",
    )

    CloseMessageWindow()

    label("loc_8E67")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #230
        0x102,
        (
            "#1035F#6P...Sorry, Estelle.\x02\x03",

            "#1040FI actually need to...prepare something\x01",
            "from the ship's storeroom. Something to\x01",
            "help if I need to sneak around again.\x02\x03",

            "Could I ask you to wait a bit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #231
        0x101,
        (
            "#1004F#5POh, uh, sure!\x02\x03",

            "#1015FDo you want some help?\x01",
            "Speed things up a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x102,
        (
            "#1049F#6PNo, it's sort of a one-person job.\x02\x03",

            "#1040FI don't think it will take more than\x01",
            "thirty minutes or so. Could you wait\x01",
            "in the lounge until then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#1006F#5PWell, okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_906E")

    ChrTalk(    #234
        0x108,
        "#071FWe'll be waiting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_906E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90A1")

    ChrTalk(    #235
        0x107,
        "#061FOkay, we'll be waiting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_90A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90D9")

    ChrTalk(    #236
        0x106,
        "#051FDon't take too long, Joshua.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_90D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_911A")

    ChrTalk(    #237
        0x104,
        (
            "#035FHeh...\x01",
            "Do not tarry overlong, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_911A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9152")

    ChrTalk(    #238
        0x103,
        "#021FWait in the lounge? Happily.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_9152")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9185")

    ChrTalk(    #239
        0x105,
        "#1168FWe will be waiting, then.\x02",
    )

    CloseMessageWindow()

    label("loc_9185")

    OP_43(0x101, 0x1, 0x0, 0x18)

    def lambda_9192():

        label("loc_9192")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_9192")

    QueueWorkItem2(0x102, 1, lambda_9192)
    Sleep(1000)
    OP_43(0xF8, 0x1, 0x0, 0x19)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x1A)
    WaitChrThread(0xF9, 0x1)
    Sleep(1500)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 1020, 0, 5300, 180)
    OP_72(0x7, 0x10)
    OP_6F(0x7, 0)
    OP_70(0x7, 0xF)
    OP_73(0x7)
    Sleep(500)

    NpcTalk(    #240
        0x12,
        "Young Man's Voice",
        (
            "#4PMy man, you are a dude of many\x01",
            "talents, but lying ain't one of 'em.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9253():
        OP_6D(2490, 0, 1310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9253)
    OP_43(0x12, 0x1, 0x0, 0x17)

    def lambda_9272():

        label("loc_9272")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_9272")

    QueueWorkItem2(0x102, 1, lambda_9272)
    Sleep(1500)
    OP_72(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0x1)

    ChrTalk(    #241
        0x102,
        "#1043F#7PI'm sorry... Lying to her isn't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x12,
        (
            "#1065F#6PI think the one you should apologize to\x01",
            "eventually is Estelle.\x02\x03",

            "#1063FAnyway. You're...sure?\x01",
            "If I'm right, this could backfire and,\x01",
            "uh, mess you up. Like...badly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#1035F#7PYes. I've made my decision.\x02\x03",

            "#1040FKevin... Father Kevin...please.\x01",
            "You're the only one who can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x12,
        (
            "#1068F#6PArright, arright.\x01",
            "Don't need to lay it on THAT thick.\x02\x03",

            "#1060FC'mon, that little lie ain't gonna buy us\x01",
            "much time. Let's get to the medical bay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9499")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6D(-1470, 0, -49280, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_9560"),
        (3, "loc_956D"),
        (4, "loc_957A"),
        (5, "loc_9587"),
        (6, "loc_9594"),
        (7, "loc_95A1"),
        (SWITCH_DEFAULT, "loc_95AE"),
    )


    label("loc_9560")

    OP_D2(0x70023, 0x7002B, 0x14)
    Jump("loc_95AE")

    label("loc_956D")

    OP_D2(0x70033, 0x7003B, 0x14)
    Jump("loc_95AE")

    label("loc_957A")

    OP_D2(0x27039B, 0x27039F, 0x14)
    Jump("loc_95AE")

    label("loc_9587")

    OP_D2(0x70053, 0x7005B, 0x14)
    Jump("loc_95AE")

    label("loc_9594")

    OP_D2(0x70063, 0x7006B, 0x14)
    Jump("loc_95AE")

    label("loc_95A1")

    OP_D2(0x70073, 0x7007B, 0x14)
    Jump("loc_95AE")

    label("loc_95AE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_95CF"),
        (3, "loc_95DC"),
        (4, "loc_95E9"),
        (5, "loc_95F6"),
        (6, "loc_9603"),
        (7, "loc_9610"),
        (SWITCH_DEFAULT, "loc_961D"),
    )


    label("loc_95CF")

    OP_D2(0x70023, 0x7002B, 0x15)
    Jump("loc_961D")

    label("loc_95DC")

    OP_D2(0x70033, 0x7003B, 0x15)
    Jump("loc_961D")

    label("loc_95E9")

    OP_D2(0x27039B, 0x27039F, 0x15)
    Jump("loc_961D")

    label("loc_95F6")

    OP_D2(0x70053, 0x7005B, 0x15)
    Jump("loc_961D")

    label("loc_9603")

    OP_D2(0x70063, 0x7006B, 0x15)
    Jump("loc_961D")

    label("loc_9610")

    OP_D2(0x70073, 0x7007B, 0x15)
    Jump("loc_961D")

    label("loc_961D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_968B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965B")
    SetChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF9, 21)
    SetChrPos(0xF9, -2400, 200, -47940, 180)
    ClearChrFlags(0xF9, 0x80)
    Jump("loc_9688")

    label("loc_965B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9688")
    SetChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 20)
    SetChrPos(0xF8, -2400, 200, -47940, 180)
    ClearChrFlags(0xF8, 0x80)

    label("loc_9688")

    Jump("loc_96CB")

    label("loc_968B")

    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF8, 20)
    SetChrChipByIndex(0xF9, 21)
    SetChrPos(0xF8, -450, 200, -50200, 0)
    SetChrPos(0xF9, -2400, 200, -47940, 180)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)

    label("loc_96CB")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrPos(0x101, -2400, 200, -50200, 0)
    ClearChrFlags(0x101, 0x80)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9958")
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9731")
    SetChrSubChip(0xF9, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Jump("loc_974D")

    label("loc_9731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974D")
    SetChrSubChip(0xF8, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)

    label("loc_974D")

    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x1B)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x1C)

    def lambda_976B():
        OP_6D(-800, 200, -47820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_976B)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #245
        0x101,
        "#1004F#5PJoshua, Kevin! You're done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        "#1040F#6PSorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x109,
        (
            "#1061F#4PYeah, sorry.\x01",
            "Preparing that took a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1015F#5PI don't mind, but...are you two okay?\x02\x03",

            "You look...tired, unless I'm crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x109,
        "#1064F#4PErm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        (
            "#1035F#6PSome of it took a lot\x01",
            "of concentration.\x02\x03",

            "#1040FDon't worry, we're fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x109,
        (
            "#1066F#4PY-Yeah! The stuff Joshua made\x01",
            "will really help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1025F#5PWell, if you say so.\x02\x03",

            "#1006FLet's get going, then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF1")

    label("loc_9958")

    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xF9, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x1B)

    def lambda_9983():
        OP_6D(-540, 0, -48040, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9983)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #253
        0x101,
        "#1004F#5PJoshua! You're done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        (
            "#1040F#6PSorry to keep you waiting.\x01",
            "That took a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        (
            "#1015F#5PI don't mind, but...\x01",
            "Joshua, are you okay?\x02\x03",

            "You look...tired, unless I'm crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x102,
        (
            "#1035F#6PSome of it took a lot\x01",
            "of concentration.\x02\x03",

            "#1040FDon't worry, I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#1025F#5PWell, if you say so.\x02\x03",

            "#1006FLet's get going, then!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(30, 0, -44840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 30, 0, -44840, 0)
    SetChrPos(0x1, 30, 0, -44840, 0)
    SetChrPos(0x2, 30, 0, -44840, 0)
    SetChrPos(0x3, 30, 0, -44840, 0)
    Sleep(500)
    OP_71(0x7, 0x10)
    OP_A2(0x2201)
    OP_28(0x9C, 0x1, 0x40)
    OP_28(0x9D, 0x4, 0x2)
    OP_28(0x9D, 0x4, 0x8)
    OP_28(0x9D, 0x1, 0x1)
    OP_28(0x9D, 0x1, 0x2)
    OP_28(0x9D, 0x1, 0x4)
    OP_28(0x9D, 0x1, 0x8)
    OP_C4(0x1, 0x8)
    OP_A2(0x1E0B)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_6DEF end

    def Function_17_9C08(): pass

    label("Function_17_9C08")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3FC, 0x0, 0x866, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1414, 0x0, 0x866, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1414, 0xFFFFF862, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_9C08 end

    def Function_18_9C6B(): pass

    label("Function_18_9C6B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3CA, 0x0, 0x730, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC90, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF420, 0x0, 0x46, 0x7D0, 0x0)

    def lambda_9CC3():
        OP_8E(0xFE, 0xFFFFF3DA, 0x960, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_9CC3)
    Sleep(1800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_9C6B end

    def Function_19_9CEE(): pass

    label("Function_19_9CEE")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3A2, 0x0, 0xFFFFFC72, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_9CEE end

    def Function_20_9D20(): pass

    label("Function_20_9D20")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x492, 0x0, 0x5C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x820, 0x0, 0x154, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_9D20 end

    def Function_21_9D66(): pass

    label("Function_21_9D66")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x4A6, 0x0, 0x8E8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0xD2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_21_9D66 end

    def Function_22_9DAC(): pass

    label("Function_22_9DAC")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3FC, 0x0, 0x62C, 0x7D0, 0x0)
    Return()

    # Function_22_9DAC end

    def Function_23_9DD7(): pass

    label("Function_23_9DD7")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x5E6, 0x0, 0x7B2, 0x7D0, 0x0)
    Return()

    # Function_23_9DD7 end

    def Function_24_9E02(): pass

    label("Function_24_9E02")

    OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF9CA, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_9E26():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_9E26)
    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_9E02 end

    def Function_25_9E51(): pass

    label("Function_25_9E51")

    OP_8E(0xFE, 0x3DE, 0x32, 0xFFFFFB32, 0x7D0, 0x0)

    def lambda_9E6B():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_9E6B)
    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_9E51 end

    def Function_26_9E96(): pass

    label("Function_26_9E96")


    def lambda_9E9C():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_9E9C)
    Sleep(2000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    OP_22(0x6D, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_9E96 end

    def Function_27_9ECC(): pass

    label("Function_27_9ECC")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 490, 0, -39390, 180)
    OP_8E(0xFE, 0x186, 0x0, 0xFFFF51A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0xFFFF48CC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_27_9ECC end

    def Function_28_9F12(): pass

    label("Function_28_9F12")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 490, 0, -39390, 180)
    OP_8E(0xFE, 0x186, 0x0, 0xFFFF51A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x17C, 0x0, 0xFFFF4700, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_9F12 end

    def Function_29_9F58(): pass

    label("Function_29_9F58")

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
        (0, "loc_9FD1"),
        (1, "loc_9FD7"),
        (SWITCH_DEFAULT, "loc_9FDD"),
    )


    label("loc_9FD1")

    OP_A2(0x1200)
    Jump("loc_9FDD")

    label("loc_9FD7")

    OP_A2(0x1201)
    Jump("loc_9FDD")

    label("loc_9FDD")

    Return()

    # Function_29_9F58 end

    def Function_30_9FDE(): pass

    label("Function_30_9FDE")

    FadeToDark(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_30_9FDE end

    def Function_31_A06D(): pass

    label("Function_31_A06D")

    FadeToDark(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
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

    # Function_31_A06D end

    def Function_32_A0FA(): pass

    label("Function_32_A0FA")

    FadeToDark(0, 0, -1)
    OP_6D(-25340, 0, 52840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_32_A0FA end

    def Function_33_A18B(): pass

    label("Function_33_A18B")

    OP_A2(0xF)
    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_33_A18B end

    def Function_34_A1A5(): pass

    label("Function_34_A1A5")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x3E)
    Return()

    # Function_34_A1A5 end

    SaveToFile()

Try(main)
