from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '金',                                   # 12
        '尤莉亚上尉',                           # 13
        '摩尔根将军',                           # 14
        '奈尔',                                 # 15
        '朵洛希',                               # 16
        '阿加特',                               # 17
        '提妲',                                 # 18
        '凯文神父',                             # 19
        '拉赛尔博士',                           # 20
        '福音',                                 # 21
        '零力场发生器',                         # 22
        '艾丝蒂尔',                             # 23
        '约修亚',                               # 24
        '穆拉少校',                             # 25
        '酒杯',                                 # 26
        '酒瓶',                                 # 27
        '酒瓶',                                 # 28
        '烹调师凯西',                           # 29
        '亲卫队队员',                           # 30
        '雷伊',                                 # 31
        '亲卫队队员',                           # 32
        '亲卫队队员',                           # 33
        '酒杯',                                 # 34
        '岩穴鱼',                               # 35
        '岩穴鱼',                               # 36
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        "Function_6_1C83",         # 06, 6
        "Function_7_2C19",         # 07, 7
        "Function_8_3A5B",         # 08, 8
        "Function_9_3F33",         # 09, 9
        "Function_10_42C2",        # 0A, 10
        "Function_11_5059",        # 0B, 11
        "Function_12_51F9",        # 0C, 12
        "Function_13_5317",        # 0D, 13
        "Function_14_5409",        # 0E, 14
        "Function_15_5682",        # 0F, 15
        "Function_16_5B1A",        # 10, 16
        "Function_17_6C08",        # 11, 17
        "Function_18_6D04",        # 12, 18
        "Function_19_7F87",        # 13, 19
        "Function_20_7FD6",        # 14, 20
        "Function_21_802A",        # 15, 21
        "Function_22_805A",        # 16, 22
        "Function_23_808F",        # 17, 23
        "Function_24_88DF",        # 18, 24
        "Function_25_8F1E",        # 19, 25
        "Function_26_9E32",        # 1A, 26
        "Function_27_C2E1",        # 1B, 27
        "Function_28_C344",        # 1C, 28
        "Function_29_C3C7",        # 1D, 29
        "Function_30_C3F9",        # 1E, 30
        "Function_31_C43F",        # 1F, 31
        "Function_32_C485",        # 20, 32
        "Function_33_C4B0",        # 21, 33
        "Function_34_C4DB",        # 22, 34
        "Function_35_C52A",        # 23, 35
        "Function_36_C56F",        # 24, 36
        "Function_37_C5A5",        # 25, 37
        "Function_38_C5EB",        # 26, 38
        "Function_39_C631",        # 27, 39
        "Function_40_C6B8",        # 28, 40
        "Function_41_C747",        # 29, 41
        "Function_42_C7D4",        # 2A, 42
        "Function_43_C865",        # 2B, 43
        "Function_44_C87F",        # 2C, 44
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
    Event(0, 16)
    Jump("loc_ABC")

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_A31")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_ABC")

    label("loc_A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_A47")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_ABC")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_A5D")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_ABC")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_A7C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_ABC")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_A9B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_ABC")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC")
    SetMapFlags(0x10000000)
    Event(0, 17)

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
    Call(0, 43)
    Jump("loc_BFB")

    label("loc_BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Call(0, 44)

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

    Call(0, 10)
    Return()

    # Function_4_E84 end

    def Function_5_E89(): pass

    label("Function_5_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9B")
    TalkBegin(0xFE)
    Jump("loc_F92")

    label("loc_E9B")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F2B")
    Jump("loc_F6D")

    label("loc_F2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F47")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F6D")

    label("loc_F47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F63")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F6D")

    label("loc_F63")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_F92")

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
        (0, "loc_FF0"),
        (1, "loc_1C3A"),
        (2, "loc_1C62"),
        (SWITCH_DEFAULT, "loc_1C65"),
    )


    label("loc_FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_14B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120E")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #0
        0x8,
        (
            "#021F哎呀，好久不见。\x02\x03",

            "#021F呵呵，想不到会以\x01",
            "这种方式重逢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#214F这话是我要说的才对。\x02\x03",

            "真是的，一有什么事\x01",
            "你就拿出鞭子来抽人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#027F我只是稍微\x01",
            "疼爱你一下而已嘛。\x02\x03",

            "#525F如果你喜欢被抽的话，\x01",
            "下次要不要再用力一点呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10B,
        (
            "#216F从、从你嘴里说出来，\x01",
            "就不像是在开玩笑了呢……\x02\x03",

            "#413F总、总之……\x01",
            "既然已经到了这个地步，\x01",
            "我们就没什么好说的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#020F若是互相仇视的话，\x01",
            "只是在帮结社的忙而已呢。\x02\x03",

            "不如我们暂时停战吧。\x02\x03",

            "就让我期待\x01",
            "你的作战能力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10B,
        (
            "#210F哼哼……\x01",
            "你、你等着瞧好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 0)
    OP_A2(0x8)
    OP_A2(0x22A0)
    Jump("loc_14AE")

    label("loc_120E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1286")
    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #6
        0x8,
        (
            "#020F嗯嗯，既然如此，\x01",
            "从前的事情就不必再提。\x02\x03",

            "我们就彼此合作，\x01",
            "一起对抗结社吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 0)
    Jump("loc_14AE")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_13F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1358")

    ChrTalk(    #7
        0x8,
        (
            "#027F左舷的回收如果成功的话，\x01",
            "修理作业似乎就算大致完成了。\x02\x03",

            "我们也在等待\x01",
            "回收的结果如何。\x02\x03",

            "#026F真希望你们探索回来时,\x01",
            "就能够飞起来了……\x02\x03",

            "#525F总之只能相信拉赛尔博士,\x01",
            "然后等待结果了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_13F1")

    label("loc_1358")


    ChrTalk(    #8
        0x8,
        (
            "#027F左舷的回收如果成功的话，\x01",
            "修理作业似乎就算大致完成了。\x02\x03",

            "希望等你们探索回来时,\x01",
            "就能够飞起来了……\x02\x03",

            "#525F总之只能相信拉赛尔博士,\x01",
            "然后等待结果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F1")

    Jump("loc_14AE")

    label("loc_13F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1472")

    ChrTalk(    #9
        0x8,
        (
            "#020F呼，照明总算\x01",
            "顺利恢复了。\x02\x03",

            "但愿工程能够\x01",
            "因此有所进展……\x02\x03",

            "那么，我也该去找一些\x01",
            "力所能及的事情来做了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_14AE")

    label("loc_1472")


    ChrTalk(    #10
        0x8,
        (
            "#020F照明顺利恢复了呢。\x02\x03",

            "但愿工程能够\x01",
            "因此有所进展……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AE")

    Jump("loc_1C37")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1718")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16AE")

    ChrTalk(    #11
        0x8,
        (
            "#020F呵呵，想不到会以\x01",
            "这种方式重逢呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10B,
        (
            "#210F哼，这是我该说的才对。\x02\x03",

            "真是的，一有什么事\x01",
            "你就拿出鞭子来抽人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#020F哎呀？我只是稍微\x01",
            "疼爱你一下而已嘛。\x02\x03",

            "如果你喜欢被抽的话，\x01",
            "下次我也可以令你如愿以偿哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10B,
        (
            "#210F从、从你嘴里说出来，\x01",
            "就不像是在开玩笑了呢……\x02\x03",

            "总、总之……\x01",
            "既然已经到了这个地步，\x01",
            "我们就没什么好说的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#020F若是互相仇视的话，\x01",
            "只是在帮结社的忙而已呢。\x02\x03",

            "不如我们暂时停战吧。\x02\x03",

            "就让我期待\x01",
            "你的作战能力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10B,
        (
            "#210F哼哼……\x01",
            "你、你等着瞧好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x22A0)
    Jump("loc_1715")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_170D")

    ChrTalk(    #17
        0x8,
        (
            "#020F嗯嗯，既然如此，\x01",
            "从前的事情就不必再提。\x02\x03",

            "我们就彼此合作，\x01",
            "一起对抗结社吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1715")

    label("loc_170D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1715")

    label("loc_1715")

    Jump("loc_1C37")

    label("loc_1718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1722")
    Jump("loc_1C37")

    label("loc_1722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_1A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F6")

    ChrTalk(    #18
        0x8,
        (
            "#026F还剩下一座塔……吗。\x02\x03",

            "虽然还不清楚敌人的目的，\x01",
            "不过肯定快要接近尾声了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1002F嗯……\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1808")

    ChrTalk(    #20
        0x106,
        (
            "#050F总之结果就留到\x01",
            "以后去分析吧。\x02\x03",

            "目前必须先前往最后那座塔\x01",
            "阻止他们的行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_1808")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1870")

    ChrTalk(    #21
        0x108,
        (
            "#070F不过，现在分析结果\x01",
            "还为时过早吧。\x02\x03",

            "目前必须先前往最后那座塔\x01",
            "阻止结社的行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_1870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D9")

    ChrTalk(    #22
        0x109,
        (
            "#1060F不过，现在考虑结果\x01",
            "还为时过早吧？\x02\x03",

            "目前必须先前往最后那座塔\x01",
            "阻止他们的行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_18D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1942")

    ChrTalk(    #23
        0x105,
        (
            "#042F不过，现在分析结果\x01",
            "或许还为时过早呢。\x02\x03",

            "目前必须先前往最后那座塔\x01",
            "阻止结社的行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1942")


    ChrTalk(    #24
        0x8,
        (
            "#020F嗯，没错。\x01",
            "今后再去分析也不迟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1035F为了将来不会后悔，\x01",
            "现在应该迅速行动才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1015F终于到最后的塔了吗……\x02\x03",

            "#1002F加上还有玲这个敌人，\x01",
            "大家提高警觉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4A)
    Jump("loc_1A6A")

    label("loc_19F6")


    ChrTalk(    #27
        0x8,
        (
            "#026F塔也只剩下一座了……\x02\x03",

            "#022F虽然还不清楚敌人的目的，\x01",
            "不过肯定快要接近尾声了呢。\x02\x03",

            "你们一路上\x01",
            "也要提高警觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    Jump("loc_1C37")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_1A77")
    Jump("loc_1C37")

    label("loc_1A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_1C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEC")

    ChrTalk(    #28
        0x8,
        (
            "#020F看来这次要轮到金先生出场了。\x02\x03",

            "#025F呼，真遗憾。\x01",
            "没有人陪我一起喝酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x108,
        (
            "#071F哈哈，抱歉。\x01",
            "等回来后再奉陪你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1019F喝酒是无所谓，不过雪拉姐，\x01",
            "你可别一时大意喝多了哦……\x02\x03",

            "说不定之后\x01",
            "还有你出场的机会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#525F呵呵，没问题啦㈱\x02\x03",

            "葡萄酒是\x01",
            "醉不倒我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F嗯、嗯……\x01",
            "我可没在说酒的种类的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1048F感觉又被混过去了呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E49)
    Jump("loc_1C37")

    label("loc_1BEC")


    ChrTalk(    #34
        0x8,
        (
            "#020F那么，你们\x01",
            "一路上要小心。\x02\x03",

            "我在会这里待命，\x01",
            "需要的时候就叫我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C37")

    Jump("loc_1C68")

    label("loc_1C3A")


    ChrTalk(    #35
        0x8,
        "#020F哎呀，要更换成员了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_1C68")

    label("loc_1C62")

    Jump("loc_1C68")

    label("loc_1C65")

    Jump("loc_1C68")

    label("loc_1C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7A")
    TalkEnd(0xFE)
    Jump("loc_1C82")

    label("loc_1C7A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_1C82")

    Return()

    # Function_5_E89 end

    def Function_6_1C83(): pass

    label("Function_6_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_24B9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D1A")
    Jump("loc_1D5C")

    label("loc_1D1A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D36")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D5C")

    label("loc_1D36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D52")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D5C")

    label("loc_1D52")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D5C")

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
        (0, "loc_1DDF"),
        (1, "loc_246F"),
        (2, "loc_24A8"),
        (SWITCH_DEFAULT, "loc_24AB"),
    )


    label("loc_1DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 2)), scpexpr(EXPR_END)), "loc_211C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F84")

    ChrTalk(    #36
        0x9,
        (
            "#031F哟，各位……\x02\x03",

            "你们漂亮地战胜了\x01",
            "『怪盗绅士』嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1002F嗯，好不容易呢。\x02\x03",

            "#1007F虽然最后还是\x01",
            "和以前一样地被他逃掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1040F不过，我们确实\x01",
            "已经击败了他。\x02\x03",

            "应该不必担心\x01",
            "他会继续介入了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#035F呼……\x01",
            "虽然是敌人，但也让人佩服。\x02\x03",

            "不过，我还真想和他\x01",
            "将来在某处再次相逢。\x02\x03",

            "哪方才是真正理解美的人，\x01",
            "一定要一决雌雄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1015F随便你吧……\x02\x03",

            "#1019F不过拜托别给\x01",
            "其它人添麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x229E)
    Jump("loc_1FF3")

    label("loc_1F84")


    ChrTalk(    #41
        0x9,
        (
            "#031F如此漂亮的告别手法，\x01",
            "果然不负『怪盗绅士』之名。\x02\x03",

            "呼，真不愧是我的宿敌……\x01",
            "虽然是敌人，但也让人佩服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF3")

    Jump("loc_2119")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AE")

    ChrTalk(    #42
        0x9,
        (
            "#035F看来『怪盗绅士』\x01",
            "应该不会再插手战斗了……\x02\x03",

            "不过，我还真想和他\x01",
            "将来在某处再次相逢。\x02\x03",

            "哪方才是真正理解美的人，\x01",
            "一定要一决雌雄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1019F（变态宝座决定战……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2119")

    label("loc_20AE")


    ChrTalk(    #44
        0x9,
        (
            "#035F还真想和『怪盗绅士』\x01",
            "将来在某处再次相逢。\x02\x03",

            "究竟谁才是真正理解美学的人，\x01",
            "下次一定要决出胜负才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2119")

    Jump("loc_246C")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_246C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_231D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")
    SetChrSubChip(0x9, 0)

    ChrTalk(    #45
        0xB,
        (
            "#070F虽然想过将来有一天\x01",
            "还能像这样子喝酒……\x02\x03",

            "不过你们这么快就回来了\x01",
            "总觉得喝起来有点不够劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "#031F呼，本来还真想\x01",
            "让他稍微再焦急一点……\x02\x03",

            "不过宰相大人比我想象的还要性急呢。\x01",
            "这样一来就不能再继续拖延下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#075F真是的，不过想不到\x01",
            "这样的人居然会是皇子。\x02\x03",

            "帝国的臣民\x01",
            "真令人同情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x9)
    Jump("loc_231A")

    label("loc_2276")


    ChrTalk(    #48
        0x9,
        (
            "#035F可以的话，我还真想\x01",
            "让他稍微再焦急一点……\x02\x03",

            "不过宰相大人比我想象的还要性急呢。\x01",
            "这样一来就不能再继续拖延下去了。\x02\x03",

            "无法上演感动的会面，\x01",
            "实在是相当没有面子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231A")

    Jump("loc_246C")

    label("loc_231D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240F")

    ChrTalk(    #49
        0x9,
        (
            "#030F看来我们的旅程\x01",
            "也已经进入最后乐章了。\x02\x03",

            "呵呵，我满心期待着\x01",
            "适合点缀最后一幕的终曲。\x02\x03",

            "#037F等一切都料理妥当后\x01",
            "就去格兰赛尔城开场派对吧。\x02\x03",

            "那次晚餐会的怨念……\x01",
            "这一次我一定要发泄出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1016F想、想不到你还真会记恨。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_246C")

    label("loc_240F")


    ChrTalk(    #51
        0x9,
        (
            "#030F看来我们的旅程\x01",
            "也已经进入最后乐章了。\x02\x03",

            "呵呵，我满心期待着\x01",
            "适合点缀最后一幕的终曲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246C")

    Jump("loc_24AE")

    label("loc_246F")


    ChrTalk(    #52
        0x9,
        (
            "#035F呵呵，看来你们需要\x01",
            "我这个天才的力量了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_24AE")

    label("loc_24A8")

    Jump("loc_24AE")

    label("loc_24AB")

    Jump("loc_24AE")

    label("loc_24AE")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2C18")

    label("loc_24B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_26BB")
    TalkBegin(0xFE)
    OP_43(0x9, 0x0, 0x0, 0x3)
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
        (0, "loc_2528"),
        (1, "loc_2676"),
        (2, "loc_26AF"),
        (SWITCH_DEFAULT, "loc_26B2"),
    )


    label("loc_2528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260C")

    ChrTalk(    #53
        0x9,
        (
            "#035F哟，各位好。\x02\x03",

            "你们还喜欢\x01",
            "我的鲁特琴演奏吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1019F真是的，也不看看时候……\x01",
            "你怎么还这么悠闲自在的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#035F呵呵，我是想给在这里休息的\x01",
            "人们提供安宁的心情。\x02\x03",

            "探索的准备我也做好了，\x01",
            "你们就放心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2673")

    label("loc_260C")


    ChrTalk(    #56
        0x9,
        (
            "#035F我是想为在休息室里休息的\x01",
            "人们提供心灵上更深层的宁静……\x02\x03",

            "呼，这就是我们诗人\x01",
            "所背负的使命哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2673")

    Jump("loc_26B5")

    label("loc_2676")


    ChrTalk(    #57
        0x9,
        (
            "#035F呵呵，看来你们需要\x01",
            "我这个天才的力量了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_26B5")

    label("loc_26AF")

    Jump("loc_26B5")

    label("loc_26B2")

    Jump("loc_26B5")

    label("loc_26B5")

    TalkEnd(0xFE)
    Jump("loc_2C18")

    label("loc_26BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_2C18")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2752")
    Jump("loc_2794")

    label("loc_2752")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_276E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2794")

    label("loc_276E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_278A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2794")

    label("loc_278A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2794")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #58
        0x9,
        (
            "#030F哟，艾丝蒂尔。\x01",
            "你在舰内散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1011F嗯，算是吧……\x02\x03",

            "#1019F对了，我说你……\x01",
            "作战前怎么还在喝酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "#035F呼，这是提前庆祝的酒。\x02\x03",

            "庆祝天才诗人和传说中的\x01",
            "龙之间命运的邂逅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015F先不提什么天才诗人……\x01",
            "传说中的…………龙啊。\x02\x03",

            "#1000F难道帝国也有\x01",
            "龙的传说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#031F嗯，当然有。\x02\x03",

            "在离柏斯不远的南部地区\x01",
            "就有很多龙的传说和目击传闻。\x02\x03",

            "『百日战役』之前，\x01",
            "在帝国科学院的号召下，\x01",
            "还曾经组织规划了调查队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1004F哦～好正式啊。\x02\x03",

            "对帝国人来说，古代龙\x01",
            "果然也是未知的存在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "#030F嗯，你大体上\x01",
            "可以这么认为……\x02\x03",

            "不过，帝国人的想法\x01",
            "却更为干脆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1011F干脆……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#030F也就是说与利贝尔王国\x01",
            "相较之下还要更加现实哦。\x02\x03",

            "这次的事件如果发生在帝国，\x01",
            "肯定会立即下达捕杀的命令吧。\x02\x03",

            "#035F因为坚决抵抗外敌\x01",
            "是帝国人一贯的做法。\x02\x03",

            "管他是龙还是什么的，\x01",
            "一律都要统统消灭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1016F感、感觉杀气腾腾的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#034F毕竟以武力来安邦，\x01",
            "是埃雷波尼亚帝国的风格。\x02\x03",

            "这对于身为爱与和平使者的诗人来说\x01",
            "是略感悲哀遗憾的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A20)
    Jump("loc_2C10")

    label("loc_2B67")


    ChrTalk(    #69
        0x9,
        (
            "#035F虽然龙逃往帝国\x01",
            "也是个相当有意思的情节……\x02\x03",

            "#030F不过一旦成为现实，或许会被\x01",
            "尽可能地当成新纷争的借口。\x02\x03",

            "摩尔根将军应该也是再三考虑过\x01",
            "这种状况后才进行指挥的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C10")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_2C18")

    Return()

    # Function_6_1C83 end

    def Function_7_2C19(): pass

    label("Function_7_2C19")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CA9")
    Jump("loc_2CEB")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CC5")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CEB")

    label("loc_2CC5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CE1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CEB")

    label("loc_2CE1")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CEB")

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
        (0, "loc_2D6E"),
        (1, "loc_3A2C"),
        (2, "loc_3A4C"),
        (SWITCH_DEFAULT, "loc_3A4F"),
    )


    label("loc_2D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_3060")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBE")
    SetChrSubChip(0xB, 0)

    ChrTalk(    #70
        0xB,
        (
            "#070F虽然想过将来有一天\x01",
            "还能像这样子喝酒……\x02\x03",

            "不过你们这么快就回来了\x01",
            "总觉得喝起来有点不够劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#031F呼，本来还真想\x01",
            "让他稍微再焦急一点……\x02\x03",

            "不过宰相大人比我想象的还要性急呢。\x01",
            "这样一来就不能再继续拖延下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#075F真是的，不过想不到\x01",
            "这样的人居然会是皇子。\x02\x03",

            "帝国的臣民\x01",
            "真令人同情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x9)
    Jump("loc_2F11")

    label("loc_2EBE")


    ChrTalk(    #73
        0xB,
        (
            "#075F真是的……\x01",
            "这样的人居然会是皇子。\x02\x03",

            "真不禁要为帝国的\x01",
            "臣民流下同情的眼泪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F11")

    Jump("loc_305D")

    label("loc_2F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEE")

    ChrTalk(    #74
        0xB,
        (
            "#070F哎呀哎呀，终于可以在船内\x01",
            "放松休息一下了。\x02\x03",

            "#072F不过，我们的工作\x01",
            "恐怕从现在起才正式开始吧。\x02\x03",

            "在中枢塔之中应该会接连\x01",
            "遭遇到比以往更严酷的战斗。\x02\x03",

            "万一遇到什么危险的话，\x01",
            "不要勉强，先回到这里再说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_305D")

    label("loc_2FEE")


    ChrTalk(    #75
        0xB,
        (
            "#072F在中枢塔之中应该会接连\x01",
            "遭遇到比以往更严酷的战斗。\x02\x03",

            "万一遇到什么危险的话，\x01",
            "不要勉强，先回到这里再说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305D")

    Jump("loc_3A29")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_31BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(    #76
        0xB,
        (
            "#072F最后等待着我们的执行者是\x01",
            "『歼灭天使』玲啊……\x02\x03",

            "她那一套将我们玩弄于\x01",
            "股掌的纯熟手段，\x01",
            "实在无法想象是如何学来的。\x02\x03",

            "#572F那个女孩子……\x02\x03",

            "说不定背负着\x01",
            "不简单的过去。\x02\x03",

            "毕竟要获得强大的力量，\x01",
            "就必须付出相应的代价才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_31BB")

    label("loc_3154")


    ChrTalk(    #77
        0xB,
        (
            "#072F她那一套将我们玩弄于股掌的纯熟手段，\x01",
            "实在无法想象是如何学来的。\x02\x03",

            "说不定背负着\x01",
            "不简单的过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BB")

    Jump("loc_3A29")

    label("loc_31BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3351")

    ChrTalk(    #78
        0xB,
        (
            "#070F哦，你们几个要\x01",
            "进入下一座塔了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        "#1040F嗯，做好准备就去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1011F金先生正在\x01",
            "稍做休息吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "#070F嗯，老实说\x01",
            "我是很想休息一下……\x02\x03",

            "不过现在可不是时候。\x01",
            "你们需要的话我就马上出动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#021F呵呵，不用勉强。\x02\x03",

            "你已经击退了那个瓦鲁特，\x01",
            "就稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1040F嗯，不能勉强自己哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xB,
        (
            "#070F哈哈，谢谢大家的关心。\x02\x03",

            "不过你们不用客气。\x01",
            "需要帮忙的话请尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E43)
    Jump("loc_33B4")

    label("loc_3351")


    ChrTalk(    #85
        0xB,
        (
            "#070F说实话是想休息一下，\x01",
            "不过现在可不是时候。\x02\x03",

            "需要我的拳头帮忙时，\x01",
            "不用客气，叫我一声就行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B4")

    Jump("loc_3A29")

    label("loc_33B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_33C1")
    Jump("loc_3A29")

    label("loc_33C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DC")

    ChrTalk(    #86
        0xB,
        "#070F哟，是你们啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3444")

    ChrTalk(    #87
        0x103,
        (
            "#020F咦，今天是一个人吗？\x02\x03",

            "一个人静静地喝酒，\x01",
            "在你身上还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D0")

    label("loc_3444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_349F")

    ChrTalk(    #88
        0x106,
        (
            "#051F哎，今天是一个人哦。\x02\x03",

            "一个人静静地喝酒，\x01",
            "在你身上还真是少见啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D0")

    label("loc_349F")


    ChrTalk(    #89
        0x102,
        (
            "#1044F咦，今天是一个人？\x01",
            "实在是相当罕见呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D0")


    ChrTalk(    #90
        0xB,
        (
            "#071F哈哈，因为\x01",
            "能和我喝酒的朋友已经回国去了。\x02\x03",

            "尽管没能赶上，\x01",
            "不过还是敬他一杯送别的酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1015F是吗……\x02\x03",

            "金先生确实是经常和\x01",
            "奥利维尔对饮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        (
            "#1041F想想的话，\x01",
            "这个组合似乎也挺不可思议的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C5")

    ChrTalk(    #93
        0x105,
        "#048F呵呵，确实……\x02",
    )

    CloseMessageWindow()
    Jump("loc_363C")

    label("loc_35C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35EF")

    ChrTalk(    #94
        0x107,
        "#560F嘿嘿，也是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_363C")

    label("loc_35EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3617")

    ChrTalk(    #95
        0x106,
        "#051F嘿嘿，确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_363C")

    label("loc_3617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_363C")

    ChrTalk(    #96
        0x103,
        "#021F呵呵，确实。\x02",
    )

    CloseMessageWindow()

    label("loc_363C")


    ChrTalk(    #97
        0xB,
        (
            "#074F是啊，除了喜欢酒之外\x01",
            "几乎没有什么共通点。\x02\x03",

            "#070F但说不定正因为这样，\x01",
            "我们两个才会一拍即合的吧。\x02\x03",

            "因为人们都会寻求\x01",
            "自身所欠缺的事物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1011F原来如此……这也有可能。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B9")

    ChrTalk(    #99
        0x103,
        (
            "#525F也好，今后\x01",
            "你就找我一起喝酒吧。\x02\x03",

            "一个人喝对身体不好哦㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #100
        0x101,
        (
            "#1015F咦？可是……\x02\x03",

            "（和雪拉姐一起喝，\x01",
            "  我觉得对身体更不好……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#1048F（……被她听见会挨鞭子的哦。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3983")

    label("loc_37B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C9")

    ChrTalk(    #102
        0x109,
        (
            "#1060F也好，如果方便的话，\x01",
            "下次请找我一起喝酒吧。\x02\x03",

            "毕竟一个人喝\x01",
            "对身体也不好嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)

    ChrTalk(    #103
        0x101,
        (
            "#1004F咦？可是……\x02\x03",

            "神父\x01",
            "可以喝酒吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #104
        0x109,
        (
            "#1068F严格来说\x01",
            "当然不可以……\x02\x03",

            "#1066F不过一点点的话\x01",
            "相信女神也会宽恕我的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1019F真、真是油腔滑调～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3983")

    label("loc_38C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3925")

    ChrTalk(    #106
        0x106,
        (
            "#051F也好，以后就\x01",
            "找我们一起喝酒吧。\x02\x03",

            "虽然不像那家伙\x01",
            "那么会制造气氛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3983")

    label("loc_3925")


    ChrTalk(    #107
        0x102,
        (
            "#1040F如果觉得方便的话，\x01",
            "以后请找我们一起作陪吧。\x02\x03",

            "虽然我不会喝酒，\x01",
            "不过聊天还是可以的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3983")


    ChrTalk(    #108
        0xB,
        (
            "#070F不好意思。\x01",
            "让你们这么费心。\x02\x03",

            "嗯，难得有这样的提议，\x01",
            "过几天我再来邀约吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E28)
    Jump("loc_3A29")

    label("loc_39DC")


    ChrTalk(    #109
        0xB,
        (
            "#070F我暂时还要\x01",
            "在这里多喝几杯。\x02\x03",

            "如果需要帮忙的话，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A29")

    Jump("loc_3A52")

    label("loc_3A2C")


    ChrTalk(    #110
        0xB,
        "#070F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_3A52")

    label("loc_3A4C")

    Jump("loc_3A52")

    label("loc_3A4F")

    Jump("loc_3A52")

    label("loc_3A52")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_2C19 end

    def Function_8_3A5B(): pass

    label("Function_8_3A5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3AC4")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A87")
    SetChrSubChip(0xFE, 0)
    Jump("loc_3AB8")

    label("loc_3A87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A9D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_3AB8")

    label("loc_3A9D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AB3")
    SetChrSubChip(0xFE, 1)
    Jump("loc_3AB8")

    label("loc_3AB3")

    SetChrSubChip(0xFE, 0)

    label("loc_3AB8")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)

    label("loc_3AC4")

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
        (0, "loc_3B22"),
        (1, "loc_3F04"),
        (2, "loc_3F24"),
        (SWITCH_DEFAULT, "loc_3F27"),
    )


    label("loc_3B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C17")

    ChrTalk(    #111
        0x10,
        (
            "#051F哦，雪拉扎德。\x01",
            "这次轮到你出场了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#025F嗯，看来是这样。\x02\x03",

            "不能陪你喝酒实在很遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10,
        (
            "#051F喝酒无所谓，需要我帮忙的话\x01",
            "随时叫我吧。\x02\x03",

            "……需要时尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        (
            "#525F呵呵，谢谢你了。\x01",
            "我会记住这个人情的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E45)
    SetChrSubChip(0xFE, 0)
    Jump("loc_3C54")

    label("loc_3C17")


    ChrTalk(    #115
        0x10,
        (
            "#051F要帮忙的话\x01",
            "随时叫我吧。\x02\x03",

            "……需要时尽管说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_3C54")

    Jump("loc_3F01")

    label("loc_3C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3CDE")

    ChrTalk(    #116
        0x10,
        (
            "#053F『瘦狼』吗……\x02\x03",

            "在蔡斯时，我们几个\x01",
            "对他根本束手无策。\x02\x03",

            "#050F不过你要是在的话\x01",
            "说不定情况会好一点……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4E")

    label("loc_3CDE")


    ChrTalk(    #117
        0x10,
        (
            "#053F『瘦狼』瓦鲁特吗……\x02\x03",

            "听说大家在蔡斯时\x01",
            "被他整得很惨呢。\x02\x03",

            "#050F不过你要是在的话\x01",
            "说不定情况会好一点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4E")


    ChrTalk(    #118
        0x108,
        (
            "#070F别那么抬举我。\x01",
            "行不行得通，\x01",
            "得要较量过后才知道。\x02\x03",

            "如果有兴趣的话\x01",
            "你也一起过来如何？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x108, 400)

    ChrTalk(    #119
        0x10,
        (
            "#051F嘿，也对，\x02\x03",

            "我会准备妥当的。\x01",
            "有需要的话随时叫我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1006F啊，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#1040F拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E44)
    Jump("loc_3F01")

    label("loc_3E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E94")
    TurnDirection(0x10, 0x108, 0)

    ChrTalk(    #122
        0x10,
        (
            "#050F『瘦狼』……\x01",
            "那家伙的武技可是绝非寻常。\x02\x03",

            "#051F嘿嘿，我真想见识\x01",
            "你能跟他对抗到什么程度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F01")

    label("loc_3E94")

    TurnDirection(0x10, 0x108, 0)

    ChrTalk(    #123
        0x10,
        (
            "#050F『瘦狼』瓦鲁特吗……\x01",
            "似乎是个掌握极强武技的家伙。\x02\x03",

            "#051F嘿嘿，你和他\x01",
            "之间的战斗一定很精彩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F01")

    Jump("loc_3F2A")

    label("loc_3F04")


    ChrTalk(    #124
        0x10,
        "#050F要更换成员了？\x02",
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_3F2A")

    label("loc_3F24")

    Jump("loc_3F2A")

    label("loc_3F27")

    Jump("loc_3F2A")

    label("loc_3F2A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_8_3A5B end

    def Function_9_3F33(): pass

    label("Function_9_3F33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_42BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4259")

    ChrTalk(    #125
        0xD,
        "#160F……怎么，原来是你啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1000F怎么了？摩尔根将军，\x01",
            "你怎么会一个人在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xD,
        (
            "#160F嗯，我正在重新\x01",
            "检查一遍作战计划。\x02\x03",

            "即使看上去很完美的计划，\x01",
            "过些时间再回顾一下的话\x01",
            "也能够找出漏洞来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1002F那么……\x01",
            "发现什么缺陷了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "#163F不，现在还没有……\x02\x03",

            "只要没发生太大的意外，\x01",
            "这次作战应该能取得成功。\x02\x03",

            "#165F很遗憾，这次应该是\x01",
            "没有你们出场的机会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1015F嗯，那就最好了……\x02\x03",

            "#1002F不过紧要关头\x01",
            "我们还是会帮忙的。\x02\x03",

            "因为你准许我们登舰，\x01",
            "就代表多少对我们有些期待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        (
            "#160F当然，我是有这个意思……\x02\x03",

            "不过必须等我们的作战完成后，\x01",
            "你们几个才能够自由行动。\x02\x03",

            "作战行动时毕竟\x01",
            "还是要听从我们的指挥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1006F没问题，我明白的。\x02\x03",

            "我们会先乖乖地\x01",
            "在一旁观看你们的表演。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xD,
        (
            "#165F哼……小姑娘口气倒不小。\x02\x03",

            "在和龙对战之前\x01",
            "还有一些时间。\x02\x03",

            "你们就趁这个时候\x01",
            "就尽量准备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A72)
    Jump("loc_42BE")

    label("loc_4259")


    ChrTalk(    #134
        0xD,
        (
            "#160F必须等我们的作战完成后，\x01",
            "你们游击士才能够自由行动。\x02\x03",

            "作战行动时毕竟\x01",
            "还是要听从我们的指挥。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BE")

    TalkEnd(0xFE)
    Return()

    # Function_9_3F33 end

    def Function_10_42C2(): pass

    label("Function_10_42C2")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_44A4")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西(道具)\x01",                          # 1
            "买东西(食材)\x01",                          # 2
            "招牌菜『苦味菜肉蛋卷』　1800米拉\x01",      # 3
            "离开\x01",                                  # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4369")
    OP_A9(0x2C)
    TalkEnd(0x1C)
    Return()

    label("loc_4369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437F")
    OP_A9(0x2B)
    TalkEnd(0x1C)
    Return()

    label("loc_437F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4490")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4458")
    SubMira(1800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #135
        "\x06\x07\x02苦味菜肉蛋卷\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x9C4)
    OP_31(0x1, 0xFD, 0x9C4)
    OP_31(0x2, 0xFD, 0x9C4)
    OP_31(0x3, 0xFD, 0x9C4)
    OP_31(0x4, 0xFD, 0x9C4)
    OP_31(0x5, 0xFD, 0x9C4)
    OP_31(0x6, 0xFD, 0x9C4)
    OP_31(0x7, 0xFD, 0x9C4)
    OP_31(0x8, 0xFD, 0x9C4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_444A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xC)"), scpexpr(EXPR_END)), "loc_441E")
    Jump("loc_444A")

    label("loc_441E")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x06\x07\x02苦味菜肉蛋卷\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_444A")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_447E")

    label("loc_4458")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #137
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_447E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x1C)
    Return()

    label("loc_4490")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A1")
    TalkEnd(0x1C)
    Return()

    label("loc_44A1")

    Jump("loc_4542")

    label("loc_44A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4542")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",              # 0
            "买东西(道具)\x01",      # 1
            "买东西(食材)\x01",      # 2
            "离开\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451B")
    OP_A9(0x2A)
    TalkEnd(0x1C)
    Return()

    label("loc_451B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4531")
    OP_A9(0x2B)
    TalkEnd(0x1C)
    Return()

    label("loc_4531")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4542")
    TalkEnd(0x1C)
    Return()

    label("loc_4542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_464D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F2")

    ChrTalk(    #138
        0x1C,
        "……哟，是你们啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x1C,
        (
            "终于要开始探索\x01",
            "都市的中枢了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x1C,
        (
            "『埃尔赛尤』也应该能\x01",
            "飞起来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x1C,
        (
            "……你们一定要平安返回啊。\x01",
            "大家要一起回到陆地。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_464A")

    label("loc_45F2")


    ChrTalk(    #142
        0x1C,
        (
            "『埃尔赛尤』也应该能\x01",
            "飞起来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x1C,
        (
            "你们一定要平安返回啊。\x01",
            "大家要一起回到陆地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464A")

    Jump("loc_5055")

    label("loc_464D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4723")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B6")

    ChrTalk(    #144
        0x1C,
        (
            "嗯……\x01",
            "鲁特琴弹得真不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x1C,
        (
            "看来这演奏家的自称\x01",
            "可不是吹牛的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_46D5")

    label("loc_46B6")


    ChrTalk(    #146
        0x1C,
        (
            "嗯……\x01",
            "鲁特琴弹得真不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D5")

    Jump("loc_4720")

    label("loc_46D8")


    ChrTalk(    #147
        0x1C,
        (
            "看来要和空贼团\x01",
            "合作了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x1C,
        (
            "想不到那位尤莉亚\x01",
            "竟然真的同意了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4720")

    Jump("loc_5055")

    label("loc_4723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_47FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47AB")

    ChrTalk(    #149
        0x1C,
        (
            "由于在作战前\x01",
            "囤积了很多物品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x1C,
        (
            "我店内的商品种类\x01",
            "也比之前丰富许多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x1C,
        (
            "你们就尽情地享受\x01",
            "购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_47F9")

    label("loc_47AB")


    ChrTalk(    #152
        0x1C,
        (
            "由于在作战前\x01",
            "囤积了很多物品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x1C,
        (
            "我店内的商品种类\x01",
            "也比之前丰富许多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F9")

    Jump("loc_5055")

    label("loc_47FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_48D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488A")

    ChrTalk(    #154
        0x1C,
        (
            "………………………………\x01",
            "……哦，是你们啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1C,
        (
            "我的店也\x01",
            "总算整理完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x1C,
        (
            "在进行探索之前\x01",
            "好好补充一下装备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_48D2")

    label("loc_488A")


    ChrTalk(    #157
        0x1C,
        (
            "我的店也\x01",
            "总算整理完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x1C,
        (
            "在进行探索之前\x01",
            "好好补充一下装备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D2")

    Jump("loc_5055")

    label("loc_48D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_49E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498E")

    ChrTalk(    #159
        0x1C,
        (
            "『四轮之塔』也\x01",
            "只剩下一座了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1C,
        (
            "……这个任务也终于\x01",
            "快要完成了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x1C,
        (
            "但是，在空中旅行的时候，\x01",
            "总是起飞和降落最危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1C,
        "……尽可能地小心吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_49E2")

    label("loc_498E")


    ChrTalk(    #163
        0x1C,
        (
            "在空中旅行的时候，\x01",
            "总是起飞和降落最危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x1C,
        (
            "越到最后……\x01",
            "就越要小心行事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E2")

    Jump("loc_4DE3")

    label("loc_49E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4B02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8F")

    ChrTalk(    #165
        0x1C,
        (
            "……王国各地\x01",
            "据说都在发生事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x1C,
        (
            "地方部队光是要应付这些，\x01",
            "恐怕就已经疲于奔命了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1C,
        (
            "……把塔的任务交给游击士，\x01",
            "真可以说是大大的成功啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4AFF")

    label("loc_4A8F")


    ChrTalk(    #168
        0x1C,
        (
            "……把塔的任务交给游击士，\x01",
            "从战略上来看是正确的决断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1C,
        (
            "这种漂亮的用人方式，\x01",
            "真像是卡西乌斯准将的风格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFF")

    Jump("loc_4DE3")

    label("loc_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4D02")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCA")

    ChrTalk(    #170
        0x1C,
        (
            "那张座位上的女人…\x01",
            "酒量看起来相当不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x1C,
        (
            "我也想来上一杯，不过很不巧，\x01",
            "现在正在作战前的待命状态……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1C,
        "酒会降低人的判断能力……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x1C,
        "……我还是先忍着点吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4C4F")

    label("loc_4BCA")


    ChrTalk(    #174
        0x1C,
        (
            "酒会让人幸福，\x01",
            "同时也会降低人的理智……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x1C,
        (
            "从这个事实可以导出一个\x01",
            "极为单纯的结论……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x1C,
        (
            "那就是——理智\x01",
            "正是我们不幸的元凶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C4F")

    Jump("loc_4CFF")

    label("loc_4C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC6")

    ChrTalk(    #177
        0x1C,
        (
            "哟，你们调查辛苦了。\x01",
            "在出发前先填饱肚子怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x1C,
        (
            "适度地吃点东西，\x01",
            "紧要关头时就拿得出力气来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_4CFF")

    label("loc_4CC6")


    ChrTalk(    #179
        0x1C,
        (
            "在出发前先填饱肚子怎么样？\x01",
            "事先吃点东西比较有力气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CFF")

    Jump("loc_4DE3")

    label("loc_4D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA0")

    ChrTalk(    #180
        0x1C,
        (
            "哦，是你们啊……\x01",
            "怎么又来了？挺好奇的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x1C,
        (
            "这里从日用品到食品，\x01",
            "各种商品一应俱全……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x1C,
        (
            "……如果需要什么东西，\x01",
            "可以随时过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4DE3")

    label("loc_4DA0")


    ChrTalk(    #183
        0x1C,
        "这里是舰内的小卖部……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x1C,
        (
            "如果需要什么东西，\x01",
            "可以随时过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE3")

    Jump("loc_5055")

    label("loc_4DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB4")

    ChrTalk(    #185
        0x1C,
        "哟，欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x1C,
        (
            "我叫凯西……\x01",
            "是亲卫队的厨师，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1C,
        (
            "同时也经营小卖部，\x01",
            "不过现在还没开张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x1C,
        (
            "……下次有机会\x01",
            "再前来快乐地购物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_END)), "loc_4FAE")

    ChrTalk(    #189
        0x101,
        "#1011F咦，小卖部没营业？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #190
        0x101,
        (
            "#1015F……可是那里\x01",
            "有个人正在喝酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1C,
        "那是我请他喝的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1C,
        (
            "我在检查酒的残量时，\x01",
            "他跑过来跟我聊天……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x1C,
        (
            "我见他相当精于此道，\x01",
            "于是就请他喝了一杯……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1C, 400)
    Sleep(500)

    ChrTalk(    #194
        0x101,
        (
            "#1004F是、是这么回事啊……\x02\x03",

            "(奥利维尔自称美食家，\x01",
            "看来也不像是在吹牛啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAE")

    OP_A2(0x0)
    Jump("loc_5055")

    label("loc_4FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 0)), scpexpr(EXPR_END)), "loc_500E")

    ChrTalk(    #195
        0x1C,
        (
            "那个金发男人……\x01",
            "好像是帝国人的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x1C,
        (
            "……不过对于\x01",
            "葡萄酒的品味不坏。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5055")

    label("loc_500E")


    ChrTalk(    #197
        0x1C,
        "抱歉，现在还没开张……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x1C,
        (
            "下次有机会的话\x01",
            "再前来快乐地购物吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5055")

    TalkEnd(0x1C)
    Return()

    # Function_10_42C2 end

    def Function_11_5059(): pass

    label("Function_11_5059")

    TalkBegin(0xFE)
    SetChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_507E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_50AF")

    label("loc_507E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5094")
    SetChrSubChip(0xFE, 1)
    Jump("loc_50AF")

    label("loc_5094")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50AA")
    SetChrSubChip(0xFE, 2)
    Jump("loc_50AF")

    label("loc_50AA")

    SetChrSubChip(0xFE, 0)

    label("loc_50AF")

    OP_8C(0xFE, 0, 0)
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512A")

    ChrTalk(    #199
        0xFE,
        (
            "嗯，好久没有听过现场\x01",
            "演奏的鲁特琴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "音乐果然是好东西呢。\x01",
            "令人心情舒坦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_5153")

    label("loc_512A")


    ChrTalk(    #201
        0xFE,
        (
            "音乐果然是好东西呢。\x01",
            "令人心情舒坦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5153")

    Jump("loc_51F0")

    label("loc_5156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A8")

    ChrTalk(    #202
        0xFE,
        (
            "那么，接下来\x01",
            "该去填饱肚子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "等一下又要\x01",
            "到现场去接班了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_51F0")

    label("loc_51A8")


    ChrTalk(    #204
        0xFE,
        (
            "那么，接下来\x01",
            "该去填饱肚子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "问问凯西今天有什么\x01",
            "招牌菜吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F0")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_11_5059 end

    def Function_12_51F9(): pass

    label("Function_12_51F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B3")

    ChrTalk(    #206
        0xFE,
        (
            "当长期出航时，\x01",
            "我每天都在这里用餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "在严肃的工作中，\x01",
            "只有这是唯一的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "为了不让我们吃腻，\x01",
            "天天都要变换不同的菜色。\x01",
            "所以厨师的责任也十分重大哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_5313")

    label("loc_52B3")


    ChrTalk(    #209
        0xFE,
        (
            "当长期出航时，\x01",
            "我每天都在这里用餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "幸好厨师的水平相当高，\x01",
            "我们都觉得这是我们的福气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5313")

    TalkEnd(0xFE)
    Return()

    # Function_12_51F9 end

    def Function_13_5317(): pass

    label("Function_13_5317")

    TalkBegin(0xFE)
    SetChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_533C")
    SetChrSubChip(0xFE, 0)
    Jump("loc_536D")

    label("loc_533C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5352")
    SetChrSubChip(0xFE, 2)
    Jump("loc_536D")

    label("loc_5352")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5368")
    SetChrSubChip(0xFE, 1)
    Jump("loc_536D")

    label("loc_5368")

    SetChrSubChip(0xFE, 0)

    label("loc_536D")

    OP_8C(0xFE, 180, 0)
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C9")

    ChrTalk(    #211
        0xFE,
        (
            "呼，我先过来\x01",
            "休息一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "不过很快就要\x01",
            "到外面去接班了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_5400")

    label("loc_53C9")


    ChrTalk(    #213
        0xFE,
        (
            "呼，我先过来\x01",
            "休息一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "好，吃饭了吃饭了。\x02",
    )

    CloseMessageWindow()

    label("loc_5400")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_13_5317 end

    def Function_14_5409(): pass

    label("Function_14_5409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_5416")
    Jump("loc_567E")

    label("loc_5416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_5590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551B")

    ChrTalk(    #215
        0xFE,
        (
            "……热气从表面看来虽然消散了，\x01",
            "但实际上还停留在大气之中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "……被吸收了导力也一样，\x01",
            "必定会被保存在某个地方才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "……『里塔』的存在……\x01",
            "…………被折叠的次元……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "……那些蒸发掉的导力的去处，\x01",
            "也会在那里找到某些提示吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_558D")

    label("loc_551B")


    ChrTalk(    #219
        0xFE,
        (
            "……『里塔』的存在……\x01",
            "…………被折叠的次元……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "……那些蒸发掉的导力的去处，\x01",
            "也会在那里找到某些提示吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_558D")

    Jump("loc_567E")

    label("loc_5590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_567E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5628")

    ChrTalk(    #221
        0xFE,
        (
            "听说蔡斯那边\x01",
            "正陷入了危急的状况中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "呼，看来我们的研究\x01",
            "也要快点拿出成果来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "这下子必须要一鼓作气地\x01",
            "努力工作才行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_567E")

    label("loc_5628")


    ChrTalk(    #224
        0xFE,
        (
            "听说蔡斯那边\x01",
            "正陷入了危急的状况中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "呼，看来我们的研究\x01",
            "也要快点拿出成果来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567E")

    TalkEnd(0xFE)
    Return()

    # Function_14_5409 end

    def Function_15_5682(): pass

    label("Function_15_5682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_56CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_56B0")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_56CB")

    label("loc_56B0")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_56CB")

    Jump("loc_574C")

    label("loc_56CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_56F1")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_574C")

    label("loc_56F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_5712")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_574C")

    label("loc_5712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_5733")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_574C")

    label("loc_5733")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_574C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_591D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AD")
    Jump("loc_591A")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B8")
    Jump("loc_591A")

    label("loc_57B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5802")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57FB")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2020, 0, -43620, 270)
    SetChrChipByIndex(0x9, 34)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57F8")
    Call(0, 43)

    label("loc_57F8")

    Jump("loc_57FF")

    label("loc_57FB")

    Call(0, 44)

    label("loc_57FF")

    Jump("loc_591A")

    label("loc_5802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5845")
    SetChrPos(0x1A, -180, 750, -48810, 180)
    SetChrPos(0x1B, -200, 750, -49380, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_5845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5880")
    SetChrPos(0x9, -420, 200, -48050, 180)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    ClearChrFlags(0x21, 0x80)

    label("loc_5880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58CD")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -420, 200, -50170, 0)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x22, 0x80)

    label("loc_58CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_591A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_591A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -2370, 200, -48050, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x23, 0x80)

    label("loc_591A")

    Jump("loc_5B18")

    label("loc_591D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_59CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5964")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_5964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_59CB")
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

    label("loc_59CB")

    Jump("loc_5B18")

    label("loc_59CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_5A58")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A10")
    SetChrPos(0x10, -2370, 200, -46010, 0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 27)
    SetChrSubChip(0x10, 0)
    OP_44(0x10, 0x0)

    label("loc_5A10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A55")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0xB, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_5A55")

    Jump("loc_5B18")

    label("loc_5A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_5AD6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A93")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2370, 200, -41880, 0)
    SetChrPos(0x10, 4600, 0, -47630, 270)

    label("loc_5A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AD3")
    SetChrPos(0x8, -2370, 200, -39890, 180)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 20)
    SetChrSubChip(0x8, 0)
    OP_44(0x8, 0x0)
    ClearChrFlags(0x19, 0x80)

    label("loc_5AD3")

    Jump("loc_5B18")

    label("loc_5AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5B18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B18")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2370, 200, -44020, 180)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    OP_44(0x8, 0x0)

    label("loc_5B18")

    OP_0D()
    Return()

    # Function_15_5682 end

    def Function_16_5B1A(): pass

    label("Function_16_5B1A")

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
    SetChrName("摩尔根将军")

    AnonymousTalk(    #226
        (
            "\x07\x00──那么，开始介绍由王国军\x01",
            "执行的『古龙捕获作战』计划。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_5CC6():
        OP_6D(2029, 100, 52820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CC6)

    def lambda_5CDE():
        OP_67(0, 6340, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CDE)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #227
        0xD,
        (
            "#163F#5P本次作战将由\x01",
            "飞行舰队来完成。\x02\x03",

            "地面部队只负责利贝尔各地\x01",
            "的警戒和防卫工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1015F利贝尔各地？就是说\x01",
            "不只是柏斯地区吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xD,
        (
            "#160F#5P根据的昨天的情况来看，\x01",
            "龙的飞行能力相当惊人。\x02\x03",

            "不知其它地方何时又会遭受袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#1003F嗯，的确……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xD,
        (
            "#160F#5P所以在本次的作战里，\x01",
            "除了这艘『埃尔赛尤』之外，\x01",
            "又投入了警备飞艇１２艘。\x02\x03",

            "这相当于所有\x01",
            "警备艇数量的五分之二。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x8,
        "#023F#6P那种警备艇有１２艘啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        "#030F#2P这下可真是大张旗鼓了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xD,
        "#163F#5P──尤莉亚上尉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xC,
        "#178F#5P是。\x02",
    )

    CloseMessageWindow()

    def lambda_5EFF():
        OP_6D(2029, 100, 53820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EFF)
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
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #236
        "\x07\x00#1004F哇哇……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #237
        (
            "\x07\x00#073F这个是……\x01",
            "本次的作战行动图呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #238
        (
            "\x07\x00#163F嗯，没错。\x02\x03",

            "#160F现在，这艘『埃尔赛尤』\x01",
            "正在柏斯上空进行巡航。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #239
        (
            "\x07\x00#160F在本次作战中，『埃尔赛尤』\x01",
            "将担当作战司令部的功能。\x02\x03",

            "至于实际的巡逻任务……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #240
        (
            "\x07\x00#163F就由装载了广域雷达的\x01",
            "８艘警备艇负责。\x02\x03",

            "如果龙出现在上空，\x01",
            "应该能成功捕捉到方位。\x02\x03",

            "#160F然后一旦发现了龙……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 80, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #241
        (
            "\x07\x00#160F警备艇将迅速前往，\x01",
            "用机关炮进行牵制，\x01",
            "并把龙诱导至瓦雷利亚湖上空。\x02",
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
    SetChrName("摩尔根将军")

    AnonymousTalk(    #242
        (
            "\x07\x00#163F而在发现龙的同时，\x01",
            "装载了麻醉弹的警备艇\x01",
            "就会从雷斯顿要塞紧急起飞……\x02",
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
    SetChrName("摩尔根将军")

    AnonymousTalk(    #243
        (
            "\x07\x00#163F──前去迎击被围追堵截的龙。\x02\x03",

            "用飞船上所有的\x01",
            "麻醉弹使龙昏睡。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x8, 0x4, 0, 0, 0)
    OP_C6(0x8, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_6517():
        OP_6D(2029, 100, 52820, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6517)
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

    ChrTalk(    #244
        0xD,
        "#160F#5P这就是『古龙捕获作战』的概要。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        "#1004F哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        (
            "#025F#6P果然和协会的\x01",
            "作战规模不同……\x02\x03",

            "#022F如果龙没有被麻醉弹迷昏，\x01",
            "是不是会从捕获转换为剿灭呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        (
            "#163F#5P嗯……\x02\x03",

            "只能集中整个舰队的火力\x01",
            "来消灭它了。\x02\x03",

            "虽然女王陛下希望我们\x01",
            "优先考虑捕获而非剿灭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#1015F咦……为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xD,
        (
            "#160F#5P毕竟龙是传说中的\x01",
            "极为珍贵的生物。\x02\x03",

            "女王表示不忍心进行剿灭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xA,
        (
            "#043F#2P说得也是……\x02\x03",

            "而且它很有可能是被\x01",
            "『结社』操控了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        "#1007F这样啊……的确。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x101,
        (
            "#1020F说、说到这个！\x02\x03",

            "操纵龙的那个叫莱维的男人\x01",
            "不是持有『福音』吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xD,
        (
            "#163F#5P嗯……\x01",
            "你是说有导力停止现象的危险吧。\x02\x03",

            "#160F据拉赛尔博士所言，\x01",
            "导力停止现象的连锁范围\x01",
            "大约是５亚矩左右。\x02\x03",

            "所以各舰艇将会和龙\x01",
            "保持10亚矩以上的距离。\x02\x03",

            "这样一来应该没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1025F原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x9,
        (
            "#031F#2P嗯，真令人佩服。\x01",
            "这可以说是万全的对策了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xD,
        (
            "#163F我们的『百日战役』经验\x01",
            "也不是毫无意义的。\x02\x03",

            "#160F不过这次作战如果失败的话，\x01",
            "就真的一筹莫展了。\x02\x03",

            "到时候就要拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#1007F话说得这么好听……\x02\x03",

            "#1019F其实你根本不认为\x01",
            "作战会失败吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xD,
        (
            "#163F哼哼，那是自然。\x02\x03",

            "这个计划唯一的问题\x01",
            "就是要在发现龙之前\x01",
            "耐心地等待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#1015F的确……\x01",
            "不过如果这是白费功夫怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xB,
        (
            "#074F#6P不，稍微分析一下『结社』\x01",
            "至今为止的作法就知道那不可能。\x02\x03",

            "#072F他们一定会利用那头龙\x01",
            "做出一些事情来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x101,
        "#1002F嗯……的确是这样。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)
    Sleep(500)

    ChrTalk(    #262
        0xC,
        (
            "#170F#5P那么各位游击士……\x02\x03",

            "一旦发现龙之后，\x01",
            "我们会用广播告知的。\x02\x03",

            "在此之前，\x01",
            "你们就在舰内轻松休息吧。\x02",
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

    # Function_16_5B1A end

    def Function_17_6C08(): pass

    label("Function_17_6C08")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("尤莉亚的声音")

    AnonymousTalk(    #263
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

    ChrTalk(    #264
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

    # Function_17_6C08 end

    def Function_18_6D04(): pass

    label("Function_18_6D04")

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

    ChrTalk(    #265
        0xC,
        (
            "#176F#2P龙逃进了\x01",
            "迷雾峡谷的西北部……\x02\x03",

            "#178F那里是比空贼巢穴\x01",
            "还要更深入的险处。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 1)
    Sleep(400)

    ChrTalk(    #266
        0x105,
        (
            "#042F#5P也就是说，用飞船\x01",
            "很难进行搜索是吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 2)
    Sleep(400)

    ChrTalk(    #267
        0xC,
        (
            "#176F#2P很遗憾……\x02\x03",

            "#175F或许只能从地面\x01",
            "派遣搜索部队了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#1020F#6P等、等一下！\x02\x03",

            "如果派遣大批士兵过去，\x01",
            "龙又会逃跑的哦！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0)
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #269
        0x103,
        (
            "#026F#6P是啊……\x02\x03",

            "#020F最好由少数人进行搜索，\x01",
            "并设法找出龙的破绽来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xD,
        (
            "#160F#2P也就是说，\x01",
            "接下来交给你们是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x108,
        (
            "#074F#6P对于险处的探索，\x01",
            "我们比军人要更加熟悉。\x02\x03",

            "#070F这也是择材而用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xD,
        (
            "#163F#2P……唔………\x02\x03",

            "#160F不过，你们有\x01",
            "明确的搜索方向吗？\x02\x03",

            "我记得峡谷西北部\x01",
            "应该没什么路可走吧。\x02\x03",

            "如果漫无目的地乱找，\x01",
            "几天时间都不够用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#1015F#6P这、这个……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x10, 1000, 0, 40690, 0)

    NpcTalk(    #274
        0x10,
        "青年的声音",
        "#1P……这你不用担心。\x02",
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

    def lambda_7216():
        OP_6D(2800, 100, 48400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7216)

    def lambda_722E():
        OP_67(0, 4370, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_722E)

    def lambda_7246():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7246)

    def lambda_7256():
        OP_6C(52000, 4000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_7256)

    def lambda_7266():
        OP_6B(2840, 4000)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_7266)
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
    OP_43(0x10, 0x1, 0x0, 0x13)
    OP_43(0x11, 0x1, 0x0, 0x14)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #275
        0xD,
        "#161F#5P你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        "#1004F#5P阿加特，提妲！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x10,
        "#051F哟！打扰各位了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x11,
        "#560F#6P那个那个，打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1008F#5P你们怎么会……\x02\x03",

            "#1020F而、而且你的伤…\x01",
            "已经好了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x10,
        (
            "#053F伤口没问题了。\x01",
            "只不过是一点擦伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        "#1019F#5P……提妲，是真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x11,
        (
            "#066F#6P嗯、嗯……\x02\x03",

            "阿加特哥哥已经\x01",
            "不会再勉强乱来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1006F#5P是吗……\x01",
            "那就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xD,
        (
            "#163F#5P哼，体力倒是\x01",
            "永远用不完的样子。\x02\x03",

            "#160F你叫我不用担心，\x01",
            "不过作战的始末你知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x10,
        (
            "#050F嗯，卢格兰老爷子\x01",
            "大致都跟我说过了。\x02\x03",

            "龙消失在\x01",
            "迷雾峡谷西北部了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        "#1015F#5P嗯，是没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x10,
        (
            "#053F关于迷雾峡谷，\x01",
            "我知道有个人很熟悉。\x02\x03",

            "如果去找他的话，应该可以\x01",
            "前往龙所躲藏的西北部吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xD,
        "#161F#5P喔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#1004F#5P那、那是谁呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x10,
        (
            "#051F就是住在峡谷东侧的\x01",
            "维姆拉大叔。\x02\x03",

            "据说他以前曾经去过\x01",
            "没有道路的西北部。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7671")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在后篇见过维姆拉】\x01",        # 0
            "【◇在后篇没见过维姆拉】\x01",      # 1
            "【◇什么也没有变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7665"),
        (1, "loc_766B"),
        (SWITCH_DEFAULT, "loc_7671"),
    )


    label("loc_7665")

    OP_A2(0x1A80)
    Jump("loc_7671")

    label("loc_766B")

    OP_A3(0x1A80)
    Jump("loc_7671")

    label("loc_7671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_76AC")

    ChrTalk(    #291
        0x101,
        (
            "#1011F#5P原来如此，是住在\x01",
            "那间小屋里的大叔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76AC")


    ChrTalk(    #292
        0x104,
        (
            "#031F#5P呼，不愧是游击士。\x02\x03",

            "平时勤劳地收集情报，\x01",
            "终于派上用场了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xD,
        (
            "#163F#5P………………………………\x02\x03",

            "#160F不过，当你们\x01",
            "找到龙之后又要怎么做？\x02\x03",

            "那可不是光靠你们几个\x01",
            "就能轻易消灭的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x10,
        (
            "#050F龙的额头被嵌入了\x01",
            "『福音』对吧？\x02\x03",

            "当然是首先\x01",
            "解决那个东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xD,
        "#161F#5P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x103,
        (
            "#022F#5P仔细想想，龙很有可能是\x01",
            "因为那个东西才会失去控制的。\x02\x03",

            "迄今为止，『福音』\x01",
            "也已经引发了种种异常现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x108,
        (
            "#074F#5P若能使『福音』失效的话，\x01",
            "就可以让龙恢复正常吧。\x02\x03",

            "#070F嗯……道理是说得通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        (
            "#176F#5P说到使『福音』失效，\x01",
            "我想起了凯文先生使用过的方法。\x02\x03",

            "#175F那时候是用古代遗物\x01",
            "大力敲击『福音』，\x01",
            "使其短路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x10,
        (
            "#051F用不着那么麻烦了。\x02\x03",

            "只要连外壳一起\x01",
            "把『福音』破坏就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xC,
        "#173F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1004F#5P等、等等！\x02\x03",

            "要破坏『福音』\x01",
            "有那么容易吗？\x02\x03",

            "我记得它的外壳\x01",
            "是非常坚硬的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x10,
        (
            "#053F关于这一点\x01",
            "也有办法解决了。\x02\x03",

            "#050F……就是它。\x02",
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
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #303
        "\x07\x00#1004F那是……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #304
        (
            "\x07\x00#020F底部好像装着\x01",
            "什么零件的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #305
        0x10,
        (
            "#053F这是今早拉赛尔老爷子\x01",
            "给我寄来的新发明……\x02\x03",

            "#051F用来破坏『福音』\x01",
            "外壳的零件。\x02",
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

    ChrTalk(    #306
        0x101,
        "#1004F#1P#3S咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x104,
        (
            "#033F#5P嗯……\x01",
            "这东西究竟是什么构造？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x11,
        (
            "#061F#6P这个嘛……\x02\x03",

            "#560F这个零件似乎可以\x01",
            "使刀刃部位产生出只让\x01",
            "外壳材质崩溃的高频振动。\x02\x03",

            "由于振动的缘故，使用两三次后\x01",
            "就会因承受不住而坏掉了……\x02\x03",

            "#067F不过只要能够顺利融入刀身，\x01",
            "据说就能够顺利破坏『福音』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        (
            "#1008F#5P虽、虽然我不太明白,\x01",
            "不过似乎是相当厉害的发明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x104,
        (
            "#035F#5P呵……\x01",
            "真不愧是王国第一的天才学者。\x02",
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

    ChrTalk(    #311
        0x10,
        (
            "#053F虽然刚刚才\x01",
            "请提妲帮我装上。\x01",
            "但似乎可以毫无问题地正常运作。\x02\x03",

            "接下来只要找到那条龙，\x01",
            "攻击它的额头部位就可以了……\x02\x03",

            "#051F怎么样，将军大人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xD,
        (
            "#163F#5P真是的……\x02\x03",

            "#160F你们准备得这么齐全\x01",
            "我不是只能点头同意了吗。\x02",
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

    ChrTalk(    #313
        0x101,
        "#1006F#6P那么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x10,
        "#050F这个任务可以交给我们了对吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xD,
        (
            "#163F#5P嗯……\x01",
            "尽你们所能地去做吧。\x02\x03",

            "#160F不过为了以防万一\x01",
            "我会在峡谷周围部署飞行舰队。\x02\x03",

            "以便在龙逃走的时候，\x01",
            "能及时采取应对措施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x10,
        (
            "#051F很好。\x02\x03",

            "你们就别浪费子弹，\x01",
            "还是看看我的厉害吧。\x02",
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

    # Function_18_6D04 end

    def Function_19_7F87(): pass

    label("Function_19_7F87")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 1000, 0, 40690, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7FAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7FAE)
    OP_8E(0xFE, 0x654, 0x0, 0xADDE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_19_7F87 end

    def Function_20_7FD6(): pass

    label("Function_20_7FD6")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 1000, 0, 40690, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8002():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8002)
    OP_8F(0xFE, 0xFFFFFFA6, 0x0, 0xAD7A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_20_7FD6 end

    def Function_21_802A(): pass

    label("Function_21_802A")

    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xA8DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xB84C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_21_802A end

    def Function_22_805A(): pass

    label("Function_22_805A")

    Sleep(500)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xA8DE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xB518, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 0)
    Return()

    # Function_22_805A end

    def Function_23_808F(): pass

    label("Function_23_808F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80A6")
    Call(0, 39)
    Call(0, 40)

    label("loc_80A6")

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

    ChrTalk(    #317
        0x13,
        (
            "#104F#5P原来如此……\x01",
            "竟然是这个样子的啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x101,
        (
            "#1002F#6P总之\x01",
            "那个『β』就先交给博士。\x02\x03",

            "#1004F啊，我还在塔里\x01",
            "发现了这种东西。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #319
        "\x07\x05把在翡翠之塔得到的数据水晶交出。\x02",
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

    ChrTalk(    #320
        0x13,
        (
            "#103F#5P哦……\x01",
            "古代导力文明时用来\x01",
            "储存情报的记忆媒体吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x102,
        (
            "#1042F#6P内部数据\x01",
            "已经损坏了，\x01",
            "能想办法修复吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x13,
        (
            "#104F#5P这样啊……\x02\x03",

            "#100F它好像和结晶回路一样\x01",
            "都是用七耀石材料制成的。\x02\x03",

            "可能要花些时间，不过『卡佩尔』\x01",
            "也许可以想办法分析出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1006F#6P可以帮我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x13,
        "#101F#5P嗯，交给我吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 0)
    Sleep(300)

    ChrTalk(    #325
        0x13,
        (
            "#102F#5P『里塔』似乎拥有着延伸到\x01",
            "其他空间的特殊内部构造.....\x02\x03",

            "#104F嗯嗯……\x01",
            "要是我也能一起去就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x11,
        "#067F爷、爷爷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#1043F#6P恐怕那才是\x01",
            "四轮之塔的真正形态吧。\x02\x03",

            "#1042F封印着『辉之环』\x01",
            "的『设备塔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x12,
        (
            "#1067F既然它恢复了原状，\x01",
            "应该可以放心了才对……\x02\x03",

            "#1068F不过连塔顶的装置也停止了，\x01",
            "这实在让人感到有些在意啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x13,
        "#104F#5P嗯……的确。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1002F#6P无论如何……\x01",
            "我们不能就这样放任\x01",
            "『结社』的那些家伙不管。\x02\x03",

            "#1005F必须赶紧前往下一座塔才行！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "#042F尤莉亚。\x01",
            "得到其它塔的情报了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xC,
        (
            "#176F#5P刚才从蔡斯方面的\x01",
            "侦察部队传来了后续报告。\x02\x03",

            "#178F出现在『红莲之塔』中的，\x01",
            "似乎是一个戴着墨镜的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87AF")
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
        (0, "loc_87A3"),
        (1, "loc_87A9"),
        (SWITCH_DEFAULT, "loc_87AF"),
    )


    label("loc_87A3")

    OP_A2(0x1201)
    Jump("loc_87AF")

    label("loc_87A9")

    OP_A3(0x1200)
    Jump("loc_87AF")

    label("loc_87AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_87D2")

    ChrTalk(    #334
        0x10,
        "#057F『瘦狼』吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_87F2")

    label("loc_87D2")


    ChrTalk(    #335
        0x8,
        "#022F#6P『瘦狼』瓦鲁特……\x02",
    )

    CloseMessageWindow()

    label("loc_87F2")


    ChrTalk(    #336
        0xB,
        (
            "#070F#6P嘿嘿……\x02\x03",

            "#074F面对面一较高下的\x01",
            "机会终于来了。\x02",
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

    ChrTalk(    #337
        0x101,
        "#1026F#5P金先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xB,
        (
            "#070F#6P艾丝蒂尔，约修亚。\x02\x03",

            "我也和你们一起\x01",
            "去『红莲之塔』吧。\x02",
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

    # Function_23_808F end

    def Function_24_88DF(): pass

    label("Function_24_88DF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88F6")
    Call(0, 39)
    Call(0, 41)

    label("loc_88F6")

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

    ChrTalk(    #339
        0x13,
        (
            "#103F#5P什么……\x01",
            "居然只身一人闯入那里。\x02\x03",

            "#101F她本来就是个了不起的女孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xC,
        (
            "#171F#5P说到蔡斯支部的雾香小姐，\x01",
            "我听说是一位非常优秀的女性。\x02\x03",

            "真想和她见一次面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1008F#6P（嗯……\x01",
            "尤莉亚小姐和雾香小姐吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        (
            "#1040F#6P（在优秀程度方面，\x01",
            "搞不好是难分伯仲呢。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x108,
        (
            "#074F#6P先不说这个……\x02\x03",

            "#072F这次也一样，虽然塔恢复原状了，\x01",
            "可是塔顶上的装置却也停止运作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xA,
        (
            "#047F嗯……是啊。\x02\x03",

            "#043F而且出现在塔顶的结界是什么，\x01",
            "我们现在也仍然不得而知……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x11,
        (
            "#063F问题是它为何会\x01",
            "笼罩在塔顶上呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x10,
        (
            "#053F算了，以后再操心吧。\x02\x03",

            "#050F总之现在只能\x01",
            "赶紧前往下一座塔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1015F#6P嗯……说得也是。\x02\x03",

            "#1002F尤莉亚小姐。\x01",
            "有来自其它的塔的后续情报吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xC,
        (
            "#176F#5P嗯嗯……\x01",
            "这次是『绀碧之塔』。\x02\x03",

            "#178F据说出现在那里的是一位\x01",
            "能响起铃音的黑衣女子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#1020F#6P啊……\x02",
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

    ChrTalk(    #350
        0x102,
        (
            "#1043F#5P『幻惑之铃』露茜奥拉……\x02\x03",

            "#1042F#5P我记得她是\x01",
            "雪拉姐认识的人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x8,
        (
            "#026F#6P是啊，是老朋友呢。\x02\x03",

            "#524F接下来似乎该我出场了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        "#1026F#5P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x8,
        (
            "#021F#6P不要摆出那副表情啦。\x02\x03",

            "#020F姐姐是姐姐，\x01",
            "我是我。\x02\x03",

            "我只是去完成\x01",
            "身为游击士的使命而已。\x02",
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

    # Function_24_88DF end

    def Function_25_8F1E(): pass

    label("Function_25_8F1E")

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

    ChrTalk(    #354
        0x13,
        (
            "#100F#5P──这是试制品\x01",
            "『零力场发生器』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x16,
        "#1004F#6P零力场……发生器？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x13,
        (
            "#104F#5P简单地说，\x01",
            "『福音』能够产生\x01",
            "特殊的波长的导力场……\x02\x03",

            "#100F而这种回路就是用来制造出\x01",
            "与其产生的共振相互抵消的力场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x16,
        (
            "#1019F#6P听起来\x01",
            "一点都不简单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x17,
        (
            "#1044F#6P难道说……\x02\x03",

            "这种回路可以防止\x01",
            "『导力停止现象』吗？\x02",
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

    ChrTalk(    #359
        0x16,
        "#1004F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        "#173F#5P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x13,
        (
            "#104F#5P嗯……是这样没错。\x02\x03",

            "#102F说到底，所谓『导力停止现象』\x01",
            "就是导力器的导力\x01",
            "通过『福音』被吸收的现象。\x02\x03",

            "至于『吸往何处』一直都是个谜，\x01",
            "不过到这个地步总算是明朗起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xA,
        (
            "#043F#2P是因为那座浮游都市……\x01",
            "『辉之环』，对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x13,
        (
            "#100F#5P嗯，没错。\x02\x03",

            "#104F『辉之环』是从异次元\x01",
            "通过『福音』这个小缺口\x01",
            "引起了『导力停止现象』。\x02\x03",

            "由于那个缺口太过狭小，\x01",
            "所以只在小范围内造成了影响……\x02\x03",

            "但随着『辉之环』被解放出来，\x01",
            "影响范围一口气扩大了许多。\x02\x03",

            "#102F甚至扩大到\x01",
            "席卷整个王国的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x16,
        "#1026F#6P整个王国……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x17,
        "#1042F#6P这就是这次的现象吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x13,
        (
            "#104F#5P嗯，王国境内\x01",
            "所有的导力器\x01",
            "恐怕都无法运作了。\x02\x03",

            "#100F但是，这个『零力场发生器』\x01",
            "具有防止『环』的干涉的作用。\x02\x03",

            "#101F──换句话说，\x01",
            "在它这边的导力器\x01",
            "可以正常地运作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x11,
        "#560F#2P哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x16,
        "#1008F#6P太、太厉害了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x10,
        (
            "#051F#2P哦，意思是只要用这个\x01",
            "就万事ＯＫ了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x13,
        (
            "#102F#5P不……\x01",
            "还没好用到那个程度。\x02\x03",

            "#104F首先，这只是试制品，\x01",
            "能保护的对象是有限制的。\x02\x03",

            "最多只能保护大小约为\x01",
            "双手可以拿住的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x11,
        "#065F#2P双手可以拿住的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x10,
        (
            "#555F#2P嗯，这么一来\x01",
            "的确相当受限制啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x13,
        (
            "#102F#5P第二……\x01",
            "数量是有限的。\x02\x03",

            "虽说是受了卡西乌斯之托，\x01",
            "但是也只做成了１６个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x16,
        (
            "#1015F#6P１６个……\x01",
            "我觉得已经相当多了。\x02\x03",

            "#1004F这么说，是老爸拜托你的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x13,
        (
            "#100F#5P嗯……\x01",
            "不久前他来过我这里，\x01",
            "拜托我开发这个东西。\x02\x03",

            "#104F当时我根本没想到\x01",
            "会出这样的大乱子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x16,
        "#1016F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xB,
        (
            "#070F#6P不愧是大人。\x01",
            "原来早已预料到了一切啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x12,
        (
            "#1065F可是这么一来……\x02\x03",

            "#1060F这１６个要怎么运用，\x01",
            "大致上都已经决定好了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x13,
        (
            "#103F#5P喔……\x01",
            "你的观察力真是敏锐啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x16, 0)
    Sleep(75)
    SetChrSubChip(0x16, 2)
    Sleep(300)

    ChrTalk(    #380
        0x16,
        "#1004F#5P咦、咦，这话怎么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x12,
        (
            "#1063F#2P在混乱当中最重要的，\x01",
            "就是必须迅速获得正确的情报。\x02\x03",

            "无论是结社的那些家伙现身，\x01",
            "还是运送必需品等等…\x01",
            "都必须要先确保情报的准确传达。\x02\x03",

            "#1062F也就是说……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x17, 0)
    Sleep(75)
    SetChrSubChip(0x17, 2)
    Sleep(300)

    ChrTalk(    #382
        0x17,
        (
            "#1035F#5P要把它们用在\x01",
            "恢复各地的通信设置上……\x02\x03",

            "#1040F是这样没有错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x12,
        "#1061F#2P答对⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x16,
        "#1006F#5P是啊，的确如此……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    Sleep(500)

    ChrTalk(    #385
        0xC,
        (
            "#176F#5P对军队来说，导力枪和飞船\x01",
            "无法使用纵然是相当致命的……\x02\x03",

            "#178F但司令部与各部队之间\x01",
            "联系中断的后果则更为严重。\x02\x03",

            "特别是王城、哈肯大门、\x01",
            "雷斯顿要塞之间的联络\x01",
            "必须要尽快恢复才行。\x02",
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

    ChrTalk(    #386
        0x8,
        (
            "#026F#6P协会也是一样……\x02\x03",

            "#020F如果支部之间不能够取得联系，\x01",
            "那么无论发生什么都无法采取应对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x13,
        "#104F#5P嗯，看来大家都没有异议。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(300)

    ChrTalk(    #388
        0x13,
        (
            "#100F#6P那么尤莉亚上尉。\x02\x03",

            "请把这１０个『零力场发生器』\x01",
            "交给王国军吧。\x02\x03",

            "#101F只要有这些的话，埃尔赛尤号、\x01",
            "王都、雷斯顿要塞、哈肯大门，\x01",
            "以及各地关所都能保护到了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 400)
    Sleep(500)

    ChrTalk(    #389
        0xC,
        (
            "#171F#5P……不胜感激。\x02\x03",

            "我会马上派传令兵\x01",
            "将它们安排送往各地。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x13, 0)
    Sleep(75)
    SetChrSubChip(0x13, 2)
    Sleep(300)

    ChrTalk(    #390
        0x13,
        (
            "#100F#5P接下来，交给游击士协会\x01",
            "６个『零力场发生器』。\x02\x03",

            "应该能够恢复\x01",
            "各地协会的通讯器才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x16,
        "#1006F#6P嗯……明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x17,
        "#1040F#6P一定保证安全送达。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_8F1E end

    def Function_26_9E32(): pass

    label("Function_26_9E32")

    EventBegin(0x0)
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

    ChrTalk(    #393
        0x13,
        (
            "#104F#2P──埃尔赛尤号的损伤\x01",
            "并不算特别严重。\x02\x03",

            "导力引擎几乎没有受到任何损害，\x01",
            "反重力产生机关也只有轻微损伤。\x02\x03",

            "#102F可是，包括稳定装置在内\x01",
            "的小型导力系统出了些问题。\x02\x03",

            "在这种状态下\x01",
            "是无法正常浮上空中的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xC,
        "#178F#5P是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x18,
        (
            "#272F#2P总之现在只有调集人手\x01",
            "赶紧展开修理作业了。\x02\x03",

            "#277F在下虽然驽钝，\x01",
            "但也请允许我献上微薄之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xC,
        "#176F#5P……不胜感激。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x9,
        (
            "#035F#2P就算埃尔赛尤号的问题可以解决，\x01",
            "目前最大的问题还是存在于\x01",
            "这个都市某处的『辉之环』。\x02\x03",

            "#030F看来『结社』似乎\x01",
            "正在一步步地进行准备。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 1)
    Sleep(200)

    ChrTalk(    #398
        0xA,
        (
            "#1163F#5P是啊……\x02\x03",

            "如果让『辉之环』落在他们手中\x01",
            "无法想象事态会演变成什么样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x8,
        (
            "#025F#6P嗯，无论如何\x01",
            "都不会有什么好事情吧。\x02\x03",

            "#022F我们只有从迄今为止发生的事来判断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x10,
        (
            "#555F#6P哎……没错。\x02\x03",

            "看来马上采取\x01",
            "行动会比较妥当吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xB,
        (
            "#074F#6P但如果莽撞行动的话，\x01",
            "反而有可能会导致更加混乱的结果。\x02\x03",

            "#070F还是应该\x01",
            "组织探索队才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x101,
        (
            "#1015F#6P的确……\x02\x03",

            "#1007F如果不先确保移动路线，\x01",
            "接下来也无法寻找『辉之环』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x102,
        "#1043F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #404
        0x101,
        "#1004F#5P怎么了，约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x102,
        (
            "#1035F#6P不……没什么。\x02\x03",

            "#1042F──总而言之，我认为\x01",
            "探索队也需要有后备人员。\x02\x03",

            "返回埃尔赛尤号之后\x01",
            "如果能马上轮替的话，\x01",
            "那就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xC,
        (
            "#176F#5P是啊……\x02\x03",

            "#178F我们尽快来商量一下\x01",
            "各自的任务分工吧。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A67B")
    Call(0, 39)

    label("loc_A67B")

    SetChrName("")

    AnonymousTalk(    #407
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

    ChrTalk(    #408
        0xC,
        (
            "#170F#5P那么请艾丝蒂尔等\x01",
            "四名成员负责进行搜索的任务。\x02\x03",

            "由于不知道会发生什么事，\x01",
            "请各位千万不要勉强自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x101,
        "#1006F#6P没问题，别担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x102,
        (
            "#1040F#6P我们会优先确保\x01",
            "移动路线的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xC,
        "#176F#5P拜托你们了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #412
        0xC,
        (
            "#178F#5P剩下的人在此待命\x01",
            "请你们一起帮忙修理船体。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A8EF")

    ChrTalk(    #413
        0x11,
        "#560F#2P是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A946")

    label("loc_A8EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A91F")

    ChrTalk(    #414
        0x10,
        "#051F#6P嗯，放心交给我吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A946")

    label("loc_A91F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A946")

    ChrTalk(    #415
        0xB,
        "#070F#6P啊，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_A946")


    ChrTalk(    #416
        0x13,
        (
            "#103F#2P……好了，那我们走了。\x01",
            "顺便告诉大家一个好消息。\x02\x03",

            "#100F在浮游都市上面似乎\x01",
            "并不会出现『导力停止现象』。\x02\x03",

            "即使离开了埃尔赛尤号之后，\x01",
            "战术导力器也应该可以使用的。\x02",
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

    ChrTalk(    #417
        0x101,
        "#1004F#5P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x11,
        "#064F#4P你、你是怎么知道的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x13,
        (
            "#104F#2P其实，那个『零力场发生器』\x01",
            "已经在迫降的冲击当中坏掉了……\x02\x03",

            "#102F尽管如此，我们仍然可以\x01",
            "让舰内的装置正常运作。\x02\x03",

            "看来凯文神父的推测\x01",
            "大概是正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x12,
        (
            "#1065F#4P『环』具有着排除\x01",
            "外界异物的功能……\x02\x03",

            "#1060F也就是只要在都市里，\x01",
            "导力器就不会被\x01",
            "判定为异物了对吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(300)

    ChrTalk(    #421
        0x13,
        "#101F#5P嗯，就是这个样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x101,
        (
            "#1007F#5P呼～太好了。\x02\x03",

            "#1008F毕竟在搜索的时候\x01",
            "没有魔法的话会很困难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x102,
        (
            "#1040F#5P那么，舰内的\x01",
            "工房设施也可以使用吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x13, 0)
    Sleep(200)

    ChrTalk(    #424
        0x13,
        (
            "#100F#2P嗯，那个也没问题。\x02\x03",

            "#101F导力器还可进行后续的改造，\x01",
            "有空的话就过来一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1006F#5P明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        "#1040F#5P明白了。\x02",
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
    OP_43(0x13, 0x1, 0x0, 0x1B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF51")
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x1B)

    label("loc_AF51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF6A")
    Sleep(800)
    OP_43(0x10, 0x1, 0x0, 0x1B)

    label("loc_AF6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF83")
    Sleep(800)
    OP_43(0x8, 0x1, 0x0, 0x1B)

    label("loc_AF83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF9C")
    Sleep(800)
    OP_43(0xB, 0x1, 0x0, 0x1B)

    label("loc_AF9C")

    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0x1C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFC1")
    Sleep(800)
    OP_43(0xA, 0x1, 0x0, 0x1C)

    label("loc_AFC1")

    Sleep(800)
    OP_43(0x18, 0x1, 0x0, 0x1C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFE6")
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x1C)

    label("loc_AFE6")

    Sleep(2000)

    def lambda_AFF1():
        OP_6D(1700, 0, 810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFF1)

    def lambda_B009():
        OP_6B(2690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B009)
    OP_43(0x101, 0x1, 0x0, 0x1D)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B077")
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x20)
    Sleep(1500)
    OP_71(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    Jump("loc_B0B7")

    label("loc_B077")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0B7")
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x20)
    Sleep(1500)
    OP_71(0x6, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)

    label("loc_B0B7")

    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #427
        0x101,
        (
            "#1015F那么……\x02\x03",

            "我们现在赶紧到\x01",
            "舰外展开搜索活动吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B12D")

    ChrTalk(    #428
        0x105,
        "#1382F#5P嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B203")

    label("loc_B12D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B156")

    ChrTalk(    #429
        0x103,
        "#020F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B203")

    label("loc_B156")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B185")

    ChrTalk(    #430
        0x104,
        "#035F#5P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B203")

    label("loc_B185")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1AE")

    ChrTalk(    #431
        0x106,
        "#051F#5P啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B203")

    label("loc_B1AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1D7")

    ChrTalk(    #432
        0x107,
        "#560F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B203")

    label("loc_B1D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B203")

    ChrTalk(    #433
        0x108,
        "#070F#5P啊，要出发了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_B203")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #434
        0x102,
        (
            "#1035F#5P……抱歉，艾丝蒂尔。\x02\x03",

            "#1040F我许多装备都用完了，\x01",
            "必须先去进行补充才行。\x02\x03",

            "可以稍微等我一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #435
        0x101,
        "#1004F#6P哦，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x109,
        (
            "#1062F#6P嗯嗯，既然如此\x01",
            "我也得准备一下，一起去吧。\x02\x03",

            "#1061F艾丝蒂尔你们就在\x01",
            "那边的休息室等我们好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(300)

    ChrTalk(    #437
        0x101,
        "#1006F这样啊……我明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B366")

    ChrTalk(    #438
        0x105,
        "#1168F#5P那我们在这里等你们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B463")

    label("loc_B366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B39B")

    ChrTalk(    #439
        0x103,
        "#021F#5P那么我们就在这里等着。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B463")

    label("loc_B39B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3D5")

    ChrTalk(    #440
        0x104,
        (
            "#035F#5P呵……\x01",
            "那么就等你们回来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B463")

    label("loc_B3D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B404")

    ChrTalk(    #441
        0x106,
        "#051F#5P赶快弄好回来啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B463")

    label("loc_B404")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B437")

    ChrTalk(    #442
        0x107,
        "#061F#5P那么，等你们回来哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B463")

    label("loc_B437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B463")

    ChrTalk(    #443
        0x108,
        "#071F#5P那么就等你们啰。\x02",
    )

    CloseMessageWindow()

    label("loc_B463")

    OP_43(0x101, 0x1, 0x0, 0x22)

    def lambda_B470():

        label("loc_B470")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_B470")

    QueueWorkItem2(0x102, 1, lambda_B470)
    Sleep(100)

    def lambda_B486():

        label("loc_B486")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_B486")

    QueueWorkItem2(0x109, 1, lambda_B486)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4B2")
    OP_43(0xF9, 0x1, 0x0, 0x24)
    WaitChrThread(0xF9, 0x1)
    Jump("loc_B4CB")

    label("loc_B4B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4CB")
    OP_43(0xF8, 0x1, 0x0, 0x24)
    WaitChrThread(0xF8, 0x1)

    label("loc_B4CB")

    Sleep(1500)
    OP_44(0x102, 0x1)
    OP_44(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #444
        0x109,
        (
            "#1067F#5P真是的……\x01",
            "你可真是罪孽深重呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 400)
    Sleep(300)

    ChrTalk(    #445
        0x102,
        "#1043F……对不起。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 400)
    Sleep(300)

    ChrTalk(    #446
        0x109,
        (
            "#1065F#6P要道歉的话\x01",
            "就去对艾丝蒂尔说吧。\x02\x03",

            "#1063F……这样真的可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        (
            "#1035F我已经决定了。\x02\x03",

            "#1040F凯文神父……\x01",
            "这件事情就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x109,
        (
            "#1068F#6P真是的，不管你了……\x02\x03",

            "#1060F好了，时间所剩不多，\x01",
            "赶快来医务室吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBD3")

    label("loc_B61B")

    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x20)
    Sleep(1500)
    OP_71(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #449
        0x101,
        (
            "#1015F那么……\x02\x03",

            "我们现在赶紧到\x01",
            "舰外展开搜索活动吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6C1")

    ChrTalk(    #450
        0x105,
        "#1382F嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B78C")

    label("loc_B6C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6E7")

    ChrTalk(    #451
        0x103,
        "#020F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B78C")

    label("loc_B6E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B713")

    ChrTalk(    #452
        0x104,
        "#035F呼，就这么办吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B78C")

    label("loc_B713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B73B")

    ChrTalk(    #453
        0x106,
        "#051F啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B78C")

    label("loc_B73B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B763")

    ChrTalk(    #454
        0x107,
        "#560F嗯，是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B78C")

    label("loc_B763")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B78C")

    ChrTalk(    #455
        0x108,
        "#070F啊，就这样做吧。\x02",
    )

    CloseMessageWindow()

    label("loc_B78C")

    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #456
        0x102,
        (
            "#1035F#5P……真对不起，艾丝蒂尔。\x02\x03",

            "#1040F我许多装备都用完了，\x01",
            "必须先去进行补充才行。\x02\x03",

            "可以稍微等我一下吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #457
        0x101,
        (
            "#1004F#6P哦，这样啊。\x02\x03",

            "#1015F既然如此\x01",
            "我也跟你一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x102,
        (
            "#1049F#5P不，那倒不必。\x02\x03",

            "#1040F大约过３０分钟就回来,\x01",
            "你们可以在休息室等我回来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x101,
        "#1006F#6P这样啊……我明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8F5")

    ChrTalk(    #460
        0x108,
        "#071F那我们在这儿等着。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E2")

    label("loc_B8F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B923")

    ChrTalk(    #461
        0x107,
        "#061F那么，等你回来哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E2")

    label("loc_B923")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B94F")

    ChrTalk(    #462
        0x106,
        "#051F赶快弄好回来啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E2")

    label("loc_B94F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B986")

    ChrTalk(    #463
        0x104,
        (
            "#035F呼……\x01",
            "那么就等你们回来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E2")

    label("loc_B986")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9B6")

    ChrTalk(    #464
        0x103,
        "#021F那么我们在这里等着。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E2")

    label("loc_B9B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9E2")

    ChrTalk(    #465
        0x105,
        "#1168F那我们在这里等你。\x02",
    )

    CloseMessageWindow()

    label("loc_B9E2")

    OP_43(0x101, 0x1, 0x0, 0x22)

    def lambda_B9EF():

        label("loc_B9EF")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_B9EF")

    QueueWorkItem2(0x102, 1, lambda_B9EF)
    Sleep(1000)
    OP_43(0xF8, 0x1, 0x0, 0x23)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x24)
    WaitChrThread(0xF9, 0x1)
    Sleep(1500)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 1020, 0, 5300, 180)
    OP_72(0x7, 0x10)
    OP_6F(0x7, 0)
    OP_70(0x7, 0xF)
    OP_73(0x7)
    Sleep(500)

    NpcTalk(    #466
        0x12,
        "青年的声音",
        (
            "#4P哎呀呀……\x01",
            "你可真是罪孽深重呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA85():
        OP_6D(2490, 0, 1310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA85)
    OP_43(0x12, 0x1, 0x0, 0x21)

    def lambda_BAA4():

        label("loc_BAA4")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_BAA4")

    QueueWorkItem2(0x102, 1, lambda_BAA4)
    Sleep(1500)
    OP_72(0x7, 0x10)
    OP_6F(0x7, 15)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0x1)

    ChrTalk(    #467
        0x102,
        "#1043F#6P……对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x12,
        (
            "#1065F#5P要道歉的话\x01",
            "就去对艾丝蒂尔说吧。\x02\x03",

            "#1063F……这样真的可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x102,
        (
            "#1035F#6P我已经决定了。\x02\x03",

            "#1040F凯文神父……\x01",
            "这件事情就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x12,
        (
            "#1068F#5P真是的，不管你了……\x02\x03",

            "#1060F好了，时间所剩不多，\x01",
            "赶快来医务室吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBD3")

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
        (2, "loc_BC9A"),
        (3, "loc_BCA7"),
        (4, "loc_BCB4"),
        (5, "loc_BCC1"),
        (6, "loc_BCCE"),
        (7, "loc_BCDB"),
        (SWITCH_DEFAULT, "loc_BCE8"),
    )


    label("loc_BC9A")

    OP_D2(0x70023, 0x7002B, 0x14)
    Jump("loc_BCE8")

    label("loc_BCA7")

    OP_D2(0x70033, 0x7003B, 0x14)
    Jump("loc_BCE8")

    label("loc_BCB4")

    OP_D2(0x27039B, 0x27039F, 0x14)
    Jump("loc_BCE8")

    label("loc_BCC1")

    OP_D2(0x70053, 0x7005B, 0x14)
    Jump("loc_BCE8")

    label("loc_BCCE")

    OP_D2(0x70063, 0x7006B, 0x14)
    Jump("loc_BCE8")

    label("loc_BCDB")

    OP_D2(0x70073, 0x7007B, 0x14)
    Jump("loc_BCE8")

    label("loc_BCE8")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_BD09"),
        (3, "loc_BD16"),
        (4, "loc_BD23"),
        (5, "loc_BD30"),
        (6, "loc_BD3D"),
        (7, "loc_BD4A"),
        (SWITCH_DEFAULT, "loc_BD57"),
    )


    label("loc_BD09")

    OP_D2(0x70023, 0x7002B, 0x15)
    Jump("loc_BD57")

    label("loc_BD16")

    OP_D2(0x70033, 0x7003B, 0x15)
    Jump("loc_BD57")

    label("loc_BD23")

    OP_D2(0x27039B, 0x27039F, 0x15)
    Jump("loc_BD57")

    label("loc_BD30")

    OP_D2(0x70053, 0x7005B, 0x15)
    Jump("loc_BD57")

    label("loc_BD3D")

    OP_D2(0x70063, 0x7006B, 0x15)
    Jump("loc_BD57")

    label("loc_BD4A")

    OP_D2(0x70073, 0x7007B, 0x15)
    Jump("loc_BD57")

    label("loc_BD57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD95")
    SetChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF9, 21)
    SetChrPos(0xF9, -2400, 200, -47940, 180)
    ClearChrFlags(0xF9, 0x80)
    Jump("loc_BDC2")

    label("loc_BD95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC2")
    SetChrFlags(0xF8, 0x4)
    SetChrChipByIndex(0xF8, 20)
    SetChrPos(0xF8, -2400, 200, -47940, 180)
    ClearChrFlags(0xF8, 0x80)

    label("loc_BDC2")

    Jump("loc_BE05")

    label("loc_BDC5")

    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrChipByIndex(0xF8, 20)
    SetChrChipByIndex(0xF9, 21)
    SetChrPos(0xF8, -450, 200, -50200, 0)
    SetChrPos(0xF9, -2400, 200, -47940, 180)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)

    label("loc_BE05")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 19)
    SetChrPos(0x101, -2400, 200, -50200, 0)
    ClearChrFlags(0x101, 0x80)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C059")
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6B")
    SetChrSubChip(0xF9, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Jump("loc_BE87")

    label("loc_BE6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE87")
    SetChrSubChip(0xF8, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)

    label("loc_BE87")

    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x25)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x26)

    def lambda_BEA5():
        OP_6D(-800, 200, -47820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA5)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #471
        0x101,
        "#1004F#6P啊，约修亚、凯文神父。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x102,
        "#1040F#5P……久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x109,
        (
            "#1061F#5P啊，真不好意思。\x01",
            "回来得晚了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        (
            "#1015F#6P这个倒无所谓……\x02\x03",

            "……只是你们两个，\x01",
            "怎么都看上去满脸倦容啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x109,
        "#1064F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x102,
        (
            "#1035F#5P细部装备的补充\x01",
            "耗费了相当多的工夫。\x02\x03",

            "#1040F没关系，不妨碍搜索活动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x109,
        (
            "#1066F#5P对、对对对！\x01",
            "肯定会相当有帮助的～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x101,
        (
            "#1025F#6P那我就放心了……\x02\x03",

            "#1006F好～的。\x01",
            "那么就出发吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1CA")

    label("loc_C059")

    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xF9, 1)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x25)

    def lambda_C084():
        OP_6D(-540, 0, -48040, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C084)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #479
        0x101,
        "#1004F#6P啊，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x102,
        (
            "#1040F#5P……久等了。\x01",
            "似乎稍微有点迟到了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1015F#6P这个倒无所谓……\x02\x03",

            "……不过约修亚\x01",
            "怎么都看上去满脸倦容啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x102,
        (
            "#1035F#5P细部装备的补充\x01",
            "耗费了相当多的工夫。\x02\x03",

            "#1040F不要紧。\x01",
            "不会妨碍搜索活动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x101,
        (
            "#1025F#6P那我就放心了……\x02\x03",

            "#1006F好～的。\x01",
            "那么就出发吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1CA")

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

    # Function_26_9E32 end

    def Function_27_C2E1(): pass

    label("Function_27_C2E1")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3FC, 0x0, 0x866, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1414, 0x0, 0x866, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1414, 0xFFFFF862, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_C2E1 end

    def Function_28_C344(): pass

    label("Function_28_C344")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3CA, 0x0, 0x730, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC90, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF420, 0x0, 0x46, 0x7D0, 0x0)

    def lambda_C39C():
        OP_8E(0xFE, 0xFFFFF3DA, 0x960, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C39C)
    Sleep(1800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_C344 end

    def Function_29_C3C7(): pass

    label("Function_29_C3C7")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3A2, 0x0, 0xFFFFFC72, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_29_C3C7 end

    def Function_30_C3F9(): pass

    label("Function_30_C3F9")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x492, 0x0, 0x5C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x820, 0x0, 0x154, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_30_C3F9 end

    def Function_31_C43F(): pass

    label("Function_31_C43F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x4A6, 0x0, 0x8E8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0xD2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_C43F end

    def Function_32_C485(): pass

    label("Function_32_C485")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x3FC, 0x0, 0x62C, 0x7D0, 0x0)
    Return()

    # Function_32_C485 end

    def Function_33_C4B0(): pass

    label("Function_33_C4B0")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1020, 0, 5300, 180)
    OP_8E(0xFE, 0x5E6, 0x0, 0x7B2, 0x7D0, 0x0)
    Return()

    # Function_33_C4B0 end

    def Function_34_C4DB(): pass

    label("Function_34_C4DB")

    OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF9CA, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_C4FF():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C4FF)
    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_C4DB end

    def Function_35_C52A(): pass

    label("Function_35_C52A")

    OP_8E(0xFE, 0x3DE, 0x32, 0xFFFFFB32, 0x7D0, 0x0)

    def lambda_C544():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C544)
    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_C52A end

    def Function_36_C56F(): pass

    label("Function_36_C56F")


    def lambda_C575():
        OP_8E(0xFE, 0x3FC, 0x0, 0xFFFFF06A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C575)
    Sleep(2000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    OP_22(0x6D, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_C56F end

    def Function_37_C5A5(): pass

    label("Function_37_C5A5")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 490, 0, -39390, 180)
    OP_8E(0xFE, 0x186, 0x0, 0xFFFF51A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0xFFFF48CC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_37_C5A5 end

    def Function_38_C5EB(): pass

    label("Function_38_C5EB")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 490, 0, -39390, 180)
    OP_8E(0xFE, 0x186, 0x0, 0xFFFF51A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x17C, 0x0, 0xFFFF4700, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_38_C5EB end

    def Function_39_C631(): pass

    label("Function_39_C631")

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
        (0, "loc_C6AB"),
        (1, "loc_C6B1"),
        (SWITCH_DEFAULT, "loc_C6B7"),
    )


    label("loc_C6AB")

    OP_A2(0x1200)
    Jump("loc_C6B7")

    label("loc_C6B1")

    OP_A2(0x1201)
    Jump("loc_C6B7")

    label("loc_C6B7")

    Return()

    # Function_39_C631 end

    def Function_40_C6B8(): pass

    label("Function_40_C6B8")

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

    # Function_40_C6B8 end

    def Function_41_C747(): pass

    label("Function_41_C747")

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

    # Function_41_C747 end

    def Function_42_C7D4(): pass

    label("Function_42_C7D4")

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

    # Function_42_C7D4 end

    def Function_43_C865(): pass

    label("Function_43_C865")

    OP_A2(0xF)
    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_43_C865 end

    def Function_44_C87F(): pass

    label("Function_44_C87F")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x3E)
    Return()

    # Function_44_C87F end

    SaveToFile()

Try(main)
