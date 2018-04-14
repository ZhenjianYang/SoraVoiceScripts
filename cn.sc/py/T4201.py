from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '卡西乌斯',                             # 9
        '雪拉扎德',                             # 10
        '怪盗布卢布兰',                         # 11
        '瘦狼瓦鲁特',                           # 12
        '歼灭天使玲',                           # 13
        '幻惑之铃露茜奥拉',                     # 14
        '艾莉茜雅女王',                         # 15
        '科洛蒂娅公主',                         # 16
        '基库',                                 # 17
        '希德中校',                             # 18
        '理查德',                               # 19
        '亲卫队队员',                           # 20
        '亲卫队队员',                           # 21
        '亲卫队队员',                           # 22
        '亲卫队队员',                           # 23
        '亲卫队队员',                           # 24
        '亲卫队队员',                           # 25
        '亲卫队队员',                           # 26
        '布卢布兰的短剑',                       # 27
        '怪盗布卢布兰的残像',                   # 28
        '怪盗布卢布兰的残像',                   # 29
        '瘦狼瓦鲁特的残像',                     # 30
        '瘦狼瓦鲁特的残像',                     # 31
        '歼灭天使玲的残像',                     # 32
        '歼灭天使玲的残像',                     # 33
        '幻惑之铃露茜奥拉的残像',               # 34
        '幻惑之铃露茜奥拉的残像',               # 35
        '亲卫队队员',                           # 36
        '亲卫队队员',                           # 37
    )

    DeclEntryPoint(
        Unknown_00              = -2780,
        Unknown_04              = 12000,
        Unknown_08              = 63200,
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH01320 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH01320P._CP',             # 02
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4210,
        Z                   = 18000,
        Y                   = 103250,
        Direction           = 183,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -4250,
        Z                   = 18000,
        Y                   = 103250,
        Direction           = 181,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = 27460,
        Y                   = 11000,
        Z                   = 81540,
        Range               = 32180,
        Unknown_10          = 0x34BC,
        Unknown_14          = 0x14190,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -1730,
        Y                   = 19160,
        Z                   = 107150,
        Range               = 1680,
        Unknown_10          = 0x55E6,
        Unknown_14          = 0x1A7A2,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = -32759,
        Y                   = 15500,
        Z                   = 76820,
        Range               = -35080,
        Unknown_10          = 0x4074,
        Unknown_14          = 0x116D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -4630,
        Y                   = 16000,
        Z                   = 86040,
        Range               = 4660,
        Unknown_10          = 0x2EE0,
        Unknown_14          = 0x14974,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    ScpFunction(
        "Function_0_4E2",          # 00, 0
        "Function_1_5DB",          # 01, 1
        "Function_2_6BF",          # 02, 2
        "Function_3_6D5",          # 03, 3
        "Function_4_794",          # 04, 4
        "Function_5_84F",          # 05, 5
        "Function_6_9A3",          # 06, 6
        "Function_7_9C6",          # 07, 7
        "Function_8_A37",          # 08, 8
        "Function_9_AA6",          # 09, 9
        "Function_10_18E7",        # 0A, 10
        "Function_11_1A0F",        # 0B, 11
        "Function_12_1C99",        # 0C, 12
        "Function_13_2608",        # 0D, 13
        "Function_14_2631",        # 0E, 14
        "Function_15_2661",        # 0F, 15
        "Function_16_267D",        # 10, 16
        "Function_17_26A3",        # 11, 17
        "Function_18_26F0",        # 12, 18
        "Function_19_2756",        # 13, 19
        "Function_20_27BC",        # 14, 20
        "Function_21_2822",        # 15, 21
        "Function_22_2888",        # 16, 22
        "Function_23_28EE",        # 17, 23
        "Function_24_2954",        # 18, 24
        "Function_25_2A0F",        # 19, 25
        "Function_26_2ACA",        # 1A, 26
        "Function_27_2B85",        # 1B, 27
        "Function_28_2C40",        # 1C, 28
        "Function_29_2CFB",        # 1D, 29
        "Function_30_2DB6",        # 1E, 30
        "Function_31_2E71",        # 1F, 31
        "Function_32_4E33",        # 20, 32
        "Function_33_4EA9",        # 21, 33
        "Function_34_4F17",        # 22, 34
        "Function_35_4F92",        # 23, 35
        "Function_36_5053",        # 24, 36
        "Function_37_50AE",        # 25, 37
        "Function_38_516B",        # 26, 38
        "Function_39_519D",        # 27, 39
        "Function_40_51B3",        # 28, 40
        "Function_41_5270",        # 29, 41
        "Function_42_53FE",        # 2A, 42
        "Function_43_546B",        # 2B, 43
        "Function_44_552D",        # 2C, 44
        "Function_45_55E6",        # 2D, 45
        "Function_46_566D",        # 2E, 46
        "Function_47_64BE",        # 2F, 47
        "Function_48_6506",        # 30, 48
        "Function_49_65C0",        # 31, 49
        "Function_50_667A",        # 32, 50
        "Function_51_6734",        # 33, 51
        "Function_52_67EE",        # 34, 52
        "Function_53_68A8",        # 35, 53
        "Function_54_6962",        # 36, 54
        "Function_55_6A1C",        # 37, 55
        "Function_56_6AD6",        # 38, 56
        "Function_57_6B5D",        # 39, 57
    )


    def Function_0_4E2(): pass

    label("Function_0_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4EC")
    Jump("loc_525")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_500")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_525")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_514")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_525")

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_525")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    SetChrPos(0x8, -43230, 16000, 80440, 270)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1)

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_570")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 10)
    Jump("loc_5DA")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_597")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    SetChrPos(0x101, 29990, 10500, 78720, 0)
    Event(0, 6)
    Jump("loc_5DA")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_5B3")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 46)
    Jump("loc_5DA")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5C9")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_5DA")

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DA")
    Event(0, 5)

    label("loc_5DA")

    Return()

    # Function_0_4E2 end

    def Function_1_5DB(): pass

    label("Function_1_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    OP_B1("t4201_y")
    Jump("loc_600")

    label("loc_5F7")

    OP_B1("t4201_n")

    label("loc_600")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_72(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_620")
    OP_6F(0x2, 0)
    Jump("loc_638")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_631")
    OP_6F(0x2, 450)
    Jump("loc_638")

    label("loc_631")

    OP_6F(0x2, 0)

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_652")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C3, 0x1, 0x50)

    label("loc_652")

    OP_71(0x1, 0x4)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68C")

    label("loc_683")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68C")

    SetMapFlags(0x2000000)
    OP_72(0x3, 0x10)
    OP_72(0x3, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_END)), "loc_6AC")
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)

    label("loc_6AC")

    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 11)

    label("loc_6B9")

    OP_71(0x0, 0x4)
    Return()

    # Function_1_5DB end

    def Function_2_6BF(): pass

    label("Function_2_6BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6BF")

    label("loc_6D4")

    Return()

    # Function_2_6BF end

    def Function_3_6D5(): pass

    label("Function_3_6D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6F6")

    ChrTalk(    #0
        0xFE,
        "前边是女王宫。\x02",
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #1
        0xFE,
        (
            "女王陛下现在正好\x01",
            "在房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "刚才好像在谒见室\x01",
            "听取了事件相关的报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(    #3
        0xFE,
        "这不是科洛蒂娅殿下吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "女王陛下现在\x01",
            "在房间里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790")

    TalkEnd(0xFE)
    Return()

    # Function_3_6D5 end

    def Function_4_794(): pass

    label("Function_4_794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7EB")

    ChrTalk(    #5
        0xFE,
        (
            "女王陛下和科洛蒂娅殿下\x01",
            "现在不在房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "我看见\x01",
            "她们两位出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84B")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_838")

    ChrTalk(    #7
        0xFE,
        (
            "『埃尔赛尤』好像已经\x01",
            "换上新的引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "真想早点见识一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84B")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(    #9
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    label("loc_84B")

    TalkEnd(0xFE)
    Return()

    # Function_4_794 end

    def Function_5_84F(): pass

    label("Function_5_84F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x1000)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10)
    SetChrFlags(0x101, 0x8)
    OP_77(0xE6, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(10, 12000, 28900, 0)
    OP_67(-10, 3030, -10000, 0)
    OP_6B(4780, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0xBB8)
    FadeToBright(2000, 0)
    Sleep(1000)

    def lambda_8DC():
        OP_6D(-13000, 16500, 75510, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DC)

    def lambda_8F4():
        OP_67(-8000, 5500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F4)

    def lambda_90C():
        OP_6C(45000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_90C)

    def lambda_91C():
        OP_6B(6000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_91C)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    def lambda_93B():
        OP_6D(150, 18500, 104610, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_93B)

    def lambda_953():
        OP_67(0, 7270, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_953)

    def lambda_96B():
        OP_6B(7610, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_96B)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_3E(0x35F, 1)
    FadeToDark(1500, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_84F end

    def Function_6_9A3(): pass

    label("Function_6_9A3")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x74EA, 0x2EE0, 0x144CE, 0x1388, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_9A3 end

    def Function_7_9C6(): pass

    label("Function_7_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A36")
    EventBegin(0x0)

    ChrTalk(    #10
        0x101,
        (
            "#002F（老爸一定知道\x01",
            "发生了什么事情……)\x02\x03",

            "(我必须尽快找到他……！)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A36")

    Return()

    # Function_7_9C6 end

    def Function_8_A37(): pass

    label("Function_8_A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA5")
    EventBegin(0x0)

    ChrTalk(    #11
        0x101,
        (
            "#002F（雪拉姐说，\x01",
            "老爸去了空中庭园……)\x02\x03",

            "(我必须先找到他……！)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_AA5")

    Return()

    # Function_8_A37 end

    def Function_9_AA6(): pass

    label("Function_9_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB3")
    Return()

    label("loc_AB3")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    SetChrSubChip(0x8, 0)
    ClearMapFlags(0x1)

    ChrTalk(    #12
        0x101,
        "#587F#5P啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)
    Sleep(200)

    def lambda_AE9():
        OP_6D(-41470, 16000, 79880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE9)

    def lambda_B01():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B01)

    def lambda_B19():
        OP_6B(1660, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B19)

    def lambda_B29():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B29)

    def lambda_B39():
        OP_6E(532, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_B39)
    Sleep(3000)

    ChrTalk(    #13
        0x8,
        "#1128F#6P艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#002F#6P老、老爸……\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0x8, 0x7D0, 0x1770, 0x0)

    ChrTalk(    #15
        0x101,
        "#005F啊，不好了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1125F#6P我知道……\x02\x03",

            "约修亚他……\x01",
            "走了是吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x1A)
    Sleep(500)

    ChrTalk(    #17
        0x101,
        (
            "#580F为、为什么……\x02\x03",

            "为什么老爸你会知道！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#1122F#6P昨天我参加完军事会议回来时，\x01",
            "你已经在床上睡着了。\x02\x03",

            "而桌子上就放着\x01",
            "他留下的字条。\x02\x03",

            "所以，大致情况我已经明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#005F那、那!!!\x02\x03",

            "那你为什么还在这里\x01",
            "优哉游哉的啊！？\x02\x03",

            "如果不早点去找约修亚的话──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "#1125F#6P……放弃吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#580F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#1122F#6P如果他真想要消失的话，\x01",
            "即使是我也不可能找到。\x02\x03",

            "５年前，在遭遇到他的刺杀时，\x01",
            "连我也都陷入了苦战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#587F……………………………\x02\x03",

            "…………我……直到今天……\x01",
            "一直都有个疑问……\x02\x03",

            "约修亚他……到底是什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "#1128F#6P……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 500)
    Sleep(500)

    ChrTalk(    #25
        0x8,
        (
            "#1125F#6P『噬身之蛇』——\x01",
            "集结着一群身份不明者的神秘组织。\x02\x03",

            "由名为『盟主』的首领所领导，\x01",
            "企图让世界陷入黑暗的结社。\x02\x03",

            "约修亚好像也是此组织的成员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#587F『噬身之蛇』………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1122F#6P坦白地说，连游击士协会也\x01",
            "无法掌握这个组织的真面目。\x02\x03",

            "考虑到对社会的影响，\x01",
            "一直对他们的存在遮遮掩掩。\x02\x03",

            "然而，这个组织确实存在着，\x01",
            "并企图完成某些不为人知的目的。\x02\x03",

            "……比如，类似这次的政变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#587F那、那就是说……\x02\x03",

            "是那个洛伦斯少尉搞的鬼？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1122F#6P嗯，错不了。\x02\x03",

            "不过，与此相关的人\x01",
            "绝不仅仅只是那个少尉。\x02\x03",

            "#1125F……从某种意义上来说，\x01",
            "约修亚也是他们的协助者之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        (
            "#580F等、等一下……\x02\x03",

            "这是什么意思！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#1125F#6P他在留言中写清了事实。\x02\x03",

            "约修亚在这５年间，\x01",
            "一直地把游击士协会的情报\x01",
            "提供给那个组织。\x02\x03",

            "但他却无法察觉到自己的行为，\x01",
            "好像受到了某些类似催眠术的心理暗示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#587F怎么会……\x02\x03",

            "#588F怎么会这样……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(500)

    ChrTalk(    #33
        0x8,
        (
            "#1122F#6P调查这个组织，不是你的力量能做到的。\x02\x03",

            "因此，不要再进一步介入了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#004F…………………………………\x02\x03",

            "#586F啊……\x01",
            "这是…什么意思……\x02\x03",

            "难道……\x01",
            "老爸的意思是说不要管约修亚了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "#1122F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#005F#3S喂！老爸！回答我！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1125F#6P我早就知道……\x01",
            "这一天迟早会到来。\x02\x03",

            "在５年前，约修亚\x01",
            "被我收为养子之时就知道了。\x02\x03",

            "他曾经和我做过一个约定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#587F什么约定……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1122F#6P当他认为自己的存在\x01",
            "会给我们带来困扰的时候……\x02\x03",

            "当他以某种形式重新接触到\x01",
            "自己身在结社的那段过去时……\x02\x03",

            "他便会从我们的面前消失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#587F…………………………………\x02\x03",

            "………………怎么会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#1128F#6P你的心情我能体会……\x02\x03",

            "同一屋檐下生活了多年的家人突然消失，\x01",
            "自然不可能那么简单就割舍掉吧。\x02\x03",

            "#1125F但是……\x01",
            "男人心中总会有一条不能退让的底线。\x02\x03",

            "#1122F所以，你也要理解\x01",
            "约修亚的心情──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#586F……你明明知道的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "#1122F#6P什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#586F你明明早就知道……\x01",
            "约修亚总有一天会\x01",
            "从我们的面前消失……\x02\x03",

            "老爸……你明明早就知道的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#1128F#6P…………………………\x02\x03",

            "#1125F………对不起……………\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -23950, 14000, 71460, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    Sleep(500)

    ChrTalk(    #46
        0x101,
        "#583F#4S老爸是大笨蛋！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_15F5():
        OP_8E(0x101, 0xFFFF88E6, 0x36B0, 0x1108A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15F5)

    def lambda_1610():
        OP_6D(-32960, 16000, 72720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1610)

    def lambda_1628():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1628)

    def lambda_1640():
        OP_8E(0x9, 0xFFFF8B98, 0x36B0, 0x11594, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1640)
    WaitChrThread(0x9, 0x0)

    def lambda_1660():
        OP_8E(0x9, 0xFFFF822E, 0x3C8C, 0x1205C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1660)
    Sleep(1000)

    def lambda_1680():
        OP_8E(0x101, 0xFFFFC702, 0x36B0, 0x12890, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1680)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 225, 400)
    OP_8C(0x9, 135, 400)
    Sleep(1000)
    Sleep(1000)
    OP_8C(0x9, 90, 400)
    Sleep(2000)
    TurnDirection(0x9, 0x8, 400)

    def lambda_16CB():
        OP_6D(-40820, 16000, 79520, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16CB)

    def lambda_16E3():
        OP_67(0, 7000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16E3)
    OP_8E(0x9, 0xFFFF63B6, 0x3E80, 0x131C8, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #47
        0x9,
        "#522F#5P老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#1122F#6P雪拉扎德……\x02\x03",

            "被你看到了难堪的场面啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#522F#5P不会…………\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "#1128F#6P不想斥责我几句吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#524F#5P我也……经历过类似的事情，\x01",
            "当时全靠老师的开导才重新振作……\x02\x03",

            "所以，老师和约修亚的心情\x01",
            "我都完全可以理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#1125F#6P是吗……这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#025F#5P但是，站在女性的立场上，\x01",
            "我还有一句话想说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        "#1124F#6P哦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        "#022F#5P老师和约修亚，你们都好差劲！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_AA6 end

    def Function_10_18E7(): pass

    label("Function_10_18E7")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, 6360, 12000, 92750, 0)
    OP_6D(-1460, 12000, 55280, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(9570, 0)
    OP_6C(21000, 0)
    OP_6E(350, 0)
    StopSound(0x7D00, 0x61A80, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0xBB8)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x493E0, 0x2710)

    def lambda_1989():
        OP_6D(750, 20000, 110490, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1989)

    def lambda_19A1():
        OP_67(0, 6120, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19A1)
    Sleep(1000)
    Sleep(1000)

    def lambda_19C3():
        OP_6B(8280, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_19C3)

    def lambda_19D3():
        OP_6C(33000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_19D3)

    def lambda_19E3():
        OP_6E(247, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19E3)
    WaitChrThread(0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_18E7 end

    def Function_11_1A0F(): pass

    label("Function_11_1A0F")

    LoadEffect(0x1, "map\\\\mpsmk0.eff")
    LoadEffect(0x2, "map\\\\mpfire2.eff")
    LoadEffect(0x3, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x46)
    OP_22(0xAE, 0x1, 0x46)
    PlayEffect(0x3, 0xFF, 0xFF, -170, 12000, 68500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 30580, 16500, 91210, 0, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6310, 22500, 89250, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 16200, 15000, 54000, 0, 0, 0, 1400, 1800, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -21680, 15000, 54280, 0, 0, 0, 1500, 1900, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -40400, 20400, 74600, 0, 0, 0, 1500, 1800, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -24100, 16700, 90680, 0, 0, 0, 1300, 1500, 1300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 30580, 16000, 91210, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 6310, 21950, 89250, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -40400, 19900, 74600, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, -24100, 16300, 90680, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_11_1A0F end

    def Function_12_1C99(): pass

    label("Function_12_1C99")

    EventBegin(0x0)
    OP_D2(0x2701C9, 0x2701CE, 0x3)
    OP_D2(0x270267, 0x270271, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x260052, 0x260057, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x27023F, 0x270249, 0x8)
    OP_D2(0x2701C8, 0x2701CD, 0x9)
    OP_D2(0x270253, 0x27025D, 0xA)
    OP_D2(0x600E8, 0x600ED, 0xB)
    OP_D2(0x600E7, 0x600EC, 0xC)
    OP_D2(0x2601BC, 0x2601C1, 0xD)
    OP_D2(0x2600A0, 0x2600A5, 0x22)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xD, 9)
    SetChrPos(0xA, 8600, 14000, 79010, 270)
    SetChrPos(0xC, 9600, 14000, 77740, 270)
    SetChrPos(0xD, 9800, 14000, 80570, 270)
    SetChrPos(0xB, 10800, 14000, 79250, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(8029, 14000, 79890, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    LoadEffect(0x0, "Craft\\\\cr161_00.eff")
    OP_43(0xA, 0x1, 0x0, 0xD)
    OP_43(0xC, 0x1, 0x0, 0xE)
    OP_43(0xD, 0x1, 0x0, 0xF)
    OP_43(0xB, 0x1, 0x0, 0x10)
    FadeToBright(1000, 0)

    def lambda_1DFD():
        OP_6D(-150, 14000, 82580, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DFD)

    def lambda_1E15():
        OP_67(0, 6170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E15)

    def lambda_1E2D():
        OP_6C(31000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E2D)

    def lambda_1E3D():
        OP_6B(3190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E3D)

    def lambda_1E4D():
        OP_6E(346, 3000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1E4D)
    WaitChrThread(0xD, 0x1)
    Sleep(1000)
    OP_6D(730, 20000, 109310, 4000)
    Sleep(500)

    ChrTalk(    #56
        0xA,
        (
            "#230F#5P呼……\x01",
            "那好像就是女王宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        "#240F#1P也就是终点呢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0xB,
        (
            "#250F#6P真是不费吹灰之力……\x02\x03",

            "只有那个老头子\x01",
            "还算有点实力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    ChrTalk(    #59
        0xD,
        (
            "#241F#2P呵呵，确实……\x01",
            "相当厉害的高手呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #60
        0xC,
        (
            "#269F#6P但想独自抵抗咱们四个人，\x01",
            "完全不可能有任何胜算嘛。\x02\x03",

            "#263F真是，做傻事也要适可而止啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    ChrTalk(    #61
        0xA,
        (
            "#230F#5P呵呵，话也不能这么说。\x02\x03",

            "所谓的高贵和忠义\x01",
            "就是指他这样的人。\x02\x03",

            "#231F另外那个杜南公爵\x01",
            "好像也和传闻中的有很大不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        (
            "#244F#2P是啊，并不像是个\x01",
            "放荡怯懦的人。\x02\x03",

            "#240F虽然只是轻轻碰一下\x01",
            "就晕过去了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 12)
    SetChrChipByIndex(0x14, 12)
    SetChrChipByIndex(0x15, 12)
    SetChrChipByIndex(0x16, 12)
    SetChrChipByIndex(0x17, 12)
    SetChrChipByIndex(0x18, 12)
    SetChrChipByIndex(0x19, 12)
    SetChrPos(0x13, 380, 20000, 112380, 180)
    SetChrPos(0x14, 380, 20000, 113380, 180)
    SetChrPos(0x15, 380, 20000, 111380, 180)
    SetChrPos(0x16, 380, 20000, 112380, 180)
    SetChrPos(0x17, 380, 20000, 112380, 180)
    SetChrPos(0x18, 380, 20000, 113380, 180)
    SetChrPos(0x19, 380, 20000, 111380, 180)

    ChrTalk(    #63
        0x13,
        "#4P来、来了……！\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(550, 20000, 108990, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(31000, 0)
    OP_6E(319, 0)

    def lambda_2214():
        OP_6D(250, 18000, 102900, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2214)
    OP_43(0x13, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x15, 0x1, 0x0, 0x13)
    Sleep(100)
    OP_43(0x16, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x17, 0x1, 0x0, 0x15)
    Sleep(100)
    OP_43(0x18, 0x1, 0x0, 0x16)
    Sleep(100)
    OP_43(0x19, 0x1, 0x0, 0x17)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #64
        0x18,
        (
            "#5P唔……\x01",
            "如果尤莉亚队长在就好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x15,
        (
            "#5P别说丧气话！\x01",
            "拿出亲卫队的气势来！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_8C(0xD, 0, 0)
    OP_8C(0xC, 0, 0)
    OP_8C(0xA, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xB,
        "#254F#6P哼……一帮杂鱼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        "#244F#4P……还真扫兴啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    Sleep(300)

    ChrTalk(    #68
        0xC,
        (
            "#261F#6P呵呵，是啊。\x02\x03",

            "#1306F不如我们来比赛好了，\x01",
            "看看是谁先抓到女王陛下？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23E9():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23E9)

    def lambda_23F7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_23F7)
    WaitChrThread(0xA, 0x1)
    Sleep(300)

    ChrTalk(    #69
        0xA,
        "#231F#5P哦～！这倒是挺有意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#252F哈哈哈，我当然奉陪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        "#241F#2P那么──我们就开始吧。\x02",
    )

    CloseMessageWindow()

    def lambda_2476():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2476)
    Sleep(100)

    def lambda_2489():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2489)
    Sleep(100)
    OP_8C(0xC, 0, 400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_24B1():
        OP_6D(390, 19000, 105520, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24B1)
    OP_7D(0x0, 0xA, 0xA, 0x64)
    OP_7D(0x0, 0xB, 0xA, 0x64)
    OP_7D(0x0, 0xC, 0xA, 0x64)
    OP_7D(0x0, 0xD, 0xA, 0x64)
    SetChrChipByIndex(0xA, 4)

    def lambda_24EE():
        OP_8E(0xFE, 0x1EA, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_24EE)
    Sleep(100)
    SetChrChipByIndex(0xC, 8)

    def lambda_2513():
        OP_8E(0xFE, 0xFFFFFB14, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2513)
    Sleep(100)
    SetChrChipByIndex(0xD, 10)

    def lambda_2538():
        OP_8E(0xFE, 0x514, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2538)
    Sleep(100)
    SetChrSubChip(0xB, 2)
    SetChrChipByIndex(0xB, 6)
    SetChrFlags(0xB, 0x20)

    def lambda_2567():
        OP_8E(0xFE, 0xFFFFFE2A, 0x4B32, 0x19EB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2567)
    OP_43(0x13, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x19)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x16, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0x17, 0x1, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x18, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0x19, 0x1, 0x0, 0x1E)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_7D(0x1, 0xA, 0x0, 0x0)
    OP_7D(0x1, 0xC, 0x0, 0x0)
    OP_7D(0x1, 0xB, 0x0, 0x0)
    OP_7D(0x1, 0xD, 0x0, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1C99 end

    def Function_13_2608(): pass

    label("Function_13_2608")

    OP_8E(0xFE, 0xA, 0x36B0, 0x13C40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF4C, 0x36B0, 0x141E0, 0x7D0, 0x0)
    Return()

    # Function_13_2608 end

    def Function_14_2631(): pass

    label("Function_14_2631")

    OP_8E(0xFE, 0xFFFFF9F2, 0x36B0, 0x13880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF9F2, 0x36B0, 0x13D12, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_2631 end

    def Function_15_2661(): pass

    label("Function_15_2661")

    OP_8E(0xFE, 0x500, 0x36B0, 0x13DEE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_2661 end

    def Function_16_267D(): pass

    label("Function_16_267D")

    OP_8E(0xFE, 0xFFFFFEF2, 0x36B0, 0x13894, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xB, 34)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_16_267D end

    def Function_17_26A3(): pass

    label("Function_17_26A3")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_26BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26BE)
    OP_8E(0xFE, 0x5A, 0x4650, 0x18CE0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_17_26A3 end

    def Function_18_26F0(): pass

    label("Function_18_26F0")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2710():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2710)
    OP_8E(0xFE, 0x398, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0x514, 0x4650, 0x18A06, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_18_26F0 end

    def Function_19_2756(): pass

    label("Function_19_2756")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2776():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2776)
    OP_8E(0xFE, 0xFFFFFBC8, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFA9C, 0x4650, 0x18A6A, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_19_2756 end

    def Function_20_27BC(): pass

    label("Function_20_27BC")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_27DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27DC)
    OP_8E(0xFE, 0xFFFFFFB0, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0x3F2, 0x4650, 0x1938E, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_20_27BC end

    def Function_21_2822(): pass

    label("Function_21_2822")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_2842():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2842)
    OP_8E(0xFE, 0xFFFFFFB0, 0x4E20, 0x1A09A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFDB2, 0x4650, 0x1917C, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_21_2822 end

    def Function_22_2888(): pass

    label("Function_22_2888")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_28A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28A8)
    OP_8E(0xFE, 0x398, 0x4E20, 0x1A450, 0x1388, 0x0)
    OP_8E(0xFE, 0x924, 0x4650, 0x19230, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_22_2888 end

    def Function_23_28EE(): pass

    label("Function_23_28EE")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_290E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_290E)
    OP_8E(0xFE, 0xFFFFFBC8, 0x4E20, 0x1A450, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF8EE, 0x4650, 0x193F2, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_23_28EE end

    def Function_24_2954(): pass

    label("Function_24_2954")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2964():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2964)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_29B9():
        OP_96(0xFE, 0xFFFFFD8A, 0x399E, 0x14D8E, 0x1388, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29B9)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_24_2954 end

    def Function_25_2A0F(): pass

    label("Function_25_2A0F")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2A1F():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A1F)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2A74():
        OP_96(0xFE, 0xAD2, 0x3C8C, 0x15342, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A74)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 6)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_25_2A0F end

    def Function_26_2ACA(): pass

    label("Function_26_2ACA")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2ADA():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ADA)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2B2F():
        OP_96(0xFE, 0xFFFFE9BC, 0x4650, 0x15662, 0x1770, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B2F)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 7)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_26_2ACA end

    def Function_27_2B85(): pass

    label("Function_27_2B85")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2B95():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B95)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2BEA():
        OP_96(0xFE, 0xB72, 0x4074, 0x179D0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BEA)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 1)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_27_2B85 end

    def Function_28_2C40(): pass

    label("Function_28_2C40")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2C50():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C50)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2CA5():
        OP_96(0xFE, 0xFFFFF646, 0x445C, 0x181BE, 0x1388, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2CA5)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 6)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_28_2C40 end

    def Function_29_2CFB(): pass

    label("Function_29_2CFB")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2D0B():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D0B)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2D60():
        OP_96(0xFE, 0x170C, 0x4650, 0x17958, 0x1B58, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2D60)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_29_2CFB end

    def Function_30_2DB6(): pass

    label("Function_30_2DB6")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 12)

    def lambda_2DC6():
        OP_94(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC6)
    Sleep(1300)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2E1B():
        OP_96(0xFE, 0xBC2, 0x4650, 0x18D9E, 0x1770, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E1B)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(300)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 3)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_30_2DB6 end

    def Function_31_2E71(): pass

    label("Function_31_2E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E83")
    Return()

    label("loc_2E83")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E9A")
    Call(0, 56)
    Call(0, 57)

    label("loc_2E9A")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(460, 14750, 85440, 0)
    OP_67(0, 4790, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(33000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, -580, 14750, 85180, 0)
    SetChrPos(0x102, 670, 14750, 85200, 0)
    SetChrPos(0xF8, -830, 14250, 84010, 0)
    SetChrPos(0xF9, 720, 14250, 84140, 0)
    OP_D2(0x2701C9, 0x2701CE, 0x3)
    OP_D2(0x270268, 0x270272, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x27022A, 0x270234, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x270240, 0x27024A, 0x8)
    OP_D2(0x2701C8, 0x2701CD, 0x9)
    OP_D2(0x270254, 0x27025E, 0xA)
    OP_D2(0x70141, 0x70145, 0xB)
    OP_D2(0x260052, 0x260057, 0xC)
    OP_D2(0x70182, 0x70186, 0xD)
    OP_D2(0x2702F0, 0x2702FA, 0xE)
    OP_D2(0x27026B, 0x270275, 0xF)
    OP_D2(0x260068, 0x26006D, 0x10)
    OP_D2(0x704AA, 0x704AE, 0x11)
    OP_D2(0x70180, 0x70184, 0x12)
    OP_D2(0x2702EA, 0x2702F4, 0x13)
    OP_D2(0x2702EB, 0x2702F5, 0x14)
    OP_D2(0x2702EC, 0x2702F6, 0x15)
    OP_D2(0x702D2, 0x702D9, 0x16)
    OP_D2(0x702D3, 0x702DA, 0x17)
    OP_D2(0x702D4, 0x702DB, 0x18)
    OP_D2(0x7052B, 0x7052F, 0x19)
    OP_D2(0x270110, 0x270120, 0x1A)
    OP_D2(0x270111, 0x270121, 0x1B)
    OP_D2(0x270130, 0x270140, 0x1C)
    OP_D2(0x270131, 0x270141, 0x1D)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_304D"),
        (2, "loc_3064"),
        (6, "loc_307B"),
        (7, "loc_3092"),
        (SWITCH_DEFAULT, "loc_30A9"),
    )


    label("loc_304D")

    OP_D2(0x70218, 0x70224, 0x1E)
    OP_D2(0x70219, 0x70225, 0x1F)
    Jump("loc_30A9")

    label("loc_3064")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    OP_D2(0x701D1, 0x701DD, 0x1F)
    Jump("loc_30A9")

    label("loc_307B")

    OP_D2(0x70230, 0x7023C, 0x1E)
    OP_D2(0x70231, 0x7023D, 0x1F)
    Jump("loc_30A9")

    label("loc_3092")

    OP_D2(0x70248, 0x70254, 0x1E)
    OP_D2(0x70249, 0x70255, 0x1F)
    Jump("loc_30A9")

    label("loc_30A9")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_30C2"),
        (2, "loc_30D9"),
        (6, "loc_30F0"),
        (7, "loc_3107"),
        (SWITCH_DEFAULT, "loc_311E"),
    )


    label("loc_30C2")

    OP_D2(0x70218, 0x70224, 0x20)
    OP_D2(0x70219, 0x70225, 0x21)
    Jump("loc_311E")

    label("loc_30D9")

    OP_D2(0x701D0, 0x701DC, 0x20)
    OP_D2(0x701D1, 0x701DD, 0x21)
    Jump("loc_311E")

    label("loc_30F0")

    OP_D2(0x70230, 0x7023C, 0x20)
    OP_D2(0x70231, 0x7023D, 0x21)
    Jump("loc_311E")

    label("loc_3107")

    OP_D2(0x70248, 0x70254, 0x20)
    OP_D2(0x70249, 0x70255, 0x21)
    Jump("loc_311E")

    label("loc_311E")

    OP_D2(0x2600A0, 0x2600A5, 0x22)
    OP_D2(0x2600AE, 0x2600B3, 0x23)
    OP_D2(0x26008F, 0x260094, 0x24)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    LoadEffect(0x4, "Craft\\\\cr161_00.eff")
    SoundLoad(163)
    SoundLoad(164)
    SoundLoad(503)
    SoundLoad(505)
    SoundLoad(571)
    SoundLoad(155)
    SoundLoad(214)
    SoundLoad(213)
    OP_0D()
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 34)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 11)
    SetChrChipByIndex(0xF, 13)
    SetChrPos(0xC, -1510, 18000, 102060, 180)
    SetChrPos(0xA, -220, 18000, 100200, 180)
    SetChrPos(0xB, 890, 18000, 103470, 180)
    SetChrPos(0xD, 1820, 18000, 101280, 180)
    SetChrPos(0xE, -290, 18000, 101770, 180)
    SetChrPos(0xF, 850, 18000, 101660, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    FadeToBright(500, 0)
    OP_0D()

    NpcTalk(    #72
        0xA,
        "男人的声音",
        "#4P哟……是你们啊。\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B3")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32F1")

    label("loc_32B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DA")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32F1")

    label("loc_32DA")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_32F1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331D")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_335B")

    label("loc_331D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3344")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_335B")

    label("loc_3344")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_335B")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_336D():
        OP_6D(850, 18000, 103170, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_336D)

    def lambda_3385():
        OP_67(0, 4930, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3385)

    def lambda_339D():
        OP_6B(2410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_339D)

    def lambda_33AD():
        OP_6C(23000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_33AD)

    def lambda_33BD():
        OP_8F(0xFE, 0xFFFFFF24, 0x3E80, 0x16986, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33BD)
    Sleep(100)

    def lambda_33DD():
        OP_8F(0xFE, 0x3CA, 0x3E80, 0x16968, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33DD)
    Sleep(50)

    def lambda_33FD():
        OP_8F(0xFE, 0xFFFFFEFC, 0x3E80, 0x1631E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_33FD)
    Sleep(100)

    def lambda_341D():
        OP_8F(0xFE, 0x3B6, 0x3E80, 0x1631E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_341D)
    WaitChrThread(0x101, 0x0)
    Sleep(100)

    ChrTalk(    #73
        0x101,
        "#1020F#1P科洛丝！　女王陛下！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 26)
    SetChrChipByIndex(0x102, 28)
    SetChrChipByIndex(0xF8, 30)
    SetChrChipByIndex(0xF9, 32)

    ChrTalk(    #74
        0xF,
        (
            "#403F#5P艾丝蒂尔……\x01",
            "……约修亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "#093F#5P各位……\x01",
            "你们终于来了啊…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34ED")

    ChrTalk(    #76
        0x107,
        "#065F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3558")

    label("loc_34ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3511")

    ChrTalk(    #77
        0x106,
        "#057F可恶……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3558")

    label("loc_3511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3537")

    ChrTalk(    #78
        0x103,
        "#523F怎么会……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3558")

    label("loc_3537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3558")

    ChrTalk(    #79
        0x108,
        "#077F可恶……\x02",
    )

    CloseMessageWindow()

    label("loc_3558")


    ChrTalk(    #80
        0x102,
        "#1043F……还是没能赶上吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1005F#1P你、你们……\x01",
            "到底想干什么！？\x02\x03",

            "马上放了科洛丝她们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xC,
        (
            "#1306F#5P呵呵，这可不行。\x02\x03",

            "#261F因为教授向我们提了\x01",
            "私人性质的请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1020F#1P教、教授？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        (
            "#1042F私人的……\x01",
            "就是说和『福音计划』无关吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        (
            "#263F#5P呵呵，应该是吧。\x02\x03",

            "#1305F各位表现得比\x01",
            "预期的要活跃，\x01",
            "所以他要想些办法来试验你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#1019F#1P活、活跃……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(    #87
        0xB,
        (
            "#252F#5P哼哼，你们恢复了\x01",
            "各地的通讯吧？\x02\x03",

            "教授似乎对此\x01",
            "很是不满哦！\x02\x03",

            "所以就想看看你们\x01",
            "手足无措的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B6")

    label("loc_3744")


    ChrTalk(    #88
        0xD,
        (
            "#244F#5P你们恢复了各地的\x01",
            "部分通讯吧……\x02\x03",

            "#241F教授似乎对此\x01",
            "有些扫兴呢。\x02\x03",

            "所以就想看看你们\x01",
            "痛苦困惑的样子哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B6")


    ChrTalk(    #89
        0x101,
        (
            "#1005F#1P…………！\x01",
            "开、开什么玩笑！\x02\x03",

            "难道你们因为这种理由\x01",
            "就来袭击王都！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1043F……他本来就是这种人。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(    #91
        0xD,
        (
            "#244F#5P呵呵……\x01",
            "算是恶趣味吧。\x02\x03",

            "#241F浮游都市的控制\x01",
            "已经交给莱维一个人了。\x02\x03",

            "我们实在闲得太无聊，\x01",
            "就接受了教授的提议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        "#022F露茜奥拉姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3979")

    label("loc_38D1")


    ChrTalk(    #93
        0xB,
        (
            "#250F哼哼……\x01",
            "确实是种恶趣味。\x02\x03",

            "#252F浮游都市的控制\x01",
            "全部都交给莱维一人了。\x02\x03",

            "我们几个闲着也是闲着，\x01",
            "就来这里运动运动。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3979")

    ChrTalk(    #94
        0x108,
        "#077F瓦鲁特……你这家伙。\x02",
    )

    CloseMessageWindow()

    label("loc_3979")


    ChrTalk(    #95
        0xE,
        (
            "#094F#5P……我明白了。\x02\x03",

            "#093F那么只要我一个人\x01",
            "成为阶下囚就行了吧。\x02\x03",

            "能不能请你们\x01",
            "放过科洛蒂娅？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 270, 400)

    ChrTalk(    #96
        0xF,
        (
            "#402F#2P这样不行，祖母大人！\x02\x03",

            "要抓的话也应该抓我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "#230F#5P嗯，教授的要求\x01",
            "确实是“只要抓住一个就好”……\x02\x03",

            "哎呀呀，那该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)

    ChrTalk(    #98
        0xD,
        (
            "#243F#2P对了，你不是\x01",
            "很迷恋公主殿下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(300)

    ChrTalk(    #99
        0xA,
        (
            "#231F#6P呵呵，美丽的鸟儿一旦被囚禁\x01",
            "在笼中，就失去了原本的魅力。\x02\x03",

            "不过我倒是也很想欣赏一下她那\x01",
            "身陷在囚笼中也坚韧不屈的气质……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)
    Sleep(300)

    ChrTalk(    #100
        0xF,
        "#402F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1022F#1P你、你们……\x01",
            "给我适可而止吧！！\x02\x03",

            "#1005F这种事……\x01",
            "我绝不会让你们得逞！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3BC3)
    Sleep(50)

    def lambda_3BD6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3BD6)
    Sleep(50)

    def lambda_3BE9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3BE9)

    ChrTalk(    #102
        0xB,
        (
            "#252F#5P哼哼，别说笑了。\x02\x03",

            "就算没有人质，\x01",
            "你觉得能战胜我们所有人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        (
            "#261F#5P呵呵，上次咱们\x01",
            "曾有过约定，再度见面时\x01",
            "要把你们杀光，对吧？\x02\x03",

            "#1306F现在正是好机会……\x01",
            "要不要就在这里开始呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1020F#1P可恶……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(670, 16000, 93270, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(23000, 0)
    OP_6E(359, 0)
    SetChrPos(0x101, -220, 16000, 92550, 328)
    SetChrPos(0x102, 970, 16000, 92520, 328)
    SetChrPos(0xF8, -260, 16000, 90910, 328)
    SetChrPos(0xF9, 950, 16000, 90910, 328)
    OP_0D()

    ChrTalk(    #105
        0x102,
        (
            "#1035F#2P（……要克制，艾丝蒂尔。）\x02\x03",

            "#1042F（他说得没错……\x01",
            "双方的战斗力确实存在差距。）\x02\x03",

            "（现在也只有耐心寻找胜机了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1003F#5P（可、可是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "#231F#6P呵呵，没用的，约修亚。\x02\x03",

            "凭你的隐形术，或许真的\x01",
            "可以发现我们的破绽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "#240F#6P但如今你已经现形，\x01",
            "再想找出我们的破绽根本是不可能的。\x02\x03",

            "就算是你『漆黑之牙』也一样无能为力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1035F#4P……确实如此。\x02\x03",

            "#1040F不过，制造破绽的工作\x01",
            "也不一定要我来做啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)

    ChrTalk(    #110
        0xA,
        "#232F#6P什么……\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10)
    Sleep(100)
    OP_1D(0x2C)
    Sleep(500)
    Fade(500)
    OP_6D(-3840, 18000, 103030, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 4)
    SetChrPos(0x11, -14000, 18000, 101730, 90)
    ClearChrFlags(0x11, 0x80)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0x21)
    Sleep(400)
    OP_43(0xC, 0x0, 0x0, 0x22)

    def lambda_3FAF():
        OP_6D(-2250, 18000, 102720, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FAF)

    def lambda_3FC7():
        OP_67(0, 4650, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FC7)

    def lambda_3FDF():
        OP_6B(2420, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FDF)
    OP_43(0xE, 0x0, 0x0, 0x24)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0xC, 0x0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0xC, 0x20)
    OP_22(0x9B, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xC, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)

    def lambda_405A():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_405A)

    def lambda_4074():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4074)

    def lambda_408E():
        OP_6E(391, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_408E)

    def lambda_409E():
        OP_96(0xFE, 0xFFFFFB6E, 0x4650, 0x19118, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_409E)

    def lambda_40BC():
        OP_96(0xFE, 0xFFFFE746, 0x4650, 0x18F06, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_40BC)
    WaitChrThread(0x11, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xC, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    OP_43(0xA, 0x0, 0x0, 0x23)
    Sleep(300)
    SetChrChipByIndex(0x11, 19)
    SetChrSubChip(0x11, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x11, 0xA, 0x64)
    OP_96(0x11, 0xFFFFE57A, 0x4650, 0x188DA, 0xC8, 0x1770)
    OP_7D(0x1, 0x11, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xA, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(    #111
        0x101,
        "#1004F#1P哎……！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #112
        0x11,
        (
            "#701F#5P哟，大家辛苦了。\x02\x03",

            "#703F……陛下、殿下。\x01",
            "我来晚了，请恕罪。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-1270, 18000, 103090, 800)

    ChrTalk(    #113
        0xF,
        "#409F#2P希德中校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        "#090F#2P……你来得正好。\x02",
    )

    CloseMessageWindow()
    Fade(225)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #115
        0xA,
        (
            "#230F#2P喔……\x01",
            "是『剑圣』的传人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        (
            "#1306F#5P呵呵……真可惜。\x02\x03",

            "只差一点点就能\x01",
            "抓住玲的破绽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        (
            "#701F嗯，我确实很受打击啊。\x02\x03",

            "#703F没想到全力施展的偷袭\x01",
            "都奈何不了你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#252F#5P哼哼，已经算是不错了。\x02\x03",

            "难得的好机会，不如和我们\x01",
            "好好玩一玩吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x11,
        (
            "#703F多谢你的好意，不过不必了。\x02\x03",

            "#701F我的任务不过只是\x01",
            "吸引你们的注意力而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        "#254F#5P什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        "#242F！！！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 18)
    SetChrPos(0x10, -15190, 21000, 88030, 45)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x80)
    OP_22(0x197, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2590, 18000, 100370, 800)
    OP_43(0x10, 0x0, 0x0, 0x28)

    def lambda_43E3():
        OP_6D(2640, 18000, 103890, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_43E3)

    def lambda_43FB():
        OP_67(0, 6720, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43FB)

    def lambda_4413():
        OP_6B(2170, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4413)

    def lambda_4423():
        OP_6C(21000, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4423)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #122
        0xD,
        "#245F#5P…………\x02",
    )

    CloseMessageWindow()
    OP_43(0x12, 0x0, 0x0, 0x29)

    def lambda_445A():
        OP_6D(1730, 18750, 105300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_445A)

    def lambda_4472():
        OP_67(0, 6520, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4472)

    def lambda_448A():
        OP_6B(2170, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_448A)

    def lambda_449A():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_449A)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #123
        0xB,
        "#259F#6P哼……\x02",
    )

    CloseMessageWindow()

    def lambda_44C8():
        OP_6D(-2940, 18610, 101150, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44C8)

    def lambda_44E0():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44E0)

    def lambda_44F0():
        OP_6E(300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44F0)
    Sleep(1000)
    OP_43(0x11, 0x0, 0x0, 0x25)
    WaitChrThread(0x11, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0xC, 0x32, 0x64)
    OP_7D(0x0, 0xA, 0x32, 0x64)

    def lambda_4526():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4526)

    def lambda_4534():
        OP_96(0xFE, 0xFFFFF90C, 0x474A, 0x19668, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4534)

    def lambda_4552():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_4552)

    def lambda_4560():
        OP_96(0xFE, 0xFFFFF98E, 0x4650, 0x18632, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4560)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #124 op#A op#5
        0xA,
        "#235F#10A#4P唔……\x05\x02",
    )


    ChrTalk(    #125 op#A op#5
        0xC,
        "#1303F#10A#1P呀……\x05\x02",
    )

    Sleep(800)
    OP_7D(0x0, 0x11, 0x32, 0x64)
    OP_8C(0x11, 0, 800)
    SetChrChipByIndex(0x11, 21)

    def lambda_45D2():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_45D2)

    def lambda_45E2():
        OP_96(0xFE, 0xFFFFF808, 0x4650, 0x1930C, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_45E2)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_460F():
        OP_96(0xFE, 0xFFFFFA06, 0x4D26, 0x1A2D4, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_460F)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 180, 800)

    def lambda_4648():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4648)

    def lambda_4658():
        OP_96(0xFE, 0xFFFFF93E, 0x4650, 0x189DE, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4658)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0xA, 0x32, 0x1F4)
    SetChrChipByIndex(0xA, 36)

    def lambda_4692():

        label("loc_4692")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4692")

    QueueWorkItem2(0xA, 2, lambda_4692)

    def lambda_46A5():
        OP_96(0xFE, 0xFFFFF920, 0x5208, 0x17E08, 0xDAC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_46A5)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0xA, 0x1)
    OP_7D(0x1, 0xA, 0x0, 0x0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 0)

    def lambda_46F2():

        label("loc_46F2")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_46F2")

    QueueWorkItem2(0x11, 2, lambda_46F2)
    OP_43(0xA, 0x0, 0x0, 0x2D)
    Sleep(2000)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 23)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 20)

    def lambda_4723():
        OP_8F(0xFE, 0x104, 0x4650, 0x18F38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4723)

    def lambda_473E():
        OP_8F(0xFE, 0xFFFFFB3C, 0x4650, 0x18CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_473E)

    def lambda_4759():
        OP_8F(0xE, 0xFFFFFD62, 0x4650, 0x187EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4759)

    def lambda_4774():
        OP_8F(0xF, 0x21C, 0x4650, 0x188DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4774)

    def lambda_478F():
        OP_6D(960, 18500, 104830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_478F)

    def lambda_47A7():
        OP_67(0, 5600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47A7)

    def lambda_47BF():
        OP_6B(2910, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47BF)

    def lambda_47CF():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47CF)

    def lambda_47DF():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47DF)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 19)
    SetChrSubChip(0x11, 0)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0xC, 0x0, 0x0)
    OP_7D(0x1, 0xA, 0x0, 0x0)

    NpcTalk(    #126
        0x12,
        "穿军服的男人",
        "#115F#5P看来我来得正好啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xF,
        "#409F你、你是……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 1700, 16000, 92550, 328)
    SetChrPos(0x102, 2910, 16000, 92520, 328)
    SetChrPos(0xF8, 1700, 16000, 90910, 328)
    SetChrPos(0xF9, 2910, 16000, 90910, 328)

    def lambda_48AC():
        OP_6D(1120, 18500, 104420, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48AC)

    def lambda_48C4():
        OP_67(0, 6140, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_48C4)

    def lambda_48DC():
        OP_6B(2360, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48DC)

    def lambda_48EC():
        OP_6E(401, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_48EC)
    SetChrChipByIndex(0x101, 26)

    def lambda_4901():
        OP_8E(0xFE, 0x6A4, 0x4650, 0x18EA2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4901)
    Sleep(100)
    SetChrChipByIndex(0x102, 28)

    def lambda_4926():
        OP_8E(0xFE, 0xB5E, 0x4650, 0x18EB6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4926)
    Sleep(50)
    SetChrChipByIndex(0xF8, 30)

    def lambda_494B():
        OP_8E(0xFE, 0x6E0, 0x4650, 0x18894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_494B)
    Sleep(100)
    SetChrChipByIndex(0xF9, 32)

    def lambda_4970():
        OP_8E(0xFE, 0xB2C, 0x4650, 0x18894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4970)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 26)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 28)
    WaitChrThread(0xF8, 0x1)
    SetChrChipByIndex(0xF8, 30)
    WaitChrThread(0xF9, 0x1)
    SetChrChipByIndex(0xF9, 32)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D3")

    ChrTalk(    #128
        0x106,
        "#055F喂喂……\x02",
    )

    CloseMessageWindow()

    label("loc_49D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F4")

    ChrTalk(    #129
        0x107,
        "#065F啊……？\x02",
    )

    CloseMessageWindow()

    label("loc_49F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A17")

    ChrTalk(    #130
        0x103,
        "#023F不是吧……\x02",
    )

    CloseMessageWindow()

    label("loc_4A17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A3A")

    ChrTalk(    #131
        0x108,
        "#073F怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_4A3A")


    ChrTalk(    #132
        0x101,
        "#1004F#5P理、理、理……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #133
        0x101,
        "#1005F#4S#5P理查德上校！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #134
        0x12,
        (
            "#111F#5P哈哈……\x01",
            "别来无恙吗，艾丝蒂尔。\x02\x03",

            "#110F不过现在的我已经被剥夺了军衔，\x01",
            "不过是个服刑中的政治犯罢了。\x02\x03",

            "所以就不要再叫我上校啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1019F#5P不、不要叫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "#096F#6P理查德先生。\x01",
            "……真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#115F#5P……陛下和公主殿下\x01",
            "能够安康真是太好了。\x02\x03",

            "#112F我想准将应该已经\x01",
            "向您禀报过了……\x02\x03",

            "请允许我暂时以带罪之身，\x01",
            "保护陛下和公主脱离逆贼之手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        "#091F#6P呵呵，那是当然的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xF,
        "#401F#4P拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#111F#5P……荣幸之至。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1016F#5P这、这是怎么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#1040F#2P看来在我们不知情的情况下，\x01",
            "事态已经有所进展了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "#232F#6P『剑圣』的两名传人……\x02\x03",

            "再加上『漆黑之牙』和\x01",
            "本领高强的游击士们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "#240F#6P呵呵……\x01",
            "看来是稍微有些玩过头了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x12,
        (
            "#115F#6P呼……\x01",
            "现在的情势已经逆转了哦，\x02\x03",

            "#111F顺便一说，街上的那群家伙\x01",
            "我们也已经收拾掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1004F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    def lambda_4DAF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DAF)
    Sleep(50)

    def lambda_4DC2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DC2)
    Sleep(50)

    def lambda_4DD5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4DD5)
    Sleep(50)

    def lambda_4DE8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4DE8)
    Sleep(50)
    SetChrFlags(0xF, 0x20)

    def lambda_4E00():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4E00)

    def lambda_4E0E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4E0E)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_2E71 end

    def Function_32_4E33(): pass

    label("Function_32_4E33")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 13300, 23000, 107640, 225)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x10, 18)
    OP_8E(0x10, 0x550, 0x4C2C, 0x189C0, 0xFA0, 0x0)
    OP_8C(0x10, 315, 300)
    Sleep(500)
    OP_8F(0x10, 0x3D4, 0x477C, 0x189B6, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x10, 850, 18300, 100700, 3000)
    SetChrChipByIndex(0xF, 15)
    OP_0D()
    Return()

    # Function_32_4E33 end

    def Function_33_4EA9(): pass

    label("Function_33_4EA9")

    OP_7D(0x0, 0x11, 0x32, 0x64)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 20)
    OP_8E(0x11, 0xFFFFE804, 0x4650, 0x18F06, 0x2710, 0x0)
    OP_22(0x23B, 0x0, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)

    def lambda_4EE4():
        OP_8F(0xFE, 0xFFFFF038, 0x490C, 0x18D8A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4EE4)

    def lambda_4EFF():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EFF)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_33_4EA9 end

    def Function_34_4F17(): pass

    label("Function_34_4F17")

    OP_8C(0xFE, 270, 500)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_4F2E():
        OP_99(0xFE, 0xD, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F2E)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 8)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0xFE, 0x32, 0x64)
    ClearChrFlags(0xFE, 0x20)

    def lambda_4F5A():
        OP_8F(0xFE, 0xFFFFF614, 0x490C, 0x18EB6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F5A)
    Sleep(200)

    def lambda_4F7A():
        OP_99(0xFE, 0x7, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F7A)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_34_4F17 end

    def Function_35_4F92(): pass

    label("Function_35_4F92")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 4)

    def lambda_4FAA():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FAA)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_4FC4():
        OP_99(0xFE, 0x3, 0x6, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FC4)

    def lambda_4FD4():
        OP_96(0xFE, 0xFFFFF8E4, 0x4650, 0x189F2, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4FD4)
    Sleep(100)
    SetChrChipByIndex(0x1A, 35)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x1A, -1820, 18500, 100850, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x40)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_5026():
        OP_8F(0xFE, 0xFFFFE250, 0x4650, 0x18D94, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5026)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0x1A, 1)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_35_4F92 end

    def Function_36_5053(): pass

    label("Function_36_5053")


    def lambda_5059():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5059)
    Sleep(50)

    def lambda_506C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_506C)
    Sleep(50)

    def lambda_507F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_507F)
    Sleep(50)

    def lambda_5092():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5092)
    Sleep(50)

    def lambda_50A5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_50A5)
    Return()

    # Function_36_5053 end

    def Function_37_50AE(): pass

    label("Function_37_50AE")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)

    def lambda_50D0():
        OP_99(0xFE, 0x1, 0x4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50D0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFEEB2, 0x4A38, 0x18628, 0x3E8, 0x1388)

    def lambda_50FC():
        OP_8E(0xFE, 0xFFFFEEB2, 0x4650, 0x18628, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_50FC)
    OP_44(0xFE, 0x1)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0xFE, 0)

    def lambda_5125():
        OP_6D(-680, 18000, 102860, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5125)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFF5D8, 0x4650, 0x18DC6, 0x1F4, 0x1388)
    SetChrSubChip(0xFE, 1)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_37_50AE end

    def Function_38_516B(): pass

    label("Function_38_516B")

    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrPos(0xA, -1270, 18000, 101310, 270)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
    Return()

    # Function_38_516B end

    def Function_39_519D(): pass

    label("Function_39_519D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B2")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_39_519D")

    label("loc_51B2")

    Return()

    # Function_39_519D end

    def Function_40_51B3(): pass

    label("Function_40_51B3")


    def lambda_51B9():

        label("loc_51B9")

        TurnDirection(0xD, 0x10, 400)
        OP_48()
        Jump("loc_51B9")

    QueueWorkItem2(0xD, 1, lambda_51B9)
    OP_43(0x10, 0x1, 0x0, 0x27)
    OP_7D(0x0, 0xFE, 0x32, 0x64)
    OP_8F(0xFE, 0x898, 0x4970, 0x18C4A, 0x6D60, 0x0)
    SetChrChipByIndex(0xD, 10)
    SetChrSubChip(0xD, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_51FC():
        OP_96(0xFE, 0x9B0, 0x4650, 0x194BA, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_51FC)
    OP_8F(0xFE, 0x2670, 0x5D48, 0x1A5D6, 0x3E80, 0x0)
    OP_7D(0x1, 0x10, 0x0, 0x0)
    SetChrFlags(0xFE, 0x80)
    WaitChrThread(0xD, 0x1)

    def lambda_5240():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_5240)
    Sleep(100)

    def lambda_5253():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_5253)
    Sleep(100)
    OP_8C(0xE, 180, 400)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_40_51B3 end

    def Function_41_5270(): pass

    label("Function_41_5270")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrChipByIndex(0x12, 23)
    SetChrPos(0x12, 10480, 18000, 96630, 315)
    SetChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)
    OP_8E(0x12, 0x198C, 0x4650, 0x18222, 0x2710, 0x0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_52B7():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_52B7)
    OP_96(0x12, 0x8F2, 0x4650, 0x1883A, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_52E1():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_52E1)
    SetChrChipByIndex(0x12, 24)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x12, 0x1)

    def lambda_52FE():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52FE)

    def lambda_530E():
        OP_99(0xFE, 0x0, 0x9, 0xDAC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_530E)

    def lambda_531E():
        OP_8F(0xFE, 0x960, 0x4650, 0x19258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_531E)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xD, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)

    def lambda_5389():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_5389)

    def lambda_53A3():
        OP_9E(0xFE, 0x1E, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_53A3)
    OP_43(0xD, 0x1, 0x0, 0x2A)
    OP_8C(0xB, 90, 800)
    SetChrChipByIndex(0xB, 6)
    SetChrSubChip(0xB, 0)
    OP_43(0x12, 0x2, 0x0, 0x2C)
    OP_43(0xB, 0x0, 0x0, 0x2B)
    OP_8C(0xF, 0, 400)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0xB, 0x0)
    WaitChrThread(0x12, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_41_5270 end

    def Function_42_53FE(): pass

    label("Function_42_53FE")

    OP_7D(0x0, 0xFE, 0x32, 0x64)

    def lambda_540C():
        OP_99(0xFE, 0x9, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_540C)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x91A, 0x493E, 0x19BB8, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x820, 0x4C2C, 0x1A1EE, 0x5DC, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_42_53FE end

    def Function_43_546B(): pass

    label("Function_43_546B")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5488():
        OP_8C(0xFE, 135, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5488)
    OP_96(0xFE, 0x10E, 0x474A, 0x197D0, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_54BC():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54BC)
    OP_96(0xFE, 0x3F2, 0x493E, 0x19B40, 0x1F4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0x212, 0x4D26, 0x1A374, 0x5DC, 0xFA0)
    SetChrSubChip(0xFE, 1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_43_546B end

    def Function_44_552D(): pass

    label("Function_44_552D")

    OP_7D(0x0, 0xFE, 0x32, 0x64)
    SetChrFlags(0xFE, 0x20)
    OP_8C(0x12, 270, 800)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 2)

    def lambda_5551():
        OP_96(0xFE, 0x6D6, 0x4650, 0x19442, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5551)
    OP_99(0xFE, 0x3, 0x5, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 315, 800)

    def lambda_5584():
        OP_96(0xFE, 0x47E, 0x4650, 0x19618, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5584)
    OP_99(0xFE, 0x6, 0x8, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 0, 800)

    def lambda_55B7():
        OP_96(0xFE, 0x4BA, 0x474A, 0x19802, 0x64, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55B7)
    OP_99(0xFE, 0x9, 0xF, 0x7D0)
    WaitChrThread(0xFE, 0x1)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_44_552D end

    def Function_45_55E6(): pass

    label("Function_45_55E6")

    OP_7D(0x0, 0xA, 0x32, 0x1F4)
    OP_97(0xA, 0xFFFFFA24, 0x18A88, 0x249F0, 0x1B58, 0x1)
    OP_7D(0x1, 0xA, 0x0, 0x0)
    OP_8C(0xA, 180, 400)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    OP_8F(0xA, 0xFFFFFC18, 0x4A38, 0x19FA0, 0xFA0, 0x0)
    OP_44(0xA, 0x2)
    Fade(500)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -1000, 19500, 106400, 180)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0x11, 0x2)
    Return()

    # Function_45_55E6 end

    def Function_46_566D(): pass

    label("Function_46_566D")

    EventBegin(0x0)
    OP_A3(0x10F2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5687")
    Call(0, 56)
    Call(0, 57)

    label("loc_5687")

    OP_D2(0x270266, 0x270270, 0x3)
    OP_D2(0x27026B, 0x270275, 0x4)
    OP_D2(0x2701C6, 0x2701CB, 0x5)
    OP_D2(0x27026C, 0x270276, 0x6)
    OP_D2(0x260003, 0x260008, 0x7)
    OP_D2(0x270257, 0x270261, 0x8)
    OP_D2(0x270252, 0x27025C, 0x9)
    OP_D2(0x270258, 0x270262, 0xA)
    OP_D2(0x70141, 0x70145, 0xB)
    OP_D2(0x70182, 0x70186, 0xF)
    OP_D2(0x2702EA, 0x2702F4, 0x13)
    OP_D2(0x2701D4, 0x2701D9, 0x14)
    OP_D2(0x702D2, 0x702D9, 0x16)
    OP_D2(0x2700B0, 0x2700B4, 0x17)
    OP_D2(0x704AA, 0x704AE, 0x18)
    OP_D2(0x270110, 0x270120, 0x1A)
    OP_D2(0x270130, 0x270140, 0x1C)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_574A"),
        (2, "loc_5757"),
        (6, "loc_5764"),
        (7, "loc_5771"),
        (SWITCH_DEFAULT, "loc_577E"),
    )


    label("loc_574A")

    OP_D2(0x70218, 0x70224, 0x1E)
    Jump("loc_577E")

    label("loc_5757")

    OP_D2(0x701D0, 0x701DC, 0x1E)
    Jump("loc_577E")

    label("loc_5764")

    OP_D2(0x70230, 0x7023C, 0x1E)
    Jump("loc_577E")

    label("loc_5771")

    OP_D2(0x70248, 0x70254, 0x1E)
    Jump("loc_577E")

    label("loc_577E")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_5797"),
        (2, "loc_57A4"),
        (6, "loc_57B1"),
        (7, "loc_57BE"),
        (SWITCH_DEFAULT, "loc_57CB"),
    )


    label("loc_5797")

    OP_D2(0x70218, 0x70224, 0x20)
    Jump("loc_57CB")

    label("loc_57A4")

    OP_D2(0x701D0, 0x701DC, 0x20)
    Jump("loc_57CB")

    label("loc_57B1")

    OP_D2(0x70230, 0x7023C, 0x20)
    Jump("loc_57CB")

    label("loc_57BE")

    OP_D2(0x70248, 0x70254, 0x20)
    Jump("loc_57CB")

    label("loc_57CB")

    OP_D2(0x2600A0, 0x2600A5, 0x22)
    OP_D2(0x60028, 0x6002D, 0x23)
    SetChrChipByIndex(0xA, 3)
    SetChrChipByIndex(0xB, 34)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 11)
    SetChrChipByIndex(0xF, 15)
    SetChrChipByIndex(0x11, 19)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x101, 26)
    SetChrChipByIndex(0x102, 28)
    SetChrChipByIndex(0xF8, 30)
    SetChrChipByIndex(0xF9, 32)
    SetChrPos(0x101, 1700, 18000, 102050, 180)
    SetChrPos(0x102, 2910, 18000, 102070, 180)
    SetChrPos(0xF8, 1760, 18000, 100500, 180)
    SetChrPos(0xF9, 2860, 18000, 100500, 180)
    SetChrPos(0x11, -1220, 18000, 101600, 0)
    SetChrPos(0x12, 260, 18000, 102200, 0)
    SetChrPos(0xE, -670, 18000, 100330, 180)
    SetChrPos(0xF, 540, 18000, 100570, 180)
    SetChrPos(0xC, -1530, 19750, 107270, 180)
    SetChrPos(0xA, -1000, 19500, 106400, 180)
    SetChrPos(0xB, 530, 19750, 107170, 180)
    SetChrPos(0xD, 1800, 19500, 106550, 180)
    SetChrPos(0x1A, -7600, 18000, 101780, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 35)
    SetChrSubChip(0x1A, 15)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    LoadEffect(0x0, "map\\\\mp046_00.eff")
    OP_6D(2280, 18000, 101560, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(33000, 0)
    OP_6E(401, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        (
            "#1004F#5P哇……\x01",
            "猎兵们被压制住了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        "#1040F#5P嗯，真是名不虚传。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A12")

    ChrTalk(    #149
        0x103,
        "#021F#5P呵呵……干得不错么。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A72")

    label("loc_5A12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A44")

    ChrTalk(    #150
        0x106,
        (
            "#051F#5P嘿……\x01",
            "干得不错嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A72")

    label("loc_5A44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A72")

    ChrTalk(    #151
        0x108,
        "#070F#5P喔……干得不错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5A72")


    def lambda_5A78():
        OP_6D(720, 19000, 105800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5A78)

    def lambda_5A90():
        OP_67(0, 6080, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A90)

    def lambda_5AA8():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AA8)
    OP_8C(0x12, 0, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #152
        0x12,
        (
            "#112F#6P那么，你们准备怎么办？\x01",
            "『噬身之蛇』的诸位。\x02\x03",

            "已到了这种地步，\x01",
            "仍然还打算同我们较量一下吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B2C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B2C)
    Sleep(50)

    def lambda_5B3F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B3F)
    Sleep(50)

    def lambda_5B52():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5B52)
    Sleep(50)

    def lambda_5B65():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5B65)
    Sleep(50)

    def lambda_5B78():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B78)
    Sleep(50)
    SetChrFlags(0xF, 0x20)

    def lambda_5B90():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5B90)
    Sleep(400)

    ChrTalk(    #153
        0xB,
        "#254F#5P……哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xC,
        (
            "#266F#5P……真讨厌。\x02\x03",

            "#262F这样的话，我就只能\x01",
            "把帕蒂尔·玛蒂尔叫来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#232F#5P不用了，玲。\x01",
            "我们自己错失了大好机会。\x02\x03",

            "再继续纠缠下去的话\x01",
            "就太缺乏美感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xD,
        (
            "#244F#5P俘虏女王陛下和公主殿下\x01",
            "也只是在条件允许的情况下的任务。\x02\x03",

            "#240F各位，咱们撤退吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        "#250F#5P哼……没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xC,
        "#262F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0xA, 4)
    OP_0D()
    SetChrChipByIndex(0xA, 6)
    PlayEffect(0x0, 0x0, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 4)
    Sleep(1500)

    ChrTalk(    #159
        0xA,
        (
            "#230F#5P那么诸位……\x01",
            "我们就先告辞了。\x02\x03",

            "但是下一次的试练\x01",
            "已经为你们准备完毕了。\x02\x03",

            "请一定不要松懈啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#1042F#4P下一次的试练……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1020F#6P什、什么意思 ！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xD,
        (
            "#244F#5P呵呵……\x01",
            "你们很快就会知道的。\x02\x03",

            "#241F那么各位，请多保重了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0xD, 8)
    Sleep(200)
    SetChrChipByIndex(0xD, 10)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_22(0x118, 0x0, 0x64)
    OP_43(0x1B, 0x0, 0x0, 0x30)
    OP_43(0x1C, 0x0, 0x0, 0x31)
    OP_43(0x1D, 0x0, 0x0, 0x32)
    OP_43(0x1E, 0x0, 0x0, 0x33)
    OP_43(0x1F, 0x0, 0x0, 0x34)
    OP_43(0x20, 0x0, 0x0, 0x35)
    OP_43(0x21, 0x0, 0x0, 0x36)
    OP_43(0x22, 0x0, 0x0, 0x37)
    Sleep(3000)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 8)
    OP_20(0xBB8)

    def lambda_5F95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5F95)

    def lambda_5FA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5FA7)

    def lambda_5FB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5FB9)
    Sleep(300)

    def lambda_5FD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5FD0)

    def lambda_5FE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5FE2)

    def lambda_5FF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5FF4)
    Sleep(300)

    def lambda_600B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_600B)

    def lambda_601D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_601D)

    def lambda_602F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_602F)
    Sleep(300)

    def lambda_6046():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6046)

    def lambda_6058():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_6058)

    def lambda_606A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_606A)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_43(0xC, 0x3, 0x0, 0x2F)
    Sleep(500)

    ChrTalk(    #163
        0x101,
        "#1026F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1035F#4P撤退了吗……\x02",
    )

    CloseMessageWindow()
    OP_21()
    Sleep(100)
    OP_1D(0x1)
    Sleep(600)

    def lambda_60D8():
        OP_6D(1170, 18000, 102460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60D8)

    def lambda_60F0():
        OP_67(0, 6050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60F0)

    def lambda_6108():
        OP_6B(2330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6108)

    def lambda_6118():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6118)

    def lambda_6128():
        OP_6E(401, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6128)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrChipByIndex(0x11, 20)
    SetChrChipByIndex(0x12, 23)
    OP_0D()

    def lambda_6166():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6166)
    Sleep(50)

    def lambda_6179():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6179)
    Sleep(50)

    def lambda_618C():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_618C)
    Sleep(50)

    def lambda_619F():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_619F)
    Sleep(50)

    def lambda_61B2():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_61B2)
    Sleep(50)

    def lambda_61C5():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_61C5)
    Sleep(400)

    ChrTalk(    #165
        0x12,
        (
            "#110F#5P嗯，这么一来，那些猎兵\x01",
            "也要撤出市内了吧。\x02\x03",

            "很遗憾，不能深追，\x01",
            "不过也别要求太高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1020F#2P嗯……等等，还有更重要的问题！\x02\x03",

            "#1019F为什么上校会\x01",
            "出现在这里！？\x02\x03",

            "你不是在服刑中吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    Sleep(300)

    ChrTalk(    #167
        0x12,
        (
            "#115F#6P所以都告诉过你\x01",
            "我已经不是上校了……算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        (
            "#701F#6P总之现在最要紧的是\x01",
            "平息这场混乱。\x02\x03",

            "你们也来帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1006F#5P嗯、嗯……\x01",
            "那当然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#1040F#2P先去进行灭火和拯救伤员\x01",
            "的工作吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_22(0x87, 0x1, 0x3C)
    OP_22(0xAE, 0x1, 0x3C)
    Sleep(100)
    OP_22(0x87, 0x1, 0x32)
    OP_22(0xAE, 0x1, 0x32)
    Sleep(100)
    OP_22(0x87, 0x1, 0x28)
    OP_22(0xAE, 0x1, 0x28)
    Sleep(100)
    OP_22(0x87, 0x1, 0x1E)
    OP_22(0xAE, 0x1, 0x1E)
    Sleep(100)
    OP_22(0x87, 0x1, 0x14)
    OP_22(0xAE, 0x1, 0x14)
    Sleep(100)
    OP_22(0x87, 0x1, 0xA)
    OP_22(0xAE, 0x1, 0xA)
    Sleep(100)
    OP_23(0x87)
    OP_23(0xAE)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #171
        (
            "\x07\x05就这样……\x01",
            "『结社』对王城的攻击终于被艰难地压制住了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #172
        (
            "\x07\x05艾丝蒂尔等人与军队一起\x01",
            "进行灭火，并安抚混乱中的市民……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #173
        (
            "\x07\x05在此期间，其他的同伴在收到联络后\x01",
            "也一起赶了过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x9C, 0x4, 0x10)
    OP_AF(0xCD, 0x9C)
    Sleep(1000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_46_566D end

    def Function_47_64BE(): pass

    label("Function_47_64BE")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_47_64BE end

    def Function_48_6506(): pass

    label("Function_48_6506")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    SetChrPos(0xFE, -1000, 19500, 106400, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_658B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65BF")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_658B")

    label("loc_65BF")

    Return()

    # Function_48_6506 end

    def Function_49_65C0(): pass

    label("Function_49_65C0")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 4)
    SetChrPos(0xFE, -1000, 19500, 106400, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_6645")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6679")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_6645")

    label("loc_6679")

    Return()

    # Function_49_65C0 end

    def Function_50_667A(): pass

    label("Function_50_667A")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 530, 19750, 107380, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_66FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6733")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_66FF")

    label("loc_6733")

    Return()

    # Function_50_667A end

    def Function_51_6734(): pass

    label("Function_51_6734")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 530, 19750, 107380, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_67B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67ED")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_67B9")

    label("loc_67ED")

    Return()

    # Function_51_6734 end

    def Function_52_67EE(): pass

    label("Function_52_67EE")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -1530, 19750, 107220, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_6873")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68A7")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_6873")

    label("loc_68A7")

    Return()

    # Function_52_67EE end

    def Function_53_68A8(): pass

    label("Function_53_68A8")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -1530, 19750, 107220, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_692D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6961")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_692D")

    label("loc_6961")

    Return()

    # Function_53_68A8 end

    def Function_54_6962(): pass

    label("Function_54_6962")

    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 2080, 19500, 106990, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_69E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A1B")
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_69E7")

    label("loc_6A1B")

    Return()

    # Function_54_6962 end

    def Function_55_6A1C(): pass

    label("Function_55_6A1C")

    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 2080, 19500, 106990, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    OP_91(0xFE, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_6AA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AD5")
    OP_91(0xFE, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xFE, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_6AA1")

    label("loc_6AD5")

    Return()

    # Function_55_6A1C end

    def Function_56_6AD6(): pass

    label("Function_56_6AD6")

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
        (0, "loc_6B50"),
        (1, "loc_6B56"),
        (SWITCH_DEFAULT, "loc_6B5C"),
    )


    label("loc_6B50")

    OP_A2(0x1200)
    Jump("loc_6B5C")

    label("loc_6B56")

    OP_A2(0x1201)
    Jump("loc_6B5C")

    label("loc_6B5C")

    Return()

    # Function_56_6AD6 end

    def Function_57_6B5D(): pass

    label("Function_57_6B5D")

    ClearMapFlags(0x1)
    OP_6D(-67910, 0, 1890, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_57_6B5D end

    SaveToFile()

Try(main)
