from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0011   ._SN',
        MapName             = 'event',
        Location            = 'E0011.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0011_1 ._SN',
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
        '阿加特',                               # 9
        '雪拉扎德',                             # 10
        '奥利维尔',                             # 11
        '提妲',                                 # 12
        '金',                                   # 13
        '科洛丝',                               # 14
        '酒杯',                                 # 15
        '船长',                                 # 16
        '操舵手',                               # 17
        '副操舵手',                             # 18
        '操作员',                               # 19
        '乘客',                                 # 20
        '乘客',                                 # 21
        '乘客',                                 # 22
        '乘务员诺拉',                           # 23
        '鲁特尔',                               # 24
        '阿尔丹',                               # 25
        '米拉诺',                               # 26
        '西蒙',                                 # 27
        '哈尔德',                               # 28
        '乘务员亚雷克',                         # 29
        '索斯摩夫',                             # 30
        '佩特洛夫船长',                         # 31
        '乘务员罗杰',                           # 32
        '乘务员库因特',                         # 33
        '乘客',                                 # 34
        '乘客',                                 # 35
        '乘客',                                 # 36
        '乘客',                                 # 37
        '乘客',                                 # 38
        '乘客',                                 # 39
        '乘客',                                 # 40
        '乘客',                                 # 41
        '凯文神父',                             # 42
        '布露姆老奶奶',                         # 43
        '基蒂',                                 # 44
        '乘客',                                 # 45
        '乘客',                                 # 46
        '乘客',                                 # 47
        '乘客',                                 # 48
        '乘客',                                 # 49
        '乘客',                                 # 50
        '乘客',                                 # 51
        '乘客',                                 # 52
        '乘客',                                 # 53
        '乘客',                                 # 54
        '乘客',                                 # 55
        '吉米',                                 # 56
        '阿尔丹',                               # 57
        '小说',                                 # 58
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
        'ED6_DT07/CH00053 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT07/CH00040 ._CH',             # 07
        'ED6_DT07/CH00043 ._CH',             # 08
        'ED6_DT07/CH00063 ._CH',             # 09
        'ED6_DT06/CH20134 ._CH',             # 0A
        'ED6_DT07/CH01443 ._CH',             # 0B
        'ED6_DT07/CH01453 ._CH',             # 0C
        'ED6_DT07/CH01453 ._CH',             # 0D
        'ED6_DT07/CH01453 ._CH',             # 0E
        'ED6_DT07/CH01160 ._CH',             # 0F
        'ED6_DT07/CH01163 ._CH',             # 10
        'ED6_DT07/CH01120 ._CH',             # 11
        'ED6_DT07/CH01123 ._CH',             # 12
        'ED6_DT07/CH01143 ._CH',             # 13
        'ED6_DT27/CH03003 ._CH',             # 14
        'ED6_DT07/CH01540 ._CH',             # 15
        'ED6_DT07/CH01020 ._CH',             # 16
        'ED6_DT07/CH01040 ._CH',             # 17
        'ED6_DT07/CH01233 ._CH',             # 18
        'ED6_DT07/CH01140 ._CH',             # 19
        'ED6_DT07/CH01120 ._CH',             # 1A
        'ED6_DT07/CH01290 ._CH',             # 1B
        'ED6_DT07/CH01450 ._CH',             # 1C
        'ED6_DT07/CH01443 ._CH',             # 1D
        'ED6_DT07/CH01293 ._CH',             # 1E
        'ED6_DT07/CH01293 ._CH',             # 1F
        'ED6_DT07/CH01113 ._CH',             # 20
        'ED6_DT07/CH01490 ._CH',             # 21
        'ED6_DT07/CH01170 ._CH',             # 22
        'ED6_DT07/CH01130 ._CH',             # 23
        'ED6_DT07/CH01200 ._CH',             # 24
        'ED6_DT07/CH01183 ._CH',             # 25
        'ED6_DT07/CH01463 ._CH',             # 26
        'ED6_DT07/CH01140 ._CH',             # 27
        'ED6_DT27/CH03080 ._CH',             # 28
        'ED6_DT06/CH20045 ._CH',             # 29
        'ED6_DT26/CH20241 ._CH',             # 2A
        'ED6_DT26/CH20291 ._CH',             # 2B
        'ED6_DT07/CH01010 ._CH',             # 2C
        'ED6_DT07/CH01770 ._CH',             # 2D
        'ED6_DT07/CH01460 ._CH',             # 2E
        'ED6_DT07/CH01143 ._CH',             # 2F
        'ED6_DT07/CH01153 ._CH',             # 30
        'ED6_DT07/CH01103 ._CH',             # 31
        'ED6_DT07/CH01183 ._CH',             # 32
        'ED6_DT07/CH01023 ._CH',             # 33
        'ED6_DT07/CH01470 ._CH',             # 34
        'ED6_DT07/CH00050 ._CH',             # 35
        'ED6_DT07/CH01040 ._CH',             # 36
        'ED6_DT07/CH01043 ._CH',             # 37
        'ED6_DT07/CH01213 ._CH',             # 38
        'ED6_DT07/CH01070 ._CH',             # 39
        'ED6_DT07/CH01003 ._CH',             # 3A
    )

    AddCharChipPat(
        'ED6_DT07/CH00053P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT07/CH00040P._CP',             # 07
        'ED6_DT07/CH00043P._CP',             # 08
        'ED6_DT07/CH00063P._CP',             # 09
        'ED6_DT06/CH20134P._CP',             # 0A
        'ED6_DT07/CH01443P._CP',             # 0B
        'ED6_DT07/CH01453P._CP',             # 0C
        'ED6_DT07/CH01453P._CP',             # 0D
        'ED6_DT07/CH01453P._CP',             # 0E
        'ED6_DT07/CH01160P._CP',             # 0F
        'ED6_DT07/CH01163P._CP',             # 10
        'ED6_DT07/CH01120P._CP',             # 11
        'ED6_DT07/CH01123P._CP',             # 12
        'ED6_DT07/CH01143P._CP',             # 13
        'ED6_DT27/CH03003P._CP',             # 14
        'ED6_DT07/CH01540P._CP',             # 15
        'ED6_DT07/CH01020P._CP',             # 16
        'ED6_DT07/CH01040P._CP',             # 17
        'ED6_DT07/CH01233P._CP',             # 18
        'ED6_DT07/CH01140P._CP',             # 19
        'ED6_DT07/CH01120P._CP',             # 1A
        'ED6_DT07/CH01290P._CP',             # 1B
        'ED6_DT07/CH01450P._CP',             # 1C
        'ED6_DT07/CH01443P._CP',             # 1D
        'ED6_DT07/CH01293P._CP',             # 1E
        'ED6_DT07/CH01293P._CP',             # 1F
        'ED6_DT07/CH01113P._CP',             # 20
        'ED6_DT07/CH01490P._CP',             # 21
        'ED6_DT07/CH01170P._CP',             # 22
        'ED6_DT07/CH01130P._CP',             # 23
        'ED6_DT07/CH01200P._CP',             # 24
        'ED6_DT07/CH01183P._CP',             # 25
        'ED6_DT07/CH01463P._CP',             # 26
        'ED6_DT07/CH01140P._CP',             # 27
        'ED6_DT27/CH03080P._CP',             # 28
        'ED6_DT06/CH20045P._CP',             # 29
        'ED6_DT26/CH20241P._CP',             # 2A
        'ED6_DT26/CH20291P._CP',             # 2B
        'ED6_DT07/CH01010P._CP',             # 2C
        'ED6_DT07/CH01770P._CP',             # 2D
        'ED6_DT07/CH01460P._CP',             # 2E
        'ED6_DT07/CH01143P._CP',             # 2F
        'ED6_DT07/CH01153P._CP',             # 30
        'ED6_DT07/CH01103P._CP',             # 31
        'ED6_DT07/CH01183P._CP',             # 32
        'ED6_DT07/CH01023P._CP',             # 33
        'ED6_DT07/CH01470P._CP',             # 34
        'ED6_DT07/CH00050P._CP',             # 35
        'ED6_DT07/CH01040P._CP',             # 36
        'ED6_DT07/CH01043P._CP',             # 37
        'ED6_DT07/CH01213P._CP',             # 38
        'ED6_DT07/CH01070P._CP',             # 39
        'ED6_DT07/CH01003P._CP',             # 3A
    )

    DeclNpc(
        X                   = 117300,
        Z                   = 0,
        Y                   = 1350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 117300,
        Z                   = 0,
        Y                   = 1350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 88690,
        Z                   = -1000,
        Y                   = 51250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x185,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 88530,
        Z                   = -500,
        Y                   = 51980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x191,
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
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 116000,
        Z                   = 0,
        Y                   = 10280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 117420,
        Z                   = 80,
        Y                   = 7320,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57210,
        Z                   = 0,
        Y                   = 1140,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 88880,
        Z                   = 100,
        Y                   = -1240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 87830,
        Z                   = 0,
        Y                   = 170,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 89360,
        Z                   = 0,
        Y                   = 8810,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 86120,
        Z                   = 0,
        Y                   = 47320,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 27850,
        Z                   = 0,
        Y                   = -8070,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 59020,
        Z                   = -530,
        Y                   = 49310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 56990,
        Z                   = -1800,
        Y                   = 51970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 59190,
        Z                   = -1950,
        Y                   = 54200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 88770,
        Z                   = 100,
        Y                   = -4910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 115840,
        Z                   = 0,
        Y                   = -1200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 114590,
        Z                   = 100,
        Y                   = -2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 113550,
        Z                   = 80,
        Y                   = 1410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 87890,
        Z                   = 0,
        Y                   = -1220,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 87890,
        Z                   = 0,
        Y                   = -2410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 56,
        ChipIndex           = 0x38,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 57,
        ChipIndex           = 0x39,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 58,
        ChipIndex           = 0x3A,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 116990,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 56,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 57210,
        Z                   = 0,
        Y                   = 1140,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 88140,
        Z                   = -500,
        Y                   = 52020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703939,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_8C2",          # 00, 0
        "Function_1_112B",         # 01, 1
        "Function_2_1194",         # 02, 2
        "Function_3_1311",         # 03, 3
        "Function_4_13EB",         # 04, 4
        "Function_5_1576",         # 05, 5
        "Function_6_17DA",         # 06, 6
        "Function_7_1B2A",         # 07, 7
        "Function_8_1C51",         # 08, 8
        "Function_9_1DE5",         # 09, 9
        "Function_10_1F76",        # 0A, 10
        "Function_11_2361",        # 0B, 11
        "Function_12_2478",        # 0C, 12
        "Function_13_25F0",        # 0D, 13
        "Function_14_26BC",        # 0E, 14
        "Function_15_278C",        # 0F, 15
        "Function_16_28B4",        # 10, 16
        "Function_17_2E47",        # 11, 17
        "Function_18_318E",        # 12, 18
        "Function_19_3595",        # 13, 19
        "Function_20_3880",        # 14, 20
        "Function_21_3AC4",        # 15, 21
        "Function_22_3D7D",        # 16, 22
        "Function_23_3DE0",        # 17, 23
        "Function_24_3E6B",        # 18, 24
        "Function_25_4053",        # 19, 25
        "Function_26_41ED",        # 1A, 26
        "Function_27_4359",        # 1B, 27
        "Function_28_4704",        # 1C, 28
        "Function_29_4812",        # 1D, 29
        "Function_30_4925",        # 1E, 30
        "Function_31_4A48",        # 1F, 31
        "Function_32_4B53",        # 20, 32
        "Function_33_4C44",        # 21, 33
        "Function_34_4D7F",        # 22, 34
        "Function_35_4E03",        # 23, 35
        "Function_36_4EF4",        # 24, 36
        "Function_37_50B0",        # 25, 37
        "Function_38_5102",        # 26, 38
        "Function_39_5181",        # 27, 39
        "Function_40_51D6",        # 28, 40
        "Function_41_52C0",        # 29, 41
        "Function_42_53D6",        # 2A, 42
        "Function_43_543B",        # 2B, 43
        "Function_44_5E2D",        # 2C, 44
        "Function_45_5E3F",        # 2D, 45
        "Function_46_63AB",        # 2E, 46
        "Function_47_69D5",        # 2F, 47
        "Function_48_7387",        # 30, 48
        "Function_49_7440",        # 31, 49
        "Function_50_74A0",        # 32, 50
        "Function_51_7CDB",        # 33, 51
        "Function_52_814E",        # 34, 52
        "Function_53_86AA",        # 35, 53
        "Function_54_95AF",        # 36, 54
        "Function_55_9654",        # 37, 55
        "Function_56_966B",        # 38, 56
        "Function_57_9682",        # 39, 57
    )


    def Function_0_8C2(): pass

    label("Function_0_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DA")
    Event(0, 57)

    label("loc_8DA")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 91260, 0, 44910, 90)
    SetChrPos(0xD, 117350, 100, 3200, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 89280, 80, -3200, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    SetChrPos(0xC, 117350, 100, -850, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 57200, 0, -2270, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 53)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 114820, 0, 5050, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 113340, 100, 1260, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 116650, 0, 10640, 45)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 84990, 0, 9250, 180)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 84990, 0, 8270, 0)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 86180, 0, 80, 225)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 85340, 100, -1250, 0)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 117260, 100, 5450, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 88620, -1000, 52980, 0)
    Jump("loc_EF2")

    label("loc_A5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5D")
    SetChrPos(0x8, 116650, 100, 3200, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 117350, 50, 1200, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 117350, 100, -850, 0)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5")
    SetChrPos(0xD, 88410, -1000, 53020, 0)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x0, 0x2)
    Jump("loc_AF0")

    label("loc_AD5")

    SetChrPos(0xD, 116650, 100, 5200, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")
    SetChrPos(0xB, 58800, 0, -2020, 90)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_B35")

    label("loc_B11")

    OP_44(0xB, 0x0)
    SetChrPos(0xB, 117350, 100, 5200, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 9)

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_B60")
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 117350, 80, 3100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)

    label("loc_B60")

    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrPos(0x16, 114750, 0, 11170, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 28120, 0, -8480, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 180)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 117330, 100, 7280, 0)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, 86280, 0, 1960, 212)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, 84800, 100, 600, 0)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, 85460, 100, -3100, 0)
    ClearChrFlags(0x30, 0x80)
    SetChrPos(0x30, 89340, 150, -4890, 0)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, 113350, 100, -700, 0)
    ClearChrFlags(0x32, 0x80)
    SetChrPos(0x32, 113380, 0, 0, 180)
    Jump("loc_EF2")

    label("loc_C5D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_C6D"),
        (109, "loc_C7B"),
        (SWITCH_DEFAULT, "loc_C89"),
    )


    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C78")

    label("loc_C78")

    Jump("loc_C89")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C86")

    label("loc_C86")

    Jump("loc_C89")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA1")
    Event(0, 57)

    label("loc_CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CE1")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 41)
    SetChrPos(0x9, 88690, -1000, 51250, 0)
    SetChrPos(0xA, 88700, -1000, 52960, 180)
    Jump("loc_D0D")

    label("loc_CE1")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 88690, -1000, 51250, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 360)

    label("loc_D0D")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 117200, 100, 1100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 1)), scpexpr(EXPR_END)), "loc_D32")
    SetChrSubChip(0xC, 0)
    Jump("loc_D37")

    label("loc_D32")

    SetChrSubChip(0xC, 2)

    label("loc_D37")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 114820, 0, 11500, 180)
    ClearChrFlags(0x37, 0x80)
    SetChrPos(0x37, 116990, 0, 10300, 56)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 89290, 100, -3120, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 84670, 100, -1300, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 28120, 0, -8480, 270)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 113220, 100, 1280, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 91080, 0, 48580, 90)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 116700, 100, 5250, 0)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 88750, 100, 520, 0)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 87730, 0, 1190, 135)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 85440, 100, -4860, 0)
    ClearChrFlags(0x36, 0x80)
    SetChrPos(0x36, 114160, 100, -2480, 0)
    Jump("loc_EF2")

    label("loc_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_END)), "loc_EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7F")
    Event(0, 57)

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_E8E")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_E93")

    label("loc_E8E")

    ClearChrFlags(0x8, 0x80)

    label("loc_E93")

    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0xE, 5)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")
    Event(0, 43)
    Jump("loc_112A")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2A")
    Event(1, 16)
    Jump("loc_F3A")

    label("loc_F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3A")
    Event(1, 6)

    label("loc_F3A")

    Jump("loc_112A")

    label("loc_F3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61")
    Event(1, 4)

    label("loc_F61")

    Jump("loc_FE0")

    label("loc_F64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 7)), scpexpr(EXPR_END)), "loc_F8B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 0)), scpexpr(EXPR_END)), "loc_F9C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_END)), "loc_FAD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_END)), "loc_FBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_FCF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE0")
    Event(1, 5)

    label("loc_FE0")

    Jump("loc_112A")

    label("loc_FE3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_101F"),
        (102, "loc_101F"),
        (103, "loc_101F"),
        (104, "loc_101F"),
        (105, "loc_101F"),
        (106, "loc_101F"),
        (107, "loc_101F"),
        (109, "loc_101F"),
        (110, "loc_101F"),
        (112, "loc_101F"),
        (113, "loc_101F"),
        (114, "loc_101F"),
        (115, "loc_101F"),
        (SWITCH_DEFAULT, "loc_112A"),
    )


    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1035")
    Event(0, 49)
    Jump("loc_112A")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_10B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_1057")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_1068")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_1079")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_108A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_108A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 2)), scpexpr(EXPR_END)), "loc_109B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_109B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AC")
    Event(0, 54)

    label("loc_10AC")

    Jump("loc_112A")

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C8")
    Event(0, 44)
    Jump("loc_112A")

    label("loc_10C8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 4)), scpexpr(EXPR_END)), "loc_10E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 5)), scpexpr(EXPR_END)), "loc_10F4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 6)), scpexpr(EXPR_END)), "loc_1105")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_END)), "loc_1116")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1116")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1127")
    Event(0, 48)

    label("loc_1127")

    Jump("loc_112A")

    label("loc_112A")

    Return()

    # Function_0_8C2 end

    def Function_1_112B(): pass

    label("Function_1_112B")

    OP_10(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_END)), "loc_113F")
    SetChrFlags(0x39, 0x80)

    label("loc_113F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1154")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1193")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1177")
    Call(0, 55)
    Jump("loc_1193")

    label("loc_1177")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    Call(0, 56)

    label("loc_1193")

    Return()

    # Function_1_112B end

    def Function_2_1194(): pass

    label("Function_2_1194")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_12FB")

    label("loc_11B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D2")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_12FB")

    label("loc_11D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_12FB")

    label("loc_11EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_12FB")

    label("loc_1204")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_12FB")

    label("loc_121D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1236")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_12FB")

    label("loc_1236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_12FB")

    label("loc_124F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_12FB")

    label("loc_1268")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_12FB")

    label("loc_1281")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_12FB")

    label("loc_129A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B3")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_12FB")

    label("loc_12B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_12FB")

    label("loc_12CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_12FB")

    label("loc_12E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_12FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1310")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_12FB")

    label("loc_1310")

    Return()

    # Function_2_1194 end

    def Function_3_1311(): pass

    label("Function_3_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_13EA")

    label("loc_1318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13EA")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_134E")
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Jump("loc_1367")

    label("loc_134E")

    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)

    label("loc_1367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_1374")
    OP_A3(0x1F)
    Jump("loc_13B0")

    label("loc_1374")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13B0")
    Sleep(80)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    OP_A2(0x1F)

    label("loc_13B0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13D3")
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_13E7")

    label("loc_13D3")

    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)

    label("loc_13E7")

    Jump("loc_1318")

    label("loc_13EA")

    Return()

    # Function_3_1311 end

    def Function_4_13EB(): pass

    label("Function_4_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_147A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1401")
    Call(1, 7)
    Jump("loc_1477")

    label("loc_1401")

    TalkBegin(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x8,
        (
            "#552F话先说在前头，要回村子\x01",
            "等工作解决了再说吧。\x02\x03",

            "可别叫我特地带你过去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1007F小气。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    TalkEnd(0x8)

    label("loc_1477")

    Jump("loc_1575")

    label("loc_147A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148D")
    Call(1, 0)
    Jump("loc_1575")

    label("loc_148D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_1571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_156A")
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14C0")
    SetChrSubChip(0xFE, 2)
    Jump("loc_14DB")

    label("loc_14C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D6")
    SetChrSubChip(0xFE, 2)
    Jump("loc_14DB")

    label("loc_14D6")

    SetChrSubChip(0xFE, 1)

    label("loc_14DB")

    OP_8C(0x8, 360, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #2
        0x8,
        (
            "#555F话说回来军方要求谈话啊。\x02\x03",

            "特地叫我们去王都\x01",
            "可能需要保守秘密吧。\x02\x03",

            "结社的动向也令人在意,\x01",
            "看来暂时还不能放松啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_156E")

    label("loc_156A")

    Call(0, 50)

    label("loc_156E")

    Jump("loc_1575")

    label("loc_1571")

    Call(0, 45)

    label("loc_1575")

    Return()

    # Function_4_13EB end

    def Function_5_1576(): pass

    label("Function_5_1576")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E6")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1612")
    Jump("loc_1654")

    label("loc_1612")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_162E")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1654")

    label("loc_162E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_164A")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1654")

    label("loc_164A")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1654")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #3
        0x9,
        (
            "#027F到达柏斯之前\x01",
            "会经过洛连特，\x01",
            "时间还挺宽余。\x02\x03",

            "你可以散步或者在座位休息，\x01",
            "随便做什么都好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_17D9")

    label("loc_16E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_17CE")
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1719")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1734")

    label("loc_1719")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172F")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1734")

    label("loc_172F")

    SetChrSubChip(0xFE, 1)

    label("loc_1734")

    OP_8C(0x9, 360, 0)
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #4
        0x9,
        (
            "#522F话说回来\x01",
            "王国军要求谈话啊……\x02\x03",

            "特地叫我们去王都\x01",
            "是不是需要保守秘密呢。\x02\x03",

            "#022F结社的动向也令人在意\x01",
            "看来暂时还不能放松啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_17D2")

    label("loc_17CE")

    Call(0, 52)

    label("loc_17D2")

    Jump("loc_17D9")

    label("loc_17D5")

    Call(0, 46)

    label("loc_17D9")

    Return()

    # Function_5_1576 end

    def Function_6_17DA(): pass

    label("Function_6_17DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_195A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F0")
    Call(1, 10)
    Jump("loc_1957")

    label("loc_17F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1803")
    Call(1, 11)
    Jump("loc_1957")

    label("loc_1803")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1893")
    Jump("loc_18D5")

    label("loc_1893")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18AF")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18D5")

    label("loc_18AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18CB")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18D5")

    label("loc_18CB")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18D5")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #5
        0xA,
        (
            "#030F说起来柏斯有那个美人市长\x01",
            "和那清冷眼神的女佣吧。\x02\x03",

            "#031F呼，真期待能再会啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_1957")

    Jump("loc_1B29")

    label("loc_195A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_1971")
    Call(1, 4)

    label("loc_1971")

    Jump("loc_1B29")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_1B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_1B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A96")
    TalkBegin(0xA)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_A2(0x0)

    ChrTalk(    #6
        0xA,
        (
            "#032F雪拉倒是还好……\x02\x03",

            "虽然酒量大但至少还会脸红，\x01",
            "也会做出喝醉的举动……\x02\x03",

            "#034F但是爱娜……\x01",
            "喝多少都不动声色的……\x02\x03",

            "结果我轻易地上了钩，\x01",
            "每次劝酒就把整杯喝干……\x02\x03",

            "#037F……啊哈哈……哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1007F（嗯～看来还是\x01",
            "不要再问下去了比较好。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Jump("loc_1B1B")

    label("loc_1A96")

    TalkBegin(0xA)
    OP_43(0xA, 0x0, 0x0, 0x3)

    ChrTalk(    #8
        0xA,
        (
            "#034F爱娜……\x01",
            "喝多少都不动声色的……\x02\x03",

            "结果我轻易地上了钩，\x01",
            "每次劝酒就把整杯喝干……\x02\x03",

            "#037F……啊哈哈……哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_1B1B")

    Jump("loc_1B22")

    label("loc_1B1E")

    Call(0, 52)

    label("loc_1B22")

    Jump("loc_1B29")

    label("loc_1B25")

    Call(0, 47)

    label("loc_1B29")

    Return()

    # Function_6_17DA end

    def Function_7_1B2A(): pass

    label("Function_7_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_1BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B40")
    Call(1, 8)
    Jump("loc_1BA2")

    label("loc_1B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4F")
    Call(1, 9)
    Jump("loc_1BA2")

    label("loc_1B4F")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #9
        0xB,
        (
            "#060F米夏吗……\x02\x03",

            "#061F嘿嘿，要是见面了\x01",
            "能做好朋友就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    OP_8C(0xFE, 90, 400)

    label("loc_1BA2")

    Jump("loc_1C50")

    label("loc_1BA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB8")
    Call(1, 3)
    Jump("loc_1C50")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_1C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 4)), scpexpr(EXPR_END)), "loc_1C45")
    TalkBegin(0xB)

    ChrTalk(    #10
        0xB,
        (
            "#061F说到这个，之前在王都\x01",
            "第一次看到埃尔赛尤号的时候,\x01",
            "感觉真是一艘好漂亮的飞船呢。\x02\x03",

            "嘿嘿……不知道还能再见到吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_1C49")

    label("loc_1C45")

    Call(0, 51)

    label("loc_1C49")

    Jump("loc_1C50")

    label("loc_1C4C")

    Call(0, 50)

    label("loc_1C50")

    Return()

    # Function_7_1B2A end

    def Function_8_1C51(): pass

    label("Function_8_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_1DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C67")
    Call(1, 14)
    Jump("loc_1DCA")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7A")
    Call(1, 15)
    Jump("loc_1DCA")

    label("loc_1C7A")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D0A")
    Jump("loc_1D4C")

    label("loc_1D0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D26")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D4C")

    label("loc_1D26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D42")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D4C")

    label("loc_1D42")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D4C")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #11
        0xC,
        (
            "#070F接下来的柏斯地区\x01",
            "是靠近帝国的地方吧。\x02\x03",

            "真想看一次\x01",
            "传说中的哈肯大门啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_1DCA")

    Jump("loc_1DE4")

    label("loc_1DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE0")
    Call(1, 1)
    Jump("loc_1DE4")

    label("loc_1DE0")

    Call(0, 53)

    label("loc_1DE4")

    Return()

    # Function_8_1C51 end

    def Function_9_1DE5(): pass

    label("Function_9_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_1F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFB")
    Call(1, 12)
    Jump("loc_1F6E")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0E")
    Call(1, 13)
    Jump("loc_1F6E")

    label("loc_1E0E")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E9E")
    Jump("loc_1EE0")

    label("loc_1E9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1EBA")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EE0")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ED6")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EE0")

    label("loc_1ED6")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE0")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #12
        0xD,
        (
            "#048F呵呵，话说回来\x01",
            "好久没去柏斯了。\x02\x03",

            "自从和乔儿一起去柏斯超市\x01",
            "买东西以后就再也没去过了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)

    label("loc_1F6E")

    Jump("loc_1F75")

    label("loc_1F71")

    Call(1, 2)

    label("loc_1F75")

    Return()

    # Function_9_1DE5 end

    def Function_10_1F76(): pass

    label("Function_10_1F76")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FE7")

    ChrTalk(    #13
        0xFE,
        (
            "现在右手边\x01",
            "正好能看到迷雾峡谷哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "这迷雾高峰的深处，\x01",
            "就是和帝国之间的国境线。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207B")

    label("loc_1FE7")


    ChrTalk(    #15
        0xFE,
        (
            "哎呀，客人……\x01",
            "感谢您经常选择我们的服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "现在右手边\x01",
            "正好能看到迷雾峡谷哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "洛连特的雾虽然散了，\x01",
            "但那里的雾却是一年到头都是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_207B")

    Jump("loc_235D")

    label("loc_207E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_20F4")

    ChrTalk(    #18
        0xFE,
        (
            "本船现在正在\x01",
            "神秘森林上空飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "在抵达下一个停靠地洛连特市之前，\x01",
            "请尽情享受空中之旅。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218D")

    label("loc_20F4")


    ChrTalk(    #20
        0xFE,
        "……各位，请看。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "右手边能看到的是\x01",
            "利贝尔王国最大的森林地帯，\x01",
            "神秘森林。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "现在林业也非常繁荣，\x01",
            "国内消费木材的七成\x01",
            "据说都是产自这座森林。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_218D")

    Jump("loc_235D")

    label("loc_2190")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_21F2")

    ChrTalk(    #23
        0xFE,
        (
            "本船现在正在\x01",
            "托兰特平原上空飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "到达王都之前的时间\x01",
            "请轻松度过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_229B")

    label("loc_21F2")


    ChrTalk(    #25
        0xFE,
        (
            "现在右手边前方\x01",
            "可以看到\x01",
            "亚宁堡的长城。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "它的历史悠久，\x01",
            "据说可以追溯到\x01",
            "利贝尔王室诞生之前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "一种说法其为古代塞姆利亚文明\x01",
            "的遗迹，\x01",
            "其真伪程度则无法判断。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_229B")

    Jump("loc_235D")

    label("loc_229E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22FA")

    ChrTalk(    #28
        0xFE,
        (
            "本船现在正在\x01",
            "卡鲁迪亚丘陵上空飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "预计将会\x01",
            "准时抵达蔡斯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235D")

    label("loc_22FA")


    ChrTalk(    #30
        0xFE,
        (
            "现在右手边能看到的是\x01",
            "南部广阔的特迪斯海。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽然天气有点阴，\x01",
            "但还是能看到海岸线的形状。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_235D")

    TalkEnd(0x16)
    Return()

    # Function_10_1F76 end

    def Function_11_2361(): pass

    label("Function_11_2361")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B6")

    ChrTalk(    #32
        0xFE,
        (
            "这次和共和国大使\x01",
            "有大规模的贸易谈判。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "希望能顺利进行……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2474")

    label("loc_23B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2412")

    ChrTalk(    #34
        0xFE,
        (
            "最近一直工作，\x01",
            "都没时间休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "回到蔡斯后\x01",
            "打算先放松一阵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2474")

    label("loc_2412")


    ChrTalk(    #36
        0xFE,
        (
            "我现在正要\x01",
            "回蔡斯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "最近一直工作，\x01",
            "都没时间休息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "回到家后\x01",
            "打算先放松一阵。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2474")

    TalkEnd(0x17)
    Return()

    # Function_11_2361 end

    def Function_12_2478(): pass

    label("Function_12_2478")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24DE")

    ChrTalk(    #39
        0xFE,
        (
            "呵呵……\x01",
            "等一下哦，『埃尔赛尤』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "我要把那雪白的机体\x01",
            "统统收入这台相机里～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EC")

    label("loc_24DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2589")

    ChrTalk(    #41
        0xFE,
        (
            "哈哈，接下来是蔡斯吗～\x01",
            "工房船要是在飞船坪就好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "运气好的话，说不定\x01",
            "『埃尔赛尤』也会来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "唔呼～我太兴奋了，\x01",
            "拿相机的手都在颤抖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EC")

    label("loc_2589")


    ChrTalk(    #44
        0xFE,
        (
            "好了～到达之前\x01",
            "要好好准备相机才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "只有着陆的时候是从上方\x01",
            "拍摄飞船坪的唯一机会啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_25EC")

    TalkEnd(0xFE)
    Return()

    # Function_12_2478 end

    def Function_13_25F0(): pass

    label("Function_13_25F0")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_265F")

    ChrTalk(    #46
        0xFE,
        (
            "这次的互不侵犯条约是关键。\x01",
            "若是签定的话行情也会上涨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "在这之前能买多少\x01",
            "导力器就买多少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_265F")


    ChrTalk(    #48
        0xFE,
        (
            "西蒙，导力器那边\x01",
            "确实都准备好了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "在帝国商人们来之前\x01",
            "必须全部准备好才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_26B8")

    TalkEnd(0x19)
    Return()

    # Function_13_25F0 end

    def Function_14_26BC(): pass

    label("Function_14_26BC")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_271D")

    ChrTalk(    #50
        0xFE,
        (
            "应、应该是按照这边提出的\x01",
            "预算量准备好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "再多的库存\x01",
            "就要看今后的交涉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2788")

    label("loc_271D")


    ChrTalk(    #52
        0xFE,
        (
            "是、是的，已经向中央工房的\x01",
            "负责人传达过我们的意思了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "之后只要办理具体的买卖合约\x01",
            "手续就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2788")

    TalkEnd(0x1A)
    Return()

    # Function_14_26BC end

    def Function_15_278C(): pass

    label("Function_15_278C")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2806")

    ChrTalk(    #54
        0xFE,
        (
            "这次的互不侵犯条约，\x01",
            "是王国，帝国，共和国三大国\x01",
            "之间所缔结的。\x02\x03",

            "真希望以此为契机\x01",
            "三国的关系也得到发展。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_2806")


    ChrTalk(    #55
        0xFE,
        (
            "虽然卢安上下都在忙着选举，\x01",
            "不过王国整体来说还是签字仪式最热门。\x02\x03",

            "毕竟是要和１０年前百日战役中\x01",
            "战斗过的帝国缔结互不侵犯条约嘛。\x02\x03",

            "希望以此为契机\x01",
            "能够真正冰释前嫌。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_28B0")

    TalkEnd(0x1B)
    Return()

    # Function_15_278C end

    def Function_16_28B4(): pass

    label("Function_16_28B4")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2913")

    ChrTalk(    #56
        0xFE,
        (
            "在洛连特\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "那样的雾，我们也是\x01",
            "第一次经历呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_297E")

    label("loc_2913")


    ChrTalk(    #58
        0xFE,
        "啊啊，是客人您啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "在洛连特\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "再怎么说，要在那种浓雾下\x01",
            "升空也太危险了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_297E")

    Jump("loc_2E43")

    label("loc_2981")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_END)), "loc_2A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_29F0")

    ChrTalk(    #61
        0xFE,
        (
            "孩提时代我也憧憬过\x01",
            "王立学院呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "现在看来那里的制服\x01",
            "设计依然十分出色哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A66")

    label("loc_29F0")


    ChrTalk(    #63
        0xFE,
        (
            "孩提时代我也很向往\x01",
            "王立学院呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "嗯，虽然只是单纯\x01",
            "想穿那个制服而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "那个……当然是男生穿的\x01",
            "制服啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2A66")

    Jump("loc_2B37")

    label("loc_2A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2AC1")

    ChrTalk(    #66
        0xFE,
        (
            "哎呀呀，名校的学生\x01",
            "气质果然就是不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "一定接受了\x01",
            "严格的教育吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B37")

    label("loc_2AC1")


    ChrTalk(    #68
        0xFE,
        (
            "那边的客人……\x01",
            "是王立学院的学生吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "呀，不愧是名校的\x01",
            "学生啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "一举一动之间\x01",
            "都能透露出不凡的气质呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2B37")

    Jump("loc_2E43")

    label("loc_2B3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2B95")

    ChrTalk(    #71
        0xFE,
        (
            "我是独生子，\x01",
            "感觉真是寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "真想要个\x01",
            "弟弟或妹妹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C01")

    label("loc_2B95")


    ChrTalk(    #73
        0xFE,
        (
            "那边的\x01",
            "客人是兄妹吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "作为兄妹来说\x01",
            "感觉又不太一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "……不过，关系那么好\x01",
            "让人不禁莞尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2C01")

    Jump("loc_2D18")

    label("loc_2C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2C70")

    ChrTalk(    #76
        0xFE,
        (
            "那位弹鲁特琴的客人……\x01",
            "怎么说呢，令人感觉到他对自身的爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "那就叫做\x01",
            "Ｉ ＬＯＶＥ ＭＥ吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D18")

    label("loc_2C70")


    ChrTalk(    #78
        0xFE,
        "那位弹鲁特琴的客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "不仅是吟唱诗歌的内容，\x01",
            "连唱歌说话的方式都是那么独特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "怎么说呢……\x01",
            "令人感觉到他对自身的爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "那就叫做\x01",
            "Ｉ ＬＯＶＥ ＭＥ吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2D18")

    Jump("loc_2E43")

    label("loc_2D1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2DAA")

    ChrTalk(    #82
        0xFE,
        (
            "这个观景席平时总是\x01",
            "很受大家欢迎的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "不知道为什么今天\x01",
            "客人们都不在席上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "这果然……\x01",
            "都是因为那位客人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E43")

    label("loc_2DAA")


    ChrTalk(    #85
        0xFE,
        (
            "那位客人，现在倒是\x01",
            "很老实……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "不过刚才还在弹奏鲁特琴\x01",
            "大声唱歌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "结果还强求\x01",
            "我去唱二重唱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "呼，世上居然也有\x01",
            "这么强人所难的人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2E43")

    TalkEnd(0x1C)
    Return()

    # Function_16_28B4 end

    def Function_17_2E47(): pass

    label("Function_17_2E47")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(    #89
        0xFE,
        (
            "起雾的洛连特\x01",
            "也真是怪异。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "我们也好久没能\x01",
            "好好享受到自然了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1A")

    label("loc_2EA6")


    ChrTalk(    #91
        0xFE,
        (
            "哎呀～又是客人您啊。\x01",
            "最近常常见到呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "起雾的洛连特\x01",
            "也真是怪异。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "我们也好久没能\x01",
            "好好享受到自然了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2F1A")

    Jump("loc_318A")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2F7A")

    ChrTalk(    #94
        0xFE,
        "那位穿白色外套的客人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "一个人在嘀嘀咕咕的\x01",
            "到底是什么事呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2F7A")


    ChrTalk(    #96
        0xFE,
        (
            "刚才那边\x01",
            "穿白色外套的客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "一个人在嘀嘀咕咕，\x01",
            "到底是什么事呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "突然又笑出声来\x01",
            "感觉真是危险啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2FEE")

    Jump("loc_318A")

    label("loc_2FF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3059")

    ChrTalk(    #99
        0xFE,
        (
            "到王都可要早点做好\x01",
            "卸货的准备啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "这次要卸下的货物量\x01",
            "可不是普通的多哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D0")

    label("loc_3059")


    ChrTalk(    #101
        0xFE,
        "呀，接下来是王都吗～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "这样的话就得早点做好\x01",
            "卸货的准备才行啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "在王都要卸下的货物量\x01",
            "可不是普通的多哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_30D0")

    Jump("loc_318A")

    label("loc_30D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3143")

    ChrTalk(    #104
        0xFE,
        (
            "这里是货舱哦～\x01",
            "很危险，要多加小心～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "操舵室在这个上面一层。\x01",
            "十分推荐进去参观哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_318A")

    label("loc_3143")


    ChrTalk(    #106
        0xFE,
        (
            "哎呀～客人。\x01",
            "怎么了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "这里是货舱哦～\x01",
            "很危险，要多加小心～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_318A")

    TalkEnd(0x1D)
    Return()

    # Function_17_2E47 end

    def Function_18_318E(): pass

    label("Function_18_318E")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31B0")
    SetChrSubChip(0xFE, 1)
    Jump("loc_31C3")

    label("loc_31B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31C3")
    SetChrSubChip(0xFE, 2)

    label("loc_31C3")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3242")

    ChrTalk(    #108
        0xFE,
        (
            "这么浓的雾\x01",
            "连我也是第一次看见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "竟然打开灯之后\x01",
            "也只是照出眼前白茫茫一片而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3302")

    label("loc_3242")


    ChrTalk(    #110
        0xFE,
        "哟，出港延迟给你们添麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "不过，我干这工作这么久了\x01",
            "这样的浓雾还是头一次见到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "竟然打开灯之后\x01",
            "也只是照出眼前白茫茫一片而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "要在这种状况下飞行\x01",
            "就算是我也办不到啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_3302")

    Jump("loc_358C")

    label("loc_3305")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3363")

    ChrTalk(    #114
        0xFE,
        (
            "从这里望去的洛连特，\x01",
            "满眼翠绿的风景很特别哦。\x01",
            "感觉心灵都被治愈了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E3")

    label("loc_3363")


    ChrTalk(    #115
        0xFE,
        (
            "哦，来操舵室\x01",
            "看风景吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "从这里望去的洛连特，\x01",
            "满眼翠绿的风景很特别哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "眺望着雄伟的森林，\x01",
            "感觉心灵都被治愈了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_33E3")

    Jump("loc_358C")

    label("loc_33E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_344A")

    ChrTalk(    #118
        0xFE,
        (
            "现在正在托兰特平原\x01",
            "上空飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "天气又好，到甲板上\x01",
            "去看看风景怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C4")

    label("loc_344A")


    ChrTalk(    #120
        0xFE,
        (
            "哦，不是在参观船内部吗？\x01",
            "觉得无聊了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "现在正在托兰特平原\x01",
            "上空飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "天气又好，到甲板上\x01",
            "看看风景怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_34C4")

    Jump("loc_358C")

    label("loc_34C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_358C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_352B")

    ChrTalk(    #123
        0xFE,
        (
            "天空也很平静，\x01",
            "应该能准时到达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "既然这么悠闲，\x01",
            "到船内散散步怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_352B")


    ChrTalk(    #125
        0xFE,
        "哟，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "天空也很平静，\x01",
            "应该能准时到达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "嗯，再悠闲地\x01",
            "享受一下空中旅行吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_358C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x1E)
    Return()

    # Function_18_318E end

    def Function_19_3595(): pass

    label("Function_19_3595")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3606")

    ChrTalk(    #128
        0xFE,
        (
            "麻烦避开山脉边缘，\x01",
            "将航向往南稍微修正一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "感觉靠近东柏斯街道\x01",
            "正上方的路线。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3659")

    label("loc_3606")


    ChrTalk(    #130
        0xFE,
        (
            "操舵手。\x01",
            "稍微偏西北了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "由于山脉边缘有乱流，\x01",
            "太靠近的话就麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3659")

    Jump("loc_387C")

    label("loc_365C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_36C2")

    ChrTalk(    #132
        0xFE,
        (
            "操舵手，麻烦暂时\x01",
            "固定在现在的航向上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "嗯～今天\x01",
            "洛连特的风也很平静呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3728")

    label("loc_36C2")


    ChrTalk(    #134
        0xFE,
        (
            "没必要修正航向。\x01",
            "操舵手，舵保持这样就ＯＫ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "保持航向……\x01",
            "很快就会走上\x01",
            "进入洛连特的路线。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_3728")

    Jump("loc_387C")

    label("loc_372B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3794")

    ChrTalk(    #136
        0xFE,
        (
            "今天感觉上面有点风\x01",
            "吹下来似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "这附近的风\x01",
            "经常变化，\x01",
            "要时时注意才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E3")

    label("loc_3794")


    ChrTalk(    #138
        0xFE,
        (
            "操舵手，高度好像稍微\x01",
            "下降了一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "不要离开气流，\x01",
            "尽快修正高度吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_37E3")

    Jump("loc_387C")

    label("loc_37E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3837")

    ChrTalk(    #140
        0xFE,
        "好像又吹海风了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "这附近的空域\x01",
            "总是不能放松啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387C")

    label("loc_3837")


    ChrTalk(    #142
        0xFE,
        (
            "操舵手，麻烦\x01",
            "修正一下线路吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "船尾感觉稍微\x01",
            "偏北了一点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_387C")

    TalkEnd(0x1F)
    Return()

    # Function_19_3595 end

    def Function_20_3880(): pass

    label("Function_20_3880")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_38EF")

    ChrTalk(    #144
        0xFE,
        (
            "呼啦啦呼啦啦～⊙\x01",
            "天空的～男人～哟～⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "从这城～到那镇～⊙\x01",
            "旅行的～乌鸦～～⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_393A")

    label("loc_38EF")


    ChrTalk(    #146
        0xFE,
        (
            "呼啦啦呼啦啦～⊙\x01",
            "是～明白了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "路线向南修正～\x01",
            "呼啦啦呼啦啦～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_393A")

    Jump("loc_3AC0")

    label("loc_393D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3976")

    ChrTalk(    #148
        0xFE,
        (
            "呼啦啦呼啦啦～⊙\x01",
            "呼啦呼啦啦⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C3")

    label("loc_3976")


    ChrTalk(    #149
        0xFE,
        (
            "呼啦啦呼啦啦～⊙\x01",
            "啊～明白了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "就这样保持路线～\x01",
            "呼啦啦呼啦啦～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_39C3")

    Jump("loc_3AC0")

    label("loc_39C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_39FF")

    ChrTalk(    #151
        0xFE,
        (
            "呼啦啦呼啦啦⊙\x01",
            "呼啦啦呼啦啦⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A46")

    label("loc_39FF")


    ChrTalk(    #152
        0xFE,
        (
            "呼啦啦呼啦啦⊙\x01",
            "是～明白了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "立即恢复高度～\x01",
            "呼啦啦呼啦啦⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3A46")

    Jump("loc_3AC0")

    label("loc_3A49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3A75")

    ChrTalk(    #154
        0xFE,
        "呼啦啦呼啦啦～⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC0")

    label("loc_3A75")


    ChrTalk(    #155
        0xFE,
        (
            "呼啦啦呼啦啦～⊙\x01",
            "啊～明白了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "立即修正路线～\x01",
            "呼啦啦呼啦啦～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3AC0")

    TalkEnd(0x20)
    Return()

    # Function_20_3880 end

    def Function_21_3AC4(): pass

    label("Function_21_3AC4")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3B00")

    ChrTalk(    #157
        0xFE,
        (
            "哎呀呀，还真是\x01",
            "夸张的大雾啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B70")

    label("loc_3B00")


    ChrTalk(    #158
        0xFE,
        (
            "哎呀呀，还真是\x01",
            "夸张的雾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "而且还突然就\x01",
            "消散得无影无踪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "这么诡异的雾\x01",
            "连我都是第一次见呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3B70")

    Jump("loc_3D79")

    label("loc_3B73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3BE5")

    ChrTalk(    #161
        0xFE,
        (
            "虽然说发布了安全宣告，\x01",
            "却还是忍不住心惊肉跳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "总之现在坐在飞船上\x01",
            "倒还算安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C65")

    label("loc_3BE5")


    ChrTalk(    #163
        0xFE,
        (
            "不过，蔡斯的\x01",
            "地震也真是吓人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "全部都是局部地震，\x01",
            "而且还发生在很多地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "我活了这么久，\x01",
            "这还是头一次见到呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3C65")

    Jump("loc_3D79")

    label("loc_3C68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3CD4")

    ChrTalk(    #166
        0xFE,
        (
            "若不是通晓技术的人，\x01",
            "是不可能统领蔡斯市的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "让工房长兼任市长\x01",
            "真是个好主意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D79")

    label("loc_3CD4")


    ChrTalk(    #168
        0xFE,
        (
            "卢安市正热衷于\x01",
            "市长选举……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "不过现在要去的蔡斯市\x01",
            "却没有市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "取而代之的是由中央工房\x01",
            "的工房长统领整个地区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "真是个适合工房都市的\x01",
            "管理架构啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3D79")

    TalkEnd(0x21)
    Return()

    # Function_21_3AC4 end

    def Function_22_3D7D(): pass

    label("Function_22_3D7D")

    TalkBegin(0x22)

    ChrTalk(    #172
        0xFE,
        (
            "互不侵犯条约的签字仪式\x01",
            "似乎顺利结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "唔，希望以此为契机\x01",
            "来促进三国的融洽关系。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_22_3D7D end

    def Function_23_3DE0(): pass

    label("Function_23_3DE0")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3E18")

    ChrTalk(    #174
        0xFE,
        (
            "柏斯有家著名的\x01",
            "餐厅呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "我知道！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E67")

    label("loc_3E18")


    ChrTalk(    #176
        0xFE,
        (
            "柏斯有家著名的\x01",
            "餐厅呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "我知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "对了，妈妈～\x01",
            "去那里吃饭嘛～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3E67")

    TalkEnd(0x23)
    Return()

    # Function_23_3DE0 end

    def Function_24_3E6B(): pass

    label("Function_24_3E6B")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_3ECA")

    ChrTalk(    #179
        0xFE,
        (
            "我家的孩子居然说\x01",
            "想去那个安特洛丝\x01",
            "吃饭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "小孩子真是天真。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F33")

    label("loc_3ECA")


    ChrTalk(    #181
        0xFE,
        "真是的，我家这孩子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "居然说想去那个安特洛丝\x01",
            "吃饭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "唉，真好。\x01",
            "小孩子就是这么天真。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_3F33")

    Jump("loc_404F")

    label("loc_3F36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_3FA6")

    ChrTalk(    #184
        0xFE,
        (
            "艾德尔百货商店里的\x01",
            "商品质量确实好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "最近，那家百货店\x01",
            "似乎也成为流行的发源地了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_404F")

    label("loc_3FA6")


    ChrTalk(    #186
        0xFE,
        (
            "说到要去王都购物的话，\x01",
            "首选就是艾德尔百货店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "虽然好像比柏斯超市\x01",
            "规模要小，\x01",
            "但是商品质量的确很好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "啊～啊，要是有时间和钱的话，\x01",
            "真想顺路去购物啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_404F")

    TalkEnd(0x24)
    Return()

    # Function_24_3E6B end

    def Function_25_4053(): pass

    label("Function_25_4053")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_40AA")

    ChrTalk(    #189
        0xFE,
        (
            "这阵子\x01",
            "柏斯好像很平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "唔，柏斯超市\x01",
            "想必很热闹吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_410A")

    label("loc_40AA")


    ChrTalk(    #191
        0xFE,
        (
            "这阵子\x01",
            "柏斯好像很平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "利贝尔通讯上\x01",
            "没什么特别的报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "唔，真应该\x01",
            "感到高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_410A")

    Jump("loc_41E9")

    label("loc_410D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_416D")

    ChrTalk(    #194
        0xFE,
        (
            "这次的互不侵犯条约，\x01",
            "我原则上是支持的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "能重归于好\x01",
            "总是件好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E9")

    label("loc_416D")


    ChrTalk(    #196
        0xFE,
        (
            "这次的互不侵犯条约，\x01",
            "我原则上是支持的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "对于帝国，老实说\x01",
            "感觉依然很复杂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "总之能重归于好\x01",
            "还是件好事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_41E9")

    TalkEnd(0x25)
    Return()

    # Function_25_4053 end

    def Function_26_41ED(): pass

    label("Function_26_41ED")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_426A")

    ChrTalk(    #199
        0xFE,
        (
            "那个艾德尔百货店的店长\x01",
            "好像也是超市的爱好者呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "在店长所写的巡礼札记里\x01",
            "好像提过这样的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E0")

    label("loc_426A")


    ChrTalk(    #201
        0xFE,
        (
            "柏斯的超市\x01",
            "简直是购物的天堂……\x01",
            "对女性来说是个向往之地啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "那个艾德尔百货店的店长\x01",
            "也是私底下的爱好者呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_42E0")

    Jump("loc_4355")

    label("loc_42E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4355")

    ChrTalk(    #203
        0xFE,
        (
            "互不侵犯条约好像是三国之间\x01",
            "所缔结的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "能维持帝国和共和国的关系\x01",
            "真不愧是艾莉茜雅女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4355")

    TalkEnd(0x26)
    Return()

    # Function_26_41ED end

    def Function_27_4359(): pass

    label("Function_27_4359")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x27)
    ClearChrFlags(0x27, 0x10)
    TurnDirection(0x27, 0x0, 0)
    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43E9")
    Jump("loc_442B")

    label("loc_43E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4405")
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_442B")

    label("loc_4405")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4421")
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_442B")

    label("loc_4421")

    OP_51(0x27, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_442B")

    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x27, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A9")

    ChrTalk(    #205
        0xFE,
        (
            "瓦雷利亚湖畔\x01",
            "好像有不错的旅店哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "最近在钓客之间\x01",
            "似乎很流行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FB")

    label("loc_44A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_451F")

    ChrTalk(    #207
        0xFE,
        (
            "当天，签字仪式会场的离宫\x01",
            "好像一律禁止民间人士入内呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "真想亲眼目睹\x01",
            "条约缔结的瞬间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D1")

    label("loc_451F")


    ChrTalk(    #209
        0xFE,
        "这次的互不侵犯条约签字仪式……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "当天，会场艾尔贝离宫\x01",
            "好像一律禁止民间人士入内呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "毕竟刚刚发生过政变，\x01",
            "这也是没办法的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "真想亲眼目睹\x01",
            "条约缔结的瞬间啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_45D1")

    Jump("loc_46FB")

    label("loc_45D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_466F")

    ChrTalk(    #213
        0xFE,
        (
            "不过，旧情报部的残党\x01",
            "好像还没有抓到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "虽然大家可能都忘了，\x01",
            "但实在是非常可怕的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "呼，和平这种东西\x01",
            "真是容易破坏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FB")

    label("loc_466F")


    ChrTalk(    #216
        0xFE,
        (
            "互不侵犯条约的签字仪式\x01",
            "似乎在艾尔贝离宫进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "说到艾尔贝离宫……\x01",
            "就想起理查德的事件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "那家伙似乎被拘禁在\x01",
            "雷斯顿要塞里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_46FB")

    SetChrSubChip(0x27, 0)
    TalkEnd(0x27)
    Return()

    # Function_27_4359 end

    def Function_28_4704(): pass

    label("Function_28_4704")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_4781")

    ChrTalk(    #219
        0xFE,
        (
            "对士兵们来说\x01",
            "帝国的存在似乎还是\x01",
            "相当大的心理负担啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "这次的互不侵犯条约\x01",
            "最支持的人，\x01",
            "说不定是他们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_480E")

    label("loc_4781")


    ChrTalk(    #221
        0xFE,
        (
            "我的朋友是驻扎在\x01",
            "哈肯大门的士兵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "帝国的存在似乎还是\x01",
            "相当大的心理负担啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "这次的互不侵犯条约\x01",
            "最支持的\x01",
            "说不定是士兵们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_480E")

    TalkEnd(0x28)
    Return()

    # Function_28_4704 end

    def Function_29_4812(): pass

    label("Function_29_4812")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_487D")

    ChrTalk(    #224
        0xFE,
        (
            "遗憾的是这女孩\x01",
            "似乎很快要去柏斯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "如果是这孩子的话，我儿子里农\x01",
            "应该也会喜欢的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4921")

    label("loc_487D")


    ChrTalk(    #226
        0xFE,
        "呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "结果，王都也找不到\x01",
            "能做里农新娘的女孩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "回来的船上能遇到谈得来的女孩\x01",
            "可以说是捡到救命稻草了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "这样的孩子我儿子里农\x01",
            "一定会喜欢的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_4921")

    TalkEnd(0x2A)
    Return()

    # Function_29_4812 end

    def Function_30_4925(): pass

    label("Function_30_4925")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_499D")

    ChrTalk(    #230
        0xFE,
        (
            "虽然很想去看看\x01",
            "婆婆的店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "不过现在利用休假\x01",
            "正要去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "难得能够彼此认识，\x01",
            "真有点可惜……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A44")

    label("loc_499D")


    ChrTalk(    #233
        0xFE,
        (
            "这位婆婆似乎在洛连特\x01",
            "经营商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "我也在王都的百货店工作\x01",
            "所以很谈得来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "个人经营的商店…\x01",
            "实在是很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "哪怕是家很小的店，\x01",
            "我也想自己开店啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_4A44")

    TalkEnd(0x2B)
    Return()

    # Function_30_4925 end

    def Function_31_4A48(): pass

    label("Function_31_4A48")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_4ABE")

    ChrTalk(    #237
        0xFE,
        (
            "呀～神秘森林的\x01",
            "风景虽然很不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "但那边的女乘务员\x01",
            "也毫不逊色呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "嗯～越来越不想\x01",
            "下船了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4F")

    label("loc_4ABE")


    ChrTalk(    #240
        0xFE,
        (
            "呀～从飞船上看\x01",
            "神秘森林真是壮观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "看见这片大森林\x01",
            "就能感受到洛连特地区\x01",
            "多么受大自然的眷顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "嗯～真想就这样\x01",
            "一直眺望下去啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_4B4F")

    TalkEnd(0x2C)
    Return()

    # Function_31_4A48 end

    def Function_32_4B53(): pass

    label("Function_32_4B53")

    TalkBegin(0x2D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_4BB8")

    ChrTalk(    #243
        0xFE,
        (
            "洛连特好像也有\x01",
            "很不错的钓场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "因为不是很出名，\x01",
            "感觉是个罕为人知的好地方哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C40")

    label("loc_4BB8")


    ChrTalk(    #245
        0xFE,
        (
            "洛连特好像也有\x01",
            "很不错的钓场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "因为不是很出名，\x01",
            "感觉是个罕为人知的好地方哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "嗯～真想在到站之后\x01",
            "先去挑战一下试试啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_4C40")

    TalkEnd(0x2D)
    Return()

    # Function_32_4B53 end

    def Function_33_4C44(): pass

    label("Function_33_4C44")

    TalkBegin(0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_4CC3")

    ChrTalk(    #248
        0xFE,
        (
            "洛连特地区是我很想好好\x01",
            "游览一下的地方之一呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "美味的食物加上清新的空气……\x01",
            "真是个雕琢美丽的最佳环境啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7B")

    label("loc_4CC3")


    ChrTalk(    #250
        0xFE,
        "下一个停靠港是洛连特啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "这次虽然不去，\x01",
            "但以后真想去农场住一阵呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "美味的食物加上清新的空气……\x01",
            "真是个雕琢美丽的最佳环境啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "呵呵，他也想钓鱼\x01",
            "下次约他看看吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_4D7B")

    TalkEnd(0x2E)
    Return()

    # Function_33_4C44 end

    def Function_34_4D7F(): pass

    label("Function_34_4D7F")

    TalkBegin(0x2F)

    ChrTalk(    #254
        0xFE,
        (
            "明天终于就是\x01",
            "那个互不侵犯条约的签字仪式了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "百日战役终结\x01",
            "已经过了１０年了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "或许是该和帝国\x01",
            "重归于好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2F)
    Return()

    # Function_34_4D7F end

    def Function_35_4E03(): pass

    label("Function_35_4E03")

    TalkBegin(0x30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_4E62")

    ChrTalk(    #257
        0xFE,
        (
            "和帝国和解的时候\x01",
            "总算要真正到来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "这样回想起来\x01",
            "１０年真是转眼即逝啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF0")

    label("loc_4E62")


    ChrTalk(    #259
        0xFE,
        (
            "不久前还完全无法想象\x01",
            "能够和帝国和解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "这个时刻\x01",
            "总算要真正到来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "这是不断踏实地进行外交努力的\x01",
            "艾莉茜雅女王陛下的胜利啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_4EF0")

    TalkEnd(0x30)
    Return()

    # Function_35_4E03 end

    def Function_36_4EF4(): pass

    label("Function_36_4EF4")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F84")
    Jump("loc_4FC6")

    label("loc_4F84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FA0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FC6")

    label("loc_4FA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FBC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FC6")

    label("loc_4FBC")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC6")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_504B")

    ChrTalk(    #262
        0xFE,
        (
            "得赶快把事情办完，\x01",
            "赶快回家才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "我老婆只会使唤人，\x01",
            "还啰嗦…真是受够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A7")

    label("loc_504B")


    ChrTalk(    #264
        0xFE,
        (
            "今天也是老婆叫我\x01",
            "非去趟柏斯超市\x01",
            "不可。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "我老婆只会使唤人，\x01",
            "还啰嗦…真是受够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_50A7")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_36_4EF4 end

    def Function_37_50B0(): pass

    label("Function_37_50B0")

    TalkBegin(0x32)

    ChrTalk(    #266
        0xFE,
        (
            "嘿嘿，我要去柏斯超市\x01",
            "帮爸爸买东西哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "买东西，买东西，好开心～⊙\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x32)
    Return()

    # Function_37_50B0 end

    def Function_38_5102(): pass

    label("Function_38_5102")

    TalkBegin(0x33)

    ChrTalk(    #268
        0xFE,
        "说不行就是不行！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "你啊，之前也是这么说\x01",
            "结果又爬上甲板栏杆的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "无论如何，\x01",
            "都要给我乖乖待在这里！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x33, 0)
    TalkEnd(0x33)
    TalkEnd(0x33)
    Return()

    # Function_38_5102 end

    def Function_39_5181(): pass

    label("Function_39_5181")

    TalkBegin(0x34)

    ChrTalk(    #271
        0xFE,
        "来啦，姐姐～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "别老是坐着，\x01",
            "出去外面啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "我绝对会\x01",
            "乖乖听话的啦～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x34)
    Return()

    # Function_39_5181 end

    def Function_40_51D6(): pass

    label("Function_40_51D6")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_522D")

    ChrTalk(    #274
        0xFE,
        (
            "听说政变的主谋\x01",
            "全都抓住了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "不过说不定有人\x01",
            "已经逃亡到国外了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52BC")

    label("loc_522D")


    ChrTalk(    #276
        0xFE,
        (
            "唔，接下来是艾莉茜雅女王的\x01",
            "所在地，花之都格兰赛尔吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "虽然内心是雀跃不已,\x01",
            "但总忍不住\x01",
            "想起政变的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "希望别再发生第二次了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_52BC")

    TalkEnd(0x35)
    Return()

    # Function_40_51D6 end

    def Function_41_52C0(): pass

    label("Function_41_52C0")

    TalkBegin(0x36)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_5319")

    ChrTalk(    #279
        0xFE,
        (
            "说起来，卢安\x01",
            "好像有什么\x01",
            "出现幽灵的奇怪传言……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "在那之后怎样了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_53D2")

    label("loc_5319")


    ChrTalk(    #281
        0xFE,
        (
            "……说起来，很快就是\x01",
            "卢安市的市长选举了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "旅游业推进派的诺曼氏\x01",
            "和港湾地区代表的波尔多斯氏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "结果到底会是哪位候选人\x01",
            "当选呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "就算不是卢安市民\x01",
            "也非常地关心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_53D2")

    TalkEnd(0x36)
    Return()

    # Function_41_52C0 end

    def Function_42_53D6(): pass

    label("Function_42_53D6")

    TalkBegin(0x37)

    ChrTalk(    #285
        0xFE,
        (
            "哦哦～那就是\x01",
            "传说中的长城吗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "如果是遗迹的话，说不定有\x01",
            "不为人知的宝物沉眠在地下呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x37)
    Return()

    # Function_42_53D6 end

    def Function_43_543B(): pass

    label("Function_43_543B")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x29, 0x40)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x101, 87690, -1000, 52960, 90)
    SetChrPos(0x29, 88760, -1000, 52950, 270)
    OP_6D(88640, -1000, 48310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 91200, 200, 47000, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 86380, 0, 45000, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 86380, 0, 46350, 180)
    FadeToBright(1500, 0)

    def lambda_5501():
        OP_6D(88300, -1000, 52980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5501)

    def lambda_5519():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5519)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #287
        0x101,
        (
            "#007F#6P嗯……\x01",
            "是凯文先生吧。\x02\x03",

            "对不起……\x01",
            "我失态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x29,
        (
            "#1061F没关系，没关系。\x01",
            "把胸膛借给女孩子真是赚到了。\x02\x03",

            "#1060F怎样，镇定一点了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#008F#6P……嗯。\x02\x03",

            "我叫艾丝蒂尔。\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "隶属于游击士协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x29,
        (
            "#1061F艾丝蒂尔吗～\x01",
            "名字也这么可爱啊。\x02\x03",

            "………………………………\x02\x03",

            "#1064F……嗯，游击士协会？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#006F#6P嗯，我可是个游击士哦。\x02\x03",

            "#506F嘿嘿，让你看到那么丢脸的样子\x01",
            "可能很难相信吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x29,
        (
            "#1060F不，没这种事。\x01",
            "仔细一看确实是很相称的打扮。\x02\x03",

            "你应该是练什么武术的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        (
            "#501F#6P是棒术，练了一点而已。\x02\x03",

            "#006F这么说来凯文先生\x01",
            "真的是教会的神父吗？\x02\x03",

            "怎么看都不像。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x29,
        (
            "#1068F哎呀，真过分呢。\x02\x03",

            "#1066F不过，我是巡回神父……\x01",
            "性质上倒是真的有些不同啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#505F#6P巡回神父？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x29,
        (
            "#1060F有些村子没有礼拜堂对吧？\x02\x03",

            "我就是定期造访这些村子\x01",
            "并进行礼拜和主日学校教学的神父。\x02\x03",

            "嗯，就相当于教会的外派服务啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#000F#6P原来如此……\x01",
            "还有这样的神父啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x29,
        (
            "#1061F嗯，和在礼拜堂任职的神父不同，\x01",
            "很多人对法衣什么的都很随便的。\x02\x03",

            "就是这样，别太认真啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#506F#6P嗯～也罢。\x02\x03",

            "#501F那么，凯文先生\x01",
            "现在要去哪个村子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x29,
        (
            "#1060F呀～其实我\x01",
            "才刚刚来到利贝尔。\x02\x03",

            "巡回神父的人手似乎不足，\x01",
            "所以才被总部派过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#501F#6P啊，是这样啊。\x02\x03",

            "#505F教会的总部……\x01",
            "我还不知道在哪里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x29,
        (
            "#1060F塞姆里亚大陆中部的国家——\x01",
            "亚尔特利亚法典国。\x02\x03",

            "#1061F所以呢，去格兰赛尔大圣堂\x01",
            "向大主教做上任报告之前\x01",
            "打算先四处逛一下啦。\x02\x03",

            "然后就这样像闲逛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#007F#6P这…………这怎么行。\x02\x03",

            "#509F真是个散漫的神父啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x29,
        (
            "#1062F这没什么啦。\x01",
            "只是先视察一下将来要巡回的地方。\x02\x03",

            "而且还能像这样碰上\x01",
            "有烦恼的可爱女孩～\x02\x03",

            "#1071F嗯嗯，这一定是女神的指引。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#506F#6P你还真油嘴滑舌。\x02\x03",

            "#006F不过……谢谢你。\x01",
            "哭出来就好受多了。\x02\x03",

            "不行啊，嗯。\x01",
            "一定要相信约修亚才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x29,
        "#1064F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        (
            "#008F#6P啊，约修亚是像我\x01",
            "弟弟一样的男孩。\x02\x03",

            "但突然就失踪了，\x01",
            "我有点惊慌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x29,
        (
            "#1063F突然失踪……\x02\x03",

            "是离家出走吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        (
            "#506F#6P不，不是的。\x01",
            "只是先我一步回家了而已。\x02\x03",

            "因为我们是一家人嘛。\x01",
            "不可能随便走掉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x29,
        "#1063F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        (
            "#503F#6P不过，我还真是失败啊。\x01",
            "可能是告白的时机太差了吧。\x02\x03",

            "见到约修亚之后\x01",
            "可要好好蒙混过去才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x29,
        (
            "#1063F………………………………\x02\x03",

            "#1065F……对了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#004F#6P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x29,
        (
            "#1067F不……\x02\x03",

            "…………………………………\x02\x03",

            "#1060F刚才说过了，\x01",
            "我正在旅行中没什么要事。\x02\x03",

            "所以，到了洛连特我就下船\x01",
            "送艾丝蒂尔回家吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#004F#6P#3S咦咦！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x29, 0)
    SetChrChipByIndex(0x29, 65535)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_543B end

    def Function_44_5E2D(): pass

    label("Function_44_5E2D")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_A2(0x1240)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_44_5E2D end

    def Function_45_5E3F(): pass

    label("Function_45_5E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6314")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #316
        0x8,
        (
            "#052F#2P怎么，艾丝蒂尔。\x01",
            "还在船里闲逛呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        (
            "#1016F#6P嗯，是啊。\x02\x03",

            "我以前都\x01",
            "不太常搭乘飞船，\x01",
            "感觉挺新鲜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x8,
        (
            "#051F#2P正游击士经常出差，\x01",
            "会经常乘坐飞船的。\x02\x03",

            "差不多和交易商的\x01",
            "乘坐频率一样高吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1015F#6P我老爸确实也\x01",
            "经常出差呢。\x02\x03",

            "他现在在干什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x8,
        (
            "#051F#2P被推上军队领导层后\x01",
            "应该忙得团团转吧。\x02\x03",

            "呵，他平时一副从容不迫的样子，\x01",
            "这下真是活该。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1016F#6P嗯～忙碌的老爸\x01",
            "真是难以想象……\x02\x03",

            "#1011F不过阿加特，基本上对\x01",
            "老爸的评价还是肯定的吧。\x02\x03",

            "那为什么总是\x01",
            "说得好像很讨厌他？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x8,
        (
            "#551F#2P……也不是说\x01",
            "讨厌他啦。\x02\x03",

            "#555F追根究底，失礼的人\x01",
            "怎么说都应该是你老爸吧？\x02\x03",

            "每次看到别人老是说\x01",
            "『辛苦了』『厉害厉害』之类的，\x01",
            "把别人当成小孩子看待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#1007F#6P嗯～老爸确实\x01",
            "喜欢捉弄人。\x02\x03",

            "不过，他总是那么口没遮拦\x01",
            "所以我也没怎么在意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x8,
        (
            "#051F#2P你啊，幸好是女儿。\x02\x03",

            "要是儿子的话\x01",
            "现在可是正值叛逆期呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        "#1008F#6P是、是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x8,
        (
            "#551F#2P所谓老爸，对儿子来说\x01",
            "是一道必须逾越的障壁嘛。\x02\x03",

            "要是有那样高得离谱的障壁,\x01",
            "搞不好会陷入自卑情结之中无法自拔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x101,
        (
            "#1016F#6P嗯～……\x01",
            "虽然我不太能理解。\x02\x03",

            "#1006F不过说穿了就是阿加特\x01",
            "对老爸感到有自卑情结？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x8,
        "#052F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x101,
        "#1004F#6P咦，猜中了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x8,
        "#552F#2P……啰嗦，真是有其父必有其女。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1404)
    EventEnd(0x0)
    SetChrSubChip(0x8, 0)
    Jump("loc_63AA")

    label("loc_6314")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6339")
    SetChrSubChip(0xFE, 2)
    Jump("loc_6354")

    label("loc_6339")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_634F")
    SetChrSubChip(0xFE, 2)
    Jump("loc_6354")

    label("loc_634F")

    SetChrSubChip(0xFE, 1)

    label("loc_6354")

    OP_8C(0x8, 360, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #331
        0x8,
        (
            "#552F真是的，下一站是蔡斯啦。\x02\x03",

            "马上就要到了\x01",
            "别再到处乱晃啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)

    label("loc_63AA")

    Return()

    # Function_45_5E3F end

    def Function_46_63AB(): pass

    label("Function_46_63AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693B")
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #332
        0x9,
        (
            "#526F#2P哎呀，艾丝蒂尔。\x01",
            "还在船里散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        (
            "#1016F#6P嗯，是啊。\x02\x03",

            "我以前都\x01",
            "没怎么坐过飞船，\x01",
            "感觉挺新鲜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x9,
        (
            "#021F#2P记得我因工作而\x01",
            "刚刚开始乘坐飞船的时候，\x01",
            "每次都很兴奋呢。\x02\x03",

            "因为在以前的旅途中，\x01",
            "我一次也没坐过飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1011F#6P说起来，雪拉姐\x01",
            "原来是旅行艺人剧团里的吧。\x02\x03",

            "是用导力装置的\x01",
            "车子来代步旅行的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "#027F#2P呵呵，怎么可能。\x01",
            "几乎所有的车都是马车。\x02\x03",

            "只有团长\x01",
            "有辆二手的导力驱动车。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        (
            "#1015F#6P嗯～这样啊。\x02\x03",

            "这么说来，很久以前，\x01",
            "雪拉姐的剧团来镇上的时候\x01",
            "就排了好多辆大蓬马车呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x9,
        (
            "#021F#2P哎呀，亏你还记得呢。\x02\x03",

            "#526F不过飞船啊，在利贝尔以外\x01",
            "似乎还完全没有普及。\x02\x03",

            "除此以外的导力驱动交通工具\x01",
            "现在好像正在大量使用呢。\x02\x03",

            "埃雷波尼亚听说使用导力铁路\x01",
            "来连接主要都市。\x02\x03",

            "相邻的卡尔瓦德共和国则是\x01",
            "有『导力汽车』在街道上跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#1004F#6P导力……巴士？\x02\x03",

            "#1015F那是怎样的交通工具？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x9,
        (
            "#020F#2P是大型的共乘导力车。\x02\x03",

            "和飞船一样，支付车费之后\x01",
            "就可以从这个城市坐到另一个城市。\x02\x03",

            "虽然不是很快，\x01",
            "不过也别有一番悠闲的风情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1001F#6P哟～\x01",
            "真有点想坐坐看呢。\x02\x03",

            "#1006F这么说来雪拉姐\x01",
            "曾经去过共和国吧。\x02\x03",

            "听说是在那个时候认识金先生的，\x01",
            "是为了什么事情而去的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x9,
        (
            "#027F#2P是帮卡西乌斯老师的忙。\x02\x03",

            "代替老师把某文件\x01",
            "送去卡尔瓦德的东方人街。\x02\x03",

            "就是在那里认识了金先生的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        (
            "#1011F#6P这样啊……\x02\x03",

            "#1015F东方人街……\x01",
            "无法想象是个怎样的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x9,
        (
            "#021F#2P呵呵，文化和街景都不一样，\x01",
            "是个很刺激的地方哦。\x02\x03",

            "你要是有机会的话，\x01",
            "去一次也挺不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1405)
    EventEnd(0x0)
    SetChrSubChip(0x9, 0)
    Jump("loc_69D4")

    label("loc_693B")

    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6960")
    SetChrSubChip(0xFE, 2)
    Jump("loc_697B")

    label("loc_6960")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6976")
    SetChrSubChip(0xFE, 2)
    Jump("loc_697B")

    label("loc_6976")

    SetChrSubChip(0xFE, 1)

    label("loc_697B")

    OP_8C(0x9, 360, 0)
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #345
        0x9,
        (
            "#020F接下来是蔡斯，\x01",
            "很快就会到了。\x02\x03",

            "别到处乱晃而\x01",
            "错过了下船哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)

    label("loc_69D4")

    Return()

    # Function_46_63AB end

    def Function_47_69D5(): pass

    label("Function_47_69D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7066")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(89060, -1000, 51690, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 89560, -1000, 51470, 270)
    SetChrSubChip(0xA, 2)
    OP_0D()

    ChrTalk(    #346
        0xA,
        (
            "#030F哎呀，艾丝蒂尔。\x01",
            "在享受空中之旅吗？\x02\x03",

            "#031F看吧……\x01",
            "这雄伟的天空的颜色！\x02\x03",

            "简直是最棒的\x01",
            "佐酒佳肴啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1016F嗯，天气这么好\x01",
            "我也认为景色很美……\x02\x03",

            "不过很快就要到蔡斯了，\x01",
            "喝酒是不是不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xA,
        (
            "#030F呼……\x01",
            "别这么说嘛。\x02\x03",

            "#034F在这天空下的某处\x01",
            "有那可爱的约修亚……\x02\x03",

            "啊啊，他现在在想着什么\x01",
            "继续着他的旅程呢……\x02\x03",

            "#030F一想到这种事，\x01",
            "就忍不住要喝酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        (
            "#1019F……这个，完全是\x01",
            "我的台词吧。\x02\x03",

            "#1007F真是的，有奥利维尔在\x01",
            "话题就深刻不了，不过还真是得救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xA,
        (
            "#031F呵呵……\x01",
            "得您称誉实在是光荣至极。\x02\x03",

            "#030F……不过，我稍微放心点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        "#1004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        (
            "#035F『漆黒之牙』……\x02\x03",

            "我还以为听了那怪盗留下的话\x01",
            "你会有所动摇呢。\x02\x03",

            "#030F不过，你的决心似乎\x01",
            "比我想象中的更加坚定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1025F啊……\x02\x03",

            "#1016F嘿嘿，奥利维尔真是的……\x01",
            "你在为我担心吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xA,
        (
            "#031F呵呵，因为我是寻求着爱而彷徨\x01",
            "的诗人兼演奏家嘛。\x02\x03",

            "是恋爱中少女的伙伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        "#1013F啊，呜……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xA,
        (
            "#030F哦。\x01",
            "棒术就免了吧。\x02\x03",

            "不过是开个玩笑嘛。\x01",
            "只是觉得有些令人莞尔而已。\x02\x03",

            "就是那身衣服\x01",
            "也是为了让约修亚看\x01",
            "而新换的吧？\x02\x03",

            "#031F嗯，非常适合你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        (
            "#1017F谢，谢谢……\x02\x03",

            "#1007F真是的……不要突然\x01",
            "认真地说出这么让人难为情的事啦。\x02\x03",

            "还有这身衣服，是雪拉姐\x01",
            "送给我作为贺礼的。\x02\x03",

            "#1013F想让约修亚看……\x01",
            "……虽，虽然是有想过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xA,
        "#033F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1019F怎、怎么了，不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xA,
        (
            "#035F呵呵……\x01",
            "没什么，只是觉得有些超乎预想。\x02\x03",

            "#030F嗯，这话题\x01",
            "就到此为止吧。\x02\x03",

            "艾丝蒂尔也来一杯怎么样？\x01",
            "请你喝鸡尾酒哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1015F嗯～我心领了。\x01",
            "马上就要到蔡斯了。\x02\x03",

            "#1006F奥利维尔也要适可而止，\x01",
            "不然会醉倒错过下船的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xA,
        (
            "#031F呼，不必担心。\x02\x03",

            "我奥利维尔，除了美女劝酒以外\x01",
            "从来就没有醉倒过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        "#1007F这也没什么好得意的啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1406)
    EventEnd(0x0)
    SetChrSubChip(0xA, 0)
    Jump("loc_7386")

    label("loc_7066")

    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_708B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_70A6")

    label("loc_708B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70A1")
    SetChrSubChip(0xFE, 2)
    Jump("loc_70A6")

    label("loc_70A1")

    SetChrSubChip(0xFE, 1)

    label("loc_70A6")

    OP_8C(0xA, 360, 0)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_END)), "loc_7135")

    ChrTalk(    #364
        0xA,
        (
            "#031F那么，接下来是蔡斯地区吗。\x02\x03",

            "上次是直接跑去亚尔摩温泉，\x01",
            "都没好好逛过其它的地方。\x02\x03",

            "趁这次机会\x01",
            "可要好好观光一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737E")

    label("loc_7135")


    ChrTalk(    #365
        0xA,
        (
            "#033F对了，艾丝蒂尔。\x01",
            "不介意的话读一下这本书吧？\x02\x03",

            "#031F这个虽然很有趣，\x01",
            "不过在帝国却是禁止发行的书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#1019F禁止发行……是什么\x01",
            "可疑的书啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xA,
        (
            "#030F不是不是，是卡尔瓦德共和国\x01",
            "作为舞台的娱乐小说。\x02\x03",

            "出于不利于教育的理由，\x01",
            "所以没有在帝国出版。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        (
            "#1013F啊，原来如此……\x01",
            "帝国还真是严格呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "#030F虽然曾经听过评论，\x01",
            "但这次总算是看过了。\x02\x03",

            "#035F和传闻不同，内容\x01",
            "相当值得一看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        "#1011F哦～是怎样的故事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xA,
        (
            "#030F唔，反正我也看完了，\x01",
            "不介意的话就给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        (
            "#1001F可以吗？\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x39, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #373
        "\x07\x00得到了\x1F\x3C\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23C, 1)
    OP_A2(0x10B7)

    label("loc_737E")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_7386")

    Return()

    # Function_47_69D5 end

    def Function_48_7387(): pass

    label("Function_48_7387")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #374
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #375
        (
            "\x07\x05本船即将\x01",
            "抵达蔡斯市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #376
        (
            "\x07\x05着陆时会有少许摇晃，\x01",
            "请尽快回到座位上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_742A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_742E")

    label("loc_742A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_742E")

    AddParty(0x4, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    NewScene("ED6_DT21/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_7387 end

    def Function_49_7440(): pass

    label("Function_49_7440")

    EventBegin(0x0)
    OP_6D(88630, 0, 2860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88630, 0, 2860, 270)
    FadeToBright(1000, 0)
    OP_A2(0x1681)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_49_7440 end

    def Function_50_74A0(): pass

    label("Function_50_74A0")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xB, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #377
        0xB,
        "#061F啊，姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x8,
        (
            "#051F#6P怎么，艾丝蒂尔。\x02\x03",

            "还～在船内\x01",
            "到处闲逛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x101,
        (
            "#1007F真是的，别说得人\x01",
            "像野猫一样啦。\x02\x03",

            "#1008F一直坐着等待，\x01",
            "感觉静不下心来嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        (
            "#051F#6P你去过卢·洛克尔的\x01",
            "训练场了吧？\x02\x03",

            "坐飞船也要花半天时间，\x01",
            "不是很无聊吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        (
            "#1016F那次啊，去和回来\x01",
            "都是一下子就睡着了～\x02\x03",

            "去的时候因为紧张而睡眠不足，\x01",
            "回来是因为训练太疲劳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x8,
        "#551F#6P真拿你没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xB,
        (
            "#061F嘻嘻……\x01",
            "很像是姐姐的风格吧。\x02\x03",

            "#066F不过，我也好想\x01",
            "去外国一次啊。\x02\x03",

            "那样说不定也可以\x01",
            "去见爸爸妈妈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#1025F啊，是哦。\x02\x03",

            "提妲的爸爸妈妈\x01",
            "好像因工作出国去了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xB,
        (
            "#560F嗯……\x02\x03",

            "到导力器还没有普及的国家\x01",
            "去做技术指导了……\x02\x03",

            "已经快两年都没回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1015F嗯～还真久啊。\x02\x03",

            "有互通书信吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xB,
        (
            "#061F嗯，一个月一次吧⊙\x02\x03",

            "#060F前不久我写了姐姐们的事，\x01",
            "收到了爸妈的回信……\x02\x03",

            "要我代他们向你们问好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        (
            "#1016F嘿嘿，是吗。\x02\x03",

            "#1006F话说回来提妲的父母\x01",
            "是怎样的人呢？\x02\x03",

            "妈妈一定像提妲吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xB,
        (
            "#064F嗯～很难说吧？\x02\x03",

            "#060F性格嘛，特别有精神的一个人，\x01",
            "很有活力的感觉吧。\x02\x03",

            "#061F总是马上就和爷爷\x01",
            "扭在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x101,
        "#1004F扭、扭在一起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xB,
        (
            "#067F啊，其实并不是\x01",
            "关系不好哦？\x02\x03",

            "爸爸说，那也是\x01",
            "亲子关系好的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x101,
        (
            "#1016F是、是吗。\x02\x03",

            "#1011F那么\x01",
            "爸爸是怎样的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xB,
        (
            "#560F嗯，是个很沉静\x01",
            "又很壮实的人。\x02\x03",

            "听说十多年前\x01",
            "曾经当过游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        "#1004F咦，是这样吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x8,
        (
            "#051F#6P听老爷子说\x01",
            "好像还相当厉害哦。\x02\x03",

            "由于受伤引退，\x01",
            "之后好像转职当设计技师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        (
            "#1006F哦～这样啊。\x02\x03",

            "#1001F嗯～等他们回来之后\x01",
            "真想见见两人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xB,
        (
            "#061F嗯，我也想介绍给姐姐认识，\x01",
            "等他们回来以后记得来玩哦⊙\x02\x03",

            "#560F啊，当然\x01",
            "阿加特哥哥也是哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #398
        0x8,
        (
            "#055F#6P啊？\x02\x03",

            "慢着，为什么我！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xB,
        (
            "#061F因为阿加特哥哥\x01",
            "和爷爷关系很好……\x02\x03",

            "而且我写了很多阿加特哥哥\x01",
            "的事，他们回信说\x01",
            "很想见你一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x8,
        "#552F#6P……真的假的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        (
            "#1006F啊哈哈，这就叫做\x01",
            "年终算总帐吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xB,
        "#063F那个，不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x8,
        (
            "#555F#6P不……\x01",
            "也没什么不好的……\x02\x03",

            "#551F算了，要是去蔡斯工作的话，\x01",
            "我就去顺便打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xB,
        "#061F嘿嘿，是吗⊙\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x1603)
    EventEnd(0x0)
    Return()

    # Function_50_74A0 end

    def Function_51_7CDB(): pass

    label("Function_51_7CDB")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xB, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #405
        0xB,
        (
            "#560F对了姐姐。\x02\x03",

            "你知道这甲板上的风\x01",
            "为什么会这么平静吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        (
            "#1004F因为风本来就很平静……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0xB,
        (
            "#060F不是。\x01",
            "其实这个速度和高度\x01",
            "应该会引起很大的风的。\x02\x03",

            "不要说聊天了,\x01",
            "连站都会站不稳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x101,
        "#1015F是、是这样啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #409
        0x8,
        (
            "#052F#6P也就是说，有什么装置\x01",
            "可以克服这一点对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xB,
        (
            "#560F是的，这就是让飞船浮上天空的\x01",
            "『飞翔引擎』它另外的作用。\x02\x03",

            "#061F这个机关运转的时候，\x01",
            "反重力的力场\x01",
            "会覆盖整条船……\x02\x03",

            "据说这个力场同时也会\x01",
            "缓和风与惯性的影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        "#1019F（……阿加特，你懂吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        "#552F#6P（懂才有鬼……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xB,
        (
            "#060F不过，要启动飞翔引擎\x01",
            "需要大量的导力……\x02\x03",

            "为此就需要\x01",
            "高输出功率的『导力引擎』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x101,
        (
            "#1006F原来如此……\x02\x03",

            "决定飞船性能的就是引擎，\x01",
            "原来指的是这个意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x8,
        (
            "#051F#6P这么说来，王室的船上搭载的\x01",
            "新型引擎好像完成了。\x02\x03",

            "性能似乎相当厉害吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xB,
        (
            "#061F是的，我看了性能表，\x01",
            "感觉和以前真的有天壤之别。\x02\x03",

            "我想这都是多亏了开发小组和\x01",
            "维修班各位的努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        "#1016F呵呵，感觉真是辛苦了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x1604)
    EventEnd(0x0)
    Return()

    # Function_51_7CDB end

    def Function_52_814E(): pass

    label("Function_52_814E")

    EventBegin(0x0)
    OP_20(0x3E8)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 42)
    SetChrSubChip(0xA, 0)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #418
        0xA,
        (
            "#031F呀，艾丝蒂尔。\x02\x03",

            "欢迎来到我奥利维尔·朗海姆的\x01",
            "独奏会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x101,
        (
            "#1007F你在装模作样些什么。\x02\x03",

            "#1019F话说回来在这种地方\x01",
            "弹奏乐器没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        (
            "#035F呼……\x01",
            "这真是愚蠢的问题。\x02\x03",

            "就像游击士以保护人民，\x01",
            "军人以保护国家为己任一样……\x02\x03",

            "像我这样的艺术家\x01",
            "则是以将涌现而出的激情\x01",
            "当场化为有形之物为己任的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x9,
        (
            "#020F#6P好歹也算是笼络了\x01",
            "客室乘务员之后取得许得的。\x02\x03",

            "请随意弹奏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xA,
        (
            "#036F哎哎，雪拉！\x01",
            "你真是冷淡啊。\x02\x03",

            "#034F难得约你去温泉旅行\x01",
            "却一口回绝……\x02\x03",

            "我为了你，早已有\x01",
            "沉醉不醒的觉悟了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(    #423
        0x9,
        (
            "#021F#6P嗯，要是有空的话\x01",
            "倒也可以考虑考虑。\x02\x03",

            "#027F不说这个，喝到\x01",
            "醉倒这种话可别胡说。\x02\x03",

            "只不过希望你能和我步调一致，\x01",
            "慢慢享受酒的美味……\x02\x03",

            "#021F我的要求仅此而已㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xA,
        "#033F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        (
            "#1007F我说啊，奥利维尔。\x01",
            "雪拉姐是没什么自觉的。\x02\x03",

            "对自己酒量大成什么样子，\x01",
            "喝酒的步调多乱来是没有概念的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x9,
        (
            "#025F#6P什么啊，真失礼。\x02\x03",

            "#027F不过，要找我搭讪\x01",
            "就得有这种程度的觉悟。\x02\x03",

            "而且我的门坎\x01",
            "应该还没爱娜高呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x14, 0x0, 0x1F4, 0xFA0)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #427
        0xA,
        (
            "#036F她，她的事就不要提了……\x02\x03",

            "#034F光是想起那时候的事，\x01",
            "我现在还感到轻微地眩晕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x9,
        "#021F#6P呵呵，这也难怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        "#1016F（到底发生了什么事……）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_8C(0xA, 180, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 41)
    SetChrSubChip(0xA, 0)
    OP_4B(0xA, 255)
    OP_1D(0x49)
    OP_0D()
    OP_A2(0x1607)
    EventEnd(0x0)
    Return()

    # Function_52_814E end

    def Function_53_86AA(): pass

    label("Function_53_86AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91B9")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    OP_0D()

    ChrTalk(    #430
        0xC,
        "#572F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        "#1015F#6P……金先生？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xFE, 0)
    Sleep(75)
    SetChrSubChip(0xFE, 1)
    Sleep(300)

    ChrTalk(    #432
        0xC,
        (
            "#070F#2P哦哦，艾丝蒂尔。\x02\x03",

            "怎么了，找我有事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1016F#6P啊，不是。\x01",
            "倒没有什么事情……\x02\x03",

            "#1025F你好像在想什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xC,
        (
            "#074F#2P啊啊……\x02\x03",

            "#070F稍微想起一些往事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x101,
        (
            "#1015F#6P果然还是……\x01",
            "那个戴墨镜的男人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xC,
        (
            "#070F#2P啊啊……\x02\x03",

            "自从最后道别以来已经６年了……\x01",
            "感觉既漫长又短暂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        (
            "#1025F#6P这样啊……\x02\x03",

            "#1002F那个人，是金先生的\x01",
            "师兄吧。\x02\x03",

            "是什么类型的武术家呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xC,
        "#074F#2P这个啊……\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_AD(0x24007B, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1D(0x53)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #439
        (
            "\x07\x00#070F一言以蔽之，就是『天才』。\x02\x03",

            "压倒性的格斗感觉和反射神经。\x02\x03",

            "兼备力量与速度的肉体。\x02\x03",

            "以及爆发性的『气』的使用方法。\x02\x03",

            "无论任何一点都是出类拔萃的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #440
        (
            "\x07\x00#1007F确实，那动作太厉害了……\x02\x03",

            "单论力量和速度的话，\x01",
            "说不定还在那个洛伦斯少尉之上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #441
        (
            "\x07\x00#070F……或许是这样呢。\x02\x03",

            "#074F在道场的时候，我非常\x01",
            "向往他的强大。\x02\x03",

            "直到六年前──他对老师\x01",
            "龙牙师父出手为止。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #442
        (
            "\x07\x00#1020F！！！\x02\x03",

            "对自己的老师……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #443
        (
            "\x07\x00#070F虽说如此,\x01",
            "但那也是双方同意的比试。\x02\x03",

            "#074F师父从很久以前\x01",
            "就看穿了他心底的黑暗。\x02\x03",

            "沉醉于自己压倒性的实力\x01",
            "而贪图追求更高的力量……\x02\x03",

            "在训诫这种危险的同时，\x01",
            "也藉此来说明武术之心。\x02\x03",

            "#070F通过战斗来提高自己的精神境界，\x01",
            "这才是泰斗流『活人拳』的精神。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #444
        (
            "\x07\x00#1006F『活人拳』……\x01",
            "听起来好响亮的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #445
        (
            "\x07\x00#072F然而结果，这精神\x01",
            "却没能传达给瓦鲁特。\x02\x03",

            "他就像被诱惑了一样，\x01",
            "投入了武术的黑暗面。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #446
        "\x07\x00#1004F武，武术的黑暗面……？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #447
        (
            "\x07\x00#074F就是武术作为战斗的技术时\x01",
            "绝对无法否定的一面的极端……\x02\x03",

            "将自己化为魔鬼，单纯以\x01",
            "夺取对手性命为目的的拳法。\x02\x03",

            "#072F亦即『杀人拳』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #448
        "\x07\x00#1020F啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007C, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #449
        (
            "\x07\x00#072F师父向为了追求这个\x01",
            "而意图脱离道场的他\x01",
            "进行挑战……\x02\x03",

            "决斗的结果，是丢了性命。\x02\x03",

            "#074F……我身为决斗的见证人，\x01",
            "只能眼睁睁看着它发生。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #450
        "\x07\x00#1026F……金先生…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x3E8)
    Sleep(1500)

    ChrTalk(    #451
        0xC,
        (
            "#070F#2P嗯，因为这样的事情，\x01",
            "我一直在找寻瓦鲁特\x01",
            "的踪迹。\x02\x03",

            "没想到会在这利贝尔\x01",
            "再次见到他……\x02\x03",

            "这或许也是女神的指引吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x101,
        "#1003F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xC,
        (
            "#073F#2P哦，抱歉。\x02\x03",

            "让你听了这些\x01",
            "无聊的往事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        (
            "#1007F#6P不……\x01",
            "谢谢你告诉我。\x02\x03",

            "#1002F不过，金先生……\x02\x03",

            "你寻找那个男人，\x01",
            "是为了给师父报仇吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xC,
        (
            "#070F#2P哈哈，刚才我也说了\x01",
            "那是相互同意的比试结果。\x02\x03",

            "报仇就说不过去了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x101,
        (
            "#1016F#6P是，是吗……说得也是。\x02\x03",

            "#1026F但是为什么\x01",
            "还要找他呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0xC,
        (
            "#074F#2P……啊啊……\x02\x03",

            "#572F我想确认一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x101,
        "#1015F#6P确认一件事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xC,
        (
            "#071F#2P哈哈，说出来太难为情了，\x01",
            "我看还是算了吧。\x02\x03",

            "#070F无论如何，\x01",
            "要确认这件事情\x01",
            "我还远远不够成熟……\x02\x03",

            "于是就藉由协助你\x01",
            "来努力地修行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        (
            "#1012F#6P是吗……明白了。\x02\x03",

            "#1018F我也要继续努力，\x01",
            "不能拖金先生的后腿！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xC,
        "#071F#2P哦，彼此都要努力进步啊。\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_A2(0x1609)
    EventEnd(0x0)
    SetChrSubChip(0xC, 0)
    OP_1D(0x1)
    Jump("loc_95AE")

    label("loc_91B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9350")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #462
        0x101,
        (
            "#1004F#6P啊，对了。\x02\x03",

            "#1025F那男人和金先生的关系\x01",
            "我大致明白了……\x02\x03",

            "那么雾香小姐\x01",
            "又是什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xC,
        (
            "#073F#2P啊～……\x02\x03",

            "#074F详情我无法跟你说，\x01",
            "不过可以告诉你一件事。\x02\x03",

            "雾香，是死去的\x01",
            "龙牙师父的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xC,
        (
            "#070F#2P现在你知道这个就好了。\x02\x03",

            "总有一天，或许也能从那家伙口中\x01",
            "问出些什么来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        "#1006F#6P嗯……明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x160A)
    EventEnd(0x0)
    SetChrSubChip(0xC, 0)
    Jump("loc_95AE")

    label("loc_9350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950B")
    OP_A2(0x1)
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9380")
    SetChrSubChip(0xFE, 0)
    Jump("loc_939B")

    label("loc_9380")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9396")
    SetChrSubChip(0xFE, 0)
    Jump("loc_939B")

    label("loc_9396")

    SetChrSubChip(0xFE, 1)

    label("loc_939B")

    OP_8C(0xC, 0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #467
        0xC,
        (
            "#070F那么，到了王都\x01",
            "得去大使馆露个脸才行。\x02\x03",

            "太晚过去的话\x01",
            "会被大使为难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x101,
        (
            "#1015F我记得大使是……\x01",
            "那个戴眼镜看起来很严厉的女人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xC,
        "#073F怎么，你知道啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x101,
        (
            "#1006F只是见过一次而已。\x02\x03",

            "她和帝国大使那位大叔\x01",
            "吵得很激烈呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xC,
        (
            "#075F唔，她还是那么\x01",
            "讨厌埃雷波尼亚啊。\x02\x03",

            "平时倒是给人一种相当\x01",
            "从容不迫的才女气质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        "#1011F哦，是这样啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Jump("loc_95AE")

    label("loc_950B")

    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9530")
    SetChrSubChip(0xFE, 2)
    Jump("loc_954B")

    label("loc_9530")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9546")
    SetChrSubChip(0xFE, 2)
    Jump("loc_954B")

    label("loc_9546")

    SetChrSubChip(0xFE, 1)

    label("loc_954B")

    OP_8C(0xC, 0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #473
        0xC,
        (
            "#070F那么，到了王都\x01",
            "得去大使馆露个脸才行。\x02\x03",

            "太晚过去的话\x01",
            "会被大使为难的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_95AE")

    Return()

    # Function_53_86AA end

    def Function_54_95AF(): pass

    label("Function_54_95AF")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #474
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #475
        (
            "\x07\x05本船即将\x01",
            "到达王都格兰赛尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #476
        (
            "\x07\x05着陆时会有少许摇晃，\x01",
            "请尽快回到座位上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_54_95AF end

    def Function_55_9654(): pass

    label("Function_55_9654")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_55_9654 end

    def Function_56_966B(): pass

    label("Function_56_966B")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x1)
    Return()

    # Function_56_966B end

    def Function_57_9682(): pass

    label("Function_57_9682")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
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
        (0, "loc_96FE"),
        (1, "loc_9704"),
        (SWITCH_DEFAULT, "loc_970A"),
    )


    label("loc_96FE")

    OP_A2(0x1200)
    Jump("loc_970A")

    label("loc_9704")

    OP_A2(0x1201)
    Jump("loc_970A")

    label("loc_970A")

    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_57_9682 end

    SaveToFile()

Try(main)
