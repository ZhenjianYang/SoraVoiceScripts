from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1103   ._SN',
        MapName             = 'Bose',
        Location            = 'C1103.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        '剑帝莱维',                             # 9
        '阿加特',                               # 10
        '摩尔根将军',                           # 11
        '王国军士官',                           # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '残像',                                 # 23
        '折断的刀锋',                           # 24
        '古代龙',                               # 25
        '龙',                                   # 26
        '警备艇',                               # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
        ' ',                                    # 32
        ' ',                                    # 33
        ' ',                                    # 34
        ' ',                                    # 35
        ' ',                                    # 36
        ' ',                                    # 37
        ' ',                                    # 38
        ' ',                                    # 39
        ' ',                                    # 40
        ' ',                                    # 41
        ' ',                                    # 42
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT06/CH20053 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT07/CH01600 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT27/CH04540 ._CH',             # 05
        'ED6_DT27/CH04542 ._CH',             # 06
        'ED6_DT27/CH04548 ._CH',             # 07
        'ED6_DT27/CH04546 ._CH',             # 08
        'ED6_DT07/CH00150 ._CH',             # 09
        'ED6_DT07/CH00151 ._CH',             # 0A
        'ED6_DT07/CH00152 ._CH',             # 0B
        'ED6_DT07/CH00153 ._CH',             # 0C
        'ED6_DT07/CH00154 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT26/CH20343 ._CH',             # 0F
        'ED6_DT26/CH20345 ._CH',             # 10
        'ED6_DT07/CH00161 ._CH',             # 11
        'ED6_DT26/CH20346 ._CH',             # 12
        'ED6_DT07/CH00321 ._CH',             # 13
        'ED6_DT07/CH00326 ._CH',             # 14
        'ED6_DT26/CH20362 ._CH',             # 15
        'ED6_DT26/CH20340 ._CH',             # 16
        'ED6_DT07/CH00158 ._CH',             # 17
        'ED6_DT07/CH00159 ._CH',             # 18
        'ED6_DT26/CH20207 ._CH',             # 19
        'ED6_DT26/CH20364 ._CH',             # 1A
        'ED6_DT26/CH20363 ._CH',             # 1B
        'ED6_DT26/CH20243 ._CH',             # 1C
        'ED6_DT26/CH20347 ._CH',             # 1D
        'ED6_DT26/CH20348 ._CH',             # 1E
        'ED6_DT27/CH04541 ._CH',             # 1F
        'ED6_DT27/CH04547 ._CH',             # 20
        'ED6_DT27/CH04545 ._CH',             # 21
        'ED6_DT06/CH20138 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT06/CH20053P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT07/CH01600P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT27/CH04540P._CP',             # 05
        'ED6_DT27/CH04542P._CP',             # 06
        'ED6_DT27/CH04548P._CP',             # 07
        'ED6_DT27/CH04546P._CP',             # 08
        'ED6_DT07/CH00150P._CP',             # 09
        'ED6_DT07/CH00151P._CP',             # 0A
        'ED6_DT07/CH00152P._CP',             # 0B
        'ED6_DT07/CH00153P._CP',             # 0C
        'ED6_DT07/CH00154P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT26/CH20343P._CP',             # 0F
        'ED6_DT26/CH20345P._CP',             # 10
        'ED6_DT07/CH00161P._CP',             # 11
        'ED6_DT26/CH20346P._CP',             # 12
        'ED6_DT07/CH00321P._CP',             # 13
        'ED6_DT07/CH00326P._CP',             # 14
        'ED6_DT26/CH20362P._CP',             # 15
        'ED6_DT26/CH20340P._CP',             # 16
        'ED6_DT07/CH00158P._CP',             # 17
        'ED6_DT07/CH00159P._CP',             # 18
        'ED6_DT26/CH20207P._CP',             # 19
        'ED6_DT26/CH20364P._CP',             # 1A
        'ED6_DT26/CH20363P._CP',             # 1B
        'ED6_DT26/CH20243P._CP',             # 1C
        'ED6_DT26/CH20347P._CP',             # 1D
        'ED6_DT26/CH20348P._CP',             # 1E
        'ED6_DT27/CH04541P._CP',             # 1F
        'ED6_DT27/CH04547P._CP',             # 20
        'ED6_DT27/CH04545P._CP',             # 21
        'ED6_DT06/CH20138P._CP',             # 22
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_602",          # 00, 0
        "Function_1_66C",          # 01, 1
        "Function_2_67A",          # 02, 2
        "Function_3_C56",          # 03, 3
        "Function_4_CDF",          # 04, 4
        "Function_5_CF4",          # 05, 5
        "Function_6_D17",          # 06, 6
        "Function_7_159C",         # 07, 7
        "Function_8_161D",         # 08, 8
        "Function_9_2592",         # 09, 9
        "Function_10_25A6",        # 0A, 10
        "Function_11_299F",        # 0B, 11
        "Function_12_29CF",        # 0C, 12
        "Function_13_2E23",        # 0D, 13
        "Function_14_5335",        # 0E, 14
        "Function_15_534C",        # 0F, 15
        "Function_16_5393",        # 10, 16
        "Function_17_53B7",        # 11, 17
        "Function_18_53E5",        # 12, 18
        "Function_19_5413",        # 13, 19
        "Function_20_5441",        # 14, 20
        "Function_21_54F8",        # 15, 21
        "Function_22_55AE",        # 16, 22
        "Function_23_55CA",        # 17, 23
        "Function_24_55E6",        # 18, 24
        "Function_25_5602",        # 19, 25
        "Function_26_5639",        # 1A, 26
        "Function_27_5684",        # 1B, 27
        "Function_28_56CF",        # 1C, 28
        "Function_29_571A",        # 1D, 29
        "Function_30_5765",        # 1E, 30
        "Function_31_57B0",        # 1F, 31
        "Function_32_57FB",        # 20, 32
        "Function_33_5846",        # 21, 33
        "Function_34_5891",        # 22, 34
        "Function_35_58DC",        # 23, 35
        "Function_36_5927",        # 24, 36
        "Function_37_59D7",        # 25, 37
        "Function_38_5D86",        # 26, 38
        "Function_39_6132",        # 27, 39
        "Function_40_6881",        # 28, 40
        "Function_41_68F0",        # 29, 41
        "Function_42_7A54",        # 2A, 42
        "Function_43_7AB0",        # 2B, 43
        "Function_44_7B08",        # 2C, 44
        "Function_45_7B1D",        # 2D, 45
        "Function_46_7B39",        # 2E, 46
        "Function_47_7B55",        # 2F, 47
        "Function_48_7B71",        # 30, 48
        "Function_49_7C6A",        # 31, 49
        "Function_50_7CAE",        # 32, 50
        "Function_51_7CF3",        # 33, 51
        "Function_52_7D87",        # 34, 52
    )


    def Function_0_602(): pass

    label("Function_0_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_621")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 41)
    Jump("loc_66B")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_639"),
        (SWITCH_DEFAULT, "loc_64E"),
    )


    label("loc_639")

    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_64E")

    label("loc_64E")

    Jump("loc_66B")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_66B")

    Return()

    # Function_0_602 end

    def Function_1_66C(): pass

    label("Function_1_66C")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_10(0x0, 0x0)
    Return()

    # Function_1_66C end

    def Function_2_67A(): pass

    label("Function_2_67A")


    def lambda_680():
        OP_6D(-2940, 0, 5940, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_680)

    def lambda_698():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_698)

    def lambda_6A8():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A8)

    def lambda_6B8():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6B8)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 10)

    def lambda_6D2():
        OP_8E(0xFE, 0xFFFFE386, 0x0, 0x203A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D2)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)

    def lambda_6FC():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6FC)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_711():
        OP_96(0xFE, 0xFFFFF5E2, 0x0, 0x14A0, 0x578, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_711)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_73E():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_73E)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)

    def lambda_7A3():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A3)
    OP_96(0x9, 0xFFFFF268, 0x0, 0x15CC, 0xC8, 0x1388)
    WaitChrThread(0x9, 0x1)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_7D4():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7D4)

    def lambda_7E4():
        OP_96(0xFE, 0xFFFFF8EE, 0x0, 0x13E2, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7E4)
    Sleep(100)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_80F():
        OP_96(0x8, 0x4F6, 0x0, 0x104A, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_80F)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x8, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 5)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_876():
        OP_99(0x8, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_876)

    def lambda_886():
        OP_96(0x8, 0xFFFFFFA6, 0x0, 0x1176, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_886)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_8F4():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_8F4)
    WaitChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 24)

    def lambda_927():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_927)
    Sleep(400)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_949():
        OP_96(0x8, 0x6E, 0x0, 0x164E, 0xC8, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_949)

    def lambda_967():
        OP_8C(0x8, 225, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_967)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)

    def lambda_99B():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_99B)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)
    WaitChrThread(0x9, 0x1)

    def lambda_9C4():
        OP_99(0x8, 0x0, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9C4)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_A24():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_A24)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 7)
    ClearChrFlags(0x9, 0x2)

    def lambda_A5C():
        OP_8C(0x9, 45, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A5C)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_A7E():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A7E)

    def lambda_A8E():
        OP_96(0x9, 0xFFFFFD58, 0x0, 0x14C8, 0xC8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A8E)
    Sleep(200)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_AC8():
        OP_96(0x8, 0x13BA, 0x0, 0xF96, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_AC8)
    Sleep(200)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)

    def lambda_AF5():
        OP_6D(4240, 0, 3920, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF5)

    def lambda_B0D():
        OP_6C(332000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B0D)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x9, 0xF5A, 0x0, 0x4D8, 0x1F4, 0x1770)
    OP_8C(0x9, 0, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    TurnDirection(0x8, 0x9, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    Sleep(300)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 10)

    def lambda_B90():
        OP_96(0xFE, 0x1194, 0x0, 0x83E, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B90)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_BB6():
        OP_96(0xFE, 0x12B6, 0x0, 0xBCC, 0x12C, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB6)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x8, 8)
    SetChrChipByIndex(0x9, 14)

    def lambda_C01():

        label("loc_C01")

        OP_9E(0xFE, 0x14, 0x0, 0xFA0, 0x9C4)
        OP_48()
        Jump("loc_C01")

    QueueWorkItem2(0x9, 3, lambda_C01)
    Sleep(100)

    def lambda_C23():

        label("loc_C23")

        OP_9E(0xFE, 0x14, 0x0, 0xFA0, 0x9C4)
        OP_48()
        Jump("loc_C23")

    QueueWorkItem2(0x8, 3, lambda_C23)
    Sleep(500)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Return()

    # Function_2_67A end

    def Function_3_C56(): pass

    label("Function_3_C56")

    SetChrChipByIndex(0x8, 33)
    SetChrSubChip(0x8, 1)

    def lambda_C66():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C66)

    def lambda_C80():
        OP_96(0xFE, 0x474, 0x0, 0x104, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C80)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_CB2():
        OP_96(0xFE, 0xF28, 0x0, 0xFFFFFC54, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CB2)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 6)
    Return()

    # Function_3_C56 end

    def Function_4_CDF(): pass

    label("Function_4_CDF")

    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_4_CDF end

    def Function_5_CF4(): pass

    label("Function_5_CF4")

    WaitChrThread(0x9, 0x1)
    Sleep(400)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_D0E():
        OP_8C(0xFE, 110, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_D0E)
    Return()

    # Function_5_CF4 end

    def Function_6_D17(): pass

    label("Function_6_D17")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x20)

    def lambda_D2C():
        OP_6D(-1800, 0, 6230, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D2C)

    def lambda_D44():
        OP_67(0, 4450, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D44)

    def lambda_D5C():
        OP_6B(2029, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D5C)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_D7B():
        OP_8E(0xFE, 0xFFFFE642, 0x0, 0x1FD6, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D7B)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_DAF():
        OP_96(0xFE, 0xFFFFF7FE, 0x0, 0x163A, 0x578, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DAF)
    Sleep(200)

    def lambda_DD2():
        OP_99(0xFE, 0x3, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DD2)
    Sleep(100)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 332, 0)
    OP_7D(0x0, 0x8, 0x32, 0xC8)

    def lambda_E00():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x8C, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E00)
    Sleep(150)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -380, -1000, 4830, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 20, 0)
    Sleep(200)

    def lambda_E93():
        OP_6D(370, 0, 2040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E93)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 4)
    OP_8C(0x9, 200, 0)

    def lambda_EBC():
        OP_99(0xFE, 0x4, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EBC)

    def lambda_ECC():
        OP_96(0xFE, 0xFFFFFB14, 0x0, 0x5A0, 0xC8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ECC)
    OP_43(0x9, 0x0, 0x0, 0x5)
    Sleep(200)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_F00():
        OP_8C(0xFE, 330, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F00)

    def lambda_F0E():
        OP_96(0xFE, 0x5D2, 0x0, 0xFFFFF6C8, 0x1F4, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F0E)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_F40():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_F40)

    def lambda_F4E():
        OP_96(0xFE, 0x1108, 0x0, 0xC8, 0x1F4, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F4E)
    WaitChrThread(0x8, 0x1)

    def lambda_F71():
        OP_6D(-2540, 0, 3240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F71)

    def lambda_F89():
        OP_6B(1930, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F89)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 3)

    def lambda_FB0():
        OP_96(0xFE, 0x64, 0x0, 0x370, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FB0)
    Sleep(150)

    def lambda_FD3():
        OP_99(0xFE, 0x3, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FD3)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x9, 1000, 500, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x0)
    OP_44(0x9, 0x3)
    ClearChrFlags(0x9, 0x800)
    OP_8C(0x9, 110, 0)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)

    def lambda_1051():
        OP_8F(0xFE, 0xFFFFF380, 0x0, 0x816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1051)

    def lambda_106C():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_106C)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    Sleep(100)

    def lambda_109A():
        OP_6D(-4210, 0, 3570, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_109A)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 2)

    def lambda_10BC():
        OP_96(0xFE, 0xFFFFECC8, 0x0, 0xA64, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10BC)

    def lambda_10DA():
        OP_8F(0xFE, 0xFFFFF8F8, 0x0, 0x668, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DA)
    Sleep(100)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 1)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 3)
    Sleep(100)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 10)

    def lambda_112C():
        OP_8F(0xFE, 0xFFFFF196, 0x0, 0x8F2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_112C)
    Sleep(100)

    def lambda_114C():
        OP_99(0xFE, 0xA, 0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_114C)
    Sleep(100)

    def lambda_1161():
        OP_6D(-270, 0, 2070, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1161)

    def lambda_1179():
        OP_6B(2029, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1179)
    OP_23(0xD6)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x8, -1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x8, 0x0, 0x0, 0x3)
    Sleep(400)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_11F2():
        OP_8F(0xFE, 0xFFFFFC9A, 0x0, 0x46A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11F2)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1226():
        OP_96(0xFE, 0xCDA, 0x0, 0xFFFFFC4A, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1226)
    Sleep(200)

    def lambda_1249():
        OP_99(0xFE, 0x3, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1249)
    SetChrChipByIndex(0x8, 32)
    SetChrSubChip(0x8, 14)

    def lambda_1263():
        OP_8F(0xFE, 0x10AE, 0x0, 0x44C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1263)
    WaitChrThread(0x8, 0x1)
    Sleep(100)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, 4830, -1000, -1240, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    Sleep(100)

    def lambda_12DD():
        OP_6D(2850, 0, 920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12DD)

    def lambda_12F5():
        OP_6C(314000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F5)
    SetChrSubChip(0x8, 15)
    Sleep(30)
    OP_8C(0x8, 200, 0)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_1320():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1320)

    def lambda_1330():
        OP_8F(0xFE, 0xF8C, 0x0, 0x3C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1330)
    Sleep(150)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x9, 1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    ClearChrFlags(0x9, 0x800)
    OP_8C(0x9, 60, 0)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 9)

    def lambda_13B1():
        OP_8F(0xFE, 0x10C2, 0x0, 0xFFFFECFA, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13B1)

    def lambda_13CC():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13CC)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_13FA():
        OP_96(0xFE, 0x127A, 0x0, 0x88E, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13FA)
    OP_43(0x8, 0x0, 0x0, 0x4)

    def lambda_141F():
        OP_6D(4240, 0, 3920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141F)

    def lambda_1437():
        OP_6C(332000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1437)

    def lambda_1447():
        OP_6B(2130, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1447)

    def lambda_1457():
        OP_67(0, 5080, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1457)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 2)
    OP_8C(0x9, 20, 0)

    def lambda_1480():
        OP_96(0xFE, 0x1194, 0x0, 0x83E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1480)

    def lambda_149E():
        OP_99(0xFE, 0x2, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_149E)
    Sleep(350)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x8, 0, 800, -1000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x2)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 34)
    SetChrSubChip(0x9, 0)

    def lambda_151A():
        OP_8F(0xFE, 0x131A, 0x0, 0xC08, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_151A)

    def lambda_1535():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1535)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)

    def lambda_1558():
        OP_9E(0xFE, 0xF, 0xFFFFFFF8, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1558)

    def lambda_1572():
        OP_9E(0xFE, 0xF, 0xFFFFFFF8, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1572)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    Return()

    # Function_6_D17 end

    def Function_7_159C(): pass

    label("Function_7_159C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_161C")
    PlayEffect(0x3, 0xFF, 0xFF, 4760, 1100, 2720, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x3, 0xFF, 0xFF, 4700, 1200, 2700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_7_159C")

    label("loc_161C")

    Return()

    # Function_7_159C end

    def Function_8_161D(): pass

    label("Function_8_161D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17960, 0, -9210, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(59000, 0)
    OP_6E(602, 0)
    SetChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -460, 0, 4800, 21)
    ClearChrFlags(0x8, 0x80)
    OP_72(0x0, 0x4)
    OP_CF(0x19, 0x0, "Frame127_FireEmitter")
    OP_A1(0x18, 0x0)
    SetChrPos(0x18, 12660, 0, 13410, 232)
    SetChrFlags(0x18, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\\\mp015_00.eff")

    def lambda_1720():
        OP_6D(6450, 0, 10810, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1720)

    def lambda_1738():
        OP_67(0, 7880, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1738)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x1)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Fade(500)
    OP_6D(990, 3620, 6360, 0)
    OP_67(0, 5670, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(356000, 0)
    OP_6E(580, 0)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)

    ChrTalk(    #0
        0x8,
        "#121F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_B0(0x0, 0x1E)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    Fade(500)
    OP_6F(0x0, 290)
    OP_70(0x0, 0x12C)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 300)
    OP_70(0x0, 0x15E)
    OP_22(0x122, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x1E)
    OP_73(0x0)
    OP_B0(0x0, 0xF)

    def lambda_18DC():
        OP_6D(2140, 0, 8390, 3500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_18DC)

    def lambda_18F4():
        OP_67(0, 5940, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18F4)

    def lambda_190C():
        OP_6B(2290, 3500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_190C)
    Fade(500)
    OP_23(0x193)
    OP_6F(0x0, 350)
    OP_70(0x0, 0x1B3)
    OP_73(0x0)
    OP_43(0x19, 0x0, 0x0, 0x9)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #1
        0x8,
        "#124F好……这样就行了。\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x4, 0x0, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(750)

    ChrTalk(    #2
        0x8,
        (
            "#121F嗯，收集资料\x01",
            "还需要一些时间吗。\x02\x03",

            "真是的，把这么麻烦的工作\x01",
            "推给我。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -15470, 0, 11980, 90)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #3
        0x9,
        "青年的声音",
        "#4P……你说什么麻烦……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1A23():
        OP_6D(-6950, 0, 9120, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A23)

    def lambda_1A3B():
        OP_67(0, 5080, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A3B)

    def lambda_1A53():
        OP_6B(3020, 2500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1A53)

    def lambda_1A63():
        OP_6C(332000, 2500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1A63)

    def lambda_1A73():
        OP_6E(385, 2500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1A73)
    Sleep(500)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)

    def lambda_1A92():
        TurnDirection(0x8, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A92)
    OP_8E(0x9, 0xFFFFD1A2, 0x0, 0x2A44, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x8,
        "#120F#2P你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#051F#5P那把金色的剑……\x01",
            "果真是那时的红头盔队长吗。\x02\x03",

            "真好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#124F#2P等级为Ｃ，『重剑』\x01",
            "阿加特·科洛斯纳。\x02\x03",

            "#123F不，政变事件之后，\x01",
            "据说升级为B了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#053F#5P哼……\x01",
            "不愧是原情报部的人。\x02\x03",

            "#555F那个时候只会像老鼠一样\x01",
            "偷偷摸摸地行动……\x02\x03",

            "这次倒是搞得\x01",
            "相当华丽啊。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    OP_0D()
    Sleep(750)

    ChrTalk(    #8
        0x9,
        (
            "#057F#5P……这次我就不说逮捕\x01",
            "之类的场面话了。\x02\x03",

            "我要把你那张假正经的脸\x01",
            "打个稀巴烂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#124F#2P好有气势啊。\x02\x03",

            "#123F不过，那种程度的损害，\x01",
            "还不算华丽吧？\x02\x03",

            "和10年前……\x01",
            "你所看到的光景相比较来说。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x8,
        (
            "#123F#2P这个国家的游击士的经历\x01",
            "我都调查了一次。\x02\x03",

            "呵呵，你果然\x01",
            "和我有点相似嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(    #11
        0x9,
        (
            "#057F#5P…………………………………\x02\x03",

            "#053F呵呵……相似？\x02",
        )
    )

    OP_21()
    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x2B)
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 3)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #12
        0x9,
        (
            "#550F#5P#3S你这一无所知的混帐\x01",
            "还敢大放厥词！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    LoadEffect(0x3, "map\\\\mp009_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x18, 0x0, 0x0, 0x6)
    WaitChrThread(0x18, 0x0)

    ChrTalk(    #13
        0x8,
        (
            "#124F#2P……实力的差距\x01",
            "在上次交手时你就应该明白了。\x02\x03",

            "更何况这次还有龙的威胁。\x02\x03",

            "#120F你明知没有胜算，为何还要一个人追来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "#057F#6P我才不管什么胜算不胜算……\x02\x03",

            "#054F我只是看你不爽……\x01",
            "就这么简单！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#121F#2P哎呀呀……只有这种程度吗。\x02\x03",

            "这样的话，龙也派不上用场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#057F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    OP_44(0x8, 0x0)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 6)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_96(0x8, 0x15CC, 0x0, 0x16A8, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)

    def lambda_1FB9():
        OP_96(0xFE, 0x13BA, 0x0, 0xF96, 0xC8, 0x3A98)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1FB9)

    def lambda_1FD7():
        OP_99(0xFE, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1FD7)
    Sleep(100)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)

    def lambda_2046():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2046)

    def lambda_2060():
        OP_8F(0xFE, 0x1108, 0x0, 0x708, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2060)
    WaitChrThread(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 6)

    def lambda_208F():
        OP_99(0xFE, 0x0, 0x5, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_208F)
    Sleep(100)
    PlayEffect(0x3, 0x2, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0xBB8, 0x64)

    def lambda_20EF():
        OP_8F(0xFE, 0x1252, 0x0, 0xC26, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20EF)

    def lambda_210A():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_210A)

    def lambda_2124():
        OP_8F(0xFE, 0x100E, 0x0, 0x460, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2124)
    WaitChrThread(0x8, 0x2)
    OP_22(0x226, 0x0, 0x64)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 0)

    def lambda_2153():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2153)
    Sleep(100)
    PlayEffect(0x3, 0x3, 0x9, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)

    def lambda_21B3():
        OP_8F(0xFE, 0x1194, 0x0, 0x83E, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21B3)
    Sleep(100)

    def lambda_21D3():
        OP_6D(3100, 0, 170, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21D3)

    def lambda_21EB():
        OP_9E(0xFE, 0x1E, 0x0, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_21EB)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 12)
    SetChrSubChip(0x9, 0)

    def lambda_2214():
        OP_96(0x9, 0xC8A, 0x0, 0xFFFFF4CA, 0x1F4, 0x4650)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2214)
    Sleep(100)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 0)

    def lambda_2241():
        OP_96(0x9, 0xB68, 0x0, 0xFFFFF100, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2241)

    ChrTalk(    #17 op#A op#5
        0x9,
        "#056F#10A呜喔……\x05\x02",
    )

    Sleep(500)

    def lambda_227B():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_227B)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2299():
        OP_6B(2540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2299)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#121F虽然有相似的地方……\x01",
            "但我和你有决定性的不同。\x02\x03",

            "那就是挥剑的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "#057F什、什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#124F我之所以挥剑\x01",
            "是为了抛弃人道而成为修罗……\x02\x03",

            "#120F而你，只是为了填补\x01",
            "自我的空虚而挥剑罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#052F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#124F挥舞沉重的铁块，\x01",
            "让悲哀的空虚充满激情……\x02\x03",

            "当愤怒震慑心灵之际，\x01",
            "便可以从悲伤之中逃离出来。\x02\x03",

            "#121F但是，这只不过是自欺欺人罢了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2445():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2445)
    Sleep(500)

    ChrTalk(    #23
        0x9,
        "#056F…………住口………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#123F而自欺欺人者\x01",
            "是不可能向前迈进的。\x02\x03",

            "莫说是领悟『理』之境界，\x01",
            "就连堕入『修罗』之道也是妄想。\x02\x03",

            "这样子下去……\x01",
            "你永远都只是个半吊子。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x3)

    def lambda_2518():
        OP_9E(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2518)
    Sleep(500)
    Fade(250)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x9,
        "#550F#3S给我闭嘴！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x1A17)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1102   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_8_161D end

    def Function_9_2592(): pass

    label("Function_9_2592")

    OP_71(0x0, 0x20)
    OP_6F(0x0, 385)
    OP_70(0x0, 0x1B3)
    Return()

    # Function_9_2592 end

    def Function_10_25A6(): pass

    label("Function_10_25A6")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_25CE():
        OP_8F(0x9, 0xD0C, 0x0, 0xFFFFF77C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25CE)

    def lambda_25E9():
        OP_6D(4450, 0, 1950, 1000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_25E9)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 11)

    def lambda_262E():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_262E)

    def lambda_263E():
        OP_96(0x9, 0x1022, 0x0, 0x2E4, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_263E)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_266E():
        OP_96(0x8, 0x1338, 0x0, 0xB54, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_266E)
    TurnDirection(0x8, 0x9, 0)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 400)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_26A4():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26A4)

    def lambda_26B4():
        OP_96(0x9, 0x1158, 0x0, 0x834, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_26B4)
    Sleep(250)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 7)

    def lambda_2734():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2734)
    WaitChrThread(0x9, 0x1)

    def lambda_2749():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2749)

    def lambda_2759():
        TurnDirection(0x9, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2759)

    def lambda_2767():
        OP_96(0x9, 0x143C, 0x0, 0xFFFFFD9E, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2767)
    WaitChrThread(0x9, 0x1)
    Sleep(100)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 24)

    def lambda_279E():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_279E)
    Sleep(400)

    def lambda_27B3():
        OP_96(0x9, 0x1464, 0x0, 0x172, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_27B3)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_27F2():
        OP_96(0x8, 0x7A8, 0x0, 0xFFFFEC50, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_27F2)

    def lambda_2810():
        OP_6D(1870, 0, -5050, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2810)
    Sleep(200)

    def lambda_282D():
        OP_8C(0x8, 0, 0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_282D)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    TurnDirection(0x9, 0x8, 500)
    Sleep(100)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 19)

    def lambda_2877():
        OP_99(0xFE, 0x14, 0x17, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2877)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2891():
        OP_6D(1990, 2310, -4890, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2891)

    def lambda_28A9():
        OP_96(0x9, 0x87A, 0x0, 0xFFFFF060, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_28A9)
    Sleep(600)

    def lambda_28CC():
        OP_6D(1870, 0, -5050, 100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28CC)

    def lambda_28E4():
        OP_6B(3360, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28E4)
    SetChrFlags(0x9, 0x800)
    OP_22(0x55, 0x0, 0x5A)

    def lambda_28FE():
        OP_99(0xFE, 0x18, 0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28FE)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_2920():
        OP_96(0x8, 0x2A8, 0x0, 0xFFFFDCD8, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2920)
    PlayEffect(0x12, 0xFF, 0xFF, 1960, 0, -5040, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0x7D0, 0x64)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_25A6 end

    def Function_11_299F(): pass

    label("Function_11_299F")

    Sleep(200)

    def lambda_29AA():
        OP_8C(0x8, 0, 0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_29AA)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_11_299F end

    def Function_12_29CF(): pass

    label("Function_12_29CF")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 10)
    SetChrSubChip(0x9, 0)

    def lambda_29F7():
        OP_8F(0x9, 0xD0C, 0x0, 0xFFFFF77C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29F7)

    def lambda_2A12():
        OP_6D(4450, 0, 1950, 600)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A12)

    def lambda_2A2A():
        OP_6B(2870, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A2A)
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 3)

    def lambda_2A67():
        OP_96(0x9, 0x1022, 0x0, 0x2E4, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A67)
    Sleep(200)

    def lambda_2A8A():
        OP_99(0xFE, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A8A)
    OP_22(0x1F9, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x14, 0x12C)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 2)

    def lambda_2AB1():
        OP_96(0x8, 0x1338, 0x0, 0xB54, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AB1)
    TurnDirection(0x8, 0x9, 0)
    WaitChrThread(0x9, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Sleep(300)
    TurnDirection(0x9, 0x8, 400)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_2AFE():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2AFE)

    def lambda_2B0E():
        OP_96(0x9, 0x1158, 0x0, 0x834, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B0E)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 1)

    def lambda_2B36():
        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B36)
    Sleep(250)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x9, 0x1)

    def lambda_2B9A():
        OP_99(0xFE, 0x4, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B9A)

    def lambda_2BAA():
        TurnDirection(0x9, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2BAA)

    def lambda_2BB8():
        OP_96(0x9, 0x143C, 0x0, 0xFFFFFD9E, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2BB8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)

    def lambda_2BE5():
        OP_99(0xFE, 0x0, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BE5)
    Sleep(400)

    def lambda_2BFA():
        OP_96(0x9, 0x1464, 0x0, 0x172, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2BFA)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_2C39():
        OP_96(0x8, 0x7A8, 0x0, 0xFFFFEC50, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C39)

    def lambda_2C57():
        OP_6D(2800, 0, -1440, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C57)

    def lambda_2C6F():
        OP_6B(3370, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C6F)
    OP_43(0x8, 0x0, 0x0, 0xB)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x9, 0x20)
    TurnDirection(0x9, 0x8, 1000)
    ClearChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 19)

    def lambda_2CB5():
        OP_99(0xFE, 0x13, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CB5)
    WaitChrThread(0x9, 0x1)
    Sleep(100)

    def lambda_2CCF():
        OP_99(0xFE, 0x15, 0x17, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CCF)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2CE9():
        OP_6D(1990, 2310, -4890, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CE9)

    def lambda_2D01():
        OP_96(0x9, 0x87A, 0x0, 0xFFFFF060, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2D01)
    Sleep(200)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 10)
    Sleep(200)
    OP_7D(0x0, 0x8, 0x1E, 0x12C)
    SetChrChipByIndex(0x8, 31)
    SetChrSubChip(0x8, 0)

    def lambda_2D4A():
        OP_96(0x8, 0x2A8, 0x0, 0xFFFFDCD8, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D4A)
    Sleep(200)

    def lambda_2D6D():
        OP_6D(1870, 0, -5050, 100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D6D)

    def lambda_2D85():
        OP_6B(3360, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D85)
    OP_44(0x9, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 23)
    SetChrSubChip(0x9, 24)

    def lambda_2DAD():
        OP_99(0xFE, 0x18, 0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DAD)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, 1960, -1000, -5040, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_29CF end

    def Function_13_2E23(): pass

    label("Function_13_2E23")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E36")
    Call(0, 52)

    label("loc_2E36")

    OP_6D(3100, 0, 170, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 4500, 0, 2110, 180)
    SetChrPos(0x9, 2950, 0, -4500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 3)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 12660, 0, 13410, 225)
    OP_A1(0x18, 0x0)
    SetChrPos(0x18, 12660, 0, 13410, 232)
    SetChrPos(0x19, 0, 0, 0, 225)
    OP_CF(0x19, 0x0, "Frame127_FireEmitter")
    SetChrFlags(0x18, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1964), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 385)
    OP_70(0x0, 0x1B3)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "monster\\ms30703.eff")
    LoadEffect(0x2, "battle\\\\btbomb00.eff")
    LoadEffect(0x3, "map\\\\mp009_00.eff")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x9,
        "#550F#3S啊啊啊啊啊啊啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x18, 0x0, 0x0, 0xC)
    WaitChrThread(0x18, 0x0)
    Sleep(1000)

    def lambda_3014():
        OP_6D(1300, 0, -5900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3014)

    def lambda_302C():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_302C)

    def lambda_3044():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3044)

    def lambda_3054():
        OP_6C(332000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3054)

    def lambda_3064():
        OP_6E(262, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3064)
    OP_99(0x9, 0x1A, 0x1E, 0x3E8)
    WaitChrThread(0x101, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x800)

    ChrTalk(    #27
        0x9,
        "#550F可、可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#124F真难看啊……\x02\x03",

            "#120F我的同情心可是有限度的。\x01",
            "差不多该结束了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 8)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #29
        0x8,
        "#126F喝啊啊啊啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "#550F唔……\x02",
    )

    CloseMessageWindow()

    def lambda_3168():
        OP_6D(1910, 0, -4550, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3168)

    def lambda_3180():
        OP_96(0xFE, 0xBEA, 0x0, 0xFFFFF5D8, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3180)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 7)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x3, "map\\\\mp009_00.eff")

    ChrTalk(    #31
        0x8,
        "#127F#5P──喝！\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x16, 1380, 0, -6560, 0)
    ClearChrFlags(0x16, 0x80)

    def lambda_3209():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3209)
    OP_82(0x0, 0x0)

    def lambda_321E():
        OP_96(0xFE, 0x1342, 0x0, 0x8C0, 0xC8, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_321E)
    OP_22(0x9B, 0x0, 0x64)
    OP_20(0x0)
    PlayEffect(0x3, 0x1, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x17, 0x0, 0x0, 0x28)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 16)
    SetChrSubChip(0x9, 0)

    def lambda_3291():
        OP_6D(3620, 0, 240, 200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3291)
    SetChrChipByIndex(0x8, 7)
    SetChrSubChip(0x8, 5)
    WaitChrThread(0x16, 0x1)
    SetChrFlags(0x16, 0x80)
    Sleep(1000)

    def lambda_32C2():

        label("loc_32C2")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_32C2")

    QueueWorkItem2(0x9, 3, lambda_32C2)
    Sleep(500)

    ChrTalk(    #32
        0x9,
        "#056F#6P……呜啊………\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0x3)
    OP_99(0x9, 0x1, 0x4, 0x3E8)
    OP_22(0x20C, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_99(0x8, 0x5, 0x7, 0x640)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    def lambda_3338():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3338)
    Sleep(1000)

    ChrTalk(    #33
        0x8,
        "#121F……………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x8, 0, 400)

    def lambda_338D():
        OP_6D(4340, 0, 9850, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_338D)

    def lambda_33A5():
        OP_67(0, 4770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33A5)

    def lambda_33BD():
        OP_6B(4410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33BD)

    def lambda_33CD():
        OP_6C(359000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_33CD)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #34
        0x8,
        (
            "#124F#2P好了……\x01",
            "差不多到时间了。\x02\x03",

            "#120F趁现在把『福音』的\x01",
            "控制程式也调整一下吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #35
        0x9,
        "#5P#40W……慢、慢着……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x9, 400)
    Fade(500)
    OP_6D(3620, 0, 240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_1D(0x53)

    def lambda_34C0():

        label("loc_34C0")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_34C0")

    QueueWorkItem2(0x9, 3, lambda_34C0)
    Sleep(500)
    OP_99(0x9, 0x4, 0x1, 0x1F4)
    OP_44(0x9, 0x3)
    Sleep(500)

    def lambda_34F4():

        label("loc_34F4")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_34F4")

    QueueWorkItem2(0x9, 3, lambda_34F4)
    SetChrFlags(0x9, 0x20)
    OP_8C(0x9, 0, 200)
    OP_44(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    Sleep(500)

    ChrTalk(    #36
        0x9,
        (
            "#550F#40W还……还没完……\x02\x03",

            "还没结束……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-26270, 0, 18840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -26050, 0, 19690, 90)
    SetChrPos(0x107, -26220, 0, 18290, 90)
    SetChrPos(0xF8, -27300, 0, 19840, 90)
    SetChrPos(0xF9, -27540, 0, 18220, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#1020F#5P那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        "#065F#6P阿、阿加特哥哥！\x02",
    )

    CloseMessageWindow()

    def lambda_3620():
        OP_8E(0xFE, 0xFFFFC7D4, 0x0, 0x3AB6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3620)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #39
        0x101,
        "#1005F#5P提妲！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_71(0x0, 0x4)
    Fade(500)
    OP_6D(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(1780, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #40
        0x8,
        (
            "#124F……到这时候\x01",
            "还想把破碎的铁块粘起来吗。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x8,
        (
            "#123F好吧。\x01",
            "就让你带着遗憾离开这个世界吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x107, -8990, 0, 1190, 135)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 17)

    NpcTalk(    #42
        0x107,
        "少女的声音",
        "#3S不行～！！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 5)
    SetChrFlags(0x107, 0x1000)

    def lambda_37D2():
        OP_6B(2000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D2)

    def lambda_37E2():
        OP_67(0, 7000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37E2)
    OP_8E(0x107, 0xED8, 0x0, 0xFFFFFBA0, 0x1770, 0x0)
    TurnDirection(0x107, 0x8, 400)
    Sleep(500)

    ChrTalk(    #43
        0x9,
        (
            "#550F臭小鬼……\x02\x03",

            "……为什么……\x01",
            "会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#065F#6P那个那个……\x02\x03",

            "因为担心阿加特哥哥… \x01",
            "所以就和姐姐一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#3S提妲！！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x0, "map\\\\mp015_00.eff")
    TurnDirection(0x8, 0x101, 400)
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #46
        0x8,
        "#121F#6P……停下。\x02",
    )

    CloseMessageWindow()
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Fade(500)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 15390, 0, 12100, 255)
    OP_6D(11070, 0, 18710, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(21000, 0)
    OP_6E(426, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x122, 0x0, 0x64)
    Sleep(1000)

    def lambda_39A9():
        OP_6D(4220, 3290, 14610, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_39A9)

    def lambda_39C1():
        OP_67(0, 2730, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_39C1)

    def lambda_39D9():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_39D9)

    def lambda_39E9():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_39E9)

    def lambda_39F9():
        OP_6E(426, 3000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_39F9)
    OP_72(0x0, 0x20)
    Fade(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 460)
    OP_70(0x0, 0x16D)

    def lambda_3A25():
        OP_8E(0xFE, 0xFFFFEBF6, 0x0, 0x14FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A25)

    def lambda_3A40():
        OP_8E(0xFE, 0xFFFFEB92, 0x0, 0x19FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3A40)

    def lambda_3A5B():
        OP_8E(0xFE, 0xFFFFE4F8, 0x0, 0x1270, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3A5B)
    OP_73(0x0)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 80)
    OP_70(0x0, 0x78)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0x19, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_6D(3920, 0, 15460, 0)
    OP_67(0, 2610, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)
    Sleep(300)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B47")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3B7B")

    label("loc_3B47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B69")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3B7B")

    label("loc_3B69")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3B7B")

    OP_43(0xF9, 0x0, 0x0, 0x13)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA9")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3BDD")

    label("loc_3BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCB")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Jump("loc_3BDD")

    label("loc_3BCB")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_3BDD")

    OP_43(0xF8, 0x0, 0x0, 0x12)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x11)
    OP_73(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    OP_63(0xF8)
    OP_63(0xF9)
    OP_63(0x101)

    ChrTalk(    #47
        0x101,
        "#1021F#5P唔……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x0, 0x20)
    OP_6F(0x0, 465)
    OP_70(0x0, 0x1E7)
    Sleep(500)
    OP_22(0x122, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)

    def lambda_3CC1():
        OP_96(0xFE, 0xFFFFC5A4, 0x0, 0x256C, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3CC1)
    Sleep(100)

    def lambda_3CE4():
        OP_96(0xFE, 0xFFFFCE32, 0x0, 0x2ADA, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3CE4)
    Sleep(100)

    def lambda_3D07():
        OP_96(0xFE, 0xFFFFD152, 0x0, 0x25C6, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D07)
    OP_73(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x20)
    OP_6F(0x0, 487)
    OP_70(0x0, 0x205)
    Fade(500)
    OP_6D(-5710, 0, 10880, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(78000, 0)
    OP_6E(599, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DB8")

    ChrTalk(    #48
        0x108,
        "#077F#5P哦，麻烦了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E0F")

    label("loc_3DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE5")

    ChrTalk(    #49
        0x103,
        "#523F#5P唔，不妙呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E0F")

    label("loc_3DE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E0F")

    ChrTalk(    #50
        0x105,
        "#043F#5P怎、怎么办……\x02",
    )

    CloseMessageWindow()

    label("loc_3E0F")

    Sleep(500)
    Fade(500)
    OP_71(0x0, 0x4)
    OP_6D(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x8,
        "#121F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x4, 0x0, 0x5DC)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 25)
    Sleep(250)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)
    OP_43(0x8, 0x0, 0x0, 0x10)

    def lambda_3EB8():
        OP_6D(3300, 0, -900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EB8)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(    #52 op#A op#5
        0x107,
        "#065F#5P#17A啊、啊呜……\x05\x02",
    )

    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 17)
    OP_8F(0x107, 0xDCA, 0x0, 0xFFFFF95C, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_63(0x107)
    SetChrFlags(0x107, 0x2)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 18)
    Sleep(500)

    ChrTalk(    #53
        0x107,
        "#068F#5P别、别过来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#550F白、白痴……\x01",
            "那种东西管用吗！\x02\x03",

            "别管我了……\x01",
            "赶快逃跑……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #55
        0x8,
        (
            "#121F拉赛尔博士的孙女，\x01",
            "提妲·拉赛尔吗……\x02\x03",

            "听说是位天才少女，\x01",
            "但行为也太莽撞了吧。\x02\x03",

            "#124F虽然我没有兴趣\x01",
            "对付小女孩──\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x8,
        (
            "#120F──但如有必要，一样杀无赦！\x02\x03",

            "你还是乖乖地让开比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "#550F你、你这混帐……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#062F#5P我、我不会让开的！\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x107, 0x0, 0x4, 0x4B0)

    def lambda_40FD():
        OP_6B(1700, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40FD)
    Sleep(500)

    ChrTalk(    #59
        0x107,
        (
            "#063F#5P我……总是给阿加特哥哥\x01",
            "添麻烦，一直受他的照顾……\x02\x03",

            "只有现在…我才能\x01",
            "偿还这些恩情……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 6)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 7)
    Sleep(50)
    SetChrSubChip(0x107, 8)
    Sleep(50)
    SetChrSubChip(0x107, 7)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 6)
    Sleep(50)
    SetChrSubChip(0x107, 5)
    Sleep(50)
    SetChrSubChip(0x107, 4)
    Sleep(500)

    ChrTalk(    #60
        0x107,
        "#561F#5P不……不对……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #61
        0x107,
        (
            "#066F#5P虽然阿加特哥哥对我……\x01",
            "总是一副不耐烦的样子……\x02\x03",

            "一直都叫我小鬼小鬼的，\x01",
            "把我当小孩子对待……\x02\x03",

            "但其实他真的很温柔……\x01",
            "总是默默地保护着我……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x4, 0x0, 0x5DC)
    Sleep(300)

    ChrTalk(    #62
        0x107,
        "#062F#5P是我最喜欢……最重要的人！\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x0, 0x4, 0x7D0)

    def lambda_42EF():
        OP_99(0x107, 0x9, 0x17, 0x7D0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_42EF)
    Sleep(400)
    OP_22(0xD8, 0x0, 0x50)
    OP_22(0x82, 0x0, 0x50)
    WaitChrThread(0x107, 0x2)
    Sleep(300)
    OP_99(0x107, 0x18, 0x1B, 0x7D0)
    Sleep(500)

    ChrTalk(    #63
        0x107,
        (
            "#068F#5P#3S所以我……\x01",
            "绝对不会让开的！！\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "#052F……啊…………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #65
        0x8,
        (
            "#124F哼，真是勇敢。\x02\x03",

            "#121F这种半吊子真的\x01",
            "值得你这么倾慕吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrPos(0x1A, -11240, 30000, -11760, 227)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0x107, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0x8,
        (
            "#123F算了，既然有人插手，\x01",
            "这次我就暂且退下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        "#064F#5P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x3E8)
    Fade(500)
    OP_72(0x0, 0x4)
    SetChrPos(0x18, 12660, 0, 13410, 225)
    OP_6D(780, 0, 12430, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(332000, 0)
    OP_6E(552, 0)
    OP_0D()
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_CF(0x1B, 0x0, "Frame143_back_Null1")
    SetChrPos(0x1C, 9190, 0, 5540, 0)
    SetChrPos(0x1D, -230, 0, 4170, 0)
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x0, 0x20)
    PlayEffect(0x2, 0xFF, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 517)
    OP_70(0x0, 0x21C)
    OP_73(0x0)
    OP_6F(0x0, 125)
    OP_70(0x0, 0xB4)
    Sleep(1500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)

    def lambda_45E6():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45E6)

    def lambda_45F4():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_45F4)

    def lambda_4602():
        TurnDirection(0xFE, 0x1A, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4602)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x37)
    Sleep(500)
    OP_1D(0x74)
    Sleep(500)
    Fade(500)
    OP_72(0x1, 0x4)
    OP_A1(0x1A, 0x1)
    SetChrPos(0x1A, -11240, 30000, -11760, 227)
    LoadEffect(0x4, "map\\\\mp021_00.eff")
    OP_6D(-1010, 0, -1490, 0)
    OP_67(0, 22530, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(30000, 0)
    OP_6E(523, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_43(0x1A, 0x1, 0x0, 0x15)

    def lambda_46AC():
        OP_6D(-8560, 0, -7500, 13000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46AC)

    def lambda_46C4():
        OP_6C(315000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46C4)

    def lambda_46D4():
        OP_6B(1890, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_46D4)
    Sleep(2000)
    SetMessageWindowPos(100, 75, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #68 op#A op#5
        (
            "\x07\x00#163F#49A主炮和右舷副炮，\x01",
            "锁定瞄准龙！\x05\x02",
        )
    )

    Sleep(5200)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #69 op#A op#5
        (
            "\x07\x00#160F#33A着陆同时，\x01",
            "全体人员，迅速展开！\x05\x02",
        )
    )

    Sleep(3800)
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("士兵们")

    AnonymousTalk(    #70 op#A op#5
        "\x07\x00#5S#10A Yes·Sir！\x05\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Sleep(2000)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_47BF():
        OP_8C(0xFE, 125, 10)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_47BF)
    Sleep(100)

    def lambda_47D2():
        OP_8C(0xFE, 125, 16)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_47D2)
    Sleep(100)

    def lambda_47E5():
        OP_8C(0xFE, 125, 20)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_47E5)
    Sleep(100)

    def lambda_47F8():
        OP_8C(0xFE, 125, 26)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_47F8)
    Sleep(100)

    def lambda_480B():
        OP_8C(0xFE, 125, 30)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_480B)
    Sleep(100)

    def lambda_481E():
        OP_8C(0xFE, 125, 39)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_481E)
    Sleep(85)

    def lambda_4831():
        OP_8C(0xFE, 125, 40)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4831)
    Sleep(85)

    def lambda_4844():
        OP_8C(0xFE, 125, 46)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4844)
    Sleep(85)

    def lambda_4857():
        OP_8C(0xFE, 125, 50)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4857)
    Sleep(85)

    def lambda_486A():
        OP_8C(0xFE, 125, 59)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_486A)
    Sleep(85)

    def lambda_487D():
        OP_8C(0xFE, 125, 60)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_487D)
    Sleep(85)

    def lambda_4890():
        OP_8C(0xFE, 125, 66)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4890)
    Sleep(85)

    def lambda_48A3():
        OP_8C(0xFE, 125, 50)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_48A3)
    Sleep(85)
    OP_6F(0x1, 1001)
    OP_70(0x1, 0x3FC)

    def lambda_48C4():
        OP_8C(0xFE, 125, 30)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_48C4)
    Sleep(85)

    def lambda_48D7():
        OP_8C(0xFE, 125, 20)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_48D7)
    Sleep(85)

    def lambda_48EA():
        OP_8C(0xFE, 125, 14)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_48EA)
    WaitChrThread(0x1A, 0x3)
    Sleep(2000)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_23(0x79)
    OP_23(0xCC)
    OP_6D(4250, 0, 1420, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(332000, 0)
    OP_6E(321, 0)
    OP_6D(3320, 0, 260, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(321000, 0)
    OP_6E(374, 0)
    OP_0D()
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)

    ChrTalk(    #71
        0x8,
        (
            "#124F#2P呼……\x01",
            "总算登场了吗。\x02\x03",

            "#123F这样最后的实验\x01",
            "也可以开始了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x14)
    Sleep(600)
    Fade(500)
    OP_B0(0x0, 0xA)
    OP_6D(8460, 2890, 13560, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(42000, 0)
    OP_6E(374, 0)
    OP_0D()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #72
        0x107,
        "#065F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "#550F#5P慢、慢着……！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 315, 400)
    Sleep(500)

    ChrTalk(    #74
        0x8,
        (
            "#121F#6P别忘了。\x01",
            "阿加特·科洛斯纳。\x02\x03",

            "只要你还在自欺欺人，\x01",
            "就永远成不了任何气候。\x02\x03",

            "也保护不了你想要保护的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#550F#5P………咕…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#2P给、给我等一下！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -8130, 0, 9590, 90)
    SetChrPos(0xF8, -9490, 0, 10350, 90)
    SetChrPos(0xF9, -9580, 0, 8320, 90)
    SetChrSubChip(0x9, 4)
    Sleep(100)
    Fade(500)
    OP_6D(-3200, 0, 9770, 0)
    OP_67(0, 9230, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(260000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #77
        0x101,
        (
            "#1005F#6P默不吭声地听你说话，\x01",
            "你竟然就开始得意忘形，乱说一通！\x02\x03",

            "这次绝对不会让你逃跑！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #78
        0x8,
        (
            "#124F#5P艾丝蒂尔·布莱特。\x01",
            "你用心记住吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "#121F#5P这次实验结束后，\x01",
            "计划就会转移到下一阶段。\x02\x03",

            "到时要是不留神的话，\x01",
            "就一定会后悔的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    Sleep(300)
    LoadEffect(0x3, "map\\\\mp015_00.eff")
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x3, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Fade(500)
    OP_6D(19800, 0, 12010, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(4290, 0)
    OP_6C(80000, 0)
    OP_6E(431, 0)
    OP_8C(0x8, 0, 0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x101, 90, 0)
    OP_8C(0xF8, 90, 0)
    OP_8C(0xF9, 90, 0)
    OP_0D()
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 185)
    OP_70(0x0, 0xE1)
    Sleep(1000)
    OP_22(0x195, 0x0, 0x64)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    LoadEffect(0x0, "monster\\ms30704.eff")
    Fade(500)
    OP_6F(0x0, 225)
    OP_70(0x0, 0xF8)
    OP_B0(0x0, 0xA)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 235)
    OP_70(0x0, 0xF8)
    OP_43(0x18, 0x3, 0x0, 0xE)
    Sleep(500)
    OP_43(0x18, 0x2, 0x0, 0xF)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        (
            "#1020F#5P慢、慢着！\x01",
            "那到底是……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0x19)
    Sleep(400)
    LoadEffect(0x4, "monster\\ms30602b.eff")
    LoadEffect(0x5, "monster\\ms30602a.eff")
    LoadEffect(0x6, "map\\\\mp003_00.eff")
    LoadEffect(0x7, "scraft\\sc003_12.eff")
    Fade(500)
    OP_6D(-370, 0, 3680, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(200)
    OP_43(0x11, 0x1, 0x0, 0x1B)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x1C)
    Sleep(400)
    OP_43(0x12, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x1E)
    Sleep(300)
    OP_43(0x13, 0x1, 0x0, 0x1F)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x20)
    Sleep(400)
    OP_43(0x14, 0x1, 0x0, 0x21)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x22)
    Sleep(400)
    OP_43(0xC, 0x1, 0x0, 0x23)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1A)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #82
        0xA,
        (
            "#162F#2P可恶的龙！\x01",
            "别想逃跑！\x02\x03",

            "全体人员，射击开始！\x01",
            "射击射击，尽量给我打！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(10720, 30000, 32460, 0)
    OP_67(0, 9320, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(180000, 0)
    OP_6E(306, 0)
    OP_43(0x1A, 0x0, 0x0, 0x26)
    OP_43(0xC, 0x1, 0x0, 0x25)
    OP_43(0x1A, 0x1, 0x0, 0x27)
    OP_43(0x11, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x24)
    OP_43(0x12, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x25)
    OP_43(0x14, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x24)
    OP_43(0x13, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x25)
    OP_43(0x15, 0x1, 0x0, 0x24)
    Sleep(2000)

    ChrTalk(    #83
        0x8,
        (
            "#123F#6P哼，对传说中的古代龙\x01",
            "那种攻击怎么可能有效。\x02\x03",

            "#124F走吧──『古龙雷格纳特』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_50F8():
        OP_6D(14000, 17250, 12870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50F8)

    def lambda_5110():
        OP_67(0, 8180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5110)

    def lambda_5128():
        OP_6B(4220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5128)

    def lambda_5138():
        OP_6C(200000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5138)

    def lambda_5148():
        OP_6E(426, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5148)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 200)
    OP_70(0x0, 0x113)
    OP_44(0x18, 0x3)
    OP_23(0x1F7)
    OP_22(0x195, 0x0, 0x64)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x0)
    OP_43(0x18, 0x3, 0x0, 0xE)

    def lambda_51AF():
        OP_6B(4800, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_51AF)

    def lambda_51BF():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_51BF)
    OP_6F(0x0, 545)
    OP_70(0x0, 0x234)
    PlayEffect(0x0, 0xFF, 0x18, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 565)
    OP_70(0x0, 0x249)
    OP_43(0x18, 0x2, 0x0, 0xF)

    def lambda_523A():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_523A)
    Sleep(300)
    OP_44(0x18, 0x2)

    def lambda_525E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_525E)
    Sleep(100)

    def lambda_527E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_527E)
    Sleep(100)

    def lambda_529E():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_529E)
    Sleep(100)

    def lambda_52BE():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_52BE)
    Sleep(100)

    def lambda_52DE():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_52DE)
    Sleep(100)

    def lambda_52FE():
        OP_8F(0xFE, 0x4B0, 0xD6D8, 0x96A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_52FE)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2E23 end

    def Function_14_5335(): pass

    label("Function_14_5335")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_534B")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("Function_14_5335")

    label("loc_534B")

    Return()

    # Function_14_5335 end

    def Function_15_534C(): pass

    label("Function_15_534C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5392")
    PlayEffect(0x0, 0xFF, 0x18, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    Jump("Function_15_534C")

    label("loc_5392")

    Return()

    # Function_15_534C end

    def Function_16_5393(): pass

    label("Function_16_5393")

    SetChrChipByIndex(0xFE, 25)
    OP_8F(0xFE, 0x1108, 0x0, 0x2C6, 0x2BC, 0x0)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_16_5393 end

    def Function_17_53B7(): pass

    label("Function_17_53B7")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFDC38, 0x0, 0x20D0, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_53B7 end

    def Function_18_53E5(): pass

    label("Function_18_53E5")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFDC6A, 0x0, 0x2620, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_53E5 end

    def Function_19_5413(): pass

    label("Function_19_5413")

    SetChrChipByIndex(0xFE, 65535)
    OP_96(0xFE, 0xFFFFD508, 0x0, 0x2238, 0x1F4, 0x1388)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_19_5413 end

    def Function_20_5441(): pass

    label("Function_20_5441")

    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0)
    OP_8C(0xFE, 0, 500)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_547E():
        OP_96(0xFE, 0x1FE0, 0x206C, 0x3566, 0x2328, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_547E)
    WaitChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x1)
    OP_8C(0xFE, 90, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x4)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 1)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_5441 end

    def Function_21_54F8(): pass

    label("Function_21_54F8")


    def lambda_54FE():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_54FE)
    Sleep(6000)

    def lambda_551E():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_551E)
    Sleep(3000)

    def lambda_553E():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_553E)
    Sleep(2000)

    def lambda_555E():
        OP_8F(0xFE, 0xFFFFD418, 0x0, 0xFFFFD210, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_555E)
    PlayEffect(0x4, 0x1, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x1, 0x64)
    Return()

    # Function_21_54F8 end

    def Function_22_55AE(): pass

    label("Function_22_55AE")

    OP_8E(0xFE, 0xFFFFE656, 0x0, 0x2CE2, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_22_55AE end

    def Function_23_55CA(): pass

    label("Function_23_55CA")

    OP_8E(0xFE, 0xFFFFDFA8, 0x0, 0x2DF0, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_23_55CA end

    def Function_24_55E6(): pass

    label("Function_24_55E6")

    OP_8E(0xFE, 0xFFFFE35E, 0x0, 0x26B6, 0x1770, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_24_55E6 end

    def Function_25_5602(): pass

    label("Function_25_5602")

    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF6D2, 0x0, 0xA50, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_25_5602 end

    def Function_26_5639(): pass

    label("Function_26_5639")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEB2E, 0x0, 0xFFFFFEDE, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_26_5639 end

    def Function_27_5684(): pass

    label("Function_27_5684")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEB38, 0x0, 0x11BC, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_27_5684 end

    def Function_28_56CF(): pass

    label("Function_28_56CF")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFFA4C, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_28_56CF end

    def Function_29_571A(): pass

    label("Function_29_571A")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFC90, 0x0, 0x37A, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_29_571A end

    def Function_30_5765(): pass

    label("Function_30_5765")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE142, 0x0, 0x139C, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_30_5765 end

    def Function_31_57B0(): pass

    label("Function_31_57B0")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF344, 0x0, 0x136, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_31_57B0 end

    def Function_32_57FB(): pass

    label("Function_32_57FB")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE9DA, 0x0, 0xAA0, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_32_57FB end

    def Function_33_5846(): pass

    label("Function_33_5846")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF1F0, 0x0, 0xFFFFF880, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_33_5846 end

    def Function_34_5891(): pass

    label("Function_34_5891")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFDE68, 0x0, 0xAF0, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_34_5891 end

    def Function_35_58DC(): pass

    label("Function_35_58DC")

    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8940, 0, -7810, 0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFE4BC, 0x0, 0x550, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_35_58DC end

    def Function_36_5927(): pass

    label("Function_36_5927")

    SetChrChipByIndex(0xFE, 20)

    label("loc_592C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59D6")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_596D")
    Sleep(500)
    Jump("loc_59D3")

    label("loc_596D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5982")
    Sleep(600)
    Jump("loc_59D3")

    label("loc_5982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5997")
    Sleep(700)
    Jump("loc_59D3")

    label("loc_5997")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59AC")
    Sleep(800)
    Jump("loc_59D3")

    label("loc_59AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59C1")
    Sleep(900)
    Jump("loc_59D3")

    label("loc_59C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59D3")
    Sleep(1000)

    label("loc_59D3")

    Jump("loc_592C")

    label("loc_59D6")

    Return()

    # Function_36_5927 end

    def Function_37_59D7(): pass

    label("Function_37_59D7")

    SetChrChipByIndex(0xFE, 20)

    label("loc_59DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D85")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A57")
    PlayEffect(0x6, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_5D82")

    label("loc_5A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA1")
    PlayEffect(0x6, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_5D82")

    label("loc_5AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AEB")
    PlayEffect(0x6, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_5D82")

    label("loc_5AEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B35")
    PlayEffect(0x6, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_5D82")

    label("loc_5B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7F")
    PlayEffect(0x6, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_5D82")

    label("loc_5B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BC9")
    PlayEffect(0x6, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_5D82")

    label("loc_5BC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C13")
    PlayEffect(0x6, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_5D82")

    label("loc_5C13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5D")
    PlayEffect(0x6, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_5D82")

    label("loc_5C5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CA7")
    PlayEffect(0x6, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_5D82")

    label("loc_5CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF1")
    PlayEffect(0x6, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_5D82")

    label("loc_5CF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D3B")
    PlayEffect(0x6, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_5D82")

    label("loc_5D3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D82")
    PlayEffect(0x6, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)

    label("loc_5D82")

    Jump("loc_59DC")

    label("loc_5D85")

    Return()

    # Function_37_59D7 end

    def Function_38_5D86(): pass

    label("Function_38_5D86")

    SetChrPos(0x28, -2890, 4570, -13910, 45)

    label("loc_5D97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6131")
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0x28, 0, 0, 0, -21, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x3E0, 0x0, 0x64)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E35")
    PlayEffect(0x4, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5E35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E7A")
    PlayEffect(0x4, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EBF")
    PlayEffect(0x4, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5EBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F04")
    PlayEffect(0x4, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F49")
    PlayEffect(0x4, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8E")
    PlayEffect(0x4, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5F8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FD3")
    PlayEffect(0x4, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_5FD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6018")
    PlayEffect(0x4, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_6018")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_605D")
    PlayEffect(0x4, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_605D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A2")
    PlayEffect(0x4, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_60A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E7")
    PlayEffect(0x4, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6129")

    label("loc_60E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6129")
    PlayEffect(0x4, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6129")

    Sleep(10000)
    Jump("loc_5D97")

    label("loc_6131")

    Return()

    # Function_38_5D86 end

    def Function_39_6132(): pass

    label("Function_39_6132")

    SetChrPos(0x1C, -1050, 0, 10880, 0)
    SetChrPos(0x1D, 610, 0, 13410, 0)
    SetChrPos(0x1E, 230, 0, 7550, 0)
    SetChrPos(0x1F, 7300, 0, 7640, 0)
    SetChrPos(0x20, 9270, 0, 5590, 0)
    SetChrPos(0x21, 11970, 0, 7410, 0)
    SetChrPos(0x22, 9780, 0, 8530, 0)
    SetChrPos(0x23, -1300, 0, 16110, 0)
    SetChrPos(0x24, 8280, 0, 5580, 0)
    SetChrPos(0x25, 11320, 0, 4310, 0)
    SetChrPos(0x26, 13890, 0, 5860, 0)
    SetChrPos(0x27, 6890, 0, 9970, 0)

    label("loc_61FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6880")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x7, 0x1, 0xFF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0x2, 0xFF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6306")
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6306")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6385")
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6404")
    PlayEffect(0x2, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6483")
    PlayEffect(0x2, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6483")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6502")
    PlayEffect(0x2, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6581")
    PlayEffect(0x2, 0xFF, 0x21, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6581")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6600")
    PlayEffect(0x2, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_6600")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_667F")
    PlayEffect(0x2, 0xFF, 0x23, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_667F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66FE")
    PlayEffect(0x2, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x22, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_66FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677D")
    PlayEffect(0x2, 0xFF, 0x25, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_677D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FC")
    PlayEffect(0x2, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x1D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_6878")

    label("loc_67FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6878")
    PlayEffect(0x2, 0xFF, 0x27, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0x26, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6878")

    Sleep(2000)
    Jump("loc_61FE")

    label("loc_6880")

    Return()

    # Function_39_6132 end

    def Function_40_6881(): pass

    label("Function_40_6881")

    SetChrPos(0xFE, 3990, 800, -760, 180)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)

    def lambda_68B1():
        OP_96(0xFE, 0x1554, 0xFFFFFE0C, 0xFFFFF8F8, 0xFA0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68B1)

    def lambda_68CF():

        label("loc_68CF")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_68CF")

    QueueWorkItem2(0xFE, 2, lambda_68CF)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    OP_22(0x124, 0x0, 0x50)
    SetChrSubChip(0xFE, 5)
    Return()

    # Function_40_6881 end

    def Function_41_68F0(): pass

    label("Function_41_68F0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6903")
    Call(0, 52)

    label("loc_6903")

    OP_6D(-20380, 0, 2110, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(257000, 0)
    OP_6E(660, 0)
    SetChrFlags(0x107, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xF8, -3000, 0, -4670, 225)
    SetChrPos(0x101, -4070, 0, -3070, 225)
    SetChrPos(0xF9, -2360, 0, -2940, 225)
    SetChrPos(0xA, -5010, 0, -5490, 45)
    SetChrPos(0xB, -5010, 0, -7780, 45)
    OP_72(0x1, 0x4)
    OP_6F(0x1, 200)

    def lambda_69C5():
        OP_6D(-10260, 0, -7880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69C5)

    def lambda_69DD():
        OP_67(0, 5350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69DD)

    def lambda_69F5():
        OP_6C(257000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69F5)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x1A, 0x1)
    SetChrPos(0x1A, -11240, 0, -11760, 127)
    SetChrFlags(0x1A, 0x1)
    ClearChrFlags(0x1A, 0x80)
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    OP_43(0xC, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x2B)
    Sleep(800)
    FadeToBright(2000, 0)
    OP_43(0xA, 0x3, 0x0, 0x2A)
    Sleep(500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #84
        0x101,
        "#1020F#6P──等、等一下！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-3640, 0, -5570, 0)
    OP_67(0, 4390, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(176000, 0)
    OP_6E(310, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #85
        0x101,
        (
            "#1005F#6P让我们收手是什么意思！？\x02\x03",

            "将军难道还把我们游击士\x01",
            "当作眼中钉吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "#160F话不是这么说。\x02\x03",

            "但是，那是连警备艇的导力炮\x01",
            "也难以伤之分毫的魔兽。\x02\x03",

            "你们究竟能做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1026F#6P这，这个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CA3")

    ChrTalk(    #88
        0x105,
        "#043F#6P将军……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "#163F……即使是公主殿下\x01",
            "我还是不能相让。\x02\x03",

            "#160F勇气和匹夫之勇是不同的。\x02\x03",

            "公主殿下也看过柏斯和拉文努村\x01",
            "所受到的损害了吧。\x02\x03",

            "即使说这是一场战争\x01",
            "也不为过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#049F#6P嗯嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D3C")

    label("loc_6CA3")


    ChrTalk(    #91
        0xA,
        (
            "#163F勇气和匹夫之勇是不同的。\x02\x03",

            "#160F你们也目睹了柏斯和拉文努村\x01",
            "所受到的损害了吧。\x02\x03",

            "即使说这是一场战争\x01",
            "也不为过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1003F#6P…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_6D3C")


    ChrTalk(    #93
        0xA,
        (
            "#163F常言道：术业有专攻。\x02\x03",

            "既然是战争，\x01",
            "还是交给我们专业人士为好。\x02\x03",

            "#161F至于你们，对了……\x01",
            "如能集中精力搜索『噬身之蛇』的据点\x01",
            "就帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1005F#6P但、但是……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -10540, 0, -390, 135)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #95
        0x9,
        "青年的声音",
        "#1P……开什么玩笑………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E82")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6EC0")

    label("loc_6E82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA9")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6EC0")

    label("loc_6EA9")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE7")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6F25")

    label("loc_6EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6F25")

    label("loc_6F0E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6F25")

    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6F4C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F4C)

    def lambda_6F5A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6F5A)
    Sleep(50)

    def lambda_6F6D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6F6D)

    def lambda_6F7B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6F7B)
    Sleep(50)

    def lambda_6F8E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6F8E)

    def lambda_6F9C():

        label("loc_6F9C")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6F9C")

    QueueWorkItem2(0x101, 2, lambda_6F9C)

    def lambda_6FAD():

        label("loc_6FAD")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6FAD")

    QueueWorkItem2(0xF8, 2, lambda_6FAD)

    def lambda_6FBE():

        label("loc_6FBE")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6FBE")

    QueueWorkItem2(0xF9, 2, lambda_6FBE)

    def lambda_6FCF():

        label("loc_6FCF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6FCF")

    QueueWorkItem2(0xA, 2, lambda_6FCF)

    def lambda_6FE0():

        label("loc_6FE0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_6FE0")

    QueueWorkItem2(0xB, 2, lambda_6FE0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0x9, 0x20)
    OP_43(0x9, 0x0, 0x0, 0x30)
    OP_6D(-4720, 0, -5400, 4000)

    ChrTalk(    #96
        0x101,
        "#1004F#5P阿加特……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x0)
    SetChrPos(0x107, -11980, 0, 4770, 135)
    ClearChrFlags(0x107, 0x80)

    ChrTalk(    #97
        0x107,
        "#1P阿、阿加特！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x107, 0xFFFFE944, 0x0, 0xFFFFF100, 0x1388, 0x0)
    TurnDirection(0x107, 0x9, 400)

    def lambda_70A6():

        label("loc_70A6")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_70A6")

    QueueWorkItem2(0x107, 2, lambda_70A6)

    ChrTalk(    #98
        0x107,
        (
            "#065F#6P才刚刚做了急救，\x01",
            "不可以逞强哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        "#1286F#4P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_44(0xA, 0x2)
    OP_44(0xB, 0x2)

    ChrTalk(    #100
        0xA,
        (
            "#160F#5P……你是……\x01",
            "『重剑』阿加特吗。\x02\x03",

            "听卡西乌斯说过\x01",
            "你是个很有朝气的青年游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#1282F#4P大叔的事先不说……\x02\x03",

            "#1293F我说……将军阁下啊……\x02\x03",

            "你说术业有专攻……\x01",
            "战争就交给专业人士……？\x02\x03",

            "这句话……是认真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#163F#5P……当然是认真的。\x02\x03",

            "#160F和保护人民的游击士不同，\x01",
            "我们必须得保护国家才行。\x02\x03",

            "在这种情况下，所谓的国家\x01",
            "指的是人民和国土两者。\x02\x03",

            "能做到这件事的只有军队而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        "#1291F#4P呵呵……保护人民和国土吗……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_72E3():

        label("loc_72E3")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_72E3")

    QueueWorkItem2(0x107, 1, lambda_72E3)

    def lambda_72F4():
        OP_6D(-4580, 0, -6170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_72F4)

    def lambda_730C():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_730C)
    OP_92(0x9, 0xA, 0x258, 0x5DC, 0x0)
    OP_44(0x9, 0x1)
    Fade(250)
    OP_6B(3000, 0)

    def lambda_733C():

        label("loc_733C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_733C")

    QueueWorkItem2(0xB, 2, lambda_733C)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 30)
    SetChrSubChip(0xA, 6)
    SetChrChipByIndex(0x9, 30)
    SetChrSubChip(0x9, 30)
    OP_0D()
    Sleep(500)

    ChrTalk(    #104
        0x9,
        "#1287F#4P#4S别惹人发笑了！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #105
        0xA,
        "#163F#5P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1020F#6P等、等等！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#065F#6P阿、阿加特哥哥！？\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x33)
    Sleep(500)

    ChrTalk(    #108
        0x9,
        (
            "#1287F#4P每、每次都是一样！！\x01",
            "你们这些混账永远都不能及时赶到！！\x02\x03",

            "只会说一些统一安排行动之类的废话！\x01",
            "研究什么无聊战术，错过大好时机！\x02\x03",

            "没有命令就什么也做不到！\x01",
            "能保护的东西都保护不了！\x02\x03",

            "这次也是！\x01",
            "１０年前的战争也是一样！！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x0)

    ChrTalk(    #109
        0xA,
        (
            "#161F#5P！！\x02\x03",

            "难不成，你是那时候的……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x0, 0x0, 0x33)

    ChrTalk(    #110
        0x9,
        (
            "#1287F#4P可恶……谁会放心\x01",
            "托付给你们……\x02\x03",

            "#1285F这次……只有这次……\x02\x03",

            "我……要亲手……\x01",
            "守护米夏……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x0)
    Sleep(500)

    def lambda_75C0():
        OP_6D(-4820, 0, -5480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75C0)

    def lambda_75D8():
        OP_67(0, 6660, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_75D8)

    def lambda_75F0():
        OP_6B(3010, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_75F0)

    def lambda_7600():
        OP_6E(280, 1500)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_7600)
    SetChrFlags(0x9, 0x800)

    def lambda_7615():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7615)

    def lambda_762B():
        OP_99(0xFE, 0xA, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_762B)

    def lambda_763B():
        OP_94(0x1, 0xFE, 0x0, 0xFFFFFF38, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_763B)

    def lambda_7651():
        OP_99(0xFE, 0x22, 0x27, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7651)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #111
        0x107,
        "#065F#6P阿加特哥哥！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1020F#6P等、等等！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #113
        0xA,
        (
            "#163F#5P……唔，伤口\x01",
            "似乎没有裂开。\x02\x03",

            "只是精神和体力耗尽\x01",
            "昏过去了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x107,
        "#063F#6P……阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1007F#6P真、真是的，\x01",
            "吓死人了……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xA, 0xF, 0x11, 0x3E8)
    Sleep(500)

    ChrTalk(    #116
        0xA,
        (
            "#160F#5P总之，最好找个\x01",
            "舒适的床铺让他睡一觉。\x02\x03",

            "他在村里有间房子，\x01",
            "我就送他去拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1015F#6P啊，嗯，拜托了。\x02\x03",

            "……………………………………\x02\x03",

            "#1004F为、为什么您会知道\x01",
            "阿加特的家在拉文努村呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "#160F#5P……我原来曾经\x01",
            "见过这家伙一次。\x02\x03",

            "那时候的少年……\x01",
            "已经长得这么大了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1026F#6P那时候？\x02",
    )

    CloseMessageWindow()
    OP_99(0xA, 0x11, 0x13, 0x3E8)
    Sleep(500)

    ChrTalk(    #120
        0xA,
        "#163F#5P『百日战役』结束以后……\x02",
    )

    CloseMessageWindow()
    OP_99(0xA, 0x14, 0x17, 0x3E8)
    Sleep(500)

    ChrTalk(    #121
        0xA,
        (
            "#166F#5P建造这家伙的妹妹和村人们\x01",
            "的墓碑时候的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x107,
        "#065F#6P！！！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_END)), "loc_796D")

    ChrTalk(    #123
        0x101,
        "#1020F#6P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7984")

    label("loc_796D")


    ChrTalk(    #124
        0x101,
        "#1020F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    label("loc_7984")

    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x6, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A9")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_79EB")

    label("loc_79A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C0")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xF7, 0xFF)
    Jump("loc_79EB")

    label("loc_79C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D7")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF7, 0xFF)
    Jump("loc_79EB")

    label("loc_79D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79EB")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xF7, 0xFF)

    label("loc_79EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A02")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)
    Jump("loc_7A44")

    label("loc_7A02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A19")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xF8, 0xFF)
    Jump("loc_7A44")

    label("loc_7A19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A30")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF8, 0xFF)
    Jump("loc_7A44")

    label("loc_7A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A44")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xF8, 0xFF)

    label("loc_7A44")

    OP_A2(0x1A83)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1201   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_41_68F0 end

    def Function_42_7A54(): pass

    label("Function_42_7A54")

    OP_43(0xE, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0xF, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x10, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x12, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x14, 0x1, 0x0, 0x2B)
    Sleep(800)
    OP_43(0x15, 0x1, 0x0, 0x2B)
    Return()

    # Function_42_7A54 end

    def Function_43_7AB0(): pass

    label("Function_43_7AB0")

    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, 6580, 0, -8930, 180)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF88A, 0x0, 0xFFFFB5B4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF6C, 0x514, 0xFFFFCA90, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_7AB0 end

    def Function_44_7B08(): pass

    label("Function_44_7B08")

    OP_8F(0xFE, 0xFFFFEA34, 0x0, 0xFFFFEF7A, 0xFA0, 0x0)
    Return()

    # Function_44_7B08 end

    def Function_45_7B1D(): pass

    label("Function_45_7B1D")

    OP_8F(0xFE, 0xFFFFF254, 0x0, 0xFFFFEE8A, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xA, 400)
    Return()

    # Function_45_7B1D end

    def Function_46_7B39(): pass

    label("Function_46_7B39")

    OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0xFFFFF4F2, 0xFA0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_46_7B39 end

    def Function_47_7B55(): pass

    label("Function_47_7B55")

    OP_8E(0xFE, 0xFFFFF682, 0x0, 0xFFFFF06A, 0xFA0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_47_7B55 end

    def Function_48_7B71(): pass

    label("Function_48_7B71")

    SetChrPos(0xFE, -10540, 0, -390, 135)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)

    def lambda_7B9C():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B9C)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_7BC0():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BC0)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_7BE4():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BE4)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_7C08():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C08)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_7C2C():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C2C)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Sleep(500)

    def lambda_7C50():
        OP_99(0xFE, 0x8, 0xF, 0x640)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C50)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x1)
    Return()

    # Function_48_7B71 end

    def Function_49_7C6A(): pass

    label("Function_49_7C6A")


    def lambda_7C70():
        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C70)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    Sleep(500)

    def lambda_7C94():
        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C94)
    OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    Return()

    # Function_49_7C6A end

    def Function_50_7CAE(): pass

    label("Function_50_7CAE")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)

    def lambda_7CC8():

        label("loc_7CC8")

        OP_99(0xFE, 0x8, 0xF, 0x3E8)
        OP_48()
        Jump("loc_7CC8")

    QueueWorkItem2(0xFE, 1, lambda_7CC8)
    OP_8F(0x9, 0xFFFFEAE8, 0x0, 0xFFFFEB9C, 0x3E8, 0x0)
    OP_44(0xFE, 0x1)
    SetChrSubChip(0xFE, 8)
    Return()

    # Function_50_7CAE end

    def Function_51_7CF3(): pass

    label("Function_51_7CF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D86")
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(100)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(100)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0x9, 31)
    Sleep(100)
    SetChrSubChip(0xA, 8)
    SetChrSubChip(0x9, 32)
    Sleep(100)
    SetChrSubChip(0xA, 9)
    SetChrSubChip(0x9, 33)
    Sleep(500)
    Jump("Function_51_7CF3")

    label("loc_7D86")

    Return()

    # Function_51_7CF3 end

    def Function_52_7D87(): pass

    label("Function_52_7D87")

    FadeToDark(0, 0, -1)
    OP_6D(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
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
        (0, "loc_7E3E"),
        (1, "loc_7E44"),
        (SWITCH_DEFAULT, "loc_7E4A"),
    )


    label("loc_7E3E")

    OP_A2(0x1200)
    Jump("loc_7E4A")

    label("loc_7E44")

    OP_A2(0x1201)
    Jump("loc_7E4A")

    label("loc_7E4A")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_52_7D87 end

    SaveToFile()

Try(main)
