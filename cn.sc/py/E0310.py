from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0310   ._SN',
        MapName             = 'Event',
        Location            = 'E0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0310_1 ._SN',
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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '金',                                   # 12
        '尤莉亚上尉',                           # 13
        '摩尔根将军',                           # 14
        '操舵士勒克司',                         # 15
        '测量师艾柯',                           # 16
        '通信员利昂',                           # 17
        '拉赛尔博士',                           # 18
        '阿加特',                               # 19
        '提妲',                                 # 20
        '凯文神父',                             # 21
        '穆拉少校',                             # 22
        '奈尔',                                 # 23
        '朵洛希',                               # 24
        '亲卫队队员',                           # 25
        '亲卫队队员',                           # 26
        '亲卫队队员',                           # 27
        '空贼雷古',                             # 28
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
        'ED6_DT26/CH20362 ._CH',             # 06
        'ED6_DT06/CH20113 ._CH',             # 07
        'ED6_DT26/CH20367 ._CH',             # 08
        'ED6_DT26/CH20368 ._CH',             # 09
        'ED6_DT26/CH20369 ._CH',             # 0A
        'ED6_DT27/CH03840 ._CH',             # 0B
        'ED6_DT27/CH03850 ._CH',             # 0C
        'ED6_DT27/CH03860 ._CH',             # 0D
        'ED6_DT07/CH02020 ._CH',             # 0E
        'ED6_DT07/CH00050 ._CH',             # 0F
        'ED6_DT07/CH00060 ._CH',             # 10
        'ED6_DT27/CH03080 ._CH',             # 11
        'ED6_DT26/CH20500 ._CH',             # 12
        'ED6_DT27/CH03573 ._CH',             # 13
        'ED6_DT27/CH03210 ._CH',             # 14
        'ED6_DT26/CH20418 ._CH',             # 15
        'ED6_DT07/CH02060 ._CH',             # 16
        'ED6_DT06/CH20063 ._CH',             # 17
        'ED6_DT27/CH03570 ._CH',             # 18
        'ED6_DT27/CH03001 ._CH',             # 19
        'ED6_DT27/CH03011 ._CH',             # 1A
        'ED6_DT07/CH01320 ._CH',             # 1B
        'ED6_DT06/CH20053 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT07/CH00070P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT07/CH02080P._CP',             # 05
        'ED6_DT26/CH20362P._CP',             # 06
        'ED6_DT06/CH20113P._CP',             # 07
        'ED6_DT26/CH20367P._CP',             # 08
        'ED6_DT26/CH20368P._CP',             # 09
        'ED6_DT26/CH20369P._CP',             # 0A
        'ED6_DT27/CH03840P._CP',             # 0B
        'ED6_DT27/CH03850P._CP',             # 0C
        'ED6_DT27/CH03860P._CP',             # 0D
        'ED6_DT07/CH02020P._CP',             # 0E
        'ED6_DT07/CH00050P._CP',             # 0F
        'ED6_DT07/CH00060P._CP',             # 10
        'ED6_DT27/CH03080P._CP',             # 11
        'ED6_DT26/CH20500P._CP',             # 12
        'ED6_DT27/CH03573P._CP',             # 13
        'ED6_DT27/CH03210P._CP',             # 14
        'ED6_DT26/CH20418P._CP',             # 15
        'ED6_DT07/CH02060P._CP',             # 16
        'ED6_DT06/CH20063P._CP',             # 17
        'ED6_DT27/CH03570P._CP',             # 18
        'ED6_DT27/CH03001P._CP',             # 19
        'ED6_DT27/CH03011P._CP',             # 1A
        'ED6_DT07/CH01320P._CP',             # 1B
        'ED6_DT06/CH20053P._CP',             # 1C
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 100,
        Y                   = 99020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 1300,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        X                   = 1760,
        Z                   = 300,
        Y                   = 96770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196626,
        ChipIndex           = 0x12,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = 0,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = 0,
        Y                   = -840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 2000,
        Y                   = 49050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2670,
        Z                   = 0,
        Y                   = 100010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 3470,
        Y                   = -1000,
        Z                   = -840,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -2920,
        Y                   = 1000,
        Z                   = 49050,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -900,
        Y                   = -500,
        Z                   = 500,
        Range               = -3110,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x898,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_BE7",          # 01, 1
        "Function_2_D50",          # 02, 2
        "Function_3_ECD",          # 03, 3
        "Function_4_264D",         # 04, 4
        "Function_5_29D3",         # 05, 5
        "Function_6_43CC",         # 06, 6
        "Function_7_43EC",         # 07, 7
        "Function_8_4642",         # 08, 8
        "Function_9_46BF",         # 09, 9
        "Function_10_4919",        # 0A, 10
        "Function_11_4A13",        # 0B, 11
        "Function_12_4ED7",        # 0C, 12
        "Function_13_4F1F",        # 0D, 13
        "Function_14_4F67",        # 0E, 14
        "Function_15_4FAF",        # 0F, 15
        "Function_16_4FF7",        # 10, 16
        "Function_17_53CC",        # 11, 17
        "Function_18_56E9",        # 12, 18
        "Function_19_5847",        # 13, 19
        "Function_20_5ADB",        # 14, 20
        "Function_21_5F36",        # 15, 21
        "Function_22_5F78",        # 16, 22
        "Function_23_5FD1",        # 17, 23
        "Function_24_6523",        # 18, 24
        "Function_25_6A90",        # 19, 25
        "Function_26_726D",        # 1A, 26
        "Function_27_72B5",        # 1B, 27
        "Function_28_72FD",        # 1C, 28
        "Function_29_7345",        # 1D, 29
        "Function_30_738D",        # 1E, 30
        "Function_31_73D5",        # 1F, 31
        "Function_32_741D",        # 20, 32
        "Function_33_7465",        # 21, 33
        "Function_34_74AD",        # 22, 34
        "Function_35_7848",        # 23, 35
        "Function_36_7CE0",        # 24, 36
        "Function_37_8357",        # 25, 37
        "Function_38_8B17",        # 26, 38
        "Function_39_9193",        # 27, 39
        "Function_40_92AE",        # 28, 40
        "Function_41_99F1",        # 29, 41
        "Function_42_AFFA",        # 2A, 42
        "Function_43_B06C",        # 2B, 43
        "Function_44_B0DE",        # 2C, 44
        "Function_45_C045",        # 2D, 45
        "Function_46_D153",        # 2E, 46
        "Function_47_D5F8",        # 2F, 47
        "Function_48_D632",        # 30, 48
        "Function_49_D6B9",        # 31, 49
        "Function_50_D746",        # 32, 50
        "Function_51_D92F",        # 33, 51
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_6AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A1")
    SetChrChipByIndex(0xA, 20)
    SetChrPos(0xA, -910, 2000, 89640, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_4A1")

    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_547")
    SetChrPos(0x16, 1860, 2000, 89340, 0)
    ClearChrFlags(0x16, 0x80)
    OP_43(0x16, 0x0, 0x0, 0x2)
    SetChrPos(0x17, 2460, 2000, 88510, 0)
    ClearChrFlags(0x17, 0x80)
    OP_43(0x17, 0x0, 0x0, 0x2)
    SetChrPos(0x18, 3480, 0, -840, 270)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0x15, 24)
    SetChrPos(0x15, 130, 2000, 91480, 0)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x2)
    Jump("loc_6A7")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5CE")
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xF, -2660, 0, 99090, 315)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 11)
    ClearChrFlags(0xF, 0x10)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -840, 0, 97770, 45)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_5CB")

    Jump("loc_6A7")

    label("loc_5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_61F")
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    OP_43(0xC, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_61C")

    Jump("loc_6A7")

    label("loc_61F")

    SetChrPos(0xE, -920, 0, 97790, 0)
    ClearChrFlags(0xE, 0x10)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 13)
    OP_43(0xE, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 370, 0, 97940, 45)
    ClearChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 12)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0xC, -1600, 2000, 91460, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x15, 24)
    SetChrPos(0x15, 130, 2000, 91480, 270)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x2)

    label("loc_6A7")

    Jump("loc_908")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_70F")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70C")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_70C")

    Jump("loc_908")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_779")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_776")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_776")

    Jump("loc_908")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_824")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 530, 0, 98030, 90)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_821")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)

    label("loc_821")

    Jump("loc_908")

    label("loc_824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_8B2")
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_894")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_894")

    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_908")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_8C1")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_908")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_908")
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xA, -2290, 2000, 91270, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_929")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    Event(0, 41)
    Jump("loc_BE6")

    label("loc_929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    Event(0, 44)
    Jump("loc_BE6")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    Event(0, 45)
    Jump("loc_BE6")

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    Event(0, 46)
    Jump("loc_BE6")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    Event(1, 12)
    Jump("loc_BE6")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    Event(1, 13)
    Jump("loc_BE6")

    label("loc_9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_9ED")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_BE6")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_A0C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_BE6")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_A2B")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_BE6")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_A4A")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_BE6")

    label("loc_A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_A69")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_BE6")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_A88")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_BE6")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_AA7")
    OP_A3(0x10F6)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_BE6")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_AC6")
    OP_A3(0x10F7)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 24)
    Jump("loc_BE6")

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_AE5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F8)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_BE6")

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_BE6")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_B2A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    SetMapFlags(0x10000000)
    Event(0, 34)
    Jump("loc_BE6")

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_B49")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FA)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_BE6")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_B68")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FB)
    SetMapFlags(0x10000000)
    Event(0, 37)
    Jump("loc_BE6")

    label("loc_B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_B87")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FC)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_BE6")

    label("loc_B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_BA6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FD)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_BE6")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_END)), "loc_BC5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FE)
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_BE6")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE6")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_BE6")

    Return()

    # Function_0_472 end

    def Function_1_BE7(): pass

    label("Function_1_BE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C05")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C05")

    Call(0, 9)
    Call(0, 8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2B")
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)

    label("loc_C2B")

    Jump("loc_C3F")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C68")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C75")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C75")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_C75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA0")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_CA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC6")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_CE4")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    Jump("loc_D4F")

    label("loc_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_CEE")
    Jump("loc_D4F")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_D0C")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    Jump("loc_D4F")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_D2F")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    OP_1B(0xA, 0x0, 0x32)
    Jump("loc_D4F")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4F")
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)

    label("loc_D4F")

    Return()

    # Function_1_BE7 end

    def Function_2_D50(): pass

    label("Function_2_D50")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D75")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_EB7")

    label("loc_D75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_EB7")

    label("loc_D8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_EB7")

    label("loc_DA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_EB7")

    label("loc_DC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_EB7")

    label("loc_DD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_EB7")

    label("loc_DF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_EB7")

    label("loc_E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E24")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_EB7")

    label("loc_E24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_EB7")

    label("loc_E3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_EB7")

    label("loc_E56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_EB7")

    label("loc_E6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E88")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_EB7")

    label("loc_E88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_EB7")

    label("loc_EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_EB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_EB7")

    label("loc_ECC")

    Return()

    # Function_2_D50 end

    def Function_3_ECD(): pass

    label("Function_3_ECD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1B42")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "离开\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F35"),
        (1, "loc_1B10"),
        (2, "loc_1B3C"),
        (SWITCH_DEFAULT, "loc_1B3F"),
    )


    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_END)), "loc_1265")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(    #0
        0xA,
        (
            "#1162F啊，各位……\x02\x03",

            "中枢塔的情况\x01",
            "怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1003F嗯，一下子就受到了\x01",
            "执行者的欢迎了。\x02\x03",

            "#1007F……那个『怪盗绅士』。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #2
        0xA,
        "#1163F呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1040F不过他答应我们\x01",
            "收手了……\x02\x03",

            "所以科洛丝也可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #4
        0xA,
        (
            "#1167F是吗……\x02\x03",

            "#1382F呼，感觉心里的\x01",
            "一块石头落地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1016F哈哈，我能理解你的心情。\x02\x03",

            "布卢布兰不知为什么，\x01",
            "对科洛丝很执着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1035F不过，接下来肯定还有\x01",
            "其他执行者在等着……\x02\x03",

            "#1042F提高警觉继续探索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        "#1162F嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1006F嗯！　明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A5)
    Jump("loc_118F")

    label("loc_1136")


    ChrTalk(    #9
        0x105,
        (
            "#1162F他能够收手\x01",
            "真是个好消息……\x02\x03",

            "不过还是不能\x01",
            "掉以轻心呢。\x02\x03",

            "请大家\x01",
            "一定要小心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    Jump("loc_1262")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(    #10
        0xA,
        (
            "#1167F他能够收手，\x01",
            "说实话，我真是松了口气。\x02\x03",

            "#1162F不过，还是不能\x01",
            "掉以轻心呢。\x02\x03",

            "各位，接下来也请\x01",
            "提高警觉继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_1262")

    label("loc_121B")


    ChrTalk(    #11
        0xA,
        (
            "#1162F接下来的战斗应该还是\x01",
            "不能够掉以轻心的……\x02\x03",

            "提起精神前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1262")

    Jump("loc_1B0D")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(    #12
        0xA,
        (
            "#1167F接下来在舰桥\x01",
            "好像要进行重要的测试。\x02\x03",

            "看来修复工程也快要\x01",
            "接近尾声了。\x02\x03",

            "#1162F希望我们能完成使命，\x01",
            "全体成员一起回到地面上。\x02\x03",

            "各位……\x01",
            "即使到最后一刻都请不要放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_1394")

    label("loc_132A")


    ChrTalk(    #13
        0x105,
        (
            "#1160F希望我们能完成使命，\x01",
            "全体成员一起回到地面上。\x02\x03",

            "那么，诸位……\x01",
            "即使到最后一刻都请不要放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1394")

    Jump("loc_1B0D")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_14B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145B")

    ChrTalk(    #14
        0xA,
        (
            "#1160F空贼团的各位\x01",
            "也能平安无事真是太好了。\x02\x03",

            "他们好像来得\x01",
            "比我们还要早。\x02\x03",

            "关于浮游都市\x01",
            "他们或许会有什么\x01",
            "有用的情报也说不定。\x02\x03",

            "有机会过去拜访一下\x01",
            "他们的话可能也很有意义。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_14AD")

    label("loc_145B")


    ChrTalk(    #15
        0xA,
        (
            "#1160F空贼团的各位好像\x01",
            "比我们还要早。\x02\x03",

            "他们或许会有什么\x01",
            "有用的情报也说不定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AD")

    Jump("loc_1B0D")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_19ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183E")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #16
        0xA,
        (
            "#1168F乔丝特小姐……\x01",
            "欢迎来到埃尔赛尤号。\x02\x03",

            "很不巧正值修复作业中，\x01",
            "无法好好地招待您……\x02\x03",

            "请把这里当作自己的船，\x01",
            "不要拘束。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10B,
        (
            "#414F嗯、嗯……谢谢。\x02\x03",

            "#415F嘿嘿，受到这样的欢迎，\x01",
            "感觉身上都痒起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 400)

    ChrTalk(    #18
        0x101,
        (
            "#1019F真、真不卫生……\x01",
            "你几天没洗澡了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(    #19
        0x10B,
        (
            "#216F笨、笨蛋！\x01",
            "我不是这个意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1016F对、对不起对不起。\x01",
            "我知道的，只是顺口说出来而已……\x02\x03",

            "你想，一提到空贼\x01",
            "总有种肮脏的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10B,
        (
            "#212F哼，清一色的男人才会这样吧？\x02\x03",

            "#210F我们打扫和洗衣服的工作都是\x01",
            "我在做，堪称完美。\x02\x03",

            "说清楚一点，\x01",
            "就是毫不逊色于这艘船。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(    #22
        0x102,
        (
            "#1040F的确……\x01",
            "飞船内确实出人意料地整洁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10B,
        "#211F嘿嘿，没错吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #24
        0x101,
        (
            "#1015F哦～原来如此……\x02\x03",

            "#1019F……等等，约修亚为什么\x01",
            "要帮乔丝特说话？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #25
        0x102,
        (
            "#1044F咦……！？\x02\x03",

            "我、我没有帮她说话啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "#1167F咳、咳………\x02\x03",

            "#1382F总、总之希望\x01",
            "大家都能和睦相处。\x02\x03",

            "在这种情况下，\x01",
            "合作比什么都重要。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_A2(0x22A6)
    Jump("loc_19EA")

    label("loc_183E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18A7")

    ChrTalk(    #27
        0xA,
        (
            "#1382F总、总之希望\x01",
            "大家珍惜船上的和谐氛围。\x02\x03",

            "在这种情况下，\x01",
            "合作比什么都重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EA")

    label("loc_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195F")

    ChrTalk(    #28
        0xA,
        (
            "#1167F不管过去发生过什么，\x01",
            "现在都处于同样的境遇下……\x02\x03",

            "与空贼团的各位互相帮助，\x01",
            "我想是理所当然的。\x02\x03",

            "#1160F尤莉亚小姐那边\x01",
            "我会去解释的。\x02\x03",

            "各位请专注于\x01",
            "都市的探索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_19EA")

    label("loc_195F")


    ChrTalk(    #29
        0xA,
        (
            "#1167F不管过去发生过什么，\x01",
            "现在都处于同样的境遇下……\x02\x03",

            "#1160F与空贼团的各位互相帮助，\x01",
            "我想是理所当然的。\x02\x03",

            "各位请专注于\x01",
            "都市的探索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EA")

    Jump("loc_1B0D")

    label("loc_19ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")

    ChrTalk(    #30
        0xA,
        (
            "#1162F现在船员们正在\x01",
            "确认受损的位置。\x02\x03",

            "等到确认完成，就应该会\x01",
            "展开修复工作吧。\x02\x03",

            "#1167F接下来不知道还会\x01",
            "发生些什么……\x02\x03",

            "总之要尽快\x01",
            "飞起来才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_1B0D")

    label("loc_1A98")


    ChrTalk(    #31
        0xA,
        (
            "#1162F等确认完损伤情况，就应该会\x01",
            "展开修复工作吧。\x02\x03",

            "接下来不知道还会\x01",
            "发生些什么。\x02\x03",

            "应该要尽快恢复\x01",
            "飞行能力才好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0D")

    Jump("loc_1B3F")

    label("loc_1B10")


    ChrTalk(    #32
        0xA,
        (
            "#1160F明白了。\x01",
            "要更换成员是吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_1B3F")

    label("loc_1B3C")

    Jump("loc_1B3F")

    label("loc_1B3F")

    Jump("loc_2649")

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_22AE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BA7"),
        (1, "loc_227D"),
        (2, "loc_22A8"),
        (SWITCH_DEFAULT, "loc_22AB"),
    )


    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_1EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3D")

    ChrTalk(    #33
        0xA,
        (
            "#043F在最后之塔上等待我们的执行者……\x01",
            "似乎是那个玲呢。\x02\x03",

            "就像艾丝蒂尔所说的，\x01",
            "真希望她快点醒悟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1003F虽然不知道我们的话\x01",
            "她能听进去多少……\x02\x03",

            "#1002F不过我们会尽力一试的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#1035F是啊……\x01",
            "只能尽力而为了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE2")

    ChrTalk(    #36
        0x106,
        (
            "#051F嗯，就这么做吧。\x02\x03",

            "要救那个女孩子，\x01",
            "也没其他的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE8")

    label("loc_1CE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #37
        0x108,
        (
            "#070F按照游击士的精神，\x01",
            "就应该这么做。\x02\x03",

            "要救那个女孩子，\x01",
            "也没其他的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE8")

    label("loc_1D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D95")

    ChrTalk(    #38
        0x103,
        (
            "#020F嗯，就这么做吧。\x02\x03",

            "要救那个女孩子，\x01",
            "也没其他的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE8")

    label("loc_1D95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE8")

    ChrTalk(    #39
        0x109,
        (
            "#1067F本来就应该这么做呢。\x02\x03",

            "要救那个女孩子，\x01",
            "也没其他的办法了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE8")


    ChrTalk(    #40
        0xA,
        (
            "#047F我们的声音一定\x01",
            "可以传达到玲的心中。\x02\x03",

            "#040F现在就相信那个女孩的心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4B)
    Jump("loc_1EA1")

    label("loc_1E3D")


    ChrTalk(    #41
        0xA,
        (
            "#047F我们的声音一定\x01",
            "可以传达到玲的心中……\x02\x03",

            "#040F现在就相信那个女孩的心，\x01",
            "然后一切尽力而为吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA1")

    Jump("loc_227A")

    label("loc_1EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_20E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209C")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #42
        0xA,
        (
            "#040F啊……\x01",
            "艾丝蒂尔，约修亚。\x02\x03",

            "刚才收到了玛诺利亚\x01",
            "守备队的联络。\x02\x03",

            "特蕾莎老师和孩子们\x01",
            "已经安全避难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1004F啊，真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        "#047F嗯，大家都很好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1007F呼～太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#1040F嗯……\x01",
            "暂时可以安心了。\x02\x03",

            "#1043F不过，塔还是那副样子……\x01",
            "依然不能掉以轻心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#026F嗯，这时候高兴\x01",
            "还为时过早。\x02\x03",

            "#022F现在就调整好心情\x01",
            "向塔出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1002F嗯……说得也是。\x02\x03",

            "那么我们先走了，科洛丝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#042F嗯，需要我的话\x01",
            "随时都可以来找我。\x02\x03",

            "那么各位，\x01",
            "一定要小心……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_20E3")

    label("loc_209C")


    ChrTalk(    #50
        0xA,
        (
            "#040F院长和孤儿院的孩子们\x01",
            "似乎都顺利地避难了。\x02\x03",

            "暂时可以\x01",
            "放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E3")

    Jump("loc_227A")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_227A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2239")

    ChrTalk(    #51
        0xA,
        (
            "#040F蔡斯的守备队\x01",
            "也正在努力呢。\x02\x03",

            "目前防卫线\x01",
            "似乎还没被打破。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1011F是吗……\x01",
            "也就是说可以暂时放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2198")

    ChrTalk(    #53
        0x107,
        "#561F可是可是，我还是很担心……\x02",
    )

    CloseMessageWindow()

    label("loc_2198")


    ChrTalk(    #54
        0x102,
        (
            "#1042F我们还是赶紧\x01",
            "去调查塔吧。\x02\x03",

            "对蔡斯的攻击\x01",
            "应该是声东击西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x108,
        (
            "#072F是啊。\x01",
            "塔一定是要害。\x02\x03",

            "现在应该优先\x01",
            "考虑制服执行者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1002F嗯，我明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_227A")

    label("loc_2239")


    ChrTalk(    #57
        0xA,
        (
            "#040F蔡斯的防卫线\x01",
            "据说还没被打破。\x02\x03",

            "我们也赶紧\x01",
            "去压制塔吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227A")

    Jump("loc_22AB")

    label("loc_227D")


    ChrTalk(    #58
        0xA,
        (
            "#040F明白了。\x01",
            "要更换成员是吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_22AB")

    label("loc_22A8")

    Jump("loc_22AB")

    label("loc_22AB")

    Jump("loc_2649")

    label("loc_22AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_2649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EA")
    OP_4A(0xFE, 255)

    ChrTalk(    #59
        0xA,
        (
            "#040F哎呀，艾丝蒂尔。\x02\x03",

            "莫非你\x01",
            "心情平静不下来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1000F嗯，有一点。\x01",
            "总是无法静静地坐在座位上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        (
            "#045F对了，你在定期船上\x01",
            "也一直会散步吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "被你这么一说倒也是。\x02\x03",

            "举止得体地坐着\x01",
            "总觉得绑手绑脚的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#048F呵呵……\x01",
            "果然像是艾丝蒂尔会说的话。\x02\x03",

            "不过在『埃尔赛尤』上\x01",
            "你不必担心这个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1011F咦？怎么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        (
            "#047F虽然所属于王室，\x01",
            "不过这艘船是巡洋舰……\x02\x03",

            "和普通的飞行客船\x01",
            "运动性能相差悬殊。\x02\x03",

            "#040F用最大战速飞行的话\x01",
            "要想站着都很困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1004F这、这么厉害啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "#048F呵呵，你一定会吓一跳的哦。\x02\x03",

            "简直像遭遇暴风雨一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1004F是、是这样啊……\x02\x03",

            "#1015F那么，现在一定是\x01",
            "暴风雨前的寂静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#047F嗯，你说得没错……\x01",
            "有可能只是片刻的平静。\x02\x03",

            "#040F如果你要在舰内参观，\x01",
            "就要趁现在哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1006F哦，说得也是。\x02\x03",

            "那么我就去\x01",
            "继续散步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "#040F嗯，那么回头见。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A21)
    Jump("loc_2649")

    label("loc_25EA")


    ChrTalk(    #72
        0xA,
        (
            "#040F正如艾丝蒂尔所说，\x01",
            "现在是暴风雨前的寂静。\x02\x03",

            "如果要在舰内参观的话，\x01",
            "或许只能趁现在了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2649")

    TalkEnd(0xFE)
    Return()

    # Function_3_ECD end

    def Function_4_264D(): pass

    label("Function_4_264D")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "离开\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26AE"),
        (1, "loc_29AC"),
        (2, "loc_29CC"),
        (SWITCH_DEFAULT, "loc_29CF"),
    )


    label("loc_26AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2966")

    ChrTalk(    #73
        0x12,
        (
            "#052F怎么了？你们。\x02\x03",

            "还在这种地方\x01",
            "转来转去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1000F嗯，还想再整顿\x01",
            "一下装备嘛。\x02\x03",

            "倒是阿加特你，\x01",
            "为什么会在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #75
        0x12,
        (
            "#050F要支援你们的话，\x01",
            "这里是最方便的了。\x02\x03",

            "在舰桥上可以完全\x01",
            "掌握外界的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1028F哦～这些话听起来\x01",
            "嘴上功夫倒是很厉害嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        "#1040F拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x12,
        (
            "#050F可别勉强啊。\x01",
            "不管怎么说对手都不简单。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_282B")

    ChrTalk(    #79
        0x107,
        "#062F是、是的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B8")

    label("loc_282B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_285B")

    ChrTalk(    #80
        0x103,
        "#022F嗯，有必要特别小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B8")

    label("loc_285B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288B")

    ChrTalk(    #81
        0x108,
        "#072F嗯，应该慎重地前进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B8")

    label("loc_288B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28B8")

    ChrTalk(    #82
        0x105,
        "#042F是……我们会小心的。\x02",
    )

    CloseMessageWindow()

    label("loc_28B8")


    ChrTalk(    #83
        0x101,
        (
            "#1002F阿加特也是……\x01",
            "麻烦你做好准备哦。\x02\x03",

            "也不知道什么时候\x01",
            "就需要借助你的力量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x12,
        (
            "#051F不用你说我也会这么做。\x02\x03",

            "好了，你们要努力一点，\x01",
            "我会从这里好好地欣赏的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E25)
    Jump("loc_29A9")

    label("loc_2966")


    ChrTalk(    #85
        0x12,
        (
            "#050F我会从这里\x01",
            "观察调查的情况的。\x02\x03",

            "需要我的时候\x01",
            "尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A9")

    Jump("loc_29CF")

    label("loc_29AC")


    ChrTalk(    #86
        0x12,
        "#050F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    Jump("loc_29CF")

    label("loc_29CC")

    Jump("loc_29CF")

    label("loc_29CF")

    TalkEnd(0xFE)
    Return()

    # Function_4_264D end

    def Function_5_29D3(): pass

    label("Function_5_29D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AD9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A6F")
    Jump("loc_2AB1")

    label("loc_2A6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A8B")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AB1")

    label("loc_2A8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AA7")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AB1")

    label("loc_2AA7")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AB1")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_2ADC")

    label("loc_2AD9")

    TalkBegin(0xFE)

    label("loc_2ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2BDB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B63")

    ChrTalk(    #87
        0xC,
        (
            "#178F接下来要进行\x01",
            "飞翔引擎的驱动测试。\x02\x03",

            "待殿下回来的时候，\x01",
            "我们一定会让船恢复可飞行的状态。\x02\x03",

            "请您耐心期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD8")

    label("loc_2B63")


    ChrTalk(    #88
        0xC,
        (
            "#178F接下来要进行\x01",
            "飞翔引擎的驱动测试。\x02\x03",

            "等各位回来的时候，\x01",
            "我们一定会让船恢复可飞行的状态。\x02\x03",

            "你们就耐心期待吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD8")

    Jump("loc_43B1")

    label("loc_2BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_2EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C44")

    ChrTalk(    #89
        0xC,
        (
            "#170F空贼团那帮家伙\x01",
            "已经得救了吧。\x02\x03",

            "刚才，从他们的飞艇上\x01",
            "传来了通讯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C8B")

    label("loc_2C44")


    ChrTalk(    #90
        0xC,
        (
            "#170F空贼团那帮家伙\x01",
            "已经得救了吧。\x02\x03",

            "从他们的飞艇上\x01",
            "刚传来了通讯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8B")


    ChrTalk(    #91
        0x101,
        "#1011F啊，已经取得联络了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #92
        0xC,
        (
            "#170F嗯，他们也在\x01",
            "忙着修船呢。\x02\x03",

            "#176F虽然和他们合作\x01",
            "让人有点无法接受……\x02\x03",

            "不过在这种状况下也没办法。\x01",
            "我也要遵从指示。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x22AB)
    Jump("loc_2EDE")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2E23")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB4")

    ChrTalk(    #93
        0xC,
        (
            "#170F空贼团的各位\x01",
            "似乎也在忙着修船。\x02\x03",

            "#176F想不到会在这种地方\x01",
            "遭遇同样的困境……\x02\x03",

            "命运真是讽刺呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2DB4")


    ChrTalk(    #94
        0xC,
        (
            "#170F空贼团的各位\x01",
            "似乎也在忙着修船。\x02\x03",

            "呼，想不到会在这种地方\x01",
            "#176F遇上同样的困境……\x02\x03",

            "命运真是讽刺呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E20")

    Jump("loc_2EDE")

    label("loc_2E23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E87")

    ChrTalk(    #95
        0xC,
        (
            "#170F从空贼团的飞艇上\x01",
            "传来了通讯。\x02\x03",

            "目前应该先确认一下\x01",
            "有没有物资不足的情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EDE")

    label("loc_2E87")


    ChrTalk(    #96
        0xC,
        (
            "#170F从空贼团的飞艇上\x01",
            "刚传来了通讯。\x02\x03",

            "目前应该先确认一下\x01",
            "有没有物资不足的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDE")

    Jump("loc_43B1")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE1")
    TurnDirection(0xC, 0x10B, 0)

    ChrTalk(    #97
        0xC,
        (
            "#178F哟，你就是乔丝特啊。\x02\x03",

            "本来我是不愿意和\x01",
            "罪犯一起合作的……\x02\x03",

            "不过在这种状况下也没办法。\x01",
            "我就特别准许你登舰吧。\x02\x03",

            "不过你也要认真\x01",
            "帮大家一起工作哦。\x02\x03",

            "和其他船员一起\x01",
            "帮忙作业吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10B,
        "#212F嗯、嗯……我知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22AA)
    Jump("loc_3066")

    label("loc_2FE1")

    TurnDirection(0xC, 0x10B, 0)

    ChrTalk(    #99
        0xC,
        (
            "#178F因为现在是这样的状况。\x01",
            "就特别准许你登舰吧。\x02\x03",

            "不过你也要认真\x01",
            "帮大家一起工作哦。\x02\x03",

            "有空闲的话就去帮忙\x01",
            "船员们的作业吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3066")

    Jump("loc_3175")

    label("loc_3069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311E")

    ChrTalk(    #100
        0xC,
        (
            "#178F哟，各位。\x01",
            "你们救了空贼小姑娘吗。\x02\x03",

            "#176F和罪犯一起合作\x01",
            "罪犯一起合作的……\x02\x03",

            "不过在这种状况下也没办法。\x01",
            "我就特别准许你登舰吧。\x02\x03",

            "#178F毕竟也不能把她\x01",
            "丢在野外。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3175")

    label("loc_311E")


    ChrTalk(    #101
        0xC,
        (
            "#170F对空贼小姑娘，\x01",
            "我就特别准许你登舰吧。\x02\x03",

            "不过，当然也会为此\x01",
            "要求她好好地工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3175")

    Jump("loc_43B1")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3236")

    ChrTalk(    #102
        0xC,
        (
            "#170F现在最大的问题\x01",
            "就是修复要用到的材料……\x02\x03",

            "总之准备先把船体的碎片\x01",
            "再加工后使用。\x02\x03",

            "虽然说这毕竟只是应急措施，\x01",
            "不过应该能充分具备\x01",
            "可以承受飞行的强度。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3289")

    label("loc_3236")


    ChrTalk(    #103
        0xC,
        (
            "#170F修复工作所用的材料\x01",
            "准备使用船体的碎片。\x02\x03",

            "回收部队已经在船外\x01",
            "展开活动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3289")

    Jump("loc_33B4")

    label("loc_328C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3352")

    ChrTalk(    #104
        0xC,
        (
            "#178F修复工作所用的材料\x01",
            "准备使用船体的碎片。\x02\x03",

            "当前，队员们\x01",
            "正在进行回收工作。\x02\x03",

            "用人力来回收\x01",
            "或许相当地辛苦，\x01",
            "不过现在也没有其他的办法了。\x02\x03",

            "抱歉，如果你们哪位有空的话\x01",
            "请过去帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_33B4")

    label("loc_3352")


    ChrTalk(    #105
        0xC,
        (
            "#178F为了进行修复工作，\x01",
            "队员们\x01",
            "正在回收船体的碎片。\x02\x03",

            "抱歉，如果你们哪位有空的话\x01",
            "请过去帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B4")

    Jump("loc_43B1")

    label("loc_33B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_37B7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3550")

    ChrTalk(    #106
        0xC,
        (
            "#178F在下一座塔上等待的\x01",
            "是手持巨大镰刀的少女……\x02\x03",

            "她一定就是那个在背后\x01",
            "指挥凯诺娜事件的人了。\x02\x03",

            "#176F本来应该由我亲自前去\x01",
            "对其进行制裁的……\x02\x03",

            "现在这个责任就\x01",
            "落到殿下的肩上了。\x02\x03",

            "#178F为了女王陛下，\x01",
            "请一并替在下完成使命吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x105,
        (
            "#040F虽然我不认为自己\x01",
            "能替代尤莉亚小姐……\x02\x03",

            "不过我会和大家携手\x01",
            "一同努力的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #108
        0xC,
        "#172F是！　祝您旗开得胜。\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1E48)
    Jump("loc_3632")

    label("loc_3550")


    ChrTalk(    #109
        0xC,
        (
            "#178F在下一座塔上等待的\x01",
            "是手持巨大镰刀的少女……\x02\x03",

            "#176F本来应该由我亲自前去\x01",
            "对其进行制裁的……\x02\x03",

            "现在这个责任就\x01",
            "落到殿下的肩上了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #110
        0xC,
        (
            "#172F为了女王陛下，\x01",
            "请一并替在下完成使命吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x8)

    label("loc_3632")

    Jump("loc_37B4")

    label("loc_3635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3730")

    ChrTalk(    #111
        0xC,
        (
            "#178F下一个执行者是手持巨大镰刀的少女……\x02\x03",

            "她一定就是那个在背后\x01",
            "指挥凯诺娜事件的人了。\x02\x03",

            "#176F本来应该是\x01",
            "由我来制裁她的……\x02\x03",

            "现在就把这个任务交给\x01",
            "接受了陛下命令的各位吧。\x02\x03",

            "#178F我尤莉亚的心愿就托付给各位了。\x01",
            "……请各位尽量放手去做。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_37B4")

    label("loc_3730")


    ChrTalk(    #112
        0xC,
        (
            "#178F既然是扰乱过王都秩序的对手，\x01",
            "本该由我亲自来制裁……\x02\x03",

            "现在就把这个任务交给\x01",
            "接受了陛下命令的各位吧。\x01",
            "请各位尽量放手去做吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B4")

    Jump("loc_43B1")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3992")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385A")

    ChrTalk(    #113
        0xC,
        (
            "#170F卢安近郊的守备队\x01",
            "顺利抵达了玛诺利亚村。\x02\x03",

            "他们报告说街道附近的居民\x01",
            "也已经完成避难了……\x02\x03",

            "似乎总算是度过了\x01",
            "危急的状况啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_38AD")

    label("loc_385A")


    ChrTalk(    #114
        0xC,
        (
            "#170F卢安近郊的守备队\x01",
            "顺利抵达了玛诺利亚村。\x02\x03",

            "似乎总算是度过了\x01",
            "危急的状况啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AD")

    Jump("loc_398F")

    label("loc_38B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393C")

    ChrTalk(    #115
        0xC,
        (
            "#170F卢安近郊的守备队\x01",
            "顺利抵达了玛诺利亚村。\x02\x03",

            "他们报告说街道附近的居民\x01",
            "也已经完成避难了……\x02\x03",

            "总算是度过了\x01",
            "危急的状况啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_398F")

    label("loc_393C")


    ChrTalk(    #116
        0xC,
        (
            "#170F卢安近郊的守备队\x01",
            "顺利抵达了玛诺利亚村。\x02\x03",

            "似乎总算是度过了\x01",
            "危急的状况啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398F")

    Jump("loc_43B1")

    label("loc_3992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3B97")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A35")

    ChrTalk(    #117
        0xC,
        (
            "#178F在蔡斯近郊\x01",
            "守备队正在奋战中。\x02\x03",

            "我们赌上王国军人的名誉，\x01",
            "一定会保障城镇的安全。\x02\x03",

            "请不必担心──\x01",
            "殿下请专注于塔的调查上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3A98")

    label("loc_3A35")


    ChrTalk(    #118
        0xC,
        (
            "#178F我们赌上王国军人的名誉，\x01",
            "一定会保障城镇的安全。\x02\x03",

            "请不必担心──\x01",
            "现在请专注于塔的调查上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A98")

    Jump("loc_3B94")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B33")

    ChrTalk(    #119
        0xC,
        (
            "#178F在蔡斯近郊\x01",
            "王国军的守备队正在奋战。\x02\x03",

            "我们赌上王国军人的名誉，\x01",
            "一定会保障蔡斯市区的安全。\x02\x03",

            "请不必担心。\x01",
            "各位请专注于塔的调查上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3B94")

    label("loc_3B33")


    ChrTalk(    #120
        0xC,
        (
            "#178F我们赌上王国军人的名誉，\x01",
            "一定会保障蔡斯的安全。\x02\x03",

            "请不必担心。\x01",
            "各位请专注于塔的调查上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B94")

    Jump("loc_43B1")

    label("loc_3B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3E20")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD6")

    ChrTalk(    #121
        0xC,
        (
            "#170F殿下您可能已经知道了，\x01",
            "下降到地面的时候请使用\x01",
            "货舱的货物升降机。\x02\x03",

            "人员的配置已经完成，\x01",
            "应该随时都能使用。\x02\x03",

            "敌人的实力也相当强──\x01",
            "请一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x105,
        (
            "#040F谢谢你，尤莉亚小姐。\x02\x03",

            "我不在时埃尔赛尤号就\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xC, 29)
    SetChrSubChip(0xC, 0)
    OP_99(0xC, 0x0, 0x1, 0x5DC)

    ChrTalk(    #123
        0xC,
        "#172F是！　请交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x0, 0x5DC)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1E47)
    Jump("loc_3D27")

    label("loc_3CD6")


    ChrTalk(    #124
        0xC,
        (
            "#170F下降到地面的时候请使用\x01",
            "货舱的货物升降机。\x02\x03",

            "那么，殿下──\x01",
            "请保重贵体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D27")

    Jump("loc_3E1D")

    label("loc_3D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC0")

    ChrTalk(    #125
        0xC,
        (
            "#170F下降到地面的时候请使用\x01",
            "货舱的货物升降机。\x02\x03",

            "人员的配置已经完成，\x01",
            "应该随时都能使用。\x02\x03",

            "我期待着各位的奋斗。\x01",
            "──愿女神保佑各位。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3E1D")

    label("loc_3DC0")


    ChrTalk(    #126
        0xC,
        (
            "#170F下降到地面的时候请使用\x01",
            "货舱的货物升降机。\x02\x03",

            "人员的配置已经完成，\x01",
            "应该随时都能使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1D")

    Jump("loc_43B1")

    label("loc_3E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_43B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404D")

    ChrTalk(    #127
        0xC,
        (
            "#170F这不是艾丝蒂尔吗。\x02\x03",

            "『埃尔赛尤』\x01",
            "还让你满意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1001F嗯，当然。\x02\x03",

            "女王陛下的船\x01",
            "果然就是不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xC,
        (
            "#171F承蒙夸奖。\x02\x03",

            "新型引擎总算是赶上了，\x01",
            "我们也才刚放下心来。\x02\x03",

            "#176F本来没想到过会有\x01",
            "这么大规模的作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1007F的确……\x02\x03",

            "谁也想象不到\x01",
            "龙竟然会出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "#178F嗯，对我们来说\x01",
            "是个完全未知的对手。\x02\x03",

            "虽说有万全的计划，\x01",
            "不过也绝不能掉以轻心。\x02\x03",

            "考虑到万一的情况，\x01",
            "应该做好最坏的打算才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1015F我们就是为了以防万一\x01",
            "才被叫来的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        (
            "#175F嗯，我们想尽可能地\x01",
            "不借助各位的力量……\x02\x03",

            "现在只有女神知道\x01",
            "结果会是怎样了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A6D)
    Jump("loc_43B1")

    label("loc_404D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 0)), scpexpr(EXPR_END)), "loc_433F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D9")

    ChrTalk(    #134
        0x101,
        (
            "#1011F啊，对了，尤莉亚小姐。\x02\x03",

            "奈尔那家伙说想要\x01",
            "采访尤莉亚小姐哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "#173F采访……？　找我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1006F嗯，他说想让市民们了解\x01",
            "亲卫队的真实一面。\x02\x03",

            "那家伙对工作很正经，\x01",
            "我觉得这个理由也挺可信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xC,
        (
            "#176F关于他的报导方式，\x01",
            "我也早就有所了解。\x02\x03",

            "不然我也不会允许\x01",
            "他随行采访了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1015F嗯，就事论事的话，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xC,
        (
            "#175F我也完全赞同\x01",
            "他所选择的题材……\x02\x03",

            "可是，这次\x01",
            "我得谢绝他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1004F咦……？　你不是赞成吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "#176F迄今为止，我对其他通讯社\x01",
            "的采访请求都是婉言谢绝。\x02\x03",

            "所以不能只对他的\x01",
            "通讯社开放特例。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1007F嗯、嗯……也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        (
            "#170F抱歉，\x01",
            "请这么转达他吧。\x02\x03",

            "对于报道本身，\x01",
            "我是很期待的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#1015F哦，明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x1A6E)
    Jump("loc_433C")

    label("loc_42D9")


    ChrTalk(    #145
        0xC,
        (
            "#176F很遗憾，我不能接受利贝尔\x01",
            "通讯社的提议。\x02\x03",

            "虽然我赞同他的题材，\x01",
            "不过毕竟以前从未有过先例。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_433C")

    Jump("loc_43B1")

    label("loc_433F")


    ChrTalk(    #146
        0xC,
        (
            "#170F一旦发现古代龙，\x01",
            "作战就随之展开。\x02\x03",

            "我们也会竭尽全力，\x01",
            "但是结果不得而知。\x02\x03",

            "艾丝蒂尔也请\x01",
            "做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43C8")
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Jump("loc_43CB")

    label("loc_43C8")

    TalkEnd(0xFE)

    label("loc_43CB")

    Return()

    # Function_5_29D3 end

    def Function_6_43CC(): pass

    label("Function_6_43CC")

    TalkBegin(0xFE)

    ChrTalk(    #147
        0xFE,
        "#030F◆无台词。\x02",
    )

    CloseMessageWindow()
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    # Function_6_43CC end

    def Function_7_43EC(): pass

    label("Function_7_43EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_441A")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_4435")

    label("loc_441A")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_4435")

    Jump("loc_44B6")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_445B")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_44B6")

    label("loc_445B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_447C")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_44B6")

    label("loc_447C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_449D")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_44B6")

    label("loc_449D")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_44B6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4583")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4507")
    SetChrChipByIndex(0xA, 20)
    SetChrPos(0xA, -910, 2000, 89640, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_4507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4511")
    Jump("loc_4580")

    label("loc_4511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_454C")
    OP_8C(0xA, 45, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4549")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_4549")

    Jump("loc_4580")

    label("loc_454C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4580")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_457D")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3280, 0, 260, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_457D")

    Jump("loc_4580")

    label("loc_4580")

    Jump("loc_4640")

    label("loc_4583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_45B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45AD")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_45AD")

    Jump("loc_4640")

    label("loc_45B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_45DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45DA")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_45DA")

    Jump("loc_4640")

    label("loc_45DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_460A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4607")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_4607")

    Jump("loc_4640")

    label("loc_460A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4640")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4640")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_4640")

    OP_0D()
    Return()

    # Function_7_43EC end

    def Function_8_4642(): pass

    label("Function_8_4642")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4666")
    OP_10(0x0, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0x7, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0xA, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_46BE")

    label("loc_4666")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468A")
    OP_10(0x9, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0xA, 0x0)
    OP_10(0x8, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_46BE")

    label("loc_468A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_46A9")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0xB, 0x1)
    OP_10(0xA, 0x1)
    OP_10(0x8, 0x0)
    OP_10(0x1, 0x0)
    Jump("loc_46BE")

    label("loc_46A9")

    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x0)
    OP_10(0xA, 0x1)

    label("loc_46BE")

    Return()

    # Function_8_4642 end

    def Function_9_46BF(): pass

    label("Function_9_46BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_4701")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    Jump("loc_476C")

    label("loc_4701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4732")
    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_72(0xF, 0x4)
    Jump("loc_476C")

    label("loc_4732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 7)), scpexpr(EXPR_END)), "loc_474A")
    OP_B1("E0310_2")
    OP_71(0x19, 0x4)
    Jump("loc_476C")

    label("loc_474A")

    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)

    label("loc_476C")

    Jump("loc_4918")

    label("loc_476F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_END)), "loc_47AC")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_72(0xE, 0x4)
    Jump("loc_4882")

    label("loc_47AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_47D3")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_4882")

    label("loc_47D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_47FA")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    Jump("loc_4882")

    label("loc_47FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 7)), scpexpr(EXPR_END)), "loc_482B")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_4882")

    label("loc_482B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4852")
    OP_B1("E0310_4")
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_4882")

    label("loc_4852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 0)), scpexpr(EXPR_END)), "loc_4879")
    OP_B1("E0310_4")
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x14, 0x4)
    Jump("loc_4882")

    label("loc_4879")

    OP_B1("E0310_3")

    label("loc_4882")

    Jump("loc_4918")

    label("loc_4885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_48B1")
    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_4918")

    label("loc_48B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48F1")
    OP_B1("E0310_1")
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    Jump("loc_4918")

    label("loc_48F1")

    OP_B1("E0310_1")
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)

    label("loc_4918")

    Return()

    # Function_9_46BF end

    def Function_10_4919(): pass

    label("Function_10_4919")

    EventBegin(0x0)
    OP_22(0xAB, 0x1, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("尤莉亚上尉")

    AnonymousTalk(    #148
        (
            "\x07\x05巡逻艇『梅尔杰号』传来联络！\x02\x03",

            "在玛鲁加矿山上空\x01",
            "发现了飞行中的龙！\x02\x03",

            "全体船员立刻前往工作岗位！\x02\x03",

            "协会有关人员\x01",
            "请迅速前来舰桥！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #149
        0x101,
        "#1005F──来了呢！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_4919 end

    def Function_11_4A13(): pass

    label("Function_11_4A13")

    EventBegin(0x0)
    OP_6D(-470, 2000, 93430, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(300)
    OP_43(0x101, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x8, 0x0, 0x0, 0xD)
    Sleep(500)
    OP_43(0x9, 0x0, 0x0, 0xF)
    Sleep(500)
    OP_43(0xB, 0x0, 0x0, 0xE)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #150
        0x101,
        "#1005F#6P现在怎么样了！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 225, 400)
    OP_8C(0xA, 180, 400)

    ChrTalk(    #151
        0xD,
        (
            "#160F#5P你们也听到了，\x01",
            "龙出现在了玛鲁加矿山上空。\x02\x03",

            "请看显示器。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B75():
        OP_6D(720, 2000, 95220, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B75)

    def lambda_4B8D():
        OP_67(0, 5150, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4B8D)
    OP_8C(0xD, 45, 400)

    def lambda_4BAC():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BAC)
    Sleep(50)

    def lambda_4BBF():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BBF)
    Sleep(50)

    def lambda_4BD2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4BD2)
    Sleep(50)

    def lambda_4BE5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4BE5)
    Sleep(50)

    def lambda_4BF8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BF8)
    WaitChrThread(0x101, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x3C)
    Sleep(150)
    OP_22(0x127, 0x0, 0x64)
    OP_73(0xC)
    OP_22(0x9D, 0x0, 0x64)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x1)
    OP_74(0xC, 0x8, 0x1)
    OP_74(0xC, 0xA, 0x1)
    OP_0D()
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_AD(0x24010E, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #152
        (
            "\x07\x00#1002F玛鲁加矿山……\x01",
            "出现在洛连特了啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #153
        "\x07\x00#022F终于发现了呢……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #154
        0xC,
        (
            "#178F#5P迎击地点\x01",
            "设定在哪里？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(400)

    ChrTalk(    #155
        0xD,
        (
            "#163F#2P让我看看……\x02\x03",

            "虽说要诱导到湖上，\x01",
            "不过不能让它接近王都。\x02\x03",

            "#160F──迎击地点\x01",
            "就定在雷那特川河口附近！\x02\x03",

            "巡逻艇沿着河岸诱导龙！\x02\x03",

            "攻击艇立刻出发！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xC,
        "#170F#5P是，长官！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #157
        0xC,
        (
            "#176F#6P──这里是『埃尔赛尤』。\x01",
            "通告作战行动中的全舰艇。\x02\x03",

            "#178F迎击地点\x01",
            "就设定在雷那特川河口附近！\x02\x03",

            "全巡逻艇以B队形沿着河岸\x01",
            "将龙诱导到迎击地点。\x02\x03",

            "全攻击艇立刻出发，\x01",
            "迅速赶往迎击地点。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_4A13 end

    def Function_12_4ED7(): pass

    label("Function_12_4ED7")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4EFE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EFE)
    OP_8E(0xFE, 0xFFFFFB6E, 0x7D0, 0x1659E, 0x1388, 0x0)
    Return()

    # Function_12_4ED7 end

    def Function_13_4F1F(): pass

    label("Function_13_4F1F")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4F46():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F46)
    OP_8E(0xFE, 0xFFFFF6AA, 0x7D0, 0x163AA, 0x1388, 0x0)
    Return()

    # Function_13_4F1F end

    def Function_14_4F67(): pass

    label("Function_14_4F67")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4F8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F8E)
    OP_8E(0xFE, 0xFFFFF9B6, 0x7D0, 0x15EC8, 0x1388, 0x0)
    Return()

    # Function_14_4F67 end

    def Function_15_4FAF(): pass

    label("Function_15_4FAF")

    SetChrPos(0xFE, -1040, 2000, 83000, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4FD6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FD6)
    OP_8E(0xFE, 0xFFFFFF4C, 0x7D0, 0x1630A, 0x1388, 0x0)
    Return()

    # Function_15_4FAF end

    def Function_16_4FF7(): pass

    label("Function_16_4FF7")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToDark(0, 0, -1)
    OP_AD(0x24010F, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #158
        0xC,
        (
            "#178F#5P全攻击艇出发完毕。\x02\x03",

            "部署完成的预定时间是\x01",
            "１２:２０。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "#163F#2P嗯……\x02\x03",

            "#160F『埃尔赛尤』出发。\x01",
            "迅速赶往迎击地点的西南方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xC,
        "#170F#5P是，长官。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #161
        0xC,
        (
            "#178F#6P恢复对各部位的导力传达。\x02\x03",

            "『埃尔赛尤』出发。\x01",
            "火速赶往雷那特川河口西南方。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS219._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS230._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS231._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS232._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4FF7 end

    def Function_17_53CC(): pass

    label("Function_17_53CC")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #162
        0xC,
        (
            "#170F#5P全体攻击艇\x01",
            "都已到达部属位置。\x02\x03",

            "麻醉弹的装填也已完成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xD,
        (
            "#163F#2P好，接下来\x01",
            "就等龙出现了。\x02\x03",

            "#160F全体攻击艇做好射击准备。\x01",
            "随命令一同开始攻击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xC,
        "#178F#5P是，长官！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1002F呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        "#042F#6P终于要开始了呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS233._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS234._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS235._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_53CC end

    def Function_18_56E9(): pass

    label("Function_18_56E9")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_57F7():
        OP_6B(3300, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #167
        0xD,
        "#162F#2P#5S射击！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_56E9 end

    def Function_19_5847(): pass

    label("Function_19_5847")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #168
        0xD,
        "#164F#2P嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1018F#6P成、成功了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        "#020F#6P……太漂亮了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xB,
        (
            "#071F#4P嗯，就算是\x01",
            "巨龙也无从抵抗啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "#031F哎呀……\x01",
            "真是华丽的场面啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #173
        0xC,
        (
            "#170F#5P──确认龙已坠入\x01",
            "瓦雷利亚湖！\x02\x03",

            "要按照预定计划，\x01",
            "用绳索捕捉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xD,
        (
            "#163F#2P嗯……\x02\x03",

            "#160F在确认安全的情况下，\x01",
            "『埃尔赛尤』也一起降落。\x02\x03",

            "降在湖面上后进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xC,
        "#171F#5P是，长官！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_23(0x7A)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5847 end

    def Function_20_5ADB(): pass

    label("Function_20_5ADB")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_23(0x7A)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x8, -2390, 2000, 91050, 0)
    SetChrPos(0xB, -1610, 2000, 89800, 0)
    SetChrPos(0x9, -180, 2000, 90890, 0)
    SetChrPos(0xA, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #176
        0xC,
        (
            "#176F#5P『埃尔赛尤』降落完毕。\x02\x03",

            "#178F龙还没有任何反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xD,
        (
            "#163F#2P好……\x01",
            "我们去亲眼看一下吧。\x02\x03",

            "#160F上尉，你也跟来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #178
        0xC,
        "#172F#5P是！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -1050, 2000, 94150, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    OP_0D()
    Sleep(200)

    def lambda_5CBC():
        OP_6D(-340, 2000, 90490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5CBC)

    def lambda_5CD4():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5CD4)

    def lambda_5CE4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_5CE4)
    Sleep(70)

    def lambda_5CF7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5CF7)
    Sleep(70)

    def lambda_5D0A():

        label("loc_5D0A")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5D0A")

    QueueWorkItem2(0x101, 2, lambda_5D0A)

    def lambda_5D1B():

        label("loc_5D1B")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_5D1B")

    QueueWorkItem2(0x9, 2, lambda_5D1B)
    Sleep(70)

    def lambda_5D31():

        label("loc_5D31")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5D31")

    QueueWorkItem2(0x8, 2, lambda_5D31)
    Sleep(80)

    def lambda_5D47():

        label("loc_5D47")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5D47")

    QueueWorkItem2(0xB, 2, lambda_5D47)
    Sleep(70)

    def lambda_5D5D():

        label("loc_5D5D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5D5D")

    QueueWorkItem2(0xA, 2, lambda_5D5D)

    def lambda_5D6E():
        OP_8F(0xFE, 0x294, 0x7D0, 0x15FEA, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D6E)
    OP_43(0xD, 0x0, 0x0, 0x16)
    OP_43(0xC, 0x0, 0x0, 0x15)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    def lambda_5DA1():

        label("loc_5DA1")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_5DA1")

    QueueWorkItem2(0x9, 2, lambda_5DA1)
    Sleep(2300)

    ChrTalk(    #179
        0x101,
        "#1004F#5P啊，等一等……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x0)
    TurnDirection(0xC, 0x101, 400)
    Sleep(500)

    ChrTalk(    #180
        0xC,
        (
            "#171F呵呵，你们也一起来吧。\x02\x03",

            "这是传说中的古代龙。\x01",
            "平常很难得有机会可以见到吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1008F#5P嗯、嗯。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    AddParty(0x4, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    AddParty(0x7, 0xFA, 0xFF)
    OP_6D(-890, 2000, 88540, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -890, 2000, 88540, 180)
    SetChrPos(0x105, -890, 2000, 88540, 180)
    SetChrPos(0x103, -890, 2000, 88540, 180)
    SetChrPos(0x104, -890, 2000, 88540, 180)
    SetChrPos(0x108, -890, 2000, 88540, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1A23)
    OP_28(0x95, 0x1, 0x20)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_20_5ADB end

    def Function_21_5F36(): pass

    label("Function_21_5F36")

    Sleep(800)
    OP_8E(0xFE, 0xFFFFFF1A, 0x7D0, 0x16E04, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFE5C, 0x7D0, 0x15D2E, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFD12, 0x7D0, 0x1564E, 0x7D0, 0x0)
    Return()

    # Function_21_5F36 end

    def Function_22_5F78(): pass

    label("Function_22_5F78")

    OP_8E(0xFE, 0xFFFFFE5C, 0x7D0, 0x15D2E, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFBB4, 0x7D0, 0x1480C, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFC36, 0x7D0, 0x1451E, 0x7D0, 0x0)

    def lambda_5FBA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5FBA)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_5F78 end

    def Function_23_5FD1(): pass

    label("Function_23_5FD1")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x50)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x103, -2390, 2000, 91050, 0)
    SetChrPos(0x108, -1610, 2000, 89800, 0)
    SetChrPos(0x104, -180, 2000, 90890, 0)
    SetChrPos(0x105, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrName("操舵士勒克司")

    ChrTalk(    #182
        0xE,
        (
            "#5P不行！\x01",
            "诱导弹无法锁定目标！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xE,
        "#5P明明已经探测到热源了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xC,
        (
            "#176F#2P也就是说有\x01",
            "某种干扰波吗……\x02\x03",

            "#177F那就切换到主炮！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrName("测量师艾柯")

    ChrTalk(    #185
        0xF,
        "#2P龙的速度持续上升中……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xF,
        (
            "#2P时速２３００塞尔矩──\x01",
            "２４００、２５００、２６００……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xD,
        (
            "#162F#2P可恶，这是什么怪物啊。\x02\x03",

            "竟能轻松超越\x01",
            "警备艇的最高速度……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(300)

    ChrTalk(    #188
        0xC,
        (
            "#172F#5P不过，用搭载了新型引擎的\x01",
            "『埃尔赛尤』就有可能进行追击！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #189
        0xC,
        (
            "#176F#2P──通告全体船员！\x02\x03",

            "#177F接下来『埃尔赛尤』将加速至\x01",
            "最大战速３２００塞尔矩！\x02\x03",

            "全体进行抗重力准备！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1020F咦咦？这是怎么回事！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 600)

    ChrTalk(    #191
        0x105,
        (
            "#046F#5P会有紧急加速的重力袭来！\x02\x03",

            "请蹲下\x01",
            "将姿势摆低！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1002F！　明白了！\x02",
    )

    CloseMessageWindow()
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x70025, 0x7002D, 0x1E)
    OP_D2(0x70035, 0x7003D, 0x1F)
    OP_D2(0x70045, 0x7004D, 0x20)
    OP_D2(0x70075, 0x7007D, 0x21)
    OP_8C(0x105, 0, 600)
    Fade(500)
    SetChrChipByIndex(0x105, 32)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x101, 29)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 30)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x104, 31)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x108, 33)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0xD, 6)
    SetChrSubChip(0xD, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #193
        0xC,
        (
            "#177F#2P──开始加速！\x01",
            "绝对不能让龙逃跑！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xE,
        "#5P是，长官！\x02",
    )

    CloseMessageWindow()
    OP_22(0x129, 0x1, 0x46)
    Sleep(200)
    OP_24(0x129, 0x50)
    Sleep(200)
    OP_24(0x129, 0x5A)
    Sleep(200)
    OP_24(0x129, 0x64)
    Sleep(500)

    def lambda_647F():

        label("loc_647F")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_647F")

    QueueWorkItem2(0x101, 3, lambda_647F)
    Fade(500)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    Sleep(1000)

    ChrTalk(    #195
        0x101,
        "#1021F哇哇哇……\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)

    def lambda_64D7():
        OP_6D(-2040, 2000, 69140, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_64D7)

    def lambda_64EF():
        OP_67(0, 7960, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64EF)
    Sleep(1000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_5FD1 end

    def Function_24_6523(): pass

    label("Function_24_6523")

    EventBegin(0x0)
    OP_6D(720, 2000, 95220, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 2000, 91550, 0)
    SetChrPos(0x103, -2390, 2000, 91050, 0)
    SetChrPos(0x108, -1610, 2000, 89800, 0)
    SetChrPos(0x104, -180, 2000, 90890, 0)
    SetChrPos(0x105, -2160, 2020, 92450, 0)
    SetChrPos(0xC, -1090, 2200, 93560, 0)
    SetChrPos(0xD, -210, 2000, 92630, 0)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x70025, 0x7002D, 0x1E)
    OP_D2(0x70035, 0x7003D, 0x1F)
    OP_D2(0x70045, 0x7004D, 0x20)
    OP_D2(0x70075, 0x7007D, 0x21)
    SetChrChipByIndex(0x101, 29)
    SetChrChipByIndex(0x103, 30)
    SetChrChipByIndex(0x104, 31)
    SetChrChipByIndex(0x108, 33)
    SetChrChipByIndex(0xD, 6)
    SetChrChipByIndex(0x105, 32)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x104, 0)
    SetChrSubChip(0x108, 0)
    SetChrSubChip(0xD, 0)
    OP_22(0x7A, 0x1, 0x50)
    OP_22(0x129, 0x1, 0x64)

    def lambda_6673():

        label("loc_6673")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6673")

    QueueWorkItem2(0x101, 3, lambda_6673)
    OP_71(0x3, 0x4)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xD, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #196
        0xF,
        "#2P……龙的高度下降了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        "#2P再这样下去将会跟丢目标。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xC,
        (
            "#177F#2P要紧跟到最后一刻！\x02\x03",

            "#175F……可恶。\x01",
            "云层还没冲破吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x103,
        (
            "#024F#6P等等！\x01",
            "这是什么地区！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(400)

    ChrTalk(    #200
        0xC,
        "#173F#2P！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240120, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(160, 220, -1, -1)
    SetChrName("尤莉亚上尉")

    AnonymousTalk(    #201
        "\x07\x00#172F是迷雾峡谷吗……！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 250, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #202
        (
            "\x07\x00#1020F莫非我们\x01",
            "已经进入了雾中！？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #203
        "\x07\x00#162F唔……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #204
        0xF,
        "#2P龙的高度下降至１２００亚矩。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xF,
        "#2P１１００、１０００、９００……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xF,
        (
            "#2P……………………\x01",
            "……目标丢失。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(400)

    ChrTalk(    #207
        0xC,
        "#175F#5P可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x105,
        "#043F#6P尤莉亚上尉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#1015F跟、跟丢了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xC,
        (
            "#176F#5P……嗯。\x02\x03",

            "#175F在迷雾峡谷的西北部……\x01",
            "被它逃到雾气浓密的险处去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xD,
        (
            "#160F#2P……埃尔赛尤号要停到\x01",
            "那个空贼巢穴去吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 2)

    ChrTalk(    #212
        0xC,
        (
            "#175F#5P不……按照埃尔赛尤号的\x01",
            "大小是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xD,
        (
            "#163F#2P是吗……\x02\x03",

            "#160F──作战结束。\x02\x03",

            "让后续的巡逻艇\x01",
            "监视峡谷周围。\x02\x03",

            "#163F让『埃尔赛尤』\x01",
            "暂时返回柏斯。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x7A)
    OP_23(0x129)
    Sleep(1000)
    OP_A2(0x1A24)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_6523 end

    def Function_25_6A90(): pass

    label("Function_25_6A90")

    EventBegin(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x8, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_6D(490, 2000, 88600, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xC, -250, 2000, 92100, 270)
    SetChrPos(0x11, -1630, 2000, 92100, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_6B54():

        label("loc_6B54")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6B54")

    QueueWorkItem2(0xC, 1, lambda_6B54)
    Sleep(100)

    def lambda_6B6A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B6A)
    Sleep(400)

    def lambda_6B7D():
        OP_6D(190, 2000, 92150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6B7D)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(300)
    OP_43(0x102, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x1C)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x1D)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x12, 0x1, 0x0, 0x1F)
    Sleep(300)
    OP_43(0x14, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0x21)
    WaitChrThread(0x101, 0x1)
    OP_44(0xC, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #214
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x13,
        "#064F爷、爷爷！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x11,
        (
            "#101F#5P好久不见了，\x02\x03",

            "#100F提妲。\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x13,
        "#067F嘿嘿……嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x12,
        (
            "#051F喂喂，老爷子。\x01",
            "你怎么在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x11,
        (
            "#104F#5P说来话长，几天前\x01",
            "我就乘上埃尔赛尤号了。\x02\x03",

            "#100F话说回来……\x01",
            "艾丝蒂尔，约修亚，\x02\x03",

            "你们都能平安\x01",
            "返回真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#1016F哈哈……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        (
            "#1035F……很抱歉，\x01",
            "让您担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x11,
        (
            "#101F#5P哪里，只要能回来\x01",
            "就万事大吉了。\x02\x03",

            "#102F不过想不到『四轮之塔』\x01",
            "居然发生了异变呢……\x02\x03",

            "现在我也得集中精神\x01",
            "进行调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1006F嗯，拜托了。\x02\x03",

            "#1015F不过……\x01",
            "应该先去哪座塔好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#1043F是啊……\x01",
            "如果考虑距离的话\x01",
            "还是『琥珀』和『红莲』比较近……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xC,
        (
            "#176F不过以『埃尔赛尤』的速度，\x01",
            "去哪座塔都差不多。\x02\x03",

            "#178F或许应该先去已经掌握了\x01",
            "敌人情报的地方会比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        "#1004F敌人的情报？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xC,
        (
            "#178F刚才前往『翡翠之塔』的\x01",
            "侦察部队传来了后续报告。\x02\x03",

            "据说是出现了一个\x01",
            "戴着面具、身穿白衣的可疑男人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #228
        0x101,
        "#1005F是那个怪盗男！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xA,
        (
            "#043F虽说只是侦察部队，\x01",
            "不过竟能以一己之力击破……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7052")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第１章选择了阿加特】\x01",        # 0
            "【◇第１章选择了雪拉扎德】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7046"),
        (1, "loc_704C"),
        (SWITCH_DEFAULT, "loc_7052"),
    )


    label("loc_7046")

    OP_A2(0x1201)
    Jump("loc_7052")

    label("loc_704C")

    OP_A3(0x1200)
    Jump("loc_7052")

    label("loc_7052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7086")

    ChrTalk(    #230
        0x12,
        (
            "#057F嘿，看来不只是个\x01",
            "古怪的家伙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70AF")

    label("loc_7086")


    ChrTalk(    #231
        0x8,
        "#022F看来他的实力在我们的想象之上。\x02",
    )

    CloseMessageWindow()

    label("loc_70AF")


    ChrTalk(    #232
        0x102,
        (
            "#1035F『怪盗绅士』布卢布兰……\x02\x03",

            "#1042F以分身和影缝为主要攻击手段，\x01",
            "使用各种魔术般技巧的执行者。\x02\x03",

            "一般的战法在他面前大概行不通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1007F是吗……\x02\x03",

            "#1015F不过，至少了解了敌人的真身，\x01",
            "总比去其他的塔更有把握……\x02\x03",

            "#1006F嗯！\x01",
            "先去『翡翠之塔』吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xC,
        "#170F明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_71C1():
        OP_6D(310, 2000, 95070, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_71C1)

    def lambda_71D9():
        OP_67(0, 4710, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71D9)

    def lambda_71F1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_71F1)
    Sleep(800)
    OP_8C(0x11, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #235
        0xC,
        (
            "#172F#2P准备出发！\x02\x03",

            "本舰现在前往\x01",
            "洛连特地区的『翡翠之塔』！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E00)
    OP_BB(0x1, 0x0, 0x200033)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_6A90 end

    def Function_26_726D(): pass

    label("Function_26_726D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7294():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7294)
    OP_8F(0xFE, 0xFFFFFE70, 0x7E4, 0x161E8, 0xBB8, 0x0)
    Return()

    # Function_26_726D end

    def Function_27_72B5(): pass

    label("Function_27_72B5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_72DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72DC)
    OP_8F(0xFE, 0xFFFFFA74, 0x7E4, 0x161E8, 0xBB8, 0x0)
    Return()

    # Function_27_72B5 end

    def Function_28_72FD(): pass

    label("Function_28_72FD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7324():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7324)
    OP_8F(0xFE, 0xFFFFF5A6, 0x7D0, 0x15E64, 0xBB8, 0x0)
    Return()

    # Function_28_72FD end

    def Function_29_7345(): pass

    label("Function_29_7345")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_736C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_736C)
    OP_8F(0xFE, 0x64, 0x7D0, 0x15EC8, 0xBB8, 0x0)
    Return()

    # Function_29_7345 end

    def Function_30_738D(): pass

    label("Function_30_738D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_73B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73B4)
    OP_8F(0xFE, 0xFFFFF9C0, 0x7D0, 0x15C70, 0xBB8, 0x0)
    Return()

    # Function_30_738D end

    def Function_31_73D5(): pass

    label("Function_31_73D5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_73FC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73FC)
    OP_8F(0xFE, 0xFFFFF650, 0x7D0, 0x157C0, 0xBB8, 0x0)
    Return()

    # Function_31_73D5 end

    def Function_32_741D(): pass

    label("Function_32_741D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7444():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7444)
    OP_8F(0xFE, 0xFFFFFBA0, 0x7D0, 0x158EC, 0xBB8, 0x0)
    Return()

    # Function_32_741D end

    def Function_33_7465(): pass

    label("Function_33_7465")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -1170, 2000, 83500, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_748C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_748C)
    OP_8F(0xFE, 0xFFFFFDB2, 0x7D0, 0x15694, 0xBB8, 0x0)
    Return()

    # Function_33_7465 end

    def Function_34_74AD(): pass

    label("Function_34_74AD")

    EventBegin(0x0)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2400, 2000, 91710, 0)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #236
        0xC,
        "#176F#2P已到达『翡翠之塔』上空。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#1004F啊～真的好快呢。\x02\x03",

            "不到30分钟\x01",
            "就抵达了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x13,
        (
            "#061F#6P嘿嘿，差不多。\x02\x03",

            "#560F应该用了定期船\x01",
            "将近三倍的速度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1006F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        (
            "#1042F#6P『翡翠之塔』的塔顶\x01",
            "情况怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xC,
        "#178F#2P马上会显示在屏幕上。\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)

    def lambda_7774():
        OP_67(0, 5150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7774)
    OP_72(0x13, 0x4)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x3C)
    SetChrSubChip(0xC, 2)
    Sleep(100)

    def lambda_77A9():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_77A9)

    def lambda_77B7():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77B7)
    Sleep(50)
    OP_22(0x127, 0x0, 0x64)

    def lambda_77CF():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77CF)

    def lambda_77DD():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77DD)
    Sleep(50)

    def lambda_77F0():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_77F0)
    OP_73(0x13)
    WaitChrThread(0x101, 0x0)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x13, 0x6, 0x2)
    OP_74(0x13, 0x8, 0x2)
    OP_74(0x13, 0xA, 0x2)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0706   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_34_74AD end

    def Function_35_7848(): pass

    label("Function_35_7848")

    EventBegin(0x0)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x13, 0x4)
    OP_6F(0x13, 60)
    OP_74(0x13, 0x6, 0x2)
    OP_74(0x13, 0x8, 0x2)
    OP_74(0x13, 0xA, 0x2)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2400, 2000, 91710, 0)
    OP_4A(0xA, 255)

    def lambda_7979():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7979)

    def lambda_7987():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7987)

    def lambda_7995():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7995)

    def lambda_79A3():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_79A3)

    def lambda_79B1():
        OP_8C(0xFE, 45, 0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_79B1)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(    #242
        0x102,
        (
            "#1042F#6P尤莉亚小姐。\x02\x03",

            "我们应该怎样\x01",
            "下降到地面呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xC,
        (
            "#176F#5P很不巧，没有能让\x01",
            "『埃尔赛尤』着陆的地方。\x02\x03",

            "#178F我们会在滞空状态放下升降机，\x01",
            "请你们乘上去下降到地面。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #244
        0x101,
        "#1004F升降机？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xA,
        (
            "#040F#4P就是投放榴弹炮时\x01",
            "使用的货用升降机。\x02\x03",

            "被设置在货舱里面。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, -180, 400)

    ChrTalk(    #246
        0x101,
        "#1006F#5P这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(500)

    ChrTalk(    #247
        0x102,
        (
            "#1040F#6P那么，请选择调查塔\x01",
            "内部的成员人选吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x13, 0x4)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C3C")
    Call(0, 48)

    label("loc_7C3C")

    SetChrName("")

    AnonymousTalk(    #248
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(200)
    Sleep(1000)
    OP_A2(0x10F9)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0310   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_35_7848 end

    def Function_36_7CE0(): pass

    label("Function_36_7CE0")

    EventBegin(0x0)
    OP_6D(-740, 2000, 46900, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, -430, 2000, 47400, 180)
    SetChrPos(0x102, -1430, 2000, 47400, 180)
    SetChrPos(0xF8, -1430, 2000, 48400, 180)
    SetChrPos(0xF9, -430, 2000, 48400, 180)
    SetChrPos(0x11, -920, 2000, 45630, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0x11,
        (
            "#100F我会暂时待在\x01",
            "下面的工房里。\x02\x03",

            "在调查塔时，如果需要整备导力器\x01",
            "或合成回路的话就来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        "#1006F#5P嗯，我们会的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F46")

    ChrTalk(    #251
        0x11,
        (
            "#102F提妲……\x01",
            "你一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x107,
        (
            "#560F#5P嗯……不用担心。\x02\x03",

            "#061F我也\x01",
            "和姐姐他们一起\x01",
            "旅行过很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x11,
        "#100F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1006F#5P博士，请别担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x106,
        "#051F#5P没事，交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x11,
        (
            "#104F嗯，拜托了。\x02\x03",

            "#102F……敌人的目的\x01",
            "尚不清楚。\x02\x03",

            "你们小心上路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8090")

    label("loc_7F46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_805A")

    ChrTalk(    #257
        0x11,
        (
            "#102F提妲……\x01",
            "你一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x107,
        (
            "#560F#5P嗯……不用担心。\x02\x03",

            "#061F我也\x01",
            "和姐姐他们一起\x01",
            "旅行过很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x11,
        "#100F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1006F#5P博士，请别担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x102,
        "#1040F#5P请交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x11,
        (
            "#104F嗯，拜托了。\x02\x03",

            "#102F……敌人的目的\x01",
            "尚不清楚。\x02\x03",

            "你们小心上路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8090")

    label("loc_805A")


    ChrTalk(    #263
        0x11,
        (
            "#102F……敌人的目的\x01",
            "尚不清楚。\x02\x03",

            "你们小心上路吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8090")

    OP_8C(0x11, 90, 400)

    def lambda_809D():

        label("loc_809D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_809D")

    QueueWorkItem2(0x101, 1, lambda_809D)

    def lambda_80AE():

        label("loc_80AE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_80AE")

    QueueWorkItem2(0x102, 1, lambda_80AE)

    def lambda_80BF():

        label("loc_80BF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_80BF")

    QueueWorkItem2(0xF8, 1, lambda_80BF)

    def lambda_80D0():

        label("loc_80D0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_80D0")

    QueueWorkItem2(0xF9, 1, lambda_80D0)
    SetChrFlags(0x11, 0x4)
    OP_8E(0x11, 0x686, 0x802, 0xB252, 0x7D0, 0x0)
    ClearChrFlags(0x11, 0x4)
    OP_8E(0x11, 0x820, 0x0, 0xC170, 0x7D0, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_812D():
        OP_6D(-710, 2000, 47510, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_812D)
    TurnDirection(0x101, 0x102, 400)

    def lambda_814C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_814C)

    def lambda_815A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_815A)
    Sleep(50)

    def lambda_816D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_816D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #264
        0x101,
        (
            "#1006F#2P那么，准备完成之后\x01",
            "就必须马上下降到地面才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x102,
        (
            "#1040F#6P嗯。\x01",
            "是货舱的升降机吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1210, 2000, 46360, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1210, 2000, 46360, 180)
    SetChrPos(0x102, -1210, 2000, 46360, 180)
    SetChrPos(0xF8, -1210, 2000, 46360, 180)
    SetChrPos(0xF9, -1210, 2000, 46360, 180)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_82FB")
    SetChrPos(0x12, 770, 2000, 89910, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 28)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_82FB")

    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_A2(0x1E01)
    OP_28(0x99, 0x1, 0x800)
    OP_28(0x9A, 0x4, 0x2)
    OP_28(0x9A, 0x4, 0x8)
    OP_28(0x9A, 0x1, 0x1)
    OP_28(0x9A, 0x1, 0x2)
    OP_28(0x9A, 0x1, 0x4)
    OP_28(0x9A, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_36_7CE0 end

    def Function_37_8357(): pass

    label("Function_37_8357")

    EventBegin(0x0)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    ClearChrFlags(0x101, 0x80)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #266
        0xC,
        (
            "#178F#5P已到达『红莲之塔』上空。\x02\x03",

            "塔顶部分果然\x01",
            "被漆黑的结界所覆盖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1002F#4P那么\x01",
            "就像『翡翠之塔』一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x102,
        (
            "#1035F#6P内部很有可能已经\x01",
            "变成另一个空间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_85DF():
        OP_6D(-130, 2000, 90500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_85DF)

    def lambda_85F7():
        OP_67(0, 5000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_85F7)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -1040, 2000, 83000, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_8630():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8630)

    def lambda_8642():
        OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14FF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8642)

    def lambda_865D():

        label("loc_865D")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_865D")

    QueueWorkItem2(0x101, 1, lambda_865D)
    Sleep(50)

    def lambda_8673():

        label("loc_8673")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_8673")

    QueueWorkItem2(0x102, 1, lambda_8673)
    Sleep(50)

    def lambda_8689():

        label("loc_8689")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_8689")

    QueueWorkItem2(0x13, 1, lambda_8689)
    Sleep(50)

    def lambda_869F():

        label("loc_869F")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_869F")

    QueueWorkItem2(0xA, 1, lambda_869F)
    Sleep(50)

    def lambda_86B5():

        label("loc_86B5")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_86B5")

    QueueWorkItem2(0x12, 1, lambda_86B5)
    Sleep(50)

    def lambda_86CB():

        label("loc_86CB")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_86CB")

    QueueWorkItem2(0x8, 1, lambda_86CB)
    Sleep(100)

    def lambda_86E1():

        label("loc_86E1")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_86E1")

    QueueWorkItem2(0x14, 1, lambda_86E1)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #269
        0xB,
        "#070F#4P哟，让你们久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1004F#5P啊，金先生。\x02\x03",

            "#1015F和雾香小姐的联络中\x01",
            "都说了什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xB,
        (
            "#074F#4P嗯，她是在询问\x01",
            "我们这边的情况如何了。\x02\x03",

            "#070F我把在『翡翠之塔』发生的事\x01",
            "大致跟她说了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        "#1006F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x102,
        "#1040F#5P辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xB,
        (
            "#070F#4P好，那我们赶快\x01",
            "进入『塔』里吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8875")
    Call(0, 48)

    label("loc_8875")

    SetChrName("")

    AnonymousTalk(    #275
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择固定队员外的一名同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(200)
    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, -1320, 2000, 87840, 180)
    SetChrPos(0x1, -1320, 2000, 87840, 180)
    SetChrPos(0x2, -1320, 2000, 87840, 180)
    SetChrPos(0x3, -1320, 2000, 87840, 180)
    OP_69(0x0, 0x0)
    SetChrSubChip(0xC, 0)
    SetChrChipByIndex(0xC, 4)
    SetChrPos(0xC, -1090, 2000, 94920, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 1330, 0, 98300, 225)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    OP_D2(0x600FE, 0x60103, 0x1D)
    OP_D2(0x600FC, 0x60101, 0x1E)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x10)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0xF, -1740, 0, 97950, 0)
    SetChrChipByIndex(0xF, 11)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0x10, 530, 0, 98030, 90)
    SetChrChipByIndex(0x10, 12)
    ClearChrFlags(0x10, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AE7")
    OP_44(0xA, 0xFF)
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_8C(0xA, 0, 0)

    label("loc_8AE7")

    Sleep(500)
    OP_A2(0x1E0A)
    OP_28(0x9A, 0x1, 0x10)
    OP_28(0x9A, 0x1, 0x20)
    OP_28(0x9A, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_37_8357 end

    def Function_38_8B17(): pass

    label("Function_38_8B17")

    EventBegin(0x0)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    ClearChrFlags(0x101, 0x80)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)

    def lambda_8B45():

        label("loc_8B45")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_8B45")

    QueueWorkItem2(0x101, 3, lambda_8B45)
    OP_6D(-20, 2000, 95340, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_71(0x14, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #276
        0x101,
        (
            "#1025F#5P卢安地区吗……\x02\x03",

            "特蕾莎院长和那些孩子们\x01",
            "现在不知道怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xA,
        (
            "#043F#4P我想应该已经在军队的\x01",
            "保护下去避难了。\x02\x03",

            "#049F希望她们能平安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        (
            "#1040F#5P没事的，别担心。\x02\x03",

            "在父亲的命令下，军队和\x01",
            "协会正在进行联合镇压。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xA,
        "#542F#4P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1006F#5P的确，老爸\x01",
            "是不会在此事上有任何疏忽的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x12,
        "#051F#6P嗯……那是自然。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #282
        0xC,
        (
            "#178F#5P──各位游击士，\x02\x03",

            "还有5分钟\x01",
            "就将到达『绀碧之塔』上空。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_8FAA():
        OP_6D(370, 2000, 93430, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FAA)

    def lambda_8FC2():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FC2)

    def lambda_8FDA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8FDA)
    Sleep(50)

    def lambda_8FED():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FED)

    def lambda_8FFB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8FFB)
    Sleep(50)

    def lambda_900E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_900E)

    def lambda_901C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_901C)
    Sleep(50)

    def lambda_902F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_902F)

    def lambda_903D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_903D)
    Sleep(400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #283
        0x101,
        "#1026F#5P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x8,
        (
            "#026F#6P嗯……\x02\x03",

            "#020F到达后就要出发了哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90F0")
    Call(0, 48)

    label("loc_90F0")

    SetChrName("")

    AnonymousTalk(    #285
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择固定队员外的一名同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x1E11)
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_8B17 end

    def Function_39_9193(): pass

    label("Function_39_9193")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91AA")
    Call(0, 48)
    Call(0, 49)

    label("loc_91AA")

    OP_6D(-1320, 2000, 87840, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1320, 2000, 87840, 180)
    SetChrPos(0x1, -1320, 2000, 87840, 180)
    SetChrPos(0x2, -1320, 2000, 87840, 180)
    SetChrPos(0x3, -1320, 2000, 87840, 180)
    SetChrPos(0xC, -1900, 2000, 93320, 0)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrPos(0x18, -2920, 2000, 49050, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9286")
    SetChrPos(0xA, 80, 2000, 91070, 0)
    ClearChrFlags(0xA, 0x80)

    label("loc_9286")

    OP_28(0x9A, 0x1, 0x80)
    OP_28(0x9A, 0x1, 0x100)
    OP_28(0x9A, 0x1, 0x200)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_39_9193 end

    def Function_40_92AE(): pass

    label("Function_40_92AE")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(460, 2000, 94360, 0)
    OP_67(0, 4750, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -310, 2000, 91660, 0)
    SetChrPos(0x102, -1460, 2000, 91520, 0)
    SetChrPos(0x13, -2630, 2000, 90470, 0)
    SetChrPos(0xA, 220, 2020, 90650, 0)
    SetChrPos(0x12, -2550, 2000, 89380, 0)
    SetChrPos(0x8, -1000, 2020, 90140, 0)
    SetChrPos(0xB, -80, 2000, 89260, 0)
    SetChrPos(0x14, -1380, 2000, 88780, 0)
    SetChrPos(0xE, -1040, 200, 99240, 0)
    SetChrPos(0xF, -3530, 200, 99080, 315)
    SetChrPos(0x10, 1380, 200, 99090, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #286
        0xC,
        (
            "#178F#5P已到达『琥珀之塔』上空。\x02\x03",

            "来自侦察部队的后续报告也\x01",
            "终于传过来了。\x02\x03",

            "#176F……从塔中现身的袭击者\x01",
            "是一名手持巨大镰刀的少女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        (
            "#1003F#4P是吗……\x01",
            "我也已经猜到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x13,
        "#063F#6P……小玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x102,
        (
            "#1035F#6P『歼灭天使』玲……\x02\x03",

            "当初我在结社的时候，\x01",
            "她还是候补『执行者』……\x02\x03",

            "#1043F想不到她竟已能操纵\x01",
            "那架『帕蒂尔·玛蒂尔』了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #290
        0x101,
        (
            "#1004F#2P约修亚……\x01",
            "你知道那架巨大机器人吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #291
        0x102,
        (
            "#1042F#6P那是结社的实验室开发的\x01",
            "战略级巨大人形兵器。\x02\x03",

            "因为操控困难，所以开发计划\x01",
            "应该已被冻结了才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x14,
        (
            "#1063F#4P那个女孩子\x01",
            "可以轻松地操控吗……\x02\x03",

            "#1068F真是个可怕的小家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x13,
        "#561F#6P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)
    Sleep(300)

    ChrTalk(    #294
        0x101,
        (
            "#1006F#5P没事的，提妲。\x01",
            "别摆出这样的表情嘛。\x02\x03",

            "我一定会让那孩子\x01",
            "醒过来的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    Sleep(300)

    ChrTalk(    #295
        0x13,
        "#560F#6P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        "#1043F#6P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #297
        0x101,
        (
            "#1015F#2P那个……\x01",
            "我是不是有点太乐观了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x102,
        (
            "#1035F#6P……不。\x02\x03",

            "#1040F说不定你……\x01",
            "真的能进入那孩子的心。\x02\x03",

            "让我们一起呼唤她吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1016F#2P……嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98BF")
    Call(0, 48)

    label("loc_98BF")

    SetChrName("")

    AnonymousTalk(    #300
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(-1160, 2000, 46570, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1160, 2000, 46570, 180)
    SetChrPos(0x1, -1160, 2000, 46570, 180)
    SetChrPos(0x2, -1160, 2000, 46570, 180)
    SetChrPos(0x3, -1160, 2000, 46570, 180)
    OP_28(0x9A, 0x1, 0x400)
    OP_28(0x9A, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x2)
    SetMapFlags(0x1)
    SetMapFlags(0x2000000)
    Return()

    # Function_40_92AE end

    def Function_41_99F1(): pass

    label("Function_41_99F1")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x101, -290, 2000, 90360, 0)
    SetChrPos(0x102, -1500, 2000, 90260, 0)
    SetChrPos(0x13, -1660, 2000, 88720, 0)
    SetChrPos(0x14, 500, 2000, 89150, 0)
    SetChrPos(0x12, -1880, 2000, 87500, 0)
    SetChrPos(0x8, -2540, 2000, 88900, 0)
    SetChrPos(0xB, -140, 2000, 87500, 0)
    SetChrPos(0xA, -490, 2000, 88880, 0)
    TurnDirection(0x101, 0xC, 0)
    TurnDirection(0x102, 0xC, 0)
    TurnDirection(0x13, 0xC, 0)
    TurnDirection(0xA, 0xC, 0)
    TurnDirection(0x12, 0xC, 0)
    TurnDirection(0x8, 0xC, 0)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0x14, 0xC, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 15)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrChipByIndex(0xC, 4)
    SetChrPos(0xC, -1130, 2000, 92290, 180)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)
    OP_6D(-10, 2000, 92570, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x7A, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #301
        0xC,
        (
            "#176F#5P出现在各地的机器人和\x01",
            "装甲兽已经基本上被消灭了。\x02\x03",

            "#171F警戒体制虽然还在持续，\x01",
            "不过应该也快要解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xA,
        "#542F#4P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x12,
        (
            "#051F#6P虽然还有诸多不明之处，\x01",
            "不过『塔』的异变也已得到平息……\x02\x03",

            "感觉可以松口气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x8,
        (
            "#524F#6P说得也是……\x01",
            "如果是这样就太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xB,
        (
            "#074F#4P可是……\x01",
            "怎么也看不出敌人的意图。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        "#1003F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x14,
        (
            "#1063F#4P艾丝蒂尔，\x01",
            "你好像很没精神呢。\x02\x03",

            "是因为那小家伙的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1007F#6P……嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_9DA5():
        OP_6D(-10, 2000, 91570, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DA5)
    OP_8C(0x101, 180, 400)

    def lambda_9DC4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DC4)

    def lambda_9DD2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DD2)
    Sleep(50)

    def lambda_9DE5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9DE5)

    def lambda_9DF3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9DF3)
    Sleep(50)

    def lambda_9E06():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9E06)

    def lambda_9E14():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9E14)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #309
        0x101,
        (
            "#1025F#5P我明明不知道她受过的苦，\x01",
            "还自以为是地对她大加指责，\x02\x03",

            "会不会已经伤害到她了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x13,
        "#063F#6P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xA,
        "#043F#4P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1003F#5P像我这种人，既没有人生阅历，\x01",
            "又总是被大家保护着……\x02\x03",

            "怎么可能有资格去\x01",
            "拯救那孩子呢……\x02\x03",

            "#1007F我真是太异想天开了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x102,
        "#1040F#6P……你说得不对哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #315
        0x102,
        (
            "#1035F#6P玲她……\x01",
            "其实是个真正的天才。\x02\x03",

            "瞬间吸收所有信息\x01",
            "并将其转换为自己的力量……\x02\x03",

            "迅速适应任何环境，\x01",
            "并逐渐控制自己和周遭环境……\x02\x03",

            "#1042F她似乎天生\x01",
            "就具备了这种才能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        "#1026F#2P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x102,
        (
            "#1043F#6P在被『结社』收留之前，\x01",
            "那孩子所处的环境\x01",
            "非常残酷……\x02\x03",

            "但是，和我不同，\x01",
            "那孩子的心并没有坏掉。\x02\x03",

            "#1035F因为她可以承受任何逆境，\x01",
            "并强迫自己去接受、适应......\x02\x03",

            "所以才能够在这样的遭遇下保持自我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x101,
        "#1020F#2P不、不过这样的话……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x102,
        (
            "#1043F#6P嗯……是啊。\x02\x03",

            "无论再怎么控制感情，\x01",
            "我想心也不可能不会痛的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        "#1026F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x102,
        (
            "#1035F#6P在我的印象中，\x01",
            "从来没有见过玲\x01",
            "像这次这样激动。\x02\x03",

            "我想大概是你的话\x01",
            "触碰到了连玲自己\x01",
            "也没有察觉的真实情感。\x02\x03",

            "#1040F……这是只有你才能做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x101,
        (
            "#1025F#2P约修亚……\x02\x03",

            "#1007F……既然这样的话，\x01",
            "我也不能一直垂头丧气的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #323
        0x101,
        (
            "#1022F#6P你看着吧～玲！\x02\x03",

            "#1005F下次见面，我一定要\x01",
            "彻底面对真实的你！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #324
        0x13,
        "#067F#6P姐、姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x8,
        "#027F#6P呵呵，真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x14,
        (
            "#1061F#4P哈哈。\x01",
            "这才是艾丝蒂尔啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(300)

    ChrTalk(    #327
        0x101,
        (
            "#1016F#5P嗯，先不说这个……\x02\x03",

            "#1015F总之，我们接下来该怎么办？\x02\x03",

            "既然不明白『结社』的意图，\x01",
            "回王都也不太合适……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xC,
        (
            "#170F#5P这样的话，今天\x01",
            "先去一下雷斯顿要塞怎样？\x02\x03",

            "这样一来也可以和\x01",
            "卡西乌斯准将讨论今后的方向。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A435():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A435)

    def lambda_A443():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A443)
    Sleep(50)

    def lambda_A456():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A456)

    def lambda_A464():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A464)
    Sleep(50)

    def lambda_A477():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A477)

    def lambda_A485():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A485)
    Sleep(50)

    def lambda_A498():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A498)

    def lambda_A4A6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A4A6)
    Sleep(200)

    ChrTalk(    #329
        0x101,
        "#1004F#4P啊，也对……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x102,
        "#1040F#6P这样的确比较好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "#040F#4P那么，尤莉亚小姐，\x01",
            "请带我们前往雷斯顿要塞吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xC,
        "#171F#5P明白──\x02",
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1040, 2000, 83000, 0)

    NpcTalk(    #333
        0x11,
        "老人的声音",
        "#1P不、不好了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A674():
        OP_6D(-130, 2000, 90500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A674)

    def lambda_A68C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A68C)

    def lambda_A69E():
        OP_8E(0xFE, 0xFFFFFB50, 0x7D0, 0x14FF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_A69E)

    def lambda_A6B9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6B9)

    def lambda_A6C7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6C7)
    Sleep(50)

    def lambda_A6DA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A6DA)

    def lambda_A6E8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A6E8)
    Sleep(50)

    def lambda_A6FB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A6FB)

    def lambda_A709():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A709)
    Sleep(50)

    def lambda_A71C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A71C)

    def lambda_A72A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A72A)
    Sleep(50)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x11, 0x3)

    ChrTalk(    #334
        0x13,
        "#064F#5P爷、爷爷？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1015F#5P怎、怎么了？\x01",
            "这么惊慌的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x11,
        (
            "#105F#4P这是你们在塔上找到的\x01",
            "数据水晶……\x02\x03",

            "刚才『卡佩尔』\x01",
            "分析了其中的一个！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#1004F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x102,
        "#1042F#5P上面记载着什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x11,
        (
            "#105F#4P『设备塔』的功能！\x02\x03",

            "四座塔是为了将『辉之环』\x01",
            "维系于异次元\x01",
            "而建造出来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        "#1020F#5P异、异次元……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        "#1044F#5P『辉之环』在那种地方！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x14,
        (
            "#1064F#5P等、等一等！\x02\x03",

            "那么莫非\x01",
            "那些『里塔』的空间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x11,
        (
            "#104F#4P嗯，应该也是\x01",
            "属于异次元的空间吧。\x02\x03",

            "#102F而『福音』的真面目是……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("男人的声音")

    AnonymousTalk(    #344
        (
            "\x07\x05──没错。\x01",
            "是『辉之环』的『终端』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5A)
    Sleep(500)

    def lambda_AA89():
        OP_6D(1970, 2000, 92640, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA89)

    def lambda_AAA1():
        OP_67(0, 5150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AAA1)

    def lambda_AAB9():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AAB9)

    def lambda_AAC7():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAC7)
    Sleep(50)

    def lambda_AADA():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AADA)

    def lambda_AAE8():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_AAE8)
    Sleep(50)

    def lambda_AAFB():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAFB)

    def lambda_AB09():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AB09)
    Sleep(50)

    def lambda_AB1C():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AB1C)

    def lambda_AB2A():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AB2A)
    Sleep(50)

    def lambda_AB3D():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AB3D)
    OP_72(0xC, 0x4)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    Sleep(150)
    OP_22(0x127, 0x0, 0x64)
    OP_73(0xC)
    WaitChrThread(0x101, 0x2)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x3)
    OP_74(0xC, 0x8, 0x3)
    OP_74(0xC, 0xA, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(    #345
        0x102,
        "#1042F#6P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x101,
        "#1020F#6P教、教授！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x12,
        "#052F#6P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xA,
        "#044F#4P这、这个人就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x14,
        "#1063F#4P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xC,
        (
            "#173F#6P为、为什么他能……\x02\x03",

            "#177F利昂！\x01",
            "到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x10,
        "#6P我、我不知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x10,
        (
            "#6P刚才收到了一个通讯，\x01",
            "控制权就突然被夺走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x11,
        (
            "#104F#2P这就是所谓的系统入侵吗……\x02\x03",

            "#102F高精度的智能信息处理系统\x01",
            "似乎反倒是成了麻烦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("怀斯曼教授")

    AnonymousTalk(    #354
        (
            "\x07\x05哼哼……\x01",
            "初次见面，拉赛尔博士。\x02\x03",

            "这么了不起的系统\x01",
            "竟然能凭一己之力完成。\x02\x03",

            "不愧是爱普斯泰恩博士的\x01",
            "入室弟子之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #355
        0x11,
        (
            "#102F#2P哼，这算是挖苦吗？\x02\x03",

            "#104F我告诉你，航行控制\x01",
            "是独立于系统的。\x02\x03",

            "就算你想操控也是白费心机！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("怀斯曼教授")

    AnonymousTalk(    #356
        (
            "\x07\x05哪里哪里，\x01",
            "我当然不会这么做了。\x02\x03",

            "只是不想让诸位\x01",
            "错过难得的决定性瞬间，\x02\x03",

            "所以才特意前来通知的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #357
        0x11,
        "#102F#2P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x102,
        "#1046F#6P决定性瞬间……难道是！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(55, 160, -1, -1)
    SetChrName("怀斯曼教授")

    AnonymousTalk(    #359
        (
            "\x07\x05呵呵，你们就到\x01",
            "前方甲板上去欣赏吧。\x02\x03",

            "那么诸位，祝晚上愉快。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x0)
    OP_74(0xC, 0x8, 0x0)
    OP_74(0xC, 0xA, 0x0)
    OP_0D()
    Sleep(200)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x101, 0x102, 600)
    Sleep(300)

    ChrTalk(    #360
        0x101,
        "#1005F#2P约修亚……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 600)
    Sleep(300)

    ChrTalk(    #361
        0x102,
        "#1042F#6P嗯……去甲板上看看！\x02",
    )

    CloseMessageWindow()
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
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_41_99F1 end

    def Function_42_AFFA(): pass

    label("Function_42_AFFA")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x101, 25)
    OP_8E(0xFE, 0xFFFFF27C, 0x7D0, 0x15F7C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF1C8, 0x7D0, 0x15388, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFCCC, 0x7D0, 0x14E60, 0x1770, 0x0)

    def lambda_B046():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B046)
    OP_8E(0xFE, 0xFFFFFB8C, 0x7D0, 0x146CC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_AFFA end

    def Function_43_B06C(): pass

    label("Function_43_B06C")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFF27C, 0x7D0, 0x15F7C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFF1C8, 0x7D0, 0x15388, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFCCC, 0x7D0, 0x14E60, 0x1770, 0x0)

    def lambda_B0B8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0B8)
    OP_8E(0xFE, 0xFFFFFB8C, 0x7D0, 0x146CC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_B06C end

    def Function_44_B0DE(): pass

    label("Function_44_B0DE")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_22(0x7A, 0x1, 0x50)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_6D(20, 2000, 97320, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_BB(0x4, 0x1, 0x1D)
    OP_BD()
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 250, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -650, 2000, 90170, 0)
    SetChrPos(0x8, -1850, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)

    def lambda_B344():

        label("loc_B344")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_B344")

    QueueWorkItem2(0x101, 3, lambda_B344)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #362
        0xC,
        (
            "#176F#2P──安定翼收纳完成。\x02\x03",

            "#178F持续加速至最大战速，\x01",
            "前往湖上的浮游都市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xE,
        "#5P是，长官。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 5)
    Sleep(300)

    ChrTalk(    #364
        0x15,
        "#270F#5P如果敌人出来迎击呢？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(200)

    ChrTalk(    #365
        0xC,
        (
            "#176F#6P……这个嘛。\x02\x03",

            "#170F如果遇到阻碍的话，就请您强行突破，\x01",
            "不过首要目的还是在都市着陆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x15,
        (
            "#272F#5P明白了。\x02\x03",

            "#275F顺便说一下，请不必对我客套。\x02\x03",

            "军衔姑且不论，既然\x01",
            "我现在的职务是炮兵，\x01",
            "就要服从你的指挥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        "#171F#6P……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_B524():
        OP_6D(-650, 2000, 93400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B524)

    def lambda_B53C():
        OP_67(0, 5790, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B53C)
    Sleep(100)
    SetChrSubChip(0x15, 3)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(200)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #368
        0x101,
        (
            "#1004F#6P哎，穆拉先生\x01",
            "还会担任炮手啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x9,
        (
            "#031F因为他曾在帝国导力化\x01",
            "程度最高的机甲师团服役。\x02\x03",

            "别看他长这样，那方面的工作\x01",
            "基本上都能胜任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x15,
        "#276F#5P……『别看他长这样』是多余的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        "#1006F#6P原来是这么回事啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #372
        0x101,
        (
            "#1004F#5P对了，奥利维尔，\x01",
            "你是什么时候换了衣服的？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B68F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B68F)
    Sleep(50)

    def lambda_B6A2():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B6A2)
    Sleep(50)

    def lambda_B6B5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B6B5)

    def lambda_B6C3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B6C3)

    def lambda_B6D1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B6D1)
    Sleep(50)

    def lambda_B6E4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B6E4)

    def lambda_B6F2():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B6F2)
    Sleep(400)

    ChrTalk(    #373
        0x102,
        (
            "#1040F#5P不是要以帝国皇子的\x01",
            "身份进行视察吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x9,
        (
            "#031F#4P哈哈哈。\x01",
            "那只是冠冕堂皇的说辞。\x02\x03",

            "#030F这段旅程一结束，\x01",
            "我那自由且优雅的生活\x01",
            "就要宣告终止了。\x02\x03",

            "至少在那之前，\x01",
            "让我再穿一穿这种轻松的服饰吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xB,
        (
            "#071F#2P哈哈……\x01",
            "可以说是你最后的轻松时光吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#025F#6P呼，要是被埃雷波尼亚的\x01",
            "国民知道的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x9,
        (
            "#035F#4P就算被知道了\x01",
            "我也完全不介意。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(300)

    ChrTalk(    #378
        0x9,
        (
            "#037F#5P如何？二位记者，\x01",
            "要不要在利贝尔通讯上爆这个料呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x16,
        "#143F哟，真的可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x17,
        (
            "#151F那我们就要\x01",
            "把照片拍个够了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x15,
        (
            "#274F#5P拜托，别把这家伙的\x01",
            "胡言乱语都当真了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #382
        0x101,
        (
            "#1016F#5P嗯，先不说这个……\x02\x03",

            "#1015F奈尔先生，你们怎么\x01",
            "又不知不觉地跟上船来了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B996():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B996)

    def lambda_B9A4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B9A4)
    Sleep(50)

    def lambda_B9B7():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B9B7)

    def lambda_B9C5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B9C5)

    def lambda_B9D3():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B9D3)
    Sleep(100)

    ChrTalk(    #383
        0xA,
        (
            "#1382F#5P和古代龙事件时一样，\x01",
            "是祖母指名让你们随行的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x16,
        (
            "#141F嗯，正如您所说的。\x02\x03",

            "是陛下为我们向卡西乌斯\x01",
            "准将美言了几句。\x02\x03",

            "于是我们就作为\x01",
            "随军记者登舰了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x17,
        (
            "#151F我们在哈肯大门也拍下了\x01",
            "公主殿下你们的英姿了呢⊙\x02\x03",

            "请期待冲洗出来的照片哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xA,
        "#1165F#5P谢、谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x12,
        (
            "#551F#6P真拿你没办法……\x01",
            "怎么一点紧张感也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x13,
        "#067F#5P哈、哈哈……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #389
        0x13,
        (
            "#560F#6P说到这个，爷爷。\x01",
            "『零力场发生器』的情况怎样？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB8E():
        OP_6D(-1680, 2000, 94250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BB8E)

    def lambda_BBA6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BBA6)

    def lambda_BBB4():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BBB4)
    Sleep(50)

    def lambda_BBC7():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BBC7)

    def lambda_BBD5():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_BBD5)
    Sleep(50)

    def lambda_BBE8():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BBE8)

    def lambda_BBF6():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBF6)

    def lambda_BC04():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BC04)
    Sleep(50)

    def lambda_BC17():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC17)

    def lambda_BC25():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BC25)

    def lambda_BC33():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BC33)
    Sleep(500)
    SetChrSubChip(0x11, 1)
    Sleep(200)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #390
        0x11,
        (
            "#100F#5P嗯，现在的状况很好。\x02\x03",

            "没什么意外的话\x01",
            "应该能支撑到降落在\x01",
            "浮游都市才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x14,
        (
            "#1064F#4P请、请等一下。\x02\x03",

            "换句话说……\x01",
            "有什么意外就麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x11,
        (
            "#104F#5P嗯，\x01",
            "肯定会坠落吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        "#1019F#6P别说得这么干脆啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(100)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(200)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    SetChrSubChip(0x11, 2)

    ChrTalk(    #394
        0xF,
        "#2P雷达有反应……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xF,
        (
            "#2P隐形舰艇５艘，\x01",
            "正急速接近中。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x77)
    Sleep(500)

    def lambda_BE20():
        OP_6D(20, 2000, 97320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE20)

    def lambda_BE38():
        OP_67(0, 5160, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE38)
    SetChrSubChip(0x15, 4)

    def lambda_BE55():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BE55)

    def lambda_BE63():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BE63)
    Sleep(50)

    def lambda_BE76():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BE76)

    def lambda_BE84():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_BE84)
    Sleep(50)

    def lambda_BE97():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BE97)

    def lambda_BEA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BEA5)
    Sleep(50)

    def lambda_BEB8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BEB8)

    def lambda_BEC6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BEC6)
    Sleep(50)

    def lambda_BED9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BED9)

    def lambda_BEE7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BEE7)
    Sleep(50)

    def lambda_BEFA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BEFA)
    SetChrSubChip(0xF, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #396
        0x15,
        "#270F#5P来了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x102,
        (
            "#1042F似乎是『方舟』所搭载的\x01",
            "高速艇呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x11,
        (
            "#102F#5P呼，总算识破了\x01",
            "敌人的隐形技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xC,
        (
            "#177F#2P──准备展开主炮！\x01",
            "维持最大战速强行突破！\x02\x03",

            "#177F只攻击挡路的舰艇！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #400
        0xE,
        "#1K#5P YES·SIR！\x02",
    )


    ChrTalk(    #401
        0xF,
        "#1K#6P YES·SIR！\x02",
    )


    ChrTalk(    #402
        0x10,
        "#1K#4P YES·SIR！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0810   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_44_B0DE end

    def Function_45_C045(): pass

    label("Function_45_C045")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x0, 0x1, 0xFFFFFFE2, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFF9, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -650, 2000, 90170, 0)
    SetChrPos(0x8, -1850, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0xA, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0xF, 8)
    SetChrChipByIndex(0x10, 9)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -920, 2100, 93680, 0)
    SetChrPos(0xE, -1040, 100, 99020, 0)
    SetChrPos(0xF, -3400, 100, 98950, 315)
    SetChrPos(0x10, 1300, 100, 98950, 45)

    def lambda_C2CC():

        label("loc_C2CC")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_C2CC")

    QueueWorkItem2(0x101, 3, lambda_C2CC)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #403
        0xF,
        "#2P１号、２号、５号敌舰已击坠。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xF,
        (
            "#2P３号和４号\x01",
            "也已经完全甩开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#1018F#6P成功了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xB,
        "#070F#4P嗯，真漂亮！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x9,
        (
            "#035F#4P哎呀……\x01",
            "这就是最尖端的空战吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x15,
        (
            "#277F#5P嗯……\x01",
            "这座主炮很厉害。\x02\x03",

            "威力非常强大，\x01",
            "而且射击精度高，后坐力也小。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x11, 2)
    Sleep(200)

    ChrTalk(    #409
        0x11,
        (
            "#101F#6P哇哈哈，那当然。\x02\x03",

            "#100F本来我还想装上和雷达\x01",
            "连动的迎击炮……\x02\x03",

            "#104F不过，这个课题就留到下次吧。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(200)
    Sleep(100)

    ChrTalk(    #410
        0xF,
        "#2P雷达有反应……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xF,
        (
            "#2P８点钟方向\x01",
            "有一艘全长２５０亚矩的\x01",
            "巨型战舰正在接近中……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)

    ChrTalk(    #412
        0x101,
        "#1020F#6P那、那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x14,
        "#1063F#4P就是那艘『方舟』吗……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(300)

    ChrTalk(    #414
        0xC,
        (
            "#178F#5P……约修亚。\x02\x03",

            "你了解『方舟』的\x01",
            "基本性能和武装吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x102,
        (
            "#1035F机动性和最大战速\x01",
            "都不及『埃尔赛尤』。\x02\x03",

            "#1042F但是，它不仅有强力的主炮，\x01",
            "舰身还被无数的自动炮塔所守护着。\x02\x03",

            "攻击、防御都一样无懈可击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xC,
        "#176F#5P这样啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #417
        0xC,
        (
            "#177F#2P向４点钟方向全速脱离！\x02\x03",

            "一边躲开敌人战列舰的追击，\x01",
            "一边朝浮游都市上空前进！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xE,
        "#5P是，长官！\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x0, 0x2F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT43.dat", 0x0, 0x1)

    label("loc_C763")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C77D")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_C77A")
    Jump("loc_C77D")

    label("loc_C77A")

    Jump("loc_C763")

    label("loc_C77D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_82(0x0, 0x0)
    OP_20(0x7D0)
    Sleep(1000)
    OP_22(0x7A, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    OP_21()
    Sleep(500)

    ChrTalk(    #419
        0xF,
        (
            "#2P……已脱离『方舟』的\x01",
            "射程范围了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        "#1167F#6P呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x13,
        "#562F#6P好、好可怕……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        "#025F#6P真是惊心动魄啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        (
            "#1007F#6P嗯，心脏跳得好快。\x02\x03",

            "#1006F不过，现在可以说已经\x01",
            "完全躲过敌人的攻击了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x102,
        "#1042F#2P不……还不能掉以轻心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x12,
        (
            "#057F#4P嗯，这个对手不能用常理来衡量。\x02\x03",

            "直到最后一刻\x01",
            "都不能够大意。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4410, 1200, 98860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(700)
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #426
        0xF,
        (
            "#2P前方的云散开了……！\x02\x03",

            "已经来到浮游都市上空……！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x0, 0x2F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xF, 0)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT44.dat", 0x83, 0x1)

    label("loc_CA32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA4C")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_CA49")
    Jump("loc_CA4C")

    label("loc_CA49")

    Jump("loc_CA32")

    label("loc_CA4C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_6D(-280, 2000, 94450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    OP_D2(0x6007C, 0x60081, 0x1D)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 29)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x15, 4)
    OP_82(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #427
        0xE,
        "#5P到、到达都市上空了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1020F#6P………好壮观……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xA,
        (
            "#1162F#6P这个……\x01",
            "就是古代塞姆里亚文明的精华吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x14,
        "#1063F#4P……真是超乎想象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x11,
        (
            "#102F#6P嗯……前方可以\x01",
            "看到一根巨大的柱子般的东西。\x02\x03",

            "应该是这座都市的\x01",
            "重要设施之一才对。\x02\x03",

            "如果要着陆的话，\x01",
            "在那附近可能会比较好。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(    #432
        0xC,
        (
            "#176F#2P明白了。\x02\x03",

            "#178F艾柯，周围情况怎样？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xF, 1)
    Sleep(300)

    ChrTalk(    #433
        0xF,
        "#2P……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xF,
        (
            "#2P５０塞尔矩以内\x01",
            "没有敌舰的反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xF,
        (
            "#2P可以认为已经完全\x01",
            "甩掉了『方舟』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xC,
        "#176F#2P好……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #437
        0xC,
        (
            "#170F#2P勒克司，一边减速一边\x01",
            "降落在前方的『柱子』附近。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)

    ChrTalk(    #438
        0xE,
        "#5P是，长官。\x02",
    )

    CloseMessageWindow()

    def lambda_CD2F():
        OP_6D(-420, 2000, 92420, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CD2F)

    def lambda_CD47():
        OP_67(0, 5790, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CD47)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    WaitChrThread(0x101, 0x1)
    OP_63(0x17)
    Fade(250)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x17, 23)
    OP_0D()
    Sleep(500)

    ChrTalk(    #439
        0x17,
        "#153F#4P咦～？\x02",
    )

    CloseMessageWindow()

    def lambda_CDA7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CDA7)

    def lambda_CDB5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_CDB5)
    Sleep(50)

    def lambda_CDC8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDC8)

    def lambda_CDD6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CDD6)
    Sleep(50)

    def lambda_CDE9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CDE9)

    def lambda_CDF7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CDF7)

    def lambda_CE05():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CE05)
    Sleep(50)

    def lambda_CE18():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CE18)

    def lambda_CE26():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CE26)
    Sleep(50)

    def lambda_CE39():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CE39)

    def lambda_CE47():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CE47)
    Sleep(400)

    ChrTalk(    #440
        0x101,
        "#1004F#5P怎么了？朵洛希？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x16,
        (
            "#142F#5P怎么了？\x01",
            "感光结晶回路用完了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x17,
        (
            "#154F#4P啊，不是的。\x01",
            "这个没有问题～\x02\x03",

            "我发觉前面好像有奇怪的\x01",
            "东西在接近～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #443
        0x16,
        "#144F#5P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x101,
        "#1020F#5P不、不会吧！？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_D02B():
        OP_6D(20, 2000, 97320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D02B)

    def lambda_D043():
        OP_67(0, 5160, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D043)

    def lambda_D05B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_D05B)

    def lambda_D069():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D069)

    def lambda_D077():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D077)
    Sleep(50)

    def lambda_D08A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D08A)

    def lambda_D098():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D098)
    Sleep(50)

    def lambda_D0AB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D0AB)
    Sleep(50)

    def lambda_D0BE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D0BE)
    Sleep(50)

    def lambda_D0D1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D0D1)
    Sleep(50)

    def lambda_D0E4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D0E4)

    def lambda_D0F2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D0F2)
    SetChrSubChip(0x15, 4)
    SetChrSubChip(0x11, 2)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_21()

    ChrTalk(    #445
        0xC,
        "#173F#2P──那、那是什么！？\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x3, 0x0, 0x2F)
    FadeToDark(1200, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0810   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_45_C045 end

    def Function_46_D153(): pass

    label("Function_46_D153")

    EventBegin(0x0)
    OP_D2(0x270009, 0x27000D, 0x1D)
    OP_D2(0x270019, 0x27001D, 0x1E)
    OP_D2(0x70025, 0x7002D, 0x1F)
    OP_D2(0x70035, 0x7003D, 0x20)
    OP_D2(0x70055, 0x7005D, 0x21)
    OP_D2(0x70065, 0x7006D, 0x22)
    OP_D2(0x70075, 0x7007D, 0x23)
    OP_D2(0x270089, 0x27008D, 0x24)
    OP_D2(0x2703A1, 0x2703A5, 0x25)
    OP_D2(0x600AC, 0x600B1, 0x26)
    OP_D2(0x600F2, 0x600F7, 0x27)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_71(0x3, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xD, 0x4)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_22(0x7A, 0x1, 0x50)
    OP_6D(-340, 2000, 93880, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0xC, 18)
    SetChrChipByIndex(0xA, 20)
    SetChrChipByIndex(0x11, 21)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x15, 1630, 200, 97420, 90)
    SetChrPos(0x11, -3630, 200, 97420, 270)
    SetChrPos(0xC, -1090, 2000, 93560, 0)
    SetChrPos(0x101, -1840, 2000, 91330, 0)
    SetChrPos(0x102, -750, 2000, 91300, 0)
    SetChrPos(0xB, -190, 2000, 89100, 0)
    SetChrPos(0x14, -2650, 2000, 88000, 0)
    SetChrPos(0x16, -1580, 2000, 87900, 0)
    SetChrPos(0x17, -1170, 2000, 87000, 0)
    SetChrPos(0x13, -2790, 2000, 90230, 0)
    SetChrPos(0x9, -760, 2000, 90170, 0)
    SetChrPos(0x8, -1790, 2000, 89910, 0)
    SetChrPos(0x12, -3280, 2000, 88660, 0)
    SetChrPos(0xA, -2130, 2000, 92320, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0xC, 0x0)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0x101, 29)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x8, 31)
    SetChrChipByIndex(0x9, 32)
    SetChrChipByIndex(0x12, 33)
    SetChrChipByIndex(0x13, 34)
    SetChrChipByIndex(0xB, 35)
    SetChrChipByIndex(0x14, 36)
    SetChrChipByIndex(0xA, 37)
    SetChrChipByIndex(0x16, 38)
    SetChrChipByIndex(0x17, 39)
    OP_22(0x85, 0x0, 0x64)

    def lambda_D3E0():

        label("loc_D3E0")

        OP_7C(0x64, 0x0, 0x3E8, 0xBB8)
        OP_48()
        Jump("loc_D3E0")

    QueueWorkItem2(0x101, 3, lambda_D3E0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #446
        0x101,
        "#1000F#4P啊啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        "#1030F………刚才是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x11,
        (
            "#100F#2P不好！\x01",
            "左翼被切断了！\x02\x03",

            "反重力力场也在下降！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xE,
        "#1P舵、舵变得难以掌控了……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 4)
    Sleep(200)

    ChrTalk(    #450
        0x15,
        "#270F……我来帮忙！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrPos(0x15, 580, 0, 97840, 270)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x15, 24)
    OP_0D()
    OP_8E(0x15, 0xFFFFF8A8, 0x0, 0x17F2A, 0x1388, 0x0)
    OP_8E(0x15, 0xFFFFF934, 0x0, 0x182E0, 0x1388, 0x0)
    Sleep(1000)

    ChrTalk(    #451
        0xC,
        (
            "#170F#4P可恶……\x02\x03",

            "全体人员准备抗冲击！\x02\x03",

            "埃尔赛尤号，紧急着陆！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_23(0x85)
    OP_23(0x7A)
    OP_0D()
    OP_44(0x101, 0x3)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x1)

    label("loc_D586")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D5A0")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_D59D")
    Jump("loc_D5A0")

    label("loc_D59D")

    Jump("loc_D586")

    label("loc_D5A0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_AD(0x2400AC, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_22(0x85, 0x0, 0x64)
    Sleep(3000)
    OP_23(0x85)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_46_D153 end

    def Function_47_D5F8(): pass

    label("Function_47_D5F8")

    OP_24(0x7A, 0x46)
    Sleep(200)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_23(0x7A)
    Return()

    # Function_47_D5F8 end

    def Function_48_D632(): pass

    label("Function_48_D632")

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
        (0, "loc_D6AC"),
        (1, "loc_D6B2"),
        (SWITCH_DEFAULT, "loc_D6B8"),
    )


    label("loc_D6AC")

    OP_A2(0x1200)
    Jump("loc_D6B8")

    label("loc_D6B2")

    OP_A2(0x1201)
    Jump("loc_D6B8")

    label("loc_D6B8")

    Return()

    # Function_48_D632 end

    def Function_49_D6B9(): pass

    label("Function_49_D6B9")

    FadeToDark(0, 0, -1)
    OP_6D(-29190, 2000, 59400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_49_D6B9 end

    def Function_50_D746(): pass

    label("Function_50_D746")

    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_D764"),
        (2, "loc_D7B6"),
        (4, "loc_D812"),
        (3, "loc_D864"),
        (7, "loc_D8BD"),
        (SWITCH_DEFAULT, "loc_D913"),
    )


    label("loc_D764")


    ChrTalk(    #452
        0x101,
        (
            "#1016F啊，这里是船的后侧呢。\x02\x03",

            "#1008F传说中的龙啊……\x01",
            "心里真是七上八下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D913")

    label("loc_D7B6")


    ChrTalk(    #453
        0x103,
        (
            "#025F……这里是后甲板呢。\x02\x03",

            "#020F传说中究竟是什么样子，\x01",
            "真想赶快近距离好好确认一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D913")

    label("loc_D812")


    ChrTalk(    #454
        0x105,
        (
            "#047F这里是船尾呢。\x02\x03",

            "#042F……从古代活到现在的龙。\x01",
            "必须好好看个清楚才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D913")

    label("loc_D864")


    ChrTalk(    #455
        0x104,
        (
            "#033F哎呀，这是船尾吗？\x02\x03",

            "#035F……呵呵，连我在\x01",
            "传说中的龙面前\x01",
            "似乎也略感紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D913")

    label("loc_D8BD")


    ChrTalk(    #456
        0x108,
        (
            "#073F哟，这边是船尾啊。\x02\x03",

            "#070F……对方可是传说中的角色。\x01",
            "一定要亲眼看个仔细。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D913")

    label("loc_D913")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_50_D746 end

    def Function_51_D92F(): pass

    label("Function_51_D92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAB5")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_D959"),
        (2, "loc_D99C"),
        (4, "loc_D9D9"),
        (3, "loc_DA1A"),
        (7, "loc_DA59"),
        (SWITCH_DEFAULT, "loc_DA9A"),
    )


    label("loc_D959")


    ChrTalk(    #457
        0x101,
        (
            "#1007F下去也没意义。\x02\x03",

            "#1000F……现在赶紧去龙所在的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA9A")

    label("loc_D99C")


    ChrTalk(    #458
        0x103,
        (
            "#026F下去也没意义。\x02\x03",

            "#020F……赶紧去龙所在的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA9A")

    label("loc_D9D9")


    ChrTalk(    #459
        0x105,
        (
            "#047F下去也没意义。\x02\x03",

            "#042F……现在赶紧去龙所在的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA9A")

    label("loc_DA1A")


    ChrTalk(    #460
        0x104,
        (
            "#030F……传说中的角色近在眼前。\x02\x03",

            "#035F没必要绕道了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA9A")

    label("loc_DA59")


    ChrTalk(    #461
        0x108,
        (
            "#074F下去也没意义。\x02\x03",

            "#070F……现在赶紧去龙所在的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA9A")

    label("loc_DA9A")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_DAB5")

    Return()

    # Function_51_D92F end

    SaveToFile()

Try(main)
