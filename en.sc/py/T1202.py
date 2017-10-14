from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1202   ._SN',
        MapName             = 'Bose',
        Location            = 'T1202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1202_1 ._SN',
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
        'Loewe',                                # 9
        'General Morgan',                       # 10
        '花束',                                 # 11
        '花束',                                 # 12
        '花束',                                 # 13
        'Elder Reisen',                         # 14
        'Figaro',                               # 15
        'Pesca',                                # 16
        'Gray',                                 # 17
        'Vince',                                # 18
        'Lewey',                                # 19
        'Fran',                                 # 20
        'Sting',                                # 21
        'Birnette',                             # 22
        'Mirano',                               # 23
        'Targeting Camera',                     # 24
        'Ravennue Trail',                       # 25
        'Abandoned Mine Trail',                 # 26
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
        'ED6_DT26/CH20356 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT06/CH20137 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT07/CH00054 ._CH',             # 09
        'ED6_DT26/CH20355 ._CH',             # 0A
        'ED6_DT26/CH20357 ._CH',             # 0B
        'ED6_DT07/CH01490 ._CH',             # 0C
        'ED6_DT07/CH01060 ._CH',             # 0D
        'ED6_DT07/CH01470 ._CH',             # 0E
        'ED6_DT07/CH01070 ._CH',             # 0F
        'ED6_DT07/CH01230 ._CH',             # 10
        'ED6_DT26/CH20354 ._CH',             # 11
        'ED6_DT27/CH03540 ._CH',             # 12
        'ED6_DT27/CH03790 ._CH',             # 13
        'ED6_DT07/CH01180 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT26/CH20356P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT06/CH20137P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT07/CH00054P._CP',             # 09
        'ED6_DT26/CH20355P._CP',             # 0A
        'ED6_DT26/CH20357P._CP',             # 0B
        'ED6_DT07/CH01490P._CP',             # 0C
        'ED6_DT07/CH01060P._CP',             # 0D
        'ED6_DT07/CH01470P._CP',             # 0E
        'ED6_DT07/CH01070P._CP',             # 0F
        'ED6_DT07/CH01230P._CP',             # 10
        'ED6_DT26/CH20354P._CP',             # 11
        'ED6_DT27/CH03540P._CP',             # 12
        'ED6_DT27/CH03790P._CP',             # 13
        'ED6_DT07/CH01180P._CP',             # 14
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        X                   = 33060,
        Z                   = 8000,
        Y                   = 36610,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 20640,
        Z                   = -4000,
        Y                   = 19180,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 19590,
        Z                   = -4000,
        Y                   = 16200,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 17380,
        Z                   = -4000,
        Y                   = 9850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -120,
        Z                   = 0,
        Y                   = 28460,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -1120,
        Z                   = 0,
        Y                   = 26660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2120,
        Z                   = 0,
        Y                   = 28460,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4040,
        Z                   = 0,
        Y                   = 17210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 33030,
        Z                   = 8000,
        Y                   = 35790,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 25990,
        Z                   = -4000,
        Y                   = 14870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2080,
        Z                   = 0,
        Y                   = -80,
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
        X                   = 7170,
        Z                   = 8000,
        Y                   = 78890,
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
        X                   = 5000,
        Y                   = 0,
        Z                   = 34240,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 5150,
        Y                   = 4550,
        Z                   = 41780,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 5310,
        Y                   = 0,
        Z                   = 23020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4400,
        Z                   = 54640,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = -3900,
        Y                   = -100,
        Z                   = 7250,
        Range               = -100,
        Unknown_10          = 0x76C,
        Unknown_14          = 0x203A,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 5100,
        Y                   = 8000,
        Z                   = 67350,
        Range               = 9000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x10AFE,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = 34960,
        TriggerZ            = -3850,
        TriggerY            = 8220,
        TriggerRange        = 1000,
        ActorX              = 35010,
        ActorZ              = -4200,
        ActorY              = 5190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33020,
        TriggerZ            = 8000,
        TriggerY            = 35080,
        TriggerRange        = 1000,
        ActorX              = 33020,
        ActorZ              = 9200,
        ActorY              = 35080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_49A",          # 00, 0
        "Function_1_671",          # 01, 1
        "Function_2_73E",          # 02, 2
        "Function_3_8BB",          # 03, 3
        "Function_4_935",          # 04, 4
        "Function_5_959",          # 05, 5
        "Function_6_9EE",          # 06, 6
        "Function_7_A12",          # 07, 7
        "Function_8_BB2",          # 08, 8
        "Function_9_12CA",         # 09, 9
        "Function_10_1A8D",        # 0A, 10
        "Function_11_1D5D",        # 0B, 11
        "Function_12_2164",        # 0C, 12
        "Function_13_29F8",        # 0D, 13
        "Function_14_2D35",        # 0E, 14
        "Function_15_2FD7",        # 0F, 15
        "Function_16_4432",        # 10, 16
        "Function_17_4744",        # 11, 17
        "Function_18_6AEA",        # 12, 18
        "Function_19_6B37",        # 13, 19
        "Function_20_6B89",        # 14, 20
        "Function_21_6BCD",        # 15, 21
        "Function_22_6C0A",        # 16, 22
        "Function_23_6C47",        # 17, 23
        "Function_24_6C94",        # 18, 24
        "Function_25_6CB0",        # 19, 25
        "Function_26_6CB6",        # 1A, 26
        "Function_27_6DC0",        # 1B, 27
        "Function_28_6EAD",        # 1C, 28
        "Function_29_6EB1",        # 1D, 29
        "Function_30_6EB5",        # 1E, 30
    )


    def Function_0_49A(): pass

    label("Function_0_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_4BC")
    OP_A2(0x1C01)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_4DF")

    label("loc_4BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_56A")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xF, 18320, -4000, 10850, 208)
    SetChrPos(0x11, 24450, -4000, 9390, 180)
    SetChrPos(0x13, 22320, -4000, 11950, 154)
    SetChrPos(0x12, 14750, -4000, 21340, 270)
    SetChrPos(0x10, 22180, -4000, 19220, 188)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564")
    SetChrFlags(0x14, 0x10)

    label("loc_564")

    Jump("loc_567")

    label("loc_567")

    Jump("loc_670")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_608")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 4720, 0, 28930, 225)
    OP_43(0x11, 0x0, 0x0, 0x3)
    SetChrPos(0x13, 2730, 0, 27400, 45)
    OP_43(0x13, 0x0, 0x0, 0x5)
    SetChrPos(0x12, 2610, 0, 28970, 135)
    SetChrPos(0x10, 18000, -4000, 22100, 345)
    SetChrPos(0xE, 13250, 4550, 33630, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 18030, -4000, 11140, 244)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_605")
    ClearChrFlags(0x16, 0x80)

    label("loc_605")

    Jump("loc_670")

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_670")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, 21720, 0, 30550, 163)
    OP_43(0x11, 0x0, 0x0, 0x3)
    SetChrPos(0x10, 17940, -4000, 22470, 339)
    SetChrPos(0xE, 20170, -4000, 10980, 232)
    OP_43(0xE, 0x0, 0x0, 0x4)
    SetChrPos(0xF, 13000, 4550, 33630, 191)

    label("loc_670")

    Return()

    # Function_0_49A end

    def Function_1_671(): pass

    label("Function_1_671")

    OP_16(0x2, 0xFA0, 0xFFFE5638, 0xFFFE98A0, 0x230043)
    OP_B2(0x0, 0x4, 0x80)
    OP_B2(0x0, 0x5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_69C")
    OP_71(0x15, 0x4)
    Jump("loc_724")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6D3")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    Jump("loc_724")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_724")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_B2(0x1, 0x4, 0x80)
    OP_B2(0x1, 0x5, 0x80)

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73D")

    Return()

    # Function_1_671 end

    def Function_2_73E(): pass

    label("Function_2_73E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8A5")

    label("loc_763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8A5")

    label("loc_77C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_795")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8A5")

    label("loc_795")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8A5")

    label("loc_7AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8A5")

    label("loc_7C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8A5")

    label("loc_7E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8A5")

    label("loc_7F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8A5")

    label("loc_812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8A5")

    label("loc_82B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8A5")

    label("loc_844")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8A5")

    label("loc_85D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8A5")

    label("loc_876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8A5")

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8A5")

    label("loc_8BA")

    Return()

    # Function_2_73E end

    def Function_3_8BB(): pass

    label("Function_3_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_911")

    label("loc_8C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90E")
    OP_8E(0xFE, 0x13C4, 0x0, 0x6ED2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xF96, 0x0, 0x72C4, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    Jump("loc_8C2")

    label("loc_90E")

    Jump("loc_934")

    label("loc_911")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_934")
    OP_8D(0xFE, 20530, 32090, 23220, 29410, 2000)
    Jump("loc_911")

    label("loc_934")

    Return()

    # Function_3_8BB end

    def Function_4_935(): pass

    label("Function_4_935")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_958")
    OP_8D(0xFE, 18440, 12240, 22280, 12290, 1000)
    Jump("Function_4_935")

    label("loc_958")

    Return()

    # Function_4_935 end

    def Function_5_959(): pass

    label("Function_5_959")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9ED")
    OP_8E(0xFE, 0xDC0, 0x0, 0x6E0A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x105E, 0x0, 0x6B44, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xEB0, 0x0, 0x65D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x0, 0x6770, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xAAA, 0x0, 0x6B08, 0x7D0, 0x0)
    Jump("Function_5_959")

    label("loc_9ED")

    Return()

    # Function_5_959 end

    def Function_6_9EE(): pass

    label("Function_6_9EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A11")
    OP_8D(0xFE, 14450, 14900, 22350, 7670, 1000)
    Jump("Function_6_9EE")

    label("loc_A11")

    Return()

    # Function_6_9EE end

    def Function_7_A12(): pass

    label("Function_7_A12")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B05")

    ChrTalk(    #0
        0xFE,
        (
            "We have elected to accept Ragnard's\x01",
            "goldia crystal as his apology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It still staggers me, in honesty.\x01",
            "He can create great crystals of\x01",
            "septium at will?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Dragons truly defy all logic, at least as\x01",
            "we men know it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_B05")


    ChrTalk(    #3
        0xFE,
        "Everyone, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "We have elected to accept Ragnard's\x01",
            "goldia crystal as his apology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "We will use every single mira it brings\x01",
            "us to restore the village.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BAE")

    TalkEnd(0xD)
    Return()

    # Function_7_A12 end

    def Function_8_BB2(): pass

    label("Function_8_BB2")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(    #6
        0xFE,
        "I am worried about the orbments, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "But seeing these saplings lined up\x01",
            "and growing...it feels like my fears\x01",
            "float away on the wind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "By the time these bear fruit,\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I can't say why...but I'm certain of it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D4A")

    label("loc_CCF")


    ChrTalk(    #10
        0xFE,
        (
            "Looking at these saplings makes\x01",
            "my fears float away on the wind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Keep growing, little saplings.\x01",
            "You're our hope.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_12C6")

    label("loc_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")

    ChrTalk(    #12
        0xFE,
        "So the orbments have stopped, have they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I've always said we should never rely\x01",
            "on them too much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It's not bad to use their power for some\x01",
            "things, but these days we're completely\x01",
            "enthralled by them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_EAA")

    label("loc_E37")


    ChrTalk(    #15
        0xFE,
        (
            "We're far too reliant on orbments\x01",
            "nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I think we need to value the blessings\x01",
            "of nature a bit more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAA")

    Jump("loc_12C6")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(    #17
        0xFE,
        (
            "To properly grow a tree, you first need\x01",
            "to plow the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It will be a while before these new trees\x01",
            "bear fruit, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Thankfully, I'm used to waiting.\x01",
            "I'll watch them grow patiently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1080")

    label("loc_F83")


    ChrTalk(    #20
        0xFE,
        (
            "To properly grow a tree, you first need\x01",
            "to plow the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "It will be a while before these new trees\x01",
            "bear fruit, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I'm used to waiting, though.\x01",
            "Nothing to worry about here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "We endured so much at the end of\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1080")

    Jump("loc_12C6")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_12C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_111C")

    ChrTalk(    #24
        0xFE,
        (
            "Pesca's passion for this seems genuine\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "This time, I'll be the one to bend and\x01",
            "let him use his machines, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C6")

    label("loc_111C")


    ChrTalk(    #26
        0xFE,
        "I had a long talk with Pesca yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I appreciate his passion, at the\x01",
            "very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I'm still not all that keen on this idea\x01",
            "of his to bring in a 'tractor' to till\x01",
            "the earth in place of our hands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "But, well, perhaps it's time I bend a\x01",
            "little. Tilling all that land without\x01",
            "help would be hard, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Seems I have to bow to technology for once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Just once, though!\x01",
            "This won't be a habit!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_12C6")

    TalkEnd(0x10)
    Return()

    # Function_8_BB2 end

    def Function_9_12CA(): pass

    label("Function_9_12CA")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E7")

    ChrTalk(    #32
        0xFE,
        (
            "I heard Emile complaining.\x01",
            "Apparently this orbment thing has shut\x01",
            "down all distribution too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Without any way to ship, we can't even\x01",
            "export what fruit we have, and we'll run\x01",
            "out of everyday stuff quickly out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "This, uh, might be pretty bad...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_146F")

    label("loc_13E7")


    ChrTalk(    #35
        0xFE,
        (
            "Having the ENTIRE national distribution\x01",
            "network shut down is a pretty big problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "This isn't really the time to space out...\x02",
    )

    CloseMessageWindow()

    label("loc_146F")

    Jump("loc_1A89")

    label("loc_1472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_163C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1595")

    ChrTalk(    #37
        0xFE,
        (
            "Just as I was being all satisfied that\x01",
            "we'd planted the saplings, our orbments\x01",
            "conk out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I'm just glad this happened AFTER we\x01",
            "were done with the tractor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "If it had stopped dead in the middle of\x01",
            "the field? Gray would NEVER, EVER let\x01",
            "me hear the end of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1639")

    label("loc_1595")


    ChrTalk(    #40
        0xFE,
        (
            "Just as I was being all satisfied that\x01",
            "we'd planted the saplings, our orbments\x01",
            "conk out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I'm just glad this happened AFTER we\x01",
            "were done with the tractor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1639")

    Jump("loc_1A89")

    label("loc_163C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_17EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_170C")

    ChrTalk(    #42
        0xFE,
        (
            "It may look like an empty plot now,\x01",
            "but we intend to get saplings in the\x01",
            "ground soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "We've gotten an incredible amount\x01",
            "of help from all over Liberl, so I think\x01",
            "it'll all work out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_170C")


    ChrTalk(    #44
        0xFE,
        (
            "It may look like an empty plot now,\x01",
            "but we intend to get saplings in the\x01",
            "ground soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "We've gotten a kinda overwhelming\x01",
            "amount of charity from outside the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "I think we'll manage to pull this off!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_17E9")

    Jump("loc_1A89")

    label("loc_17EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18F0")

    ChrTalk(    #47
        0xFE,
        (
            "For now, we're just going to set our sights\x01",
            "on rebuilding the orchard and focus on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Even old Gray's acknowledged the fact\x01",
            "that tractors, y'know, exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Once I get it back from the repair shop,\x01",
            "I better make good use of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A89")

    label("loc_18F0")


    ChrTalk(    #50
        0xFE,
        (
            "For now, we're just going to set our sights\x01",
            "on rebuilding the orchard and focus on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "While we were talking, I brought up my\x01",
            "tractor again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Still can't believe I got old Gray to admit\x01",
            "that a tractor might actually be useful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I kinda wonder if he understands how I feel\x01",
            "a little better, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Anyway, once I get my tractor back from the\x01",
            "repair shop, I better make good use of it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1A89")

    TalkEnd(0xF)
    Return()

    # Function_9_12CA end

    def Function_10_1A8D(): pass

    label("Function_10_1A8D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B2B")

    ChrTalk(    #55
        0xFE,
        (
            "There's a contingent of soldiers still\x01",
            "guarding the old mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "That must be a thankless job.\x01",
            "I should take them something later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C3C")

    label("loc_1B2B")


    ChrTalk(    #57
        0xFE,
        (
            "The outer signs of damage and flame may\x01",
            "be gone, but I still haven't quite managed\x01",
            "to put my feelings in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "There's a contingent of soldiers still\x01",
            "guarding the old mine, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I think it will be a long time before\x01",
            "we can really put all this behind us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1C3C")

    Jump("loc_1D59")

    label("loc_1C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CB3")

    ChrTalk(    #60
        0xFE,
        "The view here feels so much lonelier now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "We all must come together and rebuild\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D59")

    label("loc_1CB3")


    ChrTalk(    #62
        0xFE,
        (
            "We've finally cleared up the damage to\x01",
            "the orchard. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "The view here feels so much lonelier now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "We all must come together and rebuild\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1D59")

    TalkEnd(0xE)
    Return()

    # Function_10_1A8D end

    def Function_11_1D5D(): pass

    label("Function_11_1D5D")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1E47")

    ChrTalk(    #65
        0xFE,
        (
            "Awww, I've been weeding for a million-\x01",
            "bajillion years and now I'm getting sick\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I'm not gonna stop, though.\x01",
            "We gotta work really hard now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "The village is still in trouble!\x01",
            "We gotta keep it together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_1E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ED4")

    ChrTalk(    #68
        0xFE,
        (
            "Even if orbments don't work, we can\x01",
            "totally take care of the saplings!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "We gotta, so they can give us fruit\x01",
            "even quicker!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_1ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1F8E")

    ChrTalk(    #70
        0xFE,
        (
            "It's sorta funny, I never cared much\x01",
            "about the orchards before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "But now I'm gonna do my best to take\x01",
            "care of the trees!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I wanna see them with fruit soon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_200E")

    label("loc_1F8E")


    ChrTalk(    #73
        0xFE,
        (
            "We're gonna plant new saplings in\x01",
            "the orchards, like they said!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I'm gonna help out too so they give\x01",
            "us fruit soon!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_200E")

    Jump("loc_2160")

    label("loc_2011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2063")
    TurnDirection(0xFE, 0x106, 0)

    ChrTalk(    #75
        0xFE,
        "Agate! Do your best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "We're all rooting for you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2160")

    label("loc_2063")

    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #77
        0xFE,
        "Hi, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Are you gonna go beat up the dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#051FYeah, somethin' like that.\x02\x03",

            "Just you wait, kiddo.\x01",
            "I'll get this all taken care of soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Do your best! We'll be rooting for you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2160")

    TalkEnd(0x11)
    Return()

    # Function_11_1D5D end

    def Function_12_2164(): pass

    label("Function_12_2164")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F1")

    ChrTalk(    #82
        0xFE,
        "Oh, hi, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "And Mister and Miss Bracer, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#051FHey there, squirt. You doing all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_221D")

    label("loc_21F1")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #85
        0xFE,
        "Oh! Mister and Miss Bracer, hi.\x02",
    )

    CloseMessageWindow()

    label("loc_221D")


    ChrTalk(    #86
        0x101,
        "#1001FHiya, Lewey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1040FI haven't seen you in a while.\x01",
            "Have you been doing all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #88
        0xFE,
        "Uh-huh! I'm okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "We're all just helping out in the orchards.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Dad and everybody are having trouble\x01",
            "because the stuff isn't working.\x01",
            "So I'm helping!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AC")

    ChrTalk(    #91
        0x106,
        (
            "#051FYeah, you're working super hard, kiddo.\x02\x03",

            "You keep it up and help the village get\x01",
            "back on its feet, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C7")

    label("loc_23AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2449")

    ChrTalk(    #92
        0x103,
        (
            "#020FYou're a very hard worker, Lewey.\x02\x03",

            "It's going to be a lot of work, but keep\x01",
            "at it and help everyone when they need\x01",
            "it, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C7")

    label("loc_2449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C7")

    ChrTalk(    #93
        0x108,
        (
            "#070FHaha! That's the spirit!\x02\x03",

            "It will be a lot of work to repair this\x01",
            "village, but keep up the good work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C7")


    ChrTalk(    #94
        0xFE,
        "Yeah! I will!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x2094)
    Jump("loc_264E")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_25E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_255A")

    ChrTalk(    #95
        0xFE,
        "We're all helping out with the orchard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Dad's having trouble because\x01",
            "stuff stopped working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E5")

    label("loc_255A")


    ChrTalk(    #97
        0xFE,
        (
            "Even without stuff working,\x01",
            "I bet we'll be okay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "But Dad seems worried\x01",
            "about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "I wonder if something bad happened?\x02",
    )

    CloseMessageWindow()

    label("loc_25E5")

    Jump("loc_264E")

    label("loc_25E8")


    ChrTalk(    #100
        0xFE,
        "We're all helping out with the orchard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Dad's having trouble because\x01",
            "stuff stopped working.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264E")

    Jump("loc_29F4")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_29F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 5)), scpexpr(EXPR_END)), "loc_26CC")

    ChrTalk(    #102
        0xFE,
        (
            "Today we get to play a lot since we were\x01",
            "inside for so long!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Miss, you should play with us too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_29F4")

    label("loc_26CC")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #104
        0xFE,
        "Hi, Miss Bracer!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2746")

    ChrTalk(    #105
        0xFE,
        (
            "And Agate's here too!!\x01",
            "Agate's back, Agate's back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27A9")

    ChrTalk(    #106
        0x101,
        "#1018FHeeey, Lewey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        (
            "#051F'Sup, squirt?\x01",
            "You seem like you're doin' good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E5")

    label("loc_27A9")


    ChrTalk(    #108
        0x101,
        (
            "#1001FHeeey, Lewey!\x02\x03",

            "You look like you're doing great.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E5")


    ChrTalk(    #109
        0xFE,
        "Yeah, I'm okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Especially since the scary dragon is\x01",
            "gone now, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C7")

    ChrTalk(    #111
        0x106,
        (
            "#051FYeah, don't worry.\x01",
            "That kind of thing'll never happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1006FSo you play outside as much as you want,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2940")

    label("loc_28C7")


    ChrTalk(    #113
        0x101,
        (
            "#1006FYeah, the dragon will never bother people\x01",
            "again. Don't worry.\x02\x03",

            "So you play outside as much as you want,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2940")


    ChrTalk(    #114
        0xFE,
        "Okay! Oh, but.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Now that we can play outside,\x01",
            "I'll give you this book!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #116
        "\x07\x00Received #577i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x241, 1)
    OP_A2(0x10BC)
    OP_0D()

    ChrTalk(    #117
        0xFE,
        "See you later!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A4D)

    label("loc_29F4")

    TalkEnd(0x12)
    Return()

    # Function_12_2164 end

    def Function_13_29F8(): pass

    label("Function_13_29F8")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEB")

    ChrTalk(    #118
        0xFE,
        (
            "Really, our village wasn't all that\x01",
            "damaged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I heard what happened to Bose, and it\x01",
            "sounds awful! We got off light in\x01",
            "comparison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "When I think about it that way, village\x01",
            "life doesn't seem that bad at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2B94")

    label("loc_2AEB")


    ChrTalk(    #121
        0xFE,
        (
            "I heard what happened to Bose, and it\x01",
            "sounds awful! We got off light in\x01",
            "comparison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "When I think about it that way, village\x01",
            "life doesn't seem that bad at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B94")

    Jump("loc_2D31")

    label("loc_2B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2BF6")

    ChrTalk(    #123
        0xFE,
        "Vince is so motivated, for once!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "I just worry about how long it will last.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D31")

    label("loc_2BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2D31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C79")

    ChrTalk(    #125
        0xFE,
        "Vince is talking like THAT again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "He was like this the last time some\x01",
            "saplings were being planted, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D31")

    label("loc_2C79")


    ChrTalk(    #127
        0xFE,
        "Vince is talking like THAT again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "He was like this the last time some\x01",
            "saplings were being planted, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "He'll be sick of it again in three\x01",
            "days, at most. Just watch.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2D31")

    TalkEnd(0x13)
    Return()

    # Function_13_29F8 end

    def Function_14_2D35(): pass

    label("Function_14_2D35")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2DC8")

    ChrTalk(    #130
        0x16,
        "Ah, everyone. Good work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x16,
        (
            "I plan on remaining in Ravennue for a\x01",
            "little while yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x16,
        "You take care on your way back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD3")

    label("loc_2DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2E91")

    ChrTalk(    #133
        0x16,
        (
            "I must have words with Father and have\x01",
            "our family prepare our own restoration\x01",
            "fund.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x16,
        (
            "Blast all to 'business.' These people\x01",
            "shouldn't have to rely on handouts\x01",
            "to rebuild their lives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD3")

    label("loc_2E91")


    ChrTalk(    #135
        0x16,
        (
            "An allowance for buying saplings\x01",
            "and other things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x16,
        (
            "These people will need funding to rebuild\x01",
            "their orchards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x16,
        (
            "They're taking donations right now, but\x01",
            "they shouldn't be beholden to that\x01",
            "just to rebuild their lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        (
            "I must have words with Father and have\x01",
            "our family prepare our own restoration\x01",
            "fund.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2FD3")

    TalkEnd(0x16)
    Return()

    # Function_14_2D35 end

    def Function_15_2FD7(): pass

    label("Function_15_2FD7")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_2FE4")
    OP_A2(0x6)

    label("loc_2FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Sting previously\x01",               # 0
            "Set as did not meet Sting previously\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3061"),
        (1, "loc_3067"),
        (SWITCH_DEFAULT, "loc_306D"),
    )


    label("loc_3061")

    OP_A2(0x6)
    Jump("loc_306D")

    label("loc_3067")

    OP_A3(0x6)
    Jump("loc_306D")

    label("loc_306D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CE")

    ChrTalk(    #139
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_32BA")

    ChrTalk(    #140
        0x101,
        (
            "#1000FOh, hey, you're, um...\x02\x03",

            "Sting! Right? With the Bose branch.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #141
        0xFE,
        "That right. And you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "You're that recently-promoted bracer\x01",
            "that Lugran can't stop talking about.\x01",
            "And her runaway friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1011FLugran's been talking about us? Uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1041FWe kind of have been a relevant topic\x01",
            "in the news lately, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#1000FNah, it was the only thing we could do,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Ravennue seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C5")

    label("loc_32BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_331F")

    ChrTalk(    #150
        0x103,
        (
            "#020FHello, Sting.\x01",
            "It's been quite a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_3388")

    label("loc_331F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3381")

    ChrTalk(    #151
        0x106,
        "#050FSting. Haven't seen you in a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_3388")

    label("loc_3381")

    TurnDirection(0xFE, 0x101, 400)

    label("loc_3388")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343C")

    ChrTalk(    #152
        0xFE,
        "Scherazard's with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#020FNo, hardly.\x01",
            "It was the only thing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3678")

    label("loc_343C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F2")

    ChrTalk(    #156
        0xFE,
        "Agate, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x106,
        (
            "#051FHey, no need for that.\x01",
            "Only thing I could do, really.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3678")

    label("loc_34F2")


    ChrTalk(    #160
        0xFE,
        "You lot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "You're that recently-promoted bracer\x01",
            "that Lugran can't stop talking about.\x01",
            "And her runaway friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1011FLugran's been talking about us? Uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        (
            "#1041FWe kind of have been a relevant topic\x01",
            "in the news lately, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1000FNah, it was the only thing we could do,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3678")


    ChrTalk(    #167
        0xFE,
        "Ravennue seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()

    label("loc_36C5")

    OP_A2(0x1A53)
    OP_A2(0x7)
    Jump("loc_442E")

    label("loc_36CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3725")

    ChrTalk(    #169
        0xFE,
        "Ravennue seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()
    Jump("loc_442E")

    label("loc_3725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x408, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4317")
    EventBegin(0x0)
    OP_8C(0xFE, 90, 0)
    Fade(1000)
    OP_6D(2360, 500, 17530, 0)
    OP_67(0, 6610, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2780, 0, 18120, 90)
    SetChrPos(0x102, 2540, 0, 16820, 90)
    SetChrPos(0xF8, 1370, 0, 18000, 90)
    SetChrPos(0xF9, 1100, 0, 16660, 90)
    OP_0D()

    ChrTalk(    #171
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "Ah, you all.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_384D")

    ChrTalk(    #173
        0x106,
        (
            "#051FHeh, you're the same cool customer as\x01",
            "always, Sting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "Heh. Just who I am.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F8")

    label("loc_384D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A2")

    ChrTalk(    #175
        0x103,
        "#020FStill the same as always, Sting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "Heh. Just who I am.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F8")

    label("loc_38A2")


    ChrTalk(    #177
        0x101,
        "#1000FHello, Sting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#1040FThank you for your help so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "Ah, you two.\x02",
    )

    CloseMessageWindow()

    label("loc_38F8")

    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #180
        0xFE,
        (
            "Actually.\x01",
            "Sorry to ask this out of the blue, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "Mind taking a look at this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1004FHuh...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #183
        (
            "\x07\x05Sting pulled a gemstone out of his pocket.\x01",
            "It glowed...black.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #184
        0xFE,
        "It looks like a quartz of some kind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "I couldn't use it in my orbment, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        "#1015FJoshua, isn't this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#1035FYes, it's most likely an ancient Zemurian\x01",
            "quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #188
        0xFE,
        (
            "Really? I'd heard talk about them,\x01",
            "but I never expected to see one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I thought these were supposed to work\x01",
            "with these new orbments we have, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1011FI think so, but first, uh, a question.\x02\x03",

            "#1015FSting, where exactly did you FIND that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "About that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "It was around the Amberl Tower.\x01",
            "I fought this bizarre monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "It was like a living fossil, or...\x01",
            "Anyway, it was strange, put it that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "I picked this up after I defeated it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D39")

    ChrTalk(    #195
        0x101,
        "#1004FWait a minute, that sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#1042FThat sounds EXACTLY like the thing we\x01",
            "encountered atop the other tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "Ah, so you found one too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF1")

    label("loc_3D39")


    ChrTalk(    #198
        0x101,
        "#1002FYou don't think it could be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        (
            "#1042FYes, it may be a result of the shadow\x01",
            "towers manifesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "The shadow towers. Right, what you\x01",
            "encountered during the invasion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF1")


    ChrTalk(    #201
        0xFE,
        (
            "Anyway, I only ever found the one.\x01",
            "Haven't seen another since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Whatever it was, it was much, much\x01",
            "stronger than your average monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Wouldn't hurt to watch out for more\x01",
            "of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1002FYeah, no kidding.\x01",
            "Thanks for letting us know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "By the way. Not to pry, but your orbments\x01",
            "seem to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Mind fillin' me in on what's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#1000FRight, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        "#1040FLet's take it from the top.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #210
        (
            "\x07\x05Estelle and Joshua showed Sting the Zero Field Generator\x01",
            "and explained about them, and how they needed to deliver\x01",
            "the ZFGs.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #211
        0xFE,
        "So that's what's going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "Here, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #213
        "\x07\x00Received #717i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x2CD, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #214
        0x101,
        "#1004FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#1044FSting? Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "My orbment's about as useful as a rock\x01",
            "right now, so a quartz is pointless for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "But all of you are on a pretty\x01",
            "important mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "What needs to happen seems obvious to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1004FWow...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4207")

    ChrTalk(    #220
        0x106,
        (
            "#051FAh, just come out and say you want\x01",
            "to help us already, ya lug.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428D")

    label("loc_4207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4264")

    ChrTalk(    #221
        0x103,
        (
            "#027FA very cool and distant\x01",
            "way of saying you want to help us,\x01",
            "Sting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428D")

    label("loc_4264")


    ChrTalk(    #222
        0x102,
        "#1040FThank you very much for this.\x02",
    )

    CloseMessageWindow()

    label("loc_428D")


    ChrTalk(    #223
        0xFE,
        "You don't need to thank me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "You just concentrate on accomplishing\x01",
            "your mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1006FWe will! See you, Sting!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2041)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_442E")

    label("loc_4317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C1")

    ChrTalk(    #226
        0xFE,
        (
            "You just concentrate on accomplishing\x01",
            "your mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "Everyone needs to do everything they can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "If they do, we'll find a way out of\x01",
            "this mess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_442E")

    label("loc_43C1")


    ChrTalk(    #229
        0xFE,
        (
            "You just concentrate on accomplishing\x01",
            "your mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "If you do, we'll figure out a way out\x01",
            "of this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442E")

    TalkEnd(0x14)
    Return()

    # Function_15_2FD7 end

    def Function_16_4432(): pass

    label("Function_16_4432")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4604")

    ChrTalk(    #231
        0xFE,
        "Oh, my, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I was just praying for Mischa and\x01",
            "everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x106,
        (
            "#050FI see...\x02\x03",

            "Sorry I always leave you to be the one\x01",
            "to take care of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "No, not at all. She's a wonderful listener,\x01",
            "and I know she wouldn't want you sitting\x01",
            "around for her in any event!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "Besides, I have quite a lot to pray for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "I was just praying for our village, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "There's been so much strangeness in the\x01",
            "world lately...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46BF")

    label("loc_4604")


    ChrTalk(    #238
        0xFE,
        (
            "I was just offering my prayers to those\x01",
            "at Aidios' side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "That they might watch over our little\x01",
            "village of Ravennue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "There's been so much strangeness in the\x01",
            "world lately...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46BF")

    OP_A2(0xB)
    Jump("loc_4740")

    label("loc_46C5")


    ChrTalk(    #241
        0xFE,
        (
            "I was just offering my prayers to those\x01",
            "at Aidios' side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "There's been so much strangeness in the\x01",
            "world lately...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4740")

    TalkEnd(0x15)
    Return()

    # Function_16_4432 end

    def Function_17_4744(): pass

    label("Function_17_4744")

    EventBegin(0x0)
    OP_DB()
    OP_A3(0x1C01)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_475F")
    AddParty(0x5, 0xF7, 0xFF)
    AddParty(0x6, 0xF8, 0xFF)

    label("loc_475F")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x101, 33050, 8000, 37090, 0)
    OP_6D(20530, 440, 8360, 0)
    OP_67(0, 13770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(326000, 0)
    OP_6E(335, 0)
    SetChrFlags(0xD, 0x80)
    FadeToBright(1000, 0)

    def lambda_47D5():
        OP_6D(21820, 440, 6800, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47D5)
    OP_67(0, 7790, -10000, 7000)
    Fade(500)
    OP_6D(26270, 5270, 52540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 32950, 8000, 37000, 180)
    SetChrPos(0x106, 26650, 5360, 52720, 0)
    SetChrPos(0x107, 25890, 5210, 52420, 0)
    ClearChrFlags(0x106, 0x80)
    ClearChrFlags(0x107, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x107, 17)
    SetChrPos(0xA, 32990, 8000, 35450, 0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 15)
    OP_43(0x106, 0x1, 0x0, 0x15)
    OP_43(0x107, 0x1, 0x0, 0x16)
    OP_6A(0x17)
    OP_43(0x17, 0x2, 0x0, 0x17)
    WaitChrThread(0x107, 0x1)
    SetChrSubChip(0x107, 0)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6A(0xFF)
    OP_44(0x17, 0x2)
    OP_DC()

    ChrTalk(    #243
        0x107,
        "#064F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x106,
        "#052F#6PYou...\x02",
    )

    CloseMessageWindow()

    def lambda_4921():
        OP_6D(32800, 8000, 38500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4921)

    def lambda_4939():
        OP_6C(145000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4939)
    Sleep(4000)
    SetChrPos(0x106, 33360, 8000, 49000, 180)
    SetChrPos(0x107, 32439, 8000, 49000, 180)

    def lambda_4970():
        OP_8E(0xFE, 0x8250, 0x1F40, 0x9B96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4970)
    Sleep(200)

    def lambda_4990():
        OP_8E(0xFE, 0x7EB7, 0x1F40, 0x9C5E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4990)
    Sleep(2000)

    ChrTalk(    #245
        0x9,
        "#163F#6PYou two...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    WaitChrThread(0x107, 0x1)
    SetChrSubChip(0x107, 0)

    ChrTalk(    #246
        0x106,
        (
            "#051F#6PNever thought we'd meet here\x01",
            "of all places.\x02\x03",

            "What brings you out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "#163F#4POh... A little whimsy, I suppose.\x02\x03",

            "#165FYou're here to make an offering to your sister,\x01",
            "correct? Allow me to pardon myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x106,
        (
            "#551F#6PHey, hey, I didn't say you were in the\x01",
            "way or anything.\x02\x03",

            "#050FAnd those flowers... They yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        (
            "#166F#4PYes, although...\x02\x03",

            "If I'd known the flowers would have company,\x01",
            "I would have picked a different color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#051F#6PI figured there was someone other than me\x01",
            "settin' some flowers down here every year.\x02\x03",

            "Didn't think it was you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        (
            "#163F#4PWas it?\x02\x03",

            "An old man like me can hardly remember\x01",
            "the things he's done over the years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x106,
        "#051F#6PHeh, says the army general.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x107,
        (
            "#061F#5PHeehee...!\x02\x03",

            "#560FAgate, could I place my flowers, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x9,
        "#161F#4POh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(400)

    ChrTalk(    #255
        0x106,
        "#051F#6PYeah, go on.\x02",
    )

    CloseMessageWindow()

    def lambda_4D21():
        OP_6D(33700, 8000, 36340, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D21)
    OP_43(0x9, 0x1, 0x0, 0x18)

    def lambda_4D40():
        OP_8E(0xFE, 0x8066, 0x1F40, 0x8DFE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4D40)
    Sleep(500)
    OP_8C(0x106, 180, 400)
    Sleep(500)

    def lambda_4D6C():
        OP_8E(0xFE, 0x82B4, 0x1F40, 0x91B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4D6C)
    WaitChrThread(0x107, 0x1)
    SetChrSubChip(0x107, 0)
    WaitChrThread(0x106, 0x1)
    Sleep(500)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrFlags(0x107, 0x2)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 10)
    OP_0D()
    OP_99(0x107, 0x0, 0x2, 0x5DC)
    SetChrPos(0xB, 32689, 8000, 35750, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 10)
    SetChrSubChip(0xB, 15)
    OP_0D()
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_0D()

    def lambda_4E0D():
        OP_8F(0xFE, 0x7F9E, 0x1F40, 0x91B4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4E0D)
    WaitChrThread(0x107, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #256
        "\x07\x05Agate and Tita stood for a moment in silent prayer.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #257
        0x106,
        "#053F#6P*sigh*...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(500)

    ChrTalk(    #258
        0x106,
        (
            "#050F#6PSorry 'bout all this, Tita. Thanks for\x01",
            "coming out here with me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)
    Sleep(500)

    ChrTalk(    #259
        0x107,
        (
            "#066F#2PNo, I wanted to give my respects to\x01",
            "Mischa, too.\x02\x03",

            "So...thank you, Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x106,
        (
            "#051F#6PWhoa, there, that's enough of that.\x01",
            "I should be thanking you.\x02\x03",

            "And hey, I promised I'd let you meet\x01",
            "her once work had calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x107,
        "#067F#2PI guess you did, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "#163F#6PHaha...\x02\x03",

            "#165FThe dragon apparently said as much\x01",
            "already, but you've certainly changed,\x01",
            "Mr. Crosner.\x02\x03",

            "You feel much calmer somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x9, 400)
    Sleep(500)

    ChrTalk(    #263
        0x106,
        (
            "#551F#6PAh, cut that out. I've still got a ways\x01",
            "to go.\x02\x03",

            "#051FBut now I'm ready to actually do\x01",
            "something about it.\x02\x03",

            "Everything really does start here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x9,
        (
            "#163F#6PHmm...\x02\x03",

            "#160FThe downsides of the army which\x01",
            "you spoke of...\x02\x03",

            "Having thought them over again,\x01",
            "I believe your argument had some\x01",
            "merit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x106,
        (
            "#552F#6PNah, that was just...you know, blowin'\x01",
            "off some steam at people who didn't\x01",
            "deserve it.\x02\x03",

            "It's not like I think the army did anything\x01",
            "wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        (
            "#163F#6PNo. Listen closely, now.\x02\x03",

            "#160FIf there's anything I've learned from this,\x01",
            "it's that we need both bracers and the army\x01",
            "to properly function as a society.\x02\x03",

            "The organization and hierarchy of the army is\x01",
            "certainly useful, but there are times when the\x01",
            "bracers' swift actions lead to better results.\x02\x03",

            "Without both, we could never have stopped\x01",
            "this crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x106,
        (
            "#050F#6P...True enough.\x02\x03",

            "It's thanks to your plan that we\x01",
            "found the dragon at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x9,
        (
            "#166F#6PAlan Richard had the right of it, in a way.\x02\x03",

            "The flow of information since orbments were\x01",
            "developed has increased rapidly, to a point\x01",
            "where no single group can capably manage it.\x02\x03",

            "The only way for us to process it all is to\x01",
            "expand our numbers and allocate the work\x01",
            "to progressively fragmented subdivisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x106,
        (
            "#555F#6PThe army's sure got that down.\x02\x03",

            "You've got the border garrison,\x01",
            "airship crews, the Royal Guard,\x01",
            "even the Intelligence Division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x9,
        (
            "#163F#6PIndeed.\x02\x03",

            "#160FIt was a necessary evolution to keep\x01",
            "pace with the times.\x02\x03",

            "Even if a multitude of issues have fallen\x01",
            "through the cracks in the process...\x02\x03",

            "For us, there's no turning back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x106,
        "#552F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #272
        0x9,
        (
            "#163F#6PThat being said, you bracers are free to\x01",
            "do as you will.\x02\x03",

            "#165FWe as the army are limited, but you can\x01",
            "- and by all accounts should--protect the\x01",
            "people to the utmost of your abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x106,
        "#052F#6PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x9,
        (
            "#163F#6PThat may cause our two factions to clash\x01",
            "every so often, but we'll just as often come\x01",
            "in support for one another.\x02\x03",

            "Whatever the situation may call for, we've\x01",
            "found a way to compensate for our flaws\x01",
            "and keep from straying down the wrong path.\x02\x03",

            "#160FPersonally, I wouldn't have it any other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x106,
        (
            "#051F#6PHeh... Kinda got a point there.\x02\x03",

            "All right, if it makes you happy,\x01",
            "we'll keep buttin' in on your business\x01",
            "at every possible turn, General.\x02\x03",

            "Hope you're ready.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #276
        0x9,
        (
            "#165F#6PI could say the same to you.\x02\x03",

            "Keep in mind not to do anything\x01",
            "TOO reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x107,
        "#061F#2PHeehee...!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 32780, 8000, 45130, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #278
        0x8,
        "Young Man's Voice",
        "#2PHeh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #279
        0x8,
        "Young Man's Voice",
        (
            "#2PPardon me for disturbing such a\x01",
            "peaceful moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(32100, 8000, 40770, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(3680, 0)
    OP_6C(315000, 0)
    OP_6E(275, 0)

    def lambda_5B41():

        label("loc_5B41")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5B41")

    QueueWorkItem2(0x106, 1, lambda_5B41)
    Sleep(50)

    def lambda_5B57():

        label("loc_5B57")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5B57")

    QueueWorkItem2(0x9, 1, lambda_5B57)
    Sleep(50)

    def lambda_5B6D():

        label("loc_5B6D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5B6D")

    QueueWorkItem2(0x107, 1, lambda_5B6D)
    OP_0D()
    Sleep(500)

    ChrTalk(    #280
        0x106,
        "#054F#5P#3SYOU!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x107,
        "#065F#5POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x9,
        "#160F#5PYou are...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x72)
    Sleep(800)

    ChrTalk(    #283
        0x8,
        (
            "#124F#4PI believe this is the first time we've met,\x01",
            "General Morgan.\x02\x03",

            "#120FI am an Enforcer of Ouroboros. You may\x01",
            "call me Leonhardt.\x02\x03",

            "It's a pleasure to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #284
        0x9,
        "#161F#5P#3SWhat did you--\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 8)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_5CD8():
        OP_96(0xFE, 0x8098, 0x1F40, 0x9524, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5CD8)
    Sleep(100)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5D0D():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xFFFFFF38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5D0D)
    WaitChrThread(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 7)
    Sleep(500)

    ChrTalk(    #285
        0x106,
        (
            "#057F#5PYou...\x02\x03",

            "What the hell are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x8,
        (
            "#121F#4PThis is a place where the dead rest.\x01",
            "There's only one proper thing to do.\x02\x03",

            "Or do you intend to reenact our last\x01",
            "meeting here, in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x106,
        "#555F#5PTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x107,
        "#063F#5PAgate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x106,
        "#053F#5PI know.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 65535)
    OP_0D()
    Sleep(1000)

    def lambda_5E70():
        OP_8F(0xFE, 0x81B0, 0x1F40, 0x8E08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5E70)
    Sleep(1500)

    def lambda_5E90():
        OP_91(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5E90)
    Sleep(200)

    def lambda_5EB0():
        OP_91(0xFE, 0xFFFFFBB4, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5EB0)
    Sleep(500)
    Fade(500)
    OP_6D(33220, 8000, 35580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x2, 0x5DC)
    SetChrPos(0xC, 33290, 8000, 35750, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 10)
    SetChrSubChip(0xC, 15)
    OP_0D()
    Sleep(500)
    Fade(500)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 18)
    OP_0D()

    def lambda_5F84():
        OP_8F(0xFE, 0x81CE, 0x1F40, 0x9024, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5F84)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #290
        "\x07\x05Loewe offered silent prayer.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #291
        0x8,
        "#124F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x9,
        (
            "#160F#6PLeonhardt... 'Loewe the Bladelord,' yes?\x02\x03",

            "I, too, do not wish to disturb the dead...\x02\x03",

            "But I have a question I would ask of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x8,
        "#124F#2PBy all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x9,
        (
            "#163F#6PEarlier, it seemed as though you kept the\x01",
            "dragon from causing greater damage than\x01",
            "it otherwise would have.\x02\x03",

            "And here you are now, offering prayers\x01",
            "for the departed.\x02\x03",

            "#160FSo why? Why would a man such as you\x01",
            "bring chaos to our land?\x02\x03",

            "What sort of demons in your soul drive\x01",
            "you to such acts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x8,
        (
            "#124F#2P...\x02\x03",

            "#121FThe only reason I reined in the\x01",
            "dragon's rampage was to conduct\x01",
            "a proper experiment.\x02\x03",

            "I had no goal beyond that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x9,
        "#160F#6PSurely--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x8,
        (
            "#124F#2PGeneral. I simply act as the hand of the\x01",
            "society, as it orders.\x02\x03",

            "I am bound to the will of the society and\x01",
            "no other.\x02\x03",

            "#123FDo not think to compare yourself to me.\x01",
            "You, who are bound by force to silence\x01",
            "over Hamel.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #298
        0x9,
        "#161F#6P#4S...!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #299
        0x106,
        (
            "#052F#2PHamel? What's that place got to do\x01",
            "with anything?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #300
        0x8,
        (
            "#125F#5PIn any case... Agate Crosner.\x02\x03",

            "#122FYour resolve has clearly hardened, but\x01",
            "that means nothing if you don't have the\x01",
            "strength to support it.\x02\x03",

            "Should you fail to measure up the next\x01",
            "time we meet, more than your sword will\x01",
            "end up broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x106,
        (
            "#051F#2POh, don't you worry about me.\x02\x03",

            "And the same goes for you, too, pal.\x01",
            "Don't think you can just strut around\x01",
            "all confident forever.\x02\x03",

            "I'll catch up to you real quick. Be ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x8,
        "#125F#5PHeh... I look forward to it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    def lambda_65E1():
        OP_6D(33420, 8000, 38810, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_65E1)

    def lambda_65F9():
        OP_67(0, 8500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_65F9)

    def lambda_6611():
        OP_8E(0xFE, 0x7E5E, 0x1F40, 0xC56C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6611)
    Sleep(1600)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    SetChrFlags(0x8, 0x80)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x9, 0x1)

    def lambda_6651():
        OP_6D(33100, 8000, 36700, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6651)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    ChrTalk(    #303
        0x107,
        (
            "#063F#2P...Mr. Leonhardt's eyes looked so lonely.\x02\x03",

            "He tries to be cold, but he was so sad\x01",
            "when he was praying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x106,
        "#057F#2P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x9, 400)

    def lambda_6704():
        OP_6D(33800, 8000, 36470, 1000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_6704)
    OP_8F(0x106, 0x8138, 0x1F40, 0x9178, 0x5DC, 0x0)

    def lambda_6730():

        label("loc_6730")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_6730")

    QueueWorkItem2(0x107, 1, lambda_6730)
    WaitChrThread(0x106, 0x2)
    Sleep(500)

    ChrTalk(    #305
        0x106,
        (
            "#050F#6PHey. General.\x02\x03",

            "Hamel was a village just across the\x01",
            "border in Erebonia, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 315, 400)

    ChrTalk(    #306
        0x9,
        "#161F#6PYou know the name, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x106,
        (
            "#053F#6PUs Ravennue folks occasionally had\x01",
            "contact with 'em before the war.\x02\x03",

            "#555FNot anymore, though. Not sure why.\x02\x03",

            "Why would he bring that name up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x9,
        (
            "#163F#6P...\x02\x03",

            "#166FI'm afraid I am not free to speak on the\x01",
            "subject.\x02\x03",

            "It connects to matters of international\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x106,
        "#052F#6PTo what...?!\x02",
    )

    CloseMessageWindow()

    def lambda_6907():
        OP_6D(34070, 8000, 34770, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6907)

    def lambda_691F():
        OP_67(0, 6330, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_691F)

    def lambda_6937():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_6937)

    def lambda_6947():
        OP_6C(157000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6947)
    Sleep(500)
    OP_8C(0x9, 180, 400)

    def lambda_6963():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_6963)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #310
        0x9,
        (
            "#166F#6PI can, however, say this:\x02\x03",

            "If my suspicions about that man are true...\x02\x03",

            "#163F...then that man, Loewe, has stared into\x01",
            "the pits of Gehenna with his two own eyes.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400B2, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1A82)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x127), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0x12, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AAE")
    ShowSaveMenu()

    label("loc_6AAE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0xBB8)
    OP_21()
    OP_A3(0x1A82)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4744 end

    def Function_18_6AEA(): pass

    label("Function_18_6AEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B36")
    OP_8E(0xFE, 0x6AFE, 0xFFFFF060, 0x2486, 0x4B0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(800)
    OP_8E(0xFE, 0x5F00, 0xFFFFF060, 0x186A, 0x4B0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(800)
    Jump("Function_18_6AEA")

    label("loc_6B36")

    Return()

    # Function_18_6AEA end

    def Function_19_6B37(): pass

    label("Function_19_6B37")

    Sleep(500)

    label("loc_6B3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B88")
    OP_8E(0xFE, 0x34F8, 0xFFFFF060, 0x2EAE, 0x5DC, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x33D6, 0xFFFFF060, 0x41AA, 0x5DC, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    Jump("loc_6B3C")

    label("loc_6B88")

    Return()

    # Function_19_6B37 end

    def Function_20_6B89(): pass

    label("Function_20_6B89")

    Sleep(250)

    label("loc_6B8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BCC")
    OP_8E(0xFE, 0x53D4, 0xFFFFF060, 0x2396, 0x578, 0x0)
    Sleep(900)
    OP_8E(0xFE, 0x54CE, 0xFFFFF060, 0x35A2, 0x578, 0x0)
    Sleep(900)
    Jump("loc_6B8E")

    label("loc_6BCC")

    Return()

    # Function_20_6B89 end

    def Function_21_6BCD(): pass

    label("Function_21_6BCD")

    OP_8E(0xFE, 0x681A, 0x1F40, 0xE506, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x1F40, 0xE506, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x1F40, 0xD37C, 0x7D0, 0x0)
    Return()

    # Function_21_6BCD end

    def Function_22_6C0A(): pass

    label("Function_22_6C0A")

    OP_8E(0xFE, 0x6522, 0x1F40, 0xE5CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8A, 0x1F40, 0xE5CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8A, 0x1F40, 0xD37C, 0x7D0, 0x0)
    Return()

    # Function_22_6C0A end

    def Function_23_6C47(): pass

    label("Function_23_6C47")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C93")
    OP_51(0x17, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_23_6C47")

    label("loc_6C93")

    Return()

    # Function_23_6C47 end

    def Function_24_6C94(): pass

    label("Function_24_6C94")

    OP_8E(0xFE, 0x8660, 0x1F40, 0x8D5E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_24_6C94 end

    def Function_25_6CB0(): pass

    label("Function_25_6CB0")

    ClearMapFlags(0x2000000)
    Return()

    # Function_25_6CB0 end

    def Function_26_6CB6(): pass

    label("Function_26_6CB6")

    EventBegin(0x1)

    ChrTalk(    #311
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_6CE2():
        OP_6D(35190, -3850, 5430, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6CE2)

    def lambda_6CFA():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6CFA)

    def lambda_6D0A():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_6D0A)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #312
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB0")
    OP_C0(0xE, 0xA, 0x8976, 0xFFFFF0F6, 0x21D4, 0xB4, 0x88C2, 0xFFFFEF98, 0x1446)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_6DBF")

    label("loc_6DB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DBF")
    EventEnd(0x1)

    label("loc_6DBF")

    Return()

    # Function_26_6CB6 end

    def Function_27_6DC0(): pass

    label("Function_27_6DC0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #313
        (
            "\x07\x05The six good souls lost in the fires of war sleep here.\x01",
            "《Septian Calendar 1192》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #314
        (
            "\x07\x05Lief, Abel, Nicole, Vim, Ileana, Mischa.\x01",
            "May you rest peacefully by the Goddess' side.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_6DC0 end

    def Function_28_6EAD(): pass

    label("Function_28_6EAD")

    SetPlaceName(0x2E)
    Return()

    # Function_28_6EAD end

    def Function_29_6EB1(): pass

    label("Function_29_6EB1")

    SetPlaceName(0x2D)
    Return()

    # Function_29_6EB1 end

    def Function_30_6EB5(): pass

    label("Function_30_6EB5")

    SetPlaceName(0x2F)
    Return()

    # Function_30_6EB5 end

    SaveToFile()

Try(main)
