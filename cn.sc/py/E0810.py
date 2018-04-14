from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0810   ._SN',
        MapName             = 'Event',
        Location            = 'E0810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '尤莉亚上尉',                           # 10
        '摩尔根将军',                           # 11
        '奈尔',                                 # 12
        '朵洛希',                               # 13
        '古代龙',                               # 14
        '飞船',                                 # 15
        '飞船',                                 # 16
        '飞船',                                 # 17
        '飞船',                                 # 18
        '飞船',                                 # 19
        '飞船',                                 # 20
        '目标用照相机',                         # 21
        '目标用照相机',                         # 22
        '目标',                                 # 23
        '目标',                                 # 24
        '目标',                                 # 25
        '目标',                                 # 26
        '怀斯曼教授',                           # 27
        '福音',                                 # 28
        '歼灭天使玲',                           # 29
        '帕蒂尔·玛蒂尔',                       # 30
        '幻想乐曲·德尔基昂',                   # 31
        '艾丝蒂尔',                             # 32
        '约修亚',                               # 33
        '卡西乌斯',                             # 34
        '基库',                                 # 35
        '穆拉',                                 # 36
        '拉赛尔博士',                           # 37
        '多伦',                                 # 38
        '吉尔',                                 # 39
        '阿加特',                               # 40
        '雪拉扎德',                             # 41
        '奥利维尔',                             # 42
        '科洛丝',                               # 43
        '提妲',                                 # 44
        '金',                                   # 45
        '凯文',                                 # 46
        '乔丝特',                               # 47
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
        'ED6_DT27/CH03580 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH02070 ._CH',             # 04
        'ED6_DT27/CH04550 ._CH',             # 05
        'ED6_DT27/CH04558 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT27/CH04510 ._CH',             # 08
        'ED6_DT26/CH20363 ._CH',             # 09
        'ED6_DT27/CH03550 ._CH',             # 0A
        'ED6_DT26/CH20341 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH02070P._CP',             # 04
        'ED6_DT27/CH04550P._CP',             # 05
        'ED6_DT27/CH04558P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT27/CH04510P._CP',             # 08
        'ED6_DT26/CH20363P._CP',             # 09
        'ED6_DT27/CH03550P._CP',             # 0A
        'ED6_DT26/CH20341P._CP',             # 0B
        'ED6_DT26/CH20341P._CP',             # 0C
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
        NpcIndex            = 0x84,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 458759,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E2,
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


    ScpFunction(
        "Function_0_5EE",          # 00, 0
        "Function_1_A3A",          # 01, 1
        "Function_2_B65",          # 02, 2
        "Function_3_D02",          # 03, 3
        "Function_4_D67",          # 04, 4
        "Function_5_EC8",          # 05, 5
        "Function_6_106C",         # 06, 6
        "Function_7_17B6",         # 07, 7
        "Function_8_17D2",         # 08, 8
        "Function_9_1852",         # 09, 9
        "Function_10_19C8",        # 0A, 10
        "Function_11_1A77",        # 0B, 11
        "Function_12_1B2B",        # 0C, 12
        "Function_13_1C01",        # 0D, 13
        "Function_14_1CD7",        # 0E, 14
        "Function_15_1D04",        # 0F, 15
        "Function_16_1D31",        # 10, 16
        "Function_17_1D5E",        # 11, 17
        "Function_18_21D4",        # 12, 18
        "Function_19_22B9",        # 13, 19
        "Function_20_239E",        # 14, 20
        "Function_21_2483",        # 15, 21
        "Function_22_2568",        # 16, 22
        "Function_23_2D3D",        # 17, 23
        "Function_24_2E13",        # 18, 24
        "Function_25_3418",        # 19, 25
        "Function_26_3498",        # 1A, 26
        "Function_27_3554",        # 1B, 27
        "Function_28_3841",        # 1C, 28
        "Function_29_38A1",        # 1D, 29
        "Function_30_3909",        # 1E, 30
        "Function_31_3971",        # 1F, 31
        "Function_32_39D9",        # 20, 32
        "Function_33_45CB",        # 21, 33
        "Function_34_4623",        # 22, 34
        "Function_35_4704",        # 23, 35
        "Function_36_4840",        # 24, 36
        "Function_37_4938",        # 25, 37
        "Function_38_550B",        # 26, 38
        "Function_39_5621",        # 27, 39
        "Function_40_5677",        # 28, 40
        "Function_41_57CD",        # 29, 41
        "Function_42_58C3",        # 2A, 42
        "Function_43_593F",        # 2B, 43
        "Function_44_5A7B",        # 2C, 44
        "Function_45_5B71",        # 2D, 45
        "Function_46_5C8D",        # 2E, 46
        "Function_47_5E59",        # 2F, 47
        "Function_48_5EC9",        # 30, 48
        "Function_49_5F3E",        # 31, 49
        "Function_50_5FAE",        # 32, 50
        "Function_51_6023",        # 33, 51
        "Function_52_605E",        # 34, 52
        "Function_53_6590",        # 35, 53
        "Function_54_68E9",        # 36, 54
        "Function_55_6C86",        # 37, 55
        "Function_56_6D04",        # 38, 56
        "Function_57_6D82",        # 39, 57
        "Function_58_6E00",        # 3A, 58
        "Function_59_6E7E",        # 3B, 59
        "Function_60_700A",        # 3C, 60
        "Function_61_712C",        # 3D, 61
        "Function_62_71CD",        # 3E, 62
        "Function_63_78AB",        # 3F, 63
        "Function_64_7A98",        # 40, 64
        "Function_65_7C7F",        # 41, 65
        "Function_66_7CBB",        # 42, 66
        "Function_67_864F",        # 43, 67
        "Function_68_8683",        # 44, 68
        "Function_69_875F",        # 45, 69
        "Function_70_883B",        # 46, 70
        "Function_71_8A25",        # 47, 71
        "Function_72_8C0D",        # 48, 72
        "Function_73_8DE5",        # 49, 73
        "Function_74_8FFE",        # 4A, 74
        "Function_75_91DB",        # 4B, 75
        "Function_76_9493",        # 4C, 76
        "Function_77_9524",        # 4D, 77
        "Function_78_9655",        # 4E, 78
        "Function_79_980D",        # 4F, 79
        "Function_80_99C5",        # 50, 80
        "Function_81_9B6F",        # 51, 81
        "Function_82_B204",        # 52, 82
        "Function_83_B250",        # 53, 83
        "Function_84_B29E",        # 54, 84
        "Function_85_B304",        # 55, 85
        "Function_86_B3C2",        # 56, 86
        "Function_87_B46A",        # 57, 87
        "Function_88_B580",        # 58, 88
        "Function_89_B716",        # 59, 89
        "Function_90_B8AC",        # 5A, 90
        "Function_91_BA42",        # 5B, 91
        "Function_92_BBD8",        # 5C, 92
        "Function_93_BD6E",        # 5D, 93
        "Function_94_BE8C",        # 5E, 94
        "Function_95_C0A3",        # 5F, 95
        "Function_96_C2DE",        # 60, 96
        "Function_97_C326",        # 61, 97
        "Function_98_C561",        # 62, 98
        "Function_99_C5A9",        # 63, 99
        "Function_100_CEA6",       # 64, 100
        "Function_101_CF09",       # 65, 101
        "Function_102_D02C",       # 66, 102
        "Function_103_D136",       # 67, 103
        "Function_104_D264",       # 68, 104
        "Function_105_D2EF",       # 69, 105
        "Function_106_D604",       # 6A, 106
        "Function_107_D66B",       # 6B, 107
        "Function_108_EBFE",       # 6C, 108
        "Function_109_EC59",       # 6D, 109
        "Function_110_EC90",       # 6E, 110
        "Function_111_ECA6",       # 6F, 111
        "Function_112_ED52",       # 70, 112
        "Function_113_ED8B",       # 71, 113
        "Function_114_EDF1",       # 72, 114
        "Function_115_EE61",       # 73, 115
        "Function_116_EF7B",       # 74, 116
        "Function_117_F01D",       # 75, 117
        "Function_118_F079",       # 76, 118
        "Function_119_F225",       # 77, 119
        "Function_120_F26D",       # 78, 120
        "Function_121_F3E3",       # 79, 121
        "Function_122_F40D",       # 7A, 122
        "Function_123_F428",       # 7B, 123
        "Function_124_F52A",       # 7C, 124
        "Function_125_F5C1",       # 7D, 125
        "Function_126_F5FE",       # 7E, 126
        "Function_127_F621",       # 7F, 127
        "Function_128_F660",       # 80, 128
        "Function_129_F6FB",       # 81, 129
        "Function_130_F8C1",       # 82, 130
        "Function_131_F974",       # 83, 131
        "Function_132_F993",       # 84, 132
        "Function_133_F9E0",       # 85, 133
        "Function_134_FA12",       # 86, 134
        "Function_135_FA88",       # 87, 135
    )


    def Function_0_5EE(): pass

    label("Function_0_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FD)
    OP_A3(0x10F0)
    Event(0, 59)
    Jump("loc_A39")

    label("loc_60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_630")
    OP_A3(0x10FE)
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_A39")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F0)
    Event(0, 63)
    Jump("loc_A39")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_672")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F1)
    Event(0, 64)
    Jump("loc_A39")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F2)
    Event(0, 65)
    Jump("loc_A39")

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F3)
    Event(0, 66)
    Jump("loc_A39")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F4)
    Event(0, 70)
    Jump("loc_A39")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6")
    OP_A3(0x10FF)
    OP_A3(0x10F5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 75)
    Jump("loc_A39")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_717")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F6)
    Event(0, 81)
    Jump("loc_A39")

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F7)
    Event(0, 99)
    Jump("loc_A39")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F8)
    Event(0, 78)
    Jump("loc_A39")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10F9)
    Event(0, 79)
    Jump("loc_A39")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10FA)
    Event(0, 105)
    Jump("loc_A39")

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BC")
    OP_A3(0x10FF)
    OP_A3(0x10FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 80)
    Jump("loc_A39")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FF)
    OP_A3(0x10FC)
    Event(0, 107)
    Jump("loc_A39")

    label("loc_7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_7FC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_A39")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_81B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_A39")

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_83A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_A39")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_859")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_A39")

    label("loc_859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_878")
    OP_A3(0x10F4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 22)
    Jump("loc_A39")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_897")
    OP_A3(0x10F5)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_A39")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_8FB")
    OP_A3(0x10F6)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_76(0xFF, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    Event(0, 27)
    Jump("loc_A39")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_911")
    OP_A3(0x10F7)
    SetMapFlags(0x10000000)
    Event(0, 32)
    Jump("loc_A39")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_930")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F8)
    SetMapFlags(0x10000000)
    Event(0, 62)
    Jump("loc_A39")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_94A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    Event(0, 37)
    Jump("loc_A39")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 2)), scpexpr(EXPR_END)), "loc_964")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FA)
    Event(0, 52)
    Jump("loc_A39")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 3)), scpexpr(EXPR_END)), "loc_97E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FB)
    Event(0, 54)
    Jump("loc_A39")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 4)), scpexpr(EXPR_END)), "loc_9DD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10FC)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    Event(0, 60)
    Jump("loc_A39")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 5)), scpexpr(EXPR_END)), "loc_A39")
    OP_A3(0x10FD)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFF, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 77)

    label("loc_A39")

    Return()

    # Function_0_5EE end

    def Function_1_A3A(): pass

    label("Function_1_A3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_A59")
    OP_B1("E0800_7")
    Jump("loc_A88")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_A6C")
    OP_B1("E0800_4")
    Jump("loc_A88")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 0)), scpexpr(EXPR_END)), "loc_A7F")
    OP_B1("E0800_6")
    Jump("loc_A88")

    label("loc_A7F")

    OP_B1("E0800_5")

    label("loc_A88")

    Jump("loc_B64")

    label("loc_A8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 6)), scpexpr(EXPR_END)), "loc_AAA")
    OP_B1("E0800_1")
    Jump("loc_ACE")

    label("loc_AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC5")
    OP_B1("E0800_2")
    Jump("loc_ACE")

    label("loc_AC5")

    OP_B1("E0800_2")

    label("loc_ACE")

    Jump("loc_B64")

    label("loc_AD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_AF0")
    OP_B1("E0800_4")
    Jump("loc_B25")

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B08")
    OP_B1("E0800_3")
    Jump("loc_B25")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1C")
    OP_B1("E0800_2")
    Jump("loc_B25")

    label("loc_B1C")

    OP_B1("E0800_1")

    label("loc_B25")

    Jump("loc_B64")

    label("loc_B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 5)), scpexpr(EXPR_END)), "loc_B48")
    OP_B1("E0800_2y")
    Jump("loc_B58")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_END)), "loc_B58")
    OP_B1("E0800_2")

    label("loc_B58")

    Jump("loc_B64")

    label("loc_B5B")

    OP_B1("E0800_1")

    label("loc_B64")

    Return()

    # Function_1_A3A end

    def Function_2_B65(): pass

    label("Function_2_B65")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -158650, -10000, -35510, 0)
    OP_B0(0x0, 0x14)
    SetChrPos(0x8, -158650, -5000, -35510, 90)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x80)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")

    def lambda_C15():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C15)
    OP_43(0xD, 0x2, 0x0, 0x3)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_C41():
        OP_67(0, -4360, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C41)

    def lambda_C59():
        OP_6B(5920, 13000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C59)
    Sleep(2000)

    def lambda_C6E():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C6E)
    SetMessageWindowPos(250, 240, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #0 op#5
        "\x07\x00#1P#3S可恶～～～！！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(2700)

    def lambda_CCA():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CCA)
    OP_56(0x0)
    SetMapFlags(0x2000000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_B65 end

    def Function_3_D02(): pass

    label("Function_3_D02")

    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1000)
    OP_22(0x120, 0x0, 0xA)
    Return()

    # Function_3_D02 end

    def Function_4_D67(): pass

    label("Function_4_D67")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -158650, -10000, -35510, 0)
    OP_B0(0x0, 0x14)
    SetChrPos(0x8, -158650, -5000, -35510, 90)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x80)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")
    OP_43(0xD, 0x2, 0x0, 0x3)

    def lambda_E1E():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E1E)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_E43():
        OP_67(0, -4360, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E43)

    def lambda_E5B():
        OP_6B(5920, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E5B)
    Sleep(2000)

    def lambda_E70():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E70)
    Sleep(2000)

    def lambda_E90():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E90)
    FadeToDark(3000, 0, -1)
    OP_20(0xBB8)
    OP_0D()
    OP_21()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1103   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_4_D67 end

    def Function_5_EC8(): pass

    label("Function_5_EC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0xAAE60, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 10000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_F77():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F77)

    def lambda_F87():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F87)
    FadeToBright(2000, 0)

    def lambda_FA0():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FA0)
    Sleep(500)

    def lambda_FC0():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FC0)
    OP_24(0x125, 0x55)
    Sleep(500)

    def lambda_FE4():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FE4)
    OP_24(0x125, 0x5A)
    Sleep(500)

    def lambda_1008():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1008)
    OP_24(0x125, 0x5F)
    Sleep(500)

    def lambda_102C():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_102C)
    OP_24(0x125, 0x64)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_EC8 end

    def Function_6_106C(): pass

    label("Function_6_106C")

    EventBegin(0x0)
    LoadEffect(0x1, "map\\mp078_00.eff")
    LoadEffect(0x2, "monster\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-2510, 8550, -1900, 0)
    OP_67(0, 13580, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(57000, 0)
    OP_6E(860, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x0)
    ClearChrFlags(0xD, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 270)
    OP_43(0x14, 0x3, 0x0, 0x7)
    OP_A1(0xE, 0x1)
    OP_A1(0xF, 0x2)
    OP_A1(0x10, 0x3)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_11E7():
        OP_6D(10080, -10000, 12130, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11E7)

    def lambda_11FF():
        OP_67(0, 6620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11FF)

    def lambda_1217():
        OP_6B(5200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1217)

    def lambda_1227():
        OP_6C(57000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1227)

    def lambda_1237():
        OP_6E(723, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1237)
    WaitChrThread(0x101, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x3C)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x384)
    SetChrPos(0xE, 88460, -4550, 76480, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_22(0x79, 0x1, 0x50)

    def lambda_1291():
        OP_D1(254, 0, 90000, -20000, 4500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1291)

    def lambda_12AB():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_12AB)
    Sleep(4000)
    OP_24(0x79, 0x55)

    def lambda_12CF():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_12CF)
    Sleep(200)
    OP_24(0x79, 0x5A)

    def lambda_12F3():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_12F3)
    Sleep(200)
    OP_24(0x79, 0x5F)

    def lambda_1317():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1317)
    Sleep(100)
    OP_24(0x79, 0x64)

    def lambda_133B():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_133B)
    Sleep(1000)
    OP_72(0x1, 0x20)
    OP_73(0x1)

    def lambda_1363():
        OP_6D(32950, -10000, 22130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1363)
    OP_B0(0x1, 0x5A)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x3AC)
    OP_43(0xE, 0x1, 0x0, 0x9)
    Sleep(2700)
    Fade(500)
    OP_44(0x101, 0x0)
    SetChrPos(0xE, 54240, -6550, 20200, 270)
    OP_D1(14, 5000, 70000, 20000, 0)
    OP_6D(33690, -3500, 13040, 0)
    OP_67(0, 500, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(225000, 0)
    OP_6E(723, 0)
    OP_0D()
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x3C)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_43(0x0, 0x0, 0x0, 0x43)
    PlayEffect(0x1, 0x1, 0xE, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x0, 0x8)
    Sleep(2000)
    OP_72(0x1, 0x20)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_A2(0x1)
    OP_23(0x235)
    OP_44(0x0, 0x0)
    Sleep(2000)

    def lambda_1485():
        OP_6D(44940, 0, 13160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1485)

    def lambda_149D():
        OP_6C(200000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149D)

    def lambda_14AD():
        OP_6E(829, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14AD)
    OP_72(0x2, 0x4)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 701)
    OP_70(0x2, 0x384)
    SetChrPos(0xF, 93570, 14000, -1680, 270)
    OP_D1(15, 0, 90000, -20000, 0)
    OP_72(0x3, 0x4)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 701)
    OP_70(0x3, 0x384)
    SetChrPos(0x10, 85510, 5000, -36750, 270)
    OP_D1(16, 0, 90000, -40000, 0)
    OP_43(0xF, 0x1, 0x0, 0xA)

    def lambda_1544():
        OP_D1(254, -5000, 90000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1544)
    Sleep(2500)
    OP_43(0x10, 0x1, 0x0, 0xB)

    def lambda_156A():
        OP_D1(254, 0, 110000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_156A)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    Fade(500)
    OP_6D(11050, 4050, -830, 0)
    OP_67(0, 2210, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(91000, 0)
    OP_6E(829, 0)
    OP_0D()
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_43(0x0, 0x0, 0x0, 0x43)
    PlayEffect(0x1, 0x1, 0xE, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xF, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x10, 0, 1500, -5000, 110, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x0, 0x8)
    Sleep(2000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 125)
    OP_70(0x0, 0x91)
    OP_73(0x0)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 100)
    OP_70(0x0, 0x78)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)
    OP_A2(0x1)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_43(0xD, 0x3, 0x0, 0xC)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    Sleep(200)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_43(0x10, 0x3, 0x0, 0x10)
    Sleep(200)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_43(0xF, 0x3, 0x0, 0xF)
    Sleep(200)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_23(0x235)
    OP_44(0x0, 0x0)
    OP_43(0xE, 0x3, 0x0, 0xE)
    Sleep(400)
    OP_43(0x10, 0x0, 0x0, 0xD)
    Sleep(1000)
    OP_43(0xF, 0x0, 0x0, 0xD)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x0, 0xD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_6_106C end

    def Function_7_17B6(): pass

    label("Function_7_17B6")

    Sleep(900)

    label("loc_17BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17D1")
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    Jump("loc_17BB")

    label("loc_17D1")

    Return()

    # Function_7_17B6 end

    def Function_8_17D2(): pass

    label("Function_8_17D2")

    PlayEffect(0x2, 0xFF, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_180C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1851")
    PlayEffect(0x2, 0xFF, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_180C")

    label("loc_1851")

    Return()

    # Function_8_17D2 end

    def Function_9_1852(): pass

    label("Function_9_1852")


    def lambda_1858():
        OP_D1(254, 5000, 70000, 20000, 2600)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1858)

    def lambda_1872():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1872)
    Sleep(100)

    def lambda_1892():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1892)
    Sleep(100)

    def lambda_18B2():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_18B2)
    Sleep(200)

    def lambda_18D2():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_18D2)
    Sleep(300)

    def lambda_18F2():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_18F2)
    Sleep(500)

    def lambda_1912():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1912)
    Sleep(1800)

    def lambda_1932():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1932)
    Sleep(400)

    def lambda_1952():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1952)
    Sleep(300)

    def lambda_1972():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1972)
    Sleep(200)

    def lambda_1992():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1992)
    Sleep(100)

    def lambda_19B2():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_19B2)
    Return()

    # Function_9_1852 end

    def Function_10_19C8(): pass

    label("Function_10_19C8")


    def lambda_19CE():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_19CE)
    OP_72(0x2, 0x20)
    Sleep(2100)

    def lambda_19F3():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_19F3)
    OP_6F(0x2, 901)
    OP_70(0x2, 0x3AC)
    Sleep(400)

    def lambda_1A21():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A21)
    Sleep(300)

    def lambda_1A41():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A41)
    Sleep(200)

    def lambda_1A61():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A61)
    Return()

    # Function_10_19C8 end

    def Function_11_1A77(): pass

    label("Function_11_1A77")


    def lambda_1A7D():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A7D)
    OP_72(0x3, 0x20)
    Sleep(900)
    OP_6F(0x3, 901)
    OP_70(0x3, 0x3AC)
    Sleep(900)

    def lambda_1AB5():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AB5)
    Sleep(400)

    def lambda_1AD5():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AD5)
    Sleep(300)

    def lambda_1AF5():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AF5)
    Sleep(200)

    def lambda_1B15():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1B15)
    Return()

    # Function_11_1A77 end

    def Function_12_1B2B(): pass

    label("Function_12_1B2B")


    def lambda_1B31():
        OP_D1(254, 0, 270000, -50000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B31)

    def lambda_1B4B():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B4B)
    Sleep(100)

    def lambda_1B6B():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B6B)
    Sleep(100)

    def lambda_1B8B():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B8B)
    Sleep(200)

    def lambda_1BAB():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BAB)
    Sleep(200)

    def lambda_1BCB():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BCB)
    Sleep(300)

    def lambda_1BEB():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BEB)
    Return()

    # Function_12_1B2B end

    def Function_13_1C01(): pass

    label("Function_13_1C01")


    def lambda_1C07():
        OP_D1(254, 0, 90000, 30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C07)

    def lambda_1C21():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C21)
    Sleep(100)

    def lambda_1C41():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C41)
    Sleep(100)

    def lambda_1C61():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C61)
    Sleep(200)

    def lambda_1C81():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C81)
    Sleep(200)

    def lambda_1CA1():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CA1)
    Sleep(300)

    def lambda_1CC1():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CC1)
    Return()

    # Function_13_1C01 end

    def Function_14_1CD7(): pass

    label("Function_14_1CD7")

    OP_72(0x1, 0x20)
    OP_73(0x1)
    OP_6F(0x1, 940)
    OP_70(0x1, 0x385)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 900)
    OP_70(0x1, 0x2BD)
    Return()

    # Function_14_1CD7 end

    def Function_15_1D04(): pass

    label("Function_15_1D04")

    OP_72(0x2, 0x20)
    OP_73(0x2)
    OP_6F(0x2, 940)
    OP_70(0x2, 0x385)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 900)
    OP_70(0x2, 0x2BD)
    Return()

    # Function_15_1D04 end

    def Function_16_1D31(): pass

    label("Function_16_1D31")

    OP_72(0x3, 0x20)
    OP_73(0x3)
    OP_6F(0x3, 940)
    OP_70(0x3, 0x385)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 900)
    OP_70(0x3, 0x2BD)
    Return()

    # Function_16_1D31 end

    def Function_17_1D5E(): pass

    label("Function_17_1D5E")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    OP_6D(-98750, -550, -5980, 0)
    OP_67(0, 11650, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(219000, 0)
    OP_6E(905, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    OP_71(0x0, 0x4)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 90000, 0, -150000, 315)
    SetChrPos(0x10, 113500, 0, -130000, 315)
    SetChrPos(0x11, 137000, 0, -110000, 315)
    SetChrPos(0x12, 160500, 0, -90000, 315)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 135000, 0, 0)
    OP_D1(16, 0, 135000, 0, 0)
    OP_D1(17, 0, 135000, 0, 0)
    OP_D1(18, 0, 135000, 0, 0)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    FadeToBright(2000, 0)

    def lambda_1ECC():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1ECC)
    WaitChrThread(0x101, 0x0)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x384)
    Sleep(100)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 701)
    OP_70(0x3, 0x384)
    Sleep(100)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 701)
    OP_70(0x2, 0x384)
    Sleep(100)
    OP_B0(0x4, 0x3C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 701)
    OP_70(0x4, 0x384)

    def lambda_1F54():
        OP_6D(-56120, -2750, -26300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F54)

    def lambda_1F6C():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F6C)

    def lambda_1F84():
        OP_6B(7460, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F84)

    def lambda_1F94():
        OP_6C(139000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F94)

    def lambda_1FA4():
        OP_6E(905, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1FA4)
    Sleep(2000)
    OP_22(0x79, 0x1, 0x50)
    OP_43(0xF, 0x1, 0x0, 0x12)
    OP_43(0x10, 0x1, 0x0, 0x13)
    OP_43(0x11, 0x1, 0x0, 0x14)
    OP_43(0x12, 0x1, 0x0, 0x15)
    WaitChrThread(0x101, 0x0)

    def lambda_1FDF():
        OP_6D(-25590, -2750, 4840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FDF)

    def lambda_1FF7():
        OP_6C(107000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FF7)
    Sleep(2000)
    OP_44(0xF, 0x2)

    def lambda_2010():
        OP_D1(254, 0, 250000, 0, 9000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2010)
    OP_72(0x1, 0x20)
    Sleep(500)
    OP_44(0x10, 0x2)

    def lambda_2038():
        OP_D1(254, 0, 270000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2038)
    OP_72(0x2, 0x20)
    Sleep(500)
    OP_44(0x11, 0x2)

    def lambda_2060():
        OP_D1(254, 0, 270000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2060)
    OP_72(0x3, 0x20)
    Sleep(500)
    OP_44(0x12, 0x2)

    def lambda_2088():
        OP_D1(254, 0, 290000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2088)
    OP_72(0x4, 0x20)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_44(0xF, 0x3)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    OP_44(0x10, 0x3)
    SetChrPos(0x10, 0, 6000, -16000, 315)
    OP_44(0x11, 0x3)
    SetChrPos(0x11, 0, 6000, 16000, 315)
    OP_44(0x12, 0x3)
    SetChrPos(0x12, 10000, 0, 45000, 315)
    Fade(1000)
    OP_6D(-13160, -10000, -660, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(282000, 0)
    OP_6E(1343, 0)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x46)
    WaitChrThread(0x12, 0x2)
    Sleep(400)
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 901)
    OP_70(0x1, 0x3AC)
    Sleep(400)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 901)
    OP_70(0x2, 0x3AC)
    Sleep(400)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 901)
    OP_70(0x3, 0x3AC)
    Sleep(400)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 901)
    OP_70(0x4, 0x3AC)
    OP_73(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1D5E end

    def Function_18_21D4(): pass

    label("Function_18_21D4")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_21E9():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21E9)

    def lambda_2203():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2203)
    Sleep(1900)

    def lambda_2223():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2223)
    Sleep(200)

    def lambda_2243():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2243)
    Sleep(200)

    def lambda_2263():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2263)
    Sleep(100)

    def lambda_2283():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2283)
    Sleep(100)

    def lambda_22A3():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22A3)
    Return()

    # Function_18_21D4 end

    def Function_19_22B9(): pass

    label("Function_19_22B9")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_22CE():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22CE)

    def lambda_22E8():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22E8)
    Sleep(2500)

    def lambda_2308():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2308)
    Sleep(200)

    def lambda_2328():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2328)
    Sleep(200)

    def lambda_2348():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2348)
    Sleep(100)

    def lambda_2368():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2368)
    Sleep(100)

    def lambda_2388():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2388)
    Return()

    # Function_19_22B9 end

    def Function_20_239E(): pass

    label("Function_20_239E")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_23B3():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23B3)

    def lambda_23CD():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_23CD)
    Sleep(3300)

    def lambda_23ED():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_23ED)
    Sleep(200)

    def lambda_240D():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_240D)
    Sleep(200)

    def lambda_242D():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_242D)
    Sleep(100)

    def lambda_244D():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_244D)
    Sleep(100)

    def lambda_246D():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_246D)
    Return()

    # Function_20_239E end

    def Function_21_2483(): pass

    label("Function_21_2483")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_2498():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2498)

    def lambda_24B2():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_24B2)
    Sleep(4300)

    def lambda_24D2():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_24D2)
    Sleep(200)

    def lambda_24F2():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_24F2)
    Sleep(200)

    def lambda_2512():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2512)
    Sleep(100)

    def lambda_2532():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2532)
    Sleep(100)

    def lambda_2552():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2552)
    Return()

    # Function_21_2483 end

    def Function_22_2568(): pass

    label("Function_22_2568")

    EventBegin(0x0)
    LoadEffect(0x1, "map\\mp078_00.eff")
    LoadEffect(0x2, "monster\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    OP_71(0x0, 0x4)
    OP_6D(-95940, 3750, -1830, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(7300, 0)
    OP_6C(225000, 0)
    OP_6E(919, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    SetChrPos(0x10, 0, 6000, -15000, 315)
    SetChrPos(0x11, 0, 6000, 15000, 315)
    SetChrPos(0x12, 10000, 0, 45000, 315)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 280000, 0, 0)
    OP_22(0x125, 0x1, 0x50)
    OP_22(0x79, 0x1, 0x64)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_6F(0x1, 940)
    OP_6F(0x2, 940)
    OP_6F(0x3, 940)
    OP_6F(0x4, 940)
    FadeToBright(2000, 0)

    def lambda_2710():
        OP_6D(-8020, 3750, 7710, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2710)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 150000, 0, 0, 270)
    OP_72(0x0, 0x4)
    OP_D1(15, 5000, 70000, 20000, 0)
    OP_D1(16, -5000, 90000, 0, 0)
    OP_D1(17, 0, 110000, -20000, 0)
    SetChrPos(0xF, 224240, -6550, 20200, 270)
    SetChrPos(0x10, 226930, 7000, -1680, 270)
    SetChrPos(0x11, 231430, 1000, -23970, 270)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x61A80, 0x0)
    Fade(1000)
    OP_6D(168880, 3750, 210, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(6360, 0)
    OP_6C(110000, 0)
    OP_6E(916, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_23(0x125)
    OP_43(0x14, 0x3, 0x0, 0x7)
    OP_0D()
    OP_43(0x0, 0x0, 0x0, 0x43)
    PlayEffect(0x1, 0x1, 0xF, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x7, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x1, 0x0)
    PlayEffect(0x1, 0x2, 0x10, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x7, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x2, 0x0)
    OP_82(0x7, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)

    def lambda_29A4():
        OP_6D(169150, 3750, 0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29A4)

    def lambda_29BC():
        OP_67(0, 1740, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29BC)

    def lambda_29D4():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29D4)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 100)
    OP_70(0x0, 0x78)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_B0(0x0, 0x14)

    def lambda_2A1E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A1E)
    Sleep(100)

    def lambda_2A3E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A3E)
    Sleep(100)

    def lambda_2A5E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A5E)
    Sleep(200)

    def lambda_2A7E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A7E)
    Sleep(200)

    def lambda_2A9E():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A9E)
    Sleep(300)

    def lambda_2ABE():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2ABE)
    Sleep(1000)
    OP_44(0x14, 0x3)
    OP_72(0x1, 0x20)
    OP_43(0xF, 0x0, 0x0, 0x17)
    Sleep(200)
    OP_72(0x2, 0x20)
    OP_43(0x10, 0x0, 0x0, 0x17)
    Sleep(200)
    OP_72(0x3, 0x20)
    OP_43(0x11, 0x0, 0x0, 0x17)
    Sleep(3000)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFF, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_44(0xD, 0x1)
    SetChrPos(0xD, 250000, 0, 0, 270)

    def lambda_2B97():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2B97)
    OP_B0(0x0, 0xF)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    SetChrPos(0x10, 0, 6000, -15000, 315)
    SetChrPos(0x11, 0, 6000, 15000, 315)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_6F(0x1, 940)
    OP_6F(0x2, 940)
    OP_6F(0x3, 940)
    OP_6F(0x4, 940)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    Fade(1000)
    OP_6D(38580, 3750, 0, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(7300, 0)
    OP_6C(90000, 0)
    OP_6E(919, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0x125, 0x1, 0x46)
    OP_0D()

    def lambda_2CB3():
        OP_6D(38580, 3750, 0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CB3)

    def lambda_2CCB():
        OP_67(0, 1200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CCB)

    def lambda_2CE3():
        OP_6B(12530, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CE3)

    def lambda_2CF3():
        OP_6E(970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2CF3)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x41)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1300)
    FadeToDark(1000, 0, -1)
    OP_22(0x120, 0x0, 0x4B)
    Sleep(1300)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_22_2568 end

    def Function_23_2D3D(): pass

    label("Function_23_2D3D")


    def lambda_2D43():
        OP_D1(254, 20000, 90000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D43)

    def lambda_2D5D():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D5D)
    Sleep(100)

    def lambda_2D7D():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D7D)
    Sleep(100)

    def lambda_2D9D():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D9D)
    Sleep(200)

    def lambda_2DBD():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DBD)
    Sleep(300)

    def lambda_2DDD():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DDD)
    Sleep(500)

    def lambda_2DFD():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DFD)
    Return()

    # Function_23_2D3D end

    def Function_24_2E13(): pass

    label("Function_24_2E13")

    EventBegin(0x0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\mp078_00.eff")
    LoadEffect(0x2, "monster\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    OP_6D(17660, 13750, -20070, 0)
    OP_67(0, 2990, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(60000, 0)
    OP_6E(1289, 0)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 10000, 0, -45000, 90)
    SetChrPos(0x10, 0, 6000, -15000, 90)
    SetChrPos(0x11, 0, 6000, 15000, 90)
    SetChrPos(0x12, 10000, 0, 45000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 268000, 0, 0)
    OP_D1(17, 0, 272000, 0, 0)
    OP_D1(18, 0, 280000, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_B0(0x4, 0x3C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 941)
    OP_70(0x4, 0x3E8)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 150000, 4000, 0, 270)
    ClearChrFlags(0xD, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    FadeToBright(2000, 0)
    Sleep(600)
    OP_43(0x0, 0x3, 0x0, 0x43)
    PlayEffect(0x1, 0x1, 0xF, 0, 1500, -5000, 250, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x10, 0, 1500, -5000, 268, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x3, 0x11, 0, 1500, -5000, 272, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x12, 0, 1500, -5000, 290, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xD, 0x0, 0x0, 0x1A)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x0, 0x19)

    def lambda_312C():
        OP_6D(17020, 13750, 23220, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_312C)

    def lambda_3144():
        OP_6C(120000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3144)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 170)
    OP_70(0x0, 0xBE)
    OP_73(0x0)
    OP_6F(0x0, 195)
    OP_70(0x0, 0xD7)
    OP_73(0x0)
    OP_6F(0x0, 220)
    OP_70(0x0, 0xE6)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    SetChrPos(0xD, 60000, 4000, 0, 270)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_6D(63240, 6750, -2890, 0)
    OP_67(0, 2630, -10000, 0)
    OP_6B(5120, 0)
    OP_6C(120000, 0)
    OP_6E(934, 0)
    OP_0D()

    def lambda_3208():
        OP_6D(62720, 6750, 2750, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3208)

    def lambda_3220():
        OP_6B(3990, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3220)

    def lambda_3230():
        OP_6C(57000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3230)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0xD)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_73(0x0)
    OP_B0(0x0, 0xB)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0x9)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_73(0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_A2(0x1)
    OP_23(0x235)
    OP_44(0x0, 0x3)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 270)
    OP_70(0x0, 0x122)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    Fade(1000)
    OP_6D(60540, 6750, 220, 0)
    OP_67(0, -129430, -10000, 0)
    OP_6B(660, 0)
    OP_6C(90000, 0)
    OP_6E(934, 0)

    def lambda_331D():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_331D)
    OP_73(0x0)
    OP_B0(0x0, 0x2)
    OP_6F(0x0, 290)
    OP_70(0x0, 0x12C)
    Sleep(100)

    def lambda_3352():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3352)
    Sleep(100)

    def lambda_3372():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3372)
    Sleep(200)

    def lambda_3392():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3392)
    Sleep(200)

    def lambda_33B2():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_33B2)
    Sleep(300)

    def lambda_33D2():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_33D2)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0xDC, 0x0, 0x64)
    Sleep(6000)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2E13 end

    def Function_25_3418(): pass

    label("Function_25_3418")

    PlayEffect(0x2, 0x7, 0xD, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_3452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3497")
    PlayEffect(0x2, 0x7, 0xD, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_3452")

    label("loc_3497")

    Return()

    # Function_25_3418 end

    def Function_26_3498(): pass

    label("Function_26_3498")


    def lambda_349E():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_349E)
    Sleep(2500)

    def lambda_34BE():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_34BE)
    Sleep(400)

    def lambda_34DE():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_34DE)
    Sleep(300)

    def lambda_34FE():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_34FE)
    Sleep(200)

    def lambda_351E():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_351E)
    Sleep(100)

    def lambda_353E():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_353E)
    Return()

    # Function_26_3498 end

    def Function_27_3554(): pass

    label("Function_27_3554")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x3E418, 0x0)
    OP_6D(-30090, -10000, -9900, 0)
    OP_67(0, -12470, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(57000, 0)
    OP_6E(923, 0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    SetChrPos(0xF, -30000, 0, 0, 90)
    SetChrPos(0x10, -15000, 0, 25000, 90)
    SetChrPos(0x11, -15000, 0, -25000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_D1(17, 0, 90000, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_B0(0x1, 0x1E)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    OP_B0(0x3, 0x1E)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 500)
    OP_70(0x3, 0x208)
    OP_B0(0x2, 0x1E)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)
    OP_0D()
    LoadEffect(0x0, "map\\mp079_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_36D6():
        OP_6E(1100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36D6)
    PlayEffect(0x0, 0xFF, 0xFF, -35000, -35000, 0, 90, -90, 0, 10000, 10000, 10000, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(600)
    OP_43(0xF, 0x2, 0x0, 0x1D)
    OP_43(0x10, 0x2, 0x0, 0x1E)
    OP_43(0x11, 0x2, 0x0, 0x1F)
    Sleep(3000)

    def lambda_373F():
        OP_6D(-13570, 30000, -19950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_373F)

    def lambda_3757():
        OP_67(0, -10590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3757)

    def lambda_376F():
        OP_6B(2480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_376F)
    StopSound(0x4E20, 0x6F158, 0x1388)
    OP_72(0x0, 0x20)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 55)
    OP_70(0x0, 0x4B)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -25000, -55000, 0, 90)
    OP_72(0x0, 0x4)
    OP_43(0xD, 0x2, 0x0, 0x1C)

    def lambda_37C6():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_37C6)
    Sleep(1000)

    def lambda_37E6():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_37E6)
    Sleep(1000)

    def lambda_3806():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0xB3B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3806)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_3554 end

    def Function_28_3841(): pass

    label("Function_28_3841")

    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1300)
    OP_22(0x120, 0x0, 0xA)
    Return()

    # Function_28_3841 end

    def Function_29_38A1(): pass

    label("Function_29_38A1")


    def lambda_38A7():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_38A7)
    OP_D1(15, -10000, 80000, -10000, 700)
    OP_D1(15, 10000, 95000, 5000, 700)
    OP_D1(15, -5000, 85000, -5000, 800)
    OP_D1(15, 0, 90000, 0, 800)
    Return()

    # Function_29_38A1 end

    def Function_30_3909(): pass

    label("Function_30_3909")


    def lambda_390F():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_390F)
    OP_D1(16, -10000, 95000, 10000, 600)
    OP_D1(16, 5000, 80000, -10000, 600)
    OP_D1(16, -5000, 95000, 5000, 700)
    OP_D1(16, 0, 90000, 0, 700)
    Return()

    # Function_30_3909 end

    def Function_31_3971(): pass

    label("Function_31_3971")


    def lambda_3977():
        OP_91(0xFE, 0xBB8, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3977)
    OP_D1(17, 15000, 80000, -10000, 700)
    OP_D1(17, -5000, 90000, 10000, 700)
    OP_D1(17, 5000, 85000, -8000, 800)
    OP_D1(17, 0, 90000, 0, 800)
    Return()

    # Function_31_3971 end

    def Function_32_39D9(): pass

    label("Function_32_39D9")

    EventBegin(0x0)
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-20560, 20530, -22790, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(8670, 0)
    OP_6C(54000, 0)
    OP_6E(523, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 20000, 0, 20000, 90)
    SetChrPos(0x10, 20000, 0, -20000, 90)
    SetChrPos(0x11, 60000, 0, 30000, 90)
    SetChrPos(0x12, 60000, 0, -30000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_D1(17, 0, 90000, 0, 0)
    OP_D1(18, 0, 90000, 0, 0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -10000, 0, 0, 270)
    OP_48()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    OP_89(0xA, -28840, 3200, 90, 270)
    OP_89(0x9, -28240, 3200, 820, 270)
    OP_89(0xB, -27820, 3200, -1500, 270)
    OP_89(0xC, -28450, 3200, -850, 270)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_22(0x125, 0x1, 0x50)
    OP_22(0x79, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_3BDC():
        OP_6B(7490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BDC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0xC,
        (
            "#156F#5P这么久了，\x02\x03",

            "艾丝蒂尔他们\x01",
            "不要紧吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "#142F#2P该不会\x01",
            "被击败了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#176F#5P如果是那样，基库\x01",
            "应该会回来报告危机的。\x02\x03",

            "#178F现在只能信任他们继续等待了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        "#145F#2P可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#160F#5P………………………………\x02\x03",

            "#163F离黄昏还有一个小时……\x01",
            "时间一到，就开始突入。\x02\x03",

            "上尉，你先做好准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        "#175F#5P遵命……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #7
        "\x07\x05#3S不用了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0xB,
        "#143F#2P什、什么声音！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "#178F#5P刚才那是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        "#161F#5P从哪儿传来的！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0xC,
        (
            "#153F#5P咦～？\x02\x03",

            "好像有什么庞然大物\x01",
            "从下面飞上来了哦～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "#173F#5P什么！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-73960, 11720, -1060, 0)
    OP_67(0, 7820, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(311000, 0)
    OP_6E(901, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -130000, -30000, 0, 90)
    OP_6F(0x0, 55)
    OP_70(0x0, 0x4B)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, 15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, -15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xD, 0x3, 0x0, 0x21)
    Sleep(200)
    OP_43(0xD, 0x0, 0x0, 0x22)
    OP_75(0x0, 0xD, 0x7)
    Sleep(3000)
    Fade(500)
    OP_6D(-6420, 12220, -23160, 0)
    OP_67(0, 1380, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(290000, 0)
    OP_6E(528, 0)
    WaitChrThread(0xD, 0x0)
    OP_72(0x0, 0x20)
    OP_73(0x0)

    def lambda_407F():
        OP_6B(10, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_407F)

    def lambda_408F():
        OP_67(0, 500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408F)

    def lambda_40A7():
        OP_6E(360, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40A7)
    OP_6F(0x0, 76)
    OP_70(0x0, 0x5F)
    OP_73(0x0)
    OP_6F(0x0, 170)
    OP_70(0x0, 0xC3)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 195)
    OP_70(0x0, 0xD7)
    Sleep(1500)
    SetMessageWindowPos(230, 280, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #13
        (
            "\x07\x05所有守护利贝尔的\x01",
            "士兵们请听着。\x02\x03",

            "我名叫『雷格纳特』。\x01",
            "是自古沉眠于此地的龙之眷族。\x02\x03",

            "之前虽然被恶人所控制，\x01",
            "不过现已被游击士们解救。\x02\x03",

            "详细情况请向他们询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x20)
    OP_73(0x0)

    def lambda_41C1():
        OP_67(0, -1000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41C1)

    def lambda_41D9():
        OP_91(0xFE, 0x186A0, 0x186A0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_41D9)
    OP_6F(0x0, 575)
    OP_70(0x0, 0x258)

    def lambda_4202():
        OP_8C(0xD, 315, 100)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4202)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 600)
    OP_70(0x0, 0x26C)
    OP_43(0xD, 0x0, 0x0, 0x23)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(-120890, 30000, 45390, 0)
    OP_67(0, 34330, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(125000, 0)
    OP_6E(1200, 0)
    OP_0D()

    def lambda_4275():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4275)
    Sleep(6000)
    Fade(500)
    OP_44(0xD, 0x3)
    OP_6D(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(1000)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0x9)
    Sleep(500)

    ChrTalk(    #14
        0xA,
        "#161F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "#153F#5P啊啊……\x01",
            "已经看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "#143F#2P请问……\x01",
            "我们不用追上去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#176F#5P……到了那种高度\x01",
            "我们就束手无策了。\x02\x03",

            "就算『埃尔赛尤』能上去，\x01",
            "我们也会窒息的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "#163F#5P真没办法……\x02\x03",

            "#165F这下可要彻彻底底\x01",
            "向他们问个清楚才行啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x50)
    OP_24(0x125, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    OP_24(0x125, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    OP_24(0x125, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    OP_24(0x125, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(200)
    OP_23(0x79)
    OP_23(0x125)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05就这样，扰乱柏斯地区平静的\x01",
            "古代龙骚动终于顺利落幕了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05艾丝蒂尔一行人则向摩尔根将军\x01",
            "报告了整个事件的详细经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05在好不容易解脱之后，\x01",
            "他们便将龙托付的金耀石结晶\x01",
            "分别送交了市长和村长。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05然后，一个星期过去了──\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_39D9 end

    def Function_33_45CB(): pass

    label("Function_33_45CB")

    Sleep(200)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1600)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1800)

    label("loc_460C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4622")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_460C")

    label("loc_4622")

    Return()

    # Function_33_45CB end

    def Function_34_4623(): pass

    label("Function_34_4623")


    def lambda_4629():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4629)
    Sleep(900)

    def lambda_4649():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4649)
    Sleep(800)

    def lambda_4669():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4669)
    Sleep(700)

    def lambda_4689():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4689)
    Sleep(500)

    def lambda_46A9():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46A9)
    Sleep(400)

    def lambda_46C9():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46C9)
    Sleep(300)

    def lambda_46E9():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46E9)
    WaitChrThread(0xD, 0x1)
    Return()

    # Function_34_4623 end

    def Function_35_4704(): pass

    label("Function_35_4704")


    def lambda_470A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_470A)
    Sleep(200)

    def lambda_472A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_472A)
    Sleep(200)

    def lambda_474A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_474A)
    Sleep(200)

    def lambda_476A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_476A)
    Sleep(200)

    def lambda_478A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_478A)
    Sleep(200)

    def lambda_47AA():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47AA)
    Sleep(200)

    def lambda_47CA():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47CA)
    Sleep(200)

    def lambda_47EA():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47EA)
    Sleep(200)

    def lambda_480A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_480A)
    Sleep(200)

    def lambda_482A():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_482A)
    Return()

    # Function_35_4704 end

    def Function_36_4840(): pass

    label("Function_36_4840")


    def lambda_4846():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x61A8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4846)
    Sleep(200)

    def lambda_4866():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFF9E58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4866)
    Sleep(500)

    def lambda_4886():
        OP_8F(0xFE, 0xFFFF2928, 0x0, 0x61A8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4886)
    Sleep(200)

    def lambda_48A6():
        OP_8F(0xFE, 0xFFFF2928, 0x0, 0xFFFF9E58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_48A6)
    WaitChrThread(0xF, 0x1)

    def lambda_48C6():
        OP_D1(254, 0, 45000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_48C6)
    WaitChrThread(0x10, 0x1)

    def lambda_48E5():
        OP_D1(254, 0, 135000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_48E5)
    WaitChrThread(0x11, 0x1)

    def lambda_4904():
        OP_D1(254, 0, 135000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4904)
    WaitChrThread(0x12, 0x1)

    def lambda_4923():
        OP_D1(254, 0, 45000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4923)
    Return()

    # Function_36_4840 end

    def Function_37_4938(): pass

    label("Function_37_4938")

    EventBegin(0x0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE2, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "monster\\\\msc0331.eff")
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    LoadEffect(0x2, "map\\mp078_01.eff")
    OP_6D(-1460, 0, -1110, 0)
    OP_67(0, 6600, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(315000, 0)
    OP_6E(416, 0)
    OP_D0(360000, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x0)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xE, 0, -5000, 0, 270)
    SetChrPos(0x10, 136000, -5000, -50000, 270)
    SetChrPos(0x11, 136000, -5000, -50000, 270)
    SetChrPos(0x12, 136000, -5000, -50000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 30000, 0)
    OP_D1(17, 0, 270000, 30000, 0)
    OP_D1(18, 0, 270000, 30000, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x64)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    FadeToBright(1000, 0)

    def lambda_4B33():
        OP_6D(-520, 0, -2050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B33)

    def lambda_4B4B():
        OP_67(0, 2770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B4B)
    WaitChrThread(0x101, 0x0)
    OP_43(0xE, 0x0, 0x0, 0x29)

    def lambda_4B6F():
        OP_6D(-1790, 0, -9260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B6F)

    def lambda_4B87():
        OP_67(0, 2060, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B87)

    def lambda_4B9F():
        OP_6C(280000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B9F)

    def lambda_4BAF():
        OP_D0(365000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4BAF)
    Sleep(4000)

    def lambda_4BC4():
        OP_67(0, 6060, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4BC4)

    def lambda_4BDC():
        OP_6C(75000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BDC)

    def lambda_4BEC():
        OP_D0(350000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BEC)
    WaitChrThread(0x101, 0x0)

    def lambda_4C01():
        OP_67(0, 2060, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C01)
    WaitChrThread(0x101, 0x0)
    PlayEffect(0x2, 0x0, 0x10, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x11, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x12, 0, 1000, -11500, 183, 0, -26, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0x0)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x1388)
    OP_43(0x0, 0x0, 0x0, 0x43)

    def lambda_4CE4():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4CE4)
    Sleep(1000)

    def lambda_4CF9():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_4CF9)
    Sleep(1000)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0x1388)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x2710)

    def lambda_4D38():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4D38)
    Sleep(1000)

    def lambda_4D4D():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4D4D)
    Sleep(1000)
    OP_98(0x0, 0x12)
    OP_98(0x1, 0xC350, 0xFFFFEC78, 0xFFFFEC78)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFEC78, 0x0)

    def lambda_4D8C():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4D8C)
    Sleep(500)

    def lambda_4DA1():
        OP_D1(254, 0, 270000, -30000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_4DA1)
    Sleep(2500)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_24(0x235, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    SetChrPos(0xE, -25000, 0, 0, 270)
    SetChrPos(0x10, 125000, -6000, 0, 270)
    SetChrPos(0x11, 135000, -2000, 15000, 270)
    SetChrPos(0x12, 135000, -8000, -15000, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 10000, 0)
    OP_D1(18, 0, 270000, -10000, 0)
    OP_B0(0x0, 0x3C)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(88140, -3850, 0, 0)
    OP_67(0, 2000, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(282000, 0)
    OP_6E(1045, 0)
    OP_D0(365000, 0)
    PlayEffect(0x2, 0x0, 0x10, -800, 1500, -12000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x11, 500, 500, -11000, 180, 2, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x12, 700, 400, -12000, 182, 3, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(500, 0)

    def lambda_4FBA():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4FBA)

    def lambda_4FD5():
        OP_8F(0xFE, 0xC350, 0xFFFFE890, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4FD5)

    def lambda_4FF0():
        OP_8F(0xFE, 0xD6D8, 0xFFFFF830, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FF0)

    def lambda_500B():
        OP_8F(0xFE, 0xD6D8, 0xFFFFE0C0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_500B)
    OP_43(0x0, 0x0, 0x0, 0x43)
    Sleep(6000)

    def lambda_5032():
        OP_6C(306000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5032)
    OP_82(0x2, 0x0)
    OP_82(0x5, 0x0)
    OP_43(0x12, 0x0, 0x0, 0x26)
    Sleep(1500)
    PlayEffect(0x1, 0xFF, 0xFF, 95000, -5000, -15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x4, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)
    OP_43(0x10, 0x0, 0x0, 0x2E)
    Sleep(1000)
    Fade(500)
    OP_6D(430, -3850, 8540, 0)
    OP_6C(29000, 0)
    OP_D0(360000, 0)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    SetChrPos(0x10, 100000, -8000, 0, 270)
    SetChrPos(0x11, 105000, -6000, 15000, 270)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)

    def lambda_5125():
        OP_D1(254, 0, 245000, 20000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_5125)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0x8AD4, 0x0, 0x689C)
    OP_98(0x1, 0xFFFF88B4, 0x0, 0x30C)

    def lambda_515F():
        OP_98(0x2, 0xFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_515F)

    def lambda_516F():
        OP_D1(254, 0, 235000, 20000, 8000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_516F)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0x9E5C, 0x0, 0xB6BC)
    OP_98(0x1, 0xFFFFAFC4, 0x0, 0x3DA4)

    def lambda_51A9():
        OP_98(0x2, 0xFE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_51A9)

    def lambda_51B9():
        OP_6D(6320, -2850, 15060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_51B9)

    def lambda_51D1():
        OP_6C(54000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51D1)

    def lambda_51E1():
        OP_D0(380000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51E1)

    def lambda_51F1():
        OP_67(0, 3150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_51F1)
    SetChrPos(0xE, 0, 0, 0, 270)

    def lambda_521A():
        OP_D1(254, 0, 290000, 35000, 100)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_521A)
    OP_43(0xE, 0x0, 0x0, 0x2A)
    WaitChrThread(0xE, 0x3)

    def lambda_5240():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5240)
    Sleep(1000)

    def lambda_525F():
        OP_D1(254, 0, 250000, -35000, 1400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_525F)
    OP_43(0xE, 0x0, 0x0, 0x2B)
    WaitChrThread(0xE, 0x3)

    def lambda_5285():
        OP_D1(254, 0, 270000, 0, 6000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5285)
    Sleep(2000)
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x43)
    PlayEffect(0x2, 0x0, 0x10, 0, 1000, -12000, 160, 3, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x2, 0x1, 0x11, 1300, 1200, -12000, 152, 0, -30, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_5324():
        OP_6D(-27950, -3850, -25800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5324)

    def lambda_533C():
        OP_6C(125000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_533C)

    def lambda_534C():
        OP_67(0, 3800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_534C)

    def lambda_5364():
        OP_D0(340000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5364)

    def lambda_5374():
        OP_D1(254, 0, 270000, 20000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5374)
    OP_43(0xE, 0x0, 0x0, 0x2D)
    WaitChrThread(0x101, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x2, 0x4)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_72(0x3, 0x4)
    PlayEffect(0x2, 0x0, 0x10, 500, 1000, -12000, 150, 0, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0x1, 0x11, 500, 1000, -12000, 130, 0, -30, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    SetChrPos(0x12, 8000, -4000, -56000, 270)
    OP_71(0x4, 0x4)
    OP_D1(18, -5000, 300000, -30000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -17000, -5000, -41000, 280, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_72(0x4, 0x4)
    PlayEffect(0x2, 0x3, 0x12, 500, 1000, -9000, 210, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x12, 0x0, 0x0, 0x28)
    Sleep(2000)
    OP_43(0xE, 0x0, 0x0, 0x2C)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4938 end

    def Function_38_550B(): pass

    label("Function_38_550B")


    def lambda_5511():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_5511)

    def lambda_552B():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_552B)
    Sleep(700)

    def lambda_554B():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_554B)
    Sleep(600)

    def lambda_556B():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_556B)
    Sleep(500)

    def lambda_558B():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_558B)
    Sleep(400)

    def lambda_55AB():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_55AB)
    Sleep(300)

    def lambda_55CB():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_55CB)
    Sleep(200)

    def lambda_55EB():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_55EB)
    Sleep(100)

    def lambda_560B():
        OP_8F(0xFE, 0xD6D8, 0xFFFF8AD0, 0xFFFFC568, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_560B)
    Return()

    # Function_38_550B end

    def Function_39_5621(): pass

    label("Function_39_5621")


    def lambda_5627():
        OP_D1(254, 0, 300000, -20000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_5627)

    def lambda_5641():
        OP_8F(0xFE, 0x61A8, 0xFFFFF830, 0xFFFFB1E0, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5641)
    Sleep(1500)

    def lambda_5661():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5661)
    Return()

    # Function_39_5621 end

    def Function_40_5677(): pass

    label("Function_40_5677")


    def lambda_567D():
        OP_8F(0xFE, 0xBB8, 0xFFFFF830, 0xFFFF38C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_567D)
    Sleep(2500)

    def lambda_569D():
        OP_D1(254, -10000, 300000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_569D)

    def lambda_56B7():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_56B7)
    Sleep(200)

    def lambda_56D7():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_56D7)
    Sleep(200)

    def lambda_56F7():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_56F7)
    Sleep(200)

    def lambda_5717():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5717)
    Sleep(200)

    def lambda_5737():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5737)
    Sleep(200)

    def lambda_5757():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5757)
    Sleep(200)

    def lambda_5777():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5777)
    Sleep(200)

    def lambda_5797():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5797)
    Sleep(200)

    def lambda_57B7():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFFF060, 0x11170, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_57B7)
    Return()

    # Function_40_5677 end

    def Function_41_57CD(): pass

    label("Function_41_57CD")


    def lambda_57D3():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_57D3)

    def lambda_57ED():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57ED)
    Sleep(200)

    def lambda_580D():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_580D)
    Sleep(200)

    def lambda_582D():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_582D)
    Sleep(200)

    def lambda_584D():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_584D)
    Sleep(200)

    def lambda_586D():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_586D)
    Sleep(200)

    def lambda_588D():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_588D)
    Sleep(200)

    def lambda_58AD():
        OP_8F(0xFE, 0xFFFB6C20, 0xFFFFEC78, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58AD)
    Return()

    # Function_41_57CD end

    def Function_42_58C3(): pass

    label("Function_42_58C3")


    def lambda_58C9():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_58C9)
    Sleep(300)

    def lambda_58E9():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_58E9)
    Sleep(100)

    def lambda_5909():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5909)
    Sleep(100)

    def lambda_5929():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5929)
    Return()

    # Function_42_58C3 end

    def Function_43_593F(): pass

    label("Function_43_593F")


    def lambda_5945():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5945)
    Sleep(100)

    def lambda_5965():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5965)
    Sleep(100)

    def lambda_5985():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5985)
    Sleep(100)

    def lambda_59A5():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_59A5)
    Sleep(100)

    def lambda_59C5():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x2328, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_59C5)
    Sleep(600)

    def lambda_59E5():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_59E5)
    Sleep(100)

    def lambda_5A05():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A05)
    Sleep(100)

    def lambda_5A25():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A25)
    Sleep(100)

    def lambda_5A45():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A45)
    Sleep(100)

    def lambda_5A65():
        OP_8F(0xFE, 0xFFFFF448, 0xFFFFF060, 0x1770, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A65)
    Return()

    # Function_43_593F end

    def Function_44_5A7B(): pass

    label("Function_44_5A7B")


    def lambda_5A81():
        OP_D1(254, 0, 250000, -40000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_5A81)

    def lambda_5A9B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A9B)
    Sleep(200)

    def lambda_5ABB():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5ABB)
    Sleep(200)

    def lambda_5ADB():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5ADB)
    Sleep(200)

    def lambda_5AFB():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5AFB)
    Sleep(200)

    def lambda_5B1B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B1B)
    Sleep(200)

    def lambda_5B3B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B3B)
    Sleep(200)

    def lambda_5B5B():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0xEA60, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B5B)
    Return()

    # Function_44_5A7B end

    def Function_45_5B71(): pass

    label("Function_45_5B71")


    def lambda_5B77():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B77)
    Sleep(200)

    def lambda_5B97():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5B97)
    Sleep(200)

    def lambda_5BB7():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5BB7)
    Sleep(200)

    def lambda_5BD7():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5BD7)
    Sleep(3600)

    def lambda_5BF7():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5BF7)
    Sleep(200)

    def lambda_5C17():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C17)
    Sleep(200)

    def lambda_5C37():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C37)
    Sleep(200)

    def lambda_5C57():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C57)
    Sleep(200)

    def lambda_5C77():
        OP_8F(0xFE, 0xFFFF7748, 0xFFFFF060, 0xFFFFC568, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C77)
    Return()

    # Function_45_5B71 end

    def Function_46_5C8D(): pass

    label("Function_46_5C8D")

    PlayEffect(0x0, 0x0, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -5000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x1, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, 5000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x2, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, 0, 10000, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, 10000, 0)
    Sleep(500)
    PlayEffect(0x0, 0x4, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -14000, -4000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -12000, -6000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x6, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -14000, -12000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x7, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -16000, -20000, 0)
    Return()

    # Function_46_5C8D end

    def Function_47_5E59(): pass

    label("Function_47_5E59")

    PlayEffect(0x0, 0x0, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x1, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, 5000, 0)
    Return()

    # Function_47_5E59 end

    def Function_48_5EC9(): pass

    label("Function_48_5EC9")

    Sleep(600)
    PlayEffect(0x0, 0x2, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, 10000, 0)
    Return()

    # Function_48_5EC9 end

    def Function_49_5F3E(): pass

    label("Function_49_5F3E")

    PlayEffect(0x0, 0x4, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, -4000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x10, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -6000, 0)
    Return()

    # Function_49_5F3E end

    def Function_50_5FAE(): pass

    label("Function_50_5FAE")

    Sleep(600)
    PlayEffect(0x0, 0x6, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -4000, -8000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x7, 0x11, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -6000, -10000, 0)
    Return()

    # Function_50_5FAE end

    def Function_51_6023(): pass

    label("Function_51_6023")

    Sleep(1400)
    PlayEffect(0x0, 0x5, 0x12, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0xE, -50000, -2000, -6000, 0)
    Return()

    # Function_51_6023 end

    def Function_52_605E(): pass

    label("Function_52_605E")

    EventBegin(0x0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\\\mpsmk0.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    OP_6D(81300, -9500, 23840, 0)
    OP_67(0, 4140, -10000, 0)
    OP_6B(5040, 0)
    OP_6C(71000, 0)
    OP_6E(869, 0)
    OP_D0(360000, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 250000, 10000, 15000, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0x10, 50000, 0, 0, 270)
    SetChrPos(0x11, 60000, 0, 15000, 270)
    SetChrPos(0x12, 60000, 0, -15000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x4, 0x4)
    OP_22(0x79, 0x1, 0x5A)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x11, 0x0, 0x0, 0x35)
    Sleep(3700)
    PlayEffect(0x2, 0xFF, 0xFF, 45000, -5000, 15000, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x11, 0x1)
    OP_72(0x1, 0x4)
    SetMapFlags(0x10)

    def lambda_6302():
        OP_6D(50100, -8000, 13150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6302)

    def lambda_631A():
        OP_67(0, 2880, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_631A)

    def lambda_6332():
        OP_D0(355000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6332)

    def lambda_6342():
        OP_D1(254, 0, 270000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_6342)
    OP_98(0x0, 0xF)
    OP_98(0x1, 0x249F0, 0xFFFFE0C0, 0x3A98)
    OP_98(0x1, 0xC350, 0xFFFFE0C0, 0x3A98)
    OP_98(0x1, 0xFFFF3CB0, 0xFFFFE0C0, 0x3A98)

    def lambda_638A():
        OP_98(0x2, 0xFE, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_638A)
    Sleep(4800)
    OP_44(0xF, 0x1)
    Fade(1000)
    OP_6D(30780, -300, 10150, 0)
    OP_6B(2410, 0)
    OP_6C(50000, 0)
    OP_6E(869, 0)
    SetChrPos(0xE, 10000, 0, 0, 270)
    OP_D1(14, 0, 270000, -10000, 0)
    SetChrPos(0xF, 100000, -4000, 30000, 270)
    OP_D1(15, 0, 270000, 0, 0)

    def lambda_641C():
        OP_6D(-9720, 3450, 2950, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_641C)

    def lambda_6434():
        OP_6C(47000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6434)

    def lambda_6444():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6444)

    def lambda_645F():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_645F)

    def lambda_6479():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6479)
    Sleep(1500)

    def lambda_6499():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6499)
    Sleep(400)

    def lambda_64B9():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_64B9)
    Sleep(400)

    def lambda_64D9():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_64D9)
    Sleep(400)

    def lambda_64F9():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_64F9)
    Sleep(400)

    def lambda_6519():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6519)
    Sleep(400)

    def lambda_6539():
        OP_8F(0xFE, 0x0, 0xFFFFF060, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6539)
    Sleep(400)

    def lambda_6559():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF060, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6559)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_52_605E end

    def Function_53_6590(): pass

    label("Function_53_6590")

    PlayEffect(0x1, 0x0, 0x11, 0, -5000, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1000, -3000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_6600():
        OP_91(0xFE, 0x7D0, 0xFFFFFC18, 0x7D0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6600)
    OP_D1(254, 5000, 274000, 5000, 200)
    OP_D1(254, 5000, 270000, 0, 300)
    OP_D1(254, 5000, 272000, 3000, 300)
    PlayEffect(0x1, 0x1, 0x11, 0, -5000, 3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 0, 3000, 4000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_66BE():
        OP_91(0xFE, 0xFFFFFC18, 0xFFFFFC18, 0xFFFFF830, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66BE)
    OP_D1(254, 8000, 262000, -8000, 200)
    OP_D1(254, 2000, 268000, 0, 300)
    OP_D1(254, 6000, 264000, -6000, 300)
    PlayEffect(0x1, 0x2, 0x11, -6000, -2000, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x11, 2000, -2000, -1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_677C():
        OP_91(0xFE, 0x3E8, 0xFFFFF060, 0x3E8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_677C)
    OP_D1(254, 8000, 284000, 10000, 200)
    OP_D1(254, 5000, 270000, -4000, 200)
    OP_D1(254, 7000, 280000, 6000, 200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_67D9():
        OP_6D(50100, -10000, 13150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_67D9)

    def lambda_67F1():
        OP_67(0, 8029, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67F1)

    def lambda_6809():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6809)

    def lambda_6819():
        OP_D1(254, 7000, 280000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6819)

    def lambda_6833():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6833)
    Sleep(500)

    def lambda_6853():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6853)
    Sleep(400)

    def lambda_6873():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6873)
    Sleep(300)

    def lambda_6893():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6893)
    Sleep(200)

    def lambda_68B3():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68B3)
    Sleep(100)

    def lambda_68D3():
        OP_8F(0xFE, 0xEA60, 0xFFFF8AD0, 0x3A98, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68D3)
    Return()

    # Function_53_6590 end

    def Function_54_68E9(): pass

    label("Function_54_68E9")

    EventBegin(0x0)
    OP_A1(0xE, 0x0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    SetChrPos(0xF, 150000, -2000, 8000, 270)
    SetChrPos(0xE, 150000, 0, -8000, 270)
    SetChrPos(0x10, 300000, 0, -9300, 270)
    SetChrPos(0x11, 300000, 0, 6700, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x4)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-68280, 2400, -1300, 0)
    OP_67(0, 2170, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(90000, 0)
    OP_6E(869, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF1, 0xFFFFFFFA, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_6A8F():
        OP_67(0, -2830, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A8F)
    OP_43(0xE, 0x0, 0x0, 0x37)
    OP_43(0xF, 0x0, 0x0, 0x38)
    OP_43(0x10, 0x0, 0x0, 0x39)
    OP_43(0x11, 0x0, 0x0, 0x3A)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_20(0xBB8)
    OP_21()
    Sleep(6000)
    OP_1D(0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0xE, 0, 0, 0, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x5A)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_6D(-13440, -10000, -2430, 0)
    OP_67(0, 11980, -10000, 0)
    OP_6B(10090, 0)
    OP_6C(250000, 0)
    OP_6E(473, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    FadeToBright(2000, 0)

    def lambda_6BDD():
        OP_67(0, 12960, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6BDD)

    def lambda_6BF5():
        OP_6B(5620, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BF5)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0xE, 40000, 0, 0, 270)

    def lambda_6C1B():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6C1B)
    Fade(1000)
    OP_6D(24340, -10000, -15770, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(8039, 0)
    OP_6C(118000, 0)
    Sleep(10000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_54_68E9 end

    def Function_55_6C86(): pass

    label("Function_55_6C86")


    def lambda_6C8C():
        OP_D1(254, 0, 260000, 30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6C8C)

    def lambda_6CA6():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0xFFFFE0C0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CA6)
    WaitChrThread(0xFE, 0x1)

    def lambda_6CC6():
        OP_D1(254, 0, 250000, 40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6CC6)
    OP_97(0xFE, 0xFFFF3CB0, 0xFFFF63C0, 0xFFFEA070, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xC350, 0x0)
    Return()

    # Function_55_6C86 end

    def Function_56_6D04(): pass

    label("Function_56_6D04")


    def lambda_6D0A():
        OP_D1(254, 0, 280000, -30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6D0A)

    def lambda_6D24():
        OP_8F(0xFE, 0xFFFF3CB0, 0xFFFFF830, 0x1F40, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D24)
    WaitChrThread(0xFE, 0x1)

    def lambda_6D44():
        OP_D1(254, 0, 290000, -40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6D44)
    OP_97(0xFE, 0xFFFF3CB0, 0x9C40, 0x15F90, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0x186A0, 0xC350, 0x0)
    Return()

    # Function_56_6D04 end

    def Function_57_6D82(): pass

    label("Function_57_6D82")


    def lambda_6D88():
        OP_D1(254, 0, 260000, 30000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6D88)

    def lambda_6DA2():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0xFFFFDBAC, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DA2)
    WaitChrThread(0xFE, 0x1)

    def lambda_6DC2():
        OP_D1(254, 0, 250000, 40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6DC2)
    OP_97(0xFE, 0xFFFF3CB0, 0xFFFF5EAC, 0xFFFEA070, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xC350, 0x0)
    Return()

    # Function_57_6D82 end

    def Function_58_6E00(): pass

    label("Function_58_6E00")


    def lambda_6E06():
        OP_D1(254, 0, 280000, -30000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6E06)

    def lambda_6E20():
        OP_8F(0xFE, 0xFFFF3CB0, 0x0, 0x1A2C, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E20)
    WaitChrThread(0xFE, 0x1)

    def lambda_6E40():
        OP_D1(254, 0, 290000, -40000, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6E40)
    OP_97(0xFE, 0xFFFF3CB0, 0x972C, 0x15F90, 0xA410, 0x0)
    OP_8F(0xFE, 0xFFFE7960, 0x0, 0x186A0, 0xC350, 0x0)
    Return()

    # Function_58_6E00 end

    def Function_59_6E7E(): pass

    label("Function_59_6E7E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopSound(0x4E20, 0xC3500, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 400)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x46)
    OP_A1(0xF, 0x1)
    SetChrPos(0xF, 10000, 20000, 0, 270)

    def lambda_6F2A():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F2A)

    def lambda_6F3A():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F3A)
    FadeToBright(2000, 0)

    def lambda_6F53():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6F53)
    Sleep(500)

    def lambda_6F73():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6F73)
    Sleep(500)

    def lambda_6F93():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6F93)
    Sleep(500)

    def lambda_6FB3():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6FB3)
    Sleep(500)

    def lambda_6FD3():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6FD3)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_59_6E7E end

    def Function_60_700A(): pass

    label("Function_60_700A")

    EventBegin(0x0)
    StopSound(0x4E20, 0xC3500, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 400)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x64)
    OP_A1(0xF, 0x1)
    SetChrPos(0xF, -79470, -30000, -91440, 270)
    OP_6D(-98020, -10000, -92900, 0)
    OP_67(0, -6950, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(232000, 0)
    OP_6E(854, 0)
    FadeToBright(1000, 0)

    def lambda_70C9():
        OP_6D(-101640, -10000, -90970, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70C9)

    def lambda_70E1():
        OP_67(0, -8000, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_70E1)

    def lambda_70F9():
        OP_6B(7000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_70F9)
    OP_43(0xF, 0x0, 0x0, 0x3D)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_60_700A end

    def Function_61_712C(): pass

    label("Function_61_712C")


    def lambda_7132():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7132)
    Sleep(500)

    def lambda_7152():
        OP_8F(0xFE, 0xFFFCF20C, 0x186A0, 0xFFFE9A8A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7152)
    Sleep(500)

    def lambda_7172():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7172)
    Sleep(500)

    def lambda_7192():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7192)
    Sleep(500)

    def lambda_71B2():
        OP_8F(0xFE, 0xFFFCE654, 0x186A0, 0xFFFE9A8A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_71B2)
    WaitChrThread(0xF, 0x1)
    Return()

    # Function_61_712C end

    def Function_62_71CD(): pass

    label("Function_62_71CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0x1B, 0x7)
    SetChrPos(0xE, 0, 0, 0, 270)
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x4)
    OP_48()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-32090, 3430, -1640, 0)
    OP_67(0, 8860, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(311000, 0)
    OP_6E(515, 0)
    OP_22(0x1C3, 0x0, 0x64)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    OP_89(0x1A, 3260, 3600, -510, 0)
    OP_89(0x1B, 3310, 3600, 1000, 0)
    SetChrChipByIndex(0x1A, 10)
    SetChrSubChip(0x1A, 0)
    SetChrFlags(0x1A, 0x800)
    ClearChrFlags(0x1A, 0x1)
    OP_22(0x79, 0x1, 0x3C)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    LoadEffect(0x0, "map\\mp061_00.eff")
    LoadEffect(0x1, "map\\mp085_00.eff")
    LoadEffect(0x2, "battle\\mgaria0.eff")
    LoadEffect(0x3, "map\\mp085_01.eff")

    def lambda_7323():
        OP_6D(3000, 3450, -220, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7323)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(2780, 3510, 470, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x1A,
        (
            "#1154F#6P──时机已经成熟。\x02\x03",

            "#1150F从现在起，『福音计划』\x01",
            "正式进入第三阶段。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)

    def lambda_73EE():
        OP_99(0x1A, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_73EE)
    PlayEffect(0x2, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_743D():
        OP_99(0x1A, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_743D)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)

    def lambda_745A():
        OP_99(0x1A, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_745A)
    Sleep(1000)
    Fade(500)
    OP_6D(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 6)

    def lambda_74C1():
        OP_99(0x1A, 0x0, 0x9, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_74C1)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    WaitChrThread(0x1A, 0x0)
    Sleep(500)

    ChrTalk(    #24
        0x1A,
        (
            "#1151F#5P被封印在七耀之力无法到达\x01",
            "的黑暗夹缝中的『环』啊──\x02\x03",

            "望汝通过『福音』，\x01",
            "再度重现于世间吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x1B, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_20(0x7D0)
    Sleep(100)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_23(0x1C3)
    OP_21()
    OP_1D(0x70)
    Sleep(500)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(2420, 6690, 3310, 0)
    OP_67(0, 1830, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ClearChrFlags(0x1A, 0x800)
    OP_0D()

    def lambda_762E():
        OP_67(0, 700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_762E)

    def lambda_7646():
        OP_6D(2420, 8690, 3310, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7646)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0x1)
    PlayEffect(0x1, 0x1, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x0, 0x64)
    Sleep(2000)
    Sleep(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    OP_82(0x1, 0x0)
    SetChrFlags(0x1A, 0x800)
    OP_0D()
    OP_99(0x1A, 0x9, 0x0, 0x7D0)
    Sleep(500)

    ChrTalk(    #25
        0x1A,
        (
            "#1155F#5P看吧！\x01",
            "耸立在四方的『桩』！\x02\x03",

            "它们便是将你封锁在\x01",
            "黑暗深处的最后束缚！\x02\x03",

            "如今它已在人类的伪装下\x01",
            "以虚假的形态留存于世，\x02\x03",

            "就用你那支配万物的神圣之手，\x01",
            "将一切真相揭露出来吧！\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x1, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(1500)
    OP_6D(2420, 8690, 3310, 0)
    OP_67(0, 700, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ClearChrFlags(0x1A, 0x800)
    OP_0D()
    PlayEffect(0x3, 0x2, 0xFF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x0, 0x64)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_62_71CD end

    def Function_63_78AB(): pass

    label("Function_63_78AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS240._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS241._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS240._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, -36000, -110000, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, -36000, -110000, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, -36000, -110000, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -160000, 0, 1000)
    OP_C6(0x2, 0x0, -160000, 0, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Call(0, 71)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_63_78AB end

    def Function_64_7A98(): pass

    label("Function_64_7A98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS242._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS243._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS242._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, -125000, 0, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, -125000, 0, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, -125000, 0, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -90000, -110000, 1000)
    OP_C6(0x2, 0x0, -90000, -110000, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Call(0, 72)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FB)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_64_7A98 end

    def Function_65_7C7F(): pass

    label("Function_65_7C7F")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToDark(0, 0, -1)
    Call(0, 73)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FD)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_65_7C7F end

    def Function_66_7CBB(): pass

    label("Function_66_7CBB")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp078_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-37160, -10000, -21180, 0)
    OP_67(0, -10620, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(31000, 0)
    OP_6E(619, 0)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, 38760, -10000, -14790, 270)
    OP_A1(0xF, 0x2)
    SetChrPos(0xF, 50390, -10000, 4970, 90)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, 70850, -10000, -32060, 90)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 90000, 10000, 0)
    OP_D1(16, 0, 90000, -10000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 700)
    OP_70(0x1, 0x30C)

    def lambda_7DD3():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7DD3)
    Sleep(2000)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 470)
    OP_70(0x2, 0x23A)
    Sleep(100)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 470)
    OP_70(0x3, 0x23A)

    def lambda_7E26():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7E26)
    Sleep(200)

    def lambda_7E46():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7E46)
    Sleep(3000)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrPos(0xE, -8760, 0, -14790, 270)
    SetChrPos(0xF, 40390, 0, 4970, 90)
    SetChrPos(0x10, 55850, 0, -26060, 90)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 80000, 10000, 0)
    OP_D1(16, 0, 95000, -10000, 0)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_6D(-1430, 11270, -30440, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(6040, 0)
    OP_6C(46000, 0)
    OP_6E(619, 0)
    SetChrPos(0x0, -8340, 11270, -29600, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFF6, 0x0, 0x0, 0x0)
    OP_0D()

    def lambda_7F93():
        OP_6D(-9890, 11270, -27200, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7F93)

    def lambda_7FAB():
        OP_6C(63000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FAB)

    def lambda_7FBB():
        OP_6B(7790, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7FBB)
    Sleep(2000)
    PlayEffect(0x0, 0x0, 0x10, 300, 3300, -8000, 95, 0, 350, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_43(0x0, 0x0, 0x0, 0x43)

    def lambda_800C():
        OP_D1(254, 0, 280000, -35000, 300)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_800C)
    OP_43(0xE, 0x0, 0x0, 0x44)
    WaitChrThread(0xE, 0x3)

    def lambda_8032():
        OP_D1(254, 0, 270000, 0, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_8032)

    def lambda_804C():
        OP_D1(254, 0, 90000, 10000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_804C)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_24(0x235, 0x0)
    OP_23(0x235)
    OP_43(0x0, 0x0, 0x0, 0x43)
    PlayEffect(0x0, 0x0, 0xF, 1000, 3300, -8300, 90, 0, 10, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_80BB():
        OP_D1(254, 0, 260000, 35000, 300)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_80BB)
    OP_43(0xE, 0x0, 0x0, 0x45)
    WaitChrThread(0xE, 0x3)

    def lambda_80E1():
        OP_D1(254, 0, 270000, 0, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_80E1)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_44(0x0, 0x0)
    OP_24(0x235, 0x0)
    OP_23(0x235)

    def lambda_8118():
        OP_D1(254, 0, 270000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_8118)

    def lambda_8132():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8132)
    Sleep(200)

    def lambda_8152():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8152)
    Sleep(200)

    def lambda_8172():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8172)
    Sleep(200)

    def lambda_8192():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8192)
    Sleep(200)

    def lambda_81B2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_81B2)
    Sleep(200)

    def lambda_81D2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_81D2)
    Sleep(200)

    def lambda_81F2():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_81F2)
    Sleep(200)

    def lambda_8212():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8212)
    Sleep(800)

    def lambda_8232():
        OP_D1(254, 0, 90000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_8232)

    def lambda_824C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_824C)
    Sleep(200)

    def lambda_826C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_826C)
    Sleep(200)

    def lambda_828C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_828C)
    Sleep(200)

    def lambda_82AC():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_82AC)
    Sleep(200)

    def lambda_82CC():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_82CC)
    Sleep(200)

    def lambda_82EC():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_82EC)

    def lambda_8307():
        OP_D1(254, 0, 90000, -30000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_8307)

    def lambda_8321():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8321)
    Sleep(200)

    def lambda_8341():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8341)

    def lambda_835C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_835C)
    Sleep(200)

    def lambda_837C():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_837C)

    def lambda_8397():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8397)
    Sleep(200)

    def lambda_83B7():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_83B7)
    Sleep(200)

    def lambda_83D7():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_83D7)
    Sleep(200)

    def lambda_83F7():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_83F7)
    Sleep(200)

    def lambda_8417():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8417)
    Sleep(200)

    def lambda_8437():
        OP_91(0xFE, 0xFFFCF2C0, 0x0, 0xFFFE7960, 0x84D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8437)
    Sleep(2500)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0xE, 0x3)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x3)
    OP_6D(54490, 3940, -20960, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(294000, 0)
    OP_6E(619, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFF6, 0x0, 0x0, 0x0)
    SetChrPos(0xE, -38760, 0, -14790, 270)
    SetChrPos(0xF, 40390, 0, 4970, 90)
    SetChrPos(0x10, 60850, 0, -32060, 90)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 84000, -10000, 0)
    OP_D1(16, 0, 96000, 10000, 0)
    OP_6F(0x2, 470)
    OP_70(0x2, 0x23A)
    OP_6F(0x3, 470)
    OP_70(0x3, 0x23A)
    OP_0D()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("摩尔根将军")

    AnonymousTalk(    #26
        (
            "\x07\x00#163F哼……真是阴魂不散。\x02\x03",

            "别以为速度快一些\x01",
            "就能够逃出这个包围网。\x02\x03",

            "#160F继续追赶，将它拿下！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("士兵们")

    AnonymousTalk(    #27
        "\x07\x00#5S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E1D)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_66_7CBB end

    def Function_67_864F(): pass

    label("Function_67_864F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8682")
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    Jump("Function_67_864F")

    label("loc_8682")

    Return()

    # Function_67_864F end

    def Function_68_8683(): pass

    label("Function_68_8683")


    def lambda_8689():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8689)
    Sleep(100)

    def lambda_86A9():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_86A9)
    Sleep(100)

    def lambda_86C9():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_86C9)
    Sleep(200)

    def lambda_86E9():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_86E9)
    Sleep(200)

    def lambda_8709():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8709)
    Sleep(200)

    def lambda_8729():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8729)
    Sleep(200)

    def lambda_8749():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFFCEA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8749)
    Return()

    # Function_68_8683 end

    def Function_69_875F(): pass

    label("Function_69_875F")


    def lambda_8765():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8765)
    Sleep(100)

    def lambda_8785():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8785)
    Sleep(100)

    def lambda_87A5():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87A5)
    Sleep(200)

    def lambda_87C5():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87C5)
    Sleep(200)

    def lambda_87E5():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87E5)
    Sleep(200)

    def lambda_8805():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8805)
    Sleep(200)

    def lambda_8825():
        OP_8F(0xFE, 0xFFFFDDC8, 0x0, 0xFFFFC63A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8825)
    Return()

    # Function_69_875F end

    def Function_70_883B(): pass

    label("Function_70_883B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToDark(0, 0, -1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS246._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS247._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS246._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C6(0x2, 0x3, -1, 0, 0)
    Sleep(2000)
    OP_C6(0x1, 0x0, 0, -144000, 0)
    OP_C6(0x1, 0x1, 1300, 1300, 0)
    OP_C6(0x2, 0x0, 0, -144000, 0)
    OP_C6(0x2, 0x1, 1300, 1300, 0)
    OP_C6(0x0, 0x0, 0, -144000, 1000)
    OP_C6(0x0, 0x1, 1300, 1300, 1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x0)
    OP_C7(0x0, 0x0, 0x1)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x0, -94000, -16000, 1000)
    OP_C6(0x2, 0x0, -94000, -16000, 1000)
    Sleep(400)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C7(0x0, 0x1, 0x0)
    OP_C7(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Call(0, 74)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E1E)
    OP_A2(0x10FE)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_70_883B end

    def Function_71_8A25(): pass

    label("Function_71_8A25")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(-24410, 4960, -25560, 0)
    OP_67(0, -5640, -10000, 0)
    OP_6B(5030, 0)
    OP_6C(44000, 0)
    OP_6E(561, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_8AEA():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8AEA)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_8B1B():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8B1B)

    def lambda_8B36():
        OP_6D(-42500, 30000, -12940, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B36)

    def lambda_8B4E():
        OP_67(0, 15420, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B4E)

    def lambda_8B66():
        OP_6B(5030, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8B66)

    def lambda_8B76():
        OP_6E(464, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8B76)

    def lambda_8B86():
        OP_6C(57000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_8B86)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x0)
    Return()

    # Function_71_8A25 end

    def Function_72_8C0D(): pass

    label("Function_72_8C0D")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(-4680, 30000, 7570, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(5750, 0)
    OP_6C(140000, 0)
    OP_6E(500, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_8CD2():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8CD2)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_8D03():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8D03)

    def lambda_8D1E():
        OP_6D(-21610, -2850, 5220, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D1E)

    def lambda_8D36():
        OP_67(0, 14310, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D36)

    def lambda_8D4E():
        OP_6B(4500, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D4E)

    def lambda_8D5E():
        OP_6C(224000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_8D5E)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_72_8C0D end

    def Function_73_8DE5(): pass

    label("Function_73_8DE5")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_6D(-15370, 30000, 3100, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(5750, 0)
    OP_6C(236000, 0)
    OP_6E(500, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_8EBE():
        OP_6D(13380, 30000, 4450, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8EBE)

    def lambda_8ED6():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8ED6)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0x101, 0x0)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_8F0C():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8F0C)

    def lambda_8F27():
        OP_6D(-15600, -10000, 380, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8F27)

    def lambda_8F3F():
        OP_67(0, 6870, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F3F)

    def lambda_8F57():
        OP_6B(6430, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F57)

    def lambda_8F67():
        OP_6E(613, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8F67)

    def lambda_8F77():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_8F77)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_73_8DE5 end

    def Function_74_8FFE(): pass

    label("Function_74_8FFE")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    OP_6D(5220, 28870, 190, 0)
    OP_67(0, -8260, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(103000, 0)
    OP_6E(646, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 30000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x46)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x96)

    def lambda_90C3():
        OP_6B(7000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_90C3)

    def lambda_90D3():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_90D3)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0x101, 0x0)
    OP_72(0x5, 0x20)
    OP_73(0x5)

    def lambda_9109():
        OP_90(0xFE, 0xFFFF3CB0, 0xFFFF15A0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9109)

    def lambda_9124():
        OP_6D(-28550, -10000, -240, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9124)

    def lambda_913C():
        OP_67(0, 15830, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_913C)

    def lambda_9154():
        OP_6B(5900, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9154)
    OP_6F(0x5, 150)
    OP_70(0x5, 0x14A)
    Sleep(3450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(400)
    OP_22(0xDD, 0x0, 0x64)
    OP_73(0x5)
    PlayEffect(0x0, 0xFF, 0xFF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_74_8FFE end

    def Function_75_91DB(): pass

    label("Function_75_91DB")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_6D(-150870, 26810, -13480, 0)
    OP_67(0, -3250, -10000, 0)
    OP_6B(1830, 0)
    OP_6C(262000, 0)
    OP_6E(742, 0)
    OP_A1(0x1D, 0x1)
    SetChrPos(0x1D, -100380, -10000, -13480, 270)
    OP_22(0x113, 0x0, 0x64)
    SetChrPos(0x1C, 0, 0, 0, 135)
    ClearChrFlags(0x1C, 0x80)
    OP_CF(0x1C, 0x1, "Frame85__ren")
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 281)
    OP_70(0x1, 0x12C)
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x2, 0x1, 0x1D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x1D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x1D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x1D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x1D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x1D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_940D():
        OP_67(0, -5540, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_940D)

    def lambda_9425():
        OP_6B(2400, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9425)

    def lambda_9435():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9435)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_944F():
        OP_90(0xFE, 0xFFF9E580, 0x3D090, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_944F)
    OP_43(0x1D, 0x3, 0x0, 0x4C)
    Sleep(3500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_75_91DB end

    def Function_76_9493(): pass

    label("Function_76_9493")

    Sleep(500)
    OP_24(0x113, 0x5F)
    Sleep(500)
    OP_24(0x113, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x55)
    Sleep(500)
    OP_24(0x113, 0x50)
    Sleep(500)
    OP_24(0x113, 0x4B)
    Sleep(500)
    OP_24(0x113, 0x46)
    Sleep(500)
    OP_24(0x113, 0x41)
    Sleep(500)
    OP_24(0x113, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x37)
    Sleep(500)
    OP_24(0x113, 0x32)
    Sleep(500)
    OP_24(0x113, 0x2D)
    Sleep(500)
    OP_24(0x113, 0x28)
    Sleep(500)
    OP_24(0x113, 0x23)
    Sleep(500)
    OP_24(0x113, 0x1E)
    Sleep(500)
    OP_24(0x113, 0x19)
    Sleep(500)
    OP_24(0x113, 0x14)
    Return()

    # Function_76_9493 end

    def Function_77_9524(): pass

    label("Function_77_9524")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_A1(0xF, 0x1)
    OP_8C(0xF, 270, 0)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_22(0x79, 0x1, 0x64)
    OP_6D(92340, 13360, 25280, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(247000, 0)
    OP_6E(437, 0)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_95BE():
        OP_6D(22320, 13360, 9400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_95BE)

    def lambda_95D6():
        OP_67(0, 3320, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_95D6)
    FadeToBright(1000, 0)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    def lambda_9601():
        OP_6D(-45160, 13360, -800, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_9601)

    def lambda_9619():
        OP_6C(270000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9619)

    def lambda_9629():
        OP_6E(352, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_9629)
    Sleep(4000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_77_9524 end

    def Function_78_9655(): pass

    label("Function_78_9655")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xE, 38760, -5000, -10000, 270)
    SetChrPos(0xF, 48390, -5000, -3000, 270)
    SetChrPos(0x10, 58850, -5000, -17000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_B0(0x3, 0x2D)
    OP_B0(0x4, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 700)
    OP_70(0x3, 0x30C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 700)
    OP_70(0x4, 0x30C)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_9796():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9796)
    Sleep(1000)

    def lambda_97B6():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_97B6)
    Sleep(1000)

    def lambda_97D6():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_97D6)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_78_9655 end

    def Function_79_980D(): pass

    label("Function_79_980D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    OP_6B(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A1(0xE, 0x2)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xE, 38760, -5000, -10000, 270)
    SetChrPos(0xF, 48390, -5000, -3000, 270)
    SetChrPos(0x10, 58850, -5000, -17000, 270)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_B0(0x3, 0x2D)
    OP_B0(0x4, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 700)
    OP_70(0x3, 0x30C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 700)
    OP_70(0x4, 0x30C)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_994E():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_994E)
    Sleep(1000)

    def lambda_996E():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_996E)
    Sleep(1000)

    def lambda_998E():
        OP_91(0xFE, 0xFFF9E580, 0x2710, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_998E)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_79_980D end

    def Function_80_99C5(): pass

    label("Function_80_99C5")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -9020, 0, -61470, 0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0xAAE60, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 10000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_9A8A():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A8A)

    def lambda_9A9A():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A9A)
    FadeToBright(2000, 0)

    def lambda_9AB3():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9AB3)
    Sleep(500)

    def lambda_9AD3():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9AD3)
    Sleep(500)

    def lambda_9AF3():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9AF3)
    Sleep(500)

    def lambda_9B13():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9B13)
    Sleep(500)

    def lambda_9B33():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9B33)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_80_99C5 end

    def Function_81_9B6F(): pass

    label("Function_81_9B6F")

    EventBegin(0x0)
    LoadEffect(0x0, "monster\\\\msc0331.eff")
    LoadEffect(0x1, "battle\\\\btbomb00.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    LoadEffect(0x3, "map\\\\mpsmk0.eff")
    LoadEffect(0x4, "map\\mp094_00.eff")
    LoadEffect(0x5, "map\\mp078_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, 0, 0, 0, 270)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    OP_6F(0x1, 200)
    OP_70(0x1, 0x258)
    OP_A1(0xF, 0x2)
    OP_A1(0x10, 0x3)
    OP_A1(0x11, 0x4)
    OP_A1(0x12, 0x5)
    OP_A1(0x13, 0x6)
    SetChrPos(0xF, 56000, 0, -30000, 270)
    SetChrPos(0x10, 78000, 6000, -16000, 270)
    SetChrPos(0x11, 50000, 3000, 0, 270)
    SetChrPos(0x12, 78000, 6000, 16000, 270)
    SetChrPos(0x13, 56000, 0, 30000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    ClearChrFlags(0x13, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_B0(0x2, 0x2D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 680)
    OP_70(0x2, 0x30C)
    OP_B0(0x3, 0x2D)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 680)
    OP_70(0x3, 0x30C)
    OP_B0(0x4, 0x2D)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 680)
    OP_70(0x4, 0x30C)
    OP_B0(0x5, 0x2D)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 680)
    OP_70(0x5, 0x30C)
    OP_B0(0x6, 0x2D)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 680)
    OP_70(0x6, 0x30C)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_6D(8660, -10000, -10260, 0)
    OP_67(0, 13390, -10000, 0)
    OP_6B(6420, 0)
    OP_6C(134000, 0)
    OP_6E(626, 0)
    OP_22(0x12B, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x64)
    FadeToBright(2000, 0)

    def lambda_9E66():
        OP_6D(8520, -3850, -19480, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_9E66)

    def lambda_9E7E():
        OP_67(0, 3330, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9E7E)

    def lambda_9E96():
        OP_6C(147000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9E96)
    OP_43(0xF, 0x0, 0x0, 0x58)
    OP_43(0x10, 0x0, 0x0, 0x59)
    OP_43(0x11, 0x0, 0x0, 0x5A)
    OP_43(0x12, 0x0, 0x0, 0x5B)
    OP_43(0x13, 0x0, 0x0, 0x5C)
    Sleep(19000)
    Fade(500)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    SetChrPos(0xF, 250000, -6000, 0, 270)
    SetChrPos(0x10, 350000, -6000, 10000, 270)
    SetChrPos(0x11, 450000, -6000, -10000, 270)
    SetChrPos(0x12, 550000, -6000, 14000, 270)
    SetChrPos(0x13, 650000, -6000, -14000, 270)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_6F(0x6, 800)
    OP_70(0x6, 0x384)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(30440, -6550, 0, 0)
    OP_67(0, 1450, -10000, 0)
    OP_6B(5720, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)

    def lambda_A094():
        OP_D1(254, 0, 270000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A094)

    def lambda_A0AE():
        OP_D1(254, 0, 270000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_A0AE)

    def lambda_A0C8():
        OP_D1(254, 0, 270000, -35000, 5000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_A0C8)

    def lambda_A0E2():
        OP_D1(254, 0, 270000, 35000, 5000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_A0E2)

    def lambda_A0FC():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A0FC)

    def lambda_A117():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFFD8F0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A117)

    def lambda_A132():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x2710, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A132)

    def lambda_A14D():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE890, 0xFFFFC950, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A14D)

    def lambda_A168():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE890, 0x36B0, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A168)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_43(0x15, 0x3, 0x0, 0x52)
    OP_6D(-2080, -10000, 0, 0)
    OP_67(0, 14540, -10000, 0)
    OP_6B(8420, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    Sleep(1000)
    OP_6F(0x1, 200)
    OP_70(0x1, 0x258)
    OP_43(0x15, 0x3, 0x0, 0x53)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_A277():
        OP_6D(20000, -10000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A277)

    def lambda_A28F():
        OP_67(0, 1800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A28F)

    def lambda_A2A7():
        OP_6B(6160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A2A7)
    WaitChrThread(0x0, 0x0)
    OP_72(0x1, 0x20)
    OP_73(0x1)

    def lambda_A2C4():
        OP_6D(4740, -8700, 19700, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A2C4)

    def lambda_A2DC():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A2DC)

    def lambda_A2EC():
        OP_6B(5780, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A2EC)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0x1, 601)
    OP_70(0x1, 0x384)
    Sleep(1500)
    OP_22(0x111, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 901)
    OP_70(0x1, 0x5DC)
    Sleep(1000)

    def lambda_A334():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A334)
    Sleep(100)

    def lambda_A354():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A354)
    Sleep(100)

    def lambda_A374():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A374)
    Sleep(100)

    def lambda_A394():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A394)
    Sleep(100)

    def lambda_A3B4():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A3B4)
    Sleep(100)

    def lambda_A3D4():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A3D4)
    Sleep(100)

    def lambda_A3F4():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0xDAC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A3F4)
    Sleep(1000)
    Fade(1000)
    OP_44(0xE, 0x1)
    OP_6D(20000, -10000, 0, 0)
    OP_67(0, 1800, -10000, 0)
    OP_6B(6160, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xE, 150000, 0, 0, 270)

    def lambda_A482():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0x0, 0x14820, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A482)
    Sleep(800)

    def lambda_A4A2():
        OP_6D(-20000, 11800, 0, 2600)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A4A2)

    def lambda_A4BA():
        OP_67(0, -4600, -10000, 2600)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A4BA)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_44(0xF, 0x1)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    SetChrPos(0x16, -300000, 0, 0, 90)
    SetChrPos(0xE, -500000, 0, 0, 90)
    SetChrPos(0xF, 10000, -8000, 0, 270)
    SetChrPos(0x10, 25000, -8000, 25000, 270)
    SetChrPos(0x11, 25000, -8000, -27000, 270)
    SetChrPos(0x12, 50000, -2000, 15000, 270)
    SetChrPos(0x13, 50000, -2000, -17000, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 266000, -5000, 0)
    OP_D1(17, 0, 274000, 5000, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_6D(-60920, -6600, 8860, 0)
    OP_67(0, 1880, -10000, 0)
    OP_6B(7840, 0)
    OP_6C(106000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_43(0x15, 0x3, 0x0, 0x54)
    FadeToBright(1000, 0)

    def lambda_A6B1():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A6B1)

    def lambda_A6CC():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x3A98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A6CC)

    def lambda_A6E7():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFFBD98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A6E7)

    def lambda_A702():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A702)

    def lambda_A71D():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFE0C0, 0xFFFF7B30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A71D)

    def lambda_A738():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A738)

    def lambda_A753():
        OP_8F(0xFE, 0xFFFE7960, 0xFFFFF830, 0xFFFFE4A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A753)

    label("loc_A768")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A77E")
    Sleep(15)
    Jump("loc_A768")

    label("loc_A77E")

    OP_43(0x16, 0x0, 0x0, 0x5D)
    Sleep(500)
    StopSound(0x4E20, 0xB8538, 0x7D0)

    def lambda_A79D():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A79D)

    def lambda_A7B8():
        OP_6D(-161860, -6600, 14140, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A7B8)

    def lambda_A7D0():
        OP_67(0, 4460, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A7D0)

    def lambda_A7E8():
        OP_6B(7650, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A7E8)

    def lambda_A7F8():
        OP_6C(250000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_A7F8)

    def lambda_A808():
        OP_D0(345000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_A808)
    WaitChrThread(0x0, 0x1)

    def lambda_A81D():
        OP_67(0, 2640, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A81D)
    Sleep(1000)
    Fade(500)
    OP_24(0x79, 0x28)
    OP_24(0x125, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    SetChrPos(0x16, 150000, 0, 0, 90)
    SetChrPos(0xE, 0, 0, 0, 90)
    OP_D1(14, 0, 90000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x14, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x32, 0x5, 0x0, 0x0, 0x0)
    OP_6D(45680, -8500, -5700, 0)
    OP_67(0, 1840, -10000, 0)
    OP_6B(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    OP_43(0x16, 0x0, 0x0, 0x5E)
    OP_43(0xE, 0x0, 0x0, 0x56)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    PlayEffect(0x4, 0x0, 0xE, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x0, 0x0)
    Sleep(400)
    PlayEffect(0x4, 0x0, 0xE, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x0, 0x2)
    Fade(500)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x3C)
    ClearMapFlags(0x10)
    OP_44(0xE, 0x3)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    SetChrPos(0xE, -300000, -4000, -20000, 90)
    SetChrPos(0xF, 0, -4000, 0, 270)
    SetChrPos(0x10, 0, -4000, 20000, 270)
    SetChrPos(0x11, 50000, -4000, 20000, 270)
    SetChrPos(0x12, 50000, -4000, 20000, 270)
    SetChrPos(0x13, 50000, -4000, 20000, 270)
    OP_D1(14, 0, 86000, 0, 0)
    OP_D1(15, 0, 270000, -5000, 0)
    OP_D1(16, 0, 270000, 5000, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 270000, 0, 0)
    OP_D1(19, 0, 270000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFEC, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFCE, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    OP_6D(-54120, -10000, -5500, 0)
    OP_67(0, 1480, -10000, 0)
    OP_6B(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    OP_43(0x10, 0x2, 0x0, 0x62)
    Sleep(600)
    OP_43(0xF, 0x2, 0x0, 0x60)
    Sleep(2000)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x26FC78, 0x0)
    SetMapFlags(0x10)
    StopSound(0x4E20, 0xB8538, 0xBB8)
    Sleep(1000)
    OP_43(0x0, 0x3, 0x0, 0x43)
    PlayEffect(0x5, 0x0, 0x11, 0, 1000, -12000, 176, 0, -26, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AC10():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AC10)
    Sleep(500)

    def lambda_AC30():
        OP_D1(254, 0, 266000, 20000, 1000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_AC30)
    Sleep(1000)
    Fade(500)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x64)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x3)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    SetChrPos(0xE, 0, 2000, 0, 90)
    SetChrPos(0xF, 150000, 0, -10000, 270)
    SetChrPos(0x10, 150000, 0, 40000, 270)
    SetChrPos(0x11, 150000, 5000, 20000, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_76(0xFF, 0x0, 0x1, 0xF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x14, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x32, 0x5, 0x0, 0x0, 0x0)
    OP_6D(79930, -8400, -24930, 0)
    OP_67(0, 1480, -10000, 0)
    OP_6B(12090, 0)
    OP_6C(120000, 0)
    OP_6E(536, 0)
    OP_D0(350000, 0)

    def lambda_ADA3():
        OP_6D(13700, -4100, -18370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_ADA3)

    def lambda_ADBB():
        OP_6C(192000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ADBB)
    PlayEffect(0x5, 0x0, 0xF, -500, 1000, -12000, 180, 0, 10, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AE00():
        OP_D1(254, 0, 270000, -20000, 1000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_AE00)

    def lambda_AE1A():
        OP_8F(0xFE, 0xFFFCF2C0, 0x2710, 0xFFFFB1E0, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AE1A)

    def lambda_AE35():
        OP_D1(254, 0, 90000, 25000, 1000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_AE35)

    def lambda_AE4F():
        OP_8F(0xFE, 0x0, 0x7D0, 0x4E20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AE4F)
    WaitChrThread(0x0, 0x0)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_82(0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x57)
    Sleep(1000)
    PlayEffect(0x5, 0x0, 0x10, 500, 1000, -12000, 180, 0, -40, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AEBD():
        OP_D1(254, 0, 270000, 40000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_AEBD)

    def lambda_AED7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0xAFC8, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AED7)
    WaitChrThread(0xE, 0x3)

    def lambda_AEF7():
        OP_D1(254, 0, 90000, 0, 10000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_AEF7)
    PlayEffect(0x4, 0x1, 0xE, 2000, -2000, 28000, 0, 0, 0, 3000, 3000, 3000, 0x11, 0, 0, 0, 0)
    OP_22(0x2BA, 0x0, 0x64)
    OP_7C(0x190, 0x0, 0xBB8, 0x258)
    OP_83(0x1, 0x2)
    OP_82(0x0, 0x2)
    OP_23(0x235)
    OP_44(0x0, 0x3)
    PlayEffect(0x1, 0xFF, 0x11, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_AF9E():
        OP_D1(254, 20000, 270000, -60000, 4000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_AF9E)

    def lambda_AFB8():
        OP_8F(0xFE, 0xFFFDB610, 0xFFFF8AD0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AFB8)
    Sleep(2500)
    OP_43(0x15, 0x3, 0x0, 0x52)
    PlayEffect(0x2, 0xFF, 0xFF, 20000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 5000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, -10000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)

    def lambda_B092():
        OP_6D(23830, -4100, -19830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B092)

    def lambda_B0AA():
        OP_67(0, 1580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B0AA)

    def lambda_B0C2():
        OP_6C(243000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B0C2)

    def lambda_B0D2():
        OP_D1(254, 0, 90000, 20000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_B0D2)

    def lambda_B0EC():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B0EC)
    Sleep(600)

    def lambda_B10C():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B10C)
    Sleep(500)

    def lambda_B12C():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B12C)
    Sleep(400)

    def lambda_B14C():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B14C)
    Sleep(300)

    def lambda_B16C():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B16C)
    Sleep(200)

    def lambda_B18C():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B18C)
    Sleep(100)

    def lambda_B1AC():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B1AC)
    Sleep(100)

    def lambda_B1CC():
        OP_8F(0xFE, 0x30D40, 0x7D0, 0x4E20, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B1CC)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2200)
    OP_A2(0x10FF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_81_9B6F end

    def Function_82_B204(): pass

    label("Function_82_B204")

    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x14)
    Sleep(100)
    OP_23(0x79)
    Return()

    # Function_82_B204 end

    def Function_83_B250(): pass

    label("Function_83_B250")

    OP_22(0x125, 0x1, 0x14)
    Sleep(100)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x125, 0x64)
    Return()

    # Function_83_B250 end

    def Function_84_B29E(): pass

    label("Function_84_B29E")

    OP_24(0x125, 0x5A)
    OP_22(0x79, 0x1, 0x14)
    Sleep(100)
    OP_24(0x125, 0x50)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x125, 0x46)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x125, 0x3C)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x125, 0x32)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x125, 0x28)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x64)
    Return()

    # Function_84_B29E end

    def Function_85_B304(): pass

    label("Function_85_B304")

    Sleep(1000)

    def lambda_B30F():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B30F)
    Sleep(500)

    def lambda_B32F():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_B32F)
    Sleep(1000)

    def lambda_B34E():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B34E)
    Sleep(500)

    def lambda_B36E():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_B36E)
    Sleep(1000)

    def lambda_B38D():
        OP_8F(0xFE, 0xFFFCF2C0, 0xFFFFF060, 0xFFFFEC78, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B38D)
    Sleep(500)

    def lambda_B3AD():
        OP_D1(254, 0, 266000, 20000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_B3AD)
    Return()

    # Function_85_B304 end

    def Function_86_B3C2(): pass

    label("Function_86_B3C2")

    OP_98(0x0, 0xE)
    OP_98(0x1, 0x9C40, 0x0, 0xFFFFB1E0)
    OP_98(0x1, 0x11170, 0x0, 0x4E20)
    OP_98(0x1, 0x11171, 0x0, 0x4E21)

    def lambda_B3F6():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B3F6)

    def lambda_B406():
        OP_D1(254, 0, 90000, -20000, 1200)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_B406)
    WaitChrThread(0xE, 0x3)

    def lambda_B425():
        OP_D1(254, 0, 98000, 20000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_B425)

    def lambda_B43F():
        OP_6D(45680, -10500, -5700, 2400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B43F)

    def lambda_B457():
        OP_67(0, 1480, -10000, 2400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B457)
    Return()

    # Function_86_B3C2 end

    def Function_87_B46A(): pass

    label("Function_87_B46A")


    def lambda_B470():
        OP_D1(254, 0, 90000, -20000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_B470)

    def lambda_B48A():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B48A)
    Sleep(300)

    def lambda_B4AA():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B4AA)
    Sleep(300)

    def lambda_B4CA():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B4CA)
    Sleep(300)

    def lambda_B4EA():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B4EA)
    Sleep(300)

    def lambda_B50A():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B50A)
    Sleep(800)

    def lambda_B52A():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B52A)
    Sleep(300)

    def lambda_B54A():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B54A)
    Sleep(300)

    def lambda_B56A():
        OP_8F(0xFE, 0x1388, 0x1F40, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B56A)
    Return()

    # Function_87_B46A end

    def Function_88_B580(): pass

    label("Function_88_B580")


    def lambda_B586():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B586)
    Sleep(13000)

    def lambda_B5A6():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B5A6)
    Sleep(400)

    def lambda_B5C6():
        OP_8F(0xFE, 0xFFFFF830, 0xFA0, 0xFFFF9688, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B5C6)
    Sleep(1500)

    def lambda_B5E6():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_B5E6)

    def lambda_B600():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B600)
    Sleep(100)

    def lambda_B620():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B620)
    Sleep(100)

    def lambda_B640():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B640)
    Sleep(100)

    def lambda_B660():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B660)
    Sleep(100)

    def lambda_B680():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B680)
    Sleep(100)

    def lambda_B6A0():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B6A0)
    Sleep(100)

    def lambda_B6C0():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B6C0)
    Sleep(100)

    def lambda_B6E0():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B6E0)
    Sleep(100)

    def lambda_B700():
        OP_8F(0xFE, 0xFFFE7190, 0xFA0, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B700)
    Return()

    # Function_88_B580 end

    def Function_89_B716(): pass

    label("Function_89_B716")


    def lambda_B71C():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B71C)
    Sleep(12000)

    def lambda_B73C():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B73C)
    Sleep(400)

    def lambda_B75C():
        OP_8F(0xFE, 0x7148, 0x1770, 0xFFFFB5C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B75C)
    Sleep(3500)

    def lambda_B77C():
        OP_D1(254, 0, 270000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_B77C)

    def lambda_B796():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B796)
    Sleep(100)

    def lambda_B7B6():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B7B6)
    Sleep(100)

    def lambda_B7D6():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B7D6)
    Sleep(100)

    def lambda_B7F6():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B7F6)
    Sleep(100)

    def lambda_B816():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B816)
    Sleep(100)

    def lambda_B836():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B836)
    Sleep(100)

    def lambda_B856():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B856)
    Sleep(100)

    def lambda_B876():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B876)
    Sleep(100)

    def lambda_B896():
        OP_8F(0xFE, 0xFFFEEAA8, 0x7D0, 0xFFFFF060, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B896)
    Return()

    # Function_89_B716 end

    def Function_90_B8AC(): pass

    label("Function_90_B8AC")


    def lambda_B8B2():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8B2)
    Sleep(12000)

    def lambda_B8D2():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8D2)
    Sleep(400)

    def lambda_B8F2():
        OP_8F(0xFE, 0x0, 0xBB8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8F2)
    Sleep(2000)

    def lambda_B912():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_B912)

    def lambda_B92C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B92C)
    Sleep(100)

    def lambda_B94C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B94C)
    Sleep(100)

    def lambda_B96C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B96C)
    Sleep(100)

    def lambda_B98C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B98C)
    Sleep(100)

    def lambda_B9AC():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B9AC)
    Sleep(100)

    def lambda_B9CC():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B9CC)
    Sleep(100)

    def lambda_B9EC():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B9EC)
    Sleep(100)

    def lambda_BA0C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BA0C)
    Sleep(100)

    def lambda_BA2C():
        OP_8F(0xFE, 0xFFFE7960, 0xBB8, 0x0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BA2C)
    Return()

    # Function_90_B8AC end

    def Function_91_BA42(): pass

    label("Function_91_BA42")


    def lambda_BA48():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BA48)
    Sleep(12000)

    def lambda_BA68():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BA68)
    Sleep(400)

    def lambda_BA88():
        OP_8F(0xFE, 0x6978, 0x1770, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BA88)
    Sleep(4200)

    def lambda_BAA8():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_BAA8)

    def lambda_BAC2():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BAC2)
    Sleep(100)

    def lambda_BAE2():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BAE2)
    Sleep(100)

    def lambda_BB02():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB02)
    Sleep(100)

    def lambda_BB22():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB22)
    Sleep(100)

    def lambda_BB42():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB42)
    Sleep(100)

    def lambda_BB62():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB62)
    Sleep(100)

    def lambda_BB82():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB82)
    Sleep(100)

    def lambda_BBA2():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BBA2)
    Sleep(100)

    def lambda_BBC2():
        OP_8F(0xFE, 0xFFFEE2D8, 0x1770, 0x2EE0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BBC2)
    Return()

    # Function_91_BA42 end

    def Function_92_BBD8(): pass

    label("Function_92_BBD8")


    def lambda_BBDE():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BBDE)
    Sleep(12000)

    def lambda_BBFE():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BBFE)
    Sleep(400)

    def lambda_BC1E():
        OP_8F(0xFE, 0x1770, 0xFFFFF448, 0x36B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC1E)
    Sleep(3000)

    def lambda_BC3E():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_BC3E)

    def lambda_BC58():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC58)
    Sleep(100)

    def lambda_BC78():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC78)
    Sleep(100)

    def lambda_BC98():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC98)
    Sleep(100)

    def lambda_BCB8():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BCB8)
    Sleep(100)

    def lambda_BCD8():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BCD8)
    Sleep(100)

    def lambda_BCF8():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BCF8)
    Sleep(100)

    def lambda_BD18():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BD18)
    Sleep(100)

    def lambda_BD38():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BD38)
    Sleep(100)

    def lambda_BD58():
        OP_8F(0xFE, 0xFFFE90D0, 0xBB8, 0xFFFFD8F0, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BD58)
    Return()

    # Function_92_BBD8 end

    def Function_93_BD6E(): pass

    label("Function_93_BD6E")

    PlayEffect(0x0, 0x0, 0xF, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 10000, 0)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, -5000, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x11, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 5000, 0)
    Sleep(400)
    PlayEffect(0x0, 0x3, 0x12, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, -5000, 0)
    Sleep(200)
    PlayEffect(0x0, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x16, 0, 0, 0, 0)
    Return()

    # Function_93_BD6E end

    def Function_94_BE8C(): pass

    label("Function_94_BE8C")

    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 15000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 10000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, 25000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 20000, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 20000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 30000, 0)
    Sleep(400)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, 50000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 35000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, 30000, 0, 0, 0, 3000, 3000, 3000, 0xE, -100000, 0, 40000, 0)
    Sleep(1200)
    SetChrPos(0x16, 160000, 0, 0, 90)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, -5000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -45000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -8000, -25000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -35000, 0)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x16, 0, -10000, -10000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -40000, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x16, 0, -6000, -20000, 0, 0, 0, 3000, 3000, 3000, 0xE, -90000, 0, -25000, 0)
    Return()

    # Function_94_BE8C end

    def Function_95_C0A3(): pass

    label("Function_95_C0A3")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x7, 0xFE, 1000, -1000, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0xFE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_C151():
        OP_91(0xFE, 0xFA0, 0xFFFFF448, 0xFFFFF830, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C151)
    OP_D1(254, 5000, 274000, -15000, 200)
    OP_D1(254, 0, 270000, 0, 300)
    OP_D1(254, 5000, 272000, -10000, 300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C1AE():
        OP_D1(254, 10000, 272000, -30000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C1AE)

    def lambda_C1C8():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1C8)
    Sleep(200)

    def lambda_C1E8():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1E8)
    Sleep(200)

    def lambda_C208():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C208)
    Sleep(200)

    def lambda_C228():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C228)
    Sleep(200)

    def lambda_C248():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C248)
    Sleep(200)

    def lambda_C268():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C268)
    Sleep(200)

    def lambda_C288():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C288)
    Sleep(200)

    def lambda_C2A8():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2A8)
    Sleep(200)

    def lambda_C2C8():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0xFFFFF830, 0xCB20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2C8)
    Return()

    # Function_95_C0A3 end

    def Function_96_C2DE(): pass

    label("Function_96_C2DE")

    OP_43(0xF, 0x0, 0x0, 0x5F)
    Sleep(1400)
    PlayEffect(0x2, 0xFF, 0xFF, 0, -10000, 0, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    Return()

    # Function_96_C2DE end

    def Function_97_C326(): pass

    label("Function_97_C326")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x3, 0x5, 0xFE, 0, -1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xFE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_C3D4():
        OP_91(0xFE, 0xBB8, 0xFFFFF830, 0x7D0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C3D4)
    OP_D1(254, -10000, 266000, 10000, 200)
    OP_D1(254, 5000, 270000, 0, 300)
    OP_D1(254, 0, 268000, 10000, 300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C431():
        OP_D1(254, 15000, 268000, 30000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C431)

    def lambda_C44B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C44B)
    Sleep(200)

    def lambda_C46B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C46B)
    Sleep(200)

    def lambda_C48B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C48B)
    Sleep(200)

    def lambda_C4AB():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4AB)
    Sleep(200)

    def lambda_C4CB():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4CB)
    Sleep(200)

    def lambda_C4EB():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4EB)
    Sleep(200)

    def lambda_C50B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C50B)
    Sleep(200)

    def lambda_C52B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C52B)
    Sleep(200)

    def lambda_C54B():
        OP_8F(0xFE, 0x4E20, 0xFFFFB1E0, 0x55F0, 0xCB20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C54B)
    Return()

    # Function_97_C326 end

    def Function_98_C561(): pass

    label("Function_98_C561")

    OP_43(0x10, 0x0, 0x0, 0x61)
    Sleep(1400)
    PlayEffect(0x2, 0xFF, 0xFF, 0, -10000, 20000, 260, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    Return()

    # Function_98_C561 end

    def Function_99_C5A9(): pass

    label("Function_99_C5A9")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp009_00.eff")
    LoadEffect(0x1, "battle\\btbomb00.eff")
    LoadEffect(0x2, "map\\mpsmk0.eff")
    LoadEffect(0x3, "map\\mp095_00.eff")
    LoadEffect(0x4, "monster\\ms30800c.eff")
    LoadEffect(0x5, "map\\mp106_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x1)
    OP_6D(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xE, 0x1)
    SetChrPos(0xE, -40000, 0, 0, 90)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 90000, 20000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_22(0x158, 0x1, 0x64)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x96)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 3)
    SetChrPos(0x8, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    OP_CF(0x8, 0x2, "Frame134_on_head")
    OP_A1(0x1E, 0x2)
    SetChrPos(0x1E, 200000, 80000, 80000, 270)
    ClearChrFlags(0x1E, 0x100)
    OP_D1(30, 0, 270000, 0, 0)
    OP_B0(0x2, 0x14)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_6D(63620, -10000, 7720, 0)
    OP_67(0, 3450, -10000, 0)
    OP_6B(10700, 0)
    OP_6C(200000, 0)
    OP_6E(1448, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xA, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xA, 0x2, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x19, 0x5, 0x0, 0x0, 0x0)
    StopSound(0x4E20, 0x1E8480, 0xBB8)

    def lambda_C7E5():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C7E5)
    OP_D1(30, 0, 225000, 0, 0)
    SetChrPos(0x1E, 100000, 20000, 100000, 270)
    FadeToBright(1000, 0)
    Sleep(2700)
    OP_22(0x159, 0x0, 0x64)
    Sleep(300)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C84A():
        OP_D1(254, 10000, 225000, 40000, 1500)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_C84A)

    def lambda_C864():
        OP_D0(355000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C864)

    def lambda_C874():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C874)
    Sleep(100)

    def lambda_C894():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C894)
    Sleep(100)

    def lambda_C8B4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C8B4)
    Sleep(100)

    def lambda_C8D4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C8D4)
    Sleep(100)

    def lambda_C8F4():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C8F4)
    Sleep(100)

    def lambda_C914():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C914)
    Sleep(100)

    def lambda_C934():
        OP_8F(0xFE, 0x0, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C934)
    Sleep(900)
    Fade(500)
    OP_44(0xE, 0x1)
    OP_44(0x0, 0x0)
    OP_44(0x1E, 0x3)
    OP_71(0x1, 0x4)
    OP_6D(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    OP_6B(4050, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    OP_D0(340000, 0)
    SetChrPos(0x1E, 150000, 80000, 80000, 270)
    OP_D1(30, 0, 270000, 0, 0)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 5)
    SetChrFlags(0x8, 0x8)

    def lambda_C9E3():
        OP_D0(360000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C9E3)
    OP_98(0x0, 0x1E)
    OP_98(0x1, 0x11170, 0x9C40, 0xFFFF63C0)
    OP_98(0x1, 0x0, 0x2710, 0x88B8)
    OP_98(0x1, 0xFFFE2B40, 0xFFFFD8F0, 0x61A8)

    def lambda_CA21():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CA21)
    OP_43(0x1E, 0x0, 0x0, 0x68)
    Sleep(5000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    Fade(500)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF6, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFE7, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x8)
    OP_6D(-1030, 3860, -600, 0)
    OP_67(0, 8810, -10000, 0)
    OP_6B(2090, 0)
    OP_6C(137000, 0)
    OP_6E(362, 0)
    SetChrPos(0x1E, 0, 0, 0, 270)
    OP_D1(30, 0, 270000, 0, 0)
    OP_0D()
    SetChrPos(0x0, 1310, 3860, -1340, 0)
    Sleep(500)

    ChrTalk(    #28
        0x8,
        (
            "#124F#5P──来，让我看看吧。\x02\x03",

            "#123F当希望之翼折断时……\x01",
            "你们能如何应对。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x84)
    Sleep(500)
    Play3DEffect(0x3, 0x0, 0x2, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x3, 0x1, 0x2, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x159, 0x0, 0x64)

    def lambda_CBF0():
        OP_D1(254, 0, 270000, 20000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_CBF0)

    def lambda_CC0A():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC0A)
    Sleep(100)

    def lambda_CC25():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC25)
    Sleep(100)

    def lambda_CC40():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC40)
    Sleep(100)

    def lambda_CC5B():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC5B)
    Sleep(100)

    def lambda_CC76():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC76)
    Sleep(100)

    def lambda_CC91():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CC91)
    Sleep(100)

    def lambda_CCAC():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_CCAC)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x1E, 0x1)
    OP_44(0x1E, 0x3)
    OP_72(0x1, 0x4)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF1, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFD8, 0xFFFFFFFB, 0x0, 0x0, 0x0)
    SetChrPos(0x1E, -120000, 0, -20000, 90)
    OP_D1(30, 0, 90000, 0, 0)
    SetChrPos(0xE, 0, 6000, 0, 270)
    OP_D1(14, 0, 270000, 0, 0)
    OP_6D(-12820, 5000, -13570, 0)
    OP_67(0, 1270, -10000, 0)
    OP_6B(7550, 0)
    OP_6C(294000, 0)
    OP_6E(548, 0)
    OP_43(0x1E, 0x0, 0x0, 0x65)
    OP_0D()

    def lambda_CDBD():
        OP_6D(520, 3000, 12000, 1900)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_CDBD)

    def lambda_CDD5():
        OP_6C(354000, 1900)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_CDD5)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_23(0x125)
    OP_23(0x158)
    OP_23(0x1C3)
    Sleep(1000)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x1)

    label("loc_CE33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE4D")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_CE4A")
    Jump("loc_CE4D")

    label("loc_CE4A")

    Jump("loc_CE33")

    label("loc_CE4D")

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
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x22AF)
    OP_A2(0x10FF)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_99_C5A9 end

    def Function_100_CEA6(): pass

    label("Function_100_CEA6")

    OP_8F(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xE290, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0, 0, 0, 270, 0, 0, 10000, 10000, 10000, 0xFF, 0, 0, 0, 0)
    OP_22(0x9B, 0x0, 0x64)
    OP_8F(0xFE, 0x186A0, 0x0, 0xFFFFD8F0, 0xE290, 0x0)
    Return()

    # Function_100_CEA6 end

    def Function_101_CF09(): pass

    label("Function_101_CF09")

    OP_72(0x2, 0x20)
    OP_B0(0x2, 0x2)
    OP_6F(0x2, 412)
    OP_70(0x2, 0x1A0)

    def lambda_CF26():
        OP_D1(254, 0, 90000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_CF26)
    OP_8F(0xFE, 0xFFFFF830, 0x0, 0xFFFFC950, 0xE290, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x258, 0x0, 0x1388, 0x3E8)
    OP_43(0xFE, 0x2, 0x0, 0x66)
    OP_8F(0xFE, 0x1F40, 0x0, 0xFFFFC950, 0x4E20, 0x0)
    OP_22(0x9B, 0x0, 0x64)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 416)
    OP_70(0x2, 0x1AB)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(6520, 3000, -5000, 0)
    OP_6C(72000, 0)

    def lambda_CFC8():
        OP_D1(254, 0, 90000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_CFC8)
    OP_98(0x0, 0x1E)
    OP_98(0x1, 0x249F0, 0xFA0, 0xFFFFEC78)
    OP_98(0x1, 0x493E0, 0x1F40, 0x7530)

    def lambda_D002():
        OP_98(0x2, 0xFE, 0xE290, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_D002)
    OP_73(0x2)
    OP_22(0x15A, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    Return()

    # Function_101_CF09 end

    def Function_102_D02C(): pass

    label("Function_102_D02C")

    PlayEffect(0x4, 0xFF, 0xFF, -2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 4000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 6000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_102_D02C end

    def Function_103_D136(): pass

    label("Function_103_D136")

    PlayEffect(0x2, 0x7, 0xE, 3000, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0xE, -3000, 0, 3000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)

    def lambda_D1DB():
        OP_8F(0xFE, 0x0, 0xFA0, 0x2710, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1DB)
    OP_D1(254, 5000, 270000, -25000, 200)
    OP_D1(254, 0, 270000, -15000, 400)
    OP_D1(254, 5000, 270000, -20000, 600)
    WaitChrThread(0xFE, 0x1)

    def lambda_D234():
        OP_D1(254, 10000, 270000, -25000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D234)

    def lambda_D24E():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFFFFB1E0, 0x3A98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D24E)
    Return()

    # Function_103_D136 end

    def Function_104_D264(): pass

    label("Function_104_D264")

    OP_D1(30, 10000, 270000, 40000, 2000)

    def lambda_D27D():
        OP_D1(254, 10000, 270000, -40000, 2000)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_D27D)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 350)
    OP_70(0x2, 0x172)
    OP_73(0x2)
    OP_B0(0x2, 0x5)
    OP_6F(0x2, 370)
    OP_70(0x2, 0x177)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 320)
    OP_70(0x2, 0x154)
    OP_44(0x1E, 0x3)
    OP_D1(30, 0, 270000, 0, 1000)
    Return()

    # Function_104_D264 end

    def Function_105_D2EF(): pass

    label("Function_105_D2EF")

    EventBegin(0x0)
    OP_D2(0x2701C7, 0x2701CC, 0xA)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(325000, 0)
    OP_6E(343, 0)
    OP_71(0x0, 0x4)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, -183080, -50000, -10000, 270)
    OP_A1(0x1D, 0x1)
    SetChrPos(0x1D, -183080, 15000, -10000, 270)
    OP_22(0x113, 0x1, 0x5F)
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x2, 0x0, 0x1D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x1D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x1D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x1D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x1D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x1D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x1, 0xA)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 281)
    OP_70(0x1, 0x12C)
    SetChrPos(0x1C, 0, 0, 0, 315)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 10)
    SetChrSubChip(0x1C, 0)
    OP_CF(0x1C, 0x1, "Frame85__ren")
    OP_8C(0x1C, 315, 0)
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(315000, 0)
    OP_6E(343, 0)

    def lambda_D58F():
        OP_67(0, -2500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D58F)

    def lambda_D5A7():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D5A7)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_D5C1():
        OP_90(0xFE, 0x0, 0xAFC8, 0x249F0, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_D5C1)
    OP_43(0x1D, 0x3, 0x0, 0x6A)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x1D, 0x3)
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_105_D2EF end

    def Function_106_D604(): pass

    label("Function_106_D604")

    OP_24(0x113, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x55)
    Sleep(500)
    OP_24(0x113, 0x50)
    Sleep(500)
    OP_24(0x113, 0x4B)
    Sleep(500)
    OP_24(0x113, 0x46)
    Sleep(500)
    OP_24(0x113, 0x41)
    Sleep(500)
    OP_24(0x113, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x37)
    Sleep(500)
    OP_24(0x113, 0x32)
    Sleep(500)
    OP_24(0x113, 0x28)
    Sleep(500)
    OP_24(0x113, 0x1E)
    Sleep(500)
    OP_23(0x113)
    Return()

    # Function_106_D604 end

    def Function_107_D66B(): pass

    label("Function_107_D66B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\\\mp077_00.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x70061, 0x70069, 0xA)
    OP_D2(0x270399, 0x27039D, 0xB)
    OP_D2(0x260240, 0x260245, 0xC)
    OP_D2(0x70180, 0x70184, 0xD)
    OP_D2(0x2701D2, 0x2701D7, 0xE)
    OP_D2(0x70142, 0x70146, 0xF)
    OP_D2(0x70153, 0x70157, 0x10)
    OP_D2(0x70158, 0x7015C, 0x11)
    OP_D2(0x70020, 0x70028, 0x12)
    OP_D2(0x70030, 0x70038, 0x13)
    OP_D2(0x270398, 0x27039C, 0x14)
    OP_D2(0x70050, 0x70058, 0x15)
    OP_D2(0x70060, 0x70068, 0x16)
    OP_D2(0x70070, 0x70078, 0x17)
    OP_D2(0x270080, 0x270084, 0x18)
    OP_D2(0x2700A0, 0x2700A4, 0x19)
    OP_D2(0x26023E, 0x260243, 0x1A)
    OP_D2(0x26023F, 0x260244, 0x1B)
    OP_D2(0x26019D, 0x2601A2, 0x1C)
    OP_D2(0x26019E, 0x2601A3, 0x1D)
    SetChrChipByIndex(0x1F, 26)
    SetChrChipByIndex(0x20, 27)
    SetChrChipByIndex(0x21, 12)
    SetChrChipByIndex(0x22, 13)
    SetChrChipByIndex(0x23, 14)
    SetChrChipByIndex(0x24, 15)
    SetChrChipByIndex(0x25, 16)
    SetChrChipByIndex(0x26, 17)
    SetChrChipByIndex(0x28, 18)
    SetChrChipByIndex(0x29, 19)
    SetChrChipByIndex(0x2A, 20)
    SetChrChipByIndex(0x27, 21)
    SetChrChipByIndex(0x2B, 22)
    SetChrChipByIndex(0x2C, 23)
    SetChrChipByIndex(0x2D, 24)
    SetChrChipByIndex(0x2E, 25)
    OP_6D(190000, 32299, -15160, 0)
    OP_67(0, -520, -10000, 0)
    OP_6B(1300, 0)
    OP_6C(360000, 0)
    OP_6E(750, 0)
    OP_D0(360000, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrPos(0x22, 200000, 32299, -15160, 270)
    SetChrPos(0x14, 197920, 33120, -15080, 0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_A1(0xE, 0x1)
    ClearChrFlags(0xE, 0x100)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xE, 200000, 0, 0, 270)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 360)
    OP_70(0x1, 0x1CC)
    OP_A1(0xF, 0x2)
    ClearChrFlags(0xF, 0x100)
    OP_D1(15, 4000, 270000, 0, 0)
    SetChrPos(0xF, 200000, 30000, 0, 270)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_A1(0xD, 0x0)
    ClearChrFlags(0xD, 0x100)
    SetChrPos(0x1F, 0, 0, 0, 0)
    SetChrPos(0x20, 0, 0, 0, 0)
    SetChrPos(0x21, 0, 0, 0, 0)
    OP_CF(0x1F, 0x0, "Frame144_back_Null2")
    OP_CF(0x20, 0x0, "Frame145_back_Null3")
    OP_CF(0x21, 0x0, "Frame143_back_Null1")
    OP_71(0x0, 0x20)
    OP_71(0x0, 0x8)
    OP_6F(0x0, 30)
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0xD, 0x7)
    OP_71(0x1, 0x4)
    OP_71(0x0, 0x4)
    OP_22(0x125, 0x1, 0x46)
    FadeToBright(2000, 0)
    OP_6A(0x14)

    def lambda_D99C():
        OP_8F(0xFE, 0xFFFB6C20, 0x7E2B, 0xFFFFC4C8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_D99C)
    OP_43(0x14, 0x0, 0x0, 0x81)
    OP_43(0x14, 0x3, 0x0, 0x82)
    OP_22(0x155, 0x1, 0x64)
    Sleep(5000)
    OP_43(0x21, 0x3, 0x0, 0x85)
    Sleep(13500)
    OP_43(0x22, 0x3, 0x0, 0x84)
    Sleep(1500)
    OP_6A(0xFF)

    def lambda_D9EA():
        OP_6D(-202480, -120, -15440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D9EA)

    def lambda_DA02():
        OP_67(0, 2280, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA02)

    def lambda_DA1A():
        OP_6B(1900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DA1A)

    def lambda_DA2A():
        OP_6C(702000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DA2A)

    def lambda_DA3A():
        OP_D0(360000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_DA3A)
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x1)
    ClearChrFlags(0x1F, 0x1)
    ClearChrFlags(0x20, 0x1)
    OP_23(0x155)
    OP_23(0x125)
    SetChrPos(0xD, -270000, -30000, -5080, 90)
    OP_D1(13, -5000, 90000, 0, 0)

    def lambda_DAAF():
        OP_8F(0xFE, 0xFFFEA070, 0x7530, 0xFFFFEC28, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DAAF)
    Sleep(300)
    OP_1D(0x76)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -15080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -5080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -200000, -5000, -25080, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x102, 0x3, 0x0, 0x86)

    def lambda_DB7C():
        OP_6D(-200300, -5320, -13480, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB7C)

    def lambda_DB94():
        OP_67(0, -4420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB94)

    def lambda_DBAC():
        OP_6C(785000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBAC)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xD, 0x1)
    OP_44(0x22, 0x1)
    SetChrFlags(0x22, 0x80)
    OP_6D(21490, 30000, 11030, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(4480, 0)
    OP_6C(230000, 0)
    OP_6E(262, 0)
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xD, 0, 15000, 0, 90)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    Sleep(1000)
    FadeToBright(2000, 0)

    def lambda_DCA0():
        OP_6B(4000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DCA0)
    OP_6C(237000, 8000)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(-1420, 30000, 5980, 0)
    OP_67(0, 7720, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x1F,
        (
            "#1004F#4P等、等等雷格纳特！\x01",
            "你怎么会在这里……\x02\x03",

            "#1019F而且怎么\x01",
            "连老爸也在这里啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 1)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 8)
    Sleep(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 9)
    Sleep(500)

    ChrTalk(    #30
        0x21,
        (
            "#080F#5P这什么话，毕竟整个王国的\x01",
            "导力都完全恢复了嘛。\x02\x03",

            "#081F我就把剩下的事都推给了摩尔根将军，\x01",
            "然后就让它搭我过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1F,
        "#1007F#4P搭、搭你过来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x20,
        (
            "#1054F#6P真是惊人……\x02\x03",

            "#1053F……初次见面，雷格纳特。\x01",
            "我从艾丝蒂尔那里听说了你的事情。\x02\x03",

            "#1040F危难之时得你相救，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #33
        (
            "\x07\x05呵呵，不必向我道谢。\x02\x03",

            "新时代的清风已经吹来……\x01",
            "我只是出来活动活动翅膀而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #34
        0x1F,
        (
            "#1016F#4P嘿嘿……\x01",
            "不过还真是死里逃生啊。\x02\x03",

            "#1004F对了，说起来……\x02\x03",

            "#1015F我记得你只能\x01",
            "在暗中观察人类吧？\x02\x03",

            "这样帮助我们没问题么？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #35
        (
            "\x07\x05那是你们在『辉之环』面前\x01",
            "做出答复之前的事了。\x02\x03",

            "而现在答案既已出现，\x01",
            "古代盟约也就随之解除，禁忌也消失了。\x02\x03",

            "所以我才应『剑圣』的请求，\x01",
            "前来迎接你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #36
        0x20,
        "#1044F#6P古代的盟约……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x1F,
        "#1019F#4P真是越听越糊涂啊……\x02",
    )

    CloseMessageWindow()
    OP_99(0x21, 0x9, 0xB, 0x7D0)
    Sleep(100)
    OP_43(0x21, 0x0, 0x0, 0x6C)
    WaitChrThread(0x21, 0x0)

    ChrTalk(    #38
        0x21,
        "#083F#5P不用看我，我也不知道。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x21, 0x0)
    OP_99(0x21, 0xD, 0x9, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x21,
        (
            "#080F#5P因为这个老顽固\x01",
            "口风很紧，每次一提到关键问题\x01",
            "时就开始遮遮掩掩。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    SetChrName("古龙雷格纳特")

    AnonymousTalk(    #40
        (
            "\x07\x05呵呵，别见怪。\x01",
            "龙也有龙自己的规矩。\x02\x03",

            "不过有句话可以告诉你们……\x01",
            "命运的齿轮，现在才\x01",
            "刚刚开始转动。\x02\x03",

            "而且，齿轮一旦开始转动，\x01",
            "不到最后绝不会停止……\x02\x03",

            "你们要牢记这一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #41
        0x21,
        "#082F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x1F,
        "#1020F#4P等、等一等……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x20,
        (
            "#1042F#6P就是说利贝尔还会\x01",
            "发生同样的事情？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(100)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 9)
    OP_0D()
    OP_99(0x21, 0x9, 0xB, 0x3E8)
    Sleep(500)

    ChrTalk(    #44
        0x21,
        (
            "#085F#5P不，这命运应该会\x01",
            "降临到其他的地方，\x01",
            "由其他的人来承担吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x21, 0xB, 0x9, 0x3E8)
    Sleep(500)

    ChrTalk(    #45
        0x21,
        (
            "#080F#5P──总之这次\x01",
            "你们干得很好。\x02\x03",

            "现在什么也不用想，\x01",
            "好好休息一下吧。\x02\x03",

            "和你们那些患难与共的好伙伴一起！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1F,
        "#1008F#4P啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x8)
    Sleep(500)
    OP_A2(0x2)
    OP_72(0x2, 0x4)
    OP_D1(15, 0, 270000, 0, 0)
    SetChrPos(0xF, 120000, 10000, 0, 270)
    OP_48()
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2B, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x2A, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0x27, 0x1)
    ClearChrFlags(0x28, 0x1)
    ClearChrFlags(0x29, 0x1)
    ClearChrFlags(0x23, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x2D, 0x1)
    ClearChrFlags(0x2C, 0x1)
    ClearChrFlags(0x24, 0x1)
    SetChrBattleFlags(0x2B, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0x2A, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0x27, 0x20)
    SetChrBattleFlags(0x28, 0x20)
    SetChrBattleFlags(0x29, 0x20)
    SetChrBattleFlags(0x23, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0x2D, 0x20)
    SetChrBattleFlags(0x2C, 0x20)
    SetChrBattleFlags(0x24, 0x20)
    SetChrFlags(0x2B, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    OP_89(0x2B, 104080, 11860, 60, 270)
    OP_89(0xC, 104670, 11950, 840, 270)
    OP_89(0x2A, 104430, 12360, -900, 270)
    OP_89(0xB, 105220, 12330, 930, 270)
    OP_89(0x27, 104890, 12270, -480, 270)
    OP_89(0x28, 105150, 12350, -1520, 270)
    OP_89(0x29, 106610, 11480, 1420, 270)
    OP_89(0x9, 106600, 11650, 150, 270)
    OP_89(0x2D, 106770, 12050, -1460, 270)
    OP_89(0x2C, 107810, 11410, -220, 270)
    OP_89(0x23, 107450, 11320, 910, 270)
    OP_89(0x24, 107670, 12010, -1810, 270)
    SetChrChipByIndex(0x2B, 10)
    SetChrSubChip(0x2B, 0)
    SetChrChipByIndex(0x2A, 11)
    SetChrSubChip(0x2A, 0)
    SetChrPos(0xF, 220000, 10000, -30000, 270)
    OP_D1(15, 0, 270000, 0, 0)

    def lambda_E5A8():
        OP_8F(0xFE, 0x0, 0x2710, 0xFFFFB1E0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E5A8)
    OP_22(0x125, 0x1, 0x14)

    def lambda_E5C8():
        OP_6D(51560, 15660, -17500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E5C8)

    def lambda_E5E0():
        OP_67(0, 8200, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5E0)

    def lambda_E5F8():
        OP_6C(102000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E5F8)

    def lambda_E608():
        OP_6E(792, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E608)
    WaitChrThread(0x101, 0x1)

    def lambda_E61D():
        OP_67(0, 2200, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E61D)
    WaitChrThread(0x101, 0x1)
    OP_24(0x125, 0x1E)
    Sleep(1000)
    OP_24(0x125, 0x28)
    Sleep(1000)
    OP_24(0x125, 0x32)
    Sleep(1000)
    OP_44(0xF, 0x1)
    SetChrPos(0xF, -90000, 10000, -25000, 90)
    OP_D1(15, 0, 90000, 0, 0)
    LoadEffect(0x1, "map\\\\mp032_00.eff")
    Fade(1000)
    OP_71(0x0, 0x4)
    OP_6D(-74360, 12520, -24750, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(246000, 0)
    OP_6E(528, 0)
    OP_8C(0x2B, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_8C(0x2A, 90, 0)
    OP_8C(0xB, 90, 0)
    OP_8C(0x27, 90, 0)
    OP_8C(0x28, 90, 0)
    OP_8C(0x29, 90, 0)
    OP_8C(0x23, 90, 0)
    OP_8C(0x9, 90, 0)
    OP_8C(0x2D, 90, 0)
    OP_8C(0x2C, 90, 0)
    OP_8C(0x24, 90, 0)
    OP_43(0x2C, 0x0, 0x0, 0x6F)
    OP_43(0x9, 0x0, 0x0, 0x70)
    OP_43(0x27, 0x0, 0x0, 0x71)
    OP_43(0x28, 0x0, 0x0, 0x72)
    OP_43(0xB, 0x0, 0x0, 0x73)
    OP_43(0x29, 0x0, 0x0, 0x74)
    OP_43(0x2A, 0x0, 0x0, 0x75)
    OP_43(0x2B, 0x0, 0x0, 0x76)
    OP_43(0x2D, 0x0, 0x0, 0x77)
    OP_43(0xC, 0x0, 0x0, 0x78)
    OP_43(0x23, 0x0, 0x0, 0x79)
    OP_43(0x24, 0x0, 0x0, 0x7A)
    OP_24(0x125, 0x3C)
    OP_0D()
    Sleep(1000)
    OP_24(0x125, 0x46)

    def lambda_E78E():
        OP_6D(-70360, 16370, -24750, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E78E)

    def lambda_E7A6():
        OP_67(0, 3800, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7A6)

    def lambda_E7BE():
        OP_6C(206000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E7BE)
    OP_72(0x1, 0x4)
    OP_D1(14, 0, 90000, 10000, 0)
    SetChrPos(0xE, -120000, 5000, -50000, 90)
    SetChrBattleFlags(0x2E, 0x20)
    SetChrBattleFlags(0x25, 0x20)
    SetChrBattleFlags(0x26, 0x20)
    OP_48()
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x25, 0x1)
    ClearChrFlags(0x26, 0x1)
    OP_89(0x2E, -119350, 11040, -46600, 75)
    OP_89(0x25, -120480, 11010, -46460, 75)
    OP_89(0x26, -116240, 15200, -48160, 75)
    SetChrFlags(0x2E, 0x2)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x2E, 29)
    SetChrSubChip(0x2E, 24)
    SetChrChipByIndex(0x25, 29)
    SetChrSubChip(0x25, 48)
    OP_43(0x2E, 0x0, 0x0, 0x7B)
    OP_43(0x25, 0x0, 0x0, 0x7C)
    OP_9F(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x79, 0x1, 0x32)

    def lambda_E894():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E894)
    Sleep(4200)

    def lambda_E8B4():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E8B4)
    Sleep(200)

    def lambda_E8D4():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E8D4)
    Sleep(200)

    def lambda_E8F4():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E8F4)
    Sleep(200)

    def lambda_E914():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E914)
    Sleep(200)

    def lambda_E934():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E934)
    Sleep(200)

    def lambda_E954():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E954)
    Sleep(200)

    def lambda_E974():
        OP_8F(0xFE, 0xFFFEC780, 0x1388, 0xFFFF3CB0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E974)
    OP_72(0x1, 0x20)
    OP_43(0x26, 0x0, 0x0, 0x83)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x26, 0x0)
    Sleep(2000)
    Fade(500)
    OP_44(0x2B, 0x0)
    OP_44(0xC, 0x0)
    OP_44(0x2E, 0x0)
    SetChrPos(0xE, 100000, 0, 0, 90)
    SetChrPos(0xF, 100000, 0, -20000, 90)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 5)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 5)
    ClearChrFlags(0x21, 0x2)
    SetChrSubChip(0x21, 0)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_A3(0x2)
    OP_43(0x102, 0x3, 0x0, 0x87)
    OP_6D(6010, 29000, -1560, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(650, 0)
    OP_6C(297000, 0)
    OP_6E(750, 0)
    OP_24(0x125, 0x14)
    OP_24(0x79, 0x14)
    OP_0D()
    Sleep(600)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 8)
    Sleep(100)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 9)
    Sleep(200)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 8)
    Sleep(100)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 9)
    Sleep(600)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 10)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 10)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 11)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 11)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 10)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 10)
    Sleep(150)
    SetChrChipByIndex(0x1F, 26)
    SetChrSubChip(0x1F, 9)
    SetChrChipByIndex(0x20, 27)
    SetChrSubChip(0x20, 9)
    Sleep(1000)
    Fade(100)
    OP_43(0x1F, 0x0, 0x0, 0x6D)
    Sleep(50)
    OP_43(0x20, 0x0, 0x0, 0x6E)
    OP_0D()

    def lambda_EB3E():
        OP_6E(600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB3E)
    Sleep(4500)
    OP_A2(0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x125)
    OP_23(0x79)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT47.dat", 0x8, 0x0)
    OP_21()
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_107_D66B end

    def Function_108_EBFE(): pass

    label("Function_108_EBFE")

    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 12)
    Sleep(200)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(200)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 14)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(80)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 15)
    Sleep(300)
    SetChrChipByIndex(0x21, 12)
    SetChrSubChip(0x21, 13)
    Sleep(200)
    Return()

    # Function_108_EBFE end

    def Function_109_EC59(): pass

    label("Function_109_EC59")

    OP_99(0xFE, 0x10, 0x11, 0x5DC)
    OP_99(0xFE, 0xD, 0xF, 0x5DC)
    Sleep(50)
    SetChrSubChip(0xFE, 21)
    Sleep(50)

    label("loc_EC7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC8F")
    OP_99(0xFE, 0x10, 0x15, 0x5DC)
    Jump("loc_EC7A")

    label("loc_EC8F")

    Return()

    # Function_109_EC59 end

    def Function_110_EC90(): pass

    label("Function_110_EC90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ECA5")
    OP_99(0xFE, 0x10, 0x15, 0x5DC)
    Jump("Function_110_EC90")

    label("loc_ECA5")

    Return()

    # Function_110_EC90 end

    def Function_111_ECA6(): pass

    label("Function_111_ECA6")

    OP_48()
    Sleep(400)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x1C2, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 56)
    Sleep(2000)
    SetChrSubChip(0xFE, 56)
    Sleep(100)
    SetChrSubChip(0xFE, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 58)
    Sleep(150)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 60)
    Sleep(200)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 58)
    Sleep(150)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 60)
    Sleep(200)
    SetChrSubChip(0xFE, 59)
    Sleep(150)
    SetChrSubChip(0xFE, 58)
    Sleep(100)
    SetChrSubChip(0xFE, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 56)
    Return()

    # Function_111_ECA6 end

    def Function_112_ED52(): pass

    label("Function_112_ED52")

    OP_48()
    Sleep(250)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x2BC, 0x0)
    Sleep(1500)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 32)
    Sleep(100)
    SetChrSubChip(0xFE, 33)
    Return()

    # Function_112_ED52 end

    def Function_113_ED8B(): pass

    label("Function_113_ED8B")

    OP_48()
    Sleep(350)
    OP_91(0xFE, 0xA28, 0x0, 0x0, 0x258, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 8)
    Sleep(1000)
    SetChrSubChip(0xFE, 9)
    Sleep(100)
    SetChrSubChip(0xFE, 10)
    Sleep(1000)
    SetChrSubChip(0xFE, 9)
    Sleep(100)
    SetChrSubChip(0xFE, 8)
    Sleep(1000)
    SetChrSubChip(0xFE, 11)
    Sleep(200)
    SetChrSubChip(0xFE, 12)
    Return()

    # Function_113_ED8B end

    def Function_114_EDF1(): pass

    label("Function_114_EDF1")

    OP_48()
    Sleep(300)
    OP_91(0xFE, 0xA28, 0x0, 0x0, 0x28A, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 6)
    Sleep(500)
    SetChrSubChip(0xFE, 6)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_114_EDF1 end

    def Function_115_EE61(): pass

    label("Function_115_EE61")

    OP_48()
    Sleep(200)
    OP_91(0xFE, 0x9C4, 0x0, 0x0, 0x2EE, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(1000)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 15)
    Sleep(150)
    SetChrSubChip(0xFE, 14)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Return()

    # Function_115_EE61 end

    def Function_116_EF7B(): pass

    label("Function_116_EF7B")

    OP_48()
    Sleep(300)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x1F4, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 16)
    Sleep(1000)
    SetChrSubChip(0xFE, 17)
    Sleep(200)
    SetChrSubChip(0xFE, 18)
    Sleep(200)
    SetChrSubChip(0xFE, 19)
    Sleep(200)
    SetChrSubChip(0xFE, 20)
    Sleep(200)
    SetChrSubChip(0xFE, 21)
    Sleep(200)
    SetChrSubChip(0xFE, 22)
    Sleep(1500)
    SetChrSubChip(0xFE, 21)
    Sleep(200)
    SetChrSubChip(0xFE, 20)
    Sleep(200)
    SetChrSubChip(0xFE, 19)
    Sleep(200)
    SetChrSubChip(0xFE, 18)
    Sleep(200)
    SetChrSubChip(0xFE, 17)
    Sleep(200)
    SetChrSubChip(0xFE, 16)
    Return()

    # Function_116_EF7B end

    def Function_117_F01D(): pass

    label("Function_117_F01D")

    OP_48()
    Sleep(200)
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 37)
    SetChrChipByIndex(0xFE, 29)
    Sleep(2000)
    SetChrSubChip(0xFE, 37)
    Sleep(100)
    SetChrSubChip(0xFE, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 39)
    Sleep(2000)
    SetChrSubChip(0xFE, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 37)
    Return()

    # Function_117_F01D end

    def Function_118_F079(): pass

    label("Function_118_F079")

    OP_48()
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(150)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 5)
    Sleep(150)
    SetChrSubChip(0xFE, 8)
    Sleep(200)
    SetChrSubChip(0xFE, 9)
    Sleep(300)
    SetChrSubChip(0xFE, 6)
    Sleep(400)
    SetChrSubChip(0xFE, 7)
    Sleep(500)
    OP_9E(0xFE, 0x8, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    SetChrSubChip(0xFE, 15)
    Sleep(300)
    SetChrSubChip(0xFE, 13)
    Sleep(150)

    label("loc_F1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F224")
    SetChrSubChip(0xFE, 8)
    Sleep(150)
    SetChrSubChip(0xFE, 9)
    Sleep(150)
    SetChrSubChip(0xFE, 10)
    Sleep(150)
    SetChrSubChip(0xFE, 11)
    Sleep(150)
    SetChrSubChip(0xFE, 12)
    Sleep(150)
    SetChrSubChip(0xFE, 13)
    Sleep(150)
    Jump("loc_F1DC")

    label("loc_F224")

    Return()

    # Function_118_F079 end

    def Function_119_F225(): pass

    label("Function_119_F225")

    OP_48()
    Sleep(350)
    OP_91(0xFE, 0x8FC, 0x0, 0x0, 0x226, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 30)
    Sleep(150)
    SetChrSubChip(0xFE, 31)
    Sleep(150)
    SetChrSubChip(0xFE, 23)
    Return()

    # Function_119_F225 end

    def Function_120_F26D(): pass

    label("Function_120_F26D")

    OP_48()
    Sleep(250)
    OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 46)
    Sleep(500)

    label("loc_F29B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F3E2")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xC, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Jump("loc_F29B")

    label("loc_F3E2")

    Return()

    # Function_120_F26D end

    def Function_121_F3E3(): pass

    label("Function_121_F3E3")

    OP_48()
    Sleep(450)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x190, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 7)
    Return()

    # Function_121_F3E3 end

    def Function_122_F40D(): pass

    label("Function_122_F40D")

    OP_48()
    Sleep(450)
    OP_91(0xFE, 0x834, 0x0, 0x0, 0x190, 0x0)
    Return()

    # Function_122_F40D end

    def Function_123_F428(): pass

    label("Function_123_F428")

    Sleep(2500)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 34)
    Sleep(150)
    SetChrSubChip(0xFE, 35)
    Sleep(150)
    SetChrSubChip(0xFE, 36)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)

    label("loc_F4E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F529")
    SetChrSubChip(0xFE, 24)
    Sleep(150)
    SetChrSubChip(0xFE, 25)
    Sleep(150)
    SetChrSubChip(0xFE, 26)
    Sleep(150)
    SetChrSubChip(0xFE, 27)
    Sleep(150)
    SetChrSubChip(0xFE, 28)
    Sleep(150)
    SetChrSubChip(0xFE, 29)
    Sleep(150)
    Jump("loc_F4E1")

    label("loc_F529")

    Return()

    # Function_123_F428 end

    def Function_124_F52A(): pass

    label("Function_124_F52A")

    Sleep(2500)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 43)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 41)
    Sleep(150)
    SetChrSubChip(0xFE, 40)
    Sleep(150)
    SetChrSubChip(0xFE, 41)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 43)
    Sleep(150)
    SetChrSubChip(0xFE, 42)
    Sleep(150)
    SetChrSubChip(0xFE, 44)
    Sleep(150)
    SetChrSubChip(0xFE, 45)
    Sleep(150)
    SetChrSubChip(0xFE, 48)
    Return()

    # Function_124_F52A end

    def Function_125_F5C1(): pass

    label("Function_125_F5C1")

    OP_8F(0xFE, 0xB82E, 0x7530, 0xFFFFE3EA, 0x1F40, 0x0)
    OP_8F(0xFE, 0xFFFFE6EC, 0x3F5B, 0xFFFFA588, 0x2EE0, 0x0)
    OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0xFA0, 0x0)
    Return()

    # Function_125_F5C1 end

    def Function_126_F5FE(): pass

    label("Function_126_F5FE")


    def lambda_F604():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_F604)
    OP_8F(0xFE, 0x27100, 0x249F0, 0x0, 0x1F40, 0x0)
    Return()

    # Function_126_F5FE end

    def Function_127_F621(): pass

    label("Function_127_F621")

    OP_98(0x0, 0x22)
    OP_98(0x1, 0xFFFF63C0, 0x84D0, 0xFFFFC4C8)
    OP_98(0x1, 0xFFFF15A0, 0x9470, 0x4E20)
    OP_98(0x1, 0xFFFE2B40, 0x4E20, 0x4E20)

    def lambda_F655():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_F655)
    Return()

    # Function_127_F621 end

    def Function_128_F660(): pass

    label("Function_128_F660")


    def lambda_F666():
        OP_6D(-28420, 33660, -15760, 3400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F666)

    def lambda_F67E():
        OP_67(0, -2320, -10000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F67E)

    def lambda_F696():
        OP_6C(312000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F696)
    WaitChrThread(0x101, 0x1)

    def lambda_F6AB():
        OP_6D(-16840, 34860, 10260, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F6AB)

    def lambda_F6C3():
        OP_67(0, 1060, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6C3)

    def lambda_F6DB():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F6DB)

    def lambda_F6EB():
        OP_D0(10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F6EB)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_128_F660 end

    def Function_129_F6FB(): pass

    label("Function_129_F6FB")


    def lambda_F701():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F701)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x5A)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x50)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x46)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x3C)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x32)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x28)
    Sleep(1000)
    Sleep(1000)
    OP_24(0x79, 0x1E)
    Sleep(1000)

    def lambda_F783():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4D58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F783)
    Sleep(400)

    def lambda_F7A3():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4BC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F7A3)
    Sleep(400)
    OP_24(0x79, 0x14)

    def lambda_F7C7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4A38, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F7C7)
    Sleep(400)

    def lambda_F7E7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x48A8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F7E7)
    Sleep(400)

    def lambda_F807():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4718, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F807)
    Sleep(400)

    def lambda_F827():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x44C0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F827)
    Sleep(400)
    OP_24(0x79, 0xA)

    def lambda_F84B():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F84B)
    Sleep(400)

    def lambda_F86B():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3F48, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F86B)
    Sleep(400)

    def lambda_F88B():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3CF0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F88B)
    Sleep(400)

    def lambda_F8AB():
        OP_8F(0xFE, 0xFFFCF2C0, 0x8160, 0xFFFFC518, 0x3908, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F8AB)
    Return()

    # Function_129_F6FB end

    def Function_130_F8C1(): pass

    label("Function_130_F8C1")


    def lambda_F8C7():
        OP_6C(680000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F8C7)

    def lambda_F8D7():
        OP_67(0, 3080, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F8D7)

    def lambda_F8EF():
        OP_6B(720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F8EF)

    def lambda_F8FF():
        OP_D0(355000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F8FF)
    WaitChrThread(0x101, 0x1)

    def lambda_F914():
        OP_67(0, 5580, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F914)

    def lambda_F92C():
        OP_6B(1640, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F92C)

    def lambda_F93C():
        OP_D0(370000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F93C)
    WaitChrThread(0x101, 0x1)

    def lambda_F951():
        OP_67(0, 8820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F951)

    def lambda_F969():
        OP_6B(720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F969)
    Return()

    # Function_130_F8C1 end

    def Function_131_F974(): pass

    label("Function_131_F974")

    OP_6F(0x1, 61)
    OP_70(0x1, 0x5F)
    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
    Return()

    # Function_131_F974 end

    def Function_132_F993(): pass

    label("Function_132_F993")

    OP_24(0x155, 0x5A)
    Sleep(300)
    OP_24(0x155, 0x50)
    Sleep(300)
    OP_24(0x155, 0x46)
    Sleep(300)
    OP_24(0x155, 0x3C)
    Sleep(300)
    OP_24(0x155, 0x32)
    Sleep(300)
    OP_24(0x155, 0x28)
    Sleep(300)
    OP_24(0x155, 0x1E)
    Sleep(300)
    OP_24(0x155, 0x14)
    Sleep(300)
    OP_24(0x155, 0xA)
    Return()

    # Function_132_F993 end

    def Function_133_F9E0(): pass

    label("Function_133_F9E0")

    OP_24(0x125, 0x3C)
    Sleep(500)
    OP_24(0x125, 0x32)
    Sleep(500)
    OP_24(0x125, 0x28)
    Sleep(500)
    OP_24(0x125, 0x1E)
    Sleep(500)
    OP_24(0x125, 0x14)
    Sleep(500)
    OP_24(0x125, 0xA)
    Return()

    # Function_133_F9E0 end

    def Function_134_FA12(): pass

    label("Function_134_FA12")

    Sleep(800)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(2400)

    label("loc_FA3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FA5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FA52")
    Jump("loc_FA5F")

    label("loc_FA52")

    OP_22(0x120, 0x0, 0x5A)
    Sleep(2000)
    Jump("loc_FA3F")

    label("loc_FA5F")

    OP_22(0x120, 0x0, 0x55)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x41)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x2D)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x19)
    Sleep(2000)
    Return()

    # Function_134_FA12 end

    def Function_135_FA88(): pass

    label("Function_135_FA88")

    Sleep(1100)

    label("loc_FA8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FAAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FAA0")
    Jump("loc_FAAD")

    label("loc_FAA0")

    OP_22(0x120, 0x0, 0x50)
    Sleep(2000)
    Jump("loc_FA8D")

    label("loc_FAAD")

    OP_22(0x120, 0x0, 0x46)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x28)
    Sleep(2000)
    OP_22(0x120, 0x0, 0x14)
    Sleep(2000)
    Return()

    # Function_135_FA88 end

    SaveToFile()

Try(main)
