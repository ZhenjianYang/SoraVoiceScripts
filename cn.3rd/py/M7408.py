from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7408   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '露菲娜',                               # 9
        '提妲',                                 # 10
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 11
        '穆拉',                                 # 12
        '乔丝特',                               # 13
        '约修亚',                               # 14
        '科洛丝',                               # 15
        '基库',                                 # 16
        '奥利维尔',                             # 17
        '金',                                   # 18
        '亚妮拉丝',                             # 19
        '雪拉扎德',                             # 20
        '阿加特',                               # 21
        '艾丝蒂尔',                             # 22
        '理查德',                               # 23
        '玲',                                   # 24
        '莉丝',                                 # 25
        '凯文',                                 # 26
        '赛雷斯托',                             # 27
        '基尔巴特',                             # 28
        '',                                     # 29
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
        'ED6_DT07/CH02930 ._CH',             # 00
        'ED6_DT07/CH02940 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT27/CH03470 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT27/CH03580 ._CH',             # 05
        'ED6_DT27/CH03570 ._CH',             # 06
        'ED6_DT27/CH03100 ._CH',             # 07
        'ED6_DT27/CH03250 ._CH',             # 08
        'ED6_DT27/CH03210 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT27/CH03260 ._CH',             # 0B
        'ED6_DT07/CH00070 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT27/CH03240 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT27/CH03000 ._CH',             # 10
        'ED6_DT07/CH02030 ._CH',             # 11
        'ED6_DT27/CH03510 ._CH',             # 12
        'ED6_DT07/CH02891 ._CH',             # 13
        'ED6_DT27/CH03750 ._CH',             # 14
        'ED6_DT06/CH20113 ._CH',             # 15
        'ED6_DT26/CH20219 ._CH',             # 16
        'ED6_DT26/CH20747 ._CH',             # 17
        'ED6_DT27/CH03085 ._CH',             # 18
        'ED6_DT27/CH03475 ._CH',             # 19
        'ED6_DT07/CH02895 ._CH',             # 1A
        'ED6_DT26/CH20254 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH02930P._CP',             # 00
        'ED6_DT07/CH02940P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT27/CH03470P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT27/CH03580P._CP',             # 05
        'ED6_DT27/CH03570P._CP',             # 06
        'ED6_DT27/CH03100P._CP',             # 07
        'ED6_DT27/CH03250P._CP',             # 08
        'ED6_DT27/CH03210P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT27/CH03260P._CP',             # 0B
        'ED6_DT07/CH00070P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT27/CH03240P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT27/CH03000P._CP',             # 10
        'ED6_DT07/CH02030P._CP',             # 11
        'ED6_DT27/CH03510P._CP',             # 12
        'ED6_DT07/CH02891P._CP',             # 13
        'ED6_DT27/CH03750P._CP',             # 14
        'ED6_DT06/CH20113P._CP',             # 15
        'ED6_DT26/CH20219P._CP',             # 16
        'ED6_DT26/CH20747P._CP',             # 17
        'ED6_DT27/CH03085P._CP',             # 18
        'ED6_DT27/CH03475P._CP',             # 19
        'ED6_DT07/CH02895P._CP',             # 1A
        'ED6_DT26/CH20254P._CP',             # 1B
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_40A",          # 00, 0
        "Function_1_4A6",          # 01, 1
        "Function_2_60E",          # 02, 2
        "Function_3_2B5D",         # 03, 3
        "Function_4_3BA1",         # 04, 4
        "Function_5_3C55",         # 05, 5
        "Function_6_3D96",         # 06, 6
        "Function_7_402D",         # 07, 7
        "Function_8_AB91",         # 08, 8
        "Function_9_E47B",         # 09, 9
        "Function_10_E49E",        # 0A, 10
        "Function_11_E4C1",        # 0B, 11
        "Function_12_E4FF",        # 0C, 12
        "Function_13_E54E",        # 0D, 13
        "Function_14_E5A2",        # 0E, 14
        "Function_15_E5FB",        # 0F, 15
        "Function_16_E64A",        # 10, 16
        "Function_17_E69E",        # 11, 17
        "Function_18_E701",        # 12, 18
        "Function_19_E756",        # 13, 19
        "Function_20_E7A5",        # 14, 20
        "Function_21_E7D5",        # 15, 21
        "Function_22_E824",        # 16, 22
        "Function_23_E878",        # 17, 23
        "Function_24_E947",        # 18, 24
        "Function_25_E961",        # 19, 25
        "Function_26_EA22",        # 1A, 26
        "Function_27_EA3E",        # 1B, 27
        "Function_28_EA73",        # 1C, 28
        "Function_29_EAC2",        # 1D, 29
        "Function_30_EB16",        # 1E, 30
        "Function_31_EB4B",        # 1F, 31
        "Function_32_EB7B",        # 20, 32
        "Function_33_EBCA",        # 21, 33
        "Function_34_EC1E",        # 22, 34
        "Function_35_EC3A",        # 23, 35
        "Function_36_EC5B",        # 24, 36
        "Function_37_ECAA",        # 25, 37
        "Function_38_ECFE",        # 26, 38
        "Function_39_ED2E",        # 27, 39
        "Function_40_ED63",        # 28, 40
        "Function_41_EDB2",        # 29, 41
        "Function_42_EE06",        # 2A, 42
        "Function_43_EE4A",        # 2B, 43
    )


    def Function_0_40A(): pass

    label("Function_0_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_42F")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_C4(0x0, 0x100000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_4A5")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_454")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_C4(0x0, 0x100000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_4A5")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_46A")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_4A5")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_489")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_4A5")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_4A5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_4A5")

    Return()

    # Function_0_40A end

    def Function_1_4A6(): pass

    label("Function_1_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x334), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x335), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_519")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_519")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x336), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xE16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565")
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x49), scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_565")

    label("loc_55C")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
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
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    Return()

    # Function_1_4A6 end

    def Function_2_60E(): pass

    label("Function_2_60E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x1, "map\\mp272_00.eff")
    LoadEffect(0x2, "map\\mp260_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    OP_E6(0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 25130, 180)
    SetChrPos(0xFA, -700, 0, -62170, 0)
    SetChrPos(0xFB, 800, 0, -62900, 0)
    SetChrPos(0xFC, -1000, 0, -64250, 0)
    SetChrPos(0xFD, 1160, 0, -65319, 0)
    OP_6D(0, 850, -50000, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(5560, 0)
    OP_6C(0, 0)
    OP_6E(467, 0)

    def lambda_71B():
        OP_6D(0, 3300, 18260, 10000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_71B)

    def lambda_733():
        OP_67(0, 14860, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_733)

    def lambda_74B():
        OP_6B(5070, 10000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_74B)

    def lambda_75B():
        OP_6E(521, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_75B)

    def lambda_76B():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x38C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_76B)
    Sleep(50)

    def lambda_78B():
        OP_8E(0xFE, 0x320, 0x0, 0x38AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 0, lambda_78B)
    Sleep(50)

    def lambda_7AB():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x2FE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 0, lambda_7AB)
    Sleep(50)

    def lambda_7CB():
        OP_8E(0xFE, 0xFFFFFB78, 0x0, 0x30A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFD, 0, lambda_7CB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)

    def lambda_7F5():
        OP_6D(0, 3000, 17760, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7F5)

    def lambda_80D():
        OP_6B(3270, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_80D)

    def lambda_81D():
        OP_6E(521, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_81D)
    Sleep(2000)
    Fade(1000)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_6D(0, -550, 28610, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(0, 0)
    OP_6E(332, 0)

    def lambda_884():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_884)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        (
            "\x07\x02#1586F#5P呵呵……欢迎光临。\x02\x03",

            "#1582F没想到你们竟然\x01",
            "最终能来到这里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1200, 0, 25840, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)

    def lambda_940():
        OP_6D(1000, 0, 19200, 3500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_940)

    def lambda_958():
        OP_67(0, 4910, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_958)

    def lambda_970():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_970)

    def lambda_980():
        OP_6E(370, 3500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_980)
    Sleep(1000)
    OP_44(0xFA, 0x0)
    OP_44(0xFB, 0x0)
    OP_44(0xFC, 0x0)
    OP_44(0xFD, 0x0)
    SetChrPos(0xFA, -1380, 0, 10530, 0)
    SetChrPos(0xFB, 280, 0, 10510, 0)
    SetChrPos(0xFC, -2160, 0, 8260, 0)
    SetChrPos(0xFD, -60, 0, 8450, 0)

    def lambda_9E9():
        OP_8E(0xFE, 0xFFFFFA9C, 0x0, 0x34DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_9E9)
    Sleep(150)

    def lambda_A09():
        OP_8E(0xFE, 0x118, 0x0, 0x34C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 0, lambda_A09)
    Sleep(150)

    def lambda_A29():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0x2D8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 0, lambda_A29)
    Sleep(150)

    def lambda_A49():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0x2DE6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFD, 0, lambda_A49)
    WaitChrThread(0xFA, 0x0)
    WaitChrThread(0xFB, 0x0)
    WaitChrThread(0xFC, 0x0)
    WaitChrThread(0xFD, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(150)

    ChrTalk(    #1
        0x10F,
        "#1935F#12P……姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1063F#6P我来了……\x01",
            "露菲娜姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "\x07\x02#1586F#5P你们在『炼狱』的表现\x01",
            "我在这里都看到了。\x02\x03",

            "#1587F没想到你竟然能抵挡住\x01",
            "『白面』的诱惑呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1841F#6P说实话……\x01",
            "如果不是有莉丝在一起，\x01",
            "我也许就上钩了呢。\x02\x03",

            "#1067F从这个意义上来说……\x01",
            "我大概还是老样子，\x01",
            "又无能又软弱。\x02\x03",

            "#1840F人……\x01",
            "是无法简简单单就可以改变的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1942F#12P凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "\x07\x02#1586F#5P呵呵，\x01",
            "眼神比以前更坚定了呢。\x02\x03",

            "#1582F不过……\x01",
            "看你这么缺少自信，\x01",
            "真的没问题吗？\x02\x03",

            "只要你阻止不了我，\x01",
            "这个『影之国』就不会消失。\x02\x03",

            "这个你应该明白吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6P是啊……\x02\x03",

            "#1065F而且其影响\x01",
            "不仅限于这个世界……\x02\x03",

            "恐怕『影之国』\x01",
            "还会开始侵蚀现实世界……\x02\x03",

            "#1063F……是这样吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5")
    OP_62(0xFB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E0C")

    label("loc_DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    OP_62(0xFB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E0C")

    label("loc_DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF5")
    OP_62(0xFB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E0C")

    label("loc_DF5")

    OP_62(0xFB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E0C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E39")
    OP_62(0xFC, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EA0")

    label("loc_E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E61")
    OP_62(0xFC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EA0")

    label("loc_E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E89")
    OP_62(0xFC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EA0")

    label("loc_E89")

    OP_62(0xFC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EA0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECD")
    OP_62(0xFD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F34")

    label("loc_ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF5")
    OP_62(0xFD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F34")

    label("loc_EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1D")
    OP_62(0xFD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F34")

    label("loc_F1D")

    OP_62(0xFD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F34")

    Sleep(1000)

    ChrTalk(    #8
        0x10F,
        "#1934F#12P哎……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F91")

    ChrTalk(    #9
        0x101,
        "#1005F#12P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    label("loc_F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC8")

    ChrTalk(    #10
        0x10A,
        "#1317F#12P骗、骗人吧……！？\x02",
    )

    CloseMessageWindow()

    label("loc_FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(    #11
        0x106,
        "#055F#12P真的假的……！？\x02",
    )

    CloseMessageWindow()

    label("loc_FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")

    ChrTalk(    #12
        0x107,
        "#065F#12P是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_1030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(    #13
        0x10B,
        "#216F#12P开、开玩笑吧！？\x02",
    )

    CloseMessageWindow()

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A5")

    ChrTalk(    #14
        0x102,
        (
            "#1503F#12P不……\x01",
            "并不是不可能的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E5")

    label("loc_10A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(    #15
        0x110,
        (
            "#1305F#12P哼……\x01",
            "并不是不可能的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")


    ChrTalk(    #16
        0x10,
        (
            "\x07\x02#1586F#5P呵呵……\x01",
            "亏你能察觉呢。\x02\x03",

            "#1587F这几千年来……\x01",
            "由于吸收了人类过多的愿望，\x01",
            "『影之国』的密度已达到了极限。\x02\x03",

            "为了解放这种内部压力……\x01",
            "的确有可能会开始\x01",
            "侵蚀现实世界吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        "#1065F#6P果然是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "\x07\x02#1586F#5P虽然无法\x01",
            "一下子改变整个世界……\x02\x03",

            "但是用类似异界化的过程\x01",
            "一点一点侵蚀是可能的。\x02\x03",

            "#1582F最终结果，大概就是让\x01",
            "亡灵和恶魔涌向现实世界。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1949F#12P怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D7")

    ChrTalk(    #20
        0x10E,
        "#175F#12P……太糟糕了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_12D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1308")

    ChrTalk(    #21
        0x103,
        "#1532F#12P太糟糕了……\x02",
    )

    CloseMessageWindow()

    label("loc_1308")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134A")

    ChrTalk(    #22
        0x108,
        (
            "#074F#12P看起来……\x01",
            "似乎不是说笑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138D")

    label("loc_134A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138D")

    ChrTalk(    #23
        0x10D,
        (
            "#272F#12P看起来……\x01",
            "似乎不是开玩笑的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C9")

    ChrTalk(    #24
        0x105,
        "#1162F#12P事态如此严重了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_13C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(    #25
        0x10C,
        "#112F#12P事态如此严重了吗……\x02",
    )

    CloseMessageWindow()

    label("loc_1401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1445")

    ChrTalk(    #26
        0x104,
        (
            "#1544F#12P哎呀哎呀……\x01",
            "这下可不得了了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A5")

    ChrTalk(    #27
        0x110,
        (
            "#263F#12P现实变成童话，\x01",
            "童话变成现实……\x02\x03",

            "#1306F是这种感觉吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A5")


    ChrTalk(    #28
        0x10,
        (
            "\x07\x02#1581F#5P呵呵……\x01",
            "不过你们想想看吧。\x02\x03",

            "#1586F这也是更容易反映\x01",
            "人们思想和愿望的世界。\x02\x03",

            "如果大家都希望和平幸福的话，\x01",
            "世界或许就真的\x01",
            "能变成那样……\x02\x03",

            "#1582F干脆就这么接受下来，\x01",
            "也是一种不错的选择呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1075F#6P……不。\x01",
            "那是不可能的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x10,
        "\x07\x02#1584F哎呀……\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(300)
    Fade(500)
    OP_6D(700, 0, 10800, 0)
    OP_67(0, 4170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(140000, 0)
    OP_6E(346, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13210, 0)
    SetChrPos(0xFC, -1300, 0, 11600, 0)
    SetChrPos(0xFD, 560, 0, 11350, 0)

    def lambda_168B():
        OP_6B(2600, 30000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_168B)
    OP_0D()
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #31
        0x109,
        (
            "#1067F#11P从『辉之环』这件事就能看出来，\x01",
            "事情绝没有这么简单。\x02\x03",

            "#1065F能够无限实现\x01",
            "人们愿望的女神的至宝……\x02\x03",

            "即使接受了这种恩惠，\x01",
            "人依然无法避免破灭的命运。\x02\x03",

            "#1063F大概只会\x01",
            "重蹈覆辙而已吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "\x07\x02#1583F#2P…………………………………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1067F#11P……而对于这个，\x01",
            "姐姐应该是最清楚不过的了。\x02\x03",

            "#1065F即使身为骑士也不依靠武力，\x01",
            "拼命思考，竭尽全力\x01",
            "也要追求更好结果的姐姐……\x02\x03",

            "把完全陷入绝望中的我\x01",
            "硬拉回来的姐姐……\x02\x03",

            "#1840F你之所以会这样做，\x01",
            "大概是因为知道这世上的事\x01",
            "绝不会那么顺心如意吧。\x02\x03",

            "只有人与人相互合作，\x01",
            "努力引导出更好的结果，\x01",
            "才能让世界的存在更美好……\x02\x03",

            "你就是这么想的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "\x07\x02#1585F#2P…………………………………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1065F#11P和莉丝一起坠入『炼狱』后\x01",
            "我才终于发觉到这个事实。\x02\x03",

            "#1840F然后呢……\x01",
            "才重新明白以前的我\x01",
            "是何等渺小的存在啊。\x02\x03",

            "#1076F不知道姐姐牺牲自己\x01",
            "拯救我的真正意图……\x02\x03",

            "不去想如果不逃离母亲\x01",
            "或许能为她做什么事……\x02\x03",

            "只是一味追求『惩罚』，\x01",
            "想获得救赎的结果而已，\x01",
            "我就像个撒娇的小孩……\x02\x03",

            "#1065F我看到了……\x01",
            "自己的真实面貌。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #36
        0x10F,
        "#1942F#5P凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1075F#11P不过呢……\x01",
            "我现在觉得这样也没什么不好。\x02\x03",

            "因为我觉得终于能看到\x01",
            "姐姐所到达的境地了……\x02\x03",

            "而且我开始有自信\x01",
            "向着那里\x01",
            "一步一步前进了……\x02\x03",

            "#1840F所以我……\x01",
            "终于能够坦然正视\x01",
            "现在的自己了。\x02",
        )
    )

    Jump("loc_1BE9")

    label("loc_1BE9")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C1E")

    ChrTalk(    #38
        0x102,
        "#1501F#11P凯文先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1C")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C51")

    ChrTalk(    #39
        0x107,
        "#560F#11P凯文哥哥……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1C")

    label("loc_1C51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C85")

    ChrTalk(    #40
        0x10A,
        "#1314F#11P凯文先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1C")

    label("loc_1C85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB9")

    ChrTalk(    #41
        0x105,
        "#1382F#11P凯文先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1C")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEC")

    ChrTalk(    #42
        0x10E,
        "#171F#11P凯文先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D1C")

    label("loc_1CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1C")

    ChrTalk(    #43
        0x10B,
        "#210F#11P凯文神父……\x02",
    )

    CloseMessageWindow()

    label("loc_1D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5D")

    ChrTalk(    #44
        0x101,
        (
            "#1008F#11P呵呵……\x01",
            "看来你想通了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9C")

    label("loc_1D5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D9E")

    ChrTalk(    #45
        0x103,
        (
            "#1536F#11P呵呵……\x01",
            "看来你想通了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9C")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE4")

    ChrTalk(    #46
        0x106,
        (
            "#051F#11P嘿……\x01",
            "看来你已经下定决心了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9C")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E24")

    ChrTalk(    #47
        0x108,
        (
            "#071F#11P哈哈……\x01",
            "看来你想通了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9C")

    label("loc_1E24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5F")

    ChrTalk(    #48
        0x10D,
        "#275F#11P……看来你想通了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E9C")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9C")

    ChrTalk(    #49
        0x10C,
        (
            "#111F#11P呵呵……\x01",
            "看来你想通了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDE")

    ChrTalk(    #50
        0x104,
        (
            "#1541F#11P呼……\x01",
            "好样的，决心下得好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1B")

    ChrTalk(    #51
        0x110,
        "#1307F#11P……承认现在的自己………\x02",
    )

    CloseMessageWindow()

    label("loc_1F1B")

    Sleep(300)
    OP_44(0xFA, 0x0)
    Fade(500)
    OP_6D(1000, 0, 19200, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(370, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13510, 270)
    SetChrPos(0xFC, -2000, 0, 11660, 0)
    SetChrPos(0xFD, -60, 0, 11750, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #52
        0x10,
        (
            "\x07\x02#1583F#5P………………………………\x02\x03",

            "#1586F呵呵，看来我对你的教训\x01",
            "效果过于明显了呢。\x02\x03",

            "#1582F不过，\x01",
            "这样对『我』过高评价好吗？\x02\x03",

            "这里是『影之国』……\x01",
            "意念会给世界带来影响的地方。\x02\x03",

            "如果现在的你\x01",
            "比不上『我』的话……\x02\x03",

            "就没理由赢得了『我』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #53
        0x10F,
        "#1935F#12P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1065F#6P嗯，的确是这样吧。\x02\x03",

            "#1840F──如果你\x01",
            "真的只是再现了\x01",
            "露菲娜姐姐的存在的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x10,
        "\x07\x02#1584F#5P……什…………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        "#1934F#12P哎……！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB1)
    Sleep(500)

    ChrTalk(    #57
        0x109,
        (
            "#1063F#6P我已经……\x01",
            "知道了你的真面目。\x02\x03",

            "#1065F半年前，\x01",
            "被复制到这个『影之国』……\x02\x03",

            "成为使这个世界\x01",
            "以自我操控能力存在的核心及事理……\x02\x03",

            "#1069F并将『姐姐』这个概念整合起来的\x01",
            "我的『圣痕』本身……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1720, 0, 26480, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(45000, 0)
    OP_6E(359, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13510, 0)
    SetChrPos(0xFC, -2000, 0, 11660, 0)
    SetChrPos(0xFD, -60, 0, 11750, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #58
        0x10,
        "\x07\x02#1583F#3S#5P！！\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x1C0, 0x0, 0x64)
    OP_22(0x137, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_22(0x117, 0x0, 0x64)
    OP_22(0x2F2, 0x1, 0x3C)
    OP_22(0x32E, 0x1, 0x3C)
    PlayEffect(0x2, 0x1, 0x10, 0, -500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x0, 0x2)

    def lambda_2400():
        OP_6D(1170, 0, 28620, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2400)

    def lambda_2418():

        label("loc_2418")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x1F4)
        OP_48()
        Jump("loc_2418")

    QueueWorkItem2(0x10, 3, lambda_2418)

    def lambda_2435():
        OP_8F(0xFE, 0x0, 0x0, 0x6AB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2435)
    WaitChrThread(0x10, 0x0)

    def lambda_2455():
        OP_6D(3880, 1500, 39000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2455)

    def lambda_246D():
        OP_67(0, 3770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_246D)

    def lambda_2485():
        OP_6B(2920, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2485)

    def lambda_2495():
        OP_6E(350, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2495)
    Fade(250)

    def lambda_24AA():
        OP_8F(0xFE, 0x0, 0xBB8, 0x89F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_24AA)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_24CF():

        label("loc_24CF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_24CF")

    QueueWorkItem2(0x10, 3, lambda_24CF)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        (
            "\x07\x02#5P哼……没想到………\x02\x03",

            "没想到……\x01",
            "居然能察觉到这一步……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(110, 2650, 36260, 0)
    OP_67(0, 2400, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(0, 0)
    OP_6E(344, 0)
    SetChrPos(0x10, 0, 2500, 35320, 180)
    OP_0D()
    OP_22(0x99, 0x0, 0x64)
    Fade(1000)
    SetChrFlags(0x10, 0x80)
    OP_82(0x1, 0x2)
    OP_23(0x2F2)
    OP_23(0x32E)
    OP_0D()
    Sleep(500)
    Fade(1000)

    def lambda_25C4():
        OP_6B(3050, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_25C4)
    OP_22(0x1BF, 0x0, 0x64)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2659")

    NpcTalk(    #60
        0xFD,
        "艾丝蒂尔",
        "#1002F#5P那是……！\x02",
    )

    Jump("loc_2655")

    label("loc_2655")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2659")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269A")

    NpcTalk(    #61
        0xFD,
        "约修亚",
        "#1502F#5P那是……！\x02",
    )

    Jump("loc_2696")

    label("loc_2696")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_269A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26DE")

    NpcTalk(    #62
        0xFD,
        "乔丝特",
        "#212F#5P那、那是……！\x02",
    )

    Jump("loc_26DA")

    label("loc_26DA")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_26DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2712")

    NpcTalk(    #63
        0xFD,
        "玲",
        "#262F#5P那是……\x02",
    )

    Jump("loc_270E")

    label("loc_270E")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2751")

    NpcTalk(    #64
        0xFD,
        "提妲",
        "#062F#5P那、那是……！\x02",
    )

    Jump("loc_274D")

    label("loc_274D")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2798")

    NpcTalk(    #65
        0xFD,
        "亚妮拉丝",
        "#812F#5P那是……！？\x02",
    )

    Jump("loc_2794")

    label("loc_2794")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D9")

    NpcTalk(    #66
        0xFD,
        "科洛丝",
        "#1162F#5P那是……！\x02",
    )

    Jump("loc_27D5")

    label("loc_27D5")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_27D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281D")

    NpcTalk(    #67
        0xFD,
        "雪拉扎德",
        "#1522F#5P那是……\x02",
    )

    Jump("loc_2819")

    label("loc_2819")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_281D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285D")

    NpcTalk(    #68
        0xFD,
        "阿加特",
        "#057F#5P那是……！\x02",
    )

    Jump("loc_2859")

    label("loc_2859")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_285D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2893")

    NpcTalk(    #69
        0xFD,
        "金",
        "#072F#5P那是……！\x02",
    )

    Jump("loc_288F")

    label("loc_288F")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2893")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D8")

    NpcTalk(    #70
        0xFD,
        "尤莉亚　　　　　　　",
        "#172F#5P那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_28D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291E")

    NpcTalk(    #71
        0xFD,
        "奥利维尔",
        "#1542F#5P那是……！\x02",
    )

    Jump("loc_291A")

    label("loc_291A")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_291E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2959")

    NpcTalk(    #72
        0xFD,
        "穆拉",
        "#270F#5P那是……！\x02",
    )

    Jump("loc_2955")

    label("loc_2955")

    CloseMessageWindow()
    Jump("loc_2996")

    label("loc_2959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2996")

    NpcTalk(    #73
        0xFD,
        "理查德",
        "#112F#5P那是……！\x02",
    )

    Jump("loc_2995")

    label("loc_2995")

    CloseMessageWindow()

    label("loc_2996")


    ChrTalk(    #74
        0x10F,
        "#1931F#5P凯文的『圣痕』……！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0xFD,
        "凯文",
        (
            "#1063F#5P对手是你的话……\x01",
            "我就不可能会输了！\x02\x03",

            "#1065F为了解放\x01",
            "被你厚颜无耻利用的姐姐……\x02",
        )
    )

    Jump("loc_2A35")

    label("loc_2A35")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #76
        0xFD,
        "凯文",
        "#1069F#5P#3S我要尽全力打倒你！\x02",
    )

    Jump("loc_2A70")

    label("loc_2A70")

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77 op#A
        (
            "\x07\x02#60W#55A哈哈哈……\x01",
            "好啊，凯文·格拉汉姆……\x02\x03",

            "#60A打倒作为原型的你……\x01",
            "『吾』也能在真正意义上得以完全……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC(0x0, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_60E end

    def Function_3_2B5D(): pass

    label("Function_3_2B5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp282_00.eff")
    LoadEffect(0x1, "map\\mp282_01.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -500, 0, 26340, 0)
    SetChrPos(0xFB, 780, 0, 26300, 0)
    SetChrPos(0xFC, -1150, 0, 24200, 0)
    SetChrPos(0xFD, 1450, 0, 24270, 0)
    SetChrPos(0x10, 0, 4000, 35320, 180)
    PlayEffect(0x0, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6D(0, 3200, 37890, 0)
    OP_67(0, 2720, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(378, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_6B(3500, 1500)
    OP_0D()
    OP_22(0x85, 0x1, 0x3C)

    def lambda_2CA1():

        label("loc_2CA1")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2CA1")

    QueueWorkItem2(0xFB, 3, lambda_2CA1)
    Sleep(500)
    OP_22(0x85, 0x1, 0x50)

    def lambda_2CC6():

        label("loc_2CC6")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2CC6")

    QueueWorkItem2(0xFB, 3, lambda_2CC6)
    Sleep(500)
    OP_22(0x85, 0x1, 0x64)

    def lambda_2CEB():

        label("loc_2CEB")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_2CEB")

    QueueWorkItem2(0xFB, 3, lambda_2CEB)
    Fade(500)
    OP_22(0x32E, 0x1, 0x64)
    OP_22(0x2F2, 0x1, 0x64)
    OP_22(0x137, 0x1, 0x64)
    Sleep(100)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0x4)
    WaitChrThread(0xFA, 0x0)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78 op#A
        (
            "\x07\x02#60W#75A吾之名为『意志』……\x01",
            "统律世界的核心及事理！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_20(0x7D0)
    OP_21()
    OP_1D(0x9C)

    def lambda_2DE1():
        OP_6D(0, 3050, 33290, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_2DE1)

    def lambda_2DF9():
        OP_67(0, 1620, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_2DF9)

    def lambda_2E11():
        OP_6B(5170, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 2, lambda_2E11)

    def lambda_2E21():
        OP_6E(270, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_2E21)
    WaitChrThread(0xFA, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6E")

    ChrTalk(    #79
        0x101,
        "#1002F#5P#40W求之不得……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB8")

    ChrTalk(    #80
        0x102,
        (
            "#1502F#5P#40W……不由分说吗。\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF3")

    ChrTalk(    #81
        0x10B,
        (
            "#210F#5P#40W哼……\x01",
            "说得好听！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5D")

    ChrTalk(    #82
        0x110,
        (
            "#263F#5P#40W嘻嘻，真是太天真了。\x02\x03",

            "#1306F凭这种规则\x01",
            "就以为已经赢了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2F5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9D")

    ChrTalk(    #83
        0x107,
        "#062F#5P#40W我、我不会认输的……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF2")

    ChrTalk(    #84
        0x10A,
        (
            "#815F#5P#40W虽、虽然不大清楚状况，\x01",
            "不过我们也不会输的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_2FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302D")

    ChrTalk(    #85
        0x105,
        "#1162F#5P#40W……没办法了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_302D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3066")

    ChrTalk(    #86
        0x103,
        "#1524F#5P#40W求之不得……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_3066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A3")

    ChrTalk(    #87
        0x106,
        (
            "#057F#5P#40W啧……\x01",
            "不由分说吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_30A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E6")

    ChrTalk(    #88
        0x108,
        (
            "#070F#5P#40W哎呀哎呀……\x01",
            "不由分说吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_30E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(    #89
        0x10E,
        (
            "#172F#5P#40W……不由分说吗。\x01",
            "那就没办法了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_312F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3175")

    ChrTalk(    #90
        0x104,
        (
            "#1545F#5P#40W呼……\x01",
            "看来说什么也没用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_3175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(    #91
        0x10D,
        (
            "#270F#5P#40W……不由分说吗。\x01",
            "那就没办法了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F5")

    label("loc_31BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F5")

    ChrTalk(    #92
        0x10C,
        "#111F#5P#40W……别笑死人了！\x02",
    )

    CloseMessageWindow()

    label("loc_31F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3249")

    ChrTalk(    #93
        0x101,
        (
            "#1005F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3249")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_329F")

    ChrTalk(    #94
        0x102,
        (
            "#1502F#5P#40W如果那就是规则的话，\x01",
            "我们也很乐意奉陪……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_329F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F2")

    ChrTalk(    #95
        0x10B,
        (
            "#214F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_32F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335C")

    ChrTalk(    #96
        0x110,
        (
            "#263F#5P#40W嘻嘻，真是太天真了。\x02\x03",

            "#1306F凭这种规则\x01",
            "就以为已经赢了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_335C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B3")

    ChrTalk(    #97
        0x107,
        (
            "#062F#5P#40W如、如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_33B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3406")

    ChrTalk(    #98
        0x10A,
        (
            "#815F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3458")

    ChrTalk(    #99
        0x105,
        (
            "#1166F#5P#40W如果那就是规则的话，\x01",
            "我们也很乐意奉陪！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AC")

    ChrTalk(    #100
        0x103,
        (
            "#1524F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_34AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34FF")

    ChrTalk(    #101
        0x106,
        (
            "#054F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_34FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3554")

    ChrTalk(    #102
        0x108,
        (
            "#076F#5P#40W如果那就是规则的话，\x01",
            "我们也很乐意奉陪……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A9")

    ChrTalk(    #103
        0x10E,
        (
            "#177F#5P#40W如果那就是规则的话，\x01",
            "我们也很乐意奉陪……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_35A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3603")

    ChrTalk(    #104
        0x104,
        (
            "#1550F#5P#40W呵，如果那就是规则的话，\x01",
            "我们也很乐意奉陪……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3603")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3656")

    ChrTalk(    #105
        0x10D,
        (
            "#271F#5P#40W如果那就是规则的话，\x01",
            "我们也愿意奉陪到底！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A8")

    label("loc_3656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A8")

    ChrTalk(    #106
        0x10C,
        (
            "#114F#5P#40W如果那就是规则的话，\x01",
            "我们也很乐意奉陪……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A8")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFA, 28)
    SetChrSubChip(0xFA, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFB, 30)
    SetChrSubChip(0xFB, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFC, 32)
    SetChrSubChip(0xFC, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFD, 34)
    SetChrSubChip(0xFD, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #107
        0x109,
        (
            "#1065F#5P#40W为了让我\x01",
            "能够真正承认自己……！\x02\x03",

            "#1069F而且，\x01",
            "为了大家平安重逢的约定！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10F,
        (
            "#1939F#5P#40W我们绝对……\x01",
            "会打败你的！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_C0(0x14, 0x1F40, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_24(0x85, 0x5A)
    Sleep(400)
    OP_24(0x85, 0x50)
    Sleep(400)
    OP_24(0x85, 0x46)
    Sleep(400)
    OP_24(0x85, 0x3C)
    Sleep(400)
    OP_24(0x85, 0x32)
    Sleep(400)
    OP_24(0x85, 0x28)
    Sleep(400)
    OP_24(0x85, 0x1E)
    Sleep(400)
    OP_24(0x85, 0x14)
    Sleep(400)
    OP_23(0x85)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382A")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_3851")

    label("loc_382A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383F")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_3851")

    label("loc_383F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3851")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_3851")

    OP_A2(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B3")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_38E8")

    label("loc_38B3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38CF")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_38E8")

    label("loc_38CF")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E8")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_38E8")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38FD")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_3924")

    label("loc_38FD")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3912")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_3924")

    label("loc_3912")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3924")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_3924")

    OP_A2(0x1)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x1)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3992")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_39C7")

    label("loc_3992")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AE")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_39C7")

    label("loc_39AE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C7")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_39C7")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DC")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_3A03")

    label("loc_39DC")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F1")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_3A03")

    label("loc_39F1")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A03")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_3A03")

    OP_A2(0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x2)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A71")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_3AA6")

    label("loc_3A71")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8D")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_3AA6")

    label("loc_3A8D")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA6")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_3AA6")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_20(0x1388)
    OP_21()
    OP_DC(0x0, 0x3)
    OP_E6(0x1, 0x3)
    Sleep(500)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #109
        "\x07\x05保存到此为止的过程吗？\x18\x02",
    )

    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",          # 0
            "【继续进行】\x01",      # 1
        )
    )

    Jump("loc_3B3C")

    label("loc_3B3C")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B52")
    ShowSaveMenu()

    label("loc_3B52")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xE16, 0x300001, 0x0, 0x0, 0xFF)
    SetMapFlags(0x80)
    OP_20(0x1388)
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7499   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_3_2B5D end

    def Function_4_3BA1(): pass

    label("Function_4_3BA1")

    Sleep(1500)
    OP_24(0x32E, 0x5A)
    OP_24(0x2F2, 0x5A)
    OP_24(0x137, 0x5A)
    Sleep(300)
    OP_24(0x32E, 0x50)
    OP_24(0x2F2, 0x50)
    OP_24(0x137, 0x50)
    Sleep(300)
    OP_24(0x32E, 0x46)
    OP_24(0x2F2, 0x46)
    OP_24(0x137, 0x46)
    Sleep(300)
    OP_24(0x32E, 0x3C)
    OP_24(0x2F2, 0x3C)
    OP_24(0x137, 0x3C)
    Sleep(300)
    OP_24(0x32E, 0x32)
    OP_24(0x2F2, 0x32)
    OP_24(0x137, 0x32)
    Sleep(300)
    OP_24(0x32E, 0x28)
    OP_24(0x2F2, 0x28)
    OP_24(0x137, 0x28)
    Sleep(300)
    OP_24(0x32E, 0x1E)
    OP_24(0x2F2, 0x1E)
    OP_24(0x137, 0x1E)
    Sleep(300)
    OP_24(0x32E, 0x14)
    OP_24(0x2F2, 0x14)
    OP_24(0x137, 0x14)
    Sleep(300)
    OP_24(0x32E, 0xA)
    OP_24(0x2F2, 0xA)
    OP_24(0x137, 0xA)
    Sleep(300)
    OP_24(0x32E, 0x0)
    OP_24(0x2F2, 0x0)
    OP_24(0x137, 0x0)
    OP_23(0x32E)
    OP_23(0x2F2)
    OP_23(0x137)
    Return()

    # Function_4_3BA1 end

    def Function_5_3C55(): pass

    label("Function_5_3C55")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -1710, 0, 27030, 0)
    SetChrPos(0xFB, -210, 0, 26760, 0)
    SetChrPos(0xFC, -2210, 0, 25040, 0)
    SetChrPos(0xFD, -430, 0, 24930, 0)
    SetChrChipByIndex(0xFA, 28)
    SetChrSubChip(0xFA, 0)
    SetChrChipByIndex(0xFB, 30)
    SetChrSubChip(0xFB, 0)
    SetChrChipByIndex(0xFC, 32)
    SetChrSubChip(0xFC, 0)
    SetChrChipByIndex(0xFD, 34)
    SetChrSubChip(0xFD, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 2000, 34430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(910, 0, 30370, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(346, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0xE16, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 6)
    Return()

    # Function_5_3C55 end

    def Function_6_3D96(): pass

    label("Function_6_3D96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -1710, 0, 27030, 0)
    SetChrPos(0xFB, -210, 0, 26760, 0)
    SetChrPos(0xFC, -2210, 0, 25040, 0)
    SetChrPos(0xFD, -430, 0, 24930, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 2000, 34430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(910, 0, 30370, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(346, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x00◆实际预定在异次元空间地图进行事件。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #111
        (
            "\x07\x00◆战斗结束后，在异次元空间惨叫着消失的最终Boss。\x01",
            "之后虽然『圣痕』残留了下来，\x01",
            "但已经没有不祥的颜色，散发着蓝白色的光芒。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #112
        0x109,
        "#1060F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10F,
        "#1930F『圣痕』的颜色……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #114
        "\x07\x00◆在这里『圣痕』闪耀着，发出纯白的光芒。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_3D96 end

    def Function_7_402D(): pass

    label("Function_7_402D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mp263_05.eff")
    LoadEffect(0x2, "map\\mp276_00.eff")
    LoadEffect(0x3, "map\\mp277_00.eff")
    LoadEffect(0x4, "map\\mp278_00.eff")
    LoadEffect(0x5, "map\\mp277_01.eff")
    OP_DF(0x0, 0x1, 0x1)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xFA, 390, 0, 13390, 0)
    SetChrPos(0xFB, -1280, 0, 13610, 45)
    SetChrPos(0xFC, -710, 0, 15710, 180)
    SetChrPos(0xFD, 910, 0, 15860, 180)
    SetChrChipByIndex(0xFA, 22)
    SetChrSubChip(0xFA, 0)
    SetChrFlags(0xFA, 0x800)
    ClearChrFlags(0xFA, 0x1)
    SetChrChipByIndex(0xFB, 23)
    SetChrSubChip(0xFB, 0)
    SetChrFlags(0xFB, 0x800)
    ClearChrFlags(0xFB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4182")
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x101, -1280, 0, 16700, 180)

    label("loc_4182")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B6")
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x102, 440, 0, 17500, 180)

    label("loc_41B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41EA")
    ClearChrFlags(0x110, 0x8)
    ClearChrFlags(0x110, 0x80)
    SetChrPos(0x110, -2300, 0, 17150, 180)

    label("loc_41EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_421E")
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x107, 2600, 0, 13870, 270)

    label("loc_421E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4252")
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x106, 0x80)
    SetChrPos(0x106, 3050, 0, 12840, 270)

    label("loc_4252")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4286")
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x105, 0x80)
    SetChrPos(0x105, 2550, 0, 16340, 225)

    label("loc_4286")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42BA")
    ClearChrFlags(0x10E, 0x8)
    ClearChrFlags(0x10E, 0x80)
    SetChrPos(0x10E, 3150, 0, 15430, 225)

    label("loc_42BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42EE")
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x103, 0x80)
    SetChrPos(0x103, -4180, 0, 11880, 45)

    label("loc_42EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4322")
    ClearChrFlags(0x10A, 0x8)
    ClearChrFlags(0x10A, 0x80)
    SetChrPos(0x10A, -3520, 0, 10710, 45)

    label("loc_4322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4356")
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x104, 0x80)
    SetChrPos(0x104, -3180, 0, 14760, 90)

    label("loc_4356")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_438A")
    ClearChrFlags(0x10D, 0x8)
    ClearChrFlags(0x10D, 0x80)
    SetChrPos(0x10D, -3800, 0, 13380, 90)

    label("loc_438A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43BE")
    ClearChrFlags(0x108, 0x8)
    ClearChrFlags(0x108, 0x80)
    SetChrPos(0x108, 1390, 0, 10890, 315)

    label("loc_43BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43F2")
    ClearChrFlags(0x10C, 0x8)
    ClearChrFlags(0x10C, 0x80)
    SetChrPos(0x10C, -490, 0, 10260, 0)

    label("loc_43F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4426")
    ClearChrFlags(0x10B, 0x8)
    ClearChrFlags(0x10B, 0x80)
    SetChrPos(0x10B, -1900, 0, 10500, 0)

    label("loc_4426")

    OP_6D(800, 0, 14690, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetMessageWindowPos(60, 120, -1, -1)
    SetChrName("女孩的声音")

    AnonymousTalk(    #115
        (
            "\x07\x00凯文先生……！\x01",
            "……莉丝小姐！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("少年的声音")

    AnonymousTalk(    #116
        (
            "\x07\x00振作……\x01",
            "……振作啊……！\x02",
        )
    )

    Jump("loc_44EA")

    label("loc_44EA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 250, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #117
        "\x07\x00#1067F#60W嗯……\x02",
    )

    Jump("loc_451E")

    label("loc_451E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 300, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #118
        "\x07\x00#1955F#60W啊……\x02",
    )

    Jump("loc_4552")

    label("loc_4552")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xAD)

    def lambda_4566():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_4566)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x22, 0x0)
    Sleep(1000)

    def lambda_458A():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_458A)
    Sleep(100)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0xFA, 24)
    SetChrSubChip(0xFA, 0)
    OP_0D()
    Sleep(100)

    def lambda_45C3():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFB, 3, lambda_45C3)
    Sleep(100)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0xFB, 25)
    SetChrSubChip(0xFB, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #119
        0x109,
        "#1079F#12P#40W咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10F,
        "#1949F#6P#40W这里是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46AF")

    ChrTalk(    #121
        0x101,
        (
            "#1007F#5P太、太好了……\x02\x03",

            "#1025F战斗结束之后，\x01",
            "你们突然就昏过去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_46AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4725")

    ChrTalk(    #122
        0x102,
        (
            "#1513F#5P太好了……\x02\x03",

            "#1514F你们两个在战斗结束之后\x01",
            "就一直昏迷到现在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4725")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4799")

    ChrTalk(    #123
        0x10B,
        (
            "#413F#5P唉……别吓唬人嘛。\x02\x03",

            "#210F你们在战斗结束后\x01",
            "就突然昏过去了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4799")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4813")

    ChrTalk(    #124
        0x110,
        (
            "#268F#5P呼，真是吓死人了。\x02\x03",

            "#262F哥哥和姐姐，\x01",
            "战斗结束后就突然昏过去了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_489C")

    ChrTalk(    #125
        0x107,
        (
            "#562F#5P太、太好了……！\x02\x03",

            "#063F凯文哥哥和莉丝姐姐……\x01",
            "你们战斗结束之后\x01",
            "就突然昏了过去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_489C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4914")

    ChrTalk(    #126
        0x10A,
        (
            "#1311F#5P呼～太好了……\x02\x03",

            "#1314F你们两个，\x01",
            "战斗之后可是一直昏迷到现在哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4914")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4986")

    ChrTalk(    #127
        0x105,
        (
            "#1165F#5P太好了……\x02\x03",

            "#1382F你们两个，\x01",
            "战斗结束后就一直昏迷到现在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4986")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A16")

    ChrTalk(    #128
        0x104,
        (
            "#1541F#5P呼，\x01",
            "战斗一结束你们就一起昏过去了……\x02\x03",

            "#1547F该不会是\x01",
            "做了两个人在一起\x01",
            "卿卿我我的梦吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A99")

    ChrTalk(    #129
        0x10E,
        (
            "#179F#5P太好了……\x02\x03",

            "#171F战斗一结束\x01",
            "你们俩就一起昏了过去，\x01",
            "还担心是发生了什么事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4A99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B05")

    ChrTalk(    #130
        0x103,
        (
            "#1525F#5P哎呀哎呀……\x02\x03",

            "#1527F你们两个可是\x01",
            "一直昏迷到现在哦？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4B05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B73")

    ChrTalk(    #131
        0x106,
        (
            "#551F#5P呼，别吓唬人啊。\x02\x03",

            "#555F你们两个可是\x01",
            "一直昏迷到现在哦？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4B73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BEB")

    ChrTalk(    #132
        0x108,
        (
            "#074F#5P呼……没事了吧。\x02\x03",

            "#070F你们两个在战斗之后\x01",
            "可是一直昏迷到现在哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C60")

    label("loc_4BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C60")

    ChrTalk(    #133
        0x10D,
        (
            "#278F#5P……醒来了吗。\x02\x03",

            "#277F你们两个战斗结束之后\x01",
            "可是一直昏迷到现在哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C60")

    OP_62(0x109, 0xFFFFFED4, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 1600, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xFA, 2)
    SetChrSubChip(0xFA, 0)
    ClearChrFlags(0xFA, 0x800)
    SetChrFlags(0xFA, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0xFB, 3)
    SetChrSubChip(0xFB, 0)
    ClearChrFlags(0xFB, 0x800)
    SetChrFlags(0xFB, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #134
        0x109,
        "#1847F#12P昏过去了……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10F,
        "#1950F#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #136
        (
            "\x07\x0C大概…… \x01",
            "是因为只有『精神』被召唤到\x01",
            "『她』所构筑的领域了吧。\x07\x00\x02",
        )
    )

    Jump("loc_4D97")

    label("loc_4D97")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4F3C():
        OP_6D(3060, 300, 16610, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4F3C)

    def lambda_4F54():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4F54)

    def lambda_4F6C():
        OP_6B(3320, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4F6C)

    def lambda_4F7C():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4F7C)
    WaitChrThread(0xEE, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 4770, 500, 18110, 225)
    SetChrFlags(0x22, 0x4)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4FB7():

        label("loc_4FB7")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_4FB7")

    QueueWorkItem2(0x22, 0, lambda_4FB7)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_5009():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5009)

    def lambda_5017():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_5017)
    Sleep(50)

    def lambda_502A():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_502A)

    def lambda_5038():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5038)
    Sleep(50)

    def lambda_504B():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_504B)

    def lambda_5059():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5059)
    Sleep(50)

    def lambda_506C():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_506C)

    def lambda_507A():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_507A)
    Sleep(50)

    def lambda_508D():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_508D)

    def lambda_509B():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_509B)
    Sleep(50)

    def lambda_50AE():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50AE)

    def lambda_50BC():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_50BC)
    Sleep(50)

    def lambda_50CF():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_50CF)

    def lambda_50DD():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_50DD)
    Sleep(50)

    def lambda_50F0():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50F0)

    def lambda_50FE():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_50FE)
    Sleep(50)

    def lambda_5111():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5111)

    def lambda_511F():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_511F)
    Sleep(100)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_5167():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5167)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #137
        0x105,
        "#1164F#6P始祖大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x109,
        "#1079F#6P赛雷斯托大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x22,
        (
            "\x07\x0C#1615F#5P……就在刚才，\x01",
            "我的力量完全恢复了。\x02\x03",

            "#1612F凯文先生……\x01",
            "到底发生了什么事？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        "#1935F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_525A():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_525A)

    def lambda_5268():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5268)
    Sleep(50)

    def lambda_527B():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_527B)

    def lambda_5289():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5289)
    Sleep(50)

    def lambda_529C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_529C)

    def lambda_52AA():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_52AA)
    Sleep(50)

    def lambda_52BD():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_52BD)

    def lambda_52CB():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_52CB)
    Sleep(50)

    def lambda_52DE():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_52DE)

    def lambda_52EC():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_52EC)
    Sleep(50)

    def lambda_52FF():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_52FF)

    def lambda_530D():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_530D)
    Sleep(50)

    def lambda_5320():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5320)

    def lambda_532E():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_532E)
    Sleep(50)

    def lambda_5341():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5341)

    def lambda_534F():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_534F)
    Sleep(500)

    ChrTalk(    #141
        0x109,
        "#1065F#6P……嗯，其实是………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #142
        (
            "\x07\x05凯文向大家说明了与露菲娜的告别，\x01",
            "以及将支配『影之国』的『圣痕』\x01",
            "完全消灭的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #143
        0x10E,
        "#176F#5P……是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x105,
        "#1169F#5P非常……坚强的人呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x22,
        (
            "\x07\x0C#1616F#5P已经没有\x01",
            "和她直接对话的机会了吗……\x02\x03",

            "真希望至少\x01",
            "能见她一面呢。\x02\x03",

            "#1613F……不过既然这样的话，\x01",
            "现在就已经没什么时间了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x109,
        "#1079F#6P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_5511():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5511)

    def lambda_551F():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_551F)
    Sleep(50)

    def lambda_5532():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5532)

    def lambda_5540():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5540)
    Sleep(50)

    def lambda_5553():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_5553)

    def lambda_5561():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5561)
    Sleep(50)

    def lambda_5574():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_5574)

    def lambda_5582():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5582)
    Sleep(50)

    def lambda_5595():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5595)

    def lambda_55A3():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_55A3)
    Sleep(50)

    def lambda_55B6():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_55B6)

    def lambda_55C4():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_55C4)
    Sleep(50)

    def lambda_55D7():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55D7)

    def lambda_55E5():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_55E5)
    Sleep(50)

    def lambda_55F8():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_55F8)

    def lambda_5606():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5606)
    Sleep(300)

    ChrTalk(    #147
        0x10F,
        "#1942F#6P这是什么意思……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x22,
        (
            "\x07\x0C#1615F#5P既然『圣痕』已经消失，\x01",
            "失去主人的『影之国』\x01",
            "将再次回到不稳定的状态吧。\x02\x03",

            "#1612F这个『幻影城』，\x01",
            "应该也将很快因失去实体而消失……\x02\x03",

            "恐怕『庭院』以外的\x01",
            "『星层』也都是一样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #149
        0x101,
        "#1005F你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x101, 400)
    Sleep(300)

    ChrTalk(    #150
        0x110,
        (
            "#263F哎呀，艾丝蒂尔真是的，\x01",
            "有那么吃惊吗？\x02\x03",

            "#260F这种事只要考虑一下原理\x01",
            "就知道完全是有可能的嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x110, 400)
    Sleep(300)

    ChrTalk(    #151
        0x101,
        (
            "#1007F话、话是这么说……\x02\x03",

            "#1019F呃，\x01",
            "既然你都发现了就早说啊！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #152
        0x102,
        (
            "#1502F那么，\x01",
            "还是赶快用埃尔赛尤逃离这里吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59BF():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_59BF)

    def lambda_59CD():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 0, lambda_59CD)
    Sleep(500)

    ChrTalk(    #153
        0x22,
        (
            "\x07\x0C#1615F#5P不，用不着这么做。\x02\x03",

            "#1610F现在我就在这里\x01",
            "把『天上门』打开吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #154
        0x10F,
        "#1934F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x109,
        "#1064F#6P『天上门』是……圣典里的那个？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x22,
        (
            "\x07\x0C#1616F#5P嗯……\x02\x03",

            "应该是相对于『炼狱门』而言，\x01",
            "连接现世与天界的门吧。\x02\x03",

            "#1611F在这个地方深处，\x01",
            "也存在着一个模仿它的东西。\x02\x03",

            "看来是与『影之王』同化的她\x01",
            "所准备的呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x109,
        "#1840F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10F,
        "#1952F#6P……姐姐………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x104,
        "#1545F嗯，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10D,
        (
            "#277F只要通过那道门，\x01",
            "就可以回到原来的世界吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x22,
        (
            "\x07\x0C#1616F#5P嗯，是这样没错。\x02\x03",

            "#1610F……眼见为实。\x01",
            "我马上将它打开吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(1000)

    def lambda_5E17():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5E17)
    OP_82(0x0, 0x0)
    OP_82(0x7, 0x0)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_0D()
    Sleep(500)
    Fade(500)
    SetChrPos(0x22, 0, 4500, 23000, 0)
    OP_6D(0, 0, 33270, 0)
    OP_67(0, 4110, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_5F0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5F0C)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x2, 0x6, 0x22, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Fade(500)
    OP_82(0x7, 0x2)
    OP_0D()
    Sleep(1500)

    def lambda_5F98():
        OP_6D(0, 15300, 41770, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5F98)

    def lambda_5FB0():
        OP_67(0, -1500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5FB0)

    def lambda_5FC8():
        OP_6B(3850, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5FC8)

    def lambda_5FD8():
        OP_6E(437, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5FD8)
    WaitChrThread(0xEE, 0x0)

    def lambda_5FED():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5FED)
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x0)
    OP_72(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x0)
    OP_72(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x0)
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_0D()
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40D, 0x0)
    ExitThread()
    OP_0D()
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40E, 0x0)
    ExitThread()
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_6071():
        OP_6D(0, 14550, 41420, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6071)
    OP_22(0x150, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0xFF, 0, 14500, 56000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0x1, 0xFF, 0, 15500, 56000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_7A(0x20, 0x2)
    OP_7A(0x1E, 0x2)
    OP_7B()
    Fade(2000)
    OP_22(0x138, 0x0, 0x64)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()

    def lambda_6121():
        OP_6D(0, 14550, 41420, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6121)

    def lambda_6139():
        OP_67(0, -1230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6139)

    def lambda_6151():
        OP_6B(4340, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6151)

    def lambda_6161():
        OP_6E(420, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6161)
    OP_E5(0x2, 0x1, 0x0, 200)
    OP_E5(0x2, 0x1, 0x1, 100)
    OP_E5(0x2, 0x1, 0x2, 100)
    OP_E5(0x2, 0xA, 0x0, 300)
    OP_E5(0x2, 0xA, 0x1, 300)
    OP_E5(0x2, 0xA, 0x2, 300)
    OP_E5(0x2, 0xA, 0x3, 300)
    OP_E5(0x2, 0xB, 0x0, 300)
    OP_E5(0x2, 0xB, 0x1, 300)
    OP_E5(0x2, 0xB, 0x2, 300)
    OP_E5(0x2, 0xB, 0x3, 300)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(3000)
    Fade(500)
    OP_6D(790, 5450, 42830, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(69000, 0)
    OP_6E(475, 0)
    OP_0D()
    Sleep(500)

    def lambda_621D():
        OP_6D(790, 5450, 42830, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_621D)

    def lambda_6235():
        OP_67(0, 5970, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6235)

    def lambda_624D():
        OP_6B(4960, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_624D)

    def lambda_625D():
        OP_6C(69000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_625D)

    def lambda_626D():
        OP_6E(455, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_626D)
    Fade(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x2D8, 0x0, 0x64)
    OP_72(0x401, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x40F, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x410, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x411, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x412, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x413, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x414, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x415, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x416, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x417, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x418, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x419, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41A, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41B, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41C, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41D, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41E, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41F, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x420, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x421, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x422, 0x0)
    ExitThread()
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Fade(500)
    OP_6D(-1160, 14950, 54720, 0)
    OP_67(0, 3310, -10000, 0)
    OP_6B(5710, 0)
    OP_6C(45000, 0)
    OP_6E(365, 0)

    def lambda_63C8():
        OP_6D(0, 15500, 47600, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63C8)

    def lambda_63E0():
        OP_67(0, 200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63E0)

    def lambda_63F8():
        OP_6B(4000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_63F8)

    def lambda_6408():
        OP_6C(0, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6408)

    def lambda_6418():
        OP_6E(533, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6418)
    OP_71(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x258)
    OP_71(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x320)
    OP_71(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x12C)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_6469():

        label("loc_6469")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_6469")

    QueueWorkItem2(0x10F, 3, lambda_6469)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)

    def lambda_648E():

        label("loc_648E")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_648E")

    QueueWorkItem2(0x10F, 3, lambda_648E)
    Sleep(300)
    OP_22(0x85, 0x1, 0x64)

    def lambda_64B3():

        label("loc_64B3")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_64B3")

    QueueWorkItem2(0x10F, 3, lambda_64B3)
    PlayEffect(0x4, 0x1, 0xFF, 0, 14500, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B0(0xB, 0x32)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x226)
    OP_73(0xB)
    OP_44(0x10F, 0x3)
    OP_23(0x85)

    def lambda_6525():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6525)
    OP_22(0x88, 0x0, 0x64)
    OP_6F(0xB, 550)
    OP_70(0xB, 0x258)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    SetChrPos(0x22, 4000, 500, 28500, 225)
    OP_82(0x6, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_65A3():

        label("loc_65A3")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_65A3")

    QueueWorkItem2(0x22, 0, lambda_65A3)
    OP_23(0x146)
    SetChrChipByIndex(0x22, 19)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrFlags(0x6, 0x80)
    SetChrFlags(0x7, 0x80)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x21, -390, 0, 22360, 0)
    SetChrPos(0x20, -1870, 0, 22010, 0)
    SetChrPos(0x1D, -360, 0, 25440, 0)
    SetChrPos(0x15, 60, 0, 24000, 0)
    SetChrPos(0x1F, -1230, 0, 23590, 0)
    SetChrPos(0x11, 2600, 0, 25000, 0)
    SetChrPos(0x12, 1240, 0, 23940, 0)
    SetChrPos(0x13, -4120, 0, 22470, 0)
    SetChrPos(0x14, 1050, 0, 22440, 0)
    SetChrPos(0x16, 1210, 0, 25280, 0)
    SetChrPos(0x18, -3430, 0, 24010, 0)
    SetChrPos(0x19, 2960, 0, 22470, 0)
    SetChrPos(0x1A, -2620, 0, 23250, 0)
    SetChrPos(0x1B, -2040, 0, 24850, 0)
    SetChrPos(0x1C, 2270, 0, 23590, 0)
    SetChrPos(0x1E, 3520, 0, 24000, 0)
    Sleep(1000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #162
        "\x07\x00#1004F啊……\x02",
    )

    Jump("loc_67F9")

    label("loc_67F9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #163
        "\x07\x00#1942F通往现实世界的……出口。\x02",
    )

    Jump("loc_683B")

    label("loc_683B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("赛雷斯托")

    AnonymousTalk(    #164
        (
            "\x07\x0C#1616F大家应该会回到\x01",
            "各自被卷进来时的地点附近。\x02\x03",

            "#1611F乘坐飞艇的人\x01",
            "应该会在舱内某处出现吧。\x07\x00\x02",
        )
    )

    Jump("loc_68CE")

    label("loc_68CE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 320, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #165
        "\x07\x00#1840F是吗……\x02",
    )

    Jump("loc_6900")

    label("loc_6900")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1000, 0, 26200, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #166
        0x1D,
        "#1025F#5P……看来，要分别了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x16,
        "#1169F#11P嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        "#065F#12P哎，咦……这么快！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1A,
        (
            "#813F#6P怎、怎么说呢……\x01",
            "好像完全没有实感似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x18,
        (
            "#1540F#6P哈哈，\x01",
            "最后都没空开个宴会庆祝一下啊……\x02\x03",

            "#1545F不过本来……\x01",
            "分别就是这么回事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x1B,
        (
            "#1534F#5P呵呵……\x01",
            "或许是这样没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1F,
        "#1307F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_6AE5():
        OP_6D(3520, 0, 25400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AE5)

    def lambda_6AFD():
        OP_67(0, 5560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AFD)

    def lambda_6B15():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B15)

    def lambda_6B25():
        OP_6C(48000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6B25)

    def lambda_6B35():
        OP_6E(329, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6B35)
    OP_62(0x19, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x19)
    OP_63(0x1E)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_20(0x7D0)

    def lambda_6B83():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6B83)
    Sleep(300)
    OP_8C(0x19, 270, 300)
    Sleep(500)

    ChrTalk(    #173
        0x19,
        "#070F#11P那就……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x1E,
        (
            "#119F#5P……我们先走一步，\x01",
            "怎么样？\x02",
        )
    )

    Jump("loc_6BF5")

    label("loc_6BF5")

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6D52():

        label("loc_6D52")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6D52")

    QueueWorkItem2(0x21, 3, lambda_6D52)

    def lambda_6D63():

        label("loc_6D63")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6D63")

    QueueWorkItem2(0x20, 3, lambda_6D63)

    def lambda_6D74():

        label("loc_6D74")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6D74")

    QueueWorkItem2(0x1D, 3, lambda_6D74)

    def lambda_6D85():

        label("loc_6D85")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6D85")

    QueueWorkItem2(0x15, 3, lambda_6D85)

    def lambda_6D96():

        label("loc_6D96")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6D96")

    QueueWorkItem2(0x1F, 3, lambda_6D96)

    def lambda_6DA7():

        label("loc_6DA7")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6DA7")

    QueueWorkItem2(0x11, 3, lambda_6DA7)

    def lambda_6DB8():

        label("loc_6DB8")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6DB8")

    QueueWorkItem2(0x12, 3, lambda_6DB8)

    def lambda_6DC9():

        label("loc_6DC9")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6DC9")

    QueueWorkItem2(0x13, 3, lambda_6DC9)

    def lambda_6DDA():

        label("loc_6DDA")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6DDA")

    QueueWorkItem2(0x14, 3, lambda_6DDA)

    def lambda_6DEB():

        label("loc_6DEB")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6DEB")

    QueueWorkItem2(0x16, 3, lambda_6DEB)

    def lambda_6DFC():

        label("loc_6DFC")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6DFC")

    QueueWorkItem2(0x18, 3, lambda_6DFC)

    def lambda_6E0D():

        label("loc_6E0D")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6E0D")

    QueueWorkItem2(0x1A, 3, lambda_6E0D)

    def lambda_6E1E():

        label("loc_6E1E")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6E1E")

    QueueWorkItem2(0x1B, 3, lambda_6E1E)

    def lambda_6E2F():

        label("loc_6E2F")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_6E2F")

    QueueWorkItem2(0x1C, 3, lambda_6E2F)

    def lambda_6E40():

        label("loc_6E40")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6E40")

    QueueWorkItem2(0x22, 3, lambda_6E40)
    Sleep(300)

    ChrTalk(    #175
        0x1D,
        "#1004F#5P咦……！？\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0xB3)
    Sleep(500)

    def lambda_6E7E():
        OP_6D(600, 0, 28300, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_6E7E)

    def lambda_6E96():
        OP_67(0, 4900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6E96)

    def lambda_6EAE():
        OP_6B(3180, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_6EAE)

    def lambda_6EBE():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_6EBE)

    def lambda_6ECE():
        OP_6E(329, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6ECE)
    OP_43(0x1E, 0x0, 0x0, 0x2A)
    OP_43(0x19, 0x0, 0x0, 0x2B)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x19, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1C, 0x3)
    OP_44(0x22, 0x3)
    OP_8C(0x1A, 0, 0)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #176
        0x19,
        (
            "#573F#5P……这么依依惜别下去\x01",
            "谁都没办法走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x1E,
        (
            "#111F#5P还是让年长的我们\x01",
            "来起个头吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x1D,
        (
            "#1026F#12P金大哥……\x01",
            "理查德上校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x21,
        (
            "#1075F#12P……非常感谢。\x02\x03",

            "#1840F你们……\x01",
            "考虑得这么周到，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1E,
        (
            "#110F#5P哈哈，哪里。\x02\x03",

            "#119F倒是我……\x01",
            "你们能不计前嫌，\x01",
            "如此宽大包容，实在感谢。\x02\x03",

            "#111F……托你们的福，\x01",
            "我似乎把握住重要的东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x1A,
        "#1314F#6P理查德先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        (
            "#1513F#6P彼此彼此……\x01",
            "承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x16,
        (
            "#1168F#4P以后在工作中\x01",
            "或许还有机会见面吧。\x02\x03",

            "到时还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x1E,
        (
            "#119F#5P不用客气……\x02\x03",

            "#110F需要帮忙的话\x01",
            "请随时吩咐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x19,
        (
            "#573F#5P我呢……\x01",
            "能见到大家就很高兴了。\x02\x03",

            "#070F能像这样见面，\x01",
            "机会实在很少嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x1B,
        "#1521F#6P呵呵……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1C,
        (
            "#051F#12P真想和你……\x01",
            "再多切磋切磋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x19,
        (
            "#071F#5P哈哈，有空的话\x01",
            "我会再来利贝尔玩的。\x02\x03",

            "#070F还有……\x01",
            "方便的话，\x01",
            "大家也来卡尔瓦德玩吧。\x02\x03",

            "我会和雾香\x01",
            "一起欢迎大家的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x1D,
        (
            "#1017F#12P嗯……！\x01",
            "有机会一定去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x18,
        (
            "#1541F#6P本人可是\x01",
            "随时都想去玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x13,
        (
            "#274F#5P……你先把事情\x01",
            "都完成了再说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x21,
        (
            "#1840F#12P哈哈，我们两个\x01",
            "也应该会经常因任务而到那边去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x20,
        (
            "#1946F#6P……到时候\x01",
            "还请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x19,
        "#071F#5P嗯嗯，热烈欢迎。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x19, 270, 400)
    Sleep(300)

    ChrTalk(    #195
        0x19,
        (
            "#070F#11P……那么上校。\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)
    Sleep(300)

    ChrTalk(    #196
        0x1E,
        (
            "#495F#6P真是的……\x01",
            "你怎么也叫起上校来了。\x02\x03",

            "#110F不过算了，\x01",
            "被你们这么叫倒也不错。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x7056C, 0x7056D, 0x0)
    OP_D2(0x70071, 0x70079, 0x1)
    OP_8C(0x19, 0, 400)
    OP_8C(0x1E, 0, 400)

    def lambda_7511():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7511)

    def lambda_7529():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7529)

    def lambda_7541():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_7541)

    def lambda_7551():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_7551)

    def lambda_7561():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7561)

    def lambda_7571():

        label("loc_7571")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_7571")

    QueueWorkItem2(0x22, 3, lambda_7571)
    OP_43(0x1E, 0x0, 0x0, 0x28)
    OP_43(0x19, 0x0, 0x0, 0x29)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #197
        (
            "\x07\x00#1545F呵呵……\x01",
            "接下来是我们了吧。\x02",
        )
    )

    Jump("loc_75EA")

    label("loc_75EA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #198
        "\x07\x00#1004F哎……\x02",
    )

    Jump("loc_7624")

    label("loc_7624")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-2780, 0, 25520, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(300000, 0)
    OP_6E(325, 0)

    def lambda_767D():
        OP_6D(-1750, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_767D)

    def lambda_7695():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7695)

    def lambda_76AD():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_76AD)

    def lambda_76BD():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_76BD)

    def lambda_76CD():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_76CD)
    OP_43(0x18, 0x0, 0x0, 0x26)
    OP_43(0x13, 0x0, 0x0, 0x27)
    SetChrPos(0x20, -1870, 0, 22400, 0)
    SetChrPos(0x1A, -2500, 0, 23800, 0)
    SetChrPos(0x1B, -1900, 0, 24900, 0)
    SetChrPos(0x1C, 2470, 0, 23800, 0)
    SetChrPos(0x1F, -1150, 0, 23650, 0)

    def lambda_7740():

        label("loc_7740")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_7740")

    QueueWorkItem2(0x21, 3, lambda_7740)

    def lambda_7751():

        label("loc_7751")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_7751")

    QueueWorkItem2(0x20, 3, lambda_7751)

    def lambda_7762():

        label("loc_7762")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_7762")

    QueueWorkItem2(0x1D, 3, lambda_7762)

    def lambda_7773():

        label("loc_7773")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_7773")

    QueueWorkItem2(0x15, 3, lambda_7773)

    def lambda_7784():

        label("loc_7784")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_7784")

    QueueWorkItem2(0x1F, 3, lambda_7784)

    def lambda_7795():

        label("loc_7795")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_7795")

    QueueWorkItem2(0x11, 3, lambda_7795)

    def lambda_77A6():

        label("loc_77A6")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_77A6")

    QueueWorkItem2(0x12, 3, lambda_77A6)

    def lambda_77B7():

        label("loc_77B7")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_77B7")

    QueueWorkItem2(0x14, 3, lambda_77B7)

    def lambda_77C8():

        label("loc_77C8")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_77C8")

    QueueWorkItem2(0x16, 3, lambda_77C8)

    def lambda_77D9():

        label("loc_77D9")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_77D9")

    QueueWorkItem2(0x1A, 3, lambda_77D9)

    def lambda_77EA():

        label("loc_77EA")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_77EA")

    QueueWorkItem2(0x1B, 3, lambda_77EA)

    def lambda_77FB():

        label("loc_77FB")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_77FB")

    QueueWorkItem2(0x1C, 3, lambda_77FB)

    def lambda_780C():

        label("loc_780C")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_780C")

    QueueWorkItem2(0x22, 3, lambda_780C)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1C, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #199
        0x18,
        (
            "#1545F#11P待得越久\x01",
            "就越不想回去呢。\x02\x03",

            "#1540F所以就先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x21,
        "#1840F#6P奥利维特皇子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x15,
        (
            "#1514F#6P……真是太突然了，\x01",
            "一时不知该说什么好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x18,
        (
            "#1547F#11P啊啊，没想到约修亚君\x01",
            "会说这种话！\x02\x03",

            "#1541F真想就这样\x01",
            "把你一起带回去啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x1D,
        (
            "#1019F#6P都说啦～！\x01",
            "你想都别想！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x14,
        (
            "#413F#6P唉……\x01",
            "哪有这样的皇子殿下啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #205
        0x13,
        "#270F#5P……奥利维尔。\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x18)
    Sleep(500)

    ChrTalk(    #206
        0x18,
        (
            "#1544F#11P哈哈……\x02\x03",

            "#1540F……怎么说呢，\x01",
            "大概以后\x01",
            "不会再有这样的机会了。\x02\x03",

            "#1545F虽然不像我的性格……\x01",
            "不过心里还真有点难过。\x02",
        )
    )

    Jump("loc_7AC0")

    label("loc_7AC0")

    CloseMessageWindow()

    ChrTalk(    #207
        0x1D,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        "#1534F#6P……奥利维尔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x18,
        (
            "#1541F#11P……雪拉君，那件事，\x01",
            "希望你认真考虑一下。\x02\x03",

            "虽然我也知道\x01",
            "是很厚脸皮……\x02\x03",

            "#1540F但抱有这点期待\x01",
            "至少没什么关系吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x1B,
        (
            "#1525F#6P真是的……\x01",
            "你这人啊……\x02\x03",

            "#1536F算了，\x01",
            "我就暂时将回答保留起来吧。\x02\x03",

            "所以……\x01",
            "给我好好努力哦！\x02",
        )
    )

    Jump("loc_7C27")

    label("loc_7C27")

    CloseMessageWindow()

    ChrTalk(    #211
        0x18,
        "#1541F#11P呵，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x1A,
        "#814F#6P前、前辈……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x1D,
        (
            "#1013F#6P感、感觉好像\x01",
            "有些意味深长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x21,
        "#1840F#6P啊～你们什么时候……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #215
        0x13,
        (
            "#278F#5P而我呢……\x01",
            "和这家伙一起承蒙照顾了。\x02\x03",

            "#277F剑术方面，托各位的福，\x01",
            "也有了新的进展。\x02\x03",

            "谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1C,
        (
            "#051F#6P哼，\x01",
            "让你这样厉害的家伙走在前面，\x01",
            "要追赶的话可就更辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x12,
        (
            "#179F#6P彼此彼此……\x01",
            "许多地方多亏了你帮忙。\x02\x03",

            "#171F期待下次\x01",
            "见面的机会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #218
        0x13,
        (
            "#275F#5P……啊啊，彼此彼此。\x02\x03",

            "#272F不过帝国那边，\x01",
            "今后可有得忙了吧。\x02\x03",

            "#270F大概暂时没有时间\x01",
            "出来旅行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x12,
        "#178F#6P这么严重吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x16,
        "#1382F#6P……那么请多小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        (
            "#278F#5P呼，如果这个赖皮蛋\x01",
            "周旋的手段足够巧妙，\x01",
            "就应该能避免最糟糕的事态了吧。\x02\x03",

            "#277F……对了，\x01",
            "大家如果能帮忙祈祷这家伙\x01",
            "不被女神讨厌那就帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x1D,
        "#1016F#6P啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        "#067F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x21,
        (
            "#1066F#6P嗯，向女神祈祷\x01",
            "也是我们的特许专利嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x20,
        (
            "#1937F#6P……这点小事，\x01",
            "无论多少次都交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x18,
        (
            "#1544F#11P哎呀哎呀……\x01",
            "对本人真是不信任啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 400)
    Sleep(300)
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0x18,
        (
            "#1547F#6P不过人常说\x01",
            "越喜欢的人就越想欺负。\x02\x03",

            "穆拉真是的，\x01",
            "这么容易害羞㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x13,
        (
            "#278F#5P……你想要我勒着你的脖子\x01",
            "把你拖出去吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #229
        0x18,
        (
            "#1544F#6P不，\x01",
            "我自己走过去就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #230
        0x18,
        (
            "#1541F#11P……那么各位。\x01",
            "后会有期吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270045, 0x27004A, 0x0)
    OP_D2(0x270444, 0x270446, 0x1)
    OP_8C(0x18, 0, 400)
    OP_8C(0x13, 0, 400)

    def lambda_820E():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_820E)

    def lambda_8226():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8226)

    def lambda_823E():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_823E)

    def lambda_824E():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_824E)

    def lambda_825E():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_825E)
    OP_43(0x18, 0x0, 0x0, 0x24)
    OP_43(0x13, 0x0, 0x0, 0x25)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #231
        (
            "\x07\x00#1534F呵呵，真是的……\x01",
            "到最后还一脸无所谓的样子。\x02",
        )
    )

    Jump("loc_82E6")

    label("loc_82E6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-2780, 0, 25520, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(300000, 0)
    OP_6E(325, 0)

    def lambda_833F():
        OP_6D(-1300, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_833F)

    def lambda_8357():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8357)

    def lambda_836F():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_836F)

    def lambda_837F():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_837F)

    def lambda_838F():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_838F)
    OP_43(0x1B, 0x0, 0x0, 0x22)
    OP_43(0x1A, 0x0, 0x0, 0x23)
    SetChrPos(0x21, -390, 0, 22460, 0)
    SetChrPos(0x20, -1870, 0, 22450, 0)
    SetChrPos(0x1F, -1150, 0, 23800, 0)

    def lambda_83E0():

        label("loc_83E0")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_83E0")

    QueueWorkItem2(0x21, 3, lambda_83E0)

    def lambda_83F1():

        label("loc_83F1")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_83F1")

    QueueWorkItem2(0x20, 3, lambda_83F1)

    def lambda_8402():

        label("loc_8402")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8402")

    QueueWorkItem2(0x1D, 3, lambda_8402)

    def lambda_8413():

        label("loc_8413")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8413")

    QueueWorkItem2(0x15, 3, lambda_8413)

    def lambda_8424():

        label("loc_8424")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_8424")

    QueueWorkItem2(0x1F, 3, lambda_8424)

    def lambda_8435():

        label("loc_8435")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8435")

    QueueWorkItem2(0x11, 3, lambda_8435)

    def lambda_8446():

        label("loc_8446")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8446")

    QueueWorkItem2(0x12, 3, lambda_8446)

    def lambda_8457():

        label("loc_8457")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8457")

    QueueWorkItem2(0x14, 3, lambda_8457)

    def lambda_8468():

        label("loc_8468")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8468")

    QueueWorkItem2(0x16, 3, lambda_8468)

    def lambda_8479():

        label("loc_8479")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_8479")

    QueueWorkItem2(0x1C, 3, lambda_8479)

    def lambda_848A():

        label("loc_848A")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_848A")

    QueueWorkItem2(0x22, 3, lambda_848A)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1A, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x1C, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #232
        0x1D,
        (
            "#1025F#6P雪拉姐……\x01",
            "亚妮拉丝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x1A,
        (
            "#1314F#5P艾丝蒂尔……\x01",
            "要分别了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1B,
        (
            "#1526F#11P……反正，大家\x01",
            "只要有心就能见到的。\x02\x03",

            "#1520F艾丝蒂尔，约修亚。\x01",
            "继续旅行的途中也要保重哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x1D,
        "#1016F#6P……嗯，我知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x15,
        (
            "#1501F#6P还有……\x01",
            "我一定会给你们写信的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x1B,
        (
            "#1521F#11P呵呵，这边的回信\x01",
            "你们不一定能收到，\x01",
            "偶尔写写就好啦。\x02\x03",

            "#1536F不过，\x01",
            "最近似乎导力通讯网络\x01",
            "也已经铺设好了……\x02\x03",

            "万一有什么事，\x01",
            "可以随时联络王都支部哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1D,
        (
            "#1017F#6P嗯……\x01",
            "那我们就不客气了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x15,
        (
            "#1514F#6P你们也是……\x01",
            "如果有事的话\x01",
            "就用通讯器随时联系吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x1A,
        (
            "#1316F#5P唉～真遗憾啊。\x02\x03",

            "不光艾丝蒂尔，\x01",
            "连提妲跟小玲\x01",
            "都要见不到了……\x02\x03",

            "#812F对了，还有莉丝也是！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x20,
        "#1934F#6P我，我也是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x1A,
        (
            "#816F#5P是啊！\x01",
            "难得我们\x01",
            "已经相处得这么要好了……\x02\x03",

            "#811F要是再来利贝尔的话，\x01",
            "一定要再一起去玩哦！\x02\x03",

            "#1310F我会给你们介绍\x01",
            "很美味的冰淇淋店的！\x02",
        )
    )

    Jump("loc_887E")

    label("loc_887E")

    CloseMessageWindow()

    ChrTalk(    #243
        0x20,
        (
            "#1932F#6P……那可一定要去了。\x02\x03",

            "#1937F等我们回去之后，\x01",
            "一定最先来找你。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #244
        0x21,
        "#1068F#6P我说啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x1A,
        "#1314F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 135, 400)
    Sleep(300)

    ChrTalk(    #246
        0x1A,
        (
            "#811F#5P反正我也可以\x01",
            "趁阿加特前辈不在\x01",
            "去疼爱提妲一番……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #247
        0x11,
        "#067F#6P哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x1C,
        (
            "#555F#6P喂……\x01",
            "你乱说什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x1A,
        (
            "#819F#5P啊哈哈，好了好了。\x02\x03",

            "#816F这么一来……\x01",
            "不放心的就只有一个人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1A, 180, 400)
    Sleep(300)

    ChrTalk(    #250
        0x1A,
        (
            "#1310F#5P我说，小玲。\x02\x03",

            "#811F对艾丝蒂尔她们\x01",
            "你是喜欢呢？还是讨厌呢 ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1F,
        "#1308F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x1A,
        (
            "#1314F#5P我觉得\x01",
            "这才是最关键的。\x02\x03",

            "这是姐姐的忠告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x1F,
        "#1307F#6P说、说什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x1D,
        "#1025F#6P亚妮拉丝……\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #255
        0x1A,
        (
            "#811F#5P呵呵，\x01",
            "下次再见面的话\x01",
            "可要好好让我抱一下哦？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x1B,
        (
            "#1534F#11P哎呀哎呀……\x01",
            "我们赶快上路吧。\x02\x03",

            "#1535F大家都辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x21,
        (
            "#1078F#6P嗯……\x01",
            "彼此彼此！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x16,
        (
            "#1168F#6P两位……\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270031, 0x270036, 0x0)
    OP_D2(0x270091, 0x270095, 0x1)
    OP_8C(0x1B, 0, 400)
    OP_8C(0x1A, 0, 400)

    def lambda_8C78():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_8C78)

    def lambda_8C90():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8C90)

    def lambda_8CA8():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_8CA8)

    def lambda_8CB8():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_8CB8)

    def lambda_8CC8():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8CC8)
    OP_43(0x1B, 0x0, 0x0, 0x20)
    OP_43(0x1A, 0x0, 0x0, 0x21)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #259
        (
            "\x07\x00#051F那么……\x01",
            "接下来是我们了吧。\x02",
        )
    )

    Jump("loc_8D3A")

    label("loc_8D3A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #260
        "\x07\x00#560F是、是啊。\x02",
    )

    Jump("loc_8D6D")

    label("loc_8D6D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1740, 0, 25710, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(48000, 0)
    OP_6E(304, 0)

    def lambda_8DC6():
        OP_6D(700, 0, 28000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_8DC6)

    def lambda_8DDE():
        OP_67(0, 4750, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8DDE)

    def lambda_8DF6():
        OP_6B(2980, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_8DF6)

    def lambda_8E06():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_8E06)

    def lambda_8E16():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8E16)
    OP_43(0x1C, 0x0, 0x0, 0x1E)
    OP_43(0x11, 0x0, 0x0, 0x1F)
    SetChrPos(0x15, -100, 0, 24000, 0)
    SetChrPos(0x1F, -1330, 0, 23850, 0)
    SetChrPos(0x21, -300, 0, 22460, 0)
    SetChrPos(0x20, -1900, 0, 22210, 0)

    def lambda_8E78():

        label("loc_8E78")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8E78")

    QueueWorkItem2(0x21, 3, lambda_8E78)

    def lambda_8E89():

        label("loc_8E89")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_8E89")

    QueueWorkItem2(0x20, 3, lambda_8E89)

    def lambda_8E9A():

        label("loc_8E9A")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8E9A")

    QueueWorkItem2(0x1D, 3, lambda_8E9A)

    def lambda_8EAB():

        label("loc_8EAB")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8EAB")

    QueueWorkItem2(0x15, 3, lambda_8EAB)

    def lambda_8EBC():

        label("loc_8EBC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_8EBC")

    QueueWorkItem2(0x1F, 3, lambda_8EBC)

    def lambda_8ECD():

        label("loc_8ECD")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8ECD")

    QueueWorkItem2(0x12, 3, lambda_8ECD)

    def lambda_8EDE():

        label("loc_8EDE")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8EDE")

    QueueWorkItem2(0x14, 3, lambda_8EDE)

    def lambda_8EEF():

        label("loc_8EEF")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_8EEF")

    QueueWorkItem2(0x16, 3, lambda_8EEF)

    def lambda_8F00():

        label("loc_8F00")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_8F00")

    QueueWorkItem2(0x22, 3, lambda_8F00)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x11, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_8C(0x1D, 0, 0)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #261
        0x1D,
        "#1025F#6P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x15,
        "#1501F#6P……要分别了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        (
            "#067F#5P嘿嘿……\x01",
            "姐姐……哥哥。\x02\x03",

            "#560F还有……玲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x1F,
        "#1307F#6P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x11,
        (
            "#563F#5P我……\x01",
            "不像亚妮拉丝姐姐那样\x01",
            "善于言辞……\x02\x03",

            "也没有能与玲\x01",
            "相提并论的力量……\x02\x03",

            "#066F但是……我会等你的。\x02\x03",

            "等你们三个人\x01",
            "一起回利贝尔……\x02\x03",

            "#067F嘿嘿，\x01",
            "这么想是我的自由吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1F,
        (
            "#1300F#6P………………………………\x02\x03",

            "#266F哼、哼……\x01",
            "随便你啦。\x02\x03",

            "#262F不过，那个导力装甲\x01",
            "可别只是纸上谈兵，\x01",
            "一定要给我好好完成哦！\x02\x03",

            "#1301F玲的『帕蒂尔·玛蒂尔』\x01",
            "无论什么挑战都不怕的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x11,
        "#061F#5P嗯……我会加油的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x1D,
        "#1017F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x15,
        "#1514F#6P……哈哈………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1C,
        (
            "#551F#5P哎呀哎呀……\x01",
            "真是不安分的小鬼们啊。\x02\x03",

            "#556F……虽然雪拉扎德已经说过了，\x01",
            "但你们还是要小心啊。\x02\x03",

            "尤其是艾丝蒂尔，\x01",
            "你已经是老手了，\x01",
            "可要三思而后行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x1D,
        (
            "#1007F#6P是是。\x01",
            "我知道啦。\x02\x03",

            "#1028F阿加特才是，\x01",
            "可别老是跟\x01",
            "提妲的妈妈吵架哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #272
        0x1C,
        (
            "#055F#5P那、那个可是\x01",
            "对方单方面的\x01",
            "总是在找我茬啦！\x02\x03",

            "#552F这次的事也是，\x01",
            "还不知道会怎么刁难我呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x11,
        "#067F#5P……啊、啊哈哈………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x21,
        (
            "#1066F#12P哈哈，\x01",
            "艾莉卡博士的确总是\x01",
            "不由分说就教训起人来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1C,
        (
            "#551F#5P真是的……\x01",
            "这可不是开玩笑的。\x02\x03",

            "#050F这个暂且不论……\x01",
            "喂，不良神父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x21,
        "#1079F#12P哎……说我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1C,
        (
            "#053F#5P……最开始跟你见面的时候，\x01",
            "还以为你是个很可疑的家伙，\x01",
            "但这次表现很不错嘛。\x02\x03",

            "#051F干得好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x21,
        "#1064F#12P……………………（张大嘴）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1C,
        "#052F#5P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x21,
        (
            "#1066F#12P哎呀，实在是……\x01",
            "没想到阿加特\x01",
            "会这样称赞我啊。\x02\x03",

            "到底是吹的什么风？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x1C,
        (
            "#053F#5P哈哈……没什么深刻含义啦。\x02\x03",

            "#051F在彼此的路上，\x01",
            "互相鼓励一下而已嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x21,
        "#1840F#12P是吗……太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x20,
        "#1946F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x1D,
        (
            "#1016F#6P唉，男人之间果然\x01",
            "还是有些合不来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x1C,
        "#551F#5P你少管。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x1C, 270, 400)
    Sleep(300)

    ChrTalk(    #286
        0x1C,
        (
            "#051F#11P好……\x01",
            "那我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #287
        0x11,
        "#061F#6P好的。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x600AA, 0x600AF, 0x0)
    OP_D2(0x70061, 0x70069, 0x1)
    OP_8C(0x1C, 0, 400)
    OP_8C(0x11, 0, 400)

    def lambda_9750():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9750)

    def lambda_9768():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9768)

    def lambda_9780():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9780)

    def lambda_9790():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_9790)

    def lambda_97A0():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_97A0)
    OP_43(0x1C, 0x0, 0x0, 0x1C)
    OP_43(0x11, 0x0, 0x0, 0x1D)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #288
        (
            "\x07\x00#1382F……尤莉亚小姐。\x01",
            "我们差不多也该走了吧。\x02",
        )
    )

    Jump("loc_981F")

    label("loc_981F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #289
        "\x07\x00#179F……我知道了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-1330, 0, 25880, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(306000, 0)
    OP_6E(288, 0)

    def lambda_98B9():
        OP_6D(-1750, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_98B9)

    def lambda_98D1():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_98D1)

    def lambda_98E9():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_98E9)

    def lambda_98F9():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_98F9)

    def lambda_9909():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9909)
    OP_43(0x16, 0x0, 0x0, 0x1A)
    OP_43(0x12, 0x0, 0x0, 0x1B)
    OP_43(0x17, 0x0, 0x0, 0x19)
    OP_43(0x14, 0x0, 0x0, 0x18)
    SetChrPos(0x1F, -1100, 0, 23850, 0)
    SetChrPos(0x21, 550, 0, 22660, 0)
    SetChrPos(0x20, -1000, 0, 22600, 0)

    def lambda_9968():

        label("loc_9968")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_9968")

    QueueWorkItem2(0x21, 3, lambda_9968)

    def lambda_9979():

        label("loc_9979")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_9979")

    QueueWorkItem2(0x20, 3, lambda_9979)

    def lambda_998A():

        label("loc_998A")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_998A")

    QueueWorkItem2(0x1D, 3, lambda_998A)

    def lambda_999B():

        label("loc_999B")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_999B")

    QueueWorkItem2(0x15, 3, lambda_999B)

    def lambda_99AC():

        label("loc_99AC")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_99AC")

    QueueWorkItem2(0x1F, 3, lambda_99AC)

    def lambda_99BD():

        label("loc_99BD")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_99BD")

    QueueWorkItem2(0x22, 3, lambda_99BD)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x14, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x14, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #290
        0x15,
        "#1501F#6P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x1D,
        (
            "#1025F#6P又要……有一段时间\x01",
            "不能见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x16,
        (
            "#1165F#5P嗯嗯……\x02\x03",

            "#1168F不过能以这种方式\x01",
            "和你们两人再会……\x02\x03",

            "我已经是非常\x01",
            "感谢女神的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x15,
        "#1513F#6P……我们也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x1D,
        (
            "#1016F#6P嘿嘿……\x01",
            "我还会写信的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x16,
        (
            "#1161F#5P呵呵，\x01",
            "那我就静候你们的佳音了。\x02\x03",

            "#1382F还有……\x01",
            "乔丝特。\x02",
        )
    )

    Jump("loc_9B7B")

    label("loc_9B7B")

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #296
        0x14,
        "#213F#6P咦……我、我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x16,
        (
            "#1168F#5P这次跟你在一起\x01",
            "相处得非常愉快。\x02\x03",

            "下次有机会的话\x01",
            "能再一起聊天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x14,
        (
            "#414F#6P那、那个……\x02\x03",

            "#211F……嗯，好啊。\x02\x03",

            "反正有共同话题，\x01",
            "兴趣又相近……\x02\x03",

            "#210F我可以借工作的机会\x01",
            "时常来格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x16,
        (
            "#1161F#5P呵呵……\x01",
            "那我期待着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x1D,
        "#1019F#6P唔唔……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 315, 400)
    Sleep(300)

    ChrTalk(    #301
        0x14,
        (
            "#210F#6P哼哼，\x01",
            "不甘心的话\x01",
            "你也来做点心试试吧～？\x02\x03",

            "#211F不过看你这么笨，\x01",
            "一定是困难重重吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 135, 400)
    Sleep(300)

    ChrTalk(    #302
        0x1D,
        "#1007F#5P呜……无法反驳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x16,
        "#1165F#5P呵呵，好了好了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_9DD1():
        OP_6D(200, 0, 30900, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9DD1)

    def lambda_9DE9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9DE9)
    Sleep(200)
    SetChrFlags(0x12, 0x20)
    OP_8C(0x12, 90, 400)
    OP_8C(0x14, 0, 400)
    OP_8C(0x1D, 0, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(300)

    ChrTalk(    #304
        0x16,
        "#1163F#5P那个……始祖大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x22,
        (
            "\x07\x0C#1616F#11P呵呵……\x01",
            "请不必介意我。\x02\x03",

            "#1610F我只不过是『影』……\x01",
            "拥有真正的赛雷斯托记忆的\x01",
            "假想人格而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x16,
        (
            "#1382F#5P即使如此……\x01",
            "真希望始祖大人\x01",
            "也能和祖母见一面啊。\x02\x03",

            "#1169F我还很不成熟……\x01",
            "大概让始祖大人\x01",
            "很失望吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x22,
        (
            "\x07\x0C#1616F#11P呵呵……\x02\x03",

            "#1611F这一点真是\x01",
            "和过去的我一模一样呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #308
        0x16,
        "#1164F#5P……咦…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x22,
        (
            "\x07\x0C#1610F#11P大概你的祖母\x01",
            "当初也是这样想的吧。\x02\x03",

            "#1616F没关系，就算有所迷惑，\x01",
            "也要向着自己的道路前进。\x02\x03",

            "#1611F羽翼一定……\x01",
            "会带着你展翅飞翔。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x16,
        (
            "#1382F#5P……啊………\x02\x03",

            "#1161F是……\x01",
            "非常感谢！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #311
        0x12,
        (
            "#179F#11P呵呵……\x01",
            "差不多该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A100():
        OP_6D(-1200, 0, 27900, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_A100)
    Sleep(150)
    OP_8C(0x16, 180, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(300)

    ChrTalk(    #312
        0x12,
        (
            "#170F#11P……对了，凯文先生。\x02\x03",

            "我们大家回去之后\x01",
            "有可能会引起一些\x01",
            "混乱的事态。\x02\x03",

            "#179F要是发生什么事\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x21,
        (
            "#1075F#6P嗯嗯，我知道了。\x02\x03",

            "#1060F我们这边也要\x01",
            "和封圣省取得联络，\x01",
            "考虑今后的对策。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x16,
        (
            "#1168F#5P呵呵，那么各位……\x02\x03",

            "请多多保重！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #315
        0x12,
        "基库",
        "#311F#5P啾－！\x02",
    )

    Jump("loc_A27B")

    label("loc_A27B")

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270399, 0x27039D, 0x0)
    OP_D2(0x270445, 0x270447, 0x1)
    OP_43(0x17, 0x0, 0x0, 0x17)
    Sleep(1500)
    OP_8C(0x16, 0, 400)
    OP_8C(0x12, 0, 400)

    def lambda_A2B5():
        OP_6D(0, 12500, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_A2B5)

    def lambda_A2CD():
        OP_67(0, 2800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A2CD)

    def lambda_A2E5():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_A2E5)

    def lambda_A2F5():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_A2F5)

    def lambda_A305():
        OP_6E(310, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A305)
    OP_43(0x16, 0x0, 0x0, 0x15)
    OP_43(0x12, 0x0, 0x0, 0x16)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #316
        (
            "\x07\x00#210F接下来……\x01",
            "我差不多也该走了吧。\x02",
        )
    )

    Jump("loc_A380")

    label("loc_A380")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1740, 0, 25710, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(48000, 0)
    OP_6E(308, 0)

    def lambda_A3D9():
        OP_6D(900, 0, 27400, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_A3D9)

    def lambda_A3F1():
        OP_67(0, 4800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A3F1)

    def lambda_A409():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_A409)

    def lambda_A419():
        OP_6C(40000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_A419)

    def lambda_A429():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A429)
    OP_43(0x14, 0x0, 0x0, 0x14)
    SetChrPos(0x21, -390, 0, 22360, 0)
    SetChrPos(0x20, -1800, 0, 22300, 0)
    SetChrPos(0x1F, -1400, 0, 23800, 0)

    def lambda_A473():

        label("loc_A473")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A473")

    QueueWorkItem2(0x21, 3, lambda_A473)

    def lambda_A484():

        label("loc_A484")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A484")

    QueueWorkItem2(0x20, 3, lambda_A484)

    def lambda_A495():

        label("loc_A495")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A495")

    QueueWorkItem2(0x1D, 3, lambda_A495)

    def lambda_A4A6():

        label("loc_A4A6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A4A6")

    QueueWorkItem2(0x15, 3, lambda_A4A6)

    def lambda_A4B7():

        label("loc_A4B7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A4B7")

    QueueWorkItem2(0x1F, 3, lambda_A4B7)

    def lambda_A4C8():

        label("loc_A4C8")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_A4C8")

    QueueWorkItem2(0x22, 3, lambda_A4C8)
    WaitChrThread(0x14, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_8C(0x20, 0, 0)
    OP_8C(0x1F, 0, 0)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #317
        0x15,
        "#1501F#12P乔丝特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x1D,
        "#1013F#6P嗯……那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x14,
        (
            "#413F#5P啊，\x01",
            "不用勉强说什么啦。\x02\x03",

            "#210F我才不想听\x01",
            "你那些伤感的道别呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x1D,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x14,
        (
            "#416F#5P真是的，\x01",
            "本来还想如果和约修亚发展的顺利，\x01",
            "就这么不客气地带他走呢……\x02\x03",

            "#415F对了约修亚。\x01",
            "就这样和我一起\x01",
            "穿过那扇门回去吧？\x02\x03",

            "搞不好能回到\x01",
            "同一个地方也不一定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1D,
        "#1019F#6P你、你啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x15,
        (
            "#1514F#12P我说，那个。\x01",
            "你们俩都冷静点……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 180, 600)
    Sleep(400)

    ChrTalk(    #324
        0x1D,
        "#1005F#6P#3S约修亚你闭嘴！\x02",
    )


    ChrTalk(    #325
        0x14,
        "#214F#5P#3S约修亚你闭嘴！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #326
        0x15,
        "#1512F#12P……是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x21,
        "#1068F#12P（约、约修亚……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x20,
        "#1936F#6P（……这么没用……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x14,
        (
            "#416F#5P哼，不过……\x02\x03",

            "#210F我承认\x01",
            "是过得很开心啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 0, 400)
    Sleep(300)

    ChrTalk(    #330
        0x1D,
        (
            "#1007F#6P那是我的台词哦。\x02\x03",

            "#1006F看你工作好像很忙，\x01",
            "可别太勉强自己哦？\x02\x03",

            "和我们游击士一样，\x01",
            "身体就是本钱嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x14,
        (
            "#210F哼哼，彼此彼此。\x02\x03",

            "#211F你可别受伤\x01",
            "拖约修亚的后腿哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x15,
        (
            "#1513F#12P唉……\x02\x03",

            "#1514F（虽然关系不好，\x01",
            "  但好像又微妙地合得来……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x14,
        (
            "#210F#5P好了……\x01",
            "差不多该走了。\x02\x03",

            "#415F约修亚……\x01",
            "下次就轮到我们\x01",
            "写信给你了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x15,
        "#1501F#12P嗯，我很期待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x14,
        (
            "#416F#5P那边的两个\x01",
            "貌似也挺辛苦的……\x02\x03",

            "#210F嗯，要保重身体啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x21,
        "#1840F#12P哈哈，多谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x20,
        (
            "#1937F#6P愿女神保佑\x01",
            "你和你们的飞船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x14,
        (
            "#211F#5P哈哈，谢啦！\x02\x03",

            "#210F那么，再见了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x2700A1, 0x2700A5, 0x0)
    OP_8C(0x14, 0, 400)

    def lambda_AAC9():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_AAC9)

    def lambda_AAE1():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_AAE1)

    def lambda_AAF9():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_AAF9)

    def lambda_AB09():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_AB09)

    def lambda_AB19():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AB19)
    OP_43(0x14, 0x0, 0x0, 0x13)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #339
        "\x07\x00#1307F#40W……………………………………\x02",
    )

    Jump("loc_AB7B")

    label("loc_AB7B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Call(0, 8)
    Return()

    # Function_7_402D end

    def Function_8_AB91(): pass

    label("Function_8_AB91")

    EventBegin(0x0)
    Fade(1000)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x4, "map\\mp278_00.eff")
    OP_D2(0x270020, 0x270023, 0x0)
    OP_D2(0x26036B, 0x260370, 0x1)
    OP_D2(0x26036C, 0x260371, 0x1B)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrFlags(0x6, 0x80)
    SetChrFlags(0x7, 0x80)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x1F, -1220, 0, 23600, 0)
    SetChrPos(0x1D, -970, 0, 25400, 0)
    SetChrPos(0x15, 150, 0, 23210, 0)
    SetChrPos(0x21, -100, 0, 21400, 0)
    SetChrPos(0x20, -1480, 0, 21440, 0)
    SetChrChipByIndex(0x22, 19)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x22, 0x4)
    SetChrPos(0x22, 5500, 800, 32189, 225)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)

    def lambda_AD20():

        label("loc_AD20")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_AD20")

    QueueWorkItem2(0x22, 0, lambda_AD20)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_AD68():

        label("loc_AD68")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_AD68")

    QueueWorkItem2(0x22, 3, lambda_AD68)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x40D, 0x0)
    ExitThread()
    OP_72(0x40E, 0x0)
    ExitThread()
    OP_71(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x258)
    OP_71(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x320)
    OP_71(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x12C)
    OP_E5(0x2, 0x1, 0x0, 200)
    OP_E5(0x2, 0x1, 0x1, 100)
    OP_E5(0x2, 0x1, 0x2, 100)
    OP_E5(0x2, 0xA, 0x0, 300)
    OP_E5(0x2, 0xA, 0x1, 300)
    OP_E5(0x2, 0xA, 0x2, 300)
    OP_E5(0x2, 0xA, 0x3, 300)
    OP_E5(0x2, 0xB, 0x0, 300)
    OP_E5(0x2, 0xB, 0x1, 300)
    OP_E5(0x2, 0xB, 0x2, 300)
    OP_E5(0x2, 0xB, 0x3, 300)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_72(0x410, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_72(0x412, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x417, 0x0)
    ExitThread()
    OP_72(0x418, 0x0)
    ExitThread()
    OP_72(0x419, 0x0)
    ExitThread()
    OP_72(0x41A, 0x0)
    ExitThread()
    OP_72(0x41B, 0x0)
    ExitThread()
    OP_72(0x41C, 0x0)
    ExitThread()
    OP_72(0x41D, 0x0)
    ExitThread()
    OP_72(0x41E, 0x0)
    ExitThread()
    OP_72(0x41F, 0x0)
    ExitThread()
    OP_72(0x420, 0x0)
    ExitThread()
    OP_72(0x421, 0x0)
    ExitThread()
    OP_72(0x422, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B0(0xB, 0x32)
    OP_6F(0xB, 600)
    OP_70(0xB, 0x258)
    OP_6D(-170, 0, 22600, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(148000, 0)
    OP_6E(229, 0)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_AF07():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AF07)
    Sleep(100)

    def lambda_AF1A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_AF1A)
    Sleep(100)
    OP_8C(0x21, 315, 400)
    Sleep(500)

    ChrTalk(    #340
        0x1D,
        (
            "#1015F#6P……怎么了，玲？\x01",
            "从刚才开始就一直这么安静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x1F,
        (
            "#1307F#11P#40W……为什么………\x02\x03",

            "为什么大家……\x01",
            "都能露出这样的笑容呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x1D,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x15,
        "#1504F#5P玲……？\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 1)
    SetChrSubChip(0x1F, 0)
    OP_99(0x1F, 0x0, 0x2, 0x4B0)
    Sleep(500)

    ChrTalk(    #344
        0x1F,
        (
            "#1300F#11P#40W因为……都要分别了啊。\x02\x03",

            "说不定再也见不到了……\x02\x03",

            "#268F为什么能这样\x01",
            "笑着说再见呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x1D,
        "#1026F#6P玲……\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #346
        0x1F,
        (
            "#266F#11P这样的话……\x01",
            "不如大家都留在这里好了！\x02\x03",

            "#1301F既然『庭院』没事，\x01",
            "就可以随意制造出\x01",
            "自己喜欢的『影之国』了……！\x02\x03",

            "开心快乐的茶会\x01",
            "可以永远、永远继续下去啊！\x02\x03",

            "#1300F为什么大家……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(300)
    SetChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #347
        0x15,
        (
            "#1505F#5P是吗……你……\x02\x03",

            "#1503F见不到大家\x01",
            "会感到『痛苦』吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x1F, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)

    ChrTalk(    #348
        0x1F,
        "#1309F#11P………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x1D,
        "#1004F#6P哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_B308():
        OP_6B(3700, 15000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B308)
    Sleep(500)

    ChrTalk(    #350
        0x15,
        (
            "#1505F#5P最喜欢的人……\x02\x03",

            "想永远在一起的人……\x01",
            "都见不到了……\x02\x03",

            "这让你……感到痛苦吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x1D,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #352
        0x1F,
        (
            "#1301F#11P没、没那种事！\x02\x03",

            "这种事……\x01",
            "不可能的！\x02\x03",

            "#1303F因为玲就算\x01",
            "听说莱维死了\x01",
            "也不觉得『痛苦』啊！\x02\x03",

            "虽然很悲哀，\x01",
            "但是没有『痛苦』！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #353
        0x15,
        (
            "#1514F#5P那是因为，玲。\x02\x03",

            "你已经接受了\x01",
            "莱维的死。\x02\x03",

            "#1513F知道再也见不到了，\x01",
            "就能坦率地感到悲哀。\x02\x03",

            "#1503F……但是如果本来可以和\x01",
            "最喜欢的人相见却又无法见到的话……\x02\x03",

            "这确实比任何事都\x01",
            "『痛苦』。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #354
        0x1F,
        "#1309F#11P#40W不是……不是啦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x15,
        "#1505F#5P所以你对艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)

    def lambda_B75D():
        OP_6B(3500, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B75D)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #356
        0x1F,
        "#1303F#11P#4S都说不是啦！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_44(0x15, 0x1)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x20C, 0x0, 0x50)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    SetChrSubChip(0x15, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #357
        0x1D,
        "#1026F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_B84C():
        OP_6D(-170, 0, 22200, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_B84C)
    OP_8E(0x1D, 0xFFFFFBAA, 0x0, 0x60D6, 0x1F4, 0x0)
    WaitChrThread(0x23, 0x0)
    Fade(250)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1D, 0x800)
    SetChrChipByIndex(0x1D, 27)
    SetChrSubChip(0x1D, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #358
        0x1D,
        (
            "#1006F#6P我说啊，玲。\x01",
            "我来告诉你好吗？\x02\x03",

            "为什么大家\x01",
            "能笑着说再见。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #359
        0x1F,
        (
            "#1303F#11P#40W……不用了……！\x01",
            "我不想知道……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x1D,
        (
            "#1012F#6P……那是因为啊。\x02\x03",

            "不管是喜欢的人还是讨厌的人，\x01",
            "这些都无所谓……\x02\x03",

            "#1025F无论和什么样的人在一起……\x01",
            "最终都一定会分别的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0xFFFFFF9C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x1F, 0x1D, 0x1F, 0x3E8)
    Sleep(300)

    ChrTalk(    #361
        0x1F,
        "#1308F#11P#40W…………咦………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x1D,
        (
            "#1007F#6P我和约修亚也是。\x02\x03",

            "#1003F就算现在结婚，生了孩子，\x01",
            "然后永远在一起……\x02\x03",

            "也一定会因为有一方\x01",
            "寿命到头而分离……\x02\x03",

            "#1025F当然发生事故，\x01",
            "或者因双方感情不合\x01",
            "而分离的可能性也不是没有。\x02\x03",

            "我们大家……\x01",
            "都在与这种不安战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x1F,
        "#1307F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x15,
        "#1503F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x20,
        "#1935F#11P……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x21,
        "#1067F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x1D, 0x11, 0x14, 0x5DC)
    Sleep(500)

    ChrTalk(    #367
        0x1D,
        "#1018F#6P但是呢……正因如此才要笑哦！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #368
        0x1F,
        "#1308F#11P……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x1D,
        (
            "#1001F#6P大家一起欢笑\x01",
            "才能把这种不安赶走啊！\x02\x03",

            "#1018F大家都露出笑容\x01",
            "就能确实感受到不是孤单一人！\x02\x03",

            "也会为说不定还能再见面\x01",
            "而心跳，而兴奋不已！\x02\x03",

            "#1012F这样相互逞强着\x01",
            "约定下次再见，\x01",
            "然后踏上各自的道路……\x02\x03",

            "#1006F……我想大家或许都是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #370
        0x1F,
        "#1307F#11P大家都是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x1D,
        (
            "#1012F#6P嗯，大家都是哦。\x02\x03",

            "#1008F所以，玲……\x01",
            "和我们一起笑吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #372
        0x1F,
        "#1308F#11P#40W啊……\x02",
    )

    CloseMessageWindow()
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #373
        0x1D,
        (
            "#1007F#6P我无法约定\x01",
            "能一直和你在一起……\x02\x03",

            "#1017F#6P不过，我喜欢玲。\x02\x03",

            "在你长大成人之前\x01",
            "我想一直守护你。\x02\x03",

            "所以在那之前……\x01",
            "无论如何我都一定要和你在一起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x1F,
        "#1307F#11P#60W呜……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x1D,
        (
            "#1012F#6P然后……等玲长大，\x01",
            "找到了真正想做的事情……\x02\x03",

            "并且，如果那道路意味着\x01",
            "要离开我们……\x02\x03",

            "#1025F到时候一起……\x01",
            "用最灿烂的笑容来告别吧。\x02\x03",

            "#1016F虽然不知道以后会怎样……\x01",
            "我们先来做这样的约定如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x1F,
        (
            "#1309F#11P#50W唔……啊啊………\x02\x03",

            "……这……这种事………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #377
        0x15,
        (
            "#1513F#5P没必要马上决定哦。\x02\x03",

            "#5P因为我们……\x01",
            "已经做好心理准备了。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #378
        0x15,
        "#1501F#5P要成为……玲的家人。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x1F, 0x1F, 0x22, 0x708)
    Sleep(300)

    ChrTalk(    #379
        0x1F,
        "#1308F#11P#40W…………啊…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x1D,
        (
            "#1016F#6P不过，\x01",
            "这只是我们的希望而已。\x02\x03",

            "#1008F老爸也同意了，\x01",
            "接下来就看你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1F, 0x22, 0x26, 0x5DC)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_99(0x1F, 0x2D, 0x33, 0x5DC)

    def lambda_C35C():

        label("loc_C35C")

        OP_99(0xFE, 0x34, 0x37, 0x5DC)
        OP_48()
        Jump("loc_C35C")

    QueueWorkItem2(0x1F, 0, lambda_C35C)
    Sleep(300)

    ChrTalk(    #381
        0x1F,
        "#1309F#11P#40W………呜呜………………\x02",
    )

    CloseMessageWindow()
    OP_44(0x1F, 0x0)
    OP_99(0x1F, 0x38, 0x41, 0x7D0)
    Sleep(600)
    Fade(250)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(400)

    ChrTalk(    #382
        0x1F,
        "#1303F#11P#4S够……够了啦！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_C41F():
        OP_6D(-1200, 0, 22310, 1000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_C41F)

    def lambda_C437():
        OP_6B(3930, 1000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_C437)

    def lambda_C447():
        OP_6C(136000, 1000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_C447)

    def lambda_C457():
        OP_6E(229, 1000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_C457)
    OP_43(0x1F, 0x0, 0x0, 0x12)

    def lambda_C46E():

        label("loc_C46E")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_C46E")

    QueueWorkItem2(0x21, 3, lambda_C46E)

    def lambda_C47F():

        label("loc_C47F")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_C47F")

    QueueWorkItem2(0x20, 3, lambda_C47F)
    WaitChrThread(0x1F, 0x0)
    SetChrPos(0x22, 3500, 800, 29190, 225)
    Fade(250)
    ClearChrFlags(0x1D, 0x2)
    ClearChrFlags(0x1D, 0x800)
    SetChrChipByIndex(0x1D, 16)
    SetChrSubChip(0x1D, 0)

    def lambda_C4BF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_C4BF)
    ClearChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x23, 0x0)

    ChrTalk(    #383
        0x1D,
        "#1026F#5P……玲………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 1)
    SetChrSubChip(0x1F, 66)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x43), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_0D()
    Sleep(500)

    ChrTalk(    #384
        0x1F,
        (
            "#1303F#12P……那样的话……！\x01",
            "那样的话玲就要尽全力逃掉！\x02\x03",

            "不让艾丝蒂尔你们抓住，\x01",
            "全力的逃掉……！\x02\x03",

            "……所以……所以……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x15,
        (
            "#1513F#5P嗯，正合我意。\x02\x03",

            "#1501F在下决心之前\x01",
            "努力逃走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x1D,
        (
            "#1029F#5P哼哼，话说在前头，\x01",
            "我可是很缠人的哦～？\x02\x03",

            "#1028F不管玲如何擅长捉迷藏，\x01",
            "我都一定会把你找出来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x1F,
        (
            "#1309F#12P#40W呜呜……！\x01",
            "…………讨厌……………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_C6E5():
        OP_6B(3730, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C6E5)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x45), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #388
        0x1F,
        (
            "#1303F#12P#3S艾丝蒂尔、约修亚，\x01",
            "我最讨厌你们了！\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x47), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    Sleep(500)

    ChrTalk(    #389
        0x1F,
        (
            "#1309F#12P#40W……但是……\x01",
            "但是也一样最喜欢了……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    PlayEffect(0x4, 0x1, 0xFF, 0, 13000, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 18)
    SetChrSubChip(0x1F, 0)
    OP_8C(0x1F, 0, 400)

    def lambda_C81E():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_C81E)

    def lambda_C836():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_C836)

    def lambda_C84E():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_C84E)

    def lambda_C85E():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_C85E)

    def lambda_C86E():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C86E)
    OP_43(0x1F, 0x0, 0x0, 0x11)

    def lambda_C885():

        label("loc_C885")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_C885")

    QueueWorkItem2(0x1D, 3, lambda_C885)

    def lambda_C896():

        label("loc_C896")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_C896")

    QueueWorkItem2(0x15, 3, lambda_C896)
    Sleep(100)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x22, 0x3)
    SetMessageWindowPos(180, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #390
        (
            "\x07\x00#1016F#40W啊哈哈……\x02\x03",

            "#1017F……终于……\x01",
            "终于传达到了……\x02\x03",

            "#1027F……我的……\x01",
            "我们的话终于传达给了她……\x02",
        )
    )

    Jump("loc_C9F1")

    label("loc_C9F1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #391
        "\x07\x00#1514F艾丝蒂尔……\x02",
    )

    Jump("loc_CA2C")

    label("loc_CA2C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(700, 0, 25540, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(230, 0)
    OP_D2(0x270001, 0x270005, 0x0)
    OP_D2(0x27003B, 0x270040, 0x1)
    OP_D2(0x26036D, 0x260372, 0x1B)
    SetChrPos(0x1D, -1250, 0, 24410, 0)
    SetChrPos(0x15, -120, 0, 24450, 270)
    SetChrPos(0x21, -700, 0, 21500, 0)
    SetChrPos(0x20, -2180, 0, 21440, 0)

    def lambda_CAE7():

        label("loc_CAE7")

        TurnDirection(0xFE, 0x1D, 400)
        OP_48()
        Jump("loc_CAE7")

    QueueWorkItem2(0x22, 3, lambda_CAE7)
    SetChrPos(0x22, 3500, 800, 29190, 225)
    OP_0D()
    Sleep(300)
    OP_8C(0x1D, 90, 400)
    SetChrFlags(0x1D, 0x20)

    def lambda_CB1B():
        OP_6D(1200, 0, 25540, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_CB1B)

    def lambda_CB33():
        OP_8F(0xFE, 0xFFFFFD58, 0x0, 0x5F50, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_CB33)

    def lambda_CB4E():
        OP_99(0xFE, 0x4, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_CB4E)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x1D, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)
    SetChrFlags(0x1D, 0x8)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0x8F, 0x0, 0x64)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    SetChrSubChip(0x15, 5)
    Sleep(300)

    ChrTalk(    #392
        0x1D,
        (
            "#1027F#6P#60W呜……呜呜……\x02\x03",

            "……约修亚……约修亚……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0x15, 0x9, 0xB, 0x4B0)
    Sleep(300)

    ChrTalk(    #393
        0x15,
        "#1513F#11P嗯……你很努力了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0x15, 0xC, 0xF, 0x4B0)
    Sleep(300)

    ChrTalk(    #394
        0x15,
        (
            "#1501F#11P……但是，\x01",
            "今后还有很多事要面对呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)

    ChrTalk(    #395
        0x1D,
        (
            "#1027F#6P#40W嗯……嗯……\x02\x03",

            "#1007F…………呜……………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x1D, 0x20)
    ClearChrFlags(0x1D, 0x8)
    SetChrSubChip(0x1D, 0)

    def lambda_CDCC():
        OP_8F(0xFE, 0xFFFFFB1E, 0x0, 0x5F5A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_CDCC)
    WaitChrThread(0x1D, 0x1)
    Sleep(500)

    def lambda_CDF1():
        OP_6D(700, 0, 24950, 1000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_CDF1)
    OP_8C(0x1D, 180, 400)
    OP_8C(0x15, 180, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #396
        0x1D,
        (
            "#1007F#5P#40W对不起……\x01",
            "凯文先生，莉丝小姐。\x02\x03",

            "#1025F我们……\x01",
            "必须要走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x21,
        (
            "#1840F#12P啊啊……\x01",
            "是要去追那孩子吧？\x02\x03",

            "那就竭尽所能……\x01",
            "全力去追吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x20,
        (
            "#1937F#6P愿空之女神\x01",
            "祝福你们三人……\x02\x03",

            "#1932F下次见面时，\x01",
            "希望能看到你们三人在一起……\x02\x03",

            "我期待着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x1D,
        "#1017F#5P嗯……交给我们吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x15,
        (
            "#1501F#5P你们俩也是……\x01",
            "在那之前要多多保重哦！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_CFBC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_CFBC)
    Sleep(100)
    OP_8C(0x15, 0, 400)

    def lambda_CFD6():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_CFD6)

    def lambda_CFEE():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_CFEE)

    def lambda_D006():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_D006)

    def lambda_D016():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_D016)

    def lambda_D026():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_D026)
    OP_43(0x1D, 0x0, 0x0, 0xF)
    OP_43(0x15, 0x0, 0x0, 0x10)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #401
        "\x07\x00#1840F…………………………………\x02",
    )

    Jump("loc_D093")

    label("loc_D093")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #402
        (
            "\x07\x00#1946F真坚强啊……\x01",
            "……艾丝蒂尔他们。\x02",
        )
    )

    Jump("loc_D0DC")

    label("loc_D0DC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #403
        (
            "\x07\x00#1846F啊啊……\x01",
            "真是由衷的佩服啊。\x02",
        )
    )

    Jump("loc_D121")

    label("loc_D121")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-800, 0, 28830, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(321000, 0)
    OP_6E(255, 0)
    SetChrPos(0x21, 1450, 0, 24990, 0)
    SetChrPos(0x20, 110, 0, 24940, 0)
    OP_44(0x22, 0x3)
    SetChrPos(0x22, 3500, 800, 29190, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #404
        0x21,
        (
            "#1075F#6P但是……看到他们这样，\x01",
            "真是让人感到有希望存在呢。\x02\x03",

            "#1840F姐姐的目标……\x01",
            "她努力前往的地方真的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x20,
        (
            "#1937F#6P……嗯………\x02\x03",

            "#1946F我们……\x01",
            "也不能输给他们呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x17, 0x3, 0x0, 0x9)
    OP_22(0x85, 0x1, 0x3C)
    Sleep(1000)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #406
        0x22,
        (
            "\x07\x0C#1615F#11P差不多……\x01",
            "这里也快保不住了吧。\x02\x03",

            "#1610F好了……你们也抓紧吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x21,
        "#1078F#6P嗯嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x20,
        "#1934F#6P哎……但是……\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #409
        0x21,
        "#1079F#12P嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x20, 90, 400)
    Sleep(300)

    ChrTalk(    #410
        0x20,
        (
            "#1943F#5P嗯……\x01",
            "……感觉好像忘了什么似的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x21)
    OP_63(0x20)
    OP_63(0x22)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 390, 0, 9890, 0)

    NpcTalk(    #411
        0x23,
        "声音",
        "#2P喂～喂……！\x02",
    )

    Jump("loc_D49C")

    label("loc_D49C")

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D4F7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D4F7)
    Sleep(100)

    def lambda_D50A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D50A)
    Sleep(100)
    OP_8C(0x22, 180, 400)
    Sleep(300)

    ChrTalk(    #412
        0x21,
        "#1064F#12P啊！\x02",
    )


    ChrTalk(    #413
        0x20,
        "#1934F#5P啊……\x02",
    )


    ChrTalk(    #414
        0x22,
        "\x07\x0C#1614F#5P哎呀……\x07\x00\x02",
    )

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(400)
    SetChrPos(0x23, 480, 0, -14760, 0)
    Fade(1000)
    OP_6D(70, 0, 120, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(225000, 0)
    OP_6E(331, 0)

    def lambda_D5D1():
        OP_8E(0xFE, 0x50, 0x0, 0x5B86, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_D5D1)

    def lambda_D5EC():
        OP_6D(-470, 0, 24670, 5000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D5EC)

    def lambda_D604():
        OP_67(0, 4840, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D604)

    def lambda_D61C():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_D61C)

    def lambda_D62C():
        OP_6E(310, 5000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_D62C)
    OP_82(0x1, 0x0)
    SetChrPos(0x21, 1430, 0, 25900, 180)
    SetChrPos(0x20, 130, 0, 26110, 180)
    SetChrPos(0x22, 3500, 800, 29190, 180)
    OP_0D()
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x23, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #415
        0x23,
        "#1228F#40W#5P呼……呼……呼……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x23, 45, 600)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #416
        0x23,
        (
            "#1225F#5P太、太过分了吧！\x02\x03",

            "只留下那种说明\x01",
            "就把我一个人丢下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x22,
        (
            "\x07\x0C#1613F#6P对、对不起。\x01",
            "因为实在抽不出空……\x02\x03",

            "#1614F不过，只凭那种说明\x01",
            "不是也找到这里了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x23,
        (
            "#1224F#5P不、不是我自夸，\x01",
            "我可是路痴来的！\x02\x03",

            "#1228F又被天使集团追赶，\x01",
            "又差点被马拉的战车碾……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 0, 400)
    Sleep(300)

    ChrTalk(    #419
        0x23,
        (
            "#1224F#5P话、话说回来……\x01",
            "这摇晃是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x21,
        (
            "#1840F#6P啊，这座城，\x01",
            "很快就要消失了。\x02\x03",

            "那边就是\x01",
            "通往原来世界的出口，\x01",
            "小哥你也赶快逃出去吧。\x02",
        )
    )

    Jump("loc_D8CF")

    label("loc_D8CF")

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #421
        0x23,
        (
            "#1227F#5P这、这话你怎么不早说！\x02\x03",

            "#1225F没工夫待下去了……\x01",
            "我得赶快走了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x20,
        (
            "#1937F#12P嗯……请先走一步。\x02\x03",

            "#1932F……辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #423
        0x23,
        "#1224F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x21,
        (
            "#1078F#6P嗯，彼此彼此，\x01",
            "大家都辛苦了。\x02\x03",

            "#1075F下次见面可就是敌人了……\x02\x03",

            "#1840F你可别太胡闹\x01",
            "被我们骑士团给盯上哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x23,
        (
            "#1221F#5P哈、哈哈……\x02\x03",

            "#1226F哼，这是我的台词。\x02\x03",

            "下次见面时，让你看看我\x01",
            "更有出息更有进步的样子吧……\x02\x03",

            "#1221F请期待那个时刻的到来！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x23, 315, 600)
    PlayEffect(0x4, 0x1, 0xFF, 0, 13000, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_DB3B():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_DB3B)

    def lambda_DB53():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DB53)

    def lambda_DB6B():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_DB6B)

    def lambda_DB7B():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_DB7B)

    def lambda_DB8B():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_DB8B)
    OP_43(0x23, 0x0, 0x0, 0xE)

    def lambda_DBA2():

        label("loc_DBA2")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_DBA2")

    QueueWorkItem2(0x21, 3, lambda_DBA2)

    def lambda_DBB3():

        label("loc_DBB3")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_DBB3")

    QueueWorkItem2(0x20, 3, lambda_DBB3)

    def lambda_DBC4():

        label("loc_DBC4")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_DBC4")

    QueueWorkItem2(0x22, 3, lambda_DBC4)
    WaitChrThread(0x23, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x22, 0x3)
    WaitChrThread(0x11, 0x0)
    Sleep(2000)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("凯文")

    AnonymousTalk(    #426
        "\x07\x00#1077F哈哈……\x02",
    )

    Jump("loc_DC19")

    label("loc_DC19")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #427
        "\x07\x00#1946F……呵呵………\x02",
    )

    Jump("loc_DC51")

    label("loc_DC51")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(3600, 0, 29100, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(324, 0)
    SetChrPos(0x20, 130, 0, 26110, 0)
    SetChrPos(0x22, 3500, 800, 29050, 0)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_43(0x17, 0x3, 0x0, 0xA)
    OP_22(0x85, 0x1, 0x46)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)
    Sleep(300)
    OP_22(0x85, 0x1, 0x5A)
    OP_8C(0x22, 225, 400)
    Sleep(300)

    ChrTalk(    #428
        0x22,
        (
            "\x07\x0C#1615F#5P好了……\x01",
            "你们也赶快吧。\x02\x03",

            "#1612F大概只能撑几分钟了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DD57():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DD57)
    Sleep(100)
    OP_8C(0x20, 45, 400)
    Sleep(300)

    ChrTalk(    #429
        0x21,
        (
            "#1065F#6P……知道了。\x02\x03",

            "#1063F赛雷斯托小姐……\x01",
            "您今后打算怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x22,
        (
            "\x07\x0C#1616F#5P我将在『庭院』再度\x01",
            "进入永远的沉眠。\x02\x03",

            "直到这『影之国』\x01",
            "缓缓消失的那一日。\x02\x03",

            "#1611F然后就能……\x01",
            "从这职责中解脱出来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x21,
        (
            "#1067F#6P这样啊……\x02\x03",

            "#1840F实在是……\x01",
            "承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x20,
        "#1937F#6P……祝您好梦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x22,
        (
            "\x07\x0C#1616F#5P呵呵，谢谢。\x02\x03",

            "#1610F你们离开以后\x01",
            "我就会停止『方石』的运作。\x02\x03",

            "它不会再度苏醒了，\x01",
            "你们随便处置便是。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x21,
        (
            "#1075F#6P……明白了。\x02\x03",

            "#1078F我会把它\x01",
            "托付给合适的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x20, 90, 400)
    Sleep(300)

    ChrTalk(    #435
        0x20,
        (
            "#1934F#6P凯文……\x01",
            "你打算交给艾莉卡博士？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #436
        0x21,
        (
            "#1068F#11P嗯，\x01",
            "不这样也没法摆平她吧。\x02\x03",

            "都把她可爱的孩子\x01",
            "给卷进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x20,
        "#1946F#6P……说得也是。\x02",
    )

    CloseMessageWindow()

    def lambda_E06C():
        OP_6D(2230, 0, 27400, 2000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_E06C)

    def lambda_E084():
        OP_67(0, 4910, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_E084)

    def lambda_E09C():
        OP_6B(2580, 2000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_E09C)

    def lambda_E0AC():
        OP_6E(318, 2000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_E0AC)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #438
        0x21,
        (
            "#1078F#11P那么莉丝。\x01",
            "我们也走吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439 op#A
        0x20,
        (
            "#1936F#6P#15A嗯……\x02\x03",

            "#1938F#30A……要不\x01",
            "我们牵着手过去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #440 op#A
        0x21,
        "#1064F#11P#10A哎……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_1D(0xCA)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(800)

    ChrTalk(    #441 op#A op#5
        0x20,
        (
            "#1937F#6P#20A……呵呵，开玩笑。\x02\x03",

            "#1946F#25A不过，还是一起走吧。\x02\x03",

            "#42A前往姐姐的梦想里……\x01",
            "那历尽艰险终将抵达的彼岸。\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #442 op#A op#5
        0x21,
        "#1840F#11P#16A啊啊……\x05\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #443 op#A op#5
        0x21,
        (
            "#1078F#11P#50A那就重新说一次……\x01",
            "请多关照了，搭档！\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #444 op#A op#5
        0x20,
        "#1932F#6P#16A嗯……！\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x21, 0, 400)
    OP_8C(0x20, 0, 400)
    OP_D2(0x270081, 0x270085, 0x0)
    OP_D2(0x2705A7, 0x2705AB, 0x1)

    def lambda_E2E6():

        label("loc_E2E6")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_E2E6")

    QueueWorkItem2(0x22, 3, lambda_E2E6)
    OP_43(0x21, 0x0, 0x0, 0xC)
    OP_43(0x20, 0x0, 0x0, 0xD)

    def lambda_E305():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_E305)

    def lambda_E31D():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_E31D)

    def lambda_E335():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_E335)

    def lambda_E345():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_E345)

    def lambda_E355():
        OP_6E(300, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E355)
    WaitChrThread(0x23, 0x0)
    Sleep(1000)

    def lambda_E36F():
        OP_6D(0, 14000, 52460, 8000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_E36F)

    def lambda_E387():
        OP_67(0, 2000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_E387)

    def lambda_E39F():
        OP_6B(4300, 8000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_E39F)

    def lambda_E3AF():
        OP_6E(400, 8000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_E3AF)
    Sleep(4000)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_44(0x23, 0x0)
    OP_44(0x23, 0x1)
    OP_44(0x23, 0x2)
    OP_44(0x23, 0x3)
    OP_44(0x22, 0x0)
    OP_44(0x22, 0x1)
    OP_44(0x22, 0x2)
    OP_44(0x22, 0x3)
    OP_82(0x1, 0x0)
    OP_43(0x23, 0x0, 0x0, 0xB)
    WaitChrThread(0x23, 0x0)
    FadeToBright(2600, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_dt51.dat", 0x0, 0x0)

    label("loc_E437")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E451")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_E44E")
    Jump("loc_E451")

    label("loc_E44E")

    Jump("loc_E437")

    label("loc_E451")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_AB91 end

    def Function_9_E47B(): pass

    label("Function_9_E47B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E49D")
    OP_7C(0x14, 0x14, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_9_E47B")

    label("loc_E49D")

    Return()

    # Function_9_E47B end

    def Function_10_E49E(): pass

    label("Function_10_E49E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E4C0")
    OP_7C(0x1E, 0x1E, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_10_E49E")

    label("loc_E4C0")

    Return()

    # Function_10_E49E end

    def Function_11_E4C1(): pass

    label("Function_11_E4C1")

    OP_24(0x85, 0x3C)
    Sleep(340)
    OP_24(0x85, 0x32)
    Sleep(340)
    OP_24(0x85, 0x28)
    Sleep(340)
    OP_24(0x85, 0x1E)
    Sleep(340)
    OP_24(0x85, 0x14)
    Sleep(340)
    OP_24(0x85, 0xA)
    Sleep(340)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_11_E4C1 end

    def Function_12_E4FF(): pass

    label("Function_12_E4FF")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E523():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E523)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_E4FF end

    def Function_13_E54E(): pass

    label("Function_13_E54E")

    Sleep(200)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E577():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E577)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_E54E end

    def Function_14_E5A2(): pass

    label("Function_14_E5A2")

    OP_8E(0xFE, 0xFFFFFA92, 0x0, 0x648C, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E5D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E5D0)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_E5A2 end

    def Function_15_E5FB(): pass

    label("Function_15_E5FB")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E61F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E61F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_E5FB end

    def Function_16_E64A(): pass

    label("Function_16_E64A")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E673():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E673)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_E64A end

    def Function_17_E69E(): pass

    label("Function_17_E69E")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x7A3A, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E6D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6D6)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_E69E end

    def Function_18_E701(): pass

    label("Function_18_E701")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x800)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_E720():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E720)

    def lambda_E72E():
        OP_96(0xFE, 0xFFFFEF3E, 0x0, 0x5EEC, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E72E)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_18_E701 end

    def Function_19_E756(): pass

    label("Function_19_E756")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E77A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E77A)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_E756 end

    def Function_20_E7A5(): pass

    label("Function_20_E7A5")

    OP_8E(0xFE, 0x50A, 0x0, 0x648C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1E, 0x0, 0x74F4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_20_E7A5 end

    def Function_21_E7D5(): pass

    label("Function_21_E7D5")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E7F9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7F9)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_E7D5 end

    def Function_22_E824(): pass

    label("Function_22_E824")

    Sleep(500)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_E84D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E84D)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_E824 end

    def Function_23_E878(): pass

    label("Function_23_E878")

    Fade(250)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 2)
    ClearChrFlags(0x12, 0x20)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0x17, 0x8)
    SetChrChipByIndex(0x17, 27)

    def lambda_E8A1():

        label("loc_E8A1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E8A1")

    QueueWorkItem2(0xFE, 1, lambda_E8A1)

    def lambda_E8B4():
        OP_8F(0xFE, 0x1F4, 0xBB8, 0x7454, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_E8B4)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x17, 0x2)
    WaitChrThread(0x17, 0x2)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x17, 10)
    OP_97(0x17, 0x0, 0x6D60, 0x3F7A0, 0x1388, 0x1)
    OP_8E(0x17, 0x0, 0x30D4, 0xD73C, 0x1770, 0x0)

    def lambda_E91C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E91C)
    OP_22(0x99, 0x0, 0x64)
    OP_8F(0x17, 0x0, 0x30D4, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_E878 end

    def Function_24_E947(): pass

    label("Function_24_E947")

    Sleep(600)
    OP_8F(0xFE, 0x4F6, 0x0, 0x5E38, 0x3E8, 0x0)
    Return()

    # Function_24_E947 end

    def Function_25_E961(): pass

    label("Function_25_E961")

    OP_22(0x197, 0x0, 0x64)
    Sleep(800)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, 2760, 4000, 12950, 0)

    def lambda_E996():

        label("loc_E996")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E996")

    QueueWorkItem2(0xFE, 1, lambda_E996)
    OP_22(0x8C, 0x0, 0x64)
    OP_8F(0xFE, 0x7D0, 0xBB8, 0x7148, 0x1770, 0x0)
    OP_97(0xFE, 0x1F4, 0x7454, 0xFFF810C0, 0x1B58, 0x1)
    SetChrChipByIndex(0xFE, 27)
    OP_8C(0xFE, 135, 200)

    def lambda_E9E3():
        OP_8F(0xFE, 0x1F4, 0x12C, 0x7454, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E9E3)
    Sleep(500)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 2)
    WaitChrThread(0x17, 0x2)
    Fade(250)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x17, 0x8)
    OP_0D()
    Return()

    # Function_25_E961 end

    def Function_26_EA22(): pass

    label("Function_26_EA22")

    OP_8E(0xFE, 0x64, 0x0, 0x704E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_26_EA22 end

    def Function_27_EA3E(): pass

    label("Function_27_EA3E")

    Sleep(400)
    OP_8E(0xFE, 0x3E8, 0x0, 0x70BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x320, 0x0, 0x74A4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_27_EA3E end

    def Function_28_EA73(): pass

    label("Function_28_EA73")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EA97():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA97)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_EA73 end

    def Function_29_EAC2(): pass

    label("Function_29_EAC2")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EAEB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EAEB)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_EAC2 end

    def Function_30_EB16(): pass

    label("Function_30_EB16")

    Sleep(400)
    OP_8E(0xFE, 0xABE, 0x0, 0x65AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2EE, 0x0, 0x75F8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_30_EB16 end

    def Function_31_EB4B(): pass

    label("Function_31_EB4B")

    OP_8E(0xFE, 0xABE, 0x0, 0x65AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC68, 0x0, 0x75DA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_31_EB4B end

    def Function_32_EB7B(): pass

    label("Function_32_EB7B")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EB9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EB9F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_EB7B end

    def Function_33_EBCA(): pass

    label("Function_33_EBCA")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EBF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EBF3)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_EBCA end

    def Function_34_EC1E(): pass

    label("Function_34_EC1E")

    OP_8E(0xFE, 0x1A4, 0x0, 0x758A, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_34_EC1E end

    def Function_35_EC3A(): pass

    label("Function_35_EC3A")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x7530, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_35_EC3A end

    def Function_36_EC5B(): pass

    label("Function_36_EC5B")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EC7F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EC7F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_EC5B end

    def Function_37_ECAA(): pass

    label("Function_37_ECAA")

    Sleep(500)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_ECD3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ECD3)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_ECAA end

    def Function_38_ECFE(): pass

    label("Function_38_ECFE")

    OP_8E(0xFE, 0xFFFFF2A4, 0x0, 0x6554, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0x7274, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_38_ECFE end

    def Function_39_ED2E(): pass

    label("Function_39_ED2E")

    Sleep(400)
    OP_8E(0xFE, 0xFFFFF2A4, 0x0, 0x693C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF9DE, 0x0, 0x768E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_39_ED2E end

    def Function_40_ED63(): pass

    label("Function_40_ED63")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_ED87():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ED87)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_ED63 end

    def Function_41_EDB2(): pass

    label("Function_41_EDB2")

    Sleep(200)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_EDDB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EDDB)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_41_EDB2 end

    def Function_42_EE06(): pass

    label("Function_42_EE06")

    OP_8E(0xFE, 0xD0C, 0x0, 0x645A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7E4, 0x0, 0x6A9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB64, 0x0, 0x7580, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_42_EE06 end

    def Function_43_EE4A(): pass

    label("Function_43_EE4A")

    Sleep(400)
    OP_8E(0xFE, 0xD0C, 0x0, 0x645A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7E4, 0x0, 0x6A9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14A, 0x0, 0x759E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_43_EE4A end

    SaveToFile()

Try(main)
