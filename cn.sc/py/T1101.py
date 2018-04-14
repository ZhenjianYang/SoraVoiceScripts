from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1101   ._SN',
            'ED6_DT21/T1101_1 ._SN',
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
        '梅贝尔市长',                           # 9
        '莉拉',                                 # 10
        '雅哈多老人',                           # 11
        '哈里',                                 # 12
        '米娜',                                 # 13
        '奥维德',                               # 14
        '爱蕾吉娅',                             # 15
        '雷塔',                                 # 16
        '法娜',                                 # 17
        '斯丁克',                               # 18
        '米拉诺',                               # 19
        '西柏斯街道方向',                       # 20
        '东柏斯街道方向',                       # 21
        '柏斯市·南街区',                       # 22
        '柏斯国际空港',                         # 23
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT27/CH03790 ._CH',             # 09
        'ED6_DT07/CH01230 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT27/CH03790P._CP',             # 09
        'ED6_DT07/CH01230P._CP',             # 0A
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
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 53880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 52760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 53360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 51940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 65250,
        Z                   = 0,
        Y                   = 61510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 19300,
        Z                   = 0,
        Y                   = 48720,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 41,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 44,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = 43880,
        Y                   = 0,
        Z                   = 39840,
        Range               = 45290,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC4F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 56070,
        Y                   = 0,
        Z                   = 39690,
        Range               = 52630,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC36E,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = 53860,
        TriggerZ            = 0,
        TriggerY            = 40250,
        TriggerRange        = 1700,
        ActorX              = 53860,
        ActorZ              = 1000,
        ActorY              = 40250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4A6",          # 00, 0
        "Function_1_661",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_7B4",          # 03, 3
        "Function_4_8B1",          # 04, 4
        "Function_5_9D8",          # 05, 5
        "Function_6_B63",          # 06, 6
        "Function_7_DFF",          # 07, 7
        "Function_8_1211",         # 08, 8
        "Function_9_139C",         # 09, 9
        "Function_10_14F8",        # 0A, 10
        "Function_11_175D",        # 0B, 11
        "Function_12_1A02",        # 0C, 12
        "Function_13_2236",        # 0D, 13
        "Function_14_27AA",        # 0E, 14
        "Function_15_27F0",        # 0F, 15
        "Function_16_2836",        # 10, 16
        "Function_17_287C",        # 11, 17
        "Function_18_28E7",        # 12, 18
        "Function_19_3154",        # 13, 19
        "Function_20_32D3",        # 14, 20
        "Function_21_3334",        # 15, 21
        "Function_22_3920",        # 16, 22
        "Function_23_393C",        # 17, 23
        "Function_24_396C",        # 18, 24
        "Function_25_399C",        # 19, 25
        "Function_26_39F1",        # 1A, 26
        "Function_27_4078",        # 1B, 27
        "Function_28_409B",        # 1C, 28
        "Function_29_40BE",        # 1D, 29
        "Function_30_40EC",        # 1E, 30
        "Function_31_4105",        # 1F, 31
        "Function_32_411B",        # 20, 32
        "Function_33_47A6",        # 21, 33
        "Function_34_4CEF",        # 22, 34
        "Function_35_4DEE",        # 23, 35
        "Function_36_4E78",        # 24, 36
        "Function_37_4ED5",        # 25, 37
        "Function_38_4F2E",        # 26, 38
        "Function_39_4F32",        # 27, 39
        "Function_40_4F36",        # 28, 40
        "Function_41_4F3A",        # 29, 41
        "Function_42_4F3E",        # 2A, 42
        "Function_43_4F42",        # 2B, 43
        "Function_44_4F46",        # 2C, 44
        "Function_45_4F4A",        # 2D, 45
    )


    def Function_0_4A6(): pass

    label("Function_0_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_527")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xA, 52840, 0, 42530, 180)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0x10, 0x80)
    SetChrPos(0xF, 67450, 0, 52800, 260)
    Jump("loc_524")

    label("loc_4EA")

    SetChrPos(0xE, 49520, 0, 44390, 180)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrPos(0xB, 50500, 0, 46500, 180)
    SetChrPos(0xC, 51550, 0, 46750, 180)

    label("loc_524")

    Jump("loc_57A")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_57A")
    SetChrPos(0xA, 46680, 0, 77450, 180)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrPos(0xE, 66340, 0, 51290, 315)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    SetChrFlags(0x11, 0x10)

    label("loc_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_58A")
    SetChrFlags(0xD, 0x80)

    label("loc_58A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    ClearChrFlags(0x12, 0x80)

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_5C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_660")

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5DA")
    OP_A3(0x10F3)
    Event(0, 18)
    Jump("loc_660")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_5F0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_660")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_606")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_660")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_61C")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_660")

    label("loc_61C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_642")
    SetMapFlags(0x10000000)
    Event(1, 6)
    Jump("loc_660")

    label("loc_642")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_660")
    Event(0, 33)

    label("loc_660")

    Return()

    # Function_0_4A6 end

    def Function_1_661(): pass

    label("Function_1_661")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x230041)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6AA")
    OP_72(0xA, 0x10)
    OP_6F(0xA, 59)
    OP_72(0xB, 0x10)
    OP_6F(0xB, 59)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 59)
    OP_72(0xD, 0x10)
    OP_6F(0xD, 59)

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B6")
    OP_64(0x0, 0x1)

    label("loc_6B6")

    Return()

    # Function_1_661 end

    def Function_2_6B7(): pass

    label("Function_2_6B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B3")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_2_6B7")

    label("loc_7B3")

    Return()

    # Function_2_6B7 end

    def Function_3_7B4(): pass

    label("Function_3_7B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B0")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_3_7B4")

    label("loc_8B0")

    Return()

    # Function_3_7B4 end

    def Function_4_8B1(): pass

    label("Function_4_8B1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_8FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D4")
    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_8FB")

    label("loc_8D4")


    ChrTalk(    #0
        0xFE,
        (
            "哑、哑口无言\x01",
            "大概就是像这样吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    Jump("loc_9D4")

    label("loc_8FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_941")

    ChrTalk(    #1
        0xFE,
        (
            "怎么会\x01",
            "变成这样…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "我、我们该\x01",
            "怎么办才好…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_941")

    Jump("loc_9D4")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_9A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_997")

    ChrTalk(    #3
        0xFE,
        (
            "米娜说的\x01",
            "一定没错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "好！只要努力的话\x01",
            "就绝对会成功的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A5")

    label("loc_997")

    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_9A5")

    Jump("loc_9D4")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9CB")

    ChrTalk(    #5
        0xFE,
        "………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D4")

    label("loc_9CB")

    Call(0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_9D4")

    TalkEnd(0xB)
    Return()

    # Function_4_8B1 end

    def Function_5_9D8(): pass

    label("Function_5_9D8")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")
    Call(0, 6)
    Jump("loc_A41")

    label("loc_9F1")


    ChrTalk(    #6
        0xFE,
        (
            "在谈论经济之前\x01",
            "还是先想想清楚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "否则不管说多少好话\x01",
            "也都是没用的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A41")

    Jump("loc_B5F")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #8
        0xFE,
        (
            "那种巨大的东西\x01",
            "竟然会漂浮在天上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "龙的出现也许\x01",
            "就是这次事件的预兆吧…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_B5F")

    label("loc_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_AF2")

    ChrTalk(    #10
        0xFE,
        (
            "看来劝说别人\x01",
            "有时也需要说说谎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "真是好麻烦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_AF2")

    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_B00")

    Jump("loc_B5F")

    label("loc_B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B56")

    ChrTalk(    #12
        0xFE,
        (
            "哈里的想法\x01",
            "总是很有跳跃性，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "要是多想想\x01",
            "身边的事就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5F")

    label("loc_B56")

    Call(0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_B5F")

    TalkEnd(0xC)
    Return()

    # Function_5_9D8 end

    def Function_6_B63(): pass

    label("Function_6_B63")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_C5E")

    ChrTalk(    #14
        0xB,
        (
            "因为导力器瘫痪，\x01",
            "定期船也都停运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "这样下去的话\x01",
            "超市的商品就无法补充了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "是啊，经济方面的影响\x01",
            "确实不容忽视…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "比起那个，\x01",
            "照明问题也很让人担心吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "晚上都不敢去厕所，\x01",
            "这也是大问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF0")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C68")
    Jump("loc_DF0")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D73")

    ChrTalk(    #20
        0xB,
        "喂，米娜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "你觉得我有没有\x01",
            "商业的才能？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "当然有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "嗯，不但充满热情，\x01",
            "而且人缘也不差。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xC,
        (
            "虽然有点老实过头了，\x01",
            "不过这也算是有信用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "……所以，我相信你会成功的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xB,
        "是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "好！我会努力的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DF0")

    label("loc_D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_DF0")

    ChrTalk(    #30
        0xB,
        (
            "嗯，不管怎么样，\x01",
            "只要成为商人就算成功了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        (
            "这个嘛，\x01",
            "等当上商人才烦恼这个吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "………………\x02",
    )

    CloseMessageWindow()

    label("loc_DF0")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x2)
    OP_A2(0x3)
    Return()

    # Function_6_B63 end

    def Function_7_DFF(): pass

    label("Function_7_DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E0B")
    Call(1, 1)
    Return()

    label("loc_E0B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9E")

    ChrTalk(    #34
        0xFE,
        (
            "城里的状况\x01",
            "总算是平静了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "难道大家都忘了天上\x01",
            "还漂浮着那个东西了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "嗯嗯，虽然习惯了，\x01",
            "但还是觉得可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_EF6")

    label("loc_E9E")


    ChrTalk(    #37
        0xFE,
        (
            "难道大家都忘了天上\x01",
            "还漂浮着一个岛了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "嗯嗯，虽然习惯了，\x01",
            "但还是觉得可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF6")

    Jump("loc_120D")

    label("loc_EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB8")

    ChrTalk(    #39
        0xFE,
        (
            "在这里看那个岛\x01",
            "看得很清楚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "它在夜空中出现的同时\x01",
            "城里的灯就全部熄灭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "龙的袭击事件才刚过去，\x01",
            "本以为不会再有事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "我们的柏斯还\x01",
            "真是多灾多难啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_101D")

    label("loc_FB8")


    ChrTalk(    #43
        0xFE,
        (
            "在这里看那个岛\x01",
            "看得很清楚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "为什么会出现\x01",
            "那种东西呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "我们的柏斯还\x01",
            "真是多灾多难啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101D")

    Jump("loc_120D")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_10F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(    #46
        0xFE,
        (
            "超市也\x01",
            "重新开始营业了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "呼呼呼～\x01",
            "还真是多灾多难的城市啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F3")

    label("loc_1077")


    ChrTalk(    #48
        0xFE,
        (
            "超市也\x01",
            "重新开始营业了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "定期船的国际航行也恢复了，\x01",
            "总算是恢复了原状。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "呼呼呼～\x01",
            "还真是多灾多难的城市啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10F3")

    Jump("loc_120D")

    label("loc_10F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_120D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1148")

    ChrTalk(    #51
        0xFE,
        (
            "柏斯的未来就跟今早的阳光一样，\x01",
            "十分的光明啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "呼呼呼～\x02",
    )

    CloseMessageWindow()
    Jump("loc_120D")

    label("loc_1148")


    ChrTalk(    #53
        0xFE,
        (
            "柏斯的超市\x01",
            "算得上是王国的经济中心之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "好像要和帝国\x01",
            "进行交易呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "互不侵犯条约签署之后，\x01",
            "国际性的交易也会更多吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "柏斯的未来就跟今早的阳光一样，\x01",
            "十分的光明啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "呼呼呼～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_120D")

    TalkEnd(0xA)
    Return()

    # Function_7_DFF end

    def Function_8_1211(): pass

    label("Function_8_1211")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1266")

    ChrTalk(    #58
        0xFE,
        (
            "超市似乎\x01",
            "要开始大甩卖活动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "在这种时期进行活动\x01",
            "还真是不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1398")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C1")

    ChrTalk(    #60
        0xFE,
        (
            "本来想去看看\x01",
            "有没有什么便宜货……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "不过现在还是\x01",
            "没工夫去啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_12EC")

    label("loc_12C1")


    ChrTalk(    #62
        0xFE,
        (
            "在这种时候，\x01",
            "很少有地方会征打工的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EC")

    Jump("loc_1398")

    label("loc_12EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1337")

    ChrTalk(    #63
        0xFE,
        "我正在找新的工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "嗯，果然还是\x01",
            "超市最好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1398")

    label("loc_1337")


    ChrTalk(    #65
        0xFE,
        "我正在找新的工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "要是有薪水高的地方\x01",
            "就最好不过了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "嗯，果然还是\x01",
            "超市最好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1398")

    TalkEnd(0xF)
    Return()

    # Function_8_1211 end

    def Function_9_139C(): pass

    label("Function_9_139C")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_140D")

    ChrTalk(    #68
        0xFE,
        "昨天晚上真恐怖啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "城里的人们一直\x01",
            "愤怒地叫到了半夜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "这种时候\x01",
            "需要更齐心协力才对啊…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F4")

    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_14F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_147A")

    ChrTalk(    #71
        0xFE,
        (
            "『安特洛丝餐厅』的料理\x01",
            "果然和传闻中一样完美啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "现在想起那味道\x01",
            "还忍不住流口水呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F4")

    label("loc_147A")


    ChrTalk(    #73
        0xFE,
        (
            "不久前我们去过\x01",
            "那家『安特洛丝餐厅』呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "那里的每道料理\x01",
            "都十分美味啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "现在想起那味道\x01",
            "还忍不住流口水呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_14F4")

    TalkEnd(0x10)
    Return()

    # Function_9_139C end

    def Function_10_14F8(): pass

    label("Function_10_14F8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_15B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(    #76
        0xFE,
        (
            "因为超市里总能\x01",
            "听见吵闹的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "要不就去试试\x01",
            "推销一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "一会准备\x01",
            "去看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_15AF")

    label("loc_156B")


    ChrTalk(    #79
        0xFE,
        (
            "在超市外面都能\x01",
            "听见商人的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "要不就去试试\x01",
            "推销一下吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AF")

    Jump("loc_1759")

    label("loc_15B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(    #81
        0xFE,
        "那、那究竟是什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "还有，为什么导力器\x01",
            "会突然瘫痪？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "够了！\x01",
            "我什么也不想知道！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1664")

    label("loc_1625")


    ChrTalk(    #84
        0xFE,
        "那、那究竟是什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "还有，为什么导力器\x01",
            "会突然瘫痪？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1664")

    Jump("loc_1759")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1708")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_16BA")

    ChrTalk(    #86
        0xFE,
        (
            "真高兴啊！\x01",
            "超市又开张了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "真是值得庆贺，\x01",
            "去买点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1705")

    label("loc_16BA")


    ChrTalk(    #88
        0xFE,
        (
            "呵呵，真高兴啊。\x01",
            "超市又开张了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "今天值得庆祝，\x01",
            "去买点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1705")

    Jump("loc_1759")

    label("loc_1708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1759")

    ChrTalk(    #90
        0xFE,
        (
            "呵呵，今天\x01",
            "去买点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "最近实在无聊，\x01",
            "唯一的乐趣就是购物了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1759")

    TalkEnd(0xE)
    Return()

    # Function_10_14F8 end

    def Function_11_175D(): pass

    label("Function_11_175D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_186F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1852")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过后篇一章【食材收集】委托】\x01",                  # 0
            "【◇完成过前篇【寻找荧光菇】、【探索护卫】委托】\x01",      # 1
            "【◇没有完成】\x01",                                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_181C"),
        (1, "loc_182E"),
        (2, "loc_1840"),
        (SWITCH_DEFAULT, "loc_1852"),
    )


    label("loc_181C")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_1852")

    label("loc_182E")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_1852")

    label("loc_1840")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_1852")

    label("loc_1852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_186F")
    Call(1, 4)
    Return()

    label("loc_186F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1911")

    ChrTalk(    #92
        0xD,
        (
            "哟！超市\x01",
            "终于恢复营业了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        (
            "在本地商人的帮助下，总算\x01",
            "和『安特洛丝餐厅』进行商谈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "……就是这样，为了计划的实现\x01",
            "好！马上开始营业吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FE")

    label("loc_1911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_19FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_197F")

    ChrTalk(    #95
        0xD,
        (
            "果然还是要\x01",
            "老老实实开始营业啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xD,
        (
            "要和『安特洛丝餐厅』\x01",
            "商谈的话，\x01",
            "需要本地人的协助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FE")

    label("loc_197F")


    ChrTalk(    #97
        0xD,
        (
            "嗯，这就是\x01",
            "柏斯超市吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "果然还是要\x01",
            "老老实实开始营业啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "要和『安特洛丝餐厅』\x01",
            "商谈的话，\x01",
            "需要本地人的协助。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19FE")

    TalkEnd(0xD)
    Return()

    # Function_11_175D end

    def Function_12_1A02(): pass

    label("Function_12_1A02")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_1A0F")
    OP_A2(0x8)

    label("loc_1A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8B")
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
        (0, "loc_1A7F"),
        (1, "loc_1A85"),
        (SWITCH_DEFAULT, "loc_1A8B"),
    )


    label("loc_1A7F")

    OP_A2(0x8)
    Jump("loc_1A8B")

    label("loc_1A85")

    OP_A3(0x8)
    Jump("loc_1A8B")

    label("loc_1A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_1B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(    #100
        0x11,
        (
            "柏斯这边\x01",
            "有我一个人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        "……谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3A")

    label("loc_1AE8")


    ChrTalk(    #102
        0x11,
        "是你们吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        (
            "柏斯这边\x01",
            "有我一个人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        "……谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_1B3A")

    Jump("loc_1B7A")

    label("loc_1B3D")


    ChrTalk(    #105
        0x11,
        (
            "柏斯这边\x01",
            "有我一个人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x11,
        "……谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()

    label("loc_1B7A")

    Jump("loc_2232")

    label("loc_1B7D")


    ChrTalk(    #107
        0x11,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1E54")

    ChrTalk(    #108
        0x101,
        (
            "#1011F啊，你是……\x02\x03",

            "斯丁克……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #109
        0x11,
        (
            "你是……\x01",
            "那时的准游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        "呀，看样子已经晋升正游击士了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1016F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D18")

    ChrTalk(    #112
        0x103,
        "#027F好久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #113
        0x11,
        "雪拉扎德吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        "#026F哪里，这是应该做的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DEA")

    ChrTalk(    #117
        0x106,
        "#051F好久不见，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #118
        0x11,
        "阿加特吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x106,
        "#051F哪里，这是我们的义务啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E51")

    label("loc_1DEA")


    ChrTalk(    #122
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#1002F嗯，这是应该的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1E51")

    Jump("loc_21C8")

    label("loc_1E54")


    ChrTalk(    #125
        0x101,
        (
            "#1015F（啊？这个人……）\x02\x03",

            "（仔细看看的话，\x01",
            "　竟然也戴着游击士的徽章啊？）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F61")

    ChrTalk(    #126
        0x103,
        "#027F好久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #127
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        "#026F哪里，这是应该做的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C8")

    label("loc_1F61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2033")

    ChrTalk(    #130
        0x106,
        "#051F好久不见，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #131
        0x11,
        "阿加特吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x106,
        "#051F哪里，这是我们的义务啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C8")

    label("loc_2033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2069")

    ChrTalk(    #135
        0x108,
        "#070F（嗯，看来他也是游击士。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_209E")

    label("loc_2069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209E")

    ChrTalk(    #136
        0x104,
        "#030F（嗯，看来也是个游击士啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_209E")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #137
        0x11,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        (
            "卢格兰老爷子提到的那个\x01",
            "新人正游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1011F卢格兰爷爷说的？\x02\x03",

            "#1015F那应该就是我了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x11,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        (
            "这次的巨龙骚乱事件，\x01",
            "全靠你们全力帮助才解决的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1002F哪里，身为游击士，\x01",
            "这是应该做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x11,
        "……真是让人信赖的回答啊。\x02",
    )

    CloseMessageWindow()

    label("loc_21C8")


    ChrTalk(    #146
        0x11,
        (
            "柏斯这边\x01",
            "有我一个人就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        (
            "……你们也继续自己\x01",
            "本来的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        "……谢谢你们的帮忙。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x9)

    label("loc_2232")

    TalkEnd(0x11)
    Return()

    # Function_12_1A02 end

    def Function_13_2236(): pass

    label("Function_13_2236")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224D")
    Call(0, 35)
    Call(0, 37)

    label("loc_224D")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    OP_6D(59660, 480, 80570, 0)
    OP_67(0, 9550, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(500)

    def lambda_22CC():
        OP_6D(59380, 0, 76340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22CC)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x10)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x11)
    WaitChrThread(0xF9, 0x1)
    Sleep(300)

    ChrTalk(    #149
        0x101,
        (
            "#1015F那么……\x01",
            "因为飞船无法使用，\x01",
            "所以现在只能徒步旅行了。\x02\x03",

            "洛连特支部和卢安支部，\x01",
            "要去哪边好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#1035F#6P恩……\x01",
            "我觉得走哪边都无所谓。\x02\x03",

            "#1043F因为每个地方的\x01",
            "状况都一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1007F这样啊……的确。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2448")

    ChrTalk(    #152
        0x106,
        (
            "#053F嗯，在这种状况下。\x02\x03",

            "#050F走哪边都一样。\x01",
            "反正也要确认一下\x01",
            "各地的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2503")

    label("loc_2448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AB")

    ChrTalk(    #153
        0x103,
        (
            "#026F是啊，在这种状况下……\x02\x03",

            "#524F不管走哪边\x01",
            "反正也要确认一下\x01",
            "各地的情况呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2503")

    label("loc_24AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(    #154
        0x108,
        (
            "#074F在这种状况下，\x02\x03",

            "#070F不管走哪边\x01",
            "反正也要确认一下\x01",
            "各地的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2503")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254A")

    ChrTalk(    #155
        0x107,
        (
            "#560F要是遇到有困难的人\x01",
            "我们就顺便帮帮他们好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_254A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2591")

    ChrTalk(    #156
        0x108,
        (
            "#070F要是遇到有困难的人\x01",
            "我们也可以顺便帮助他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D7")

    label("loc_2591")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D7")

    ChrTalk(    #157
        0x103,
        (
            "#524F要是遇到有困难的人\x01",
            "我们也可以顺便帮助他们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D7")


    ChrTalk(    #158
        0x101,
        "#1006F嗯……说的对！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #159
        (
            "\x07\x05※在导力停止现象中，只有装备『零力\x01",
            "　场发生器』的角色才可以使用魔法。\x01",
            "　请在主选单的[Equip]选项内\x01",
            "　将『零力场发生器』装备上吧。\x02\x03",

            "※另外，由于提妲的武器是导力炮，如\x01",
            "　果不装备『零力场发生器』的话就连\x01",
            "　普通攻击和战技也都无法使用。不过\x01",
            "　由于Ｓ超杀技『炮射冲击II』是使用\x01",
            "　火药式的枪械，所以可以正常使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_C4(0x0, 0x8)
    OP_28(0x9A, 0x1, 0x1000)
    OP_28(0x9A, 0x1, 0x2000)
    OP_28(0x9B, 0x4, 0x2)
    OP_28(0x9B, 0x4, 0x8)
    OP_28(0x9B, 0x1, 0x1)
    OP_28(0x9B, 0x1, 0x2)
    OP_28(0x9B, 0x1, 0x4)
    OP_28(0x9B, 0x1, 0x10)
    OP_28(0x9B, 0x1, 0x40)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_3E(0x151, 4)
    OP_4B(0xE, 255)
    OP_4B(0xA, 255)
    OP_20(0x3E8)
    OP_21()
    EventEnd(0x0)
    OP_1D(0x1A)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2236 end

    def Function_14_27AA(): pass

    label("Function_14_27AA")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE65A, 0x0, 0x124F8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_27AA end

    def Function_15_27F0(): pass

    label("Function_15_27F0")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_27F0 end

    def Function_16_2836(): pass

    label("Function_16_2836")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEAC4, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_2836 end

    def Function_17_287C(): pass

    label("Function_17_287C")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE696, 0x1E0, 0x136DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x3)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xE6A0, 0x0, 0x12BEC, 0x7D0, 0x0)
    Return()

    # Function_17_287C end

    def Function_18_28E7(): pass

    label("Function_18_28E7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28FE")
    Call(0, 35)
    Call(0, 36)

    label("loc_28FE")

    Call(0, 19)
    SetChrPos(0xF8, 60660, 0, 76570, 135)
    SetChrPos(0x101, 61720, 0, 76670, 135)
    SetChrPos(0xF7, 61830, 0, 77710, 135)
    SetChrPos(0xF9, 60400, 0, 77960, 135)
    SetChrPos(0xFA, 62880, 0, 75050, 315)
    SetChrPos(0xFB, 63770, 0, 75420, 315)
    SetChrPos(0xFC, 62310, 0, 74280, 315)
    OP_6D(61500, 0, 77120, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(324000, 0)
    OP_6E(262, 0)
    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2A13")

    ChrTalk(    #160
        0x106,
        (
            "#051F#6P那么，我们就先走一步，\x01",
            "到『川蝉亭』等你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2A13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2A5E")

    ChrTalk(    #161
        0x103,
        (
            "#021F#6P那么，我们就先走一步，\x01",
            "到『川蝉亭』等你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2AA7")

    ChrTalk(    #162
        0x108,
        (
            "#071F#6P那么，我们就先走一步，\x01",
            "到『川蝉亭』等你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2AEF")

    ChrTalk(    #163
        0x104,
        (
            "#031F#6P那么，我们就先走一步，\x01",
            "到『川蝉亭』等你们啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEF")


    ChrTalk(    #164
        0x101,
        (
            "#1006F#5P嗯，好的。\x02\x03",

            "登记的事情就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B72")

    ChrTalk(    #165
        0x103,
        (
            "#027F#5P卢格兰爷爷已经和他们联系过了，\x01",
            "应该不会定不到房间的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_2B72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC6")

    ChrTalk(    #166
        0x106,
        (
            "#051F#5P卢格兰爷爷已经和他们联系过了，\x01",
            "应该不会定不到房间的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_2BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1A")

    ChrTalk(    #167
        0x108,
        (
            "#070F#5P卢格兰爷爷已经和他们联系过了，\x01",
            "应该不会定不到房间的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_2C1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6B")

    ChrTalk(    #168
        0x104,
        (
            "#030F#5P卢格兰爷爷已经和他们联系过了，\x01",
            "应该不会定不到房间的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2C9B")

    ChrTalk(    #169
        0x107,
        "#061F#6P好啦，交给我们吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D24")

    label("loc_2C9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2CC9")

    ChrTalk(    #170
        0x105,
        "#048F#6P是，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D24")

    label("loc_2CC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2CF7")

    ChrTalk(    #171
        0x104,
        "#031F#6P呼，包在我身上。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D24")

    label("loc_2CF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2D24")

    ChrTalk(    #172
        0x108,
        "#071F#6P啊啊～交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2D24")

    OP_8C(0xFA, 180, 400)

    def lambda_2D31():
        OP_8E(0xFE, 0xF8D4, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_2D31)
    Sleep(500)
    OP_8C(0xFB, 180, 400)

    def lambda_2D58():
        OP_8E(0xFE, 0xFCEE, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_2D58)
    Sleep(500)
    OP_8C(0xFC, 180, 400)

    def lambda_2D7F():
        OP_8E(0xFE, 0xF46A, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_2D7F)

    def lambda_2D9A():
        OP_6D(62540, 0, 74000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D9A)

    def lambda_2DB2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2DB2)
    Sleep(100)

    def lambda_2DC5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DC5)
    Sleep(100)

    def lambda_2DD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2DD8)
    Sleep(100)

    def lambda_2DEB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2DEB)
    WaitChrThread(0xFC, 0x1)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    WaitChrThread(0x101, 0x0)

    def lambda_2E12():
        OP_6D(60780, 0, 77800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E12)
    WaitChrThread(0x101, 0x0)

    def lambda_2E2F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2E2F)
    Sleep(50)

    def lambda_2E42():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E42)
    Sleep(50)

    def lambda_2E55():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2E55)
    Sleep(50)

    def lambda_2E68():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2E68)
    Sleep(400)

    ChrTalk(    #173
        0x101,
        (
            "#1006F#6P那么，我们就再去\x01",
            "确认一下留言板吧？\x02\x03",

            "不知道柏斯各地在龙的骚乱之后\x01",
            "有没有顺利恢复正常…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

    ChrTalk(    #174
        0x106,
        (
            "#051F#5P嗯～老爷子难得\x01",
            "这么大方一次。\x02\x03",

            "尽快去湖边会合吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302D")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F81")

    ChrTalk(    #175
        0x103,
        (
            "#020F#5P好啦，卢格兰爷爷\x01",
            "难得邀请咱们一次，\x02\x03",

            "还是尽快\x01",
            "去湖边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302D")

    label("loc_2F81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD6")

    ChrTalk(    #176
        0x108,
        (
            "#070F#5P哈哈，老爷爷\x01",
            "特地邀请我们一次。\x02\x03",

            "还是尽快\x01",
            "到湖边去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302D")

    label("loc_2FD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302D")

    ChrTalk(    #177
        0x104,
        (
            "#035F#5P呼～那位老人\x01",
            "特地邀请我们一次。\x02\x03",

            "#030F还是尽早\x01",
            "到湖畔去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302D")


    ChrTalk(    #178
        0x101,
        (
            "#1015F#6P说的也对啊……\x02\x03",

            "#1001F嗯！那我们就尽快完成工作，\x01",
            "然后就去瓦雷利亚湖吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A6")

    ChrTalk(    #179
        0x107,
        "#061F#5P嗯⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_30A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C9")

    ChrTalk(    #180
        0x105,
        "#041F#5P是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_30C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F2")

    ChrTalk(    #181
        0x104,
        "#031F#5P呼，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3114")

    label("loc_30F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3114")

    ChrTalk(    #182
        0x108,
        "#071F#5P噢噢！\x02",
    )

    CloseMessageWindow()

    label("loc_3114")

    Sleep(100)
    Call(0, 20)
    Sleep(100)
    OP_4B(0xA, 255)
    OP_4B(0xE, 255)
    OP_28(0x78, 0x4, 0x40)
    OP_28(0x96, 0x1, 0x800)
    OP_28(0x96, 0x1, 0x1000)
    OP_28(0x97, 0x4, 0x2)
    OP_28(0x97, 0x4, 0x8)
    OP_28(0x97, 0x1, 0x1)
    OP_28(0x97, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_18_28E7 end

    def Function_19_3154(): pass

    label("Function_19_3154")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_318D")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_318D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31C6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31AE")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_31B2")

    label("loc_31AE")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_31B2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3213")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31E7")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_31FF")

    label("loc_31E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31FB")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_31FF")

    label("loc_31FB")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_31FF")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3260")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3234")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_324C")

    label("loc_3234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3248")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_324C")

    label("loc_3248")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_324C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3260")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32AD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3281")
    AddParty(0x2, 0xFA, 0xFF)
    Jump("loc_3299")

    label("loc_3281")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3295")
    AddParty(0x2, 0xFB, 0xFF)
    Jump("loc_3299")

    label("loc_3295")

    AddParty(0x2, 0xFC, 0xFF)

    label("loc_3299")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32D2")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32D2")

    Return()

    # Function_19_3154 end

    def Function_20_32D3(): pass

    label("Function_20_32D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_32E3")
    RemoveParty(0x7, 0xFF)

    label("loc_32E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_32F3")
    RemoveParty(0x4, 0xFF)

    label("loc_32F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3303")
    RemoveParty(0x6, 0xFF)

    label("loc_3303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3313")
    RemoveParty(0x3, 0xFF)

    label("loc_3313")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3323")
    RemoveParty(0x5, 0xFF)

    label("loc_3323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3333")
    RemoveParty(0x2, 0xFF)

    label("loc_3333")

    Return()

    # Function_20_32D3 end

    def Function_21_3334(): pass

    label("Function_21_3334")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3347")
    Call(0, 34)

    label("loc_3347")

    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    OP_6D(59000, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 59000, 500, 81490, 180)
    SetChrPos(0x106, 59000, 500, 81490, 180)
    SetChrPos(0xF8, 59000, 500, 81490, 180)
    SetChrPos(0xF9, 59000, 500, 81490, 180)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x106, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Sleep(1000)

    def lambda_3426():
        OP_6D(59010, 0, 74980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3426)

    def lambda_343E():
        OP_6C(65000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_343E)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #183
        0x101,
        (
            "#1006F啊，这次被通缉的魔兽\x01",
            "真是遍布各地啊…\x02\x03",

            "反正机会难得，\x01",
            "不如顺便去一趟拉文努村怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FF")

    ChrTalk(    #184
        0x107,
        "#560F啊……⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x106,
        (
            "#555F我说你啊……\x01",
            "为什么要用那么期待的眼神看我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x107,
        (
            "#067F嘿嘿嘿……\x02\x03",

            "阿加特哥哥的故乡，\x01",
            "我一直都很想去看一次的。\x02\x03",

            "#063F那个，不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x106,
        (
            "#053F……现在不行。\x02\x03",

            "#050F等我们将通缉魔兽\x01",
            "全部解决之后再说吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        "#561F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1019F真是的，小气鬼～\x02\x03",

            "难得提妲也在一起，\x01",
            "你就不能破一次例吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x106,
        "#551F什、什么叫破例……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x107,
        (
            "#065F姐、姐姐，没关系啦！\x02\x03",

            "把工作放在第一位\x01",
            "是理所当然的事情…\x02\x03",

            "#562F对不起，阿加特哥哥，\x01",
            "我又任性了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x106,
        (
            "#552F不、不是的……\x02\x03",

            "#556F那个……总之。\x01",
            "等工作完成之后我一定会带你去的。\x02\x03",

            "所以暂时先忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x107,
        "#061F是的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F0")

    label("loc_36FF")


    ChrTalk(    #194
        0x106,
        (
            "#555F我说你啊……\x01",
            "在定期船上已经说过了啊。\x02\x03",

            "要去拉文努村的话，\x01",
            "还是等柏斯的事件告一段落之后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1019F真是的，小气鬼～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37EC")

    ChrTalk(    #196
        0x104,
        (
            "#035F呼，阿加特兄\x01",
            "说得没错啊。\x02\x03",

            "#037F丢下提妲妹妹不管的话，\x01",
            "我们去了\x01",
            "也没意义呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_37EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3856")

    ChrTalk(    #197
        0x105,
        (
            "#045F呵呵，也许正如阿加特\x01",
            "说的那样。\x02\x03",

            "#542F丢下提妲不管的话，\x01",
            "我们去了\x01",
            "也没意义啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_3856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38BB")

    ChrTalk(    #198
        0x103,
        (
            "#021F呵呵，也许正如\x01",
            "阿加特所说啊。\x02\x03",

            "#027F扔下提妲不管的话，\x01",
            "我们去了\x01",
            "也没意思嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BB")


    ChrTalk(    #199
        0x101,
        "#1001F哈，是这样的吗⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x106,
        "#055F真是无法理解！\x02",
    )

    CloseMessageWindow()

    label("loc_38F0")

    OP_A2(0x1A0D)
    OP_28(0x93, 0x4, 0x2)
    OP_28(0x93, 0x4, 0x8)
    OP_28(0x93, 0x1, 0x1)
    OP_28(0x93, 0x1, 0x2)
    OP_28(0x93, 0x1, 0x10)
    OP_28(0x93, 0x1, 0x80)
    OP_4B(0xE, 255)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_21_3334 end

    def Function_22_3920(): pass

    label("Function_22_3920")

    OP_8E(0xFE, 0xE678, 0x0, 0x121CE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_3920 end

    def Function_23_393C(): pass

    label("Function_23_393C")

    OP_8E(0xFE, 0xE678, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE966, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_393C end

    def Function_24_396C(): pass

    label("Function_24_396C")

    OP_8E(0xFE, 0xE678, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE330, 0x0, 0x12548, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_396C end

    def Function_25_399C(): pass

    label("Function_25_399C")

    OP_8E(0xFE, 0xE678, 0x190, 0x13560, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xE678, 0x0, 0x12872, 0x7D0, 0x0)
    Return()

    # Function_25_399C end

    def Function_26_39F1(): pass

    label("Function_26_39F1")

    EventBegin(0x0)
    OP_6D(63080, 0, 53130, 0)
    OP_67(0, 9460, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(265, 0)
    SetChrPos(0xA, 62320, 0, 51020, 360)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    def lambda_3A71():
        OP_6D(62390, 0, 58620, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A71)
    FadeToBright(2000, 0)
    OP_8E(0xA, 0xF370, 0x0, 0xE704, 0x7D0, 0x0)
    OP_4A(0xA, 255)
    SetChrPos(0x8, 61930, 0, 68420, 180)
    SetChrPos(0x9, 62610, 0, 68980, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #201
        0x8,
        "女性的声音",
        "#6P您好啊，雅哈多爷爷。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3B1A():
        OP_6D(62420, 0, 60760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B1A)

    def lambda_3B32():
        OP_67(0, 9360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B32)

    def lambda_3B4A():
        OP_6E(272, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B4A)

    def lambda_3B5A():
        OP_8E(0xFE, 0xF1EA, 0x0, 0xEF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3B5A)
    Sleep(100)

    def lambda_3B7A():
        OP_8E(0xFE, 0xF492, 0x0, 0xF104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B7A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #202
        0xA,
        "啊，这不是市长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        "是要去教会做礼拜吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x8,
        (
            "#611F#5P不，准备去\x01",
            "视察一下超市。\x02\x03",

            "礼拜的话，准备之后再去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    ChrTalk(    #205
        0x9,
        (
            "#623F#2P小姐……\x02\x03",

            "前几天您也是这么说的，\x01",
            "但最后也是没去啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #206
        0x8,
        (
            "#615F#6P好啦，莉拉～\x01",
            "那种事情何必记这么清楚。\x02\x03",

            "#612F今天我一定会去的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "呵呵，工作虽然不能丢下，\x01",
            "不过日常生活也是很重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "像你这种责任重大\x01",
            "的人就更是如此。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D13():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D13)
    Sleep(150)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #209
        0x8,
        (
            "#617F#5P嗯，我会记住的。\x02\x03",

            "#611F那么我们就先\x01",
            "失陪了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        "#621F#5P失陪了。（点头致意）\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3D90():

        label("loc_3D90")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3D90")

    QueueWorkItem2(0xA, 1, lambda_3D90)
    OP_43(0x8, 0x1, 0x0, 0x1B)
    Fade(1000)
    OP_6D(59360, 0, 60210, 0)
    OP_67(0, 10720, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x1C)
    WaitChrThread(0x8, 0x1)
    Sleep(300)
    OP_72(0xB, 0x10)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3B)
    OP_73(0xB)

    def lambda_3E16():
        OP_8E(0xFE, 0xD516, 0x1F4, 0xEA6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E16)
    Sleep(500)

    def lambda_3E36():
        OP_8E(0xFE, 0xD516, 0x1F4, 0xEA6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E36)

    def lambda_3E51():
        OP_6D(62320, 0, 59140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E51)

    def lambda_3E69():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E69)

    def lambda_3E81():
        OP_6C(242000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E81)

    def lambda_3E91():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3E91)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_6F(0xB, 59)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x10)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x1)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #211
        0xA,
        (
            "#6P呼～自从她父亲去世之后，\x01",
            "这孩子就马上被选为市长候补。\x01",
            "当时我还在担心她承担不了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "#6P但现在看来，\x01",
            "她已经完全是个称职的市长了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xA,
        (
            "#6P嗯，其实我也觉得\x01",
            "她可以不用这么卖力的…\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_8E(0xA, 0xF370, 0x0, 0xE8F8, 0x7D0, 0x1)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 90, 400)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA)

    ChrTalk(    #214
        0xA,
        "#5P……那、那是什么？\x02",
    )

    CloseMessageWindow()

    def lambda_4001():
        OP_6D(64379, 0, 59730, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4001)

    def lambda_4019():
        OP_67(0, 7140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4019)

    def lambda_4031():
        OP_6B(3110, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4031)

    def lambda_4041():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4041)

    def lambda_4051():
        OP_6E(632, 7000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4051)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_39F1 end

    def Function_27_4078(): pass

    label("Function_27_4078")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xE088, 0x19A, 0xEA6A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_27_4078 end

    def Function_28_409B(): pass

    label("Function_28_409B")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xE470, 0x0, 0xEA6A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_28_409B end

    def Function_29_40BE(): pass

    label("Function_29_40BE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CD, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_29_40BE end

    def Function_30_40EC(): pass

    label("Function_30_40EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4104")
    OP_A2(0xC)
    Call(0, 32)

    label("loc_4104")

    Return()

    # Function_30_40EC end

    def Function_31_4105(): pass

    label("Function_31_4105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411A")
    Call(0, 32)

    label("loc_411A")

    Return()

    # Function_31_4105 end

    def Function_32_411B(): pass

    label("Function_32_411B")

    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4170")
    SetChrPos(0x101, 46000, 0, 45140, 90)
    SetChrPos(0x102, 45600, 0, 44220, 90)
    SetChrPos(0xF8, 44800, 0, 45140, 90)
    SetChrPos(0xF9, 44400, 0, 44220, 90)
    Jump("loc_41B4")

    label("loc_4170")

    SetChrPos(0x101, 55500, 0, 45140, 270)
    SetChrPos(0x102, 55900, 0, 44220, 270)
    SetChrPos(0xF8, 56700, 0, 45140, 270)
    SetChrPos(0xF9, 57100, 0, 44220, 270)

    label("loc_41B4")

    OP_69(0x101, 0x0)

    def lambda_41C1():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41C1)
    Sleep(30)

    def lambda_41DC():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41DC)
    Sleep(30)

    def lambda_41F7():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_41F7)
    Sleep(30)

    def lambda_4212():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4212)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4270")

    def lambda_422F():
        OP_6D(47500, 0, 44800, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_422F)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jump("loc_42B4")

    label("loc_4270")


    def lambda_4276():
        OP_6D(52500, 0, 44800, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4276)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    label("loc_42B4")

    OP_0D()
    WaitChrThread(0xD, 0x1)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4327")

    ChrTalk(    #215
        0x101,
        (
            "#1015F#2P啊……？\x02\x03",

            "怎么回事\x01",
            "这种地方为什么聚集了这么多人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_4327")


    ChrTalk(    #216
        0x101,
        (
            "#1011F#1P啊……？\x02\x03",

            "怎么回事\x01",
            "这种地方为什么聚集了这么多人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4369")

    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x102, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_43C2")

    ChrTalk(    #217
        0x102,
        (
            "#1043F#3P原来如此……\x02\x03",

            "#1035F……是这样吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F3")

    label("loc_43C2")


    ChrTalk(    #218
        0x102,
        (
            "#1043F#4P原来如此……\x02\x03",

            "#1035F……是这样吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F3")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_444D")

    ChrTalk(    #219
        0x101,
        "#1020F#2P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4438():
        OP_6D(47500, 8000, 35000, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4438)
    Jump("loc_447F")

    label("loc_444D")


    ChrTalk(    #220
        0x101,
        "#1020F#1P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_446D():
        OP_6D(52500, 8000, 35500, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_446D)

    label("loc_447F")


    def lambda_4485():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4485)
    Sleep(100)

    def lambda_4498():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4498)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x1)
    Sleep(1400)
    OP_AD(0x2400CD, 0x0, 0x0, 0xC8)
    Sleep(2500)
    FadeToBright(0, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #221
        (
            "#1020F浮、浮游都市……！？\x02\x03",

            "好、好巨大……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459F")
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #222
        "#065F浮、浮浮……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_459F")

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #223
        (
            "#1042F从地面上看\x01",
            "更能感到它的压迫力……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_468B")

    ChrTalk(    #224
        0x106,
        (
            "#053F对一般人来说，\x01",
            "感到不安也是正常的了。\x02\x03",

            "#050F这样的话，现在\x01",
            "正是需要我们游击士的时候。\x02\x03",

            "哪怕只能起到很微小的作用，\x01",
            "也要努力让市民们安心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476D")

    label("loc_468B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4718")

    ChrTalk(    #225
        0x103,
        (
            "#022F市民们会\x01",
            "感到不安也是当然的了。\x02\x03",

            "现在正是考验我们\x01",
            "游击士的时候啊。\x02\x03",

            "哪怕只能起到很微小的作用，\x01",
            "我们也要拿出全力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476D")

    label("loc_4718")


    ChrTalk(    #226
        0x108,
        (
            "#072F这样的话，市民们\x01",
            "会害怕也是当然的。\x02\x03",

            "在这种时候，\x01",
            "我们游击士就更要努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476D")


    ChrTalk(    #227
        0x101,
        "#1002F嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#1042F是啊……\x01",
            "快行动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20EA)
    EventEnd(0x0)
    Return()

    # Function_32_411B end

    def Function_33_47A6(): pass

    label("Function_33_47A6")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, 48500, 0, 49500, 180)
    SetChrPos(0x102, 47600, 250, 49900, 180)
    SetChrPos(0xF8, 48500, 250, 50700, 180)
    SetChrPos(0xF9, 47600, 250, 51100, 180)
    OP_69(0x101, 0x0)

    def lambda_4803():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4803)
    Sleep(30)

    def lambda_481E():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_481E)
    Sleep(30)

    def lambda_4839():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4839)
    Sleep(30)

    def lambda_4854():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4854)

    def lambda_486A():
        OP_6D(48220, 0, 47000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_486A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x1)
    OP_8C(0x101, 135, 400)

    def lambda_4898():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4898)
    Sleep(120)

    def lambda_48AB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_48AB)
    Sleep(60)

    def lambda_48BE():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_48BE)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #229
        0x101,
        (
            "#1015F#2P啊……？\x02\x03",

            "怎么回事\x01",
            "这种地方为什么聚集了这么多人……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x102, 180, 400)

    ChrTalk(    #230
        0x102,
        (
            "#1043F#3P原来如此……\x02\x03",

            "#1035F……是这样吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #231
        0x101,
        "#1020F#2P啊……！？\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_49B6():
        OP_6D(48220, 8000, 35000, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_49B6)

    def lambda_49CE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_49CE)
    Sleep(100)

    def lambda_49E1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_49E1)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x1)
    Sleep(1400)
    OP_AD(0x2400CD, 0x0, 0x0, 0xC8)
    Sleep(2500)
    FadeToBright(0, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #232
        (
            "#1020F浮、浮游都市……！？\x02\x03",

            "好、好巨大……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE8")
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #233
        "#065F浮、浮浮……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4AE8")

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #234
        (
            "#1042F从地面上看\x01",
            "更能感到它的压迫力……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD4")

    ChrTalk(    #235
        0x106,
        (
            "#053F对一般人来说，\x01",
            "感到不安也是正常的了。\x02\x03",

            "#050F这样的话，现在\x01",
            "正是需要我们游击士的时候。\x02\x03",

            "哪怕只能起到很微小的作用，\x01",
            "也要努力让市民们安心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB6")

    label("loc_4BD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C61")

    ChrTalk(    #236
        0x103,
        (
            "#022F市民们会\x01",
            "感到不安也是当然的了。\x02\x03",

            "现在正是考验我们\x01",
            "游击士的时候啊。\x02\x03",

            "哪怕只能起到很微小的作用，\x01",
            "我们也要拿出全力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB6")

    label("loc_4C61")


    ChrTalk(    #237
        0x108,
        (
            "#072F这样的话，市民们\x01",
            "会害怕也是当然的。\x02\x03",

            "在这种时候，\x01",
            "我们游击士就更要努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB6")


    ChrTalk(    #238
        0x101,
        "#1002F嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        (
            "#1042F是啊……\x01",
            "快行动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20EA)
    EventEnd(0x0)
    Return()

    # Function_33_47A6 end

    def Function_34_4CEF(): pass

    label("Function_34_4CEF")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DA6"),
        (1, "loc_4DAC"),
        (SWITCH_DEFAULT, "loc_4DB2"),
    )


    label("loc_4DA6")

    OP_A2(0x1200)
    Jump("loc_4DB2")

    label("loc_4DAC")

    OP_A2(0x1201)
    Jump("loc_4DB2")

    label("loc_4DB2")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_34_4CEF end

    def Function_35_4DEE(): pass

    label("Function_35_4DEE")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4E6B"),
        (1, "loc_4E71"),
        (SWITCH_DEFAULT, "loc_4E77"),
    )


    label("loc_4E6B")

    OP_A2(0x1200)
    Jump("loc_4E77")

    label("loc_4E71")

    OP_A2(0x1201)
    Jump("loc_4E77")

    label("loc_4E77")

    Return()

    # Function_35_4DEE end

    def Function_36_4E78(): pass

    label("Function_36_4E78")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_36_4E78 end

    def Function_37_4ED5(): pass

    label("Function_37_4ED5")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_37_4ED5 end

    def Function_38_4F2E(): pass

    label("Function_38_4F2E")

    SetPlaceName(0x2A)
    Return()

    # Function_38_4F2E end

    def Function_39_4F32(): pass

    label("Function_39_4F32")

    SetPlaceName(0x26)
    Return()

    # Function_39_4F32 end

    def Function_40_4F36(): pass

    label("Function_40_4F36")

    SetPlaceName(0x25)
    Return()

    # Function_40_4F36 end

    def Function_41_4F3A(): pass

    label("Function_41_4F3A")

    SetPlaceName(0x20)
    Return()

    # Function_41_4F3A end

    def Function_42_4F3E(): pass

    label("Function_42_4F3E")

    SetPlaceName(0x28)
    Return()

    # Function_42_4F3E end

    def Function_43_4F42(): pass

    label("Function_43_4F42")

    SetPlaceName(0x2B)
    Return()

    # Function_43_4F42 end

    def Function_44_4F46(): pass

    label("Function_44_4F46")

    SetPlaceName(0x21)
    Return()

    # Function_44_4F46 end

    def Function_45_4F4A(): pass

    label("Function_45_4F4A")

    SetPlaceName(0x27)
    Return()

    # Function_45_4F4A end

    SaveToFile()

Try(main)
