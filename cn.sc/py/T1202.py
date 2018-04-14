from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '剑帝莱维',                             # 9
        '摩尔根将军',                           # 10
        '捧花',                                 # 11
        '捧花',                                 # 12
        '捧花',                                 # 13
        '莱森村长',                             # 14
        '菲戈',                                 # 15
        '贝斯卡',                               # 16
        '库赖老人',                             # 17
        '巴德斯',                               # 18
        '鲁伊',                                 # 19
        '弗兰',                                 # 20
        '斯丁克',                               # 21
        '碧尔奈婆婆',                           # 22
        '米拉诺',                               # 23
        '目标用照相机',                         # 24
        '拉文努山道方向',                       # 25
        '拉文努废坑方向',                       # 26
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
        "Function_8_B0A",          # 08, 8
        "Function_9_FAF",          # 09, 9
        "Function_10_13E3",        # 0A, 10
        "Function_11_15A9",        # 0B, 11
        "Function_12_187C",        # 0C, 12
        "Function_13_1EB5",        # 0D, 13
        "Function_14_20A3",        # 0E, 14
        "Function_15_222C",        # 0F, 15
        "Function_16_29A4",        # 10, 16
        "Function_17_2B97",        # 11, 17
        "Function_18_464C",        # 12, 18
        "Function_19_4699",        # 13, 19
        "Function_20_46EB",        # 14, 20
        "Function_21_472F",        # 15, 21
        "Function_22_476C",        # 16, 22
        "Function_23_47A9",        # 17, 23
        "Function_24_47F6",        # 18, 24
        "Function_25_4812",        # 19, 25
        "Function_26_4818",        # 1A, 26
        "Function_27_4903",        # 1B, 27
        "Function_28_49CF",        # 1C, 28
        "Function_29_49D3",        # 1D, 29
        "Function_30_49D7",        # 1E, 30
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #0
        0xFE,
        (
            "我已经收下了\x01",
            "金耀石结晶……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "不过，七耀石的结晶\x01",
            "竟能以自己的力量生出……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "龙这样的生物真是\x01",
            "超越了人的常识范围。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B06")

    label("loc_AA3")


    ChrTalk(    #3
        0xFE,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "我已经收下了\x01",
            "金耀石结晶……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "作为村子的修复资金，\x01",
            "我会小心使用的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B06")

    TalkEnd(0xD)
    Return()

    # Function_7_A12 end

    def Function_8_B0A(): pass

    label("Function_8_B0A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(    #6
        0xFE,
        (
            "导力器的事也\x01",
            "略有些担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "看着这些小树苗，\x01",
            "不安的心情也烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "等它们结出果实的时候\x01",
            "所有事情都能顺利平息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "……虽不知道为什么，\x01",
            "就是这么觉得。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_C26")

    label("loc_BCE")


    ChrTalk(    #10
        0xFE,
        (
            "看着这些小树苗，\x01",
            "不安的心情也烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "真希望它们能就这样继续\x01",
            "茁壮成长呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C26")

    Jump("loc_FAB")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB7")

    ChrTalk(    #12
        0xFE,
        (
            "呼，看来导力器\x01",
            "好像动不了了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "所以说太依赖那种东西\x01",
            "是不行的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "稍微用一下是可以，\x01",
            "但近来实在太依赖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D07")

    label("loc_CB7")


    ChrTalk(    #15
        0xFE,
        (
            "近来不管做什么\x01",
            "都太依赖导力器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "对大自然的恩惠\x01",
            "应该更加重视才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D07")

    Jump("loc_FAB")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DAC")

    ChrTalk(    #17
        0xFE,
        (
            "为了培育树苗，\x01",
            "首先不耕地怎么行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "新栽的树要结果实\x01",
            "当然需要一些时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "幸好我已经习惯等待了。\x01",
            "只要耐心地注视着它们成长就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DAC")


    ChrTalk(    #20
        0xFE,
        (
            "为了培育树苗，\x01",
            "首先不耕地怎么行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "当然到结果实\x01",
            "还要花很长时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "不过，没什么好担心的。\x01",
            "我早就习惯等待了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "百日战役之后\x01",
            "我们也忍耐了很久呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_E53")

    Jump("loc_FAB")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EBB")

    ChrTalk(    #24
        0xFE,
        (
            "贝斯卡对果树园的关爱\x01",
            "可是真心的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "这次对那些机械的力量\x01",
            "也不得不认可啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAB")

    label("loc_EBB")


    ChrTalk(    #26
        0xFE,
        (
            "昨天，和贝斯卡那家伙\x01",
            "谈过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "知道了贝斯卡那家伙\x01",
            "是真心爱着果树园的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "投入机械的想法\x01",
            "虽然之前还不能接受……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "但要是没有拖拉机\x01",
            "在这里耕作也够辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "所以，这次也不得不\x01",
            "认可机械的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "当然，只是这次而已。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_FAB")

    TalkEnd(0x10)
    Return()

    # Function_8_B0A end

    def Function_9_FAF(): pass

    label("Function_9_FAF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105B")

    ChrTalk(    #32
        0xFE,
        (
            "埃米尔那家伙在发牢骚，\x01",
            "因为流通路线好像也停了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "没有运输手段\x01",
            "我们的水果就不能出货，\x01",
            "日用品也很快就会短缺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "果，果然\x01",
            "不太妙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_109F")

    label("loc_105B")


    ChrTalk(    #35
        0xFE,
        (
            "运输路线停止了，\x01",
            "果然问题严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "可不是\x01",
            "该发呆的时候……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109F")

    Jump("loc_13DF")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1144")

    ChrTalk(    #37
        0xFE,
        (
            "刚还在想终于种好了树苗，\x01",
            "但导力器又出麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "拖拉机停止运做\x01",
            "是在帮忙做完耕种之后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "如果在工作中停止了，\x01",
            "我可就颜面扫地了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11A4")

    label("loc_1144")


    ChrTalk(    #40
        0xFE,
        (
            "刚还在想终于种好了树苗，\x01",
            "但导力器又出麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "拖拉机停止运做\x01",
            "是在帮忙做完耕种之后。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A4")

    Jump("loc_13DF")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1214")

    ChrTalk(    #42
        0xFE,
        (
            "虽然现在还是空地，\x01",
            "不过马上打算栽培树苗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "似乎捐款也募集齐了，\x01",
            "总算感觉能行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1282")

    label("loc_1214")


    ChrTalk(    #44
        0xFE,
        (
            "虽然现在还是空地，\x01",
            "不过马上打算栽培树苗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "捐款似乎\x01",
            "也募集了不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "总算感觉\x01",
            "感觉能行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1282")

    Jump("loc_13DF")

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_13DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1311")

    ChrTalk(    #47
        0xFE,
        (
            "总之为了果树园的复活，\x01",
            "我也来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "库赖爷爷似乎也\x01",
            "认同了拖拉机的有效性……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "修理回来之后\x01",
            "就得积极使用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DF")

    label("loc_1311")


    ChrTalk(    #50
        0xFE,
        (
            "总之为了果树园的复活，\x01",
            "我也来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "谈话中还说到了\x01",
            "我买的拖拉机……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "意外的是库赖爷爷\x01",
            "竟然也稍微认同其的有效性了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "嗯～是不是稍微\x01",
            "理解我的想法了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "修理回来之后\x01",
            "就得积极使用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_13DF")

    TalkEnd(0xF)
    Return()

    # Function_9_FAF end

    def Function_10_13E3(): pass

    label("Function_10_13E3")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_14D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1441")

    ChrTalk(    #55
        0xFE,
        (
            "里面的废坑还留有\x01",
            "士兵在警卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "真是辛苦啊。\x01",
            "看来得去慰问一下呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_1441")


    ChrTalk(    #57
        0xFE,
        (
            "火灾后的痕迹虽然收拾过，\x01",
            "但心情还得好好整理整理啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "里面的废坑还留有\x01",
            "士兵在警卫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "看来想一会半会儿\x01",
            "忘记那个事件是不可能的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_14D1")

    Jump("loc_15A5")

    label("loc_14D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_15A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1531")

    ChrTalk(    #60
        0xFE,
        (
            "这里的景色\x01",
            "变得相当凄凉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "必须和大家齐心协力\x01",
            "努力重建才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A5")

    label("loc_1531")


    ChrTalk(    #62
        0xFE,
        (
            "总算把果树园\x01",
            "收拾得差不多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "这里的景色\x01",
            "变得相当凄凉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "必须和大家齐心协力\x01",
            "努力重建才行啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_15A5")

    TalkEnd(0xE)
    Return()

    # Function_10_13E3 end

    def Function_11_15A9(): pass

    label("Function_11_15A9")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1627")

    ChrTalk(    #65
        0xFE,
        (
            "啊～啊，一直除草\x01",
            "到底是烦人啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "不过，现在是\x01",
            "要努力的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "村子情况严峻。\x01",
            "我们不振作可不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1878")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1697")

    ChrTalk(    #68
        0xFE,
        (
            "即使不能开动导力器…\x01",
            "但是照顾树苗还是能行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "为了让它们早点开花结果，\x01",
            "可要努力照顾才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1878")

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_176D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1719")

    ChrTalk(    #70
        0xFE,
        (
            "我以前都很讨厌\x01",
            "做果园的活……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "不过，从今以后\x01",
            "打算努力照顾它们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "因为想早点\x01",
            "看到它们开花结果嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176A")

    label("loc_1719")


    ChrTalk(    #73
        0xFE,
        (
            "听说果树园\x01",
            "在种新树苗啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "为了让它们早点开花结果\x01",
            "我也要努力帮忙啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_176A")

    Jump("loc_1878")

    label("loc_176D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1878")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17B8")
    TurnDirection(0xFE, 0x106, 0)

    ChrTalk(    #75
        0xFE,
        (
            "阿加特哥哥！\x01",
            "要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "我也会支持你的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1878")

    label("loc_17B8")

    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #77
        0xFE,
        "啊，阿加特哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "难道\x01",
            "要去打龙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#051F啊啊，是这个打算。\x02\x03",

            "嗯，放心等着吧。\x01",
            "马上解决掉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "不愧是哥哥！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "加油啊！\x01",
            "我也会支持你的！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1878")

    TalkEnd(0x11)
    Return()

    # Function_11_15A9 end

    def Function_12_187C(): pass

    label("Function_12_187C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18EF")

    ChrTalk(    #82
        0xFE,
        "咦，阿加特哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "而且……\x01",
            "还有姐姐和哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#051F哟，这不是鲁伊吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_190F")

    label("loc_18EF")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #85
        0xFE,
        (
            "啊……\x01",
            "姐姐和哥哥。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190F")


    ChrTalk(    #86
        0x101,
        "#1001F呀嗬～鲁伊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1040F好久不见了呢。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #88
        0xFE,
        "嗯、嗯！我很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "现在，大家\x01",
            "都在果树园里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "因为导力器不能动了，\x01",
            "爸爸他们似乎非常忙……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A08")

    ChrTalk(    #91
        0x106,
        (
            "#051F喔，很努力嘛。\x02\x03",

            "我们也要多多支持\x01",
            "村子里的人们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_1A08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(    #92
        0x103,
        (
            "#020F呵呵，看来很努力呢。\x02\x03",

            "虽然暂时会辛苦一点，\x01",
            "但大家要齐心协力撑过去哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABF")

    label("loc_1A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABF")

    ChrTalk(    #93
        0x108,
        (
            "#070F哈哈，真孝顺啊。\x02\x03",

            "虽然暂时会辛苦一点，\x01",
            "不过就努力点撑过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABF")


    ChrTalk(    #94
        0xFE,
        "嗯、嗯！明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x2094)
    Jump("loc_1BFE")

    label("loc_1ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #95
        0xFE,
        (
            "大家都在\x01",
            "都在果树园里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "因为导力器不能动了，\x01",
            "爸爸他们好像很忙嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1B3F")


    ChrTalk(    #97
        0xFE,
        (
            "即使没有导力器，\x01",
            "我们村子也不要紧哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "但是，爸爸他们\x01",
            "好像在担心什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "是不是有什么困难呢？\x02",
    )

    CloseMessageWindow()

    label("loc_1BAB")

    Jump("loc_1BFE")

    label("loc_1BAE")


    ChrTalk(    #100
        0xFE,
        (
            "大家都在\x01",
            "都在果树园里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "因为导力器不能动了，\x01",
            "爸爸他们好像很忙嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFE")

    Jump("loc_1EB1")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 5)), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(    #102
        0xFE,
        (
            "之前一直待在家里，\x01",
            "今天要玩个痛快！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "姐姐你们\x01",
            "来一起玩吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB1")

    label("loc_1C56")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #104
        0xFE,
        "啊～姐姐！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(    #105
        0xFE,
        "还有阿加特哥哥！！\x02",
    )

    CloseMessageWindow()

    label("loc_1CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEE")

    ChrTalk(    #106
        0x101,
        "#1018F嗨～鲁伊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        "#051F哟，看来挺精神嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1F")

    label("loc_1CEE")


    ChrTalk(    #108
        0x101,
        (
            "#1001F嗨～鲁伊！\x02\x03",

            "太好了……\x01",
            "看来挺精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1F")


    ChrTalk(    #109
        0xFE,
        "嗯，很好哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "因为那个可怕的龙\x01",
            "已经不在了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC2")

    ChrTalk(    #111
        0x106,
        (
            "#051F啊啊，那种事\x01",
            "绝对不会再发生第二次了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1006F所以，出门尽情\x01",
            "玩耍也没问题哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_1DC2")


    ChrTalk(    #113
        0x101,
        (
            "#1006F嗯，那种事\x01",
            "不会再发生第二次了。\x02\x03",

            "所以，出门尽情\x01",
            "玩耍也没问题哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0E")


    ChrTalk(    #114
        0xFE,
        "嗯！啊，对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "因为能出去玩了，\x01",
            "这本书就给姐姐吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #116
        "\x07\x00得到了\x1F\x41\x02\x07\x00。\x02",
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
        "那么，姐姐再见！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A4D)

    label("loc_1EB1")

    TalkEnd(0x12)
    Return()

    # Function_12_187C end

    def Function_13_1EB5(): pass

    label("Function_13_1EB5")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1F8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")

    ChrTalk(    #118
        0xFE,
        (
            "我们的村子\x01",
            "意外的平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "不过柏斯那样的大城市，\x01",
            "一定很严重吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "这样看来\x01",
            "待在乡下倒也不坏。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1F88")

    label("loc_1F3C")


    ChrTalk(    #121
        0xFE,
        (
            "不过柏斯那样的大城市，\x01",
            "一定很严重吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "这样看来\x01",
            "待在乡下倒也不坏。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F88")

    Jump("loc_209F")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FD6")

    ChrTalk(    #123
        0xFE,
        (
            "巴德斯那家伙\x01",
            "意外的有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "不过，不知道会持续多久？\x02",
    )

    CloseMessageWindow()
    Jump("loc_209F")

    label("loc_1FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_209F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2031")

    ChrTalk(    #125
        0xFE,
        (
            "巴德斯真是的，\x01",
            "又说那种话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "之前种树苗的时候\x01",
            "也说过同样的话吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_209F")

    label("loc_2031")


    ChrTalk(    #127
        0xFE,
        (
            "巴德斯真是的，\x01",
            "又说那种话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "之前种树苗的时候\x01",
            "也说过同样的话吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "反正做三天\x01",
            "又会开始厌烦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_209F")

    TalkEnd(0x13)
    Return()

    # Function_13_1EB5 end

    def Function_14_20A3(): pass

    label("Function_14_20A3")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2113")

    ChrTalk(    #130
        0x16,
        (
            "啊，是你们。\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x16,
        (
            "我打算\x01",
            "继续视察一下村子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x16,
        (
            "你们回去的时候\x01",
            "也要当心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_217B")

    ChrTalk(    #133
        0x16,
        (
            "和丈夫商量了一下，\x01",
            "我们也得准备一些重建资金才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x16,
        (
            "不能从一开始\x01",
            "就完全依赖捐款啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_217B")


    ChrTalk(    #135
        0x16,
        (
            "买树苗也\x01",
            "需要很多费用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x16,
        (
            "果树园的重建\x01",
            "怎么说都需要资金啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x16,
        (
            "虽然有募集捐款，\x01",
            "但可不能完全靠那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x16,
        (
            "和丈夫商量了一下，\x01",
            "我们也得准备一些重建资金才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2228")

    TalkEnd(0x16)
    Return()

    # Function_14_20A3 end

    def Function_15_222C(): pass

    label("Function_15_222C")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_2239")
    OP_A2(0x6)

    label("loc_2239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前篇遇到过斯丁克】\x01",        # 0
            "【◇在前篇没遇到过斯丁克】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22A9"),
        (1, "loc_22AF"),
        (SWITCH_DEFAULT, "loc_22B5"),
    )


    label("loc_22A9")

    OP_A2(0x6)
    Jump("loc_22B5")

    label("loc_22AF")

    OP_A3(0x6)
    Jump("loc_22B5")

    label("loc_22B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2758")

    ChrTalk(    #139
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2465")

    ChrTalk(    #140
        0x101,
        (
            "#1000F请问，唔……\x02\x03",

            "斯丁克先生……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #141
        0xFE,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "卢格兰老爷子提到的那个\x01",
            "正游击士的新人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1011F卢格兰爷爷说的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#1041F这样看来，大概\x01",
            "说的是我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1000F不，在那种情况下这是当然的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "最近在拉文努村\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274F")

    label("loc_2465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B6")

    ChrTalk(    #150
        0x103,
        "#020F好久不见，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_2510")

    label("loc_24B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(    #151
        0x106,
        "#050F很久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_2510")

    label("loc_2509")

    TurnDirection(0xFE, 0x101, 400)

    label("loc_2510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2597")

    ChrTalk(    #152
        0xFE,
        "雪拉扎德吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        "#020F不，在那种情况下这是当然的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2703")

    label("loc_2597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261A")

    ChrTalk(    #156
        0xFE,
        "阿加特吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x106,
        "#051F哪里，那是我们的义务啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2703")

    label("loc_261A")


    ChrTalk(    #160
        0xFE,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "卢格兰老爷子提到的那个\x01",
            "正游击士的新人吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1011F卢格兰爷爷说的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x102,
        (
            "#1041F这样看来，大概\x01",
            "说的是我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1000F不，在那种情况下这是当然的。\x02",
    )

    CloseMessageWindow()

    label("loc_2703")


    ChrTalk(    #167
        0xFE,
        (
            "最近在拉文努村\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274F")

    OP_A2(0x1A53)
    OP_A2(0x7)
    Jump("loc_29A0")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27AE")

    ChrTalk(    #169
        0xFE,
        (
            "最近在拉文努村\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A0")

    label("loc_27AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2926")

    ChrTalk(    #171
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "唔，是你们啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2818")

    ChrTalk(    #173
        0x106,
        "#050F还是老样子啊，斯丁克。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2880")

    label("loc_2818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(    #174
        0x103,
        "#020F还是老样子呢，斯丁克。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2880")

    label("loc_284A")


    ChrTalk(    #175
        0x101,
        "#1001F你好，斯丁克先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        "#1041F好久不见了。\x02",
    )

    CloseMessageWindow()

    label("loc_2880")


    ChrTalk(    #177
        0xFE,
        (
            "现在不能使用魔法，\x01",
            "消灭魔兽需要多花一些时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "特别在敌人数量较多的情况下\x01",
            "需要十分注意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#1002F嗯，我明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x102,
        "#1042F斯丁克先生也请小心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_29A0")

    label("loc_2926")


    ChrTalk(    #181
        0xFE,
        (
            "现在不能使用魔法，\x01",
            "消灭魔兽需要多花一些时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "敌人数量较多的情况下\x01",
            "需要特别注意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "你们也要小心点……\x02",
    )

    CloseMessageWindow()

    label("loc_29A0")

    TalkEnd(0x14)
    Return()

    # Function_15_222C end

    def Function_16_29A4(): pass

    label("Function_16_29A4")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B45")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AD2")

    ChrTalk(    #184
        0xFE,
        "啊，阿加特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "刚刚正在给\x01",
            "你的妹妹祈祷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x106,
        (
            "#050F是吗……\x02\x03",

            "真不好意思。\x01",
            "总是让您陪我妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "哪里，没那回事。\x01",
            "对我来说她是个很好的倾诉对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "而且以前也总是\x01",
            "拜托她各种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "刚刚就在为村子的事\x01",
            "祈祷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "最近世间\x01",
            "似乎总是发生奇怪的事件……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3F")

    label("loc_2AD2")


    ChrTalk(    #191
        0xFE,
        (
            "所以要到女神身边为大家\x01",
            "祈愿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "祈求她们保佑\x01",
            "这拉文努村……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "最近世间\x01",
            "似乎总是发生奇怪的事件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3F")

    OP_A2(0xB)
    Jump("loc_2B93")

    label("loc_2B45")


    ChrTalk(    #194
        0xFE,
        (
            "所以要到女神身边为大家\x01",
            "祈愿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "最近世间\x01",
            "似乎总是发生奇怪的事件呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B93")

    TalkEnd(0x15)
    Return()

    # Function_16_29A4 end

    def Function_17_2B97(): pass

    label("Function_17_2B97")

    EventBegin(0x0)
    OP_A3(0x1C01)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB1")
    AddParty(0x5, 0xF7, 0xFF)
    AddParty(0x6, 0xF8, 0xFF)

    label("loc_2BB1")

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

    def lambda_2C27():
        OP_6D(21820, 440, 6800, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C27)
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

    ChrTalk(    #196
        0x107,
        "#064F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x106,
        "#052F#5P你……\x02",
    )

    CloseMessageWindow()

    def lambda_2D75():
        OP_6D(32800, 8000, 38500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D75)

    def lambda_2D8D():
        OP_6C(145000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D8D)
    Sleep(4000)
    SetChrPos(0x106, 33360, 8000, 49000, 180)
    SetChrPos(0x107, 32439, 8000, 49000, 180)

    def lambda_2DC4():
        OP_8E(0xFE, 0x8250, 0x1F40, 0x9B96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2DC4)
    Sleep(200)

    def lambda_2DE4():
        OP_8E(0xFE, 0x7EB7, 0x1F40, 0x9C5E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2DE4)
    Sleep(2000)

    ChrTalk(    #198
        0x9,
        "#163F#6P你是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    WaitChrThread(0x107, 0x1)
    SetChrSubChip(0x107, 0)

    ChrTalk(    #199
        0x106,
        (
            "#051F#6P没想到你\x01",
            "会在这种地方。\x02\x03",

            "什么风把你吹来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "#163F#2P没什么……只不过是一时兴起。\x02\x03",

            "#165F来祭拜妹妹的吧？\x01",
            "我就不打扰了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x106,
        (
            "#551F#6P喂喂。\x01",
            "我可没说你碍事啊。\x02\x03",

            "#050F那花……是你献的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x9,
        (
            "#166F#2P……算是吧。\x02\x03",

            "早知道是这样\x01",
            "就考虑用别的颜色了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#051F#6P虽然知道每年都有人\x01",
            "来献上和我的一样的花……\x02\x03",

            "却没想到是你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x9,
        (
            "#163F#2P这可怎么说呢……\x02\x03",

            "我也上了年纪了。\x01",
            "已经忘了为什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x106,
        "#051F#6P哼，就知道你会这样说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        (
            "#061F#6P嘿嘿……\x02\x03",

            "#560F请问，我也可以\x01",
            "献花吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        "#161F#2P噢……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(400)

    ChrTalk(    #208
        0x106,
        "#051F#5P啊啊，拜托了。\x02",
    )

    CloseMessageWindow()

    def lambda_3053():
        OP_6D(33700, 8000, 36340, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3053)
    OP_43(0x9, 0x1, 0x0, 0x18)

    def lambda_3072():
        OP_8E(0xFE, 0x8066, 0x1F40, 0x8DFE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3072)
    Sleep(500)
    OP_8C(0x106, 180, 400)
    Sleep(500)

    def lambda_309E():
        OP_8E(0xFE, 0x82B4, 0x1F40, 0x91B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_309E)
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

    def lambda_313F():
        OP_8F(0xFE, 0x7F9E, 0x1F40, 0x91B4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_313F)
    WaitChrThread(0x107, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #209
        (
            "\x07\x05阿加特和提妲\x01",
            "默默祈祷了片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #210
        0x106,
        "#053F#6P呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)
    Sleep(500)

    ChrTalk(    #211
        0x106,
        (
            "#050F#5P不好意思，提妲。\x01",
            "让你特地陪我。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)
    Sleep(500)

    ChrTalk(    #212
        0x107,
        (
            "#066F#4P不，我也想\x01",
            "好好地和米夏\x01",
            "打个招呼……\x02\x03",

            "谢谢，阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x106,
        (
            "#051F#5P喂喂。\x01",
            "要道谢的是我吧。\x02\x03",

            "还有，答应过等工作告一段落\x01",
            "之后让你见见她的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x107,
        "#067F#4P嘿嘿……是呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x9,
        (
            "#163F#5P呵呵……\x02\x03",

            "#165F龙似乎也说过，\x01",
            "你好像变了。\x02\x03",

            "给人的感觉\x01",
            "变得沉稳了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x9, 400)
    Sleep(500)

    ChrTalk(    #216
        0x106,
        (
            "#551F#6P别说了，我还不够成熟。\x02\x03",

            "#051F不过，我倒是感觉你\x01",
            "好像也已有所觉悟了。\x01",
            "从这次事件开始，\x02\x03",

            "去改变自己以往的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x9,
        (
            "#163F#5P唔……\x02\x03",

            "#160F……关于你所说过的，\x01",
            "军队这个组织的弊病……\x02\x03",

            "重新考虑过后，感觉\x01",
            "你的话也有一番道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x106,
        (
            "#552F#6P那是……\x01",
            "单纯的说气话罢了。\x02\x03",

            "我并不是说\x01",
            "军队有什么错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        (
            "#163F#5P好了，听我说。\x02\x03",

            "#160F从这次事件也可以知道\x01",
            "人和组织是不同的。\x02\x03",

            "军队的组织力派上了用场，\x01",
            "但因为游击士的机动能力强，\x01",
            "也将事件引导向好的结果。\x02\x03",

            "无论缺了哪边，这次的事件\x01",
            "都无法解决，你不这么认为吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x106,
        (
            "#050F#6P……算是吧。\x02\x03",

            "有了你们提供的线索，\x01",
            "才知道了龙的所在地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#166F#5P虽然不想借理查德说过的话……\x02\x03",

            "导力器发明之后，\x01",
            "物品和信息的流动，都变得更快更大了。\x02\x03",

            "为了更高效的处理物流和信息，\x01",
            "组织就需要不断扩张，并且\x01",
            "必须要做到细分化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x106,
        (
            "#555F#6P……军队就是个很好的例子。\x02\x03",

            "国境师团，飞行舰队，王室亲卫队，\x01",
            "王都警备队，情报部……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "#163F#5P嗯……\x02\x03",

            "#160F而这些，都可以说是\x01",
            "对应时代潮流变化的产物。\x02\x03",

            "虽说这变化中失去的东西\x01",
            "也不在少数……\x02\x03",

            "但后退是不可能了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x106,
        "#552F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #225
        0x9,
        (
            "#163F#5P所以你……\x02\x03",

            "#165F你们游击士\x01",
            "就用和我们不同的方法\x01",
            "把该守护的东西守护好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x106,
        "#052F#6P……啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x9,
        (
            "#163F#5P为了彼此要守护的东西\x01",
            "时而对立，时而配合……\x02\x03",

            "以此彼此弥补，\x01",
            "相互确认是否正确。\x02\x03",

            "#160F你不认为这就是\x01",
            "处理我们之间关系的正确做法吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x106,
        (
            "#051F#6P……呵呵，没错。\x02\x03",

            "嗯，今后我依然会\x01",
            "毫不客气地批判你们的。\x02\x03",

            "做好心理准备哦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #229
        0x9,
        (
            "#165F#5P呼，那也是我想说的。\x02\x03",

            "别再轻率行事，\x01",
            "你要时时记在心上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x107,
        "#061F#4P嘻嘻……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 32780, 8000, 45130, 180)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #231
        0x8,
        "青年的声音",
        "#2P呵呵……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #232
        0x8,
        "青年的声音",
        (
            "#2P不好意思，\x01",
            "稍微打扰一下。\x02",
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

    def lambda_39CF():

        label("loc_39CF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39CF")

    QueueWorkItem2(0x106, 1, lambda_39CF)
    Sleep(50)

    def lambda_39E5():

        label("loc_39E5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39E5")

    QueueWorkItem2(0x9, 1, lambda_39E5)
    Sleep(50)

    def lambda_39FB():

        label("loc_39FB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_39FB")

    QueueWorkItem2(0x107, 1, lambda_39FB)
    OP_0D()
    Sleep(500)

    ChrTalk(    #233
        0x106,
        "#054F#6P#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x107,
        "#065F#6P啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x9,
        "#160F#6P你是……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x72)
    Sleep(800)

    ChrTalk(    #236
        0x8,
        (
            "#124F#2P和将军阁下是初次见面吧。\x02\x03",

            "#120F我是『噬身之蛇』的执行者─\x01",
            "莱恩哈特。\x02\x03",

            "以后请记住我。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x9,
        "#161F#6P#3S什么！？\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 8)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_3B0E():
        OP_96(0xFE, 0x8098, 0x1F40, 0x9524, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3B0E)
    Sleep(100)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3B43():
        OP_91(0xFE, 0xFFFFFF38, 0x0, 0xFFFFFF38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3B43)
    WaitChrThread(0x106, 0x2)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 7)
    Sleep(500)

    ChrTalk(    #238
        0x106,
        (
            "#057F#6P……你小子……\x02\x03",

            "打算干什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x8,
        (
            "#121F#2P这里是死者长眠之地。\x01",
            "只可能会来做一件事吧。\x02\x03",

            "倒是你，打算在这里\x01",
            "继续前几天的决斗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x106,
        "#555F#6P呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x107,
        "#063F#6P阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x106,
        "#053F#6P……知道了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 65535)
    OP_0D()
    Sleep(1000)

    def lambda_3C69():
        OP_8F(0xFE, 0x81B0, 0x1F40, 0x8E08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C69)
    Sleep(1500)

    def lambda_3C89():
        OP_91(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3C89)
    Sleep(200)

    def lambda_3CA9():
        OP_91(0xFE, 0xFFFFFBB4, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3CA9)
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

    def lambda_3D7D():
        OP_8F(0xFE, 0x81CE, 0x1F40, 0x9024, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D7D)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #243
        "\x07\x05莱维静静的祈祷。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #244
        0x8,
        "#124F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "#160F#5P莱恩哈特……\x01",
            "就是『剑帝』莱维吗。\x02\x03",

            "我也同样不想打扰\x01",
            "死者的长眠……\x02\x03",

            "不过，就问一个问题行吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        "#124F#6P请便……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "#163F#5P这次事件中，\x01",
            "你似乎为了不造成过大伤害\x01",
            "而尽力控制住了龙的失控。\x02\x03",

            "并且现在，也为了悼念死者\x01",
            "而来此祈祷……\x02\x03",

            "#160F但为什么你又\x01",
            "要招来破坏和混沌？\x02\x03",

            "是有什么……\x01",
            "无法公开的内情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x8,
        (
            "#124F#6P……呵………\x02\x03",

            "#121F控制龙的失控\x01",
            "是为了正确进行实验。\x02\x03",

            "除此以外别无他意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        "#160F#5P但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x8,
        (
            "#124F#6P……我只是按照给我的命令，\x01",
            "作为『结社』的部下来行动。\x02\x03",

            "并不为任何人的意志所左右。\x02\x03",

            "#123F别把我和将『哈梅尔』这个名字忘记的你们\x01",
            "混为一谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #251
        0x9,
        "#161F#5P#4S！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #252
        0x106,
        (
            "#052F#6P你说『哈梅尔』？\x01",
            "为什么知道那个名字……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #253
        0x8,
        (
            "#125F#5P好了……\x01",
            "阿加特·科洛斯纳。\x02\x03",

            "#122F就算有坚定的意志，\x01",
            "但没有相应的实力就毫无意义。\x02\x03",

            "下次，可别以为只是碎了剑\x01",
            "就可以了事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x106,
        (
            "#051F#6P哼……正合我意。\x02\x03",

            "倒是你，别以为\x01",
            "永远都能绰绰有余。\x02\x03",

            "我很快就会赶上你，\x01",
            "做好准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        "#125F#5P呵……我期待着。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    def lambda_41EE():
        OP_6D(33420, 8000, 38810, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_41EE)

    def lambda_4206():
        OP_67(0, 8500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4206)

    def lambda_421E():
        OP_8E(0xFE, 0x7E5E, 0x1F40, 0xC56C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_421E)
    Sleep(1600)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    SetChrFlags(0x8, 0x80)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x9, 0x1)

    def lambda_425E():
        OP_6D(33100, 8000, 36700, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_425E)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    ChrTalk(    #256
        0x107,
        (
            "#063F#2P……那位哥哥。\x01",
            "有着寂寞的眼神。\x02\x03",

            "做祈祷的时候，一直……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x106,
        "#057F#5P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x9, 400)

    def lambda_42F5():
        OP_6D(33800, 8000, 36470, 1000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_42F5)
    OP_8F(0x106, 0x8138, 0x1F40, 0x9178, 0x5DC, 0x0)

    def lambda_4321():

        label("loc_4321")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_4321")

    QueueWorkItem2(0x107, 1, lambda_4321)
    WaitChrThread(0x106, 0x2)
    Sleep(500)

    ChrTalk(    #258
        0x106,
        (
            "#050F#6P喂……将军。\x02\x03",

            "『哈梅尔』就是\x01",
            "越过国境，\x01",
            "帝国边界处的一座村子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 315, 400)

    ChrTalk(    #259
        0x9,
        (
            "#161F#5P你……\x01",
            "知道那个名字吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x106,
        (
            "#053F#6P爆发战争前，和拉文努村\x01",
            "有过几次交流。\x02\x03",

            "#555F现在似乎完全\x01",
            "断绝了联系……\x02\x03",

            "为什么会说到那个名字？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "#163F#5P…………………………………\x02\x03",

            "#166F……关于这件事\x01",
            "我是不能说的。\x02\x03",

            "因为关系到国家间的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x106,
        "#052F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    def lambda_44A3():
        OP_6D(34070, 8000, 34770, 2000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_44A3)

    def lambda_44BB():
        OP_67(0, 6330, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_44BB)

    def lambda_44D3():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_44D3)

    def lambda_44E3():
        OP_6C(157000, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_44E3)
    Sleep(500)
    OP_8C(0x9, 180, 400)

    def lambda_44FF():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_44FF)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #263
        0x9,
        (
            "#166F#6P只是，我就说一点。\x02\x03",

            "如果，我的直觉\x01",
            "是对的话……\x02\x03",

            "#163F……那个叫莱维的男子，\x01",
            "肯定见过相当恐怖的地狱。\x02",
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

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4610")
    ShowSaveMenu()

    label("loc_4610")

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

    # Function_17_2B97 end

    def Function_18_464C(): pass

    label("Function_18_464C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4698")
    OP_8E(0xFE, 0x6AFE, 0xFFFFF060, 0x2486, 0x4B0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(800)
    OP_8E(0xFE, 0x5F00, 0xFFFFF060, 0x186A, 0x4B0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(800)
    Jump("Function_18_464C")

    label("loc_4698")

    Return()

    # Function_18_464C end

    def Function_19_4699(): pass

    label("Function_19_4699")

    Sleep(500)

    label("loc_469E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46EA")
    OP_8E(0xFE, 0x34F8, 0xFFFFF060, 0x2EAE, 0x5DC, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x33D6, 0xFFFFF060, 0x41AA, 0x5DC, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    Jump("loc_469E")

    label("loc_46EA")

    Return()

    # Function_19_4699 end

    def Function_20_46EB(): pass

    label("Function_20_46EB")

    Sleep(250)

    label("loc_46F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_472E")
    OP_8E(0xFE, 0x53D4, 0xFFFFF060, 0x2396, 0x578, 0x0)
    Sleep(900)
    OP_8E(0xFE, 0x54CE, 0xFFFFF060, 0x35A2, 0x578, 0x0)
    Sleep(900)
    Jump("loc_46F0")

    label("loc_472E")

    Return()

    # Function_20_46EB end

    def Function_21_472F(): pass

    label("Function_21_472F")

    OP_8E(0xFE, 0x681A, 0x1F40, 0xE506, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x1F40, 0xE506, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7EAE, 0x1F40, 0xD37C, 0x7D0, 0x0)
    Return()

    # Function_21_472F end

    def Function_22_476C(): pass

    label("Function_22_476C")

    OP_8E(0xFE, 0x6522, 0x1F40, 0xE5CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8A, 0x1F40, 0xE5CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7A8A, 0x1F40, 0xD37C, 0x7D0, 0x0)
    Return()

    # Function_22_476C end

    def Function_23_47A9(): pass

    label("Function_23_47A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47F5")
    OP_51(0x17, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x106, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_23_47A9")

    label("loc_47F5")

    Return()

    # Function_23_47A9 end

    def Function_24_47F6(): pass

    label("Function_24_47F6")

    OP_8E(0xFE, 0x8660, 0x1F40, 0x8D5E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_24_47F6 end

    def Function_25_4812(): pass

    label("Function_25_4812")

    ClearMapFlags(0x2000000)
    Return()

    # Function_25_4812 end

    def Function_26_4818(): pass

    label("Function_26_4818")

    EventBegin(0x1)

    ChrTalk(    #264
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_4844():
        OP_6D(35190, -3850, 5430, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4844)

    def lambda_485C():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_485C)

    def lambda_486C():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_486C)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #265
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F3")
    OP_C0(0xE, 0xA, 0x8976, 0xFFFFF0F6, 0x21D4, 0xB4, 0x88C2, 0xFFFFEF98, 0x1446)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_4902")

    label("loc_48F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4902")
    EventEnd(0x1)

    label("loc_4902")

    Return()

    # Function_26_4818 end

    def Function_27_4903(): pass

    label("Function_27_4903")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #266
        (
            "\x07\x05七耀历１１９２年\x01",
            "由于战火而失去的\x01",
            "６个善良的灵魂，长眠与此。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #267
        (
            "\x07\x05雷夫、阿贝尔、尼高尔、\x01",
            "维姆、依蕾娜、米夏。\x01",
            "愿你们在女神的怀抱中得到安宁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4903 end

    def Function_28_49CF(): pass

    label("Function_28_49CF")

    SetPlaceName(0x2E)
    Return()

    # Function_28_49CF end

    def Function_29_49D3(): pass

    label("Function_29_49D3")

    SetPlaceName(0x2D)
    Return()

    # Function_29_49D3 end

    def Function_30_49D7(): pass

    label("Function_30_49D7")

    SetPlaceName(0x2F)
    Return()

    # Function_30_49D7 end

    SaveToFile()

Try(main)
